import time


def merge_sort(data,drawData,timeTick):
    merge_sort_algo(data,0,len(data)-1,drawData,timeTick)

def merge_sort_algo(data,left,right,drawData,timeTick):
    if left < right:
        mid = (left+right)//2
        merge_sort_algo(data,left,mid,drawData,timeTick)
        merge_sort_algo(data,mid+1,right,drawData,timeTick)
        merge(data,left,mid,right,drawData,timeTick)

def merge(data,left,mid,right,drawData,timeTick):

    drawData(data,color(len(data),left,mid,right))
    time.sleep(timeTick)
    leftpart = data[left:mid+1]
    rightpart = data[mid+1:right+1]
    leftinde = rightinde = 0
    for i in range(left,right):
        if leftinde < len(leftpart) and rightinde < len(rightpart):
            if leftpart[leftinde]<=rightpart[rightinde]:
                data[i] = leftpart[leftinde]
                leftinde+=1
            else:
                data[i] = rightpart[rightinde]
                rightinde+=1
        elif leftinde < len(leftpart):
            data[i] = leftpart[leftinde]
            leftinde+=1
        else:
            data[i] = rightpart[rightinde]
            rightinde += 1

    drawData(data,["green" if x>=left and x<=right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def color(lenght,left,mid,right):
    colora = []
    for i in range(lenght):
        if i>= left and i<=right:
            if i>=left and i<=mid:
                colora.append("green")
            else:
                colora.append("orange")
        else:
            colora.append("white")
    return colora