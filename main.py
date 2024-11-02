import random
import os
import tkinter as tk
from tkinter import messagebox


def iniciar_jogo():
    erros = 0
    num_sorteado = random.randrange(0, 100)

    # Função que lida com a tentativa do jogador
    def tentar_adivinhar():
        nonlocal erros
        try:
            player = int(entry_numero.get())
            if player < 0 or player > 100:
                messagebox.showerror("Erro", "Digite um número entre 0 e 100")
                return

            if num_sorteado > player:
                messagebox.showinfo("Resultado", "Erro, o número é maior")
            elif num_sorteado < player:
                messagebox.showinfo("Resultado", "Erro, o número é menor")
            else:
                messagebox.showinfo("Parabéns", f"Número {player}. Você acertou em {erros + 1} tentativas!")
                window.destroy()  # Fechar a janela ao acertar
                return

            erros += 1
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido")

    # Limpar a tela e criar interface
    os.system('cls' if os.name == 'nt' else 'clear')  # Para quem estiver rodando no terminal
    window = tk.Tk()
    window.title("Jogo de Adivinhação")

    tk.Label(window, text="Tente adivinhar o número entre 0 e 100").pack(pady=10)

    # Campo de entrada para o número
    entry_numero = tk.Entry(window)
    entry_numero.pack(pady=5)

    # Botão para tentar adivinhar
    tk.Button(window, text="Tentar", command=tentar_adivinhar).pack(pady=10)

    window.mainloop()


# Interface inicial com botão "Jogar"
root = tk.Tk()
root.title("Início do Jogo")

tk.Label(root, text="Clique em 'Jogar' para começar o jogo de adivinhação!").pack(pady=20)

# Botão "Jogar"
tk.Button(root, text="Jogar", command=iniciar_jogo).pack(pady=10)

root.mainloop()





