import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from queue import Queue

def calculateStartEndTime(processBurstTime, elapsedTime):
    '''
        Compute start and end of the process based on elapsed time
        args:
            processBurstTime: Time of execution for some process
            elapsedTime: Elapsed time of the execution
        return:
            start:
            end:
    '''
    start = elapsedTime
    end = start + processBurstTime
    return start, end

def addProcessToGanttChart(processExecution):
    processList.append(processExecution)

def plotGanttChart(processList):
    processIdList = [item[0] for item in processList]
    processStartList = [item[1] for item in processList]
    processEndList = [item[2] for item in processList]

    df = pd.DataFrame({'Process': processIdList,
                'start':processStartList,
                'end': processEndList,
                })
    
    df['process_duration'] = df['end'] - df['start']
    print(df)

    plt.barh(y=df['Process'], width=df['process_duration'], left=df['start'])
    plt.imsave("fcfs.png", df)  
    plt.show()  

def executeFCFS(readyQueue:Queue):
    '''
        Implementation of FCFS algorithm in order to execute process in ready qeue.
        args:
            readyQeue: A list process information. Each element is a tuple composed by: process's identification
                       and process burst time.
    '''
    elapsedTime = 0
    while not readyQueue.empty():
        # Get first element from Queue
        process = readyQueue.get()
        # Get information about process dequed
        processId = process[0]
        processBurstTime = process[1]
        # Compute star and end of the process
        start, end = calculateStartEndTime(processBurstTime, elapsedTime)
        processExecution = (processId, start, end)

        addProcessToGanttChart(processExecution)
        
        elapsedTime += processBurstTime
    
    plotGanttChart(processList)

if __name__ == '__main__':
    numberProcess = int(input('How many process do you want to simulate FCFS algorithm?\t'))
    
    readyQeue = Queue()
    processList = []

    for process in range(numberProcess):
        burstTime = np.random.randint(low=0, high=20)
        readyQeue.put((process+1, burstTime))

    executeFCFS(readyQeue)
