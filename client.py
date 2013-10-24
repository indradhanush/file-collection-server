"""
Client for File-Collection Server.
Implements the Majordomo Protocol.
Author: Indradhanush Gupta
Github: https://github.com/indradhanush
Twitter: https://twitter.com/Indradhanush92
Facebook: https://www.facebook.com/Indradhanush
"""

import zmq

import os
import sys

#local
from mdp.mdpcliapi import MajorDomoClient
import mdp.MDP as MDP
from FILE_TRANSFER import N_FILE, S_FILE, R_FILE


ENDPOINT = "tcp://127.0.0.1:5555"
SERVICE = "FILE_TRANSFER" #To-Do: Modify to allow more than one service.

#MUST be absolute path. NOT relative path.
BASE_FILE_PATH = "/home/dhanush/file-collection-server/send_files/" 
CHUNK_SIZE = 20000

class Client(MajorDomoClient):
    pass
    

def files_to_send():
    """Returns a list of files or None if there are no files to send."""
    # TO DO: Implement a file poller
    for _, _, files in os.walk(BASE_FILE_PATH):
        return files

    
def main():
    verbose = '-v' in sys.argv
    mdp_client = Client(ENDPOINT, verbose)
    print "Connected"
    # while True: Rest of code to be in this infinite Loop.
    files = files_to_send()
    print files
    if files:
        for name in files:
            print "FILE: ", name
            file_size = os.path.getsize(os.path.join(BASE_FILE_PATH, name))
            request = [N_FILE, name, str(file_size)]
            mdp_client.send(SERVICE, request)
            print "Sent."
            while True:
                response = mdp_client.recv()
                print "Response: ", response
                if response is not None:
                    header = response.pop(0)
                    if header == S_FILE:
                        #Start sending the file: The first chunk.
                        print S_FILE
                        name = response.pop(0)
                        chunk = int(response.pop(0))
                        #name = os.path.join(BASE_FILE_PATH, name)
                        file = open(os.path.join(BASE_FILE_PATH, name), 'r')
                        file.seek(chunk, 0)
                        data = file.read(CHUNK_SIZE)
                        request = [S_FILE, name, str(chunk), data]
                        mdp_client.send(SERVICE, request)
        
                    elif header == R_FILE:
                        print R_FILE
                        name = response.pop(0)
                        break

                        
if __name__ == '__main__':
    main()

