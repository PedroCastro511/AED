import tkinter as tk
from tkinter import messagebox

def calcular_peso_ideal():
    try:
        altura = int(entry_altura.get())
        genero = var_genero.get()
        
        if altura <= 0:
            raise ValueError("A altura deve ser positiva.")
        
        k = 4 if genero == "Masculino" else 2  
        peso_ideal = (altura - 100) - (altura - 150) / k
        label_resultado.config(text=f"Peso Ideal: {peso_ideal:.2f} kg", fg="red")
    
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


root = tk.Tk()
root.title("Simulador de Peso Ideal")
root.geometry("370x430")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Altura (cm):", font=("Arial", 14), fg="blue").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_altura = tk.Entry(frame, font=("Arial", 14))
entry_altura.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Gênero:", font=("Arial", 14), fg="blue").grid(row=1, column=0, sticky="w", padx=10, pady=5)
var_genero = tk.StringVar()
tk.Radiobutton(frame, text="Masculino", variable=var_genero, value="Masculino", font=("Arial", 14)).grid(row=1, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(frame, text="Feminino", variable=var_genero, value="Feminino", font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=5, sticky="w")
tk.Button(root, text="Calcular Peso Ideal", font=("Arial", 14), command=calcular_peso_ideal, width=20).pack(pady=20)

label_resultado = tk.Label(root, text="Peso Ideal: ", font=("Arial", 14), fg="red")
label_resultado.pack(pady=10)

root.mainloop()
