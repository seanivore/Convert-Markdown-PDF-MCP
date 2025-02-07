"""Core MCP server implementation for markdown to PDF conversion."""

from pathlib import Path
import base64
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
from pydantic import AnyUrl
from .converter import convert_markdown_to_pdf

async def serve() -> None:
    """Run the markdown to PDF MCP server."""
    
    # Define our tool
    convert_markdown_tool = types.Tool(
        name="convert_markdown",
        description="Convert markdown to PDF using VS Code styling",
        inputSchema={
            "type": "object",
            "properties": {
                "markdown": {"type": "string", "description": "Markdown content to convert"},
                "output_path": {"type": "string", "description": "Full path where to save the PDF (must end in .pdf)"},
                "theme": {"type": "string", "enum": ["light", "high-contrast"], "default": "light"}
            },
            "required": ["markdown", "output_path"]
        }
    )

    # Create server
    app = Server(
        name="md-pdf-mcp",
        version="0.1.0"
    )

    # Set up capabilities
    app.tools = [convert_markdown_tool]  # Register tool directly
    
    app.resources = {  # Register resource schemes
        "pdf": types.ResourceTemplate(
            uriTemplate="pdf://local/{path}",
            name="PDF Files",
            description="Generated PDF files",
            mimeType="application/pdf"
        ),
        "markdown": types.ResourceTemplate(
            uriTemplate="markdown://local/{path}",
            name="Markdown Files",
            description="Source markdown files",
            mimeType="text/markdown"
        )
    }
    
    app.prompts = {  # Register prompt templates
        "convert-with-style": types.Prompt(
            name="convert-with-style",
            description="Convert markdown with custom styling options",
            arguments=[
                types.PromptArgument(
                    name="theme",
                    description="PDF theme (light or high-contrast)",
                    required=False
                )
            ]
        ),
        "batch-convert": types.Prompt(
            name="batch-convert",
            description="Convert multiple markdown files to PDF",
            arguments=[
                types.PromptArgument(
                    name="directory",
                    description="Directory containing markdown files",
                    required=True
                )
            ]
        )
    }

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        return app.tools

    @app.call_tool()
    async def call_tool(
        name: str,
        arguments: dict
    ) -> list[types.TextContent]:
        if name == "convert_markdown":
            try:
                # Validate output path
                output_path = arguments["output_path"]
                if not output_path.endswith('.pdf'):
                    output_path += '.pdf'

                # Validate theme
                theme = arguments.get("theme", "light")
                if theme not in ["light", "high-contrast"]:
                    return [types.TextContent(
                        type="text",
                        text=f"Error: Invalid theme '{theme}'. Must be either 'light' or 'high-contrast'",
                        isError=True
                    )]

                # Convert markdown to PDF
                success = convert_markdown_to_pdf(
                    arguments["markdown"],
                    output_path,
                    theme
                )
                
                if success:
                    return [types.TextContent(
                        type="text",
                        text=f"Successfully converted markdown to PDF: {output_path}"
                    )]
                else:
                    return [types.TextContent(
                        type="text",
                        text="Failed to generate PDF",
                        isError=True
                    )]
            except Exception as e:
                return [types.TextContent(
                    type="text",
                    text=f"Error: {str(e)}",
                    isError=True
                )]
                
        raise ValueError(f"Tool not found: {name}")

    # Resource handlers
    @app.list_resources()
    async def list_resources() -> types.ListResourcesResult:
        # List PDF files in current directory
        resources = []
        for file in Path().glob("*.pdf"):
            resources.append(types.Resource(
                uri=f"file:///{file.absolute()}",
                name=file.name,
                mimeType="application/pdf"
            ))
        # List markdown files in current directory
        for file in Path().glob("*.md"):
            resources.append(types.Resource(
                uri=f"file:///{file.absolute()}",
                name=file.name,
                mimeType="text/markdown"
            ))
        # Return a ListResourcesResult with just the resources field
        return types.ListResourcesResult(resources=resources)

    @app.list_resource_templates()
    async def list_resource_templates() -> types.ListResourceTemplatesResult:
        templates = list(app.resources.values())
        return types.ListResourceTemplatesResult(resourceTemplates=templates)

    @app.read_resource()
    async def read_resource(uri: str) -> types.ReadResourceResult:
        # Parse the URI to get the scheme and path
        uri_str = str(uri)  # Convert AnyUrl to string
        try:
            if uri_str.startswith("pdf://local/"):
                path = Path(uri_str.replace("pdf://local/", ""))
                if not path.exists():
                    raise ValueError(f"PDF file not found: {path}")
                # Read PDF as binary and encode as base64
                contents = [types.BlobResourceContents(
                    uri=AnyUrl(uri_str),
                    blob=base64.b64encode(path.read_bytes()).decode(),
                    mimeType="application/pdf"
                )]
                return types.ReadResourceResult(contents=contents)
            elif uri_str.startswith("markdown://local/"):
                path = Path(uri_str.replace("markdown://local/", ""))
                if not path.exists():
                    raise ValueError(f"Markdown file not found: {path}")
                # Read markdown as text
                contents = [types.TextResourceContents(
                    uri=AnyUrl(uri_str),
                    text=path.read_text(encoding='utf-8'),
                    mimeType="text/markdown"
                )]
                return types.ReadResourceResult(contents=contents)
            raise ValueError(f"Unsupported resource URI scheme: {uri_str}")
        except Exception as e:
            # Return an error resource content
            contents = [types.TextResourceContents(
                uri=AnyUrl(uri_str),
                text=f"Error reading resource: {str(e)}",
                mimeType="text/plain",
                isError=True
            )]
            return types.ReadResourceResult(contents=contents)

    # Prompt handlers
    @app.list_prompts()
    async def list_prompts() -> list[types.Prompt]:
        return list(app.prompts.values())

    @app.get_prompt()
    async def get_prompt(name: str, arguments: dict) -> types.GetPromptResult:
        if name == "convert-with-style":
            theme = arguments.get("theme", "light")
            messages = [
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"Please convert this markdown file to PDF using the {theme} theme:\n\n"
                    )
                ),
                types.PromptMessage(
                    role="assistant",
                    content=types.TextContent(
                        type="text",
                        text="I'll help you convert your markdown to a beautifully styled PDF. "
                             "Would you like to proceed with the conversion?"
                    )
                )
            ]
            return types.GetPromptResult(
                messages=messages,
                description=f"Convert markdown to PDF using {theme} theme"
            )
        elif name == "batch-convert":
            directory = arguments.get("directory", ".")
            messages = [
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"Please convert all markdown files in the directory '{directory}' to PDFs:\n\n"
                    )
                ),
                types.PromptMessage(
                    role="assistant",
                    content=types.TextContent(
                        type="text",
                        text="I'll help you convert all markdown files in the specified directory to PDFs. "
                             "Would you like to proceed with the batch conversion?"
                    )
                )
            ]
            return types.GetPromptResult(
                messages=messages,
                description=f"Batch convert markdown files in {directory} to PDFs"
            )
        raise ValueError(f"Prompt not found: {name}")

    # Use stdio transport
    async with stdio_server() as streams:
        await app.run(
            streams[0],  # stdin
            streams[1],  # stdout
            app.create_initialization_options()  # Use proper initialization options
        ) 