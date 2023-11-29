
# Function for tokenize
def tokenize(line):
    tokens = []
    token = ''
    in_string = False
    for char in line:
        if char == '"' and not in_string:
            in_string = True
            token += char
        elif char == '"' and in_string:
            token += char
            tokens.append(token)
            token = ''
            in_string = False
        elif in_string:
            token += char
        else:
            if char.isspace():
                if token:
                    tokens.append(token)
                    token = ''
            else:
                token += char
    if token:
        tokens.append(token)
    return tokens
# Function to build a symbol table with labels and their corresponding line numbers
def build_symbol_table(program_lines):
    symbol_table = {}
    line_number = 0
    for line in program_lines:
        if line.endswith(':'):  # Label definition
            label = line[:-1]  # Remove colon
            symbol_table[label] = line_number
        else:
            line_number += 1
    return symbol_table

# 这个函数负责将指令和操作数翻译成可执行的形式。如果操作数存在于符号表中，它将使用符号表中的值；如果操作数是数字，它将被转换为整数。
def translate_line(instruction, operand, symbol_table):
    instructions_without_operand = ['HLT']  # Add other instructions that do not require operands as needed
    if instruction.upper() in instructions_without_operand:
        return (instruction.upper(),)

    if operand and operand in symbol_table:
        operand = symbol_table[operand]
    elif operand and operand.isdigit():
        operand = int(operand)
    else:
        raise ValueError("Invalid operand in line: " + instruction + " " + str(operand))

    return (instruction.upper(), operand)
# Function for parse_line
def parse_line(line, symbol_table):
    tokens = tokenize(line)
    if not tokens or line.endswith(':'):
        return None, None
    instruction = tokens[0]
    operand = tokens[1] if len(tokens) > 1 else None

    # Modified part: Check the number of elements returned by translate_line
    translated = translate_line(instruction, operand, symbol_table)
    if len(translated) == 1:
        return translated[0], None  # Only instruction, no operand
    else:
        return translated
# Function for translate_program
# def translate_program(program_lines):
#     symbol_table = build_symbol_table(program_lines)
#     translated_program = []
#
#     for line in program_lines:
#         instruction, operand = parse_line(line, symbol_table)
#         if instruction is not None:
#             translated_program.append((instruction, operand))
#
#     return translated_program


def translate_program(program_lines):
    tokens = [token for line in program_lines for token in tokenize(line)]
    instructions = []
    for token in tokens:
        if token.startswith('"') and token.endswith('"'):
            instructions.append(('push_str', token))
        else:
            symbol_table = build_symbol_table(program_lines)
            translated_program = []

            for line in program_lines:
                instruction, operand = parse_line(line, symbol_table)
                if instruction is not None:
                    translated_program.append((instruction, operand))
            return translated_program
    return instructions


def translate_program(program_lines):
    instructions = []
    for line in program_lines:
        tokens = tokenize(line)
        if not tokens:
            continue
        if tokens[0] == 'push_str' and len(tokens) == 2:
            instructions.append(('push_str', tokens[1]))
        else:
            # Handle other instructions
            instructions.append((tokens[0], tokens[1] if len(tokens) > 1 else None))
    return instructions
