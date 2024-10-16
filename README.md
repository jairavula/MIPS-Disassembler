# MIPS Disassembler - Python

This Python script disassembles MIPS machine code into human-readable assembly instructions. It processes hexadecimal instructions and translates them into MIPS assembly, supporting R-type, I-type, and J-type instructions. Additionally, it automatically formats branch instructions with labels for better readability.

## Features

- **Hex to Binary Conversion**: Converts hex strings into binary.
- **Instruction Decoding**: Supports decoding for R-type, I-type, and J-type instructions.
- **Label Generation**: Automatically generates labels for branch instructions (e.g., `beq`, `bne`).
- **Formatted Output**: Produces neatly formatted MIPS assembly code, including labels and memory offsets.

## How It Works

### Main Components:

- **`hex_to_binary()`**: Converts hexadecimal strings to binary.
- **`binary_to_decimal()`**: Converts binary strings to decimal.
- **`signed_binary_to_decimal()`**: Converts signed binary numbers to decimal.
- **`dissasemble_instruction()`**: Decodes a binary string into a MIPS instruction.
- **`read_file()`**: Reads instructions from a file and converts them.
- **`format_mips()`**: Labels and formats branch instructions.
- **`create_file()`**: Converts input files into `.s` assembly files.

## Usage

1. Enter the name of the `.obj` file to be decoded inside the parameter
of the `__main__` function:
2. Run the script, specifying the file name:
   ```bash
   python Dissasembler.py
3. Ensure that the input file is within the same directory of the Python file,
the output file will be produced in the same directory of the Python file.



