import tkinter as tk
import math
from functools import partial
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return 10 - depth
    elif winner == "O":
        return depth - 10
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for (i, j) in get_available_moves(board):
        board[i][j] = "X"
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = " "
        if move_val > best_val:
            move = (i, j)
            best_val = move_val
    return move
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_turn = "O"
        self.singleplayer = False
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.frame, text=" ", width=10, height=3,
                                               command=partial(self.button_click, i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.singleplayer_button = tk.Button(self.root, text="Singleplayer", command=self.start_singleplayer)
        self.singleplayer_button.pack(side=tk.LEFT)
        
        self.multiplayer_button = tk.Button(self.root, text="Multiplayer", command=self.start_multiplayer)
        self.multiplayer_button.pack(side=tk.LEFT)
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack(side=tk.RIGHT)

    def button_click(self, i, j):
        if self.board[i][j] == " " and self.check_winner() is None:
            self.board[i][j] = self.current_turn
            self.buttons[i][j].config(text=self.current_turn)
            winner = self.check_winner()
            if winner:
                self.display_winner(winner)
            elif is_full(self.board):
                self.display_winner("Tie")
            else:
                self.current_turn = "X" if self.current_turn == "O" else "O"
                if self.singleplayer and self.current_turn == "X":
                    self.ai_move()

    def ai_move(self):
        move = best_move(self.board)
        self.board[move[0]][move[1]] = "X"
        self.buttons[move[0]][move[1]].config(text="X")
        winner = self.check_winner()
        if winner:
            self.display_winner(winner)
        elif is_full(self.board):
            self.display_winner("Tie")
        self.current_turn = "O"

    def check_winner(self):
        return check_winner(self.board)

    def display_winner(self, winner):
        if winner == "Tie":
            tk.messagebox.showinfo("Game Over", "It's a tie!")
        else:
            tk.messagebox.showinfo("Game Over", f"{winner} wins!")

    def start_singleplayer(self):
        self.restart_game()
        self.singleplayer = True

    def start_multiplayer(self):
        self.restart_game()
        self.singleplayer = False

    def restart_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_turn = "O"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
