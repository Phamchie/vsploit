import socket
import sys
import time

print('[+] starting server handler...')
time.sleep(3)

IP = '192.168.1.18'
PORT = 8080

def handler():
	session_handler = True
	while True:
		handler_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		handler_connect.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		handler_connect.bind((IP, PORT))
		handler_connect.listen(1)

		print(f'[+] server handler as started http://{IP}:{PORT}...')
		handler_socket, handler_address = handler_connect.accept()
		print(f'[+] {handler_address} has open link...')
		output_http = handler_socket.recv(1024).decode()
		html = """
	<html>
	<title>xin chào bạn</title>
	<h1>
	    hello wolrd
	</h1>
	<h2>
	    hello
	</h2>
	<body>
	    Xin chào bạn, rất vui được gặp bạn
	</body>
	<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Falun_Gong_Logo.svg/1200px-Falun_Gong_Logo.svg.png' width="300" height="300">"""
		
		response_http = 'HTTP/1.1 200 OK\r\n\r\n' + html
		handler_socket.sendall(response_http.encode())

		print(f'[+] {output_http}')

		handler_socket.close()

handler()
