 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QIcon
import PyQt5.QtCore as QtCore

import statistics as stats
import Shared.layout_info as layout
import Shared.data_info as data_info

import pandas as pd
import numpy as np
class ResultsTable(QTableWidget):
     #TODO Set link to table output
    def __init__(self, parent):
        super(ResultsTable,self).__init__(parent)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(len(data_info.resultsTableHeaders))
        self.tableWidget.setHorizontalHeaderLabels(data_info.resultsTableHeaders)
        self.tableWidget.resizeColumnsToContents()
       
        self.tableWidget.resize(layout.tableW, layout.tableH)
        self.current_row = 0
        self.tableWidget.setRowCount(3)
        self.currentResults = [0]*len(data_info.resultsTableHeaders)
        self.paramLen = 0
      

    def addParams(self, params):
        
        for key,param in params.items():
            if key in data_info.resultsTableHeaders:
                ind = data_info.resultsTableHeaders.index(key)
                itemwidget = QTableWidgetItem(str(param.value))
                itemwidget.setFlags(itemwidget.flags() |  QtCore.Qt.ItemIsEditable)
                self.tableWidget.setItem(self.current_row, ind, itemwidget)
    
    def updateTable(self, metrics):
        for key,metric in metrics.items():
            if key in data_info.resultsTableHeaders:
                ind = data_info.resultsTableHeaders.index(key)
                itemwidget = QTableWidgetItem(str(metric.value))
                self.tableWidget.setItem(self.current_row,ind, itemwidget)
    
    def addRun(self, filename):
        self.current_row += 1
        self.tableWidget.setRowCount(self.current_row+1)

  
    # def populateTable(self):
    #     df = pd.read_csv(data_info.resultsTableFile)
    #     self.tableWidget.setRowCount(len(df)+1)
        #for i, run in enumerate(df.index):
            #self.currentResults[ind]=param.paramVal
            
