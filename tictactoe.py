from tkinter import *
import tkinter.messagebox

m = tkinter.Tk()
m.title("Tic Tac Toe")

player1 = ""
player2 = ""

Label(m, text=" Player 1 ").grid(row=0)
Label(m, text=" Player 2 ").grid(row=1)

p1 = Entry(m)
p2 = Entry(m)

p1.grid(row=0, column=1)
p2.grid(row=1, column=1)

player1 = p1.get()
player2 = p2.get()

def on_submit():
    player1 = p1.get()
    player2 = p2.get()

    print("Log: " + player1 +" vs "+player2)


Button(m, text="SUBMIT", command=on_submit).grid(row=2,column=1)

clickbutton = True

buttons = StringVar()

def ttt(buttons): 
    global clickbutton
    if buttons["text"] == " " and clickbutton == True:
        buttons["text"] = "X"
        clickbutton = False
    elif buttons["text"] == " " and clickbutton == False:
        buttons["text"] = "O"
        clickbutton = True

    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
    button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
    button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
    button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
    button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
    button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
    button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
    button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        msg = "PLAYER " +p1.get()+ " has won!!"
        tkinter.messagebox.showinfo(message= msg)
        exit()
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
    button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
    button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
    button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
    button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
    button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
    button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
    button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        msg = "PLAYER "+ p2.get() + " has won!!"
        tkinter.messagebox.showinfo(message= msg)
        exit()

button1 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button1))
button1.grid(row=4, column=0, sticky=N+S+W+E)
button2 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button2))
button2.grid(row=4, column=1, sticky=N+S+W+E)
button3 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button3))
button3.grid(row=4, column=2, sticky=N+S+W+E)
button4 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button4))
button4.grid(row=5, column=0, sticky=N+S+W+E)
button5 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button5))
button5.grid(row=5, column=1, sticky=N+S+W+E)
button6 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button6))
button6.grid(row=5, column=2, sticky=N+S+W+E)
button7 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button7))
button7.grid(row=6, column=0, sticky=N+S+W+E)
button8 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button8))
button8.grid(row=6, column=1, sticky=N+S+W+E)
button9 = Button(m, text=" ", font="Times 20 bold", bg="black", fg="red",height=3,width=6, command= lambda:ttt(button9))
button9.grid(row=6, column=2, sticky=N+S+W+E)

m.mainloop()

