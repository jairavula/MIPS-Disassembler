# Jai Ravula 
# Created 10/12/2024
# Latest Update 10/15/2024

opcodes: dict = {
    "0" : "R",
    "2" : "j",
    "3" : "jal",
    "4" : "beq",
    "5" : "bne",
    "6" : "blez",
    "7" : "bgtz",
    "8" : "addi",
    "9" : "addiu",
    "10" : "slti",
    "11" : "sltiu",
    "12" : "andi",
    "13" : "ori",
    "14" : "xori",
    "15" : "lui",
    "32" : "lb", 
    "33" : "lh", 
    "34" : "lwl", 
    "35" : "lw", 
    "36" : "lbu", 
    "37" : "lhu", 
    "38" : "lwr", 
    "40" : "sb", 
    "41" : "sh",
    "42" : "swl",
    "43" : "sw",
    "46" : "swr",
    "47" : "cache",
    "48" : "ll",
    "49" : "lwc1",
    "50" : "lwc2",
    "51" : "pref",
    "53" : "ldc1",
    "54" : "ldc2",
    "56" : "sc",
    "57" : "swc1",
    "58" : "swc2",
    "61" : "sdc1",
    "62" : "sdc2"}

function_codes: dict = {
    "0" : "sll",
    "2" : "srl",
    "3" : "sra",
    "4" : "sllv",
    "6" : "srlv",
    "7" : "srav",
    "8" : "jr",
    "9" : "jalr",
    "10" : "movz",
    "11" : "movn",
    "12" : "syscall",
    "13" : "break",
    "15" : "sync",
    "16" : "mfhi",
    "17" : "mthi",
    "18" : "mflo",
    "19" : "mtlo",
    "24" : "mult",
    "25" : "multu",
    "26" : "div",
    "27" : "divu",
    "32" : "add", 
    "33" : "addu", 
    "34" : "sub", 
    "35" : "subu", 
    "36" : "and", 
    "37" : "or", 
    "38" : "xor", 
    "39" : "nor",
    "42" : "slt",
    "43" : "sltu",
    "48" : "tge",
    "49" : "tgeu",
    "50" : "tlt",
    "51" : "tltu",
    "52" : "teq",
    "54" : "tne", }

registers: dict = {
    "0" : "$zero",
    "1" : "$at",
    "2" : "$v0",
    "3" : "$v1",
    "4" : "$a0",
    "5" : "$a1",
    "6" : "$a2",
    "7" : "$a3",
    "8" : "$t0",
    "9" : "$t1",
    "10" : "$t2",
    "11" : "$t3",
    "12" : "$t4",
    "13" : "$t5",
    "14" : "$t6",
    "15" : "$t7",
    "16" : "$s0",
    "17" : "$s1",
    "18" : "$s2",
    "19" : "$s3",
    "20" : "$s4",
    "21" : "$s5",
    "22" : "$s6",
    "23" : "$s7",
    "24" : "mult",
    "25" : "multu",
    "26" : "div",
    "27" : "divu",
    "32" : "add", }

h2b: dict = {
    '0' : "0000",
    '1' : "0001",
    '2' : "0010",
    '3' : "0011",
    '4' : "0100",
    '5' : "0101",
    '6' : "0110",
    '7' : "0111",
    '8' : "1000",
    '9' : "1001",
    'a' : "1010",
    'b' : "1011",
    'c' : "1100",
    'd' : "1101", 
    'e' : "1110", 
    'f' : "1111"}

def hex_to_binary(hex: str):
    binary_str = ""
    for i in range(len(hex)-1):
        try:
            binary_str += h2b[hex[i]]
        except KeyError:
            print(f"Invalid hex character: {hex[i]}")
            return None 
    return binary_str

def binary_to_decimal(binary: str):

    decimal_value: int = 0
    length = len(binary)

    for i in range(length):
        if binary[i] == '1':
            decimal_value += 2 ** (length - i - 1)
    return str(decimal_value)

def signed_binary_to_decimal(binary: str) -> str:
    is_negative = binary[0] == '1'
    if is_negative:
        decimal_value = int(binary, 2) - (1 << len(binary))
    else:
        decimal_value = int(binary, 2)
    return str(decimal_value)

def dissasemble_instruction(binary_str: str) -> str:
    try:
        mips_instruction: str = ""
        opcode: str = binary_str[0:6]
        if opcode == "000000":
            # Execute R type dissasembly
            func: str = function_codes[binary_to_decimal(binary_str[26:32])] + ' '
            rs: str = registers[binary_to_decimal(binary_str[6:11])]
            rt: str = registers[binary_to_decimal(binary_str[11:16])]
            rd: str = registers[binary_to_decimal(binary_str[16:21])]
            shamt: str = binary_to_decimal(binary_str[21:26])
            if func == "sll " or func == "srl ":
                mips_instruction = func + rd + ', ' + rt + ', ' + shamt
            else:
                mips_instruction = func + rd + ', ' + rs + ', ' + rt


        elif opcode == "000010" or opcode == "000011":
            # Execute J type dissasembly
            func: str = opcodes[binaryto_decimal(opcode)]
            imm: str = binary_str(binary_str[6:32])
            if opcode == "000010":
                mips_instruction = func + ' ' + imm
            else:
                mips_instruction = func + ' ' + imm

        else:
            imm_labeled = ["beq", "bne"]
            imm_offsets = ["lbu", "lhu", "ll", "lw", "sb", "sw", "sc", "sh"]
            # Execute I type dissasembly
            func: str = opcodes[binary_to_decimal(opcode)]
            rs: str = registers[binary_to_decimal(binary_str[6:11])]
            rt: str = registers[binary_to_decimal(binary_str[11:16])]
            imm: str = binary_to_decimal(binary_str[16:32])

            if func in imm_labeled:
                imm = signed_binary_to_decimal(binary_str[16:32])
                mips_instruction = func + ' ' + rs + ', ' + rt + ', ' + imm
            elif func in imm_offsets:
                mips_instruction = func + ' ' + rt + ', ' + imm + '( ' + rs + ' )'
            else:
                mips_instruction = func + ' ' + rs + ', ' + rt + ', ' + imm
    
    except:
        print("Invalid Instruction, dissasembly stopped!")
        return ""

    return mips_instruction

def read_file(filepath: str):
    with open(filepath, 'r') as file:
        instructions_array = []
        for line in file:
            line.strip()
            binary_str = hex_to_binary(line)
            mips_code = dissasemble_instruction(binary_str) 
            if mips_code == "":
                return []
            instructions_array.append(mips_code)
    return instructions_array

def format_mips(instructions_array):

    if instructions_array == []:
        print("Instruction Set Cannot be disassembled")
        return

    label_map = {}
    label_count = 0

    for i, instruction in enumerate(instructions_array):
        if "beq" in instruction or "bne" in instruction:
            splits = instruction.split(',')
            offset = int(splits[2].strip())
            
            target_index = i + 1 + offset

            if 0 <= target_index < len(instructions_array):
                target_address = 0 + (target_index * 4)
                label_name = f"Addr_{target_address:04X}"


                if target_index not in label_map:
                    label_map[target_index] = label_name
                    label_count += 1

                splits[2] = f" {label_map[target_index]}"
                instructions_array[i] = ','.join(splits)

    final_output = []

    final_output.append(".globl     main \n.data \n.text \n main:")
    for i, instruction in enumerate(instructions_array):
        if i in label_map:
            final_output.append(f"  {label_map[i]}:")
        
        final_output.append(f"      {instruction}")
    final_output.append("  ori $v0, $0, 10 \n  syscall")


    for instruction in final_output:
        print(instruction)
    return final_output

def create_file(filename: str):
    instructions = read_file(f'./Test Cases/{filename}')
    result = format_mips(instructions)

    output_filename = filename.rsplit('.', 1)[0] + ".s"

    with open(output_filename, 'w') as f:
        for instruction in result:
            f.write(instruction + '\n')

    print(f"Assembly code has been written to {output_filename}")

if __name__ == "__main__":
    create_file('test_case3.obj')