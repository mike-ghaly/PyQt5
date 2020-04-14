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
![Blank Window](https://github.com/Michael-M-Mike/PyQt5/blank-window.png)


