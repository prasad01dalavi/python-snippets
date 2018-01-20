import sys
from PyQt4 import QtGui,QtCore             

class Window(QtGui.QMainWindow):           

    def __init__(self):                    
        super(Window,self).__init__()      
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Temperature Unit Converter')
        self.setWindowIcon(QtGui.QIcon('tempImage.png'))
        self.buttonSetting()          

        self.show()
        
    def buttonSetting(self):               
        btn1 = QtGui.QPushButton("Celsius to Fahrenheit >>>",self)
                                 #Give name to the button1
        btn1.clicked.connect(self.button1Click)        
        btn1.resize(200,30)      #size of the button (width, height)
        btn1.move(150,50)        #button position (from left,from up)

        btn2 = QtGui.QPushButton("<<< Fahrenheit to Celsius",self)
                                 #Give name to the button2
        btn2.clicked.connect(self.button2Click)        
        btn2.resize(200,30)      #size of the button(width, height)
        btn2.move(150,200)       #button position(from left,from up)


#--------------------Text box Setting---------------------------------#
        self.tempC = QtGui.QLineEdit(self)  #Create a fields to enter a data
        self.tempF = QtGui.QLineEdit(self)  #Create 2nd field
        
        self.tempC.resize(80,25)        #Size of textbox1(width,height)
        self.tempF.resize(80,25)        #Size of textbox2(width,height)
        
        self.tempC.move(50,130)         #textbox1 position(from left,from up)    
        self.tempF.move(350,130)        #textbox2 position(from left,from up)
#--------------------End of Text box Setting---------------------------#

#-------------------------Label Setting--------------------------------#
        self.celsius = QtGui.QLabel('° C',self)    #Give a Label 
        self.celsius.move(135,130)                 #Position of Label

        self.fahrenheit = QtGui.QLabel('° F',self) #Give a Label
        self.fahrenheit.move(435,130)              #Position of Label
#---------------------End of Label Setting-----------------------------#
 
    def button1Click(self):             #Class method
        numC = float(self.tempC.text()) #Convert string text to float
        numF = (numC*9/5) + 32          #Celsius to Fahrenheit Formula
        Fahrenheit = str(numF)          #Convert float to string text       
        self.tempF.setText(Fahrenheit)  #Display the text formatted result
        
    def button2Click(self):
        numF = float(self.tempF.text()) #Convert string text to float
        numC = (numF-32)*5/9            #Fahrenheit to Celsius Formula
        Celsius = str(numC)             #Convert float to string text
        self.tempC.setText(Celsius)     #Display the text formatted result

#-------------------End of Window Class----------------------------------------#

def runApp():                             
    app = QtGui.QApplication(sys.argv) 
    GUI = Window()                     
    sys.exit(app.exec_())                          

runApp()                               
