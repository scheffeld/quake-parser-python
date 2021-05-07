# Quake Parser

Uma API Rest que expoe um serviço de processamento de um arquivo de log do jogo Quake 3 Arena.

A partir de um arquivo `games.log`, a API processa os dados do arquivo e identifica as partidas realizadas, os jogadores conectados e as informações de morte de cada partida do log.

## Getting Started

#### Dependencies

- Python 3.8.5
- Flask 1.1.2
- Pyenv 1.2.26

#### Setup

Crie a virtualenv (use pyenv):
```shell
pyenv virtualenv quake-parser
```

Instale o Flask via pip:
```shell
pip install flask
```

Rode o projeto:
```shell
python main.py
```