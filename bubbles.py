import time


def bubble_sort(data,drawdata,timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                drawdata(data,['yellow' if x == j or x == j+1 else "#a90042" for x in range(len(data))])
                time.sleep(timeTick)
    drawdata(data,['yellow' for x in range(len(data))])