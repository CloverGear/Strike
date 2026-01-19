import random
import tkinter as tk
from pygame import mixer

window = tk.Tk()

window.geometry("1280x720")
window.title("30 Seconds Strike!")

def button_right():
    btnS = tk.Button(frameInFrame, text = "Strike!", font = ('Comic Sans', 18), command = lambda: button_strike())
    btnS.grid(row = 4, column = 0, columnspan = 5, ipadx = 50, ipady = 100)
    
def button_strike():
    if nGuessCounter == 4:
        nStrike = random.randrange(24, 30)
    elif nGuessCounter == 3:
        nStrike = random.randrange(14, 25)
    elif nGuessCounter == 2:
        nStrike = random.randrange(5, 17)
    elif nGuessCounter < 1:
        nStrike = random.randrange(1, 10)
        
    mixer.init()
    sound = mixer.Sound("StrikeSound.mp3")
    sound.play()
    
    for i in range(1, nStrike + 1):
        canvas.create_arc(-245, 5, 255, 500, start = 90 - 6 * i, extent = -6, fill = "white")
    if nStrike == 29:
        labelG = tk.Label(window, text = "Perfect!", font = ('Times New Roman', 24))
        soundP = mixer.Sound("PerfectSound.mp3")
        soundP.play()
    elif nStrike <= 28 and nStrike > 20:
        labelG = tk.Label(window, text = "Great!", font = ('Times New Roman', 24))
    elif nStrike <= 20 and nStrike > 10:
        labelG = tk.Label(window, text = "Nice!", font = ('Times New Roman', 24))
    else:
        labelG = tk.Label(window, text = "You can do better!", font = ('Times New Roman', 24))
    labelG.pack()

def button_wrong():
    global nGuessCounter
    if nGuessCounter == 4:
        strText2 = "The second hint for the word is: " + dictWordHint2[strWord]
        label2 = tk.Label(frameInFrame, text = strText2, font = ('Times New Roman', 14))
        label2.grid(row = 2, column = 0, columnspan = 5)
    elif nGuessCounter == 3:
        strText3 = "The third hint for the word is: " + dictWordHint3[strWord]
        label3 = tk.Label(frameInFrame, text = strText3, font = ('Times New Roman', 14))
        label3.grid(row = 3, column = 0, columnspan = 5)
    elif nGuessCounter == 2:
        nGuessCounter = 1
        strText4 = "The word is: " + strWord
        label4 = tk.Label(frameInFrame, text = strText4, font = ('Times New Roman', 14))
        label4.grid(row = 4, column = 0, columnspan = 5)
    nGuessCounter -= 1

def start():
    for widget in frameInFrame .winfo_children():
        widget.destroy()
        
    canvas.delete("all")
    
    canvas.create_arc(-245, 5, 255, 500, start = 90, extent = -6, fill = "white")
    
    global nGuessCounter
    global strWord
    nLen = len(listWord)
    nWord = random.randrange(0, nLen)
    strWord = listWord[nWord]
    nGuessCounter = 4
    
    strText1 = "The first hint for the word is: " + dictWordHint1[strWord]
    label1 = tk.Label(frameInFrame, text = strText1, font = ('Times New Roman', 14))
    label1.grid(row = 1, column = 0, columnspan = 5)
    
    nNum = random.randrange(0, 3)
    if nWord == 0:
        nNum1 = random.randrange(nWord + 1, nLen - 1)
        strWrongWord1 = listWord[nNum1]
        nNum2 = nNum1 + 1
        strWrongWord2 = listWord[nNum2]
    elif nWord == nLen - 1:
        nNum1 = random.randrange(1, nWord)
        strWrongWord1 = listWord[nNum1]
        nNum2 = nNum1 - 1
        strWrongWord2 = listWord[nNum2]
    else:
        nNum1 = random.randrange(0, nWord)
        strWrongWord1 = listWord[nNum1]
        nNum2 = random.randrange(nWord + 1, nLen)
        strWrongWord2 = listWord[nNum2]
    if nNum == 0:
        btn1 = tk.Button(frameInFrame, text = strWord, font = ('Comic Sans', 18), command = lambda: button_right())
        btn1.grid(row = 0, column = 0)
        btn2 = tk.Button(frameInFrame, text = strWrongWord1, font = ('Comic Sans', 18), command = lambda: button_wrong())
        btn2.grid(row = 0, column = 1)
        btn3 = tk.Button(frameInFrame, text = strWrongWord2, font = ('Comic Sans', 18), command = lambda: button_wrong())
        btn3.grid(row = 0, column = 2)
    elif nNum == 1:
        btn1 = tk.Button(frameInFrame, text = strWord, font = ('Comic Sans', 18), command = lambda: button_right())
        btn1.grid(row = 0, column = 1)
        btn2 = tk.Button(frameInFrame, text = strWrongWord1, font = ('Comic Sans', 18), command = lambda: button_wrong())
        btn2.grid(row = 0, column = 0)
        btn3 = tk.Button(frameInFrame, text = strWrongWord2, font = ('Comic Sans', 18), command = lambda: button_wrong())
        btn3.grid(row = 0, column = 2)
    else:
        btn1 = tk.Button(frameInFrame, text = strWord, font = ('Comic Sans', 18), command = lambda: button_right())
        btn1.grid(row = 0, column = 2)
        btn2 = tk.Button(frameInFrame, text = strWrongWord1, font = ('Comic Sans', 18), command = lambda: button_wrong())
        btn2.grid(row = 0, column = 1)
        btn3 = tk.Button(frameInFrame, text = strWrongWord2, font = ('Comic Sans', 18), command = lambda: button_wrong())
        btn3.grid(row = 0, column = 0)
        
listWord = ["apple", "new york", "cotton candy", "cat", "scarf"]

dictWordHint1 = {"apple" : "red", "new york" : "Famous Place", "cotton candy" : "Soft, fluffy food", "cat" : "animal", "scarf" : "Warm"}

dictWordHint2 = {"apple" : "fruit", "new york" : "Statue of Liberty", "cotton candy" : "Really Sweet", "cat": "pet", "scarf" : "Made from wool"}

dictWordHint3 = {"apple" : "round and crunchy", "new york" : "Biggest City in America", "cotton candy" : "Cloud-like", "cat" : "Three letter word", "scarf" : "Long"}

bGuessed = False

labelWelcome = tk.Label(window, text = "Welcome to the 30 Seconds Strike! game, inspired by the board game 30 seconds.\n You will see three words and a hint, and after you chose the right word, you get a chance to strike. Get it right on the first try to get a good score!", font = ('Times New Roman', 14))
labelWelcome.pack(padx = 10, pady = 20)

btn = tk.Button(window, text = "Start!", font = ('Comic Sans', 18), command = lambda: start())
btn.pack()

frame = tk.Frame(window)

frameInFrame = tk.Frame(frame)
frameInFrame.grid(row = 0, column = 0, columnspan = 2)

canvas = tk.Canvas(frame, width = 270, height = 500, bg = "black")
canvas.grid(row = 0, column = 2)

frame.pack()

window.mainloop()