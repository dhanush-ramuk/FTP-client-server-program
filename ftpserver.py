from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def create_users():
	authorizer = DummyAuthorizer()
	authorizer.add_user(username="dhanush", password="1122", homedir=".", perm="elradfmw")	
	handler.banner = "connected"
	handler.authorizer = authorizer
	initiate_server()
	
def initiate_server():
	address = ("", 2120)
	server = FTPServer(address, handler)
	server.serve_forever()
	
	
if __name__ == "__main__":
	handler = FTPHandler
	create_users()
