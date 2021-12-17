import random
def print_table(cell: list):
    """Данная функция производит печать таблицы размером 5x5

    cell -- массив длиной 25, обозначающий таблицу"""

    print("+------+------+------+------+------+")
    print('| ', cell[0], ' | ', cell[1], ' | ', cell[2], ' | ', cell[3], ' | ', cell[4], )
    print("+------+------+------+------+------+")
    print('| ', cell[5], ' | ', cell[6], ' | ', cell[7], ' | ', cell[8], ' | ', cell[9], )
    print("+------+------+------+------+------+")
    print('| ', cell[10], ' | ', cell[11], ' | ', cell[12], ' | ', cell[13], ' | ', cell[14], )
    print("+------+------+------+------+------+")
    print('| ', cell[15], ' | ', cell[16], ' | ', cell[17], ' | ', cell[18], ' | ', cell[19], )
    print("+------+------+------+------+------+")
    print('| ', cell[20], ' | ', cell[21], ' | ', cell[22], ' | ', cell[23], ' | ', cell[24], )
    print("+------+------+------+------+------+")


def validation(reply: str, cell: list):
    """Данная функция проверяет корректность сделанного игроком хода

    reply -- сделанный игроком ход
    cell -- массив длиной 25, обозначающий таблицу"""

    if reply == 'a' and cell[4] != '  ' and cell[9] != '  ' and cell[14] != '  ' and cell[19] != '  'and cell[24] != '  ':
        return True
    elif reply == 's' and cell[0] != '  ' and cell[1] != '  ' and cell[2] != '  ' and cell[3] != '  'and cell[4] != '  ':
        return True
    elif reply == 'd' and cell[0] != '  ' and cell[5] != '  ' and cell[10] != '  ' and cell[15] != '  'and cell[20] != '  ':
        return True
    elif reply == 'w' and cell[20] != '  ' and cell[21] != '  ' and cell[22] != '  ' and cell[23] != '  'and cell[24] != '  ':
        return True
    else:
        return False


def cell_movement(reply: str, cell: list):
    """Данная функция передвигает ячейку в соответствии со сделанным ходом

    reply -- сделанный игроком ход
    cell -- массив длиной 25, обозначающий таблицу"""

    global index
    if reply == 'a':
        cell[index], cell[index + 1] = cell[index + 1], cell[index]
        index = index + 1
    elif reply == 's':
        cell[index], cell[index - 5] = cell[index - 5], cell[index]
        index = index - 5
    elif reply == 'd':
        cell[index], cell[index - 1] = cell[index - 1], cell[index]
        index = index - 1
    elif reply == 'w':
        cell[index], cell[index + 5] = cell[index + 5], cell[index]
        index = index + 5
    return cell

def print_new_table():
    """Данная функция создает новую таблицу и перемешивает в ней ячейки рандомным образом"""

    global index
    cell = list(range(1, 26))
    for i in range(24):
        if cell[i] < 10:
            cell[i] = ' ' + str(cell[i])  # Идёт добавление пробелов в случае чисел, которые меньше 10 для печати ровной таблицы
        else:
            cell[i] = str(cell[i])
    cell[24] = '  '
    for i in range(200): #перемешивание ячеек рандомным образом, а также создание ограничений на перемешивание
        if cell[0] == '  ':
            random_move = random.choice(['a', 'w'])
        elif cell[4] == '  ':
            random_move = random.choice(['d', 'w'])
        elif cell[24] == '  ':
            random_move = random.choice(['d', 's'])
        elif cell[20] == '  ':
            random_move = random.choice(['a', 's'])
        elif cell[1] == '  ' or cell[2] == '  ' or cell[3] == '  ':
            random_move = random.choice(['a', 'w', 'd'])
        elif cell[21] == '  ' or cell[22] == '  ' or cell[23] == '  ':
            random_move = random.choice(['a', 'd', 's'])
        elif cell[9] == '  ' or cell[14] == '  ' or cell[19] == '  ':
            random_move = random.choice(['w', 'd', 's'])
        elif cell[5] == '  ' or cell[10] == '  ' or cell[15] == '  ':
            random_move = random.choice(['a', 's', 'w'])
        else:
            random_move = random.choice(['a', 's', 'd', 'w'])
        cell = cell_movement(random_move, cell)
    return cell

def start():
    """Данная функция предоставляет игроку выбор и объясняет правила игры"""

    print('''Нажмите 1, чтобы играть в интересные пятнашки \n введите "exit", чтобы выйти из игры''')
    a = input()
    while a != '1' and a != 'exit':
        print('Можно вводить только 1 или "exit"')
        a = input()
    else:
        if a == '1':
            a = 'Интересные пятнашки'
            print('''Вы выбрали игру "Интересные пятнашки". 
Ваша задача - перемещая ячейки с цифрами, добиться упорядочивания их по номерам(нижняя правая клетка должна быть пустая)\n''')
        else:
            a = 'exit'
            print('Вы вышли из игры')
            return a
        print('''Чтобы передвинуть на пустое место ячейку сверху - нажмите "s",
чтобы передвинуть на пустое место ячейку слева - нажмите "d",
чтобы передвинуть на пустое место ячейку снизу - нажмите "w",
чтобы передвинуть на пустое место ячейку справа - нажмите "a",
чтобы выйти из игры введите "exit"''')
        return a


def impossible():
    """Данная функция оповещает игрока о том, что такой ход сделать нельзя
       и печатает все возможные варианты хода"""

    print('Невозможно сделать такой ход!')
    print('''Чтобы передвинуть на пустое место ячейку сверху - нажмите "s",
чтобы передвинуть на пустое место ячейку слева - нажмите "d",
чтобы передвинуть на пустое место ячейку снизу - нажмите "w",
чтобы передвинуть на пустое место ячейку справа - нажмите "a",
чтобы выйти из игры введите "exit"''')


if __name__ == '__main__':

    win24 = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10',
             '11', '12', '13', '14', '15',' 16', ' 17', '18', ' 19', '20', '21', '22', '23', '24', '  ']
    losing24 = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10',
                '11', '12', '13', '14', '15', ' 16', ' 17', '18', ' 19', '20', '21', '22', '24', '23', '  ']
    index = 24
    cell = print_new_table()
    start_game = start()
    reply = ''


    while True:

        if start_game == 'exit': break
        print_table(cell)
        reply = input()

        if reply == 'exit': break
        if validation(reply, cell):
            cell = cell_movement(reply, cell)
        else:
            impossible()

        if win24 == cell:
            print_table(cell)
            print("Вы победили!")
            start_game = start()
            if start_game == "exit": break
            table = print_new_table()

        if losing24 == cell:
            print_table(cell)
            print("Вы проиграли!")
            start_game = start()
            if start_game == "exit": break
            table = print_new_table()