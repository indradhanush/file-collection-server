"""
Client for File-Collection Server.
Implements the Majordomo Protocol.
Author: Indradhanush Gupta
Github: https://github.com/indradhanush
Twitter: https://twitter.com/Indradhanush92
Facebook: https://www.facebook.com/Indradhanush
"""

import zmq
from mdp.client import MDPClient, RequestTimeout, mdp_request


ENDPOINT = "tcp://127.0.0.1:8887"
SERVICE = "FILE_TRANSFER" #To-Do: Modify to allow more than one service.

class Client(MDPClient):

    def on_timeout(self):
        print "Raising exception."
        raise RequestTimeout()

    def on_message(self, msg):
        print msg
        return

def send_request(socket, service, response=None):
    if not response:
        return mdp_request(socket, service, ["CONNECT"], 2)
    elif response == "CONNECT-OK":
        # file, name, size = get_file()
        # return mdp_request(socket, service, ["SEND", name, str(size)], 2)
        pass
        
def main():
    context = zmq.Context()
    mdp_client = Client(context, ENDPOINT, SERVICE)
    mdp_client.request(["CONNECT"])
    print 'Request...'

    # Connect to server
    # response = mdp_request(mdp_client.stream.socket, SERVICE, ["CONNECT"], 2)
    # response = send_request(mdp_client.stream.socket, SERVICE)
    # if response is not None:
    #     service, response = response
    # else:
    #     print "Request Timed Out."
    #     return
    # while True:
    #     if service == SERVICE:
            # print response
            # response = send_request(mdp_client.stream.socket, service, response)
            # raw_input()


if __name__ == '__main__':
    main()





