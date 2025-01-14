from typing import List

class BrainFInterpreter:
    def __init__(self, memory_size: int=30000):
        self.memory_size: int = memory_size
        self.reset()

    def reset(self):
        """Reset the interpreter state"""
        self.memory: List[int] = [0] * self.memory_size
        self.pointer: int = 0
        self.pc: int = 0  # pc: program counter
        self.output: List[str] = []

    def interpret(self, bf_code: str) -> str:
        "Interpret and execute code"
        while self.pc < len(bf_code):
            command: str = bf_code[self.pc]

            if command == ">":
                self.pointer = (self.pointer + 1) % self.memory_size
            elif command == "<":
                self.pointer = (self.pointer - 1) % self.memory_size
            elif command == "+":
                self.memory[self.pointer] = self.memory[self.pointer] + 1
            elif command == "-":
                self.memory[self.pointer] = self.memory[self.pointer] - 1
            elif command == ".":
                self.output.append(chr(self.memory[self.pointer]))
            elif command == ",":
                user_input: str = input('Input a character: ')
                self.memory[self.pointer] = ord(user_input[0])
            elif command == "[":
                if self.memory[self.pointer] == 0:
                    self._jump_forward(bf_code)
            elif command == "]":
                if self.memory[self.pointer] != 0:
                    self._jump_backward(bf_code)

            self.pc += 1

        return "".join(self.output)

    def _jump_forward(self, bf_code: str) -> None:
        """
        Jump past the matching closing bracket
        closing bracket: ']'
        """
        open_bracket: int = 1
        while open_bracket != 0:
            self.pc += 1
            if bf_code[self.pc] == "[":
                open_bracket += 1
            elif bf_code[self.pc] == "]":
                open_bracket -= 1

    def _jump_backward(self, bf_code: str) -> None:
        """
        Jump back to the matching opening bracket
        opening bracket: ']'
        """
        close_bracket: int = 1
        while close_bracket != 0:
            self.pc -= 1
            if bf_code[self.pc] == "]":
                close_bracket += 1
            elif bf_code[self.pc] == "[":
                close_bracket -= 1