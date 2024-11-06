# ftp_server.py
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run(server_class=FTPServer, port=21):
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.', perm='elradfmwM')
    authorizer.add_anonymous('.')
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    server = server_class(('', port), handler)
    print(f'Starting FTP server on port {port}...')
    server.serve_forever()

if __name__ == "__main__":
    run()
