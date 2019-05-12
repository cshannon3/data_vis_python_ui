
import Models.data_model as dm
import statistics as stats



#arduinoPort = '/COM4'

arduinoPort = '/COM9'

resultsTableFile = './resultstable.csv'


rawDataColumns = ['Input 1', 'Input 2', 'Input 3','Input 4', 'Input 5', 'Input 6', 'Input 7', 'Metric 1']


resultsTableHeaders = ["Param 1", "Param 2", "Param 3", "Param 4","Param 5", "Param 6", "Metric 1", "Metric 2", "Metric 3", "Metric 4"]
inputsDict = {
    "Input 1":dm.InputModel("Input 1", "ms", ""),
    "Input 2":dm.InputModel( "Input 2","mL", "Top Right",axisnum=1, xAxis="Time",isActive=False),
    "Input 3": dm.InputModel( "Input 3","mL", "Top Right", axisnum=1, xAxis="Time",isActive=True),
    "Input 4":dm.InputModel( "Input 4","mL", "",xAxis="Time", isActive=False),
    "Input 5":dm.InputModel( "Input 5","mL", "Top Left",xAxis="Time",axisnum=1, isActive=True),
    "Input 6":dm.InputModel( "Input 6","mm", "Bottom Right",xAxis="Time", axisnum=1,isActive=True),
    'Input 7':dm.InputModel( "Input 7","mm", "Bottom Right",xAxis="Time",axisnum=2, isActive=False),
}

paramsDict = {
    "Param 1": dm.ParamModel("Param 1",  100, "cm"),
    "Param 2": dm.ParamModel("Param 2",  2, "rr"),
    "Param 3": dm.ParamModel("Param 3",  20, "ro"),
    "Param 4": dm.ParamModel("Param 4",  5, "ru"),
    "Param 5": dm.ParamModel("Param 5",  400, "fd"),
    "Param 6": dm.ParamModel("Param 6",  24, "sp"),
}


def getMax(arr):
    return max(arr)
def getMin(arr):
    return min(arr)
def getMean(arr):
    return stats.mean(arr)
def getVal(val):
    return val
metricsDict = {
    "Metric 1":dm.MetricModel("Metric 1", getMean),
    "Metric 2":dm.MetricModel("Metric 2", getMax),
    "Metric 3":dm.MetricModel("Metric 3", getMin),
    "Metric 4":dm.MetricModel("Metric 4", getVal),
}
