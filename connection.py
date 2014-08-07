import socket
from PyQt4 import QtCore, QtGui
import time

class Connection(QtCore.QObject):

    server = ""
    port    = 0
    channel =  ""
    nick  = ""
    availables_to_chat = []
    s = socket.socket()
    def __init__(self,parent=None):
        super(Connection,self).__init__(parent)
        QtCore.QObject.connect(self, QtCore.SIGNAL("send_privmsg"), self.send_privmsg)


    def send_privmsg(self,text):
        self.s.send('privmsg '+self.channel+' :'+str(text).strip()+'\r\n')

    def communicate(self):
#        self.s = socket.socket()
        self.s.connect((self.server, self.port))
        self.s.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s \n" % {'nick':self.nick})
        self.s.send("NICK %s\n" % self.nick)
        while True:
            buf = self.s.recv(4096)
            lines = buf.split("\n")
            for data in lines:
                data = str(data).strip()
                if data == '':
                    continue   #you don't wanna waste your time treating empty texts
                #server ping pong
                if data.find('PING') != -1:
                    n = data.split(':')[1]
                    print "n= ",n
                    self.s.send('PONG :' + n+'\n')
                    continue
                #handling joins and quits
                if data.find('JOIN :'+self.channel) != -1:
                    new_incomer = data.split('!')[0][1::]
                 #   print 'new incomer['+new_incomer+']'
                    if new_incomer not in self.availables_to_chat:
                        self.availables_to_chat.append(new_incomer)
                        self.availables_to_chat.sort()
                        self.availables_to_chat=list(set(self.availables_to_chat))
                        self.emit(QtCore.SIGNAL("get_nicklist"), self.availables_to_chat)
                    continue
                if data.find('QUIT :') != -1:
                    left = data.split('!')[0][1::]
                    self.availables_to_chat.remove(left)
                    self.availables_to_chat.sort()
                    self.availables_to_chat=list(set(self.availables_to_chat))
                    self.emit(QtCore.SIGNAL("get_nicklist"), self.availables_to_chat)
                    continue
                self.emit(QtCore.SIGNAL("received_data"), data)
                print "I<", data
                if (("MODE "+self.nick+" +" in data) or ("MODE "+self.nick in data)):
                    self.s.send("JOIN %s\n" % self.channel)
                if "353" in data:
                    nicks = data.split(self.channel + " :")[1].split(" ")
                    self.availables_to_chat += nicks
                    self.availables_to_chat.sort()
                    self.availables_to_chat=list(set(self.availables_to_chat))
                    self.emit(QtCore.SIGNAL("get_nicklist"), self.availables_to_chat)
                if "End of /NAMES list." in data:
                    self.emit(QtCore.SIGNAL("clear_chat_history"))








