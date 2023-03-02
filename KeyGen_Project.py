import random
import string

def gerar_senha(comprimento=8):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha


import tkinter as tk

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.config(bg="black")

def exibir_senha():
    senha = gerar_senha()
    label_senha.configure(text="Senha: " + senha)

label_instrucao = tk.Label(janela, bg="black",fg="white", text="Clique no botão para gerar uma senha aleatória.")
label_instrucao.pack()

botao_gerar_senha = tk.Button(janela,bg="black", fg="white", text="Gerar Senha", command=exibir_senha)
botao_gerar_senha.pack()

label_senha = tk.Label(janela,bg="black",fg="white", text="")
label_senha.pack()

janela.mainloop()


