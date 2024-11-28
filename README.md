# CODINGAL-FaceRecognition

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

## 📖 Descrição

**CODINGAL-FaceRecognition** é uma aplicação de reconhecimento facial desenvolvida em Python, seguindo o tutorial da [Codingal](https://www.codingal.com/coding-for-kids/blog/build-face-recognition-app-with-python/). Este projeto permite identificar e reconhecer rostos utilizando técnicas avançadas de visão computacional e aprendizado de máquina.

## 🎯 Funcionalidades

- **Detecção de Rostos:** Identifica e delimita rostos em imagens e vídeos.
- **Reconhecimento Facial:** Compara rostos detectados com um banco de dados para identificar indivíduos.
- **Treinamento Personalizado:** Adicione novos rostos ao sistema para melhorar a precisão.
- **Interface Simples:** Interface amigável para fácil interação e uso.

## 🛠 Tecnologias Utilizadas

- **Python 3.8+**
- **OpenCV:** Biblioteca de visão computacional.
- **face_recognition:** Biblioteca para reconhecimento facial.
- **NumPy:** Manipulação de arrays e operações matemáticas.
- **Tkinter:** Interface gráfica do usuário (opcional, se aplicável).

## 💾 Instalação

### Pré-requisitos

- **Python 3.8 ou superior** instalado em sua máquina. [Baixe aqui](https://www.python.org/downloads/).
- **pip** para gerenciar pacotes Python.

### Passos de Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/LuccaGiovane/CODINGAL-FaceRecognition.git
   ```
2. **Navegue até o diretório do projeto:**
   ```bash
   cd CODINGAL-FaceRecognition
   ```
3. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   ```
- Windows:
   ```bash
   venv\Scripts\activate
   ```
- macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
4. **Instale as dependências necessárias:**
   ```bash
   pip install opencv-python face_recognition numpy
   ```

## 🚀 Uso
1. **Prepare o Banco de Dados de Rostos:**

  Crie uma pasta chamada **known_faces.**
  Adicione imagens dos indivíduos que você deseja reconhecer. Nomeie os arquivos com o nome da pessoa (por exemplo, lucca.jpg).

2. **Execute o Script Principal:**
  ```bash
  python main.py
  ```
3. **Interaja com a Aplicação:**

  A aplicação iniciará a câmera e começará a detectar e reconhecer rostos em tempo real.
  Rostos reconhecidos serão etiquetados com seus respectivos nomes.

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.
