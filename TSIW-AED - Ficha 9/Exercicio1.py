import os
from tkinter import Tk, Text, Button, messagebox

file_path = ".\\files\\texto.txt"


def save_to_file():
    content = text_box.get("1.0", "end-1c")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    messagebox.showinfo("Informação", "Texto salvo com sucesso!")


def clear_text():
    text_box.delete("1.0", "end")


def read_from_file():
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        text_box.delete("1.0", "end")
        text_box.insert("1.0", content)
    else:
        messagebox.showwarning("Aviso", "O arquivo não existe. Salve algo primeiro!")

app = Tk()
app.title("Bloco de Notas")
app.geometry("300x600")  

text_box = Text(app, width=30, height=15, wrap="word")
text_box.pack(pady=10) 

Button(app, text="Guardar Notas", width=30, command=save_to_file, bg="green", fg="white").pack(pady=5)
Button(app, text="Limpar Notas", width=30, command=clear_text, bg="red", fg="white").pack(pady=5)
Button(app, text="Ler Notas", width=30, command=read_from_file, bg="lightblue", fg="black").pack(pady=5)

app.mainloop()
