from __future__ import unicode_literals
import json
import requests

TOKEN = "324025303:AAGUuERiTV-He7BtGOI6dP1_Fvklb56DS24"


def getUpdates(offset=None):
    url = "https://api.telegram.org/bot{}/getUpdates?timeout=100".format(TOKEN)
    if offset:
        url = url + "&offset={}".format(offset + 1)
    r = requests.get(url)
    latestQuery = json.loads(r.content.decode("utf-8"))["result"]
    return latestQuery


def parseQuery(query):
    try:
        message = query["message"]["text"]
    except:
        message = None
    msgID = query["message"]["message_id"]
    chatID = query["message"]["from"]["id"]
    updateID = query["update_id"]
    query = (message, msgID, chatID)
    return updateID, query


def sendMessage(message, chatID):
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(
        TOKEN, chatID, message)
    r = requests.get(url)


def process(t):
    return t
