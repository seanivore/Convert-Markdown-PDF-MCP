# Python 101 – How to Generate a PDF

> / intermediate, Python, ReportLab / By Mike / September 28, 2021 / 30DaysOfPython, Python, Python PDF Series, Reportlab

[https://www.blog.pythonlibrary.org/2021/09/28/python-101-how-to-generate-a-pdf/]

The Portable Document Format (PDF) is a very popular way to share documents across multiple platforms. The goal of the PDF is to create a document that will look the same on multiple platforms and that will print the same (or very similar) on various printers. The format was originally developed by Adobe but has been made open-source.

Python has multiple libraries that you can use to create new PDFs or export portions of pre-existing PDFs. There are currently no Python libraries available for editing a PDF in-place. Here are a few of the packages you can use:

ReportLab – used for creating PDFs
pdfrw – used for splitting, merging, watermarking and rotating a PDF
PyPDF2 / PyPDF4 – used for splitting, merging, watermarking and rotating a PDF
PDFMiner – used for extracting text from PDFs
There are many other PDF packages for Python. In this article, you will learn how to create a PDF using ReportLab. The ReportLab package has been around since the year 2000. It has an open-source version as well as a paid commercial version which has some extra features in it. You will be learning about the open-source version here.

In this article, you will learn about the following:

Installing ReportLab
Creating a Simple PDF with the Canvas
Creating Drawings and Adding Images Using the Canvas
Creating Multi-page Documents with PLATYPUS
Creating a Table
ReportLab can generate almost any kind of report you can imagine. This article will not cover every feature that ReportLab has to offer, but you will learn enough about it to see how useful ReportLab can be.

Let’s get started!

Installing ReportLab
You can install ReportLab using pip:

python3 -m pip install reportlab
ReportLab depends on the Pillow package, which is an image manipulation library for Python. It will be installed as well if you do not already have it on your system. Now that you have ReportLab installed, you are ready to learn how to create a simple PDF!

Creating a Simple PDF with the Canvas
There are two ways to create PDFs using the ReportLab package. The low-level method is drawing on the “canvas”. This allows you to draw at specific locations on the page. PDFs measure their size in points internally. There are 72 points per inch. A letter-size page is 612 x 792 points. However, the default page size is A4. There are several default page sizes that you can set or you can create your own page size.

It’s always easier to see some code so that you can understand how this will work. Create a new file named hello_reportlab.py and add this code:

# hello_reportlab.py
from reportlab.pdfgen import canvas
my_canvas = canvas.Canvas("hello.pdf")
my_canvas.drawString(100, 750, "Welcome to Reportlab!")
my_canvas.save()
This will create a PDF that is A4-sized. You create a Canvas() object that takes in the path to the PDF that you want to create. To add some text to the PDF, you use drawString(). This code tells ReportLab to start drawing the text 100 points from the left and 750 from the bottom of the page. If you were to start drawing at (0, 0), your text would appear at the bottom left of the page. You can change the location you start drawing by setting the bottomup canvas argument to 0.

The last line saves the PDF to disk. Don’t forget to do that or you won’t get to see your new creation!

The PDF should look something like this when you open it:

Hello World on ReportLab Canvas
Hello World on ReportLab Canvas
While this demonstrates how easy it is to create a PDF with ReportLab, it’s kind of a boring example. You can use the canvas to draw lines, shapes and different fonts too. To learn how, create a new file named canvas_form.py and enter this code in it:

# canvas_form.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
def form(path):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(30, 750, 'OFFICIAL COMMUNIQUE')
    my_canvas.drawString(30, 735, 'OF ACME INDUSTRIES')
    my_canvas.drawString(500, 750, "12/12/2010")
    my_canvas.line(480, 747, 580, 747)
    my_canvas.drawString(275, 725, 'AMOUNT OWED:')
    my_canvas.drawString(500, 725, "$1,000.00")
    my_canvas.line(378, 723, 580, 723)
    my_canvas.drawString(30, 703, 'RECEIVED BY:')
    my_canvas.line(120, 700, 580, 700)
    my_canvas.drawString(120, 703, "JOHN DOE")
    my_canvas.save()
if __name__ == '__main__':
    form('canvas_form.pdf')
Here you import the letter size from reportlab.lib.pagesizes which has several other sizes you could use. Then in the form() function, you set the pagesize when you instantiate Canvas(). Next, you use setLineWidth() to set the line width, which is used when you draw lines. Then you change the font to Helvetica with the font size at 12 points.

The rest of the code is a series of drawing strings at various locations with lines being drawn here and there. When you draw a line(), you pass in the starting coordinate (x/y positions) and the end coordinate (x/y position) and ReportLab will draw the line for you using the line width you set.

When you open the PDF, you will see the following:

A Form Created with ReportLab Canvas
A Form Created with ReportLab Canvas
That looks pretty good. But what if you wanted to draw something or add a logo or some other photo to your report? Let’s find out how to do that next!

Creating Drawings and Adding Images Using the Canvas
The ReportLab Canvas() is very flexible. It allows you to draw different shapes, use different colors, change the line widths, and more. To demonstrate some of these features, create a new file named drawing_polygons.py and add this code to it:

# drawing_polygons.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
def draw_shapes():
    my_canvas = canvas.Canvas("drawing_polygons.pdf")
    my_canvas.setStrokeColorRGB(0.2, 0.5, 0.3)
    my_canvas.rect(10, 740, 100, 80, stroke=1, fill=0)
    my_canvas.ellipse(10, 680, 100, 630, stroke=1, fill=1)
    my_canvas.wedge(10, 600, 100, 550, 45, 90, stroke=1, fill=0)
    my_canvas.circle(300, 600, 50)
    my_canvas.save()
if __name__ == '__main__':
    draw_shapes()
Here you create a Canvas() object as you have before. You can use setStrokeColorRGB() to change the border color using RGB values between zero and one. The next few lines of code create different shapes. For the rect() function, you specify the x and y start position which is the lower left-hand coordinate of the rectangle. Then you specify the width and height of the shape.

The stroke parameter tells ReportLab whether or not to draw the border while the fill parameter tells ReportLab whether or not to fill the shape with a color. All of the shapes support these two parameters.

According to the documentation for the ellipse(), it takes in the starting (x,y) and ending (x,y) coordinates for the enclosing rectangle for the ellipse shape.

The wedge() shape is similar in that you are once again specifying a series of points for an invisible rectangle that encloses the wedge shape. What you need to do is imagine that there is a circle inside of a rectangle and you are describing the size of the rectangle. The 5th argument is startAng, which is the starting angle of the wedge. The 6th argument is for the extent, which tells the wedge how far out the arc can extend.

Lastly, you create a circle(), which takes in the (x,y) coordinates of its center and then its radius. You skip setting the stroke and fill parameters.

When you run this code, you will end up with a PDF that looks like this:

Creating Polygons with ReportLab
Creating Polygons with ReportLab
