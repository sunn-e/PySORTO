from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()

root.title('PySORTO- Sorting Visualiser')
root.maxsize = (900, 600)
# purplish color
root.config(bg='#9000F0')


# Base GUI/frame window
# User Console/window
UI_frame = Frame(root, width=600, height=200, bg='#FFB366')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Visualization window
canvas = Canvas(root, width=600, height=380, bg='#FFFFFF')
canvas.grid(row=1, column=0, padx=10, pady=5)

# Runtime window

# Visualization window
runtime_canvas = Canvas(root, width=200, height=100, bg='#FFFFFF')
runtime_canvas.grid(row=2, column=0, padx=5, pady=5)


# Variables

selected_alg = StringVar()


# test function


def drawData(data, refreshVal):
    start_time = time.time()
    # delete old canvas
    canvas.delete("all")
    runtime_canvas.delete("all")

    c_height = 400
    c_width = 600

    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 20

    # keep it less than c_height
    barscalefactor = 300

    # normalize the data array
    normalizedData = []

    for i in data:
        temp = i/max(data)
        print(i, temp)
        normalizedData.append(temp)

    # normalizedData = data
    refresh_seconds = 1
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * barscalefactor
        # bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="#9000F0")
        canvas.create_text((x0+2), y0, anchor=SW, text=str(data[i]))

        # animation
        root.update()
        time.sleep(refreshVal)
        # time.sleep(1)

    # runtime canvas/window
    print("Execution time: " + str(time.time() - start_time))
    # runtime_canvas.create_rectangle(20, 20, 20, 20, fill="#FFFF66")
    runtime_canvas.create_text(20, 20, anchor=SW,
                               text=("runtime( in seconds):" + str(time.time() -
                                                                   start_time)))


def Generate():
    print("Running" + selected_alg.get())
    # to generate user data
    # generate and save random array in data[]

    data = []

    # Minimum value in dataset
    try:
        minVal = int(minEntry.get())
    except:
        print("User did not provide minimum value. Setting it to 0.")
        minVal = 0
    finally:
        if minVal < 0:
            minVal = 0

    # Maximum value in dataset
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = random.randrange(1, 1337)
        print("User did not provide maximum value. Setting it to psudorandom value between 1 to 1337: " + str(maxVal))
    finally:
        if maxVal < 0:
            maxVal = random.randrange(1, 1337)

    # size of dataset
    try:
        sizeVal = int(sizeEntry.get())
    except:
        sizeVal = 42
    finally:
        if sizeVal < 1:
            sizeVal = random.randrange(1, 1337)

    # refrsh rate
    try:
        refreshVal = float(refreshEntry.get())
    except:
        refreshVal = 0.25
    finally:
        if refreshVal < 0:
            refreshVal = 0.25

    for temp in range(sizeVal):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, refreshVal)

# UI


# row 1
Label(UI_frame, text="Algorithm: ", bg='#FFFF66').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg,
                       values=['Bubble Sort', "Merge Sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Generate", command=Generate,
       bg='#9000F0').grid(row=0, column=2, padx=5, pady=5)

# row 2
Label(UI_frame, text="Size: ", bg='#FFFF66').grid(
    row=1, column=0, padx=5, pady=5, sticky=W)

sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W
               )

Label(UI_frame, text="Minimum Value ", bg='#FFFF66').grid(
    row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W
              )

Label(UI_frame, text="Maximum Value ", bg='#FFFF66').grid(
    row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W
              )

Label(UI_frame, text="Refresh rate in seconds ", bg='#FFFF66').grid(
    row=1, column=6, padx=5, pady=5, sticky=W)
refreshEntry = Entry(UI_frame)
refreshEntry.grid(row=1, column=7, padx=5, pady=5, sticky=W
                  )

# main loop
root.mainloop()
