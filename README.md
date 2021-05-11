# Musical Operations Project

The goal of the Musical Operations Project is to create a series of functions in Python that perform common tasks in beginner music theory and musical set theory. The musical set theory concepts used in this project can be found in [a Sideways video called "The Clock Diagram"](https://youtu.be/oGeBem72R3Y).

In this repository, the Note.py file is a Note object/class, the basis for the rest of the musical operations. All of the other Python files define functions that interact with a Note object or a group of Note objects in a Python list.

In the Documentation.md file, I will provide a brief overview of the Note object, all of the functions, and their uses.

## Prerequisities

This project was developed using **Python version 3.8.5**.

## Setup

To use the Note object class and all the functions in this project, there are several lines of code that must be executed.

If code will be written and run in a Python driver file, make sure that the driver file is at the same file level as Note.py. If code will be run using the Python interpreter, make sure that the terminal/command prompt is on the same file level as Note.py.

Next, run the following commands in the Python interpreter, or place the following lines of code at the top of the driver file.

```python
from Note import *

from functions.ChordRecognition import *
from functions.OrderNotes import *
from functions.IntervalRecognition import *
from functions.MusicalSetTheory import *
```

These lines of code will allow a user to run all the functions in the project either through the Python interpreter or through the driver file. In this repository, there is a file named TestDriver.py, which is an example of a driver file for this project that executes a few of the functions in the project.
