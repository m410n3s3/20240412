# A, B, C, D = map(int, input().split())

# if B > C and D > A and (C + D) > (A +B) and C > 0 and D > 0 and A % 2 == 0:
#     print("Valores aceitps")
# else:
#     print("Valores nao aceitos")

# Inicializando o tabuleiro vazio

# board = [" " for _ in range(9)]

# def print_board():
#     for i in range(3):
#         print("|".join(board[i*3:(i+1)*3]))
#         if i < 2:
#             print("-----")

# def check_winner(player):
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
#         [0, 4, 8], [2, 4, 6]              # Diagonais
#     ]
#     return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

# def is_draw():
#     return all(cell != " " for cell in board)

# def play_game():
#     current_player = "X"
#     while True:
#         print_board()
#         move = int(input(f"Jogador {current_player}, escolha uma posição (1-9): ")) - 1
#         if board[move] == " ":
#             board[move] = current_player
#             if check_winner(current_player):
#                 print_board()
#                 print(f"Jogador {current_player} venceu!")
#                 break
#             elif is_draw():
#                 print_board()
#                 print("Empate!")
#                 break
#             current_player = "O" if current_player == "X" else "X"
#         else:
#             print("Posição inválida, tente novamente.")

# play_game()

# import tkinter as tk
# from tkinter import messagebox

# # Inicializar a janela principal
# root = tk.Tk()
# root.title("Jogo da Velha")

# # Variáveis do jogo
# board = [" " for _ in range(9)]
# current_player = "X"
# buttons = []

# # Função para verificar o vencedor
# def check_winner():
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
#         [0, 4, 8], [2, 4, 6]              # Diagonais
#     ]
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
#             return True
#     return False

# # Função para verificar empate
# def is_draw():
#     return all(cell != " " for cell in board)

# # Função chamada quando um botão é clicado
# def button_click(index):
#     global current_player
#     if board[index] == " ":
#         board[index] = current_player
#         buttons[index].config(text=current_player)
#         if check_winner():
#             messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#             reset_board()
#         elif is_draw():
#             messagebox.showinfo("Fim de Jogo", "Empate!")
#             reset_board()
#         else:
#             current_player = "O" if current_player == "X" else "X"

# # Função para resetar o tabuleiro
# def reset_board():
#     global board, current_player
#     board = [" " for _ in range(9)]
#     current_player = "X"
#     for button in buttons:
#         button.config(text=" ")

# # Criar os botões do tabuleiro
# for i in range(9):
#     button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: button_click(i))
#     button.grid(row=i//3, column=i%3)
#     buttons.append(button)

# # Iniciar a aplicação
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import random

# # Inicializar a janela principal
# root = tk.Tk()
# root.title("Jogo da Velha")

# # Variáveis do jogo
# board = [" " for _ in range(9)]
# current_player = "X"
# buttons = []
# mode = "Player vs Player"

# # Função para verificar o vencedor
# def check_winner():
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
#         [0, 4, 8], [2, 4, 6]              # Diagonais
#     ]
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
#             return True
#     return False

# # Função para verificar empate
# def is_draw():
#     return all(cell != " " for cell in board)

# # Função chamada quando um botão é clicado
# def button_click(index):
#     global current_player
#     if board[index] == " ":
#         board[index] = current_player
#         buttons[index].config(text=current_player)
#         if check_winner():
#             messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#             reset_board()
#         elif is_draw():
#             messagebox.showinfo("Fim de Jogo", "Empate!")
#             reset_board()
#         else:
#             current_player = "O" if current_player == "X" else "X"
#             if mode == "Player vs Bot" and current_player == "O":
#                 bot_move()

# # Função para jogada do bot
# def bot_move():
#     global current_player
#     empty_cells = [i for i, cell in enumerate(board) if cell == " "]
#     move = random.choice(empty_cells)
#     board[move] = current_player
#     buttons[move].config(text=current_player)
#     if check_winner():
#         messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#         reset_board()
#     elif is_draw():
#         messagebox.showinfo("Fim de Jogo", "Empate!")
#         reset_board()
#     else:
#         current_player = "X"

# # Função para resetar o tabuleiro
# def reset_board():
#     global board, current_player
#     board = [" " for _ in range(9)]
#     current_player = "X"
#     for button in buttons:
#         button.config(text=" ")

# # Função para iniciar o jogo
# def start_game(selected_mode):
#     global mode
#     mode = selected_mode
#     reset_board()

# # Criar os botões do tabuleiro
# for i in range(9):
#     button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: button_click(i))
#     button.grid(row=i//3, column=i%3)
#     buttons.append(button)

# # Adicionar botões para selecionar o modo de jogo
# tk.Button(root, text="Player vs Player", command=lambda: start_game("Player vs Player")).grid(row=3, column=0, columnspan=1)
# tk.Button(root, text="Player vs Bot", command=lambda: start_game("Player vs Bot")).grid(row=3, column=2, columnspan=1)

# # Iniciar a aplicação
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# Inicializar a janela principal
# root = tk.Tk()
# root.title("Jogo da Velha")

# # Variáveis do jogo
# board = [" " for _ in range(9)]
# current_player = "X"
# buttons = []
# mode = "Player vs Player"

# # Função para verificar o vencedor
# def check_winner(player):
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
#         [0, 4, 8], [2, 4, 6]              # Diagonais
#     ]
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] == player:
#             return True
#     return False

# # Função para verificar empate
# def is_draw():
#     return all(cell != " " for cell in board)

# # Função chamada quando um botão é clicado
# def button_click(index):
#     global current_player
#     if board[index] == " ":
#         board[index] = current_player
#         buttons[index].config(text=current_player)
#         if check_winner(current_player):
#             messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#             reset_board()
#         elif is_draw():
#             messagebox.showinfo("Fim de Jogo", "Empate!")
#             reset_board()
#         else:
#             current_player = "O" if current_player == "X" else "X"
#             if mode == "Player vs Bot" and current_player == "O":
#                 bot_move()

# # Função para jogada do bot usando Minimax
# def bot_move():
#     global current_player
#     best_score = -float("inf")
#     best_move = None
#     for i in range(9):
#         if board[i] == " ":
#             board[i] = current_player
#             score = minimax(board, 0, False)
#             board[i] = " "
#             if score > best_score:
#                 best_score = score
#                 best_move = i
#     board[best_move] = current_player
#     buttons[best_move].config(text=current_player)
#     if check_winner(current_player):
#         messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#         reset_board()
#     elif is_draw():
#         messagebox.showinfo("Fim de Jogo", "Empate!")
#         reset_board()
#     else:
#         current_player = "X"

# def minimax(board, depth, is_maximizing):
#     if check_winner("O"):
#         return 1
#     elif check_winner("X"):
#         return -1
#     elif is_draw():
#         return 0

#     if is_maximizing:
#         best_score = -float("inf")
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "O"
#                 score = minimax(board, depth + 1, False)
#                 board[i] = " "
#                 best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = float("inf")
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "X"
#                 score = minimax(board, depth + 1, True)
#                 board[i] = " "
#                 best_score = min(score, best_score)
#         return best_score

# # Função para resetar o tabuleiro
# def reset_board():
#     global board, current_player
#     board = [" " for _ in range(9)]
#     current_player = "X"
#     for button in buttons:
#         button.config(text=" ")

# # Função para iniciar o jogo
# def start_game(selected_mode):
#     global mode
#     mode = selected_mode
#     reset_board()

# # Criar os botões do tabuleiro
# for i in range(9):
#     button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: button_click(i))
#     button.grid(row=i//3, column=i%3)
#     buttons.append(button)

# # Adicionar botões para selecionar o modo de jogo
# tk.Button(root, text="Player vs Player", command=lambda: start_game("Player vs Player")).grid(row=3, column=0, columnspan=1)
# tk.Button(root, text="Player vs Bot", command=lambda: start_game("Player vs Bot")).grid(row=3, column=2, columnspan=1)

# # Iniciar a aplicação
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import random

# # Inicializar a janela principal
# root = tk.Tk()
# root.title("Jogo da Velha")

# # Variáveis do jogo
# board = [" " for _ in range(9)]
# current_player = "X"
# buttons = []
# mode = "Player vs Player"
# difficulty = "Fácil"

# # Função para verificar o vencedor
# def check_winner(player):
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
#         [0, 4, 8], [2, 4, 6]              # Diagonais
#     ]
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] == player:
#             return True
#     return False

# # Função para verificar empate
# def is_draw():
#     return all(cell != " " for cell in board)

# # Função chamada quando um botão é clicado
# def button_click(index):
#     global current_player
#     if board[index] == " ":
#         board[index] = current_player
#         buttons[index].config(text=current_player)
#         if check_winner(current_player):
#             messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#             reset_board()
#         elif is_draw():
#             messagebox.showinfo("Fim de Jogo", "Empate!")
#             reset_board()
#         else:
#             current_player = "O" if current_player == "X" else "X"
#             if mode == "Player vs Bot" and current_player == "O":
#                 bot_move()

# # Função para jogada do bot
# def bot_move():
#     global current_player
#     if difficulty == "Fácil":
#         easy_move()
#     elif difficulty == "Médio":
#         medium_move()
#     elif difficulty == "Difícil":
#         hard_move()

# # Função para jogada do bot fácil (movimento aleatório)
# def easy_move():
#     global current_player
#     empty_cells = [i for i, cell in enumerate(board) if cell == " "]
#     move = random.choice(empty_cells)
#     board[move] = current_player
#     buttons[move].config(text=current_player)
#     if check_winner(current_player):
#         messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#         reset_board()
#     elif is_draw():
#         messagebox.showinfo("Fim de Jogo", "Empate!")
#         reset_board()
#     else:
#         current_player = "X"

# # Função para jogada do bot médio (estratégia básica)
# def medium_move():
#     global current_player
#     # Primeiro tenta ganhar
#     for i in range(9):
#         if board[i] == " ":
#             board[i] = current_player
#             if check_winner(current_player):
#                 buttons[i].config(text=current_player)
#                 if check_winner(current_player):
#                     messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#                     reset_board()
#                 elif is_draw():
#                     messagebox.showinfo("Fim de Jogo", "Empate!")
#                     reset_board()
#                 else:
#                     current_player = "X"
#                 return
#             board[i] = " "
#     # Depois tenta bloquear o jogador
#     opponent = "X" if current_player == "O" else "O"
#     for i in range(9):
#         if board[i] == " ":
#             board[i] = opponent
#             if check_winner(opponent):
#                 board[i] = current_player
#                 buttons[i].config(text=current_player)
#                 if check_winner(current_player):
#                     messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#                     reset_board()
#                 elif is_draw():
#                     messagebox.showinfo("Fim de Jogo", "Empate!")
#                     reset_board()
#                 else:
#                     current_player = "X"
#                 return
#             board[i] = " "
#     # Se não, faz movimento aleatório
#     easy_move()

# # Função para jogada do bot difícil (algoritmo Minimax)
# def hard_move():
#     global current_player
#     best_score = -float("inf")
#     best_move = None
#     for i in range(9):
#         if board[i] == " ":
#             board[i] = current_player
#             score = minimax(board, 0, False)
#             board[i] = " "
#             if score > best_score:
#                 best_score = score
#                 best_move = i
#     board[best_move] = current_player
#     buttons[best_move].config(text=current_player)
#     if check_winner(current_player):
#         messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
#         reset_board()
#     elif is_draw():
#         messagebox.showinfo("Fim de Jogo", "Empate!")
#         reset_board()
#     else:
#         current_player = "X"

# def minimax(board, depth, is_maximizing):
#     if check_winner("O"):
#         return 1
#     elif check_winner("X"):
#         return -1
#     elif is_draw():
#         return 0

#     if is_maximizing:
#         best_score = -float("inf")
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "O"
#                 score = minimax(board, depth + 1, False)
#                 board[i] = " "
#                 best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = float("inf")
#         for i in range(9):
#             if board[i] == " ":
#                 board[i] = "X"
#                 score = minimax(board, depth + 1, True)
#                 board[i] = " "
#                 best_score = min(score, best_score)
#         return best_score

# # Função para resetar o tabuleiro
# def reset_board():
#     global board, current_player
#     board = [" " for _ in range(9)]
#     current_player = "X"
#     for button in buttons:
#         button.config(text=" ")

# # Função para iniciar o jogo
# def start_game(selected_mode, selected_difficulty):
#     global mode, difficulty
#     mode = selected_mode
#     difficulty = selected_difficulty
#     reset_board()

# # Criar os botões do tabuleiro
# for i in range(9):
#     button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: button_click(i))
#     button.grid(row=i//3, column=i%3)
#     buttons.append(button)

# # Adicionar botões para selecionar o modo de jogo e a dificuldade
# tk.Button(root, text="Player vs Player", command=lambda: start_game("Player vs Player", difficulty)).grid(row=3, column=0, columnspan=1)
# tk.Button(root, text="Player vs Bot (Fácil)", command=lambda: start_game("Player vs Bot", "Fácil")).grid(row=3, column=1, columnspan=1)
# tk.Button(root, text="Player vs Bot (Médio)", command=lambda: start_game("Player vs Bot", "Médio")).grid(row=3, column=2, columnspan=1)
# tk.Button(root, text="Player vs Bot (Difícil)", command=lambda: start_game("Player vs Bot", "Difícil")).grid(row=3, column=3, columnspan=1)

# # Iniciar a aplicação
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import random

# class Pokemon:
#     def __init__(self, name, hp, attack):
#         self.name = name
#         self.hp = hp
#         self.attack = attack

#     def attack_pokemon(self, other_pokemon):
#         damage = random.randint(1, self.attack)
#         other_pokemon.hp -= damage
#         return damage

#     def is_fainted(self):
#         return self.hp <= 0

# # Criação dos Pokémon
# pikachu = Pokemon("Pikachu", 35, 10)
# charmander = Pokemon("Charmander", 39, 12)

# # Função para a batalha
# def battle(pokemon1, pokemon2):
#     if not pokemon1.is_fainted() and not pokemon2.is_fainted():
#         damage = pokemon1.attack_pokemon(pokemon2)
#         update_display()
#         messagebox.showinfo("Ataque", f"{pokemon1.name} ataca {pokemon2.name} e causa {damage} de dano!")
#         if pokemon2.is_fainted():
#             messagebox.showinfo("Fim de Jogo", f"{pokemon2.name} desmaiou! {pokemon1.name} venceu!")
#         else:
#             damage = pokemon2.attack_pokemon(pokemon1)
#             update_display()
#             messagebox.showinfo("Ataque", f"{pokemon2.name} ataca {pokemon1.name} e causa {damage} de dano!")
#             if pokemon1.is_fainted():
#                 messagebox.showinfo("Fim de Jogo", f"{pokemon1.name} desmaiou! {pokemon2.name} venceu!")

# # Função para atualizar a tela com os status dos Pokémon
# def update_display():
#     pikachu_hp_label.config(text=f"Pikachu: {pikachu.hp} HP")
#     charmander_hp_label.config(text=f"Charmander: {charmander.hp} HP")

# # Inicializando a janela principal
# root = tk.Tk()
# root.title("Batalha Pokémon")

# # Labels para mostrar o status dos Pokémon
# pikachu_hp_label = tk.Label(root, text=f"Pikachu: {pikachu.hp} HP", font=('Arial', 16))
# pikachu_hp_label.pack(pady=10)

# charmander_hp_label = tk.Label(root, text=f"Charmander: {charmander.hp} HP", font=('Arial', 16))
# charmander_hp_label.pack(pady=10)

# # Botão para iniciar a batalha
# battle_button = tk.Button(root, text="Atacar", command=lambda: battle(pikachu, charmander), font=('Arial', 16))
# battle_button.pack(pady=20)

# # Iniciar a aplicação
# update_display()
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random

class Pokemon:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.attacks = attacks

    def attack_pokemon(self, other_pokemon, attack_name):
        damage = self.attacks[attack_name]
        other_pokemon.hp -= damage
        return damage

    def is_fainted(self):
        return self.hp <= 0

# Criação dos Pokémon com ataques
pikachu = Pokemon("Pikachu", 35, {"Thunder Shock": 10, "Quick Attack": 20000000000, "Iron Tail": 12, "Electro Ball": 15})
charmander = Pokemon("Charmander", 39, {"Flamethrower": 12, "Scratch": 7, "Ember": 10, "Fire Spin": 14})

# Função para a batalha
def battle(pokemon1, pokemon2, attack_name):
    if not pokemon1.is_fainted() and not pokemon2.is_fainted():
        damage = pokemon1.attack_pokemon(pokemon2, attack_name)
        update_display()
        messagebox.showinfo("Ataque", f"{pokemon1.name} usa {attack_name} e causa {damage} de dano!")
        if pokemon2.is_fainted():
            messagebox.showinfo("Fim de Jogo", f"{pokemon2.name} desmaiou! {pokemon1.name} venceu!")
            reset_board()
        else:
            bot_attack_name = random.choice(list(pokemon2.attacks.keys()))
            damage = pokemon2.attack_pokemon(pokemon1, bot_attack_name)
            update_display()
            messagebox.showinfo("Ataque", f"{pokemon2.name} usa {bot_attack_name} e causa {damage} de dano!")
            if pokemon1.is_fainted():
                messagebox.showinfo("Fim de Jogo", f"{pokemon1.name} desmaiou! {pokemon2.name} venceu!")
                reset_board()

# Função para atualizar a tela com os status dos Pokémon
def update_display():
    pikachu_hp_label.config(text=f"Pikachu: {pikachu.hp} HP")
    charmander_hp_label.config(text=f"Charmander: {charmander.hp} HP")

# Função para resetar o tabuleiro
def reset_board():
    global pikachu, charmander
    pikachu = Pokemon("Pikachu", 35, {"Thunder Shock": 10, "Quick Attack": 20000000000, "Iron Tail": 12, "Electro Ball": 15})
    charmander = Pokemon("Charmander", 39, {"Flamethrower": 12, "Scratch": 7, "Ember": 10, "Fire Spin": 14})
    update_display()

# Inicializando a janela principal
root = tk.Tk()
root.title("Batalha Pokémon")

# Labels para mostrar o status dos Pokémon
pikachu_hp_label = tk.Label(root, text=f"Pikachu: {pikachu.hp} HP", font=('Arial', 16))
pikachu_hp_label.pack(pady=10)

charmander_hp_label = tk.Label(root, text=f"Charmander: {charmander.hp} HP", font=('Arial', 16))
charmander_hp_label.pack(pady=10)

# Botões para escolher o ataque
for attack in pikachu.attacks.keys():
    button = tk.Button(root, text=attack, command=lambda attack=attack: battle(pikachu, charmander, attack), font=('Arial', 16))
    button.pack(pady=5)

# Iniciar a aplicação
update_display()
root.mainloop()
