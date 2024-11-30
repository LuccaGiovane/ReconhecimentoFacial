<div align="center">
   <h1><b>Reconhecimento Facial</b></h1><br><br>

   <a href="" target="_blank">![License](https://img.shields.io/badge/license-MIT-blue.svg)</a>
   ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

</div>


## 📖 Descrição

É uma aplicação de reconhecimento facial desenvolvida em Python. Este projeto permite capturar, treinar e reconhecer rostos utilizando técnicas avançadas de visão computacional e aprendizado de máquina.

## 🎯 Funcionalidades

- **Detecção de Rostos:** Identifica e delimita rostos em imagens e vídeos.
- **Captura de Imagens Faciais:** Permite coletar imagens de rostos para treinamento.
- **Treinamento do Modelo:** Treina um modelo de reconhecimento facial com as imagens capturadas.
- **Reconhecimento Facial em Tempo Real:** Reconhece e identifica rostos usando a webcam.
- **Interface Simples:** Scripts fáceis de usar para cada etapa do processo.

## 🛠 Tecnologias Utilizadas

- **Python 3.8+**
- **OpenCV:** Biblioteca de visão computacional.
- **face_recognition:** Biblioteca para reconhecimento facial.
- **NumPy:** Manipulação de arrays e operações matemáticas.
- **OS e Shutil:** Manipulação de arquivos e diretórios.

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
   3.1 **Windows:**
      ```bash
      venv\Scripts\activate
      ```
   3.2 **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```
      
4. **Instale as dependências necessárias:**
   ```bash
   pip install opencv-python face_recognition numpy
   ```

## 🚀 Uso
**Inicie o Programa**
   ```bash
   python main.py
   ```
1. Insira seu nome no campo indicado e espere a captura de imagens de seu rosto via webcam e posteriormente o treinamento do modelo.
2. Após isso o script iniciará a webcam novamente e exibirá o vídeo com os rostos reconhecidos identificados.<br><br>

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.
