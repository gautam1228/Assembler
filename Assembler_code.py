opcode_dict = {
    "add": ["00000", "A"],
    "sub": ["00001", "A"],
    "mov": ["00010", "B"],
    "mov": ["00011", "C"],
    "ld": ["00100", "D"],
    "st": ["00101", "D"],
    "mul": ["00110", "A"],
    "div": ["00111", "C"],
    "rs": ["01000", "B"],
    "ls": ["01001", "B"],
    "xor": ["01010", "A"],
    "or": ["01011", "A"],
    "and": ["01100", "A"],
    "not": ["01101", "C"],
    "cmp": ["01110", "C"],
    "jmp": ["01111", "E"],
    "jlt": ["11100", "E"],
    "jgt": ["11101", "E"],
    "je": ["11111", "E"],
    "hlt": ["11010", "F"]
}
register_dict = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"
}

def instr_A()

# "A" for arithmetic, "B" for immediate, "C" for register, 
# "D" for load/store, "E" for jump, and "F" for halt.
assem_code=open("Assembler/assem_code.txt")
open=[i.strip("\n").split() for i in assem_code if len(i)>1]
for line in open:
    if line[0] in opcode_dict:  
        print(opcode_dict[line[0]][1])
        if opcode_dict[line[0]][1]=='A':
            print("calls A")
        elif opcode_dict[line[0]][1]=='B':
            print("calls B")
        elif opcode_dict[line[0]][1]=='C':
            print("calls C")
        elif opcode_dict[line[0]][1]=='D':
            print("calls D")
        elif opcode_dict[line[0]][1]=='E':
            print("calls E")
        elif opcode_dict[line[0]][1]=='F':
            print("calls F")
        

 