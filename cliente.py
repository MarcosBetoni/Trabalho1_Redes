import socket

HOST = 'localhost'  # Endereço do servidor
PORT = 5000  # Porta de conexão

# Cria o socket do cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
cliente_socket.connect((HOST, PORT))

# Envia o nome do cliente para o servidor
nome_cliente = input("Digite seu nome: ")
cliente_socket.sendall(nome_cliente.encode('utf-8'))

while True:
    # Recebe a mensagem do servidor
    mensagem = cliente_socket.recv(1024).decode('utf-8')

    # Imprime a mensagem recebida
    if mensagem.startswith('LISTA'):
        # Se a mensagem for uma lista de clientes conectados, exiba a lista
        print("Clientes conectados:")
        for cliente in mensagem.split()[1:]:
            print(f"- {cliente}")
    else:
        # Se a mensagem não for uma lista, exiba a mensagem do cliente que a enviou
        print(mensagem)

    # Envia uma nova mensagem para o servidor
    mensagem_cliente = input()
    cliente_socket.sendall(mensagem_cliente.encode('utf-8'))
