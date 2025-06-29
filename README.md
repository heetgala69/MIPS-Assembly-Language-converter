# MIPS-Assembly-Language-converter
This repository contains all the necessary code and files to implement a basic MIPS to binary converter, developed as part of a college project at NMIMS University. The program reads MIPS assembly instructions from a file and converts each instruction into a corresponding 32-bit binary representation.

# Temp Flow of program:
1. 📄 Read lines from the input file.
2. 📥 Store each command in an array.
3. 🔁 Loop through each command one by one.
4. 🧩 Split the command into individual parts (mnemonic, registers, etc.).
5. 🗂️ Identify mnemonic type (R/I/J) using a dictionary.
6. 📐 Define bit structure based on instruction type.
7. 📘 Look up register values from a dictionary.
8. 🔢 Convert integers (like registers or immediate values) to binary.
9. 📏 Pad binary strings with leading 0s to ensure correct bit length.
10. 🔗 Concatenate all parts to form a full 32-bit binary instruction.
