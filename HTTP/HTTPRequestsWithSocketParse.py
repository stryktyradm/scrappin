import socket


def parse_response(res):
    text_response = res.split('\n')
    status, lines = text_response[0], text_response[1:]
    protocol, status_code, message = status.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()

        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        key, _, value = line.partition(':')
        headers.setdefault(key.strip(), value.strip())
    content = ''.join(lines[empty_index+1:])
    return int(status_code), headers, content


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
status_code, headers, content = parse_response(response.decode())
print(f'Status code: {status_code}')
print(f'Headers: {headers}')
print(content)
