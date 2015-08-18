__author__ = 'ccai'

import socket
from urlparse import urlparse
import sys
import time


def GetResource (url,wait):
    o = urlparse (url)
    resource  = o.path
    host = o.hostname
    port = o.port
    if (port == None):
        port = 80

    sRequest= "GET %s HTTP/1.1\r\nHost:%s \r\n\r\n" %(resource,host)
    print sRequest

    address = socket.gethostbyname(host)
    print address

    return sendrequest (address,sRequest,port,wait)



def DoPartialSend (s,message,wait):
    for submessage in message:
        s.send(submessage)
        time.sleep (float(wait))



def sendrequest (ipaddress,message,port,wait):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ipaddress,port))
    DoPartialSend (s,message,wait)
    data = s.recv(8192)
    s.close()
    return data




def main (argv):
    result = GetResource (argv[0],argv[1])
    print result


if __name__ == "__main__":
    print(sys.argv)
    starttime = time.time ()
    main (sys.argv[1:])
    elapsed_time = time.time () - starttime

    print elapsed_time




