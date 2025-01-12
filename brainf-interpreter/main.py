import sys

class BrainF:
    def __init__(self, code=None):
        self.code = code

    def brainf_repl(self):
        self.code = sys.argv[1]
        try:
            with open(self.code, "r") as file:
                content = file.readlines()
            print("".join(content))
        except FileNotFoundError:
            print(f"File {self.code} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

bf = BrainF()
bf.brainf_repl()