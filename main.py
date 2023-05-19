import tkinter as tk
import random
#from time import time

#timeGame = time()

def start_game():
	window = tk.Tk()
	window.title('Пятнашки')
	global board
	board = create_board()
	
	global buttons
	buttons = [[0] * 4 for _ in range(4)]
	for i in range(4):
		for j in range(4):
			button = tk.Button(window, width=4, height=2, font=('Arial', 20, 'bold'), command=lambda row=i, col=j: get_move(row, col))
			button.grid(row=i, column=j)
			buttons[i][j] = button
	global message
	message = tk.Label(window, text='', font=('Arial', 14))
	message.grid(row=4, column=0, columnspan=4)

	update_board()

	window.mainloop()


# создаем игровое поле
def create_board():
	board = [[0] * 4 for _ in range(4)]
	nums = list(range(1, 16))
	random.shuffle(nums)
	while is_solved(nums):
		random.shuffle(nums)
	nums_iter = iter(nums)
	for i in range(4):
		for j in range(4):
			if i != 3 or  j != 3:
				board[i][j] = next(nums_iter)
			else:
				continue
	board[3][3] = 0
	return board


# обновляем интерфейс
def update_board():
	for i in range(4):
		for j in range(4):
			if board[i][j] != 0:
				buttons[i][j].config(text=str(board[i][j]))
			else:
				buttons[i][j].config(text='')
	if is_win():
		for i in range(4):
			for j in range(4):
				buttons[i][j].config(state='disabled')
		#message.config(text="Вы победили!" + "Ваше время " + str(int(timeGame = time())) + " сек.")
		message.config(text="Вы победили!")
#проверка на собираемость
def is_solved(nums):
	tmp = 0
	for i in range(len(nums)):
		if nums[i]:
			for j in range(i):
				if nums[j] > nums[i]:
					tmp += 1
	for i in range(len(nums)):
		if nums[i] == 0:
			tmp +=1 + i//4
	return tmp%2

# получаем ход пользователя
def get_move(row, col):
	for i in range(4):
		for j in range(4):
			if board[i][j] == 0:
				if (row == i and abs(col - j) == 1) or (col == j and abs(row - i) == 1):
					board[i][j], board[row][col] = board[row][col], board[i][j]
					update_board()


#проверка победы
def is_win():
	nums = list(range(1, 16))
	nums.append(0)
	flat_board = [num for row in board for num in row]
	return flat_board == nums


start_game()

