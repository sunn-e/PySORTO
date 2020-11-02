import time


def bubbleSort(data, drawData, refreshVal):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                # swap
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
                # draw
                drawData(data, ['#FFB366' if k == j or x == j +
                                1 else "#9000F0" for x in range(len(data))])
                time.sleep(refreshVal)
    drawData(data, ["#FFB366" for k in range(len(data))])
