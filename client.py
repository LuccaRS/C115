import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Digite seu nome: ")
client.send(name.encode())

answers = []

for i in range(3):
    question = client.recv(1024).decode()
    print("\n" + question)

    answer = input("Sua resposta (A/B/C/D): ")
    client.send(answer.encode())

result = client.recv(1024).decode()

print("\n=== RESULTADO FINAL ===")
print(result)

client.close()