from ftplib import FTP


def create_connection():
	ftp.connect(host='192.168.1.8', port=2120)
	ftp.login(user="dhanush", passwd="1122")
	get_command()
	
def get_command():
	while True:
		cmd = input(">>")
		cmd_array = cmd.split(" ")
		if cmd_array[0] == "push":
			upload(cmd_array[1])
		elif cmd_array[0] == "pull":
			download(cmd_array[1])
		elif cmd_array[0] == "exit":
			break
			
def upload(filename):
	ftp.storbinary('STOR '+filename, open(filename, 'rb'))
	
def download(filename):
	file = open(filename, 'wb')
	ftp.retrbinary('RETR '+filename, file.write, blocksize=1024)
	
	
	
	
if __name__ == "__main__":
	ftp = FTP()
	create_connection()
