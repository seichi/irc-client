# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Jul 17 12:06:22 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from connection import Connection

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_IRCClient(QtCore.QObject):
    def __init__(self, client):
        super(Ui_IRCClient,self).__init__()
        self.client = client

    def setupUi(self, IRCClient):
        self.show_chat = QtCore.pyqtSignal()
        self.window = IRCClient
        IRCClient.setObjectName(_fromUtf8("IRCClient"))
        IRCClient.resize(458, 469)
        self.centralwidget = QtGui.QWidget(IRCClient)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.server = QtGui.QLineEdit(self.centralwidget)
        self.server.setGeometry(QtCore.QRect(150, 90, 129, 25))
        self.server.setObjectName(_fromUtf8("server"))
        self.port = QtGui.QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(150, 150, 129, 25))
        self.port.setObjectName(_fromUtf8("port"))
        self.nickname = QtGui.QLineEdit(self.centralwidget)
        self.nickname.setGeometry(QtCore.QRect(150, 290, 129, 25))
        self.nickname.setObjectName(_fromUtf8("nickname"))
        self.channel = QtGui.QLineEdit(self.centralwidget)
        self.channel.setGeometry(QtCore.QRect(150, 220, 129, 25))
        self.channel.setObjectName(_fromUtf8("channel"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(80, 360, 92, 27))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 92, 66, 218))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.server_label = QtGui.QLabel(self.layoutWidget)
        self.server_label.setObjectName(_fromUtf8("server_label"))
        self.verticalLayout.addWidget(self.server_label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.port_label = QtGui.QLabel(self.layoutWidget)
        self.port_label.setObjectName(_fromUtf8("port_label"))
        self.verticalLayout.addWidget(self.port_label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.channel_label = QtGui.QLabel(self.layoutWidget)
        self.channel_label.setObjectName(_fromUtf8("channel_label"))
        self.verticalLayout.addWidget(self.channel_label)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.nickname_label = QtGui.QLabel(self.layoutWidget)
        self.nickname_label.setObjectName(_fromUtf8("nickname_label"))
        self.verticalLayout.addWidget(self.nickname_label)
        IRCClient.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(IRCClient)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IRCClient.setStatusBar(self.statusbar)
        self.actionQuick_Connect = QtGui.QAction(IRCClient)
        self.actionQuick_Connect.setObjectName(_fromUtf8("actionQuick_Connect"))
        self.actionDisconnet = QtGui.QAction(IRCClient)
        self.actionDisconnet.setObjectName(_fromUtf8("actionDisconnet"))
        self.actionReconnect = QtGui.QAction(IRCClient)
        self.actionReconnect.setObjectName(_fromUtf8("actionReconnect"))
        self.actionExit = QtGui.QAction(IRCClient)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionShow_menu_Bar = QtGui.QAction(IRCClient)
        self.actionShow_menu_Bar.setObjectName(_fromUtf8("actionShow_menu_Bar"))
        self.actionNext_tab = QtGui.QAction(IRCClient)
        self.actionNext_tab.setObjectName(_fromUtf8("actionNext_tab"))
        self.actionPrevious_tab = QtGui.QAction(IRCClient)
        self.actionPrevious_tab.setObjectName(_fromUtf8("actionPrevious_tab"))
        self.actionWhat_s_This = QtGui.QAction(IRCClient)
        self.actionWhat_s_This.setObjectName(_fromUtf8("actionWhat_s_This"))


        QtCore.QObject.connect(self.submit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_input)

        self.retranslateUi(IRCClient)
        QtCore.QMetaObject.connectSlotsByName(IRCClient)
        IRCClient.setTabOrder(self.server, self.port)
        IRCClient.setTabOrder(self.port, self.channel)
        IRCClient.setTabOrder(self.channel, self.nickname)
        IRCClient.setTabOrder(self.nickname, self.submit)

    def retranslateUi(self, IRCClient):
        IRCClient.setWindowTitle(QtGui.QApplication.translate("IRCClient", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("IRCClient", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.server_label.setText(QtGui.QApplication.translate("IRCClient", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.port_label.setText(QtGui.QApplication.translate("IRCClient", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.channel_label.setText(QtGui.QApplication.translate("IRCClient", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.nickname_label.setText(QtGui.QApplication.translate("IRCClient", "Nickname", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuick_Connect.setText(QtGui.QApplication.translate("IRCClient", "Quick Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnet.setText(QtGui.QApplication.translate("IRCClient", "Disconnet", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReconnect.setText(QtGui.QApplication.translate("IRCClient", "Reconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("IRCClient", "exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_menu_Bar.setText(QtGui.QApplication.translate("IRCClient", "Show menu Bar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_tab.setText(QtGui.QApplication.translate("IRCClient", "next tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious_tab.setText(QtGui.QApplication.translate("IRCClient", "previous tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWhat_s_This.setText(QtGui.QApplication.translate("IRCClient", "What\'s This", None, QtGui.QApplication.UnicodeUTF8))


    def get_input(self):
        self.client.server = str(self.server.text())
        self.client.port = int(self.port.text())
        self.client.channel = str(self.channel.text())
        if self.client.channel[0] != "#" :
           self.client.channel = "#" + self.client.channel
        self.client.nick = str(self.nickname.text())
        self.objThread = QtCore.QThread()
        self.client.moveToThread(self.objThread)
        self.objThread.started.connect(self.client.communicate)
        self.objThread.start()
        self.emit(QtCore.SIGNAL("show_chat"))
        self.window.hide()
#    def test(self):
#        print "testghhhhhhhhhhhhhhhhhhhhh"

    def show(self):
        self.window.show()
    def hide(self):
        self.window.hide()


#if __name__ == "__main__":
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    IRCClient = QtGui.QMainWindow()
#    ui = Ui_IRCClient()
#    ui.setupUi(IRCClient)
#    IRCClient.show()
#    sys.exit(app.exec_())

