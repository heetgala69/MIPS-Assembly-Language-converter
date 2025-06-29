# MIPS-Assembly-Language-converter
This repository contains all the necessary code and files to implement a basic MIPS to binary converter, developed as part of a college project at NMIMS University. The program reads MIPS assembly instructions from a file and converts each instruction into a corresponding 32-bit binary representation.

graph TD
    A[📄 Read lines from input file] --> B[📥 Store each command in an array]
    B --> C[🔁 Loop through each command]
    C --> D[🧩 Split command into parts]
    D --> E[🗂️ Identify mnemonic type using dictionary]
    E --> F[📐 Determine bit positions based on instruction format]
    F --> G[📘 Convert register names to integers using dictionary]
    G --> H[🔢 Convert integers to binary]
    H --> I[📏 Pad with leading zeros to match bit-length]
    I --> J[🔗 Concatenate all binary segments into 32-bit output]
