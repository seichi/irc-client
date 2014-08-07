import sys
from main_ui import Ui_IRCClient
import main_ui
from PyQt4 import QtCore, QtGui
import connection
from chat import Ui_chat

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



app = QtGui.QApplication(sys.argv)
IRCClient = QtGui.QMainWindow()
IRCChat = QtGui.QMainWindow()
client = connection.Connection()
ui = Ui_IRCClient(client)
ui.setupUi(IRCClient)
ui.show()
chat = Ui_chat(client)
chat.setupUi(IRCChat)
QtCore.QObject.connect(ui, QtCore.SIGNAL(_fromUtf8("show_chat")),chat.show)
sys.exit(app.exec_())
