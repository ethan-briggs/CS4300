CS4300 - Homework 1
This project contains solutions for Homework 1.

Project Structure
cs4300/
└── homework1/
    ├── src/
    │   ├── task1.py
    │   ├── task2.py
    │   ├── task3.py
    │   ├── task4.py
    │     ├── task5.py
    │   ├── task6.py
    │   └── task7.py
    ├── tests/
    │   ├── test_task1.py
    │   ├── test_task2.py
    │   ├── test_task3.py
    │   ├── test_task4.py
    │   ├── test_task5.py
    │   ├── test_task6.py
    │   └── test_task7.py
    ├── task6_read_me.txt
    ├── pyproject.toml
    └── README.md (this file)

Prerequisites
Python 3
Virtual environment (venv)
pytest testing framework
requests

Setup Instructions

Create and activate virtual environment:
python3 -m venv hw1_env --system-site-packages
source hw1_env/bin/activate

Install dependencies:
python3 -m pip install pytest requests

Running the Tests
1. Open terminal
2. Make sure you are in /home/student/CS4300/homework1
3. Type "pytest tests"
4. Ensure output has no errors and tests succeed

Task Overview
Task 1: Introduction to Python and Testing
Basic "Hello, World!" program
Simple pytest verification

Task 2: Variables and Data Types
Demonstrates integers, floats, strings, and booleans
type testing

Task 3: Control Structures
If/else statements for number classification
For loop for prime number generation
While loop for summation

Task 4: Functions and Duck Typing
calculate_discount function with duck typing
Supports various numeric types

Task 5: Lists and Dictionaries
Book list manipulation with slicing
Student database dictionary operations

Task 6: File Handling
Word count implementation for text files

File I/O operations

Task 7: Package Management
requests demo

To deactivate the virtual environment:
deactivate

Dependencies
pytest: Testing framework
requests