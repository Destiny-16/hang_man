from tkinter import *
from tkinter import messagebox
from random import randrange
from random import randint

mistake = 0


def makebody():
    global mistake
    mistake+=1
    if mistake ==1:
        dibujo.create_oval(100,150,160,210) #head
    if mistake ==2:
        dibujo.create_line(130,210,130,280,width=3) #column
    if mistake ==3 :
        dibujo.create_line(130,210,150,230,width =3) # hand  l
    if mistake ==4:
        dibujo.create_line(130,210,110,230,width=3) #hand r
    if mistake ==5:
        dibujo.create_line(130,280,150,300,width = 3) #leg l
    if mistake ==6:
        dibujo.create_line(130,280,110,300,width =3) # leg r
        messagebox.showinfo("Perdiste", "You Lose")
        root.destroy()
    print(mistake)


###########################################################words############
f = open("words.txt", "r")


answer = [""] 
answer = f.readlines()[randrange(126)]
print(answer)
word = [""] * (len(answer)-1)


def buttonClick(letter) :
    count = 0
    found = False
    for char in answer:
        if(answer[count] == letter):
            word[count] = letter
            found = True
            print(word)

        
        count = count + 1

    if(found == False):
        makebody()
    else:
        hasWon(word, answer)

    wordLabel.configure(text=word)




#################################making window#############################################
root = Tk()


root.geometry("500x500")

root.title("Hang Man Game")

root.resizable(0,0)

#####################################################################

def hasWon (word, answer):
    
    string = ""
    string = string.join(word)
    answer = answer.strip()


    if(string == answer):
        messagebox.showinfo("Perdiste", "You Win")
        root.destroy()
 

    
    


    
  
            
wordLabel = Label(root, font=("Ariel", 30), fg="black")
aButton = Button(root, text="A", command=lambda : buttonClick('a'))
bButton = Button(root, text="B", command=lambda : buttonClick('b'))
cButton = Button(root, text="C", command=lambda : buttonClick('c'))
dButton = Button(root, text="D", command=lambda : buttonClick('d'))
eButton = Button(root, text="E", command=lambda : buttonClick('e'))
fButton = Button(root, text="F", command=lambda : buttonClick('f'))
gButton = Button(root, text="G", command=lambda : buttonClick('g'))
hButton = Button(root, text="H", command=lambda : buttonClick('h'))
iButton = Button(root, text="I", command=lambda : buttonClick('i'))
jButton = Button(root, text="J", command=lambda : buttonClick('j'))
kButton = Button(root, text="K", command=lambda : buttonClick('k'))
lButton = Button(root, text="L", command=lambda : buttonClick('l'))
mButton = Button(root, text="M", command=lambda : buttonClick('m'))
nButton = Button(root, text="N", command=lambda : buttonClick('n'))
oButton = Button(root, text="O", command=lambda : buttonClick('o'))
pButton = Button(root, text="P", command=lambda : buttonClick('p'))
qButton = Button(root, text="Q", command=lambda : buttonClick('q'))
rButton = Button(root, text="R", command=lambda : buttonClick('r'))
sButton = Button(root, text="S", command=lambda : buttonClick('s'))
tButton = Button(root, text="T", command=lambda : buttonClick('t'))
uButton = Button(root, text="U", command=lambda : buttonClick('u'))
vButton = Button(root, text="V", command=lambda : buttonClick('v'))
wButton = Button(root, text="W", command=lambda : buttonClick('w'))
xButton = Button(root, text="X", command=lambda : buttonClick('x'))
yButton = Button(root, text="Y", command=lambda : buttonClick('y'))
zButton = Button(root, text="Z", command=lambda : buttonClick('z'))


wordLabel.place(x=20, y=20)
aButton.place(x=0, y=100)
bButton.place(x=20, y=100)
cButton.place(x=40, y=100)
dButton.place(x=60, y=100)
eButton.place(x=80, y=100)
fButton.place(x=100, y=100)
gButton.place(x=120, y=100)
hButton.place(x=0, y=125)
iButton.place(x=20, y=125)
jButton.place(x=40, y=125)
kButton.place(x=60, y=125)
lButton.place(x=80, y=125)
mButton.place(x=100, y=125)
nButton.place(x=120, y=125)
oButton.place(x=0, y=150)
pButton.place(x=20, y=150)
qButton.place(x=40, y=150)
rButton.place(x=60, y=150)
sButton.place(x=80, y=150)
tButton.place(x=100, y=150)
uButton.place(x=120, y=150)
vButton.place(x=0, y=175)
wButton.place(x=20, y=175)
xButton.place(x=40, y=175)
yButton.place(x=60, y=175)
zButton.place(x=80, y=175)


#############################################################################
frameahorcado=Frame(root,width=250,height=600)
frameahorcado.place(x=250,y=0)
dibujo=Canvas(frameahorcado,width=250,height=600)
dibujo.place(x=0,y=0)
dibujo.create_line(10,400,200,400,width=3)
dibujo.create_line(20,400,20,100,width=3)
dibujo.create_line(20,100,130,100,width=3)
dibujo.create_line(130,100,130,150,width=3)                      

#############################################

root.mainloop()


