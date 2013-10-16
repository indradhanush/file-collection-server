"""
Broker for File-Collection Server.
Implements the Majordomo Protocol.
Author: Indradhanush Gupta
Github: https://github.com/indradhanush
Twitter: https://twitter.com/Indradhanush92
Facebook: https://www.facebook.com/Indradhanush
"""

import zmq
from zmq.eventloop.ioloop import IOLoop
from mdp.broker import MDPBroker


FRONT_ENDPOINT = "tcp://127.0.0.1:8887"  #The endpoint to serve clients.
BACK_ENDPOINT = "tcp://127.0.0.1:8888"  #The endpoint to serve workers.
SERVICE = "FILE_TRANSFER" #To-Do: Modify to allow more than one service.


class Broker(MDPBroker):
    
    # def on_heartbeat(self, rp, msg):
    #     print 'Heartbeat..', rp
    #     return
    pass

def main():
    context = zmq.Context()
    mdp_broker = Broker(context, BACK_ENDPOINT, FRONT_ENDPOINT)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
