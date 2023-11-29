class MachineState:
    def __init__(self):
        self.accumulator = 0
        self.memory = [0] * 256
        self.pc = 0  # Program Counter
        self.flags = {'Z': False, 'S': False, 'O': False}  # Zero, Sign, Overflow flags
        self.stack = []
        self.tick_counter = 0

    def LD(self, value):
        self.accumulator = value

    def ST(self, address):
        self.memory[address] = self.accumulator

    def ADD(self, value):
        self.accumulator += value
        self.update_flags()

    def SUB(self, value):
        self.accumulator -= value
        self.update_flags()

    def MUL(self, value):
        self.accumulator *= value
        self.update_flags()

    def DIV(self, value):
        if value == 0:
            raise ValueError("Division by zero")
        self.accumulator //= value
        self.update_flags()

    def CMP(self, value):
        result = self.accumulator - value
        self.flags['Z'] = (result == 0)
        self.flags['S'] = (result < 0)

    def JMP(self, address):
        print(f'Executing JMP to address:', address)  # Debug print
        self.check_memory_address(address)
        self.pc = address

    def JZ(self, address):
        print(f'Executing JZ to address:', address)  # Debug print
        if self.flags['Z']:
            self.pc = address
        else:
            self.pc += 1


    def JNZ(self, address):
        print(f'Executing JNZ to address:', address)  # Debug print
        if not self.flags['Z']:
            self.pc = address


    def JE(self, address):
        if self.flags['Z']:
            self.pc = address


    def JNE(self, address):
        if not self.flags['Z']:
            self.pc = address


    def PUSH(self, value):
        self.stack.append(value)


    def POP(self):
        if not self.stack:
            raise IndexError("Pop from empty stack")
        return self.stack.pop()


    def CALL(self, address):
        print(f'Executing CALL to address:', address)  # Debug print
        self.PUSH(self.pc)
        self.JMP(address)


    def RET(self):
        self.pc = self.POP()


    def check_memory_address(self, address):
        if address < 0 or address >= len(self.memory):
            raise ValueError("Invalid memory address")


    def run_instruction(self, instruction, operand):
        no_operand_instructions = ['HALT']
        if instruction in no_operand_instructions:
            getattr(self, instruction)()
        elif instruction in ['JMP', 'JZ', 'JS', 'JNZ', 'CALL', 'RET']:
            getattr(self, instruction)(operand)
        else:
            getattr(self, instruction)(operand)
            self.pc += 1


    def _check_memory_bounds(self, address):
        if address < 0 or address >= len(self.memory):
            raise ValueError(f"Memory address {address} is out of bounds.")


    def update_flags(self):
        self.flags['Z'] = (self.accumulator == 0)
        self.flags['S'] = (self.accumulator < 0)

    # String operations
    def pstr(self):
        # 弹出操作和字符串
        operation = self.stack.pop()
        string = self.stack.pop()

        # 执行相应的操作
        if operation == 'reverse':
            result = string[::-1]
        elif operation == 'upper':
            result = string.upper()
        elif operation == 'lower':
            result = string.lower()
        else:
            raise ValueError("Invalid string operation")

        # 将结果压回栈中
        self.stack.append(result)

    def print_top(self):
        print(self.stack.pop())

    def push_str(self, string):
        self.stack.append(string.strip('"'))

    def split_string(self, delimiter=' '):
        if len(self.stack) < 1:
            raise ValueError("Stack is empty, cannot perform split operation.")
        input_string = self.pop()
        self.push(input_string.split(delimiter))