from __future__ import unicode_literals
from bot import *


updateID = None
print "\nfiring up"
while True:
    latestQuery = getUpdates(updateID)
    for query in latestQuery:
        updateID, query = parseQuery(query)
        try:
            print "from:", query[2], "message:", query[0]
        except:
            pass
        if query[0] is not None:
            reply = process(query[0])
            sendMessage(reply, query[2])
            print "reply sent"
