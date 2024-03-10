## Project Overview

The aim of the AirBnB clone project is to deploy a simplified version of the AirBnB website on your server. This involves developing a comprehensive web application over a four-month period, comprising various components:

1. A command interpreter for manipulating data without a visual interface.
2. A website showcasing the final product to users, featuring both static and dynamic elements.
3. A storage system, either a database or files, for storing data.
4. An API serving as a communication interface between the front-end and your data.

### Console Functionality

The primary objective initially is to manipulate a robust storage system. This storage engine provides an abstraction layer between "My object" and "How they are stored and persisted". Consequently, you can build your console code, front-end, and RestAPI without worrying about the storage details. Moreover, this abstraction enables easy changes in storage type without the need to update the entire codebase. The console serves as a tool to validate this storage engine.

### Command Interpreter Description

The command interpreter is tailored to a specific use case, as it manages the objects of the project. Its functionalities include:
- Creating a new object.
- Retrieving an object from a file or database.
- Performing operations on objects.
- Updating attributes of an object.
- Deleting an object.

**How to Start & Use:**
To begin the command line interpreter, execute `./console.py`. The console can create, destroy, and update objects. Type `help` within the console to access a list of available commands and their functions.

**Examples:**
- Interactive Mode:
```bash
$ ./console.py
( hbnb ) help

Documented commands (type help <topic>):
========================================
EOF   help   quit

( hbnb )
( hbnb )
( hbnb ) quit
$
```
- Non-Interactive Mode:
```bash
$ echo "help" | ./console.py
( hbnb )

Documented commands ( type help <topic>):
=========================================
EOF  help  quit
( hbnb )
$
$ cat test_help
help
$
$ cat test_help | ./console.py
( hbnb )

Documented commands ( type help <topic>):
=========================================
EOF  help  quit
( hbnb )
$
```

All tests should pass in non-interactive mode as well: `$ echo "python3 -m unittest discover tests" | bash`
