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

# def instr_A()

# "A" for arithmetic, "B" for immediate, "C" for register, 
# "D" for load/store, "E" for jump, and "F" for halt.
assem_code=open("Assembler/assem_code.txt")
open=[i.strip("\n").split() for i in assem_code if len(i)>1]
print(open)
# for line in open:
    # if line[0] in opcode_dict:  
    #     print(opcode_dict[line[0]][1])
        # if opcode_dict[line[0]][1]=='A':
        #     print("calls A")
        # elif opcode_dict[line[0]][1]=='B':
        #     print("calls B")
        # elif opcode_dict[line[0]][1]=='C':
        #     print("calls C")
        # elif opcode_dict[line[0]][1]=='D':
        #     print("calls D")
        # elif opcode_dict[line[0]][1]=='E':
        #     print("calls E")
        # elif opcode_dict[line[0]][1]=='F':
        #     print("calls F")

def error_e(line):
    if int(line[2][1:]) > 127:
        print("error E")
def error_g():
    if len(open[0]) != 2 or open[0][0] != 'var':
        print("error G")
# assem_code=open("assem_code.txt")
# open=assem_code.read()
# print(open)

def error_h_i():
    flag = False
    for i in range(len(open)):
        if 'hlt' in open[i]:
            flag = True
            break
    if flag == False:
        print("error H")
    elif i != len(open) - 1:
        print("error I")
error_h_i()