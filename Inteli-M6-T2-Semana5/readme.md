# Processamento de imagens e visão computacional

## 1. Introdução

Esse repositório apresenta como propósito a implementação de algoritmos de processamento de imagens e visão computacional, utilizando a linguagem de programação Python e o YOLOv8 para detecção de rachaduras em paredes de concreto, utilizando o dataset desenvolvido pela Roboflow, disponível em: <https://universe.roboflow.com/university-bswxt/crack-bphdr/dataset/2>.

## 2. Organização do repositório

O repositório está organizado da seguinte forma:

main.py: arquivo principal do projeto, responsável por executar o código de detecção de rachaduras em paredes de concreto.
modelo.ipynb: arquivo com o código utilizado para treinar o modelo YOLOv8.
best.pt: arquivo com os pesos do modelo YOLOv8, treinado com o dataset de rachaduras em paredes de concreto.
requirements.txt: arquivo com as bibliotecas necessárias para executar o código.
readme.md: arquivo com a descrição do projeto.
Demonstração.mp4: vídeo demonstrativo da execução do código.

## 3. Requerimentos

Para executar os códigos desse repositório, é necessário ter instalado em sua máquina o Python 3.10 ou superior, e as bibliotecas listadas no arquivo `requirements.txt`. Para instalar as bibliotecas, execute o comando abaixo no terminal:

```bash
pip install -r requirements.txt
```

## 4. Execução

No diretório desse projeto, utilize o comando abaixo para executar o código:

```bash
python main.py
```

## 5. Resultados

A partir da execução do script, é possível visualizar a imagem da câmera capturada pelo sistema. Caso for apresentada uma rachadura, a mesma será destacada em vermelho, como apresentado no vídeo abaixo:

<https://github.com/Pablo-RLV/Inteli-M6-T2-Semana5/assets/99209107/83d7502a-3cd5-489d-92ec-e027a317ca70>
