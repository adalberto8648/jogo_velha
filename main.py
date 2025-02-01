import tkinter as tk

#criar a janela
janela = tk.Tk()
janela.title("Jogo da Velha")

jogador_atual = "X" #começa com o jogador X

def marcar_botao(botao):
    global jogador_atual
    if botao['text'] == "":
        botao.config(text=jogador_atual)
        jogador_atual = "O" if jogador_atual == "X" else "X"

#criar tabuleiro
def criar_tabuleiro():
    for linha in range(3):
        for coluna in range(3):
            botao = tk.Button(janela,
                width=10,
                height=3,
                font=("Arial", 16),
                relief="ridge", #estilo da borda
                bg="white",     #cor de fundo
                command=lambda b=botao: marcar_botao(b))
            botao.grid(row=linha, column=coluna, padx=5, pady=5)
criar_tabuleiro()

#inicia o loop da najela
janela.mainloop()

