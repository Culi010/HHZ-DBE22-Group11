from src import serverUtils
from src import utility
import threading


# this is the dictionary which holds the calue of the function and its arguments
dict_of_thread_func = {"serverUtils.broadcast_listener" : "", "serverUtils.tcp_listener" : "" , "serverUtils.heartbeat" : "", "serverUtils.multicast_listener" : "utility.MG_SERVER" , "serverUtils.multicast_listener"  : "utility.MG_SERVER"}



class Server : 
    # initial funtion that gets executed
    def __init__(self) :
        utility.cls()
        serverUtils.startup_broadcast()
    # function which collects the threads and runs them
    def setup_listener(self,dict_threads) : 
        # loop through the 'dict_threads' dictionary
        for i in dict_threads : 
            # checks if the corresponding key in the dictionary has an argument or not
            if dict_threads[i] == "" :
                # the key does not have an argument
                # thread is created in the variable 't1', and starts it
                t1 = threading.Thread(target=eval(i))
                t1.start()
            else :      
                # the key has a value
                # thread is created in the variable 't1', and starts it
                t1 = threading.Thread(target=eval(i), args = (tuple(utility.MG_SERVER),))
                t1.start()

if __name__  == "__main__" :
    # checks if the program is not executed anywhere else
    # creates an object server which is an instance of the class Server 
    server = Server()
    # uses the instance 'server'  to invoke run 'setup_listener' function
    server.setup_listener(dict_threads=dict_of_thread_func)
