# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created: Thu Jul 17 12:37:21 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_chat(QtCore.QObject):
    def __init__(self,client,parent=None):
        super(Ui_chat,self).__init__(parent)
        self.client = client
    def setupUi(self, chat):
        self.window = chat
        chat.setObjectName(_fromUtf8("chat"))
#        chat.resize(602, 477)
        chat.resize(900,500)
        self.textEdit = QtGui.QTextEdit(chat)
#        self.textEdit.setGeometry(QtCore.QRect(10, 10, 481, 421))
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 780, 421))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.channel = QtGui.QLabel(chat)
        self.channel.setGeometry(QtCore.QRect(0, 450, 99, 20))
        self.channel.setText(_fromUtf8(""))
        self.channel.setObjectName(_fromUtf8("channel"))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily(_fromUtf8("Droid Sans Mono"))
        self.channel.setFont(font)
        self.input = QtGui.QLineEdit(chat)
        self.input.setGeometry(QtCore.QRect(100, 450, 700, 25))
        self.input.setObjectName(_fromUtf8("input"))
        self.send = QtGui.QPushButton(chat)
        self.send.setGeometry(QtCore.QRect(800, 450, 92, 25))
        self.send.setObjectName(_fromUtf8("send"))
        self.widget = QtGui.QWidget(chat)
#        self.widget.setGeometry(QtCore.QRect(510, 20, 81, 411))
        self.widget.setGeometry(QtCore.QRect(800, 20, 81, 411))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.user1 = QtGui.QLabel(self.widget)
        self.user1.setObjectName(_fromUtf8("user1"))
        self.verticalLayout.addWidget(self.user1)
        self.user2 = QtGui.QLabel(self.widget)
        self.user2.setObjectName(_fromUtf8("user2"))
        self.verticalLayout.addWidget(self.user2)
        self.user3 = QtGui.QLabel(self.widget)
        self.user3.setObjectName(_fromUtf8("user3"))
        self.verticalLayout.addWidget(self.user3)
        self.user4 = QtGui.QLabel(self.widget)
        self.user4.setObjectName(_fromUtf8("user4"))
        self.verticalLayout.addWidget(self.user4)
        self.user5 = QtGui.QLabel(self.widget)
        self.user5.setObjectName(_fromUtf8("user5"))
        self.verticalLayout.addWidget(self.user5)
        self.user6 = QtGui.QLabel(self.widget)
        self.user6.setObjectName(_fromUtf8("user6"))
        self.verticalLayout.addWidget(self.user6)
        self.user7 = QtGui.QLabel(self.widget)
        self.user7.setObjectName(_fromUtf8("user7"))
        self.verticalLayout.addWidget(self.user7)
        self.user8 = QtGui.QLabel(self.widget)
        self.user8.setObjectName(_fromUtf8("user8"))
        self.verticalLayout.addWidget(self.user8)
        self.user9 = QtGui.QLabel(self.widget)
        self.user9.setObjectName(_fromUtf8("user9"))
        self.verticalLayout.addWidget(self.user9)
        self.user10 = QtGui.QLabel(self.widget)
        self.user10.setObjectName(_fromUtf8("user10"))
        self.verticalLayout.addWidget(self.user10)
        self.user11 = QtGui.QLabel(self.widget)
        self.user11.setObjectName(_fromUtf8("user11"))
        self.verticalLayout.addWidget(self.user11)
        self.user12 = QtGui.QLabel(self.widget)
        self.user12.setObjectName(_fromUtf8("user12"))
        self.verticalLayout.addWidget(self.user12)
        self.user13 = QtGui.QLabel(self.widget)
        self.user13.setObjectName(_fromUtf8("user13"))
        self.verticalLayout.addWidget(self.user13)
        self.user14 = QtGui.QLabel(self.widget)
        self.user14.setObjectName(_fromUtf8("user14"))
        self.verticalLayout.addWidget(self.user14)
        self.user15 = QtGui.QLabel(self.widget)
        self.user15.setObjectName(_fromUtf8("user15"))
        self.verticalLayout.addWidget(self.user15)

        self.retranslateUi(chat)

#signals and slots connection

        QtCore.QMetaObject.connectSlotsByName(chat)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("received_data"), self.update_screen)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("get_nicklist"), self.update_nicklist)
        QtCore.QObject.connect(self.send, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_privmsg)
        QtCore.QObject.connect(self.input, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.send_privmsg)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL(_fromUtf8("clear_chat_history")), self.clear_chat)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("someone_quit"), self.nick_left)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL("someone_joined"), self.nick_joined)


    def retranslateUi(self, chat):
        chat.setWindowTitle(QtGui.QApplication.translate("chat", "Chat Winodw", None, QtGui.QApplication.UnicodeUTF8))
        self.send.setText(QtGui.QApplication.translate("chat", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.user1.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user2.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user3.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user4.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user5.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user6.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user7.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user8.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user9.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user10.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user11.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user12.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user13.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user14.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))
        self.user15.setText(QtGui.QApplication.translate("chat", "", None, QtGui.QApplication.UnicodeUTF8))

    def show(self):
        self.window.show()
    def hide(self):
        self.window.hide()

    def update_screen(self,string):
#        print "******************************************************"
#        print "update string called with parameter ",string
        sender=str(string).split('!')[0][1::]
        message = str(string).split(str(self.client.channel)+" :")[-1]
        self.textEdit.insertPlainText("<"+sender+">"+message+"\n"  )
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.channel.setText(str(self.client.channel))
#        chat.setWindowTitle(QtGui.QApplication.translate("chat", str(self.client.nick), None, QtGui.QApplication.UnicodeUTF8))

    def send_privmsg(self):
        self.client.emit(QtCore.SIGNAL("send_privmsg"), self.input.text())
        self.textEdit.insertPlainText("<"+self.client.nick+">"+self.input.text()+"\n")
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.input.clear()

    def clear_chat(self):
        self.textEdit.clear()

    def nick_left(self,who):
        self.textEdit.insertPlainText("\n---------->  "+ who + "  left the channel  <----------\n")
    def nick_joined(self,who):
        self.textEdit.insertPlainText("\n---------->  "+ who + "  joined the channel  <----------\n")

    def update_nicklist(self,nicklist):
        if len(nicklist) < 15:
            for i in range(len(nicklist),16):
                nicklist.append("")
        #print nicklist
        self.user1.setText(nicklist[0])
        self.user2.setText(nicklist[1])
        self.user3.setText(nicklist[2])
        self.user4.setText(nicklist[3])
        self.user5.setText(nicklist[4])
        self.user6.setText(nicklist[5])
        self.user7.setText(nicklist[6])
        self.user8.setText(nicklist[7])
        self.user9.setText(nicklist[8])
        self.user10.setText(nicklist[9])
        self.user11.setText(nicklist[10])
        self.user12.setText(nicklist[11])
        self.user13.setText(nicklist[12])
        self.user14.setText(nicklist[12])
        self.user15.setText(nicklist[14])



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    chat = QtGui.QWidget()
    ui = Ui_chat()
    ui.setupUi(chat)
    chat.show()
    sys.exit(app.exec_())

