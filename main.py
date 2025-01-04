from tkinter import *
from tkinter import ttk
from math import *



screen = Tk()
screen.title('Крестики-Нолики')
screen.geometry("500x500")
style = ttk.Style()
style.theme_use('clam')
board = [["" for row in range(10)] for col in range(10)]
current_player ="X"


def play_game():
        global screen_2
        if 'screen_2' in globals():
            screen_2.destroy()
        screen_2 = Tk()
        screen_2.title('Крестики-Нолики')
        screen_2.geometry("500x500")
        global canvas
        canvas = Canvas(screen_2, bg="white", width=500, height=500)
        canvas.pack(anchor=CENTER, expand=1)


        canvas.create_line(0, 50, 500, 50, fill='black')
        canvas.create_line(0, 100, 500, 100, fill='black')
        canvas.create_line(0, 150, 500, 150, fill='black')
        canvas.create_line(0, 200, 500, 200, fill='black')
        canvas.create_line(0, 250, 500, 250, fill='black')
        canvas.create_line(0, 300, 500, 300, fill='black')
        canvas.create_line(0, 350, 500, 350, fill='black')
        canvas.create_line(0, 400, 500, 400, fill='black')
        canvas.create_line(0, 450, 500, 450, fill='black')
        canvas.create_line(0, 500, 500, 500, fill='black')

        canvas.create_line(50, 0, 50, 500, fill='black')
        canvas.create_line(100, 0, 100, 500, fill='black')
        canvas.create_line(150, 0, 150, 500, fill='black')
        canvas.create_line(200, 0, 200, 500, fill='black')
        canvas.create_line(250, 0, 250, 500, fill='black')
        canvas.create_line(300, 0, 300, 500, fill='black')
        canvas.create_line(350, 0, 350, 500, fill='black')
        canvas.create_line(400, 0, 400, 500, fill='black')
        canvas.create_line(450, 0, 450, 500, fill='black')
        canvas.create_line(500, 0, 500, 500, fill='black')

        def move(event):
              x = event.x
              y = event.y
              col = floor(x // 50)
              row = floor(y // 50)
              global current_player
              if not check_move(row, col):
                  return
              if board[row][col] == "":
                  board[row][col] = current_player
                  if current_player == 'X':
                      canvas.create_line(col * 50, row*50, col * 50 + 50, row*50+50, fill='blue')
                      canvas.create_line(col * 50 +50, row * 50, col * 50, row * 50 + 50, fill='blue')
                  else:
                      canvas.create_oval(col * 50 + 2, row*50+2, col * 50 + 48, row*50+48, fill="white", outline="red")
                  all_moves.append((row, col))
                  print(all_moves)
                  if check_winner():
                      print(f"WIN {current_player}")
                      end_game()

                  current_player = "O" if current_player == "X" else "X"

              print(*board, sep='\n')
              print()
              print(all_moves)
        screen_2.bind('<Button 1>', move)


all_moves = []
def check_row(row):
    for col in range(6):
        if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == board[row][col + 4] != "":
             return True
        return False

def check_col(col):
    for row in range(6):
         if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == board[row + 4][col] != "":
            return True
    return False

def check_diagonal_lr():
    for row in range(6):
        for col in range(6):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == board[row + 4][col + 4] != "":
                return True
            return False

def check_diagonal_rl():
    for row in range(4, 10):
        for col in range(6):
             if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3] == board[row + 4][col - 4] != "":
                 return True
             return False

def check_winner():
    for i in range(10):
        if check_row(i) or check_col(i):
            print(f"Победитель: {current_player}")
            return True
        if check_diagonal_rl() or check_diagonal_lr():
            print(f"Победитель: {current_player}")
            return True
    return False

def check_move(row, col):
    if not all_moves:
        return True
    for r, c in all_moves:
        print(f"Проверка соседства для клетки ({row}, {col}) с ({r}, {c})")
        if abs(r-row) <= 1 and abs(c-col) <= 1:
            return True
    return False


def reset_game():
    global all_moves, board, current_player
    all_moves = []
    board = [["" for row in range(10)] for col in range(10)]
    current_player = "X"
    canvas.delete("all")
    play_game()
    screen_3.destroy()


def end_game():
    global screen_3
    screen_3 = Tk()
    screen_3.title("Победитель")
    screen_3.geometry("250x200")
    k = 'Крестики'
    o = 'Нолики'
    label = ttk.Label(screen_3, text=f"Победитель {k if current_player == 'X' else o}")
    label.pack(expand=True)
    btn_again = ttk.Button(screen_3, text="ЗАНОВО", command=reset_game)
    btn_again.pack(anchor="se")
    btn_close = ttk.Button(screen_3, text="ВЫХОД", command=close_screen)
    btn_close.pack(anchor="ne")

def close_screen():
    screen.destroy()
    screen_2.destroy()
    screen_3.destroy()

btn = ttk.Button(screen, text="ИГРАТЬ", command=play_game)
btn.place(relx=0.5, rely=0.3, anchor="c", width=300, height=100)
btn_2 = ttk.Button(text="ВЫХОД", command=lambda: screen.destroy())
btn_2.place(relx=0.5, rely=0.6, anchor="c", width=300, height=100)



screen.mainloop()

