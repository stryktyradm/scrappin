# DOC:https://docs.python.org/3/library/socket.html
# HABR: https://habr.com/ru/post/149077/
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content)
print('START HTTP MESSAGE:')
print(content)
print('END MESSAGE')
sock.send(content.encode())
response = sock.recv(10024)
sock.close()
print(response.decode())
