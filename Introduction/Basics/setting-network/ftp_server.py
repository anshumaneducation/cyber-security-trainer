
# ftp_server.py

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

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
