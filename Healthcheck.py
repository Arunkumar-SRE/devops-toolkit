import os
import socket

def check_server_health():
    server_ip="127.0.0.1"
    server_port=8000

    try:
        socket.create_connection((server_ip,server_port),timeout=5)
        print(f"server{server_ip}:{server_port} is up")
    except(socket.timeout,socket.error):
        print(f"Server{server_ip}:{server:port} is down")

if __name__ == "__main__":
    check_server_health()