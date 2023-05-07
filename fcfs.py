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

def plotGanttChart():
    '''
        Plot Grantt Chart for 
    '''
    processIdList = [item[0] for item in processExecutionList]
    processStartList = [item[1] for item in processExecutionList]
    processEndList = [item[2] for item in processExecutionList]

    df = pd.DataFrame({'Process': processIdList,
                'start':processStartList,
                'end': processEndList,
                })
    
    df['process_duration'] = df['end'] - df['start']
    print(df)

    plt.barh(y=df['Process'], width=df['process_duration'], left=df['start'])
    plt.title('Grantt Chart for Process Execution')
    plt.xlabel('Process Duration')
    plt.ylabel('Process ID')
    plt.yticks(df['Process'])
    plt.imsave('fcfs.png', df)  
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
        # Get information about process dequeued
        processId = process[0]
        processBurstTime = process[1]
        # Compute star and end of the process
        start, end = calculateStartEndTime(processBurstTime, elapsedTime)
        processExecution = (processId, start, end)
        # Add process execution to list in order to plot later
        processExecutionList.append(processExecution)
        elapsedTime += processBurstTime
    
    plotGanttChart()

if __name__ == '__main__':
    numberProcess = int(input('How many process do you want to simulate FCFS algorithm?\t'))
    
    readyQeue = Queue()
    processExecutionList = []

    for process in range(numberProcess):
        burstTime = np.random.randint(low=1, high=20)
        readyQeue.put((process+1, burstTime))

    executeFCFS(readyQeue)
