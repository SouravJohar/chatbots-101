from rivescript import RiveScript

ly = RiveScript()
ly.load_directory("bro_brain/")
ly.sort_replies()


while True:
    msg = raw_input("You> ")
    if msg == '/quit':
        quit()
    reply = ly.reply("localuser", msg)
    print "Bot>", reply



'''
flow

query -> check command and serice if true -> check psuedo command and service
