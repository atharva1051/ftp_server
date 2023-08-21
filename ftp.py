import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    current_dir = "./"
    
    import socket
    #ip_address = socket.gethostbyname(socket.gethostname())
    ip_address = "0.0.0.0"
    
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(current_dir, perm="elradfmw")  # elradfmw = read, write, list, delete, make directory, rename, file delete, and file write
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    server = FTPServer((ip_address, 2121), handler)
    
    print(f"FTP server started at {ip_address}:2121")
    
    try:
        server.serve_forever()
    
    except KeyboardInterrupt:
        print("\nFTP server stopped.")
    finally:
        server.close_all()

if __name__ == "__main__":
    run_ftp_server()
