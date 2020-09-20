import random
import tkinter as tk
import ctypes
from winsound import*
ssx = 1550
ssy = 870
sunk=0
maps = ["A1","A2","A3","A7","A8","A9","A10","B5","B6","C1","C2","C3","C10","D5","D6","D7","D8","D10","E1","E2","E3","E4","E10","F5","F6","F8","F10","G1","G3","G10","H1","H4","I7","J2","J8","J9"]
alll = ["A1", "A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
cords = {"A":85, "B":174, "C":266,"D":358, "E":449, "F":540, "G":630, "H":721, "I":812, "J":903, "1":100, "2":188, "3":277, "4":365, "5":453, "6":542, "7":630, "8":718, "9":808, "10":895}
shots = ["A1", "A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    
def getname(self, box):
    name=box.get()
    self.destroy()
    tkgame(name)
    
def close(self, func):
    global sunk, maps, alll, cords, shots
    self.destroy()
    func()
    
def quitall():
    exit()

def restart(self, func):
    quitall()
    global sunk, maps, alll, cords, shots
    sunk=1
    maps = ["A1","A2","A3","A8","A9","A10","B5","B6","C1","C2","C3","C10","D5","D6","D7","D8","D10","E1","E2","E3","E4","E10","F5","F6","F8","F10","G1","G3","G10","H1","H4","I7","J2","J8","J9"]
    alll = ["A1", "A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    cords = {"A":102, "B":120, "C":282,"D":372, "E":460, "F":551, "G":640, "H":730, "I":821, "J":911, "1":120, "2":233, "3":300, "4":385, "5":477, "6":562, "7":656, "8":740, "9":825, "10":915}
    shots = [11]
    func()

def alreadychosen(cell):
    root1 = tk.Tk()
    root1.title("Error")
    text = tk.Label(root1, text="You have already chosen "+cell+"\n \n Please choose another cell.", font="bold", fg="#ff5c5c")
    text.pack()
    canvas = tk.Frame(root1, height=int(ssy/20), width=int(ssx/5))
    canvas.pack()
    button = tk.Button(root1, text="OK", command=root1.destroy, width=int(ssx/77), height=int(ssy/288), bg="#429ef5")
    button.pack()

    
def createbuttons(self, root1, counter):
    x=0
    for y in range (0,10):
        x=x+1
        placebutton("A", x, self, root1, counter)
        placebutton("B", x, self, root1, counter)
        placebutton("C", x, self, root1, counter)
        placebutton("D", x, self, root1, counter)
        placebutton("E", x, self, root1, counter)
        placebutton("F", x, self, root1, counter)
        placebutton("G", x, self, root1, counter)
        placebutton("H", x, self, root1, counter)
        placebutton("I", x, self, root1, counter)
        placebutton("J", x, self, root1, counter) 

def placebutton(letter, x, self, root1, counter):
    cell1=letter
    cell2=x
    if len(str(cords.setdefault(cell1)))==3:
        cordy = float("0."+str(cords.setdefault(cell1)))
    else:
        cordy = float("0.0"+str(cords.setdefault(cell1)))
    cordx = float("0."+str(cords.setdefault(str(cell2))))
    cell1.lower()
    cell2=str(cell2)
    cell=cell1+cell2
    cellbut=cell+"but"
    cellbut=tk.Button(self, text=cell, bg="#2a71b0", command=lambda:hitormiss(cell, root1, cellbut, counter), width=int(ssx/512), height=int(ssy/500), pady=2.4, bd=6.5)
    cellbut.place(relx=cordx, rely=cordy)




def instructions():
    root1 = tk.Tk()
    root1.title("Instructions")
    text = tk.Label(root1, text="Instructions: \n-Firstly draw a 10x10 grid (1-10 down on the left and A-J along the top) and place the folowing ships on it ensuring they do not touch each other (except corners) \n \n 1x Aircraft carrier - 5 long \n 2x Battleships - 4 long \n 3x Cruisers - 3 long \n 4x Destroyers - 2 long \n 5x Submarines - 1 long \n \n -You and the computer take turns to shoot at a cell \n -If you hit a ship it will be displayed on your view of the computers cell \n X is a hit, O is a miss. Repeating shots on a the same cell is a waste of a turn \n ")
    text.pack()
    button = tk.Button(root1, text="OK", command=root1.destroy, width=int(ssx/77), height=int(ssy/288), bg="#429ef5")
    button.pack()


def tkinterintro():
    root = tk.Tk()
    root.title("Start Screen")

    text = tk.Label(root, text="Welcome to: ")
    text.pack()

    title = tk.PhotoImage(file="media/intro.ppm", master=root)
    title=title.zoom((int(ssx/1536)),(int(ssy/864)))
    canvas = tk.Canvas(root, height=int(ssy/3.5), width=int(ssx/2.65), bg="blue")
    canvas.pack()
    canvas.create_image(0,250,anchor="sw", image=title)

    text = tk.Label(root, text="Name:")
    text.place(relx=0.46, rely=0.83)

    box = tk.Entry(root, width=(int(ssx/80)))
    box.place(relx=0.4, rely=0.9)

    button = tk.Button(root, text="Instructions", width=int(ssx/50), height=int(ssy/250), command = instructions, bg="#429ef5")
    button.pack(side="left")

    button = tk.Button(root, text="GO", width=int(ssx/50), height=int(ssy/250), bg="#3CE844", command =lambda:getname(root, box))
    button.pack(side="right")

    root.bind('<Return>', (lambda: getname(root, box)))
    root.mainloop()

def tkgame(name):
    if len(name)>20:
        name = name[0:20]
    root1 = tk.Tk()
    root1.title("Battleships")

    text = tk.Label(root1, text=name+" press a cell to shoot at it.")
    text.pack()

    counter = tk.Label(root1, text="Hits = "+str(sunk)+"/35", fg="red")
    counter.pack()

    grid = tk.PhotoImage(file="media/Grid.ppm", master=root1)
    grid = grid.zoom((int(ssx/307)), (int(ssy/172)))
    grid = grid.subsample(4)
    canvas = tk.Canvas(root1, height=(int(ssy/2.1)), width=(int(ssx/3.6)), bg="#429ef5")
    canvas.pack()
    #Might need to change below scaling
    canvas.create_image(215,205, image=grid)

    createbuttons(canvas, root1, counter)
    
    root1.mainloop()

def hitormiss(cell, root1, cellbut, counter):
    global sunk
    n=alll.index(cell)
    del alll[n]
    horm = tk.Tk()
    cell1=cell[0]
    cell1.upper()
    if cell[1] == "1":
        if len(cell)==2:
            cell2="1"
        elif len(cell)==3:
            cell2="10"
    else:
        cell2=cell[1]
    cordx = float("0."+str(cords.setdefault(cell2)))
    cordy = float("0."+str(cords.setdefault(cell1)))

    
    if cell in maps:
        verd = "HIT"
        backgrnd = tk.PhotoImage(file="media/hit.ppm", master=horm)
        backgrnd = backgrnd.subsample(2)
        cellbut.config(text="X", command=lambda:alreadychosen(cell), bg="green",)
        PlaySound('media/explosion.wav', SND_ASYNC)
        sunk=sunk+1
        counter.config(text="Hits = "+str(sunk))
        if sunk < 10:
            counter.config(text="Hits = "+str(sunk)+"/35")
        elif sunk < 20:
            counter.config(text="Hits = "+str(sunk)+"/35", fg="#ff8103")
        elif sunk > 35:
            counter.config(text="Hits = "+str(sunk)+"/35", fg="#3fa600")
            playerwins()
    else:
        verd = "MISS"
        backgrnd = tk.PhotoImage(file="media/miss.ppm", master=horm)
        backgrnd = backgrnd.subsample(2)
        cellbut.config(text="O", command=lambda:alreadychosen(cell), bg="red")
        PlaySound('media/water.wav', SND_ASYNC)


    horm.title(verd)
    canvas = tk.Canvas(horm, height=int(ssy/4), width=int(ssx/3), bg="blue")
    canvas.pack()
    canvas.create_image(200,100, image=backgrnd)


    label = tk.Label(canvas, text=verd, fg="red", font="bold", bg="#429ef5")
    label.place(relx=0.45, rely=0.1)

    button = tk.Button(horm, text="OK", command=lambda:close(horm, computersgo), width=int(ssx/77), height=int(ssy/288), bg="#429ef5")
    button.pack(side="bottom")

    horm.mainloop()

def computersgo():
    choice=random.choice(shots)
    shots.remove(choice)
    computer = tk.Tk()
    PlaySound('media/fire.wav', SND_ASYNC)
    computer.title("Computer's Turn")

    label = tk.Label(computer, text="The computer fired at: ")
    label.pack(side="top")

    title = tk.PhotoImage(file="media/shots.ppm", master=computer)
    title = title.subsample(2)
    canvas = tk.Canvas(computer, height=int(ssy/4), width=int(ssx/3), bg="blue")
    canvas.pack()
    canvas.create_image(200,100, image=title)


    label = tk.Label(canvas, text=choice, fg="red", font="bold", bg="#429ef5")
    label.place(relx=0.45, rely=0.1)

    button = tk.Button(computer, text="OK", command=computer.destroy, width=int(ssx/77), height=int(ssy/288), bg="#429ef5")
    button.pack(side="bottom")

    button = tk.Button(computer, text="My fleet \n has sunk!", command=lambda: computerwins(), width=int(ssx/150), height=int(ssy/288), bg="red")
    button.place(relx=0, rely=0.81)

    computer.mainloop()

def computerwins():
    computer1 = tk.Tk()
    computer1.title("Take The L")

    title = tk.PhotoImage(file="media/sunk.ppm", master=computer1)
    title = title.subsample(6)
    canvas = tk.Canvas(computer1, height=int(ssy/4), width=int(ssx/3), bg="blue")
    canvas.pack()
    canvas.create_image(200,100, image=title)

    label = tk.Label(canvas, text="YOU LOSE", fg="red", font="bold", bg="#429ef5")
    label.place(relx=0.4, rely=0.1)

    button = tk.Button(computer1, text="PLAY AGAIN", command=lambda:restart(computer, tkinterintro), width=int(ssx/42), height=int(ssy/150), bg="green")
    button.pack(side="right")

    button = tk.Button(computer1, text="QUIT", command=lambda: quitall(), width=int(ssx/42), height=int(ssy/150), bg="red")
    button.pack(side="left")

    computer1.mainloop()

def playerwins():
    computer2 = tk.Tk()
    computer2.title("Victory Royale")

    title = tk.PhotoImage(file="media/sunk.ppm", master=computer2)
    title = title.subsample(6)
    canvas = tk.Canvas(computer2, height=int(ssy/4), width=int(ssx/3), bg="blue")
    canvas.pack()
    canvas.create_image(200,100, image=title)

    label = tk.Label(canvas, text="YOU WIN!!!!", fg="blue", font="bold", bg="white")
    label.place(relx=0.4, rely=0.1)

    button = tk.Button(computer2, text="PLAY AGAIN", command=lambda:restart(computer, tkinterintro), width=int(ssx/42), height=int(ssy/150), bg="green")
    button.pack(side="right")

    button = tk.Button(computer2, text="QUIT", command=lambda:quitall(), width=int(ssx/42), height=int(ssy/150), bg="red")
    button.pack(side="left")

    computer2.mainloop()

tkinterintro()
