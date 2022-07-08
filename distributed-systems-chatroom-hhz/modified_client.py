from src import clientUtils
from src import utility
import threading

# creates a list of all the functions to be passed to the thread
list_of_threads = ["clientUtils.transmit_messages","clientUtils.tcp_listener", "clientUtils.multicast_listener"]

class Client : 
    # initial funtion that gets executed
    def __init__(self) :
        utility.cls()
        clientUtils.broadcast_for_server()
    # function which collects the threads and runs them
    def look_for_servers(self, list_threads) :
        # loops through the 'list_threads' list
        for thread in list_threads : 
            # adds each of the functions to a thread in the variable 't1'
            t1 = threading.Thread(target=eval(thread))
            # starts the thread
            t1.start()

if __name__ == "__main__"  : 
    # checks if the program is not executed anywhere else
    # creates an object client which is an instance of the class Server 
    client = Client()
    # uses the instance 'client'  to invoke run 'look_for_servers' function
    client.look_for_servers(list_threads=list_of_threads)