---
title: Debugging
description: A comprehensive guide to debugging Model Context Protocol (MCP) integrations
---

Effective debugging is essential when developing MCP servers or integrating them with applications. This guide covers the debugging tools and approaches available in the MCP ecosystem.

<Info>
  This guide is for macOS. Guides for other platforms are coming soon.
</Info>

## Debugging tools overview

MCP provides several tools for debugging at different levels:

1. **MCP Inspector**
   - Interactive debugging interface
   - Direct server testing
   - See the [Inspector guide](/docs/tools/inspector) for details

2. **Claude Desktop Developer Tools**
   - Integration testing
   - Log collection
   - Chrome DevTools integration

3. **Server Logging**
   - Custom logging implementations
   - Error tracking
   - Performance monitoring

## Debugging in Claude Desktop

### Checking server status

The Claude.app interface provides basic server status information:

1. Click the <img src="/images/claude-desktop-mcp-plug-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> icon to view:
   - Connected servers
   - Available prompts and resources

2. Click the <img src="/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> icon to view:
   - Tools made available to the model

### Viewing logs

Review detailed MCP logs from Claude Desktop:

```bash
# Follow logs in real-time
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
```

The logs capture:
- Server connection events
- Configuration issues
- Runtime errors
- Message exchanges

### Using Chrome DevTools

Access Chrome's developer tools inside Claude Desktop to investigate client-side errors:

1. Create a `developer_settings.json` file with `allowDevTools` set to true:

```bash
echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json
```

2. Open DevTools: `Command-Option-Shift-i`

Note: You'll see two DevTools windows:
- Main content window
- App title bar window

Use the Console panel to inspect client-side errors.

Use the Network panel to inspect:
- Message payloads
- Connection timing

## Common issues

### Working directory

When using MCP servers with Claude Desktop:

- The working directory for servers launched via `claude_desktop_config.json` may be undefined (like `/` on macOS) since Claude Desktop could be started from anywhere
- Always use absolute paths in your configuration and `.env` files to ensure reliable operation
- For testing servers directly via command line, the working directory will be where you run the command

For example in `claude_desktop_config.json`, use:
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/data"]
}
```
Instead of relative paths like `./data`

### Environment variables

MCP servers inherit only a subset of environment variables automatically, like `USER`, `HOME`, and `PATH`.

To override the default variables or provide your own, you can specify an `env` key in `claude_desktop_config.json`:

```json
{
  "myserver": {
    "command": "mcp-server-myapp",
    "env": {
      "MYAPP_API_KEY": "some_key",
    }
  }
}
```

### Server initialization

Common initialization problems:

1. **Path Issues**
   - Incorrect server executable path
   - Missing required files
   - Permission problems
   - Try using an absolute path for `command`

2. **Configuration Errors**
   - Invalid JSON syntax
   - Missing required fields
   - Type mismatches

3. **Environment Problems**
   - Missing environment variables
   - Incorrect variable values
   - Permission restrictions

### Connection problems

When servers fail to connect:

1. Check Claude Desktop logs
2. Verify server process is running
3. Test standalone with [Inspector](/docs/tools/inspector)
4. Verify protocol compatibility

## Implementing logging

### Server-side logging

When building a server that uses the local stdio [transport](/docs/concepts/transports), all messages logged to stderr (standard error) will be captured by the host application (e.g., Claude Desktop) automatically.

<Warning>
  Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation.
</Warning>

For all [transports](/docs/concepts/transports), you can also provide logging to the client by sending a log message notification:

<Tabs>
  <Tab title="Python">
    ```python
    server.request_context.session.send_log_message(
      level="info",
      data="Server started successfully",
    )
    ```
  </Tab>
  <Tab title="TypeScript">
    ```typescript
    server.sendLoggingMessage({
      level: "info",
      data: "Server started successfully",
    });
    ```
  </Tab>
</Tabs>

Important events to log:
- Initialization steps
- Resource access
- Tool execution
- Error conditions
- Performance metrics

### Client-side logging

In client applications:

1. Enable debug logging
2. Monitor network traffic
3. Track message exchanges
4. Record error states

## Debugging workflow

### Development cycle

1. Initial Development
   - Use [Inspector](/docs/tools/inspector) for basic testing
   - Implement core functionality
   - Add logging points

2. Integration Testing
   - Test in Claude Desktop
   - Monitor logs
   - Check error handling

### Testing changes

To test changes efficiently:

- **Configuration changes**: Restart Claude Desktop
- **Server code changes**: Use Command-R to reload
- **Quick iteration**: Use [Inspector](/docs/tools/inspector) during development

## Best practices

### Logging strategy

1. **Structured Logging**
   - Use consistent formats
   - Include context
   - Add timestamps
   - Track request IDs

2. **Error Handling**
   - Log stack traces
   - Include error context
   - Track error patterns
   - Monitor recovery

3. **Performance Tracking**
   - Log operation timing
   - Monitor resource usage
   - Track message sizes
   - Measure latency

### Security considerations

When debugging:

1. **Sensitive Data**
   - Sanitize logs
   - Protect credentials
   - Mask personal information

2. **Access Control**
   - Verify permissions
   - Check authentication
   - Monitor access patterns

## Getting help

When encountering issues:

1. **First Steps**
   - Check server logs
   - Test with [Inspector](/docs/tools/inspector)
   - Review configuration
   - Verify environment

2. **Support Channels**
   - GitHub issues
   - GitHub discussions

3. **Providing Information**
   - Log excerpts
   - Configuration files
   - Steps to reproduce
   - Environment details

## Next steps

<CardGroup cols={2}>
  <Card
    title="MCP Inspector"
    icon="magnifying-glass"
    href="/docs/tools/inspector"
  >
    Learn to use the MCP Inspector
  </Card>
</CardGroup>


---
title: Inspector
description: In-depth guide to using the MCP Inspector for testing and debugging Model Context Protocol servers
---

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](/docs/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector's features and capabilities.

## Getting started

### Installation and basic usage

The Inspector runs directly through `npx` without requiring installation:


```bash
npx @modelcontextprotocol/inspector <command>
```

```bash
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### Inspecting servers from NPM or PyPi

A common way to start server packages from [NPM](https://npmjs.com) or [PyPi](https://pypi.com).

<Tabs>

  <Tab title="NPM package">
  ```bash
  npx -y @modelcontextprotocol/inspector npx <package-name> <args>
  # For example
  npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb
  ```
  </Tab>

  <Tab title="PyPi package">
  ```bash
  npx @modelcontextprotocol/inspector uvx <package-name> <args>
  # For example
  npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
  ```
  </Tab>
</Tabs>

#### Inspecting locally developed servers

To inspect servers locally developed or downloaded as a repository, the most common
way is:

<Tabs>
  <Tab title="TypeScript">
  ```bash
  npx @modelcontextprotocol/inspector node path/to/server/index.js args...
  ```
  </Tab>
  <Tab title="Python">
  ```bash
  npx @modelcontextprotocol/inspector \
    uv \
    --directory path/to/server \
    run \
    package-name \
    args...
  ```
  </Tab>
</Tabs>

Please carefully read any attached README for the most accurate instructions.

## Feature overview

<Frame caption="The MCP Inspector interface">
  <img src="/images/mcp-inspector.png" />
</Frame>

The Inspector provides several features for interacting with your MCP server:

### Server connection pane
- Allows selecting the [transport](/docs/concepts/transports) for connecting to the server
- For local servers, supports customizing the command-line arguments and environment

### Resources tab
- Lists all available resources
- Shows resource metadata (MIME types, descriptions)
- Allows resource content inspection
- Supports subscription testing

### Prompts tab
- Displays available prompt templates
- Shows prompt arguments and descriptions
- Enables prompt testing with custom arguments
- Previews generated messages

### Tools tab
- Lists available tools
- Shows tool schemas and descriptions
- Enables tool testing with custom inputs
- Displays tool execution results

### Notifications pane
- Presents all logs recorded from the server
- Shows notifications received from the server

## Best practices

### Development workflow

1. Start Development
   - Launch Inspector with your server
   - Verify basic connectivity
   - Check capability negotiation

2. Iterative testing
   - Make server changes
   - Rebuild the server
   - Reconnect the Inspector
   - Test affected features
   - Monitor messages

3. Test edge cases
   - Invalid inputs
   - Missing prompt arguments
   - Concurrent operations
   - Verify error handling and error responses

## Next steps

<CardGroup cols={2}>
    <Card
        title="Inspector Repository"
        icon="github"
        href="https://github.com/modelcontextprotocol/inspector"
    >
        Check out the MCP Inspector source code
    </Card>

    <Card
        title="Debugging Guide"
        icon="bug"
        href="/docs/tools/debugging"
    >
        Learn about broader debugging strategies
    </Card>
</CardGroup>
