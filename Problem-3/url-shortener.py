from logging import raiseExceptions
import socket
from datetime import datetime
from execute_psql import execute_psql
import psycopg2
import validators

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(0)
print(f'Listening on port {SERVER_PORT}')
 
# Accepts a http request and returns a timezone if provided, else returns UTC
def get_request_data(request):
    lines = request.split("\r\n")
    request_line = lines[0]
    words = request_line.split(" ")
    if len(words) > 1:
        URI = words[1]
        splitURL = URI.split("url=")
        if len(splitURL) > 1:
            # create new short url
            return ("create", splitURL[1])
        if len(splitURL) == 1:
            splitURL = URI.split("/")
            # create new short url
            if len(splitURL[1]) == 5:
                return ("fetch", splitURL[1])
            elif splitURL[1] == 'favicon.ico':
                return 'favicon'
            else:
                return None

    return 'hello'

def increment_url(previous_url):
    new_url = list(previous_url)
    for index,value in enumerate(new_url):
        if value != 'z':
            new_url[index] = chr(ord(value) + 1)
            break
        else:
            new_url[index] = 'a'
    return ''.join(new_url)

def get_next_url():
    previous_url = execute_psql('recent')
    if previous_url is None:
        previous_url = 'aaaaa'
    return increment_url(previous_url)   

while True:    

    # Set socket to accept connections
    client_connection, client_address = server_socket.accept()

    # Decode the request
    request = client_connection.recv(1024).decode()
    command = None
    request_data = get_request_data(request)
    if request_data == None:
        response = f"HTTP/1.0 200 OK\n\nThat is not a valid short URL"

    elif request_data != 'favicon':
        command, value = request_data
        if command == 'fetch':
            # redirect to long url
            # response_text = f'command: {command}, value: {value}'
            psql_response = execute_psql('fetch', "", value)
            response = f"HTTP/1.1 301 \r\Referrer: {psql_response}\rLocation: {psql_response}"
            client_connection.sendall(response.encode())
            client_connection.close()
        elif command == 'create':
            if validators.url(value) != True:
                response_text = f"That is not a valid original URL"
            else:
                short_url = get_next_url()
                psql_response = execute_psql('create', value, short_url)
                response_text = f"Your new short url is http://localhost:8000/{short_url}"
    if (command != 'fetch'):
        try:
            response = f"HTTP/1.0 200 OK\n\n{response_text}"
        except:
            response = f"HTTP/1.0 404 OK\n\nNo response text assigned"

        client_connection.sendall(response.encode())
        client_connection.close()
