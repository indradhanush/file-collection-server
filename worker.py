"""
Worker for File-Collection Server.
Implements the Majordomo Protocol.
Author: Indradhanush Gupta
Github: https://github.com/indradhanush
Twitter: https://twitter.com/Indradhanush92
Facebook: https://www.facebook.com/Indradhanush
"""


import zmq
from zmq.eventloop.ioloop import IOLoop
from mdp.worker import MDPWorker


ENDPOINT = "tcp://127.0.0.1:8888"
SERVICE = "FILE_TRANSFER" #To-Do: Modify to allow more than one service


class Worker(MDPWorker):

    def on_request(self, msg):
        print msg
        if msg[0] == "CONNECT":
            self.reply(b"CONNECT-OK")

def main():
    context = zmq.Context()
    mdp_worker = Worker(context, ENDPOINT, SERVICE)
    mdp_worker.HB_INTERVAL = 10
    IOLoop.instance().start()
    # mdp_worker.stop()
    
if __name__ == '__main__':
    main()
