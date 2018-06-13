# AirBnB clone - The console

### Project Description
---
The projects implements the first set of concepts in the AirBnB clone web application. We are concerned with creating our data model and then managing and storing objects via a custom-built command line interpreter called "console."

### Command Interpreter
---

#### Installation
```
git clone https://github.com/jasonmichaelhancock/AirBnB_clone.git
cd AirBnB_clone
```
#### Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$
```

Non-Interactive Mode
```
echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
$
```

#### Commands
| Command | Syntax | Summary |
| --- | --- | --- |
| all | `all <class>` | displays all objects in storage, or in specified class |
| create | `create <class>` | creates new instance of specified Class |
| destroy | `destroy <class> <id>` | deletes specified instance |
| show | `show <class> <id>` | displays instance of specified class with all attributes | 
| update | `update <class> <id> <attribute> <attribute_value>` | updates instance attribute |
| help | `help` | displays available commands |
| EOF | `EOF` | exits console |
| quit | `quit` | exits console |

### Authors
---

* [**Alex Allen**](https://github.com/sanjurosaves)
* [**Jason Hancock**](https://github.com/jasonmichaelhancock)

<br><br>
<p align="center">

<a href="https://www.holbertonschool.com"><img src="https://intranet.hbtn.io/assets/holberton-logo-simplified-d4e8a1e8bf5ad93c8c3ce32895b4b53749b477b7ba7342d7f064e6883bcd3be2.png"></a>

</p>