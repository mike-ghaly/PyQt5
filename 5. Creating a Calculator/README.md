# Making a Calculator

## Create the Design Using Layouts

We want to design a calculator app similar to the one that comes with Window 10.
As you can see, it has 2 main compenents:
- A display
- A grid of pushbuttons

![calc10](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc10.PNG)


## Buttons Grid Layout

First go ahead and drag the push buttons as shown:

![calc-1](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-1.PNG)

Then we want to put them in a grid layout. This can be done in 2 ways: 

1. Select the pushbuttons and press on the grid layout in the toolbar.
2. Select the pushbuttons, right click and pick the grid layout.

![calc-2](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-2.PNG)

Once you do this. You'll see in the object inspector that now all these pushbuttons are part of a grid layout.

![calc-4](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-4.PNG)
![calc-3](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-3.PNG)

Now go ahead and modify the pushbuttons so your design looks like this:

![calc-5](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-5.PNG)

Notice that if you resize the grid itself and make it larger, the pushbuttons will change size and fill the grid horizontally but not vertically.

![calc-6](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-6.PNG)

To fix this, we have to change the **size policy**, which simply tells our widgets if they should change size vertically, horizontally or both.

![calc-8](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-8.PNG)

Now you should have something like this:

![calc-7](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-7.PNG)

## Stylesheets

Time to make our GUIs slightly less ugly using stylesheets! 
Stylesheets are a way for us to define the visual style of our GUI (fonts, colors, etc.) It's mainly used in web development but PyQt5 does support it.

Every GUI element can have its own stylesheet. However, stylesheets have a cascading property. So if you apply a stylesheet on the grid layout specifying its colour to be green for example, that stylesheet will cascade down to all the widgets inside the grid and all of them will become green as well. If you provide one of the pushbuttons inside the grid with its own stylesheet specifying its color to be blue, it'll become blue and all other pushbuttons will remain green.

Before dealing with stylesheets, let's remove the spacing between our buttons. Click on the grid layout and in the property editor set **layoutVerticalSpacing** and **layoutHorizontalSpacing** to 0.

Now select all the pushbuttons and, from the property editor, find the "styleSheet" property and open it.

![calc-9](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-9.PNG)

Click add font and choose "Calibri" and set the font size to 20.

For colors, there're 2 main style properties that we're going to use:
- color: which is the color of the text inside the widget.
- background-color: which is the color of the widget itself.

Choose any colors you like.

![calc-10](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-10.PNG)


## centralwidget Layout

Now for the display, we can add a label to our buttons grid. Be sure to add an appropriate stylesheet to it as well.

![calc-11](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-11.PNG)


So far however if you preview the design and try to adjust the window's size, nothing will happen and no widgets will change size. This is because what's responsible for all that is the centralwidget. You need to give it a layout as well by right clicking anywhere on your window and setting any layout.

As soon as you do this, you'll notice that the grid layout of the pushbuttons resized itself to fill the entire window.

![calc-12](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-12.PNG)

________________________________________________________________________________________________________________________________________

# Challenge 1

Finish the calculator to be like the one shown here (choose any colors, styles you want... don't make it look ugly!)


![calc-f](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/calc-f.PNG)

