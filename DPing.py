__author__ = 'ccai'

import os
import sys
from urllib2 import Request, urlopen, URLError
import json
from scapy.all import *

def GetResource (ipaddress):
    try:
        request = "http://ipinfo.io/%s/json"%ipaddress
        response = urlopen(request)
        return response.read()
    except URLError:
        print 'Not able to get the service.'



def GetHostInfo (ipaddress):
    ipinfo = json.loads (GetResource(ipaddress))
    asn="N/A"
    loc="N/A"
    name="N/A"

    if (ipinfo.get('org')):
        asn = ipinfo['org']
    if (ipinfo.get("loc")):
        loc = ipinfo['loc']
    if (ipinfo.get ('hostname')):
        name = ipinfo['hostname']

    return (ipaddress,name,asn,loc)



def main (hostname):
    for i in range(1, 20):
        pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
        reply = sr1(pkt, verbose=0,timeout=1,retry=3)

        if (reply is not None):
            hostinfo = GetHostInfo (reply.src)
            if (reply.type == 3):
               # We've reached our destination
               print "Done!", hostinfo
               break
            else:
               # We're in the middle somewhere
               print "%d hops away: " % i , hostinfo
        else:
            print "%d hops has no response" %i


if __name__ == "__main__":
    if len(sys.argv) <= 1:
       print "Usage: %s <File Name>" % sys.argv[0]
       sys.exit(1)
    main (sys.argv[1])

