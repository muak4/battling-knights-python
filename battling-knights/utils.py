import sys

from game_init import KStatus, knights, items


def read_moves_file(filename):
    """
    Reads moves from a file and returns them as a list, excluding "GAME-START" and "GAME-END" markers.

    Parameters:
        filename (str): The name of the file containing the moves.

    Returns:
        list: A list containing all moves from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        moves = []
        with open(filename) as file:
            for line in file:
                if line.strip() not in ["GAME-START", "GAME-END"]:
                    moves.append(line.strip())
        return moves
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


def get_knight_from_move(move_symbol):
    """
    Retrieves the knight object corresponding to the given move symbol.

    Parameters:
        move_symbol (str): The symbol of the knight to be retrieved.

    Returns:
        Knight or None: The knight object corresponding to the move symbol, or None if not found.
    """
    return next((knight for knight in knights if knight.symbol == move_symbol), None)


def get_item_from_symbol(item_symbol):
    """
    Retrieves the item object corresponding to the given symbol.

    Parameters:
        item_symbol (str): The symbol of the item to be retrieved.

    Returns:
        Item or None: The item object corresponding to the symbol, or None if not found.
    """
    return next((item for item in items if item.symbol == item_symbol), None)


def get_item_name(item_symbol):
    """
    Retrieves the name of the item corresponding to the given symbol.

    Parameters:
        item_symbol (str): The symbol of the item whose name is to be retrieved.

    Returns:
        str: The name of the item corresponding to the symbol, or None if not found.
    """
    item = get_item_from_symbol(item_symbol)
    return item.name if item else None


def write_json_file(result):
    """
    Writes the given dictionary to a JSON file.

    Parameters:
        result (dict): The dictionary to be written to the JSON file.

    Returns:
        str: The JSON content written to the file.
    """
    json_output = '{\n'
    for i, (key, value) in enumerate(result.items()):
        json_output += f'    "{key}": {value}'
        if i < len(result) - 1:
            json_output += ','
        json_output += '\n'
    json_output += '}'

    with open('game_board.json', 'w') as f:
        f.write(json_output)

    return json_output


def is_valid_move(knight, move):
    """
    Checks if the given move is valid for the knight.

    Parameters:
        knight (Knight): The knight object.
        move (str): The move symbol.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    valid_moves = ['N', 'S', 'E', 'W']
    return knight is not None and move in valid_moves and knight.k_status == KStatus.LIVE
