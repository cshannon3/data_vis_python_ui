
#!/usr/bin/python
import sys
import serial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import PyQt5.QtCore as QtCore

#####
#TODO  
# Add Saving functionality
# Add ability to show old data using table

import Components.plot_canvas as plot_canvas
import Components.results_table as results_table
import Components.options_menu as options_menu

import arduino_controller

import Shared.layout_info as layout
import Shared.data_info as data_info
import Models.data_model as data_model




class App(QMainWindow):
 

    def __init__(self):
        super().__init__()

        self.activeDataModel = data_model.DataModel()
        self.arduinoController = arduino_controller.ArduinoController(self.activeDataModel)#, data_info.arduinoPort)

        self.plotWidget = plot_canvas.PlotCanvas(self)
        self.resTableWidget = results_table.ResultsTable(self)
        self.optionsWidget = options_menu.OptionsMenu(self, activeModel=self.activeDataModel)
        self.optionsWidget.setButtonCallbacks(self.runTest, self.getArduinoInfo, self.arduinoController.connectArduino)#, self.saveTest)
        
        self.runTimer = QtCore.QTimer(self)
        self.initUI()
        
     
       
    def initUI(self):
       
        self.setGeometry(layout.windowStartX, layout.windowStartY, layout.windowW, layout.windowH)
        
        self.resTableWidget.move(layout.tableStartX,layout.tableStartY)
        self.resTableWidget.resize(layout.tableW,layout.tableH)
        self.optionsWidget.resize(layout.optionsW, layout.optionsH)
        self.plotWidget.move(layout.plotStartX,layout.plotStartY)
         
        self.show()
 

    def runTest(self, pressed):
        
        if pressed:
            self.arduinoController.initNewRun()
            #self.resTableWidget.addParams(self.activeDataModel.params)
            #self.plotWidget.setPlot(self.activeDataModel.inputs)

            self.runTimer.timeout.connect(lambda: self.updateArduino())
            self.runTimer.setSingleShot(False)
            self.runTimer.start(500)
        else:
            print("Stop")
            self.runTimer.setSingleShot(True)

    def updateArduino(self):
        
        self.arduinoController.addDataToRun()
        self.plotWidget.updatePlot(self.activeDataModel.inputs)
        self.show()  
   
    def getArduinoInfo(self, pressed):
        self.arduinoController.getArduinoInfo(pressed)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
 
 