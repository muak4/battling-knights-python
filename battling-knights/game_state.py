from game_init import KStatus, knights, items
from utils import get_item_name, get_item_from_symbol, get_knight_from_move


def update_board():
    """
    Prints the game board with the positions of items and knights.

    Returns:
        None
    """
    board = [[' ' for _ in range(8)] for _ in range(8)]

    for item in items:
        if item.holder is None:
            board[item.position[0]][item.position[1]] = item.symbol

    for knight in knights:
        if knight.k_status == KStatus.LIVE:
            board[knight.position[0]][knight.position[1]] = knight.symbol

    print("   0   1   2   3   4   5   6   7")
    print("  |---|---|---|---|---|---|---|---|")
    for i in range(8):
        print(f"{i} | {' | '.join(board[i])} | {i}")
        print("  |---|---|---|---|---|---|---|---|")
    print("   0   1   2   3   4   5   6   7")


def generate_final_result():
    """
    Generates the final result dictionary containing information about knights and items.

    Returns:
        dict: A dictionary containing the final result.
    """
    final_result = {}

    for symbol, knight_color in {"R": "red", "B": "blue", "G": "green", "Y": "yellow"}.items():
        knight = get_knight_from_move(symbol)
        final_result[knight_color] = [
            knight.position,
            knight.k_status.name,
            get_item_name(knight.item) if knight.item else None,
            int(knight.a_score),
            knight.d_score
        ]

    for item_symbol, item_name in {"A": "axe", "D": "dagger", "H": "helmet", "M": "magic_staff"}.items():
        item = get_item_from_symbol(item_symbol)
        final_result[item_name] = [
            item.position,
            bool(item.holder)
        ]

    return final_result
