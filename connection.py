import socket
from PyQt4 import QtCore, QtGui
import ssl
import os

class Connection(QtCore.QObject):

    server = ""
    port    = 0
    channel =  ""
    nick  = ""
    availables_to_chat = []
    sock = socket.socket()
    s =""
#    s = ssl.wrap_socket(sock,
#							ssl_version=ssl.PROTOCOL_TLSv1,
#                           ca_certs="server.crt",
#                           cert_reqs=ssl.CERT_NONE )
        #cert_reqs=ssl.CERT_NONE will disable the server certificate verification wich is dangerous it
        # should've been set to ssl.CERT_REQUIRED , but it's Ok in my case since i signed the certificate by myself
    def __init__(self,parent=None):
        super(Connection,self).__init__(parent)
        QtCore.QObject.connect(self, QtCore.SIGNAL("send_privmsg"), self.send_privmsg)


    def send_privmsg(self,text):
        self.s.send('privmsg '+self.channel+' :'+str(text).strip()+'\r\n')

    def communicate(self):
        if ((os.system("ls server.crt") == 0) and (self.port == 6697)):
            s = ssl.wrap_socket(self.sock,
							ssl_version=ssl.PROTOCOL_TLSv1,
                           ca_certs="server.crt",
                           cert_reqs=ssl.CERT_NONE )
#        self.s = socket.socket()
            s.connect_ex((self.server, self.port))
        else :
            s = self.sock
            self.port = 6667
            s.connect((self.server, self.port))

        s.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s \n" % {'nick':self.nick})
        s.send("NICK %s\n" % self.nick)
        while True:
            buf = s.recv(4096)
            lines = buf.split("\n")
            for data in lines:
                data = str(data).strip()
                if data == '':
                    continue   #you don't wanna waste your time treating empty texts
                #server ping pong
                if data.find('PING') != -1:
                    n = data.split(':')[1]
                    #print "n= ",n
                    s.send('PONG :' + n+'\n')
                    continue
                #handling joins and quits
                if data.find('JOIN :'+self.channel) != -1:
                    new_incomer = data.split('!')[0][1::].replace(" ","")
                 #   print 'new incomer['+new_incomer+']'
                    if new_incomer not in self.availables_to_chat:
                        self.availables_to_chat.append(new_incomer)
                        self.availables_to_chat.sort()
                        self.availables_to_chat=list(set(self.availables_to_chat))
                        self.emit(QtCore.SIGNAL("get_nicklist"), self.availables_to_chat)
                        self.emit(QtCore.SIGNAL("someone_joined"), new_incomer)
                    continue
                if data.find('QUIT :') != -1:
                    left = data.split('!')[0][1::].replace(" ","")
                    if left in self.availables_to_chat :
                        self.availables_to_chat.remove(left)
                    if "@"+left in self.availables_to_chat :
                        self.availables_to_chat.remove("@"+left)
                    self.availables_to_chat.sort()
                    self.availables_to_chat=list(set(self.availables_to_chat))
                    self.emit(QtCore.SIGNAL("get_nicklist"), self.availables_to_chat)
                    self.emit(QtCore.SIGNAL("someone_quit"), left)

                    continue
                self.emit(QtCore.SIGNAL("received_data"), data)
                #print "I<", data
                if (("MODE "+self.nick+" +" in data) or ("MODE "+self.nick in data)):
                    s.send("JOIN %s\n" % self.channel)
                if "353" in data:
                    nicks = data.split(self.channel + " :")[1].split(" ")
                    self.availables_to_chat += nicks
                    self.availables_to_chat.sort()
                    self.availables_to_chat=list(set(self.availables_to_chat))
                    self.emit(QtCore.SIGNAL("get_nicklist"), self.availables_to_chat)
                if "End of /NAMES list." in data:
                    self.emit(QtCore.SIGNAL("clear_chat_history"))








