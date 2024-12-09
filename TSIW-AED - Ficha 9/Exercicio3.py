import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura * altura)

        label_resultado.config(text=f"IMC: {imc:.2f}")

        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"
        
        label_categoria.config(text=f"Categoria: {categoria}")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")


def sair():
    janela.quit()


def on_enter_button(event, button):
    button.config(bg="#4CAF50", fg="white")

def on_leave_button(event, button):
    button.config(bg="#5e5e5e", fg="white")


janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("325x670") 


frame_dados = tk.Frame(janela, width=300, height=150)
frame_dados.pack(padx=10, pady=10)

label_peso = tk.Label(frame_dados, text="Peso (kg):")
label_peso.grid(row=0, column=0, padx=5, pady=5)
entry_peso = tk.Entry(frame_dados)
entry_peso.grid(row=0, column=1, padx=5, pady=5)

label_altura = tk.Label(frame_dados, text="Altura (m):")
label_altura.grid(row=1, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame_dados)
entry_altura.grid(row=1, column=1, padx=5, pady=5)


frame_resultado = tk.Frame(janela, width=300, height=100)
frame_resultado.pack(padx=10, pady=10)


label_resultado = tk.Label(frame_resultado, text="IMC: ", font=("Arial", 14))
label_resultado.pack(pady=5)

label_categoria = tk.Label(frame_resultado, text="Categoria: ", font=("Arial", 12))
label_categoria.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular IMC", font=("Arial", 12, "bold"), width=20, height=2,
                           bg="#5e5e5e", fg="white", relief="raised", bd=2, command=calcular_imc)
botao_calcular.bind("<Enter>", lambda event: on_enter_button(event, botao_calcular))
botao_calcular.bind("<Leave>", lambda event: on_leave_button(event, botao_calcular))
botao_calcular.pack(pady=20)
botao_sair = tk.Button(janela, text="Sair", font=("Arial", 12, "bold"), width=20, height=2,
                       bg="#d9534f", fg="white", relief="raised", bd=2, command=sair)
botao_sair.bind("<Enter>", lambda event: on_enter_button(event, botao_sair))
botao_sair.bind("<Leave>", lambda event: on_leave_button(event, botao_sair))
botao_sair.pack(pady=10)
botao_imc = PhotoImage(file=".\\images\\imc.gif") 
label_imc = tk.Label(janela, image=botao_imc)
label_imc.pack(pady=10)

janela.mainloop()
