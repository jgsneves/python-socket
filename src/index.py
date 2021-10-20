from server.server import Server
from services.service import Service

class_service = Service()

new_server = Server(class_service)

new_server.run()