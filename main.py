import os
import tkinter as tk
from tkinter import simpledialog, messagebox, font
from PIL import Image, ImageTk
import subprocess

def criar_pasta_usuario(nome):
    # Cria a pasta no dataset se não existir
    dataset_path = os.path.join("dataset", nome)
    os.makedirs(dataset_path, exist_ok=True)
    return dataset_path

def coletar_faces(nome):
    # Executa o script collect_faces.py para coleta de rostos
    subprocess.run(["python", "collect_faces.py", nome])

def treinar_reconhecedor():
    # Executa o script train_recognizer.py para treinar o modelo
    subprocess.run(["python", "train_recognizer.py"])

def iniciar_reconhecimento():
    # Executa o script FacialRecognition.py para reconhecimento em tempo real
    subprocess.run(["python", "FacialRecognition.py"])

def cadastrar(root):
    # Solicita o nome do usuário
    nome_usuario = simpledialog.askstring("Cadastro", "Digite seu nome para iniciar:", parent=root)
    if not nome_usuario:
        messagebox.showwarning("Atenção", "Nenhum nome fornecido. Cadastro cancelado.")
        return

    # Cria pasta do usuário
    criar_pasta_usuario(nome_usuario)

    # Coleta de rostos
    print(f"Iniciando coleta de rostos para {nome_usuario}...")
    coletar_faces(nome_usuario)

    # Treinamento
    print("Treinando o modelo de reconhecimento facial...")
    treinar_reconhecedor()

    messagebox.showinfo("Sucesso", f"Cadastro concluído para {nome_usuario}.")

def iniciar(root):
    # Inicia reconhecimento
    print("Iniciando reconhecimento facial em tempo real...")
    iniciar_reconhecimento()

def main():
    # Interface gráfica principal
    root = tk.Tk()
    root.title("Reconhecimento Facial")
    root.configure(bg='#ADD8E6')  # Fundo azul claro

    # Define o tamanho da janela
    root.geometry('400x600')
    root.resizable(False, False)

    # Título
    titulo_font = font.Font(family='Helvetica', size=24, weight='bold')
    titulo_label = tk.Label(root, text="Reconhecimento Facial", bg='#ADD8E6', font=titulo_font)
    titulo_label.pack(pady=20)

    # Imagem
    image_path = os.path.join('img', 'octocat.png')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=photo, bg='#ADD8E6')
        image_label.image = photo  # Mantém uma referência
        image_label.pack(pady=10)
    else:
        messagebox.showerror("Erro", f"Imagem não encontrada: {image_path}")

    # Botão Cadastrar
    cadastrar_button = tk.Button(root, text="Cadastrar", command=lambda: cadastrar(root), width=20, height=2)
    cadastrar_button.pack(pady=10)

    # Botão Iniciar
    iniciar_button = tk.Button(root, text="Iniciar", command=lambda: iniciar(root), width=20, height=2)
    iniciar_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
