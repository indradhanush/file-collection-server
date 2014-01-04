"""
Worker for File-Collection Server.
Implements the Majordomo Protocol.
Author: Indradhanush Gupta
Github: https://github.com/indradhanush
Twitter: https://twitter.com/Indradhanush92
Facebook: https://www.facebook.com/Indradhanush
"""

import zmq

import sys
import os

#local
from mdp.mdpwrkapi import MajorDomoWorker
import mdp.MDP as MDP2
from FILE_TRANSFER import N_FILE, S_FILE, R_FILE


ENDPOINT = "tcp://127.0.0.1:5555"
SERVICE = "FILE_TRANSFER" #To-Do: Modify to allow more than one service

BASE_FILE_PATH = "/home/dhanush/file-collection-server/recv-files/"
CHUNK_SIZE = 20000


class Worker(MajorDomoWorker):
    pass
    

def main():
    verbose = '-v' in sys.argv
    print "Verbose:", verbose
    mdp_worker = Worker(ENDPOINT, SERVICE, verbose)
    reply = None
    count = 0

    while True:
        print "Count:", count
        count += 1
        response = mdp_worker.recv(reply)
        #print response
        header = response.pop(0)
        if header == N_FILE:
            print N_FILE
            name = response.pop(0)
            size = int(response.pop(0))
            print header, name, size
            offset = 0
            reply = [S_FILE, name, str(offset), str(CHUNK_SIZE)]

        elif header == S_FILE:
            print S_FILE
            name = response.pop(0);
            offset = int(response.pop(0))
            data = response.pop(0)
            file = open(os.path.join(BASE_FILE_PATH, name), 'ab+')
            file.write(data)
            file.close()
            if len(data) < CHUNK_SIZE:
                #Last Chunk received.
                reply = [R_FILE, name]
            else:
                offset += len(data)
                reply = [S_FILE, name, str(offset), str(CHUNK_SIZE)]

            
if __name__ == '__main__':
    main()





