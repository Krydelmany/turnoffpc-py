import tkinter as tk
from pytube import YouTube 

def baixar_video():
    url = entrada.get()
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()
    janela.destroy()

janela = tk.Tk()
janela.title("Baixar Vídeo")
janela.configure(background='black')
janela.configure(padx=100, pady=100)
janela.resizable(True, True) # redimensionável
janela.attributes("-topmost", True) #Sempre em cima das janelas

entrada = tk.Entry(janela,relief=tk.RIDGE)
entrada.pack(pady=5)
entrada.config(font=("Segoe UI", 10))
entrada.focus_set()

#ao clicar no botão ele puxa o titulo do video a imagem e a descrição
botao = tk.Button(janela, text="Baixar", command=baixar_video)
botao.pack(pady=0)
botao.config(font=("Segoe UI", 10))

url = input("Digite a URL do vídeo: ")
if url == "":
    print("URL inválida!")

video = YouTube(url)

stream = video.streams.get_highest_resolution()

stream.download()


janela.mainloop()