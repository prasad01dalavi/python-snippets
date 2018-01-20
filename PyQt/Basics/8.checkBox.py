import sys
from PyQt4 import QtGui,QtCore           #QtCore is for adding button
import time

class Window(QtGui.QMainWindow):         #Making a class with name Window

    def __init__(self):                  #Constructor which will be automatically called at the time of instance creation
        super(Window,self).__init__()    #Feature of Inheritance  (need to look at this)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))
        
        self.menuBarSetting()
        self.buttonSetting()               #Reference to the method home i.e. simply calling the method
        self.toolBarSetting()
        self.checkBoxSetting()
        self.show()
#-------------------------Menu Bar Setting-------------------------------------------#        
    def menuBarSetting(self):
        extractAction = QtGui.QAction('&Close the window',self)
        extractAction.setShortcut('Ctrl+Q')                     #short cut to do the same thing
        extractAction.setStatusTip('Window will be closed.')    #Working tip of the menu option 
        extractAction.triggered.connect(QtCore.QCoreApplication.instance().quit)     #When the option is selected do this

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu1 = mainMenu.addMenu('&File')
        fileMenu2 = mainMenu.addMenu('&Edit')
        fileMenu3 = mainMenu.addMenu('&Format')
        fileMenu4 = mainMenu.addMenu('&Run')
        fileMenu1.addAction(extractAction)       #Provides the option for menu1 i.e. declared as File                                   

#--------------------End of Menu Bar Setting----------------------------------------------#                                      

#------------------------Button Setting-----------------------------------------------#        
    def buttonSetting(self):
        btn = QtGui.QPushButton("Button Name",self)    #give a name to the button
        btn.clicked.connect(self.buttonMessage) #do when the button is clicked
        btn.resize(70,30)                       #size of the button (can be default)
        btn.move(210,150)                       #button position width X height

    def buttonMessage(self):
        print "Button is pressed"
        choice = QtGui.QMessageBox.question(self,'Title of The Window',
                                            'Do you want to execute pop up ?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)   #Can be Yes,No,Ok
        if choice == QtGui.QMessageBox.Yes:            
            print 'PoP Up is executed !'   
        else:
            print 'PoP Up is Cancelled !'

##        sys.exit()                     #this is like break. If i do not write it will be continuously executed
#------------------------End of Button Setting-------------------------------#

#------------------------Tool Bar Setting-----------------------------------#
    def toolBarSetting(self):
        extractAction = QtGui.QAction(QtGui.QIcon('tools.jpg'),'Tool Info',self)  #I can place icon for tool or leave the parameter
        extractAction.triggered.connect(self.toolMessage)

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)
        
    def toolMessage(self):
        print 'Tool is selected'
##        sys.exit()    #closes the window
#------------------End of toolbar setting-------------------------------#

#-------------------------Check Box--------------------------------------#
    def checkBoxSetting(self):
        checkBox = QtGui.QCheckBox('Enlarge Window',self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)  #if window is ticked then go to enlarge function
        
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            print 'Check Box is ticked.'
            self.setGeometry(50,50,1000,600)
        else:
            print 'Check Box is unticked.'
            self.setGeometry(50,50,500,300)    
        
#-----------------End of check Box-------------------------------------#

#----------------------End of Class Window-----------------------------------------------------------------#
           
def runApp():                             #Important to define a method without that it will not work. It's astonishing
    app = QtGui.QApplication(sys.argv) #Creates window app
    GUI = Window()                     #GUI is an object/instance of a class Window
    sys.exit(app.exec_())              #makes my app stable and responding            

runApp()
