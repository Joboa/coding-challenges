import sys
import time
import os
import psutil
from src.ccbf.interpreter import BrainFInterpreter


class BrainF:
    def __init__(self) -> None:
        self.interpreter: BrainFInterpreter = BrainFInterpreter()

    def execute_code(self, bf_code: str) -> str:
        """Execute BrainF code and print performance metrics"""
        process = psutil.Process(os.getpid())

        start_time: float = time.time()
        start_resource_usage: float = process.cpu_times()

        try: 
            result: str = self.interpreter.interpret(bf_code)
        except Exception as e:
            print(f"Error executing BrainF code: {type(e).__name__}: {e}")

        end_resource_usage: float = process.cpu_times()
        end_time: float = time.time()

        user_time: float = end_resource_usage.user - start_resource_usage.user
        system_time: float = end_resource_usage.system - start_resource_usage.system
        execution_time: float = end_time - start_time

        # Prevent division by zero
        if execution_time == 0:
            execution_time = 1e-9

        cpu_percent: float = ((user_time + system_time) /
                              execution_time) * 100

        print("\nOutput: ", result)
        print(
            f"{user_time:.2f}s user {system_time:.2f}s system {cpu_percent:.0f}% cpu {execution_time:.3f} total"
        )

    def run_file(self, filename: str) -> None:
        """
        Run BrainF code from a file
        Args:
            filename (str): Path to the brainf source file
        """
        try:
            with open(filename, "r") as file:
                content: str = file.read()
            self.execute_code(content)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error reading file: {type(e).__name__}: {e}")

    def run_repl(self):
        """Interactive REPL mode for BrainF"""
        print("Welcome to Custome Command BrainF (CCBF)")
        print("Type 'exit' or 'quit' to exit the REPL")

        while True:
            try:
                user_input: str = input("CCBF> ")

                if user_input.lower() in ["exit", "quit"]:
                    break
                if not user_input.strip():
                    continue

                self.execute_code(user_input)
            except KeyboardInterrupt:
                print("\nUse 'exit' or 'quit' to leave the REPL")
            except Exception as e:
                print(f"Error in repl: {e}")


def main() -> None:
    """Main entry point for the interpreter"""
    bf: BrainF = BrainF()
    if len(sys.argv) == 2:
        bf.run_file(sys.argv[1])
    else:
        bf.run_repl()


if __name__ == "__main__":
    main()
