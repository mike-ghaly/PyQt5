# 2. Using the Designer

- Qt Designer will make your life easier in that you won't have to write the GUI code we've previoulsy seen.
- It'll let you design the GUI and the code will be auto-generated for you.
- You'll only need to write the logic and functionlity of the GUI.

## Welcome Screen

When you first open Qt Designer, you'll be greeted with this screen.

![Designer-welcome-screen](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/designer-welcome.PNG)

Usually we'll use the designer to create a window of the GUI, so pick Main Window and press create.

## Object Inspector

All Elements of our GUI (labels, buttons, bars, menus, etc.) are widget objects provided by the PyQt5 library.
In the **Object Inspector** we can see all the objects that are part of our GUI.

![Designer-obj-inspec](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/designer-object-inspector.PNG)

As you can see, every object has a **name** and a **class**.
Those classes are already provided by PyQt5, we simply make instances of the classes we want in our GUI and give them names.

### Example
If we want to add 2 pushbuttons to our window, we'd create 2 instances of the QPushButton class provided by PyQt5.
Then we'd name them pb_1 and pb_2.

When we drag and drop the widgets we want, Qt Designer gives them object names by default. However, we should always rename them to something more descriptive and specific to our application.

| Object        | Description                                                                     |
|---------------|---------------------------------------------------------------------------------|
| MainWindow    | The window itself (What we created before)                                      |
| centralwidget | This is a container widget that contains all our other widgets and GUI elements |
| menubar       | ![menubar](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/menubar.PNG) |
| statusbar     | ![statusbar](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/statusbar.PNG) |                                                              
## Property Editor
Every object in our GUI has some properties. This is how we can truly customize widgets to our liking.

![Designer-property-editor](https://github.com/Michael-M-Mike/PyQt5/blob/master/img/designer-property-editor.PNG)

To change the properties of an object, first, select it from the **object inspector** and select the property you want to change in the **property editor** and just give the value you want.

### Example
- *QMainWindow*       
This is the object we created previously. It's a window object that has a title property.
It also has many other properties that we can configure.
_________________________________________________________________________________________________________________________
