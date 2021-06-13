import socket
import threading
import sys

def read_msg(sock_cli):
    while True:
        #terima pesan
        data = sock_cli.recv(65535)
        if len(data)==0:
            break
        print(data)

#buat object socket
sock_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect ke server
sock_cli.connect(("127.0.0.1",6666))

#kirim username ke server
sock_cli.send(bytes(sys.argv[1], "utf-8"))

#buat thread untuk membaca pesan dan jalankan threadnya
thread_cli = threading.Thread(target=read_msg, args=(sock_cli,))
thread_cli.start()

while True:
    #kirim / terima pesan
    dest = input("Masukkan username tujuan (ketikka bcast untuk broadcast atau addFriend untuk tambahkan teman): ")
    if dest=="addFriend":
        msg = input("Masukkan username yang ingin dijadikan teman: ")
    else:
        msg = input("Masukkan pesan anda: ")

    if(msg=="exit"):
        sock_cli.close()
        break
    
    sock_cli.send(bytes("{}|{}".format(dest,msg), "utf-8"))
