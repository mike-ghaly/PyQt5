# Layouts

When we create a GUI, we want it to be **resizeable** and look the same on all screens and resolutions.

For example, the *decimal/binary coverter* we made previously, looked like this:

![layouts1](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts1.PNG)

However, if we resize the window and make it larger, our GUI elements will ocupy the same space anyway and won't resize to fill the window.

![layouts2](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts2.PNG)

Same thing will happen if we make the window smaller.

![layouts3](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts3.PNG)

This is because so far we've been using **absolute positiong**, which means that we specified the position and the size of each widget and no matter how much the window is resized, our widgets will always be at the same position and have the same size.

As we've already seen, this may have a few issues:
- The size and the position of a widget do not change if we resize a window
- Applications might look different on various screens/platforms
- Making small changes to our design (like changing labels' font) may mess up the entire design

Instead what we want is for our widgets to automatically change size to have the look we want regardless of the window's size or platform.

![layouts4](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts4.PNG)
![layouts5](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts5.PNG)
![layouts6](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts6.PNG)

This is done by using **layouts**.

There are 4 types of layouts:

# Vertical Layout

![layoutsv](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts-v.PNG)

# Horizontal Layout

![layoutsh](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts-h.PNG)

# Form Layout

![layoutsf](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/layouts-f.PNG)

# Grid Layout

No need to show it. Our next project will be one big grid :)
