File Handling in Python
Overview
This project demonstrates various ways to work with files in Python, including reading, writing, appending, and managing file operations.

Features
Reading a File: Opens an existing file and prints its content.

Writing to a File: Clears existing content and writes new data.

Appending to a File: Adds new content without erasing existing data.

Reading & Writing: Allows both reading and updating a file.

Usage
1️⃣ Reading a File
python
file1 = open('my_file.txt', 'r')  
reading_file = file1.read()  
print(reading_file)  
file1.close()
Opens my_file.txt in read mode and prints its contents.

2️⃣ Writing to a File
python
file1 = open('my_file.txt', 'w')  
file1.write('Hey')  
file1.close()
Warning: This will erase existing content and add "Hey".

3️⃣ Appending to a File
python
file1 = open('my_file.txt', 'a')  
file1.write('\nAhoy There welcome')  
file1.close()
Adds new content without removing previous data.

4️⃣ Read & Write Mode
python
file1 = open('my_file.txt', 'r+')  
file1.write('Welcome here')  
file1.close()
Reads and writes data in the same file.

Prerequisites
Python installed

A text file named my_file.txt in the working directory

How to Run
Save the script in a .py file.

Ensure my_file.txt exists.

Run the script using:

python filename.py
Notes
Always close the file after reading/writing.

Using with open() automatically manages closing.

Writing mode ('w') will erase content before writing.
