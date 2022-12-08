board = list(range(1, 10))
combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# дисплей
def d_board():
   print("-------------")
   for i in range(3):
      print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
   print("-------------")


# выбор ячейки
def meaning(number):
   while True:
      a = input(f"Выбери номер ячейки  {number}:")
      if not (a in "123456789"):
         print("Введена несуществующая ячейка, повторите попытку...")
         continue
      a = int(a)
      if str(board[a - 1]) in "OX":
         print("Клетка уже занята")
         continue
      board[a - 1] = number
      break


def WoL():
   for n in combinations:
      if (board[n[0] - 1]) == (board[n[1] - 1]) == (board[n[2] - 1]):
         return board[n[1] - 1]
   else:
      return False


def main():
   cou = 0
   while True:
      d_board()
      if cou % 2 == 0:
         meaning('X')
      else:
         meaning('O')
      if cou > 3:
         winner = WoL()
         if winner: d_board()
         print(f'{winner} победил!')
         break
      cou += 1
      if cou > 8:
         d_board()
         print('0X Ничья 0X')
         break


main()