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

Example:

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

**1. Run inline**

The Python code will be saved in the environment variable $PYCODE

Example:

	guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
	guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
	Best School: 98
	guillaume@ubuntu:~/py/0x00$ 

Repo:

- GitHub repository: [alx-higher_level_programming](../)
- Directory: [0x00-python-hello_world](./)
- File: [1-run_inline](./1-run_inline)

**2. Hello, print**

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

- Use the function print

Example:

	guillaume@ubuntu:~/py/0x00$ ./2-print.py 
	"Programming is like building a multilingual puzzle
	guillaume@ubuntu:~/py/0x00$

Repo:

- GitHub repository: [alx-higher_level_programming](../)
- Directory: [0x00-python-hello_world](./)
- File: [2-print.py](./2-print.py)

**3. Print integer**

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code here
- The output of the script should be:
	- the number, followed by Battery street,
	- followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips

Example:

	guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
	98 Battery street
	guillaume@ubuntu:~/py/0x00$ 

Repo:

- GitHub repository: [alx-higher_level_programming](../)
- Directory: [0x00-python-hello_world](./)
- File: [3-print_number.py](./3-print_number.py)

**4. Print float**

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

- You can find the source code here
- The output of the program should be:
	- Float:, followed by the float with only 2 digits
	- followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings

Example:

	guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
	Float: 3.14
	guillaume@ubuntu:~/py/0x00$ 

Repo:

- GitHub repository: [alx-higher_level_programming](../)
- Directory: [0x00-python-hello_world](./)
- File: [4-print_float.py](./4-print_float.py)

**5. Print string**

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

- You can find the source code here
- The output of the program should be:
	- 3 times the value of str
	- followed by a new line
	- followed by the 9 first characters of str
	- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

Example:

	guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
	Holberton SchoolHolberton SchoolHolberton School
	Holberton
	guillaume@ubuntu:~/py/0x00$ 

Repo:

- GitHub repository: [alx-higher_level_programming](../)
- Directory: [0x00-python-hello_world](./)
- File: [5-print_string.py](./5-print_string.py)
