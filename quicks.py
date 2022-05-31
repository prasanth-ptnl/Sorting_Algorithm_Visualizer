import time


def par(data,head,tail,drawData,timet):
    b = head
    p = data[tail]
    drawData(data,color(len(data),head,tail,b,b))
    time.sleep(timet)
    for j in range(head,tail):
        if data[j] < p:
            drawData(data,color(len(data),head,tail,b,j,True))
            time.sleep(timet)
            data[b],data[j] = data[j],data[b]
            b+=1
        drawData(data,color(len(data),head,tail,b,j))
        time.sleep(timet)
        
    drawData(data,color(len(data),head,tail,b,tail,True))
    time.sleep(timet)
    data[b],data[tail] = data[tail],data[b]
    return b
def quick_sort(data,head,tail,drawData,timet):
    if head<tail:

        parid = par(data,head,tail,drawData,timet)
        quick_sort(data,head,parid-1,drawData,timet)
        quick_sort(data,parid+1,tail,drawData,timet)

def color(lendata,head,tail,bord,curin,isSwaping=False):
    colora = []
    for i in range(lendata):
        if i>=head and i<=tail:
            colora.append("gray")
        else:
            colora.append("white")
        if i == tail:
            colora[i] = "orange"
        elif i == bord:
            colora[i] = 'red'
        elif i == curin:
            colora[i] = 'yellow'
        if isSwaping:
            if i== bord or i== curin:
                colora[i] = 'red'
    return colora