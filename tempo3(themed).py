import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle

API_KEY = 'e8f31ebd3e93def7b4e17b1744bad3b8'

# Janela
janela = tk.Tk()
janela.title("Tempo")
janela.configure(background='#464646')
janela.configure(padx=100, pady=300)
janela.resizable(True, True)  # redimensionável
janela.attributes("-topmost", True)  # Sempre em cima das janelas

style = ThemedStyle(janela)
style.set_theme("equilux") 

font = "Segoe UI"
rotulo = ttk.Label(janela, text="Digite o nome da cidade:", font=(font, 11))
rotulo.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entrada = ttk.Entry(janela, style="TEntry")
entrada.grid(row=0, column=1, padx=5, pady=5, sticky="we")
entrada.config(font=("Segoe UI", 10))
entrada.focus_set()

font = "Segoe UI"
resultado = ttk.Label(janela, text="", font=(font, 11))
resultado.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="w")


def obter_tempo(event=None):
    cidade = entrada.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"
    requisicao = requests.get(link)

    requisicao_dict = requisicao.json()
    descricao = requisicao_dict["weather"][0]["main"]
    temperatura = requisicao_dict['main']['temp'] - 273.15

    resultado_text = f"Nome: {requisicao_dict['name']}\n" \
                     f"País: {requisicao_dict['sys']['country']}\n" \
                     f"Descrição: {descricao}\n" \
                     f"Temperatura: {temperatura:.2f}°C\n" \
                     f"Umidade: {requisicao_dict['main']['humidity']}%\n" \
                     f"Pressão: {requisicao_dict['main']['pressure']}hPa\n" \
                     f"Velocidade do vento: {requisicao_dict['wind']['speed']}m/s\n" \
                     f"Nascer do sol: {requisicao_dict['sys']['sunrise']}\n" \
                     f"Pôr do sol: {requisicao_dict['sys']['sunset']}"
    resultado.config(text=resultado_text)
    entrada.delete(0, tk.END)

botao = ttk.Button(janela, text="Obter Tempo", command=obter_tempo)
botao.grid(row=0, column=2, padx=5, pady=5, sticky="e")

entrada.bind("<Return>", obter_tempo)
entrada.delete(0, tk.END)

janela.mainloop()
