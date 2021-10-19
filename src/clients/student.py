import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

msg = ''
clientCode = 'student'
is_running = True

def get_identified_msg(msg, clientCode):
    return f'{msg},{clientCode}'

while True:
    user_input = input()
    msg = str(user_input)
    encoded_package = str.encode(get_identified_msg(msg, clientCode))
    client.send(encoded_package)
