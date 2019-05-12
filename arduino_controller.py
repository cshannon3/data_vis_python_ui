
import serial
import numpy as np
import pandas as pd
import Shared.data_info as data_info
import time
import serial.tools.list_ports


class ArduinoController:
   
    def __init__(self,activeModel, arduinoPort=""):
        self.activeDataModel = activeModel
        self.arduinoPort= arduinoPort
        self.arduinoConnect=None


    def connectArduino(self, pressed):
        if pressed:
            if self.arduinoPort=="":
                ports = list(serial.tools.list_ports.comports())
                i=0
                while i<len(ports) and not self.arduinoConnect:
                    try:
                        self.arduinoPort = ports[0].device
                        self.arduinoConnect=serial.Serial(self.arduinoPort,115200, timeout=5)
                    except:
                        i+=1
        else:
            self.arduinoConnect=None


    def getArduinoInfo(self, pressed):
        if self.arduinoConnect !=None:
            
            self.arduinoConnect.write(str.encode("A"))
            time.sleep(3)
            msg = self.arduinoConnect.read(self.arduinoConnect.inWaiting())
            data_lines = msg.decode("utf-8").splitlines()
            i = data_lines.index("INPUTS")+1
            while ("PARAMS" not in data_lines[i]):
                self.activeDataModel.addInput(data_lines[i].split(","))
                print(data_lines[i])
                i+=1
                
            i+=1
            while i<len(data_lines):
                self.activeDataModel.addParam(data_lines[i].split(","))
                i+=1
            
    
    def initNewRun(self):
        self.arduinoConnect.write(str.encode("B"))
        time.sleep(1)
        for k, v in self.activeDataModel.inputs.items():
            v.data=[]
    
    def addDataToRun(self):
        
        if self.arduinoConnect is None:
            print("Not Connected")
            return
        try:
            msg = self.arduinoConnect.read(self.arduinoConnect.inWaiting())
            data_lines = msg.decode("utf-8").splitlines()
        except:
            print("Issue w/ arduino")
            return    
      
        for datapt in data_lines:
            if ":" in datapt and  datapt.split(":")[0] in self.activeDataModel.inputs:
                self.activeDataModel.inputs[datapt.split(":")[0]].addData(datapt.split(":")[1])

      