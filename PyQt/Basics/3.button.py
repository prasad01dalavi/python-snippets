import sys
from PyQt4 import QtGui,QtCore             #QtCore is for adding button

class Window(QtGui.QMainWindow):           #Making a class with name Window

    def __init__(self):                    #Constructor
        super(Window,self).__init__()      #Feature of Inheritance
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))
        self.buttonSetting()               #Call the Method or Function

    def buttonSetting(self):               
        btn = QtGui.QPushButton("Quit",self)    #Give name to the button
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #When button is clicked then (connect to) Quit or close the application
        btn.resize(70,30)       #size of the button (width, height)
        btn.move(210,150)       #button position (from left,from up)
        self.show()

#Important to define a method without that it will not work.
def runApp():                             
    app = QtGui.QApplication(sys.argv) #Creates window app
    GUI = Window()                     #GUI is an object/instance of a class Window
    sys.exit(app.exec_())              #Makes my app stable and responding            

runApp()                               #Call the method runApp 
