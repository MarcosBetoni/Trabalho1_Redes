import socket
import threading

HOST = 'localhost'  # Endereço do servidor
PORT = 5000  # Porta de conexão

clientes_conectados = []  # Lista para armazenar sockets dos clientes conectados

def atender_cliente(cliente, endereco):
    while True:
        try:
            # Recebe a mensagem do cliente
            mensagem = cliente.recv(1024).decode('utf-8')

            # Imprime a mensagem recebida
            print(f"[Cliente {endereco}] {mensagem}")

            # Envia a mensagem para todos os clientes conectados, exceto para o cliente que a enviou
            for outro_cliente in clientes_conectados:
                if outro_cliente != cliente:
                    outro_cliente.sendall(f"[Cliente {endereco}] {mensagem}".encode('utf-8'))

        except:
            # Se ocorrer um erro, fecha a conexão com o cliente
            cliente.close()
            clientes_conectados.remove(cliente)
            break

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e porta
server_socket.bind((HOST, PORT))

# Coloca o socket em modo de escuta
server_socket.listen(5)

print(f"Servidor escutando em {HOST}:{PORT}")

while True:
    # Aceita uma nova conexão
    cliente_socket, endereco = server_socket.accept()

    # Adiciona o socket do cliente à lista de clientes conectados
    clientes_conectados.append(cliente_socket)

    # Cria uma thread para atender o cliente conectado
    thread = threading.Thread(target=atender_cliente, args=(cliente_socket, endereco))
    thread.start()

