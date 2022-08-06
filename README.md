# HackBackpackers_ShubhamSrivastava

**Problem Statement 1 - Lineage problem statement**
# Description
I have used Python's inbuilt package "sql-metadata-lineage" from PyPi which automatically generates the lineage
information. It has an inbuilt function "get_metadata" which takes "sql query" as an input. And returns two outputs:
table_map and column_map.

These two variables hold the table lineage and column linage respectively.

This python file has one example test also towards the end and two print statements to display the table 
and column lineage.

# Prerequisite
pip install sql-metadata-lineage


# How to run
Steps
1. No specific requirements. Simply execute the attached python file on Jupyter Notebook.

**Problem Statement 2 - Functions problem statement**
# Description
I have researched and written all possible corrosponding Azure Data Factory function for each of the IBM Data Stage 
function. I could not install or run my scripts on ADF. 
For each of the function type, I have created a folder and for each of the function I have created a python file.
You may pleasse open and view the specific code of each file and execute it in your environment.
These Python wrapper functions internally uses only ADF inbuilt function. There is no inbuilt Python function
used or any Python library/package installed.
Appropriate comments have also been added.
I am not using any "try {} except {}" block as they are an inbuilt Python objects / syntax. Hence the assumption
is correct data type inputs are given.

# Prerequisite
Nothing

# How to run
Steps
1. No specific requirements. Simply execute the attached python file on your environment.

**Problem Statement 3 - XML problem statement**
# Description
I have used "xml.etree.ElementTree" Python inbuilt method to parse the XML. I then first get the "root" element
of the XML and then try to access "TRANSFORMFIELD" element of it. 
The idea was this element does contain an "EXPRESSION" attribute which is doing some transformations.
There are some self-explanatory text transformation which I have done to parse and get the source , transformation and target
values.
On similar idea I am also parsing "CONNECTORFIELD" object as it also stores some related transformations.
There are two seperate functions to do the above etwo parsing and are called one after another. They have print() 
statement towards their end which is printing the output in particular format.

# Prerequisite
install xml.etree package in case it's not available.

# How to run
Steps
1.Just copy paste and run the python file on your Jupyter notebook.
2.Make sure to keep the "xml" file in the same directory as your code.
