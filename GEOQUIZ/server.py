import socket

HOST = '127.0.0.1'
PORT = 5000

questions = [
    {
        "question": "Questão 1. Qual o país que possui a maior fronteira com a França?",
        "options": ["A) Alemanha", "B) Brasil", "C) Suiça", "D) Espanha"],
        "answer": "B"
    },
    {
        "question": "Questão 2. Qual o IDH (Índice de Desenvolvimento Humano) brasileiro, sendo o 84 país no ranking mundial?",
        "options": ["A) 0,770", "B) 0,812", "C) 0,786", "D) 0,795"],
        "answer": "C"
    },
    {
        "question": "Questão 3. Qual o maior município brasileiro, com 159.534 km^2, com área maior que Portugal?",
        "options": ["A) Altamira - PA", "B) São Paulo - SP", "C) Bom Jesus da Lapa - BA", "D) Maraã - AM"],
        "answer": "A"

    },
    {

        "question": "Questão 4. Qual o segundo menor país do mundo?",
        "options": ["A) Mônaco", "B) San Marino", "C) Liechtenstein", "D) Nauru"],
        "answer": "D"
    },

    {

        "question": "Questão 5. Qual a cidade com maior número de francófonos?",
        "options": ["A) Marseille", "B) Kinshasa", "C) Paris", "D) Quebec"],
        "answer": "B"
    },

    {

        "question": "Questão 6. Em qual país está cituado a maior montanha fora da cordilheira dos Himalaias?",
        "options": ["A) Denali - Estados Unidos", "B) Ojos del Salado - Chile", "C) Aconcágua - Argentina", "D) Mont Blanc - França / Itália"],
        "answer": "C"
    },

    {

        "question": "Questão 7. Qual país possui o maior número de fuso horários?",
        "options": ["A) França", "B) Estados Unidos", "C) Rússia", "D) China"],
        "answer": "A"
    },
    

]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor aguardando conexão...")

conn, addr = server.accept()
print("Cliente conectado:", addr)

name = conn.recv(1024).decode()

responses = []

for q in questions:
    message = q["question"] + "\n"
    for opt in q["options"]:
        message += opt + "\n"

    conn.send(message.encode())

    answer = conn.recv(1024).decode().strip().upper()
    responses.append(answer)

correct = 0
result = f"\nResultado do jogador: {name}\n"

for i, q in enumerate(questions):
    user_answer = responses[i]
    correct_answer = q["answer"]

    if user_answer == correct_answer:
        correct += 1

    result += f"Q{i+1} (resposta: {user_answer} | correta: {correct_answer})\n"

result += f"\nTotal de acertos: {correct}/7\n"

conn.send(result.encode())

conn.close()