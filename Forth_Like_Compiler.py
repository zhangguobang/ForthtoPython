
import sys
from Translator import translate_program
from Machine import Machine

def read_program_from_console():
    print("Enter your program code (type 'END' to execute, 'EXIT' to finish):")
    program_lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        elif line.upper() == "EXIT":
            sys.exit("Exiting program.")
        program_lines.append(line)
    return program_lines

def main():
    try:
        while True:
            print("Forth-Like Compiler and Machine Simulator")
            program_lines = read_program_from_console()
            translated_program = translate_program(program_lines)
            machine = Machine(translated_program)
            machine.run()
            machine.display_state()
            print("\nProgram executed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

