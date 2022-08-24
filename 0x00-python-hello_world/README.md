# 0x00. Python - Hello, World

## Resources

**Read or watch:**

- [The python tutorial (only the first three chapters below)](https://docs.python.org/3/tutorial/index.html)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python (Read up until “3.1.2. Strings” included)](https://docs.python.org/3/tutorial/introduction.html)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives

### General

- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Shell Scripts

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable

### C Scripts

- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded

### Quiz questions

**Question #0**
Who created Python?

- [ ] Julien Barbier
- [ ] Yukihiro Matsumoto
- [X] Guido van Rossum

**Question #1**
What does this command line print?

	>>> print("Holberton school")

- [ ] Holberton
- [ ] “Holberton school”
- [X] Holberton school
- [ ] ‘Holberton school’

**Question #2**
What does this command line print?

	>>> print(f"{98} Battery street")

- [X] 98 Battery street
- [ ] f"98 Battery street"
- [ ] 9 Battery street
- [ ] 8 Battery street

**Question #3**
What does this command line print?

	>>> print(f"{98} Battery street, {'San Francisco'}")

- [ ] “98 Battery street, San Francisco”
- [ ] 8 Battery street, San
- [X] 98 Battery street, San Francisco
- [ ] San Francisco Battery street, 98

**Question #4**
What does this command line print?

	>>> a = "Python is cool"
	>>> print(a[4])

- [ ] P
- [ ] n
- [X] o
- [ ] h

**Question #5**
What does this command line print?

	>>> a = "Python is cool"
	>>> print(a[0:6])

- [X] Python
- [ ] Pytho
- [ ] Python is
- [ ] Python is cool

**Question #6**
What does this command line print?

	>>> a = "Python is cool"
	>>> print(a[:6])

- [ ] Pytho
- [X] Python
- [ ] Python is
- [ ] is cool

**Question #7**
What does this command line print?

	>>> a = "Python is cool"
	>>> print(a[7:])

- [ ] Python i
- [ ] Python is
- [ ] cool
- [X] is cool

**Question #8**
What does this command line print?

	>>> a = "Python is cool"
	>>> print(a[7:-5])

- [ ] on
- [ ] nohtyP
- [ ] Python
- [ ] si
- [X] is

**Question #9**
What does this command line print?

	>>> a = "Python is cool"
	>>> print(a[-2])

- [ ] ol
- [ ] l
- [X] o
- [ ] Nothing

## Tasks

**0. Run Python file**

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

	guillaume@ubuntu:~/py/0x00$ cat main.py 
	#!/usr/bin/python3
	print("Best School")

	guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
	guillaume@ubuntu:~/py/0x00$ ./0-run
	Best School
	guillaume@ubuntu:~/py/0x00$
	
Repo:

- GitHub repository: [alx-higher_level_programming](../)
- Directory: [0x00-python-hello_world](./)
- File: [0-run](./0-run)
