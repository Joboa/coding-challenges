import sys
import time
import os
import psutil
from interpreter import BrainFInterpreter


class BrainF:
    def __init__(self, bf_code=None):
        self.bf_code = bf_code
        self.interpreter = BrainFInterpreter()

    def brainf_repl(self):
        if len(sys.argv) < 2:
            print("Error!")
            print("usage: python main.py <filename.bf>")
            return

        self.bf_code = sys.argv[1]
        try:
            with open(self.bf_code, "r") as file:
                content = file.read()

                process = psutil.Process(os.getpid())

                start_time = time.time()
                start_resource_usage = process.cpu_times()

                result = self.interpreter.interpret(content)

                end_resource_usage = process.cpu_times()
                end_time = time.time()

                user_time = end_resource_usage.user - start_resource_usage.user
                system_time = end_resource_usage.system - start_resource_usage.system
                execution_time = end_time - start_time
                cpu_percent = ((user_time + system_time) /
                               execution_time) * 100

                print("\nOutput: ", result)
                print(
                    f"{user_time:.2f}s user {system_time:.2f}s system {cpu_percent:.0f}% cpu {execution_time:.3f} total"
                )

        except FileNotFoundError:
            print(f"File {self.bf_code} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


bf = BrainF()
bf.brainf_repl()
