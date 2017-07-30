def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if is_spare(game, i):
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and (is_spare or is_strike):
            result = spare_or_strike(game, i, result)
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if is_strike(game, i):
            in_first_half = True
            frame += 1
    return result


def spare_or_strike(game, i, result):
    if is_spare(game, i):
        result += spare(game, i)
    elif is_strike(game, i):
        result += spare(game, i)
        if is_spare(game, i + 2):
            result += 10 - spare(game, i)
        else:
            result += get_value(game[i + 2])
    return result


def get_value(char):
    if char.isdigit():
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def spare(game, i):
    return get_value(game[i + 1])


def is_strike(game, i):
    if game[i] == 'X' or game[i] == 'x':
        return True
    return False


def is_spare(game, i):
    if game[i] == '/':
        return True
    return False

# print(score("1/35XXX458/X3/23"))
