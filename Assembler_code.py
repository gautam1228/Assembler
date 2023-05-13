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
# "A" for arithmetic, "B" for immediate, "C" for register, 
# "D" for load/store, "E" for jump, and "F" for halt.
assem_code=open("Assembler/assem_code.txt")
open=[i.strip("\n").split() for i in assem_code if len(i)>1]
print(open)
for line in open:
    if line[0] in opcode_dict:
        print(line[0])

 