import os
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

def desligar_pc():
    tempo = entrada.get()
    unidade_tempo = escolha.get()
    
    if tempo.isdigit():
        tempo = int(tempo)
        if unidade_tempo == "Horas":
            tempo_em_segundos = tempo * 3600
        else:
            tempo_em_segundos = tempo * 60

        # Faça o código para desligar o PC após o tempo especificado
        os.system(f"shutdown /s /t {tempo_em_segundos}")
        messagebox.showinfo("Desligar PC", f"O PC será desligado em {tempo} {unidade_tempo}.")
        janela.destroy()
    else:
        messagebox.showerror("Erro", "Digite um valor válido.")
        

# Crie a janela principal
janela = tk.Tk()
janela.title("Desligar PC")
janela.configure(background='black')
janela.configure(padx=50, pady=50) 
janela.resizable(False, False) #Não redimensionável
janela.attributes("-topmost", True) #Sempre em cima das janelas 
janela.iconbitmap("C:\\Users\\giovani\\Pictures\\iconshock-super-heros-spider-man.ico")

#janela.overrideredirect(True)


# Defina a fonte
fonte_personalizada = font.Font(family="Open Sans", size=11)

# Crie um rótulo
rotulo_tempo = tk.Label(janela, text="Digite o tempo:", fg="white", bg="black", font=fonte_personalizada)
rotulo_tempo.pack(pady=10)

# Crie uma entrada de texto com bordas arredondadas
entrada = tk.Entry(janela, font=fonte_personalizada, bd=2.5,relief=tk.RIDGE)
entrada.pack(pady=5)

# Crie um rótulo para a escolha da unidade de tempo
rotulo_unidade = tk.Label(janela, text="Escolha a unidade de tempo:", fg="white", bg="black", font=fonte_personalizada)
rotulo_unidade.pack(pady=5)

# Crie uma variável de controle para a escolha
escolha = tk.StringVar(janela)
escolha.set("Horas")  # Valor padrão

# Crie um menu de opções para a escolha da unidade de tempo
menu_opcoes = tk.OptionMenu(janela, escolha, "Horas", "Minutos")
menu_opcoes.config(font=fonte_personalizada, relief=tk.RIDGE)
menu_opcoes.pack(pady=5)
menu_opcoes["menu"].config(font=fonte_personalizada)


# Crie um botão
botao = tk.Button(janela, text="Desligar PC", font=fonte_personalizada, command=desligar_pc)
botao.pack(pady=10)

# Inicie o loop da janela
janela.mainloop()
