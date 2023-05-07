import matplotlib.pyplot as plt

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

def executeFCFS(readyQeue):
    '''
        Implementation of FCFS algorithm in order to execute process in ready qeue.
        args:
            readyQeue: A list process information. Each element is a tuple composed by: process's identification
                       and process burst time.
    '''
    elapsedTime = 0
    for process in readyQeue:
        processId = process[0]
        processBurstTime = process[1]
        start, end = calculateStartEndTime(processBurstTime, elapsedTime)
        processExecution = (processId, start, end)
        addProcessToGranttChart(processExecution)
        
        elapsedTime += processBurstTime

if __name__ == '__main__':
    numberProcess = int(input('How many process do you want to simulate FCFS algorithm?\t'))
    
    readyQeue = []

    for process in range(numberProcess):
        burstTime = int(input(f'What is the burst time of the process {process+1}?\t'))
        readyQeue.append((process+1, burstTime))

    executeFCFS(readyQeue)
