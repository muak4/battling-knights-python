from game_init import KStatus, knights, items
from game_state import update_board
from utils import is_valid_move, get_item_from_symbol, get_knight_from_move


def move_knight(move):
    """
    Moves a knight based on the provided move.

    Parameters:
        move (str): A string representing the move in the format "<knight_symbol>:<move_symbol>".

    Returns:
        None
    """
    knight_mover, move_symbol = get_move_and_knight_symbols(move)

    if is_valid_move(knight_mover, move_symbol):
        last_position = knight_mover.position[:]
        knight_mover = update_position(knight_mover, move_symbol)

        print("***************************************")
        print(f'{knight_mover.name} moves to {tuple(knight_mover.position)}')
        # print_with_separator(f'{knight_mover.symbol} moves to {knight_mover.position}')

        after_move_changes(knight_mover, last_position)
        print("***************************************")
    else:
        print("Invalid Move")

    update_board()


def after_move_changes(mover_knight, position):
    """
    Handles all the expected operation that may happen after Knight make a move.
    Case 1: Check if the knight is drowned
    Case 2: Check if the knight moves on the item tile.
    Case 3: Check if the knight moves on a tile where already knight is present.

    Parameters:
        mover_knight (Knight): The knight object to be updated with the new position.
        position (list): The new position of the item.

    Returns:
        None
    """
    if is_knight_drowned(mover_knight):
        print(f'{mover_knight.name} is Drowned')
        if mover_knight.item is not None:
            print(f'{get_item_from_symbol(mover_knight.item).name} is thrown to the '
                  f'bank at position: {tuple(mover_knight.position)}')
            reset_knight_item(mover_knight, position)
        update_status_and_knight_score(mover_knight, KStatus.DROWNED)
        print(f'{mover_knight.name} Score(Attack/Defence): {mover_knight.a_score}/{mover_knight.d_score}')
        mover_knight.position = None

    for item in items:
        if item.position == mover_knight.position and item.holder is None:
            if mover_knight.item is None:
                update_knight_item_and_score(item, mover_knight)
                print(f'{mover_knight.name} picked a {item.name}')
                print(f'{mover_knight.name} Score(Attack/Defence): {mover_knight.a_score}/{mover_knight.d_score}')
            else:
                if get_item_from_symbol(item.symbol).p_value > get_item_from_symbol(mover_knight.item).p_value:
                    reset_knight_item(mover_knight, mover_knight.position[:])
                    update_status_and_knight_score(mover_knight, KStatus.LIVE)
                    update_knight_item_and_score(item, mover_knight)
                    print(f'{mover_knight.name} replaced existing item with {item.name}')
                    print(f'{mover_knight.name} Score(Attack/Defence): {mover_knight.a_score}/{mover_knight.d_score}')

    for knight in knights:
        if knight.symbol != mover_knight.symbol and knight.position == mover_knight.position and knight.k_status is KStatus.LIVE:
            print(f'{mover_knight.name} is ready for Surprise Attack')
            mover_knight.a_score += 0.5

            print(f'Attacker knight({mover_knight.name}), attack score is {mover_knight.a_score}')
            print(f'Defender knight({knight.name}), defence score is {knight.d_score}')

            if mover_knight.a_score > knight.d_score:
                print(f'Defender Knight({knight.name}), is Dead')
                update_status_and_knight_score(knight, KStatus.DEAD)
                if knight.item is not None:
                    print(f'Defender Knight dropped {get_item_from_symbol(knight.item).name} at position {tuple(knight.position[:])}')
                    reset_knight_item(knight, knight.position[:])

            else:
                print(f'Attacker Knight({mover_knight.name}), is Dead')
                update_status_and_knight_score(mover_knight, KStatus.DEAD)
                if mover_knight.item is not None:
                    print(f'Attacker Knight dropped {get_item_from_symbol(mover_knight.item).name} at position {tuple(mover_knight.position[:])}')
                    reset_knight_item(mover_knight, mover_knight.position[:])

            mover_knight.a_score -= 0.5 if mover_knight.a_score > 0 else 0


def get_move_and_knight_symbols(move):
    """
    Extracts the move symbol and corresponding knight symbol from the given move string.

    Parameters:
        move (str): The move string in the format "<knight>:<move_symbol>".
                    Example: "Red:N"

    Returns:
        tuple: A tuple containing the knight symbol and the move symbol extracted from the move string.
    """
    return get_knight_from_move(move.split(':')[0]), move.split(':')[1]


def update_position(knight, move):
    """
    Update the position of a knight based on a given move symbol.

    Parameters:
        knight (Knight): The knight object whose position is to be updated.
        move (str): The move symbol indicating the direction of movement.
                    Valid symbols are 'S' (South), 'N' (North), 'E' (East), 'W' (West).

    Returns:
        Knight: The updated knight object.

    Note:
        If the move symbol is invalid, an error message is printed and the knight's position remains unchanged.
    """
    moves = {'S': (1, 0), 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1)}

    if move in moves:
        position_x, position_y = moves[move]
        knight.position[0] += position_x
        knight.position[1] += position_y
    else:
        print("Invalid Move Symbol")

    return knight


def is_knight_drowned(knight):
    """
    Checks if a knight has drowned based on its current position.

    Parameters:
        knight (Knight): The knight object to check.

    Returns:
        bool: True if the knight has drowned (i.e., if its position is outside the 8x8 game board),
              False otherwise.
    """
    x, y = knight.position
    return not (0 <= x <= 7 and 0 <= y <= 7)


def update_status_and_knight_score(knight, status):
    """
    Updates the status of a knight and resets its scores based on the new status.

    Parameters:
        knight (Knight): The knight object whose status and scores are to be updated.
        status (KStatus): The new status of the knight.

    Returns:
        None
    """
    knight.a_score = 1 if status == KStatus.LIVE else 0
    knight.d_score = 1 if status == KStatus.LIVE else 0
    knight.k_status = status


def reset_knight_item(knight, position):
    """
    Resets the item held by a knight and updates its position in the game.

    Parameters:
        knight (Knight): The knight object whose item is to be reset.
        position (list): The new position of the item.

    Returns:
        None
    """
    item = get_item_from_symbol(knight.item)
    item.holder = None
    item.position = position
    knight.item = None


def update_knight_item_and_score(item, knight):
    """
    Updates the item held by a knight and adjusts its scores accordingly.

    Parameters:
        item (Item): The item object to be held by the knight.
        knight (Knight): The knight object to be updated with the new item.

    Returns:
        None
    """
    knight.item = item.symbol
    item.holder = knight.symbol
    item.position = knight.position
    knight.a_score += item.a_stat
    knight.d_score += item.d_stat
