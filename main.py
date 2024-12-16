#!/usr/bin/env python3
import sys
import re
from SudoLangADT import *  # ADT definitions
import sudolang  # Import lexer and parser specifications from sudolang
from interpreter import eval_program  # Evaluation function

# A dictionary to store variables and their values
variables = {}
context = []
markers = {}
translated_string = ""

def concrete2abstract(s: str, parser) -> Program:
    """
    Convert a concrete program (string) into an abstract syntax tree (ADT).
    """
    try:
        # Use the parser to parse the string
        parser.parse(s)
        return sudolang.global_ast  # Assuming the parser stores the result in global_ast
    except Exception as e:
        print("Unknown Error occurred (this is normally caused by a syntax error)")
        raise e
    return None

def process_input(input_string):
    """
    Process the input (either from REPL or file) and evaluate.
    """
    # Skip blank lines
    if input_string.strip() == "" or input_string.strip().startswith('#'):
        return  # Skip blank lines
    
    # Parse the input string into the ADT
    ast = concrete2abstract(input_string, sudolang.parser)

    if ast:
        # Interpret the program and update variables
        result = eval_program(ast, variables, context)
        if result == False or result:
            print(result)
    else:
        print(f'"{input_string}" is not a valid program.')

def start_repl(first=True, filename=None):
    if first:
        print("Welcome to the SudoLang Interpreter!")
        print("Type 'exit' to quit.")
    
    # If a file is provided, read the file's content
    if filename:
        with open(filename, 'r') as file:
            content = file.read()
            process_input(content)
        # If in -i mode, after the file is executed, show the prompt
        if '-i' in sys.argv:
            print()
            start_repl(first=False)
        return  # Exit after processing the file if -i isn't set
    
    while True:
        try:
            # Collect multi-line input
            input_lines = []
            indent_level = 0
            inConditional = False
            
            while True:
                # Determine the prompt based on indent level
                #prompt = f"--[ {'  ' * indent_level}"
                prompt = f"--[ "
                
                # Get user input
                try:
                    line = input(prompt)

                except EOFError:
                    # Allow Ctrl+D to submit input
                    print("\nExiting SudoLang.")
                    exit()
                
                # Empty line signals end of input
                if line.strip() == "":
                    break

                if not line.startswith(('else', 'if', ' ')) and inConditional:
                    process_input(line)
                    break

                if line.lower() == 'exit':
                    print("\nExiting SudoLang.")
                    exit()
                
                # Check for lines that increase indent level
                if line.strip().endswith('then'):
                    indent_level += 1
                    inConditional = True

                elif not inConditional:
                    process_input(line)
                    break

                
                # Check for lines that decrease indent level
                # Note: you might want to expand this list based on your language syntax
#                if line.strip().startswith(('else')):
#                    indent_level = max(0, indent_level - 1)
                
                input_lines.append(line)
            
            # Join the lines
            input_string = '\n'.join(input_lines)
            
            # Process the input
            process_input(input_string)
        
        except KeyboardInterrupt:
            # Handle Ctrl+C: Cancel current input and continue the loop
            print()
            continue
        
        except EOFError:
            # Handle Ctrl+D: Exit the REPL
            print("\nExiting SudoLang.")
            break
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Check if '-i' is in sys.argv for interactive mode
    if '-i' in sys.argv:
        # If there's a filename provided along with -i, process the file first, then start REPL
        if len(sys.argv) > 2:
            filename = sys.argv[2]
            start_repl(first=False, filename=filename)
        else:
            # If only -i is provided (no filename), start the REPL immediately
            start_repl(first=True)
    else:
        # If no '-i', just process the filename and exit
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            start_repl(first=False, filename=filename)
        else:
            # If no arguments, run in interactive mode
            start_repl(first=True)
