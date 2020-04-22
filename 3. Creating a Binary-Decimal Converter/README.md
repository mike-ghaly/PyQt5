# 3 Creating a Decimal/Binary Converter

## 3.1 Design the GUI in Qt Designer

### 3.1.1 Create the MainWindow and Set its title and icon

1. You can set the window title in the Designer's **property editor**.

![set-title](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/window-title.PNG)

2. Every window should have an icon. 

![icon](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/window-icon.PNG)

You can simply google icons and choose the one you like better (just make sure it has the .ico extension).
For example, we're creating an application that will convert binary to decimal and vice versa.
It would make sense if the icon is the binary 0 and 1.
You can search for "binary" in [icon-icons.com](https://icon-icons.com/)
Find an icon you like and download it on your machine.

You can set the window icon from the **property editor** as well.

![set-icon](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/set-icon.PNG)

Then select choose from file and pick the icon you downloaded.
Now if you go to **Form** in Qt Designer's menubar, and click preview, you should see a preview of your window with the title and icon you picked.

### 3.1.2 Adding Widgets

![design](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/design.PNG)

We added a total of 7 widgets:

- 3 Labels
- 2 Line Edits
- 2 Push Buttons

Now for each of those objects we must give a descriptive, specific name in the **object inspector**.

![obj-names](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/obj-names.PNG)

________________________________________________________________________________________________________________________________

## 3.2 Generate the GUI Code

In order to generate the code: 

1. Save it gui as a .ui file. 
2. Go to the .ui file location.
3. Open your command prompt CMD at this location.
4. Run the command "pyuic5 -x XXXX.ui -o XXXX.py". (Replace XXXX with actual file names).
________________________________________________________________________________________________________________________________

## 3.3 Adding Logic

![code](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/code.PNG)

Our aim now is to link inputs to outputs.
Mainly the user will enter either a decimal or a binary value and click the corresponding button.
- When the user clicks a button.
- Get the entered number (in decimal or binary depending on the button pressed)
- Convert it
- Display it in the other line edit.

### 3.3.1 Listening for Events (Buttons Clicked)

```python
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
    
      ...
    
      # Listening for Events
      self.to_decimal_b.clicked.connect(self.to_decimal)
      self.to_binary_b.clicked.connect(self.to_binary)
```

Say we created an instance of this Ui_MainWindow class called *main_window*.
This instance will have the 7 widgets as attributes.
So
```python 
main_window.to_decimal_b
``` 
is the "to_decimal" pushbutton of this instance.

```python 
self.to_decimal_b.clicked.connect(self.to_decimal)
``` 
This line connects the push button to a method (function within the Ui_MainWindow class) called "to_decimal".
Basically we'll create 2 methods "to_decimal" and "to_binary", and connect each method to an event. 
This event is the click of the corresponding push button.


### 3.3.2 Logic

To implement the logic, we'll need to manipulate both the lineEdits widgets.
This is done by using **.text()** (which returns the text currently inside the lineEdit) and **.setText("XXX")** (which takes a string as argument and sets the text of the lineEdit to that string).
Those methods also work with labels.

Note that we've assumed that the user knows what they're doing and won't enter any garbage input. (For example, we haven't done any error checking to handle what would happen if the user entered his name instead of a decimal/binary value).

```python

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
		...

    def retranslateUi(self, MainWindow):
		...

    def to_decimal(self):

        # Get binary value from its lineEdit
        binary_value = self.binary_input.text()

        # Conversion
        decimal_value = binary_to_decimal(binary_value)

        # Display decimal value in its lineEdit
        self.decimal_input.setText(decimal_value)

    def to_binary(self):

        # Get decimal value from its lineEdit
        decimal_value = self.decimal_input.text()

        # Conversion
        binary_value = decimal_to_binary(decimal_value)

        # Display decimal value in its lineEdit
        self.binary_input.setText(binary_value)

```

The functions *binary_to_decimal()* and *decimal_to_binary()* take a value as a string for input and output the converted value as a string for output.
These 2 functions are the actual *Logic*, in the sense that they got nothing to do with GUIs. They're just functions that take a string and return another string.
So we'll implement them as functions OUTSIDE the Ui_MainWindow class.

```python
def decimal_to_binary(n):
    return bin(int(n)).replace("0b", "")


def binary_to_decimal(n):
    return str(int(n, 2))
```

_______________________________________________________________________________________________________________________________________

# Challenge 1

Finish this converter, test it and make sure that it works both ways.
It should look like this:

![converter](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/proj1.PNG)

Don't worry about the rectangular border... We'll talk about that later.

# Challenge 2

Let's make a dice!
Say we want to play shoots and ladders (Selem w Te3ban) and we lost our dice :(
Well we can make a GUI that simulates a dice. It should look like this:

![dice](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/dice.PNG)

# Challenge 3

Rock, Paper, Scissors

![rps](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/rps.PNG)

Every time the user clicks a button, the labels get updated with what each player picked and who won.
