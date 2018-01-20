import sys
from PyQt4 import QtGui,QtCore             #QtCore is for adding button

class Window(QtGui.QMainWindow):           #Making a class with name Window

    def __init__(self):                    #Constructor
        super(Window,self).__init__()      #Feature of Inheritance
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))
        self.buttonSetting()               #Reference to the method home i.e. simply calling the method

    def buttonSetting(self):
        btn = QtGui.QPushButton("Button",self)  #Give a name to the button
        btn.clicked.connect(self.buttonMessage) #Call method buttonMessage when the button is clicked
        btn.resize(70,30)                       #Size of the button (can be default)
        btn.move(210,150)                       #Button position (from left,from up)
        self.show()

    def buttonMessage(self):           
        print "Button is pressed"      #When button is clicked. We get the message on Python Shell
        
def runApp():                          #Important to define a method without that it will not work.
    app = QtGui.QApplication(sys.argv) #Creates window app
    GUI = Window()                     #GUI is an object/instance of a class Window
    sys.exit(app.exec_())              #makes my app stable and responding            

runApp()
