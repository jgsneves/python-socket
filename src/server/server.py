import socket
import threading

class Server:
    def __init__(self, class_service) -> None:
        self.PORT = 5050
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.ADDRESS = (self.HOST, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.service = class_service

    def run(self):
        self.server.bind(self.ADDRESS)
        self.server.listen()
        print('Servidor está escutando...')
        while True:
            connection, client = self.server.accept()
            print('Cliente conectado: ', client)
            thread = threading.Thread(target=self.handle_connection, args=(connection, client))
            thread.start()

    def handle_connection(self, connection: socket, _):
        while True:
            data: bytes = connection.recv(1024)
            decoded_data = data.decode()
            response: str = self.service.handle_message(decoded_data)
            print(response)
            encoded_response = response.encode()
            connection.send(encoded_response)
