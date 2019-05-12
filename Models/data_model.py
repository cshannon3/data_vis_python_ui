
import numpy as np
import pandas as pd
import time
import datetime
import serial

class DataModel:
    
    def __init__(self,params = {}, metrics={}, inputs = {}):#, dfHeaderColumns=[], arduinoPort=""):
        self.params = params
        self.metrics = metrics
        self.inputs = inputs
        now = datetime.datetime.now()
        self.startdate = '_d'+ now.strftime("%Y-%m-%d-%H%M%S")
       
    
    def __str__(self):
        paraminfo = ""
        for k, param in self.params.items():
            paraminfo+=str(param)
        return "{}{}.csv".format(paraminfo, self.startdate)
    
    def addParam(self, param_info):
        self.params[param_info[0]] = ParamModel(param_info[0], value=param_info[2], paramId=param_info[1])
    def addInput(self, input_info):
        self.inputs[input_info[0]] = InputModel(input_info[0], input_info[1], input_info[2], isActive= True if "active" in input_info else False)
    



class ParamModel:
    #Param model has param value,
    #param name
    #param type
    # param nickname for filename
    def __init__(self, paramName="", value=0, paramId="" ): #, inputType=
        self.paramName = paramName
        self.value = value
        self.paramId = paramId

    def __str__(self):
        return "_{}{}".format(self.paramId, self.value)
    

    def updateValue(self, newVal):
        try:
            self.value= newVal
        except:
            pass


class MetricModel:
    def __init__(self, metricName, resultFunc, inputType):

        self.resultFunc= resultFunc
        self.metricName = metricName
        self.inputType = inputType
        self.value = 0
    
    
    def setVal(self, functionInput):
        self.value = self.resultFunc(functionInput)
    
  
class InputModel:
    def __init__(self, inputName, unit, plotLocation, axisnum=1, xAxis="", isActive=False):
        self.inputName = inputName
        self.xAxis=xAxis
        self.axisnum=axisnum
        self.unit = unit
        self.plotLocation = plotLocation
        self.isActive = isActive
        self.data=[]

    def addData(self, rawData=[]):
        for d in rawData:
            try:
                self.data.append(float(d))
            except:
                pass
  