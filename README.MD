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

### Endpoints

#### GET: /api/v1/healthcheck

##### Response

```JSON
{
  "uptime": 4.496053299,
  "status": "UP",
  "port": 3001,
  "timestamp": 1607812833792
}
```

#### GET: /api/v1/games

##### Response

```JSON
{
    "game_1": {
        "total_kills": 0,
        "players": [
            "Isgalamido"
        ],
        "kills": {
            "Isgalamido": 0
        }
    },
    "game_2": {
        "total_kills": 11,
        "players": [
            "Isgalamido",
            "Dono da Bola",
            "Mocinha"
        ],
        "kills": {
            "Isgalamido": -7,
            "Dono da Bola": 0,
            "Mocinha": 0
        }
    }
}
```

#### GET: /api/v1/games/:id

##### Response

```JSON
{
    "game_1": {
        "total_kills": 0,
        "players": [
            "Isgalamido"
        ],
        "kills": {
            "Isgalamido": 0
        }
    }
}
```