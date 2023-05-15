# Assembler Readme

This is a simple assembler program that converts assembly code into binary machine code. The program takes an assembly code file as input, performs syntax and error checking, and generates a binary output file.

## Usage

1. Create an assembly code file: Create a text file with the assembly instructions you want to convert into binary code. Each instruction should be on a separate line.

2. Define variables (optional): If your assembly code uses variables, you can declare them using the `var` keyword followed by the variable name. Variables should be declared at the beginning of the code.

3. Define labels (optional): Labels can be used for jump instructions. To define a label, simply add a colon (:) at the end of the line containing the label name.

4. Save the assembly code file: Save the assembly code file with a `.txt` extension.

5. Run the assembler: Execute the assembler program, providing the path to the assembly code file as input.

6. Check the output: The assembler will generate a binary output file containing the converted machine code. Each line of the output file represents a binary instruction.

## Instruction Format

The assembler supports the following instruction formats:

- Arithmetic instructions: `add`, `sub`, `mul`, `div`
  - Format: `<opcode> <R1> <R2> <R3>`
  - Example: `add R1 R2 R3`

- Move instructions: `mov`
  - Format: `<opcode> <R1> <R2>`
  - Example: `mov R1 $10 R3`

- Load/store instructions: `ld`, `st`
  - Format: `<opcode> <Reg> <mem_address>`
  - Example: `ld R1 var1`

- Comparison instructions: `cmp`
  - Format: `<opcode> <R1> <R2>`
  - Example: `cmp R1 R2`

- Jump instructions: `jmp`, `jlt`, `jgt`, `je`
  - Format: `<opcode> <Mem_address>`
  - Example: `jmp label1`

- Halt instruction: `hlt`
  - Format: `<opcode>`
  - Example: `hlt`

## Error Handling

The assembler performs syntax and error checking on the input assembly code. It detects and reports the following errors:

- Invalid opcode or operand
- Illegal use of registers or labels
- Missing or misplaced labels
- Incorrect number of parameters for an instruction
- Illegal immediate values or variable names

If any errors are detected, the assembler will display an error message indicating the specific line and issue encountered.

## Notes

- Variables should be declared at the beginning of the code, before any instructions that reference them.

- Labels should be defined using a colon (:) at the end of the line containing the label name. Labels can be used for jump instructions.

- The assembler assumes a specific opcode and register format, as defined in the code. If you need to modify the opcode or register format, you can update the `opcode_dict` and `register_dict` dictionaries in the code.

- The assembler outputs the binary machine code to a separate output file. The generated binary code can be used for further processing or execution on a compatible system.

## License

Feel free to modify and distribute it as needed.

## Credits

This assembler program was developed by Aditya Aggardwal, Gautam Singh, Kunal Sharma, Mehul Pahuja.

## Feedback and Contributions

Feedback, bug reports, and contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on the [GitHub repository](https://github
