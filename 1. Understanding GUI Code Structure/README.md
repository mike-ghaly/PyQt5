# 1. Understanding GUI Code Structure with a Blank Window

```python

import sys
from PyQt5.QtWidgets import QWidget, QApplication


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Window Title Here")


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())

```

The above code example shows a small window on the screen when run.

![Blank Window](https://github.com/Michael-M-Mike/PyQt5/blob/master/blank-window.PNG)

# Stepping Through The Code

```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication
```

Here we provide the necessary imports. 

## QApplication 
- For any GUI application, there is only one QApplication object, no matter whether the application has 0, 1, 2 or more windows at any given time.
- It must be created before any other objects related to the user interface.
- It needs access to the operating system so it can initialize the GUI application with with the user’s desktop settings and give it the same look and feel of the OS *(reason we imported sys)*.
- QApplication is not something we see on screen, it's an intermediary object between the OS and your GUI.

## QWidget
- Widgets are the atoms that make your GUI. They receive mouse, keyboard and other events from the window system, and can change their appearance.
- Every widget is rectangular. 
- A widget that is not embedded in a parent widget is called a window. Usually, windows have a frame and a title bar

![Widgets](https://github.com/Michael-M-Mike/PyQt5/blob/master/widgets.PNG)

________________________________________________________________________________________________________________________________________

```python
class MainWindow(QWidget):
```

- Here we create our main window *(widgets not embedded in a parent widget are windows)* of type widget *(by inheriting QWidget)*. 
- It's a class that we can setup however we like and then simply create an instance of it be our actual main window that will contains any widgets we want.
________________________________________________________________________________________________________________________________________

```python
def __init__(self):
    QWidget.__init__(self)
    self.setWindowTitle("Window Title Here")
```

In the __init__ function, we first initialize the QWidget parent object we inherited. Then we can initialize our main window how we like. For now we'll just set its title to "Window Title Here".

________________________________________________________________________________________________________________________________________

```python
app = QApplication(sys.argv)
```

__app__ is now a QApplication object (instance of QApplication). 

________________________________________________________________________________________________________________________________________

```python
main_window = MainWindow()
main_window.show()
```

__main_window__ is now an instance of the MainWindow class we created. We then show the main window.
- The __show()__ method can be called on any widget. It displays the widget on the screen. 
- A widget is first created in memory and later shown on the screen.

________________________________________________________________________________________________________________________________________

```python
sys.exit(app.exec_())
```
Finally, we enter the mainloop of the application. The event handling starts from this point. 
This line will make __app__ wait for the **exit** event (When the X is clicked to close the window) which will end the mainloop and close the __main_window__.
________________________________________________________________________________________________________________________________________

# Challenge 1

Make a GUI that has:
- Application object called "application" and two different windows: "home_window" and "misc_window".
- The title of the "home_window" is "Home".
- The title of the "home_window" is "Miscellaneous".
- When the program runs, only the "home_window" is displayed.

















