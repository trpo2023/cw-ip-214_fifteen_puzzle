import tkinter as tk
import random

# создаем игровое поле
def create_board():
	board = [[0] * 4 for _ in range(4)]
	nums = list(range(1, 16))
	random.shuffle(nums)
	nums_iter = iter(nums)
	for i in range(4):
		for j in range(4):
			if i == j == 3:
				board[i][j] = ''
			else:
				board[i][j] = next(nums_iter)
	return board

# обновляем интерфейс
def update_board():
	for i in range(4):
		for j in range(4):
			if board[i][j] != '':
				buttons[i][j].config(text=str(board[i][j]))
			else:
				buttons[i][j].config(text='')

# получаем ход пользователя
def get_move(row, col):
	for i in range(4):
		for j in range(4):
			if board[i][j] == '':
				if (row == i and abs(col - j) == 1) or (col == j and abs(row - i) == 1):
					board[i][j], board[row][col] = board[row][col], board[i][j]
					update_board()
					return

# создаем окно и игровое поле
root = tk.Tk()
root.title('Пятнашки')

board = create_board()

buttons = [[0] * 4 for _ in range(4)]
for i in range(4):
	for j in range(4):
		button = tk.Button(root, width=4, height=2, font=('Arial', 20, 'bold'), command=lambda row=i, col=j: get_move(row, col))
		button.grid(row=i, column=j)
		buttons[i][j] = button

message = tk.Label(root, text='', font=('Arial', 14))
message.grid(row=4, column=0, columnspan=4)

update_board()

root.mainloop()
