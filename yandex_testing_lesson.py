def is_under_queen_attack(position, queen_position):
    if (len(position) == 2 and len(queen_position) == 2 and 'a' <= position[0] <= 'h'
            and 'a' <= queen_position[0] <= 'h' and '1' <= position[1] <= '8' and '1' <= queen_position[1] <= '8'):
        return True
    raise ValueError
