opcode_dict = {
    "add": ["00000", "A"],
    "sub": ["00001", "A"],
    "mov": [["00010", "B"],["00011", "C"]],
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

var_dict={}
label_dict = {}
var_count=0

# opcode = str, Mem_address = str, Reg = R1 or R2 etc.
def instr_A(opcode, R1, R2, R3):
    return opcode+"00"+ register_dict[R1]+ register_dict[R2]+ register_dict[R3]

def instr_B(opcode, R1, Imm_value):
    return opcode+"0"+ register_dict[R1] + "".join([str(i) for i in bin(int(Imm_value[1:]))[2:].zfill(7)])
    
def instr_C(opcode, R1, R2):
    return opcode + "0"*5 + register_dict[R1] + register_dict[R2]

def instr_D(opcode, Reg, Mem_address):
    r1_ret = register_dict[Reg]
    unused_bits = "0"
    if mem_address in var_dict:
        ans = str(opcode) + unused_bits + r1_ret + str(bin(var_dict[mem_address])[2:].zfill(7))
    return ans

def instr_E(opcode, Mem_address):
    unused_bits = "0"*4
    if mem_address in label_dict:
        ans = str(opcode) + unused_bits + str(bin(label_dict[mem_address]-var_count)[2:].zfill(7))
    else:
        ans = str(opcode) + unused_bits + str(Mem_address) #0011_0000_label_1
    return ans

def instr_F(opcode,):
    unused_bits = "0"*11
    ans = str(opcode) + unused_bits
    return ans

def is_valid_variable_name(name):
    """Checks whether a given string could be a valid variable name in Python."""
    if not name.isidentifier():
        return False

    # Check whether name is a Python keyword
    if name in {'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
                'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
                'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
                'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'}:
        return False

    return True


def error_func_A(line): #add R1 R2 R3 
    if len(line)==4:
        Register_list=[line[1], line[2], line[3]] 
        for i in Register_list:
            if i=="FLAGS":
                return "Illegal use of FLAGS register"
            if i not in register_dict:
                return "Typos in instruction name or register name"
        return 1
    else:
        return "General Syntax Error"


def error_func_B(line):
    if len(line)==3:
        R1=line[1]
        if R1=="FLAGS":
            return "Illegal use of FLAGS register"
        if R1 not in register_dict:
            return "Typos in instruction name or register name"
        Imm_value=line[2]
        if Imm_value[0]=="$": #mov R1 $10 R3
            try:
                imm_int=int(Imm_value[1:])
            except ValueError:   
                return "Illegal Immediate values (more than 7 bits)"
            if imm_int<0 or imm_int>127:
                return "Illegal Immediate values (more than 7 bits)"
            return 1
        else:
            return "General Syntax Error"
    else:
        return "General Syntax Error"
        

def error_func_C(line, opcode):
    if len(line)==3:
        R1=line[1]
        R2=line[2]
        if R1=="FLAGS" and (R2=="FLAGS" and opcode!="00011"):
            return "Illegal use of FLAGS register"
        if R1 not in register_dict:
            return "Typos in instruction name or register name"
        if R2 not in register_dict:
            return "Typos in instruction name or register name"
    else:
        return "General Syntax Error"
    return 1
    

def error_func_D(line):
    if len(line)==3:   
        R1=line[1]
        if R1=="FLAGS":
            return "Illegal use of FLAGS register"
        if R1 not in register_dict:
            return "Typos in instruction name or register name"
        
        mem_address=line[2]
        if mem_address not in var_dict:
            if mem_address in label_dict:
                return "Misuse of labels as variables or vice-versa"
            try:
                mem_int=int(mem_address)
            except ValueError:
                if is_valid_variable_name(mem_address):
                    return "Variables not declared at the beginning"
                else:
                    return "General Syntax Error"
        return 1
    else:
        return "General Syntax Error"
        

def error_func_E(line):
    if len(line)==1:
        mem_address=line[1]
        if mem_address not in label_dict:
            if mem_address in var_dict:
                return "Misuse of labels as variables or vice-versa"
        else:
            return "Use of Undefined Labels"
        return 1
    else:
        return "General Syntax Error"
        
def error_func_F(line):
    if len(line)==1:
        return 1
    else:
        "General Syntax Error"   

def check_mov_type(line):
    if "$" in "".join(line):
        return opcode_dict[line[0]][0][1], opcode_dict[line[0]][0][0]
    else:
        return opcode_dict[line[0]][1][1], opcode_dict[line[0]][1][0]   

# "A" for arithmetic, "B" for immediate, "C" for register,
# "D" for load/store, "E" for jump, and "F" for halt.

assem_code=open("Assembler/assem_code.txt")
open=[i.strip("\n").split(' ') for i in assem_code] 

#for loop for label list
for line_no in range(len(open)):
    line=open[line_no]
    if ":" in "".join(line):
        if line[0][-1] == ":":
            label_dict[line[0][:-1]]=line_no
        else:
            print("General Syntax Error")
            quit()
    elif line[0] == "var":
        var_count+=1
            
#printing missing halt error
if "hlt" not in open[-1]:
    print("Missing hlt error")
    quit()

# main for loop
for line_no in range(len(open)):

    line=open[line_no]
    
    if line==['']:
        continue
    
    if line[0][-1]==":" and len(line[0])>1: #remove label prefix
        line.pop(0)
        
    if line == ['hlt'] and line_no != len(open) - 1:
        print("hlt not being used as the last instruction")   
        quit()
    
    if len(line) and line[0] in opcode_dict:
        instr_type = opcode_dict[line[0]][1]
        opcode = opcode_dict[line[0]][0]
        
        if line[0]=="mov":
            instr_type,opcode=check_mov_type(line)
            
        if instr_type =='A':
            print(error_func_A(line))
            quit()
        elif instr_type =='B':
            #first we'll call the err_func_B
            print(error_func_B(line))
            quit()

        elif instr_type =='C':
            #first we'll call the err_func_C
            print(error_func_C(line, opcode))
            quit()

        elif instr_type =='D':
            #first we'll call the err_func_D
            print(error_func_D(line))
            quit()
            
        elif instr_type =='E':
            #first we'll call the err_func_E
            print(error_func_E(line))
            quit()
            
        elif instr_type =='F':
            #first we'll call the err_func_F
            #if no error is caught then:
            print(error_func_F(line))
            quit()
            
    elif line[0]=="var":
        try:
            line[1]
        except Exception:
            print("General Syntax Error")
            quit()
        var_dict[line[1]] = line_no+(len(open)-var_count)
        if not is_valid_variable_name(line[1]):
           print("General Syntax Error") 
           quit()
    else:
        print("Typos in instruction name or register name")
        quit()
        
for line_no in range(len(open)):

    line=open[line_no]
    
    if line==['']:
        continue
    
    if line[0][-1]==":" and len(line[0])>1: #remove label prefix
        line.pop(0)
    
    if len(line) and line[0] in opcode_dict:
        instr_type = opcode_dict[line[0]][1]
        opcode = opcode_dict[line[0]][0]
        
        if line[0]=="mov":
            instr_type,opcode=check_mov_type(line)
        
        if instr_type =='A':
            bin_instr=instr_A(opcode, line[1], line[2], line[3])
            print(bin_instr)
        elif instr_type =='B':
            bin_instr=instr_B(opcode, line[1], line[2])
            print(bin_instr)
        elif instr_type =='C':
            bin_instr=instr_C(opcode, line[1], line[2])
            print(bin_instr)
        elif instr_type =='D':
            reg = line[1] # maybe useless but makes the function call a bit intuitive (I guess ?)
            mem_address = line[2]
            # bin_instr is the line that we'll write to the output file
            bin_instr = instr_D(opcode, reg, mem_address)
            print(bin_instr)
        elif instr_type =='E':
            mem_address = line[1]
            bin_instr = instr_E(opcode, mem_address)
            print(bin_instr)
        elif instr_type =='F':
            bin_instr = instr_F(opcode)
            print(bin_instr)
    elif line[0]=="var":
        pass
    

