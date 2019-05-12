 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import PyQt5.QtCore as QtCore


import Shared.layout_info as layout

# TODO Extract out self.buttons from class and put data_info
class OptionsMenu(QWidget):
     
    def __init__(self, parent=None, activeModel=None):
        super(OptionsMenu,self).__init__(parent)
        self.buttons = ["Run Test", "Arduino", "Connect"]
        win = QWidget(self)
        win.resize(layout.optionsW, layout.optionsH)
        win.move(0,0)
        self.paramInputs = []
        self.paramLabels = []
        self.activeDataModel = activeModel
        fbox = QFormLayout(self)

        # self.filenameLabel = QLabel(self)
        
        # self.filenameLabel.setText(str(self.activeDataModel))
        # fbox.addRow(self.filenameLabel)
        # for k, param in activeModel.params.items():
        #     #self.paramLabels.append(QPushButton(param.paramName, self))
        #     self.paramLabels.append(QLabel(self))
        #     self.paramLabels[-1].setText(param.paramName)
        #     #self.paramLabels[-1].clicked[bool].connect(self.updateEntry)
        #     self.paramInputs.append(QLineEdit(self))
        #     self.paramInputs[-1].setText(str(param.value))
        #     self.paramInputs[-1].textChanged.connect(param.updateValue)
        #     self.paramInputs[-1].editingFinished.connect(self.updateFilename)
        #     fbox.addRow(self.paramLabels[-1])
        #     fbox.addRow(self.paramInputs[-1])

        self.buttonInputs = []

        for i, buttonrow in enumerate(self.buttons):
            
            self.buttonInputs.append(QPushButton(buttonrow, self))
            if i!=1:
                self.buttonInputs[-1].setCheckable(True)
            #self.buttonInputs[-1].clicked[bool].connect(self.runTest)
            fbox.addRow(self.buttonInputs[-1])
        
        
        win.setLayout(fbox)
    
    def setButtonCallbacks(self, runTest, getArduinoInfo, connectArduino):#, saveTest):
        self.buttonInputs[0].clicked[bool].connect(runTest)
        self.buttonInputs[1].clicked[bool].connect(getArduinoInfo)
        self.buttonInputs[2].clicked[bool].connect(connectArduino)
    
    #def update(self, params):

    def updateFilename(self):
        self.filenameLabel.setText(str(self.activeDataModel))

    
    
  