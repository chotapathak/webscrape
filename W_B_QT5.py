from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
# I tried to fix it using Sys  So i import this after  
import sys


class MyWebBrowser(QMainWindow):  # I found QMainWindow Solution on GeeksofGeeks From My prespetive   
       
    def __init__(self):
       super.__init__()
        self.window = QWidget()
        self.window.setWindowTitle('alphas Oceans')

        self.layout = QVBoxLayout()
        self.layout = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton('Go')
        self.go_btn.setMinimumHeight(30) 

        self.back_btn = QPushButton('<')
        self.back_btn.setMinimumHeight(30) 

        self.forward_btn = QPushButton('>')
        self.forward_btn.setMinimumHeight(30) 
  # I think Error Starts from here
        self.Horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)      # This whole Section have First Error ( AttributeError: 'MyWebBrowser' object has no attribute 'Horizontal' )  
        self.horizontal.addWidget(self.forward_btn)
 # horizontal is BuiltIn function of PyQt  
        self.browser = QWebEngineView()
        

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl('http://google.com'))

        self.window.setLayout(self.layout)
        self.window.show()

App = QApplication(sys.argv) # sys.arg For (S.F)
window = QMainWindow(MyWebBrowser) 
#App.exec_()        
sys.exit(App.exec(sys.argv)) 
    