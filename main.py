import os
import tkinter as tk
from tkinter import simpledialog
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

def main():
    # Interface gráfica para pedir o nome do usuário
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicita o nome do usuário
    nome_usuario = simpledialog.askstring("Reconhecimento Facial", "Digite seu nome para iniciar:")
    if not nome_usuario:
        print("Nenhum nome fornecido. Encerrando o programa.")
        return

    # Cria pasta do usuário
    criar_pasta_usuario(nome_usuario)

    # Coleta de rostos
    print(f"Iniciando coleta de rostos para {nome_usuario}...")
    coletar_faces(nome_usuario)

    # Treinamento
    print("Treinando o modelo de reconhecimento facial...")
    treinar_reconhecedor()

    # Inicia reconhecimento
    print("Iniciando reconhecimento facial em tempo real...")
    iniciar_reconhecimento()

if __name__ == "__main__":
    main()
