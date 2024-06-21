# Working with text files, open, read, write, and close
# Note: Python provides inbuilt functions to handle text files

# Key concepts

"""
Description

Opening File: open() function: (r, w, a, r+)
Reading File: read() function ======== read lines
Writing File: write() function ======== write data
Closing File: close() function ========= close
"""

# Example: Write a file and read a file

# Writing to a text file
with open('Cyiza.txt', 'w') as file:  # 'w' opens the file in write mode
    file.write('Cyiza is a software tester who uses tor. \n')
    file.write('I use ruby though.')

# Reading from a text file
with open('Cyiza.txt', 'r') as file:  # 'r' opens the file in read mode
    content_of_the_file = file.read()
    print(content_of_the_file)

# Handling CSV files

"""
CSV (Comma Separated Values) file widely used for data exchange

Key Concepts:
Reading CSV files: Using 'csv.reader()'
Writing CSV files: Using 'csv.writer()'
DictReader and DictWriter: Classes to read and write CSV files as dictionaries
"""

# Example: Writing and reading CSV files

import csv

# Writing to a CSV file
with open('Cyamatare.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Age', 'Date'])
    writer.writerow(['Cyiza', '20', '4th June'])
    writer.writerow(['Kalala', '55', '8th August'])

# Reading from a CSV file
with open('Cyamatare.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML file processing

"""
Summary line

JSON: (JavaScript Object Notation) and XML (Extensible Markup Language) are
formats used to structure data

Key Concepts:
Loading JSON Data: Using json.load() for reading JSON files
Writing JSON Data: Using json.dump() for writing JSON files
Parsing JSON Data: Using json.loads() for handling JSON strings
"""

# Example: Writing and reading JSON files

import json

# Writing to a JSON file
student_data = {
    'name': 'Cyiza',
    'course': 'BLIS'
}

# Open the file
with open('Cyiza.json', 'w') as json_file:
    json.dump(student_data, json_file)

# Reading the JSON file
with open('Cyiza.json', 'r') as json_file:
    student_data = json.load(json_file)
    print(student_data)

# Exercise on reading and writing XML file

import xml.etree.ElementTree as ET

# Writing to an XML file
student_data = ET.Element('student')
name = ET.SubElement(student_data, 'name')
name.text = 'Cyiza'
course = ET.SubElement(student_data, 'course')
course.text = 'BLIS'

# Create a new XML file with the results
tree = ET.ElementTree(student_data)
tree.write('Cyiza.xml')

# Reading the XML file
tree = ET.parse('Cyiza.xml')
root = tree.getroot()

# Extract data from XML
name = root.find('name').text
course = root.find('course').text

print(f'Name: {name}')
print(f'Course: {course}')
