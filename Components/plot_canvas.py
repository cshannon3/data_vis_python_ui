from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QIcon
import PyQt5.QtCore as QtCore

import Shared.layout_info as layout
import Shared.data_info as d
#TODO extract out specific info from plot

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, dpi=100):
        fig = Figure(figsize=(layout.plotW, layout.plotH), dpi=dpi)
        fig.subplots_adjust(top=0.95,hspace=0.4, wspace=0.2, right=0.90, left=0.075)
        self.axestl = fig.add_subplot(221)
        self.axestr = fig.add_subplot(222)
        self.axestr2 = self.axestr.twinx()
        self.axesbr = fig.add_subplot(2,2,4)
        self.axesbr2 = self.axesbr.twinx()
        self.axesDict = {
            "Top Left": self.axestl,
            "Top Right": self.axestr,
            "Bottom Right": self.axesbr,
        }

        # self.axesDict = {
        #     "Top Left": PlotModel(fig.add_subplot(221)),
        #     "Top Right": PlotModel(fig.add_subplot(222)),
        #     "Bottom Right": PlotModel(fig.add_subplot(2,2,4)),
        # }
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.updatePlot(d.inputsDict)


    def updatePlot(self, inputs):
        for k,p in self.axesDict.items():
            p.cla()
        for k, inpt in inputs.items():
            if inpt.isActive:
                #self.axesDict[inpt.plotLocation].cla()
                #print(inpt.data)
                self.axesDict[inpt.plotLocation].plot(inpt.data)
        self.draw()

    # def setPlot(self, inputsDict):
        
    #     for k, inputVar in inputsDict.items():
    #         if inputVar.isActive and inputVar.plotLocation in self.axesDict:
    #             activeplot = self.axesDict[inputVar.plotLocation]
    #             if not activeplot.xInput:
    #                 activeplot.xInput= inputsDict[inputVar.xAxis]
    #             if inputVar.axisnum == 1:
    #                 activeplot.inputs_axis1.append(inputVar)
    #             else:
    #                 activeplot.inputs_axis2.append(inputVar)
    #     for k,v in self.axesDict.items():
    #         v.initialize()
    #     self.draw()
    

    # def updatePlot(self):#, inputsDict):
    #     for k, v in self.axesDict.items():
    #         v.updatePlotModel()
    #     self.draw()
        # for k, inputVar in inputsDict.items():
        #     if inputVar.isActive and inputVar.plotLocation in self.axesDict:
        #         activeplot = self.axesDict[inputVar.plotLocation]
        #         if activeplot.inputs_axis1==inputVar:
        #         activeplot.cla()
        #         activeplot.plot(inputsDict[inputVar.xAxis].data, inputVar.data)
        #         activeplot.set_title(k + " vs "+ inputVar.xAxis)
        #         activeplot.set_ylabel(k)
        #         activeplot.set_xlabel(inputVar.xAxis)


        


# class PlotModel:
#     def  __init__(self, subplot ,xInput=None, inputs_axis1=[], inputs_axis2=[]):
#         self.subplot = subplot
#         self.xInput =xInput
#         self.inputs_axis1 =inputs_axis1
#         self.inputs_axis2= inputs_axis2
        
    
    
#     def initialize(self):
#         self.subplot.cla()
#         #self.inputp1, = self.subplot.plot([n for n in range(100)],[n for n in range(100)])
#         #self.inputp2, = self.subplot.twinx().plot([],[])
#         #self.subplot.twinx().cla()
#         self.subplot.set_autoscalex_on(True)
#         self.subplot.set_xlabel(self.xInput.inputName)



#     def updatePlotModel(self):
#         #
        
#         if self.inputs_axis1 and self.xInput.data:
#             self.subplot.cla()
#             #self.inputp1.set_data([n for n in range(100)],[-n for n in range(100)])
#             #self.inputp1.set_data(self.xInput.data,self.inputs_axis1[0].data)
#             self.subplot.plot(self.xInput.data, self.inputs_axis1[0].data)
#             self.subplot.set_xlabel(self.xInput.inputName)





            #self.inputp1.set_xdata(self.xInput.data)
            #self.inputp1.set_ydata(self.xInput.data)
            #self.subplot.relim()        # Recalculate limits
           # self.subplot.autoscale_view(True,True,True) #Autoscale
           # self.subplot.draw()
            #self.inputp1.set_xdata([inp.data for inp in self.inputs_axis1])
            #for inputVar in self.inputs_axis1:
                #self.subplot.plot(self.xInput.data, inputVar.data)
        #if self.inputs_axis2:
            #self.inputp2.set_ydata(self.xInput.data)
            #self.inputp2.set_xdata([inp.data for inp in self.inputs_axis2])
            # twin = self.subplot.twinx()
            # twin.cla()
            # for inputVar in self.inputs_axis1:
            #     twin.plot(self.xInput.data, inputVar.data)
        

    
    
    # def updatePlot2(self, df):
    
    #     self.axestl.cla()
    #     self.axestr.cla()
    #     self.axestr2.cla()
    #     self.axesbr.cla()
    #     self.axesbr2.cla()

    #     self.axestl.plot(df['Pressure'])
    #     self.axestr.plot(df['Flow1'])
    #     self.axestr.plot(df['Flow2'])

    #     self.axesbr.plot(df['Distance'])
    #     self.axesbr2.plot(df['PID'],color=(1,0,0,1))

    #     self.axestl.set_title('Pressure vs Time')
    #     self.axestl.set_ylabel('Pressure')
    #     self.axestl.set_xlabel("Time(Sec)")

    #     self.axestr.set_title('Flow/Volume vs Time')
    #     self.axestr.set_ylabel('Flow(LPM)')
    #     self.axestr.set_xlabel("Time(Sec)")
       
    #     self.draw()

   