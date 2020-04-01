import datetime

def getTime():
    currentDT = datetime.datetime.now()
    return("{}:{}:{} {}:{}:{}".format(currentDT.hour,currentDT.minute,currentDT.second, currentDT.day, currentDT.month, currentDT.year))


if(__name__=="__main__"):
    print(getTime())
