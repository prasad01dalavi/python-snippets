import sys                    #Import sys module
from PyQt4 import QtGui       #Import QtGui module which contains all graphical controls

app = QtGui.QApplication([])  #Instead of sys.argv I can pass empty parameters []
window = QtGui.QWidget()      #It creates a window
window.setGeometry(50,50,500,300)          #Size of the window (a,b,width,height)
window.setWindowTitle("My First GUI App")  #Give the title to the window
window.show()                 #Show the graphics
sys.exit(app.exec_())         #Important to make the window stable
