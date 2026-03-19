# Como Executar o GEO Quiz (Cliente-Servidor)

Este projeto consiste em um sistema de quiz via terminal utilizando **Sockets TCP em Python**, dividido em dois componentes:

* Servidor (`server.py`)
* Cliente (`client.py`)

---

## Pré-requisitos

Antes de começar, você precisa ter instalado:

* Python 3.x

Para verificar se está instalado:

```bash
python --version
```

ou

```bash
python3 --version
```

---

## . Clonar o repositório

```bash
git clone https://github.com/LuccaRS/C115
```

## ▶️ 2. Executar o servidor

Abra um terminal e rode:

```bash
python server.py
```

O servidor ficará aguardando conexão:

```
Servidor aguardando conexão...
```

---

## . Executar o cliente

Abra **outro terminal** (isso é importante) e rode:

```bash
python client.py
```

---

## . Interagir com o sistema

1. Digite seu nome
2. Responda as perguntas usando:

   * A
   * B
   * C
   * D

Exemplo:

```
Digite seu nome: Joaquim
Sua resposta (A/B/C/D): A
```

---

## . Resultado final

Ao final do quiz, você verá:

* Seu nome
* Total de acertos
* Comparação entre suas respostas e as corretas

Exemplo:

```
Resultado do jogador: Lucca

Q1 (resposta: B | correta: B)
Q2 (resposta: A | correta: C)
Q3 (resposta: B | correta: B)

Total de acertos: 2/3
```

---

## Observações

* O servidor deve ser iniciado **antes** do cliente
* Cliente e servidor devem usar o **mesmo IP e porta**
* Por padrão, o sistema usa:

  * IP: `127.0.0.1` (localhost)
  * Porta: `5000`

---
