import sys
from PyQt4 import QtGui,QtCore           #QtCore is for adding button

class Window(QtGui.QMainWindow):         #Making a class with name Window

    def __init__(self):                  #Constructor which will be automatically called at the time of instance creation
        super(Window,self).__init__()    #Feature of Inheritance  (need to look at this)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('My Python App')
        self.setWindowIcon(QtGui.QIcon('python.png'))
        
        print 'Welcome to My First Python App !'
        
        self.menuBarSetting()
        self.buttonSetting()               #Reference to the method home i.e. simply calling the method
        self.toolBarSetting()
        self.checkBoxSetting()
        self.progressBarSetting()
        self.dropDownStyles()
        self.fontWidget()
        self.colorPickerWidget()
        
        self.show()
                                    
        
#-------------------------Menu Bar Setting-------------------------------------------#        
    def menuBarSetting(self):
        extractAction = QtGui.QAction('&Close the window',self)
        extractAction.setShortcut('Ctrl+Q')                     #short cut to do the same thing
        extractAction.setStatusTip('Window will be closed.')    #Working tip of the menu option 
        extractAction.triggered.connect(QtCore.QCoreApplication.instance().quit)     #When the option is selected do this

        self.statusBar()
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)       #Provides the option for menu1 i.e. declared as File

        #----------opening Files------------------------------------------------#
        openFile = QtGui.QAction('&Open File',self)
        openFile.setShortcut('Ctrl+o')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.fileOpen) #file open function is defined below

        fileMenu.addAction(openFile)
        #-------------End of opening Files---------------------------------------------#

    
        #------------------------------Editor----------------------------------------#
        openEditor = QtGui.QAction('&Editor',self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)
        
        editorMenu = mainMenu.addMenu('&Edit')
        editorMenu.addAction(openEditor)

    def fileOpen(self):
        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')  #title open file
        file = open(name,'r')

        self.editor()   #Will open the file in editor

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        #---------------------------End of Editor----------------------------------------#

#-------------------End of Menu Bar Setting----------------------------------------------#                                      

#------------------------Button Setting-----------------------------------------------#        
    def buttonSetting(self):
        btn = QtGui.QPushButton("Button Name",self)    #give a name to the button
        btn.clicked.connect(self.buttonMessage)        #do when the button is clicked
        btn.resize(70,30)                              #size of the button (can be default)
        btn.move(100,120)                              #button position width X height

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
        self.toolBar.addAction(extractAction)         #Adding jpg file i.e an object to the toolbar
                
    def toolMessage(self):
        print 'Tool is selected'

##        sys.exit()    #closes the window
#------------------End of toolbar setting-------------------------------#

#-------------------------Check Box--------------------------------------#
    def checkBoxSetting(self):
        checkBox = QtGui.QCheckBox('Enlarge Window',self)
        checkBox.move(250,25)    #it's not added to the toolbar but actually put on the toolbar
        checkBox.stateChanged.connect(self.enlarge_window)  #if window is ticked then go to enlarge function
        
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            print 'Check Box is ticked.'
            self.setGeometry(50,50,1000,600)
        else:
            print 'Check Box is unticked.'
            self.setGeometry(50,50,500,300)    
        
#-----------------End of check Box-------------------------------------#

#--------------Progress Bar--------------------------------------------#

    def progressBarSetting(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(250,60,250,20)    #dist from left,dist from up,length of the bar,height of the bar

        self.btn = QtGui.QPushButton('Download',self)
        self.btn.move (250,90)                     #dist from left, dist from up
        self.btn.clicked.connect(self.download)

    def download(self):
        self.completed = 0
        print 'Downloading Started...'

        while self.completed < 100:            
            self.completed +=0.00005
            self.progress.setValue(self.completed)   #I will get percentage of the completed value
        print 'Download Complete !'
        choice = QtGui.QMessageBox.information(self,'Download Status',   #question,information,warning,critical
                                            'Download Completed !',
                                            QtGui.QMessageBox.Ok)   #Can be Yes,No,Ok
        if choice == QtGui.QMessageBox.Ok:            
            print 'Download PoP Up is executed !'   
        else:
            pass
#-----------------End of Progress Bar---------------------------------#

#----------------------Drop Downs and Styles----------------------------#
    def dropDownStyles(self):
##        print 'Current Styles:',self.style().objectName()                 #Currently used style
        self.styleChoice = QtGui.QLabel('Styles:',self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(50, 250)
        self.styleChoice.move(50,220)
        comboBox.activated[str].connect(self.style_choice)  

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

#---------------End of Drop Downs and Styles-----------------------------#

#-------------------------Font Widget-------------------------------------------#
    def fontWidget(self):
        fontChoice = QtGui.QAction('Font Styles',self)  #Name for the font menu is given as Font
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar.addAction(fontChoice)         #add fontChoice object to the toolbar
##        self.toolBar = self.addToolBar('Font')   #This will make font tool movable which is not good actually        
        
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
#---------------------Enf of Font Widget---------------------------------------#

#-----------------------Color picker widget and Calender------------------------------------#

    def colorPickerWidget(self):
        color = QtGui.QColor(0,0,0)   #font color set to Black....!!!??? not happy with this
        fontColor = QtGui.QAction('Font Background Color',self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)    #add fontColor object to the toolbar

        cal = QtGui.QCalendarWidget(self)
        cal.move(280,135)           #280 from left,135 from up
        cal.resize(140,140)         #base X height

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color:%s}' % color.name())


#-------------------------End of color picker widget and Calender--------------------#



#----------------------End of Class Window-------------------------------------#
           
def runApp():                          #Important to define a method without that it will not work. It's astonishing
    app = QtGui.QApplication(sys.argv) #Creates window app
    GUI = Window()                     #GUI is an object/instance of a class Window
    sys.exit(app.exec_())              #makes my app stable and responding            

runApp()
