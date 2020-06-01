# FTP-client-server-program
A simple FTP client server python program to send and receive files between two computers

#### Server side
Run ftpserver.py on the computer where you want to store and provide data to the client computer. This script presents you with the status of the client connection.

#### Client side
Run ftpclient.py on the computer from where you want to send or retrieve data to the server computer.
This script will present you a shell like experience where you can run command to send or retrieve files to the server computer. The list of commands are given below,
##### Commands
 * pull filename     
[It sends the file to the server computer.] 
 * push filename       
[It retrievs the file from the server computer.] 


### IMPORTANT 
1. Change the host value in the ftpclient.py script to the private ip address of the server computer.
2. Change the username and the password values in the ftpserver.py to the client side username and password. You can provide any values.
3. Change the username and the password values in the ftpclient.py to the values you set in the ftpserver.py.

**NOTE** - As mentioned in the second line of this description, this is a simple FTP server & client implementation. It is a work in progress. 
