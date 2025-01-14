# --- Coding Challenge #81 - BrainF Interpreter --- 
The challenge is to build my own Brainf Interpereter which is an esoteric programming language created by Urban Muller in 1993. This challenge is part of John Crickett's weekly coding challenges (#81). The REPL is named custom command brainf interpreter (ccbf).

## Custom Command BrainF Interpreter (CCBF)

CCBF is a BrainF interpreter implemented in Python. This interpreter provides both a command-line interface for executing BrainF files and an interactive REPL mode for testing and experimentation.

## Features

- **File Execution**: Run BrainF programs directly from files
- **Interactive REPL**: Test and experiment with BrainF code
- **Performance Metrics**: View execution time and CPU usage statistics


## Project Structure

```
brainf-interpreter/
├── src/
│   └── ccbf/
│       ├── __init__.py
│       ├── interpreter.py  # Interpreter implementation
│       └── main.py        # CLI and REPL implementation
├── setup.py
│── README.md
│── test_case.bf # BrainF codes
```

## Installation

### Prerequisites

- Python >=3.10
- Python package installer (pip)

### Installing from Source

1. Clone the repository:
```bash
git clone https://github.com/Joboa/coding-challenges.git
cd brainf-interpreter
```

2. Install the package:
```bash
pip install -e .
```

## Usage

### Command-Line Interface

Run a BrainF file:
```bash
ccbf path/to/your/program.bf

Example: ccbf test.bf
```

Start the REPL:
```bash
ccbf

Example: CCBF> ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+++++.<<<.
```

### REPL Mode

The REPL (Read-Eval-Print Loop) provides an interactive environment for testing BrainF code:

```
Welcome to Custom Command BrainF (CCBF)
Type 'exit' or 'quit' to exit the REPL
CCBF> ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+++++.<<<.

Output: Hi
0.00s user 0.00s system 0% cpu 0.001 total
```

Commands:
- Enter BrainF code to execute it
- Type `exit` or `quit` to leave the REPL


## Technical Details

### Commands

| Character | Description |
|-----------|-------------|
| `>` | Move pointer right |
| `<` | Move pointer left |
| `+` | Increment current cell |
| `-` | Decrement current cell |
| `.` | Output current cell as ASCII |
| `,` | Input one character into current cell |
| `[` | Jump past matching `]` if current cell is 0 |
| `]` | Jump back to matching `[` if current cell is not 0 |

### Performance

The interpreter provides timing information for each execution:
- CPU time: Time spent executing instructions
- Total time: Wall clock time for execution
- CPU usage percentage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License

## Acknowledgments

- Original BrainF language by Urban Müller
- Step by step guidance by John Crickett (coding challenges guide)