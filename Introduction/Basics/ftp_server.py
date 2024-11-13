<<<<<<< HEAD
=======
# ftp_server.py
>>>>>>> 0bec01b071fca345744b304655bc863d895109b8
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

<<<<<<< HEAD
# Set up a simple user account
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", ".", perm="elradfmw")  # Username: user, Password: 12345

# Configure FTP handler with the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Set up and start the FTP server
server = FTPServer(("0.0.0.0", 21), handler)
print("FTP Server running on port 21...")
server.serve_forever()
=======
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
>>>>>>> 0bec01b071fca345744b304655bc863d895109b8
