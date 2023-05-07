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

def addProcessToGranttChart(processExecution):
    # Logic to generate Gantt Chart
    print('Generating Gantt Chart...')

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

        addProcessToGranttChart(processExecution)
        
        elapsedTime += processBurstTime

if __name__ == '__main__':
    numberProcess = int(input('How many process do you want to simulate FCFS algorithm?\t'))
    
    readyQueue = Queue()
    
    for process in range(numberProcess):
        burstTime = np.random.randint(low=0, high=20)
        readyQueue.put((process+1, burstTime))

    executeFCFS(readyQueue)
