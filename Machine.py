
from ISA import MachineState

class Machine:
    def __init__(self, program):
        self.state = MachineState()
        self.program = program  # Program is a list of (instruction, operand) tuples

    def run(self):
        try:
            while self.state.pc < len(self.program):
                instruction, operand = self.program[self.state.pc]
                if instruction == 'HALT':
                    break
                if hasattr(self.state, instruction):
                    func = getattr(self.state, instruction)
                    if operand is not None:
                        func(operand)
                    else:
                        func()
                self.state.update_flags()  # Update flags after each instruction
                print(f'Instruction: {instruction}, Operand: {operand}, PC: {self.state.pc}, Accumulator: {self.state.accumulator}, Flags: {self.state.flags}')  # Debug print
                if not self.is_jump_instruction(instruction):
                    self.state.pc += 1  # Increment program counter if not a jump instruction
        except Exception as e:
            print(f"Error during execution: {e}")

    def display_state(self):
        print(f"Accumulator: {self.state.accumulator}")
        print(f"Program Counter: {self.state.pc}")
        print(f"Flags: {self.state.flags}")
        print(f"Memory: {self.state.memory[:10]}")  # Display first 10 memory locations

    def is_jump_instruction(self, instruction):
        return instruction in ['JMP', 'JZ', 'JNZ', 'JE', 'JNE']
