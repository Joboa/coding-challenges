class BrainFInterpreter:
    def __init__(self, memory_size=30000):
        self.memory_size = memory_size
        self.reset()

    def reset(self):
        """Reset the interpreter state"""
        self.memory = [0] * self.memory_size
        self.pointer = 0
        self.pc = 0  # pc: program counter
        self.output = []

    def interpret(self, bf_code):
        "Interpret and execute code"
        while self.pc < len(bf_code):
            command = bf_code[self.pc]

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
                self.memory[self.pointer] = ord(
                    input('Input a character: ')[0])
            elif command == "[":
                if self.memory[self.pointer] == 0:
                    self._jump_forward(bf_code)
            elif command == "]":
                if self.memory[self.pointer] != 0:
                    self._jump_backward(bf_code)

            self.pc += 1

        return "".join(self.output)

    def _jump_forward(self, bf_code):
        """
        Jump past the matching closing bracket
        closing bracket: ']'
        """
        open_bracket = 1
        while open_bracket != 0:
            self.pc += 1
            if bf_code[self.pc] == "[":
                open_bracket += 1
            elif bf_code[self.pc] == "]":
                open_bracket -= 1

    def _jump_backward(self, bf_code):
        """
        Jump back to the matching opening bracket
        opening bracket: ']'
        """
        close_bracket = 1
        while close_bracket != 0:
            self.pc -= 1
            if bf_code[self.pc] == "]":
                close_bracket += 1
            elif bf_code[self.pc] == "[":
                close_bracket -= 1