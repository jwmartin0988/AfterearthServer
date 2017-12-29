import socketserver
import os

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])


    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((ip, port), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print("Server Started...")
    server.serve_forever()