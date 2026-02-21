from stack import create_stack, push, pop, is_empty


def read_input_file(file_name: str):
    """
    Reads the input text file and constructs the input stack.

    The file contains one symbol per line.
    Symbols are read from top to bottom and pushed as read.
    Therefore, the last line of the file becomes the top of the stack.

    Parameter:
    - file_name (string): Path to input text file.

    Returns:
    - input_stack (dict): Stack populated with input symbols.
    """
    input_stack = create_stack()

    # TODO:
    # - Open the file
    # - Read line by line
    # - Strip whitespace
    # - Push each symbol onto input_stack
    with open(file_name, 'r') as file:
        for line in file:
            symbol = line.strip()
            if symbol:
                push(input_stack, symbol)

    return input_stack


def normalize_stream(input_stack, buffer_stack):
    """
    Normalizes a stream of symbols using stack-based logic.

    Parameters:
    - input_stack: Stack containing input symbols (top processed first)
    - buffer_stack: Empty stack used to store completed blocks

    Returns:
    - A string representing the normalized stream, where blocks are
      separated by a single space.
    """

    # Indicates whether the system is frozen
    frozen = False

    # Stack representing the current block being built
    current_block = create_stack()

    # --------------------
    # Process input symbols
    # --------------------
    while not is_empty(input_stack):
        symbol = pop(input_stack)

        # TODO:
        # If symbol is a data symbol (A–Z),
        # push it onto current_block
        if symbol >= 'A' and symbol <= 'W':
            push(current_block, symbol)

        # TODO:
        # If symbol is a control symbol (X, Y, Z):
        #   1. End the current block if it is non-empty
        #   2. Apply the control operation according to the rules
        #   3. Update frozen state if needed
        # If symbol is a data symbol (A-W)

        else:
            # every control symbol ends the current block first
            if not is_empty(current_block):
                push(buffer_stack, current_block)
            current_block = create_stack()

            if symbol == 'Z':
                # freeze the system, X and Y won't work after this
                frozen = True
            elif symbol == 'X' and not frozen:
                # throw away the most recent block
                if not is_empty(buffer_stack):
                    pop(buffer_stack)
            elif symbol == 'Y' and not frozen:
                # make a copy of the most recent block
                if not is_empty(buffer_stack):
                    # access the top block without removing it
                    original = buffer_stack["data"][buffer_stack["top"]]
                    temp = create_stack()
                    duplicate = create_stack()
                    # empty original into temp to reverse the order
                    while not is_empty(original):
                        push(temp, pop(original))
                    # refill original and build duplicate at the same time
                    while not is_empty(temp):
                        sym = pop(temp)
                        push(original, sym)
                        push(duplicate, sym)

                    push(buffer_stack, duplicate)

    # --------------------
    # Finalize last block
    # --------------------
    # TODO:
    # If current_block is non-empty, push it onto buffer_stack
    if not is_empty(current_block):
        push(buffer_stack, current_block)

    # --------------------
    # Build output
    # --------------------
    # TODO:
    # Pop blocks from buffer_stack.
    # For each block, pop all symbols and append them to the output.
    # Separate blocks using a single space.
    output = ""
    first_block = True
    # Pop blocks from buffer_stack and process each
    while not is_empty(buffer_stack):
        block = pop(buffer_stack)
        if not first_block:
            output += " "
        first_block = False
        # Pop symbols from block and append to output
        while not is_empty(block):
            output += pop(block)

    return output


def main(file_name: str) -> None:
    """
    Extracts all input from the input text file and performs stream normalization.

    Workflow:
    - Reads the input file and constructs the input stack
    - Creates an empty buffer stack
    - Calls normalize_stream(...) to process the stream
    - Prints the final normalized output

    Parameter(s):
    - file_name (string): Path to input text file.

    Returns:
    - None
    """

    input_stack = read_input_file(file_name)
    buffer_stack = create_stack()

    normalized_output = normalize_stream(input_stack, buffer_stack)
    return normalized_output


# Initiates the program by calling main function.
if __name__ == "__main__":
    print(main('./inputs/test1.txt'))
