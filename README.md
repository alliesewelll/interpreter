# Core Interpreter Project Part 2
CSE 3341

Files Included
--------------
main.py
tokenizer.py
prog.py
decl_seq.py
decl.py
id_list.py
stmt_seq.py
stmt.py
assign.py
in_stmt.py
out_stmt.py
if_stmt.py
loop.py
cond.py
cmpr.py
comp_op.py
expr.py
term.py
op.py
parse_context.py
runtime_context.py
parse_utils.py

How to Run
----------
This interpreter is written in Python 3.

Run the program using:

    python3 main.py <program_file> <data_file>

Example:

    python3 main.py tests/data2.core tests/data2.txt

Program Behavior
----------------
The interpreter:
1. Reads the Core program from the first command-line argument.
2. Parses the program and checks for syntax/context-sensitive errors.
3. Pretty-prints the program if no such errors are found.
4. Executes the program using the integer data from the second command-line argument.

Input Data Format
-----------------
The data file should contain one integer per line.
Example:

    5
    10
    -3
    42

Errors Checked
--------------
Before execution begins, the interpreter checks for:
- syntax errors with respect to the Core grammar
- duplicate declarations
- undeclared variables used in the statement sequence

During execution, the interpreter checks for:
- attempting to read when the data file has no more integers
- attempting to access a variable that has not been initialized

Assumptions / Notes
-------------------
- The tokenizer, parser, pretty-printer, and executor were implemented using the object-oriented approach with separate classes corresponding to Core nonterminals.
- The interpreter follows the Core grammar discussed in class.
- Output is printed to standard output.
- Pretty-printing is indentation-based for readability.

Testing
-------
The interpreter was tested with:
- valid Core programs using assignment, read/write, if, if-else, and while
- invalid programs with syntax errors
- duplicate declaration cases
- undeclared variable cases
- runtime errors involving exhausted input data
- runtime errors involving uninitialized variables