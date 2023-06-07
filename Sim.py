import sys
instr_dict={
    "00000": "add",
    "00001": "sub",
    "00010": "movi",
    "00011": "mov",
    "00100": "ld",
    "00101": "st",
    "00110": "mul",
    "00111": "div",
    "01000": "rs",
    "01001": "ls",
    "01010": "xor",
    "01011": "or",
    "01100": "and",
    "01101": "not",
    "01110": "cmp",
    "01111": "jmp",
    "11100": "jlt",
    "11101": "jgt",
    "11111": "je",
    "11010": "hlt"
}


def func_add(inputline):
    # Implementation of the add instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1+num2
    if num<65536: #2^16
        output_list[R1]=num
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[R1]=0
        output_list[8]+=8
def func_sub(inputline):
    # Implementation of the sub instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1-num2
    if num1>=num2: #2^16
        output_list[R1]=num
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[R1]=0
        output_list[8]+=8

def func_movi(inputline):
    # Implementation of the mov instruction
    R1 = int(inputline[1:4],2) + 1
    imm=int(inputline[4:11], 2) 
    output_list[R1]=imm
    output_list[8]=0 #reseting FLAGS register to 0

def func_mov(inputline):
    # Implementation of the mov instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    num=output_list[R2]
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0


def func_ls(inputline):
    # Implementation of the ls instruction
    R1 = int(inputline[1:4],2) + 1
    imm=int(inputline[4:11], 2) 
    num=output_list[R1]
    while(imm):
        num=int(num*2)
        imm-=1
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_xor(inputline):
    # Implementation of the xor instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1^num2
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_or(inputline):
    # Implementation of the or instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1 | num2
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_and(inputline):
    # Implementation of the and instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1 & num2
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_not(inputline):
    # Implementation of the not instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    num=output_list[R2]
    output_list[R1]=~num
    output_list[8]=0 #reseting FLAGS register to 0

def func_ld(inputline):
    # Implementation of the ld instruction
    R1=int(inputline[1:4],2) + 1
    mem=int(inputline[4:11],2)
    output_list[R1]=input_list[mem]
    output_list[8]=0 #reseting FLAGS register to 0

def func_st(inputline):
    # Implementation of the st instruction
    R1=int(int(inputline[1:4],2) + 1)
    mem=int(inputline[4:11],2) 
    input_list[mem]=str(bin(output_list[R1]))[2:].zfill(7)
    output_list[8]=0 #reseting FLAGS register to 0

def func_mul(inputline):
    # Implementation of the mul instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1*num2
    if num<65536: #2^16
        output_list[R1]=num
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[R1]=0
        output_list[8]+=8

def func_div(inputline):
    # Implementation of the div instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    if R2 != 0:
        quotient=R1/R2
        remainder=R1%R2
        output_list[1]=quotient
        output_list[2]=remainder
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[8]+=8
        output_list[1]=0
        output_list[2]=0

def func_rs(inputline):
    # Implementation of the rs instruction
    R1 = int(inputline[1:4],2) + 1
    imm=int(inputline[4:11], 2) 
    num=output_list[R1]
    while(imm):
        num=int(num/2)
        imm-=1
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_call(instr, inputline):
    if instr == "add":
        func_add(inputline)
    elif instr == "sub":
        func_sub(inputline)
    elif instr == "movi":
        func_movi(inputline)
    elif instr == "mov":
        func_mov(inputline)
    elif instr == "ld":
        func_ld(inputline)
    elif instr == "st":
        func_st(inputline)
    elif instr == "mul":
        func_mul(inputline)
    elif instr == "div":
        func_div(inputline)
    elif instr == "rs":
        func_rs(inputline)
    elif instr == "ls":
        func_ls(inputline)
    elif instr == "xor":
        func_xor(inputline)
    elif instr == "or":
        func_or(inputline)
    elif instr == "and":
        func_and(inputline)
    elif instr == "not":
        func_not(inputline)
    elif instr == "cmp":
        func_cmp(inputline)
    elif instr == "jmp":
        func_jmp(inputline)
    elif instr == "jlt":
        func_jlt(inputline)
    elif instr == "jgt":
        func_jgt(inputline)
    elif instr == "je":
        func_je(inputline)
    elif instr == "hlt":
        func_hlt(inputline)
    else:
        print("Invalid instruction")
import sys
instr_dict={
    "00000": "add",
    "00001": "sub",
    "00010": "movi",
    "00011": "mov",
    "00100": "ld",
    "00101": "st",
    "00110": "mul",
    "00111": "div",
    "01000": "rs",
    "01001": "ls",
    "01010": "xor",
    "01011": "or",
    "01100": "and",
    "01101": "not",
    "01110": "cmp",
    "01111": "jmp",
    "11100": "jlt",
    "11101": "jgt",
    "11111": "je",
    "11010": "hlt"
}

def func_call(instr, inputline):
    if instr == "add":
        func_add(inputline)
    elif instr == "sub":
        func_sub(inputline)
    elif instr == "movi":
        func_movi(inputline)
    elif instr == "mov":
        func_mov(inputline)
    elif instr == "ld":
        func_ld(inputline)
    elif instr == "st":
        func_st(inputline)
    elif instr == "mul":
        func_mul(inputline)
    elif instr == "div":
        func_div(inputline)
    elif instr == "rs":
        func_rs(inputline)
    elif instr == "ls":
        func_ls(inputline)
    elif instr == "xor":
        func_xor(inputline)
    elif instr == "or":
        func_or(inputline)
    elif instr == "and":
        func_and(inputline)
    elif instr == "not":
        func_not(inputline)
    elif instr == "cmp":
        func_cmp(inputline)
    elif instr == "jmp":
        func_jmp(inputline)
    elif instr == "jlt":
        func_jlt(inputline)
    elif instr == "jgt":
        func_jgt(inputline)
    elif instr == "je":
        func_je(inputline)
    elif instr == "hlt":
        func_hlt(inputline)
    else:
        print("Invalid instruction")

def func_add(inputline):
    # Implementation of the add instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1+num2
    if num<65536: #2^16
        output_list[R1]=num
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[R1]=0
        output_list[8]+=8

def func_sub(inputline):
    # Implementation of the sub instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1-num2
    if num1>=num2: #2^16
        output_list[R1]=num
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[R1]=0
        output_list[8]+=8

def func_movi(inputline):
    # Implementation of the mov instruction
    R1 = int(inputline[1:4],2) + 1
    imm=int(inputline[4:11], 2) 
    output_list[R1]=imm
    output_list[8]=0 #reseting FLAGS register to 0

def func_mov(inputline):
    # Implementation of the mov instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    num=output_list[R2]
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_ld(inputline):
    # Implementation of the ld instruction
    R1=int(inputline[1:4],2) + 1
    mem=int(inputline[4:11],2)
    output_list[R1]=input_list[mem]
    output_list[8]=0 #reseting FLAGS register to 0

def func_st(inputline):
    # Implementation of the st instruction
    R1=int(int(inputline[1:4],2) + 1)
    mem=int(inputline[4:11],2) 
    input_list[mem]=str(bin(output_list[R1]))[2:].zfill(7)
    output_list[8]=0 #reseting FLAGS register to 0

def func_mul(inputline):
    # Implementation of the mul instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1*num2
    if num<65536: #2^16
        output_list[R1]=num
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[R1]=0
        output_list[8]+=8

def func_div(inputline):
    # Implementation of the div instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    if R2 != 0:
        quotient=R1/R2
        remainder=R1%R2
        output_list[1]=quotient
        output_list[2]=remainder
        output_list[8]=0 #reseting FLAGS register to 0
    else:
        output_list[8]+=8
        output_list[1]=0
        output_list[2]=0

def func_rs(inputline):
    # Implementation of the rs instruction
    R1 = int(inputline[1:4],2) + 1
    imm=int(inputline[4:11], 2) 
    num=output_list[R1]
    while(imm):
        num=int(num/2)
        imm-=1
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_ls(inputline):
    # Implementation of the ls instruction
    R1 = int(inputline[1:4],2) + 1
    imm=int(inputline[4:11], 2) 
    num=output_list[R1]
    while(imm):
        num=int(num*2)
        imm-=1
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_xor(inputline):
    # Implementation of the xor instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1^num2
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_or(inputline):
    # Implementation of the or instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1 | num2
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_and(inputline):
    # Implementation of the and instruction
    R1 = int(inputline[2:5],2) + 1
    R2 = int(inputline[5:8], 2) + 1
    R3 = int(inputline[8:11], 2) + 1
    num1=output_list[R2]
    num2=output_list[R3]
    num=num1 & num2
    output_list[R1]=num
    output_list[8]=0 #reseting FLAGS register to 0

def func_not(inputline):
    # Implementation of the not instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    num=output_list[R2]
    output_list[R1]=~num
    output_list[8]=0 #reseting FLAGS register to 0
    

def func_cmp(inputline):
    # Implementation of the cmp instruction
    R1 = int(inputline[5:8],2) + 1
    R2 = int(inputline[8:11],2) + 1
    num1=output_list[R1]
    num2=output_list[R2]  
    output_list[8]=0
    if num1<num2:
        output_list[8]+=4
    elif num1>num2:
        output_list[8]+=2
    else:
        output_list[8]+=1 

def func_jmp(inputline):
    # Implementation of the jmp instruction
    mem=int(inputline[4:11],2) 
    global pc
    pc=mem
    output_list[8]=0
    
def func_jlt(inputline):
    # Implementation of the jlt instruction
    if output_list[8]==4:
        mem=int(inputline[4:11],2) 
        global pc
        pc=mem
    output_list[8]=0

def func_jgt(inputline):
    # Implementation of the jgt instruction
    if output_list[8]==2:
        mem=int(inputline[4:11],2) 
        global pc
        pc=mem
    output_list[8]=0

def func_je(inputline):
    # Implementation of the je instruction
    if output_list[8]==1:
        mem=int(inputline[4:11],2) 
        global pc
        pc=mem
    output_list[8]=0
    
def func_hlt(inputline):
    # Implementation of the hlt instruction
    global pc
    pc=256
    output_list[8]=0

    
input_list=[]
output_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in sys.stdin:
    line = line.strip()
    if line == [' ']:
        break
    input_list.append(line)
while(len(input_list) < 128):
    input_list.append(0)
pc=0
while(pc<128):
    line=input_list[pc]
    # print(pc)
    if line !=0:
        line=str(line)
        opcode=line[0:5]
        instr=instr_dict[opcode]
        pc+=1
        func_call(instr, line[5:])
        for i in range(9):
            if i==0:
                print(str(bin(output_list[i]))[2:].zfill(7), end="        ")
            elif i==8:
                print(str(bin(output_list[i]))[2:].zfill(16))
            else:
                print(str(bin(output_list[i]))[2:].zfill(16), end=" ")
        output_list[0]=pc
for i in input_list:
    print(str(i).zfill(16))
