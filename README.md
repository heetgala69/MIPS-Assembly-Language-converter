# MIPS-Assembly-Language-converter
Made a python script to convert .asm file to its respective hex code trying to replicate qt spim.

# Abstract
The goal of this project is to create a basic MIPS assembler. An asm file with the extension input.asm serves as the input to the assembler, which is called MyAssembler in the python file. Another text file with the name output.txt contains the assembler's output. The Python file will be called MyAssembler, and Python will be able to run the file from the console as soon as an asm file from the same folder as the Python file is written in is called from the console. When the programme is launched, the compiler will attempt to read file name.asm and generate output.txt as output because it is located in the same folder as a Python file. For testing purposes, the file name "input" was utilised. If an instruction is invalid, the program's output will state invalid instruction.

# Project Design
The project is made up of various functions that are called from various Python files:
The assemblytohex function in the main file, myAssembler, calls other functions from other Python files, including removing from removing.py, instruct name from i n.py, and binary2hex from bth.py. The main file also accepts input from the file file name.asm, which contains the user-inputted file name and the python filr that needs to be constructed, and output2.txt is where the output is written.
Labels and comments are removed from the asm file using the removing function from removing.py.
To identify and categorise the instructions based on their forms, the i n.py function instruct name is utilised. The function that determines the instruction format for the instruction name is then called from the file i f.py. This file will call a function that will convert any given instruction name, register name, shamt name, or immediate name to the corresponding binary format. It will also call a function that will retrieve the corresponding opcode and function. If a register name rather than a number is given in the instruction, the function todec from the todecimal.py package is used to translate the register name to the appropriate number.
If the given number is negative, function two from the tocomplement.py file is used to translate it to its binary 2's complement counterpart. To convert decimal to its binary equivalent, use the tobinary function in tobinary.py.
The functions in file i f.py concatenate the binary values for all required variables, format them correctly, and return them to file i n.py, which then returns the binary value of the instruction to the main file myAssembler.py.
The function binary2hex from bth.py is then used to convert this binary equivalent to hex, returning the value to the variable ans from whence the function assemblytohex was originally called. Finally, the output2.txt file contains the returned value.

# Flowchart
<img width="916" alt="Screenshot 2023-10-13 at 12 41 48 PM" src="https://github.com/heetgala69/MIPS-Assembly-Language-converter/assets/115033167/47a7ac6e-b3b2-4635-b8be-dc12b9e53773">


