#!/usr/bin/env python3

# Test implementation of the holish calculator
# Proof of concept for the holish philosophy
# It's my first time using python so it's probably crap

# Colors definitions
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
RESET = "\033[0;0m"
# TODO: Find a way to make readonly variables like with bash's `declare -r`

# User input
print(f"{YELLOW} Asking for user input{RESET}")
full_command = input()
print(f"{PURPLE}DEBUG: Full command: {RESET} {full_command}")

# Tokenization
print(f"{YELLOW} Splitting the input{RESET}")
tokens = full_command.split()
print(f"{PURPLE}DEBUG: tokens: {RESET} {tokens}")

# Test enumerate
print(f"{YELLOW} Enumerate test{RESET}")
for i, t in enumerate(tokens, start=1):
	print(f"{PURPLE}DEBUG:{RESET} {i}:{t}")
# That block is useless it's only there to help me understand better how things work

# Make an empty table
print(f"{YELLOW} Making token table{RESET}")
token_table = []

# Assign a number id to each token to preserve the order
for token_id, token_str in enumerate(tokens, start=1):
	token_type = "unknown"
	token_subtype = "unknown"
	# Determine the type and subtype of the token and add it to the table
	if token_str in ("+", "-", "*", "/"):
		token_type = "operator"
		if token_str == "+":
			token_subtype = "add"
		elif token_str == "-":
			token_subtype = "sub"
		elif token_str == "*":
			token_subtype = "mul"
		elif token_str == "/":
			token_subtype = "div"
	elif token_str.startswith("--"):
		token_type = "flag"
		if token_str.startswith("--output="):
			token_subtype = "output_flag"
		elif token_str.startswith("--input="):
			token_subtype = "operand_input_flag"
		elif token_str.startswith("--global-input="):
			token_subtype = "global_input_flag"
		elif token_str.startswith("--input-output="):
			token_subtype = "io_flag"
	else:
		token_type = "operand"
	# Build the table
	row = {
		"token_id": token_id,
		"token_str": token_str,
		"token_type": token_type,
		"token_subtype": token_subtype
	}
	token_table.append(row)

print(f"{PURPLE}DEBUG: token_id: {RESET} {token_id}")
print(f"{PURPLE}DEBUG: token_table: {RESET}")
for row in token_table:
	print(f"Index: {row['token_id']}, Token: {row['token_str']}, Type: {row['token_type']}, Subtype: {row['token_subtype']}")

# TODO: Attach input flags to the preceeding operand with token_id = n-1
# TODO: Deal with flags precedence in the override chain
	# io_flag > global_input_flag > operand_input_flag
	# io_flag > output_flag
# TODO: Convert operands from strings into floats for calculation
	# Can't be bothered to deal with both integers and floats separately and mixing them so everything will be floats
# TODO: Apply input flags to operands
# TODO: Get the new value for the operands after taking the input flags into account
	# Make sure it works for floats, like `2.a --input=hex`
# TODO: Execute calculation
	# No operator precedence: calculations are done exactly as entered, strictly from left to right, unless parenthesis are used to explicitely group operations.
	# See PHILOSOPHY section in the README.
# TODO: Get result of calculation
# TODO: Apply output flag to the result
# TODO: Display the result in the requested base

# TODO LATER: Deal with spaces inside operands. And special characters.
	# Invalid characters in the operands shouldn't break the lexer.
	# Maybe force quotes around operands for now?
	# But what if there's an escaped quote inside the operand?
	# Got a headache now. Need shell-like quoting rules.

# TODO LATER: Detect short flags: `-x whatever`
	# Problem: `--input=bin` is one token but `-i bin` is two tokens
	# Maybe add `=` as separator so every flag is separated in two tokens instead? But then what if `=` is inside an operand?
	# Can't be bothered I'll just use long flags for now
