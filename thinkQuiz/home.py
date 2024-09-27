from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
import random

def age1():
    new_root.destroy()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)

    mixer.init()


    a=list(range(0,14))
    random.shuffle(a)
    a.append(14)
    c=0
    def select(event):
        callimage.place_forget()

        pa.place_forget()
        pb.place_forget()
        pc.place_forget()
        pd.place_forget()

        pla.place_forget()
        plb.place_forget()
        plc.place_forget()
        pld.place_forget()

        b = event.widget
        value = b["text"]
        c=0

        for i in range(len(a)):
            if value == correct[a[i]]:
                if value == correct[14]:
                    def close1():
                        root.destroy()

                    def playa():
                        option1.bind("<Button-1>",select)
                        option2.bind("<Button-1>",select)
                        option3.bind("<Button-1>",select)
                        option4.bind("<Button-1>",select)
                        life12.config(state=NORMAL, image=image50)
                        life2.config(state=NORMAL, image=imageaud)
                        life3.config(state=NORMAL,  image=imagephone)

                        question.delete(1.0, END)
                        question.insert(END, questions[a[0]])
                        option1.config(text=first_option[a[0]])
                        option2.config(text=second_option[a[0]])
                        option3.config(text=third_option[a[0]])
                        option4.config(text=fourth_option[a[0]])

                        amountlogo.config(image=amount)
                        root2.destroy()

                    root2 = Toplevel()
                    root2.overrideredirect(True)
                    root2.config(bg="black")
                    root2.geometry("500x500+140+30")
                    root2.title("you won 0 pound")
                    imgLabel = Label(root2, image=logo, bd=0)
                    imgLabel.pack()
                    winLabel = Label(root2, text="you Won", font=('arail', 28, "bold"), bg="black", fg="white")
                    winLabel.pack()

                    playagain = Button(root2, text="Play Again", font=("arial", 16, "bold"), bg="black", fg="white",
                                    activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                    command=playa)
                    playagain.pack()

                    close = Button(root2, text="close", font=("arial", 16, "bold"), bg="black", fg="white",
                                activebackground="black", activeforeground="white", bd=0, cursor="hand2", command=close1)
                    close.pack()
                    happy = PhotoImage(file="happy.png")
                    happyLabel = Label(root2, image=happy, bg="black")
                    happyLabel.place(x=30, y=280)

                    happyLabel1 = Label(root2, image=happy, bg="black")
                    happyLabel1.place(x=400, y=280)

                    root2.mainloop()
                    break
                question.delete(1.0,END)
                question.insert(END,questions[a[i+1]])
                option1.config(text=first_option[a[i+1]])
                option2.config(text=second_option[a[i+1]])
                option3.config(text=third_option[a[i+1]])
                option4.config(text=fourth_option[a[i+1]])
                amountlogo.config(image=amountpad[c])
            c+=1
            if value not in correct:
                option1.unbind("<Button-1>")
                option2.unbind("<Button-1>")
                option3.unbind("<Button-1>")
                option4.unbind("<Button-1>")
                c=0
                def close1():
                    root.destroy()

                def trya():
                    option1.bind("<Button-1>",select)
                    option2.bind("<Button-1>",select)
                    option3.bind("<Button-1>",select)
                    option4.bind("<Button-1>",select)
                    life12.config(state=NORMAL,image=image50)
                    life2.config(state=NORMAL,image=imageaud)
                    life3.config(state=NORMAL, image=imagephone)
                    question.delete(1.0, END)
                    a.pop()
                    random.shuffle(a)
                    a.append(14)
                    question.insert(END,questions[a[0]])
                    option1.config(text=first_option[a[0]])
                    option2.config(text=second_option[a[0]])
                    option3.config(text=third_option[a[0]])
                    option4.config(text=fourth_option[a[0]])

                    amountlogo.config(image=amount)
                    root1.destroy()

                root1=Toplevel()
                root1.overrideredirect(True)
                root1.config(bg="black")
                root1.geometry("500x500+140+30")
                root1.title("you won 0 pound")
                imgLabel=Label(root1,image=logo,bd=0)
                imgLabel.pack()
                loseLabel=Label(root1,text="you lose",font=('arail',28,"bold"),bg="black",fg="white")
                loseLabel.pack()

                tryagain=Button(root1,text="try Again",font=("arial",16,"bold"),bg="black",fg="white",
                                activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=trya)
                tryagain.pack()

                close = Button(root1, text="close", font=("arial", 16, "bold"), bg="black", fg="white",
                                activebackground="black",activeforeground="white", bd=0, cursor="hand2",command=close1)
                close.pack()
                sad=PhotoImage(file="sad.png")
                sadLabel=Label(root1,image=sad,bg="black")
                sadLabel.place(x=30,y=280)

                sadLabel1 = Label(root1, image=sad, bg="black")
                sadLabel1.place(x=400, y=280)

                root1.mainloop()
                break
    def life12():
        life12.config(image=imageNo50,state=DISABLED)
        if question.get(1.0,'end-1c')==questions[0]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[1]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[2]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[3]:
            option4.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[4]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[5]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[6]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[7]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[8]:
            option4.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[9]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[10]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[11]:
            option2.config(text='')
            option4.config(text='')
        if question.get(1.0,'end-1c')==questions[12]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[13]:
            option4.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[14]:
            option3.config(text='')
            option1.config(text='')


    def life2():
        life2.config(image=imageNoap, state=DISABLED)
        pa.place(x=580,y=190)
        pb.place(x=620, y=190)
        pc.place(x=660, y=190)
        pd.place(x=700, y=190)

        pla.place(x=580,y=320)
        plb.place(x=620, y=320)
        plc.place(x=660, y=320)
        pld.place(x=700, y=320)

        if question.get(1.0, 'end-1c') == questions[0]:
            pa.config(value=85)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[1]:
            pa.config(value=25)
            pb.config(value=10)
            pc.config(value=900)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[2]:
            pa.config(value=34)
            pb.config(value=68)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[3]:
            pa.config(value=85)
            pb.config(value=94)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[4]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=85)
        if question.get(1.0, 'end-1c') == questions[5]:
            pa.config(value=85)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[6]:
            pa.config(value=25)
            pb.config(value=10)
            pc.config(value=90)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[7]:
            pa.config(value=34)
            pb.config(value=86)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[8]:
            pa.config(value=94)
            pb.config(value=12)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[9]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=85)
            pd.config(value=67)
        if question.get(1.0, 'end-1c') == questions[10]:
            pa.config(value=95)
            pb.config(value=10)
            pc.config(value=90)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[11]:
            pa.config(value=98)
            pb.config(value=86)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[12]:
            pa.config(value=64)
            pb.config(value=88)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[13]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=85)
            pd.config(value=67)
        if question.get(1.0, 'end-1c') == questions[14]:
            pa.config(value=19)
            pb.config(value=85)
            pc.config(value=30)
            pd.config(value=67)


    def life3():
        mixer.music.load("calling.mp3")
        mixer.music.play()
        callimage.place(x=70,y=260)
        life3.config(image=noph,state=DISABLED)

    def click():
        for i in range(15):
            if question.get(1.0,"end-1c")==questions[i]:
                engine.say(f"the rootwer is {correct[i]}")
                engine.runAndWait()


    questions=["What is the capital of India",
            "Who wrote Harry Potter novels",
            "Writer of Revolution 2020",
            "In which year 3 Idiots movie Released",
            "Amoung This which is a brand of India",
            "What is the chemical symbol for water?",
            "What is the largest mammal in the world",
            "Who is credited with discovering gravity",
            " Which planet is known as the Red Planet",
            "Who painted the Mona Lisa",
            "What is the tallest mountain in the world",
            " What is the chemical symbol for gold",
            " Who wrote To Kill a Mockingbird",
            "Which country is known Land of Rising Sun",
            "What is the largest ocean in the world"]
    first_option=["Delhi","Arundati Roy","R.K. Narayan","2005","Puma","H2O","Giraffe"," Albert Einstein","Mars"," Vincent",
                "Mount Everest","Au","Anny Joe"," China","Indian Ocean"]
    second_option=["Hyderabad","Aravind Adiga","Chetan Bagat","2009","Apple","CO2","Hippopotamus","Isaac Newton","Venus",
                "Pablo Picasso","K2","Ag","Harper Lee","India","Pacific Ocean"]
    third_option=["Mumbai","J.K. Rowling","Lewis Carroll","2007","nike","NO2","Blue whale","Galileo Galilei","Jupitor","Leonardo",
                "Mount Kiliman","Xe","Ernest Heming","Japan","Atlantic Ocean"]
    fourth_option=["Bhopal","Jane Austen","Rabindranath","2010","Allen solly","H2","Elephant"," Nikola Tesla","Saturn","Michelangelo"
                ,"Mount McKinley","N","Charles Dickens","America","Arctic Ocean"]
    correct=["Delhi","J.K. Rowling","Chetan Bagat","2009","Allen solly","H2O","Blue whale","Isaac Newton","Mars","Leonardo",
            "Mount Everest","Au","Harper Lee","Japan","Pacific Ocean"]
    root=Tk()

    root.geometry("1500x1500")
    root.title("ThinQuiz")
    photo = PhotoImage(file = "thinQuiz.png")

    root.iconphoto(False, photo)

    #background
    root.config(bg="Black")

    #Question
    leftFrame=Frame(root,bg="black",padx=90)
    leftFrame.grid(row=0,column=0)

    #lifelines
    topFrame=Frame(leftFrame,bg="Black")
    topFrame.grid()
    #50:50
    image50=PhotoImage(file="image50.png")
    imageNo50=PhotoImage(file="No5050.png")
    life1=Button(topFrame,image=image50,bg="Black",border=0,activebackground="black",width=180,height=110,command=life12)
    life1.grid(row=0,column=0)
    #audience
    imageaud=PhotoImage(file="people.png")
    imageNoap=PhotoImage(file="Noap.png")
    life2=Button(topFrame,image=imageaud,bg="Black",border=0,activebackground="black",width=180,height=110,command=life2)
    life2.grid(row=0,column=1)

    #phone
    imagephone=PhotoImage(file="phone.png")
    noph=PhotoImage(file="noP.png")
    life3=Button(topFrame,image=imagephone,bg="Black",border=0,activebackground="black",width=180,height=110,command=life3)
    life3.grid(row=0,column=2)
    call=PhotoImage(file="ring.png")
    callimage=Button(root,image=call,bg="Black",bd=0,activebackground="black",cursor="hand2",command=click)

    #logo
    centerFrame=Frame(leftFrame,bg="Black")
    centerFrame.grid(row=1,column=0)

    logo=PhotoImage(file="thinQuiz.png")
    centerlogo=Label(centerFrame,image=logo,bg="Black",height=320)
    centerlogo.grid(row=0,column=2)


    #question
    bottomFrame=Frame(leftFrame)
    bottomFrame.grid(row=2,column=0)

    lay=PhotoImage(file="lay.png")
    layout=Label(bottomFrame,image=lay,bg="Black")
    layout.grid(row=0,column=0)


    question=Text(bottomFrame,font=('arial','16','bold'),width=34,height=1.3,wrap='word',bg="black",fg="white",bd=0)
    question.place(x=80,y=20)
    question.insert(END,questions[a[1]])

    labelA=Label(bottomFrame,text="A:",bg="black",fg="White",font=('arial','16','bold'))
    labelA.place(x=55,y=110)
    option1=Button(bottomFrame,text=first_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option1.place(x=100,y=105)

    labelb=Label(bottomFrame,text="B:",bg="black",fg="White",font=('arial','16','bold'))
    labelb.place(x=320,y=110)
    option2=Button(bottomFrame,text=second_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option2.place(x=370,y=105)

    labelc=Label(bottomFrame,text="C:",bg="black",fg="White",font=('arial','16','bold'))
    labelc.place(x=55,y=190)
    option3=Button(bottomFrame,text=third_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option3.place(x=100,y=185)

    labeld=Label(bottomFrame,text="D:",bg="black",fg="White",font=('arial','16','bold'))
    labeld.place(x=320,y=190)
    option4=Button(bottomFrame,text=fourth_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option4.place(x=370,y=185)

    option1.bind("<Button-1>",select)
    option2.bind("<Button-1>",select)
    option3.bind("<Button-1>",select)
    option4.bind("<Button-1>",select)

    pa=Progressbar(root,orient=VERTICAL,length=120)
    pb=Progressbar(root,orient=VERTICAL,length=120)
    pc=Progressbar(root,orient=VERTICAL,length=120)
    pd=Progressbar(root,orient=VERTICAL,length=120)

    #progressbar labels
    pla=Label(root,text="A",font=("Arial",20,"bold"),background="black",foreground="white")
    plb=Label(root,text="B",font=("Arial",20,"bold"),background="black",foreground="white")
    plc=Label(root,text="C",font=("Arial",20,"bold"),background="black",foreground="white")
    pld=Label(root,text="D",font=("Arial",20,"bold"),background="black",foreground="white")



    #Level
    rightFrame=Frame(root)
    rightFrame.grid(row=0,column=1)
    amount=PhotoImage(file="picture02.png")
    amountlogo=Label(rightFrame,image=amount,bg="yellow")
    amountlogo.grid()

    amount1=PhotoImage(file="picture1.png")
    amount2=PhotoImage(file="picture2.png")
    amount3=PhotoImage(file="picture3.png")
    amount4=PhotoImage(file="picture4.png")
    amount5=PhotoImage(file="picture5.png")
    amount6=PhotoImage(file="picture6.png")
    amount7=PhotoImage(file="picture7.png")
    amount8=PhotoImage(file="picture8.png")
    amount9=PhotoImage(file="picture9.png")
    amount10=PhotoImage(file="picture10.png")
    amount11=PhotoImage(file="picture11.png")
    amount12=PhotoImage(file="picture12.png")
    amount13=PhotoImage(file="picture13.png")
    amount14=PhotoImage(file="picture14.png")
    amount15=PhotoImage(file="picture15.png")

    amountpad = [amount1, amount2,amount3,amount4,amount5,amount6, amount7,amount8,amount9,amount10,amount11, amount12,
            amount13, amount14, amount15]

    root.mainloop()
def age2():
    new_root.destroy()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)

    mixer.init()

    a=list(range(0,14))
    random.shuffle(a)
    a.append(14)
    c=0
    def select(event):
        callimage.place_forget()

        pa.place_forget()
        pb.place_forget()
        pc.place_forget()
        pd.place_forget()

        pla.place_forget()
        plb.place_forget()
        plc.place_forget()
        pld.place_forget()

        b = event.widget
        value = b["text"]
        c=0

        for i in range(len(a)):
            if value == correct[a[i]]:
                if value == correct[14]:
                    def close1():
                        root.destroy()

                    def playa():
                        option1.bind("<Button-1>",select)
                        option2.bind("<Button-1>",select)
                        option3.bind("<Button-1>",select)
                        option4.bind("<Button-1>",select)
                        lifeo1.config(state=NORMAL, image=image50)
                        life2.config(state=NORMAL, image=imageaud)
                        life3.config(state=NORMAL,  image=imagephone)

                        question.delete(1.0, END)
                        question.insert(END, questions[a[0]])
                        option1.config(text=first_option[a[0]])
                        option2.config(text=second_option[a[0]])
                        option3.config(text=third_option[a[0]])
                        option4.config(text=fourth_option[a[0]])

                        amountlogo.config(image=amount)
                        root2.destroy()

                    root2 = Toplevel()
                    root2.overrideredirect(True)
                    root2.config(bg="black")
                    root2.geometry("500x500+140+30")
                    root2.title("you won 0 pound")
                    imgLabel = Label(root2, image=logo, bd=0)
                    imgLabel.pack()
                    winLabel = Label(root2, text="you Won", font=('arail', 28, "bold"), bg="black", fg="white")
                    winLabel.pack()

                    playagain = Button(root2, text="Play Again", font=("arial", 16, "bold"), bg="black", fg="white",
                                    activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                    command=playa)
                    playagain.pack()

                    close = Button(root2, text="close", font=("arial", 16, "bold"), bg="black", fg="white",
                                activebackground="black", activeforeground="white", bd=0, cursor="hand2", command=close1)
                    close.pack()
                    happy = PhotoImage(file="happy.png")
                    happyLabel = Label(root2, image=happy, bg="black")
                    happyLabel.place(x=30, y=280)

                    happyLabel1 = Label(root2, image=happy, bg="black")
                    happyLabel1.place(x=400, y=280)

                    root2.mainloop()
                    break
                question.delete(1.0,END)
                question.insert(END,questions[a[i+1]])
                option1.config(text=first_option[a[i+1]])
                option2.config(text=second_option[a[i+1]])
                option3.config(text=third_option[a[i+1]])
                option4.config(text=fourth_option[a[i+1]])
                amountlogo.config(image=amountpad[c])
            c+=1
            if value not in correct:
                c=0
                option1.unbind("<Button-1>")
                option2.unbind("<Button-1>")
                option3.unbind("<Button-1>")
                option4.unbind("<Button-1>")
                def close1():
                    root.destroy()

                def trya():
                    option1.bind("<Button-1>",select)
                    option2.bind("<Button-1>",select)
                    option3.bind("<Button-1>",select)
                    option4.bind("<Button-1>",select)
                    lifeo1.config(state=NORMAL,image=image50)
                    life2.config(state=NORMAL,image=imageaud)
                    life3.config(state=NORMAL, image=imagephone)
                    question.delete(1.0, END)
                    a.pop()
                    random.shuffle(a)
                    a.append(14)
                    question.insert(END,questions[a[0]])
                    option1.config(text=first_option[a[0]])
                    option2.config(text=second_option[a[0]])
                    option3.config(text=third_option[a[0]])
                    option4.config(text=fourth_option[a[0]])

                    amountlogo.config(image=amount)
                    root1.destroy()

                root1=Toplevel()
                root1.overrideredirect(True)
                root1.config(bg="black")
                root1.geometry("500x500+140+30")
                root1.title("you won 0 pound")
                imgLabel=Label(root1,image=logo,bd=0)
                imgLabel.pack()
                loseLabel=Label(root1,text="you lose",font=('arail',28,"bold"),bg="black",fg="white")
                loseLabel.pack()

                tryagain=Button(root1,text="try Again",font=("arial",16,"bold"),bg="black",fg="white",
                                activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=trya)
                tryagain.pack()

                close = Button(root1, text="close", font=("arial", 16, "bold"), bg="black", fg="white",
                                activebackground="black",activeforeground="white", bd=0, cursor="hand2",command=close1)
                close.pack()
                sad=PhotoImage(file="sad.png")
                sadLabel=Label(root1,image=sad,bg="black")
                sadLabel.place(x=30,y=280)

                sadLabel1 = Label(root1, image=sad, bg="black")
                sadLabel1.place(x=400, y=280)

                root1.mainloop()
                break
    def lifeo1():
        lifeo1.config(image=imageNo50,state=DISABLED)
        if question.get(1.0,'end-1c')==questions[0]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[1]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[2]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[3]:
            option4.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[4]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[5]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[6]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[7]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[8]:
            option4.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[9]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[10]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[11]:
            option2.config(text='')
            option4.config(text='')
        if question.get(1.0,'end-1c')==questions[12]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[13]:
            option4.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[14]:
            option3.config(text='')
            option1.config(text='')


    def life2():
        life2.config(image=imageNoap, state=DISABLED)
        pa.place(x=580,y=190)
        pb.place(x=620, y=190)
        pc.place(x=660, y=190)
        pd.place(x=700, y=190)

        pla.place(x=580,y=320)
        plb.place(x=620, y=320)
        plc.place(x=660, y=320)
        pld.place(x=700, y=320)

        if question.get(1.0, 'end-1c') == questions[0]:
            pa.config(value=85)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[1]:
            pa.config(value=25)
            pb.config(value=10)
            pc.config(value=900)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[2]:
            pa.config(value=34)
            pb.config(value=68)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[3]:
            pa.config(value=85)
            pb.config(value=94)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[4]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=85)
        if question.get(1.0, 'end-1c') == questions[5]:
            pa.config(value=85)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[6]:
            pa.config(value=25)
            pb.config(value=10)
            pc.config(value=90)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[7]:
            pa.config(value=34)
            pb.config(value=86)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[8]:
            pa.config(value=94)
            pb.config(value=12)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[9]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=85)
            pd.config(value=67)
        if question.get(1.0, 'end-1c') == questions[10]:
            pa.config(value=95)
            pb.config(value=10)
            pc.config(value=90)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[11]:
            pa.config(value=98)
            pb.config(value=86)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[12]:
            pa.config(value=64)
            pb.config(value=88)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[13]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=85)
            pd.config(value=67)
        if question.get(1.0, 'end-1c') == questions[14]:
            pa.config(value=19)
            pb.config(value=85)
            pc.config(value=30)
            pd.config(value=67)


    def life3():
        mixer.music.load("calling.mp3")
        mixer.music.play()
        callimage.place(x=70,y=260)
        life3.config(image=noph,state=DISABLED)

    def click():
        for i in range(15):
            if question.get(1.0,"end-1c")==questions[i]:
                engine.say(f"the rootwer is {correct[i]}")
                engine.runAndWait()


    questions= [
        "Which app features 'stories'?",
        "Protagonist of 'Hunger Games'?",
        "'King of Pop'?",
        "Cristiano Ronaldo's sport?",
        "Wizard in 'Harry Potter'?",
        "Maker of 'Chuck Taylor'?",
        "Gold's symbol?",
        "High school drama?",
        "'Kylie Cosmetics' owner?",
        "'Zelda' protagonist?",
        "Short videos on?",
        "Golden arches brand?",
        "'Hoodie' type?",
        "'PlayStation' creator?",
        "'Hermione' actress?"
    ]

    first_option=["Instagram","Harmione","Drake","Golf","Potter","Converse","Ag","Gossip","Kylie","Mario",
                "Tik Tok","McDonald","Shirt"," Microsoft","Indian","Selana"]
    second_option=["Facebook","Bella","Jackson","Soccer","Percy","Nike","Fe","River","Kim",
                "Kong","Youtube","Burger","Jacket","Sega","Emma"]
    third_option=["Twitter","Katniss","Sheeran","BasketBall","Edward","Adidas","Au","Stranger","Rihana","Link",
                "SnapChat","KFC","Hat","Sony","Miley"]
    fourth_option=["Tik Tok","Tris","Bieber","Tennis","Harry","Vroot","Hg","Reasons","Taylor","Sonic"
                ,"Twitch","Wendy","Pants","Nitendo","Ariana"]
    correct=["Instagram","Katniss","Jackson","Soccer","Harry","Converse","Au","River","Kylie","Link",
            "Tik Tok","McDonald","Jacket","Sony","Emma"]
    root=Tk()

    root.geometry("1570x1552")
    root.title("ThinQuiz")
    photo = PhotoImage(file = "thinQuiz.png")

    root.iconphoto(False, photo)

    #background
    root.config(bg="Black")

    #Question
    leftFrame=Frame(root,bg="black",padx=90)
    leftFrame.grid(row=0,column=0)

    #lifelines
    topFrame=Frame(leftFrame,bg="Black")
    topFrame.grid()
    #50:50
    image50=PhotoImage(file="image50.png")
    imageNo50=PhotoImage(file="No5050.png")
    lifeo1=Button(topFrame,image=image50,bg="Black",border=0,activebackground="black",width=180,height=110,command=lifeo1)
    lifeo1.grid(row=0,column=0)
    #audience
    imageaud=PhotoImage(file="people.png")
    imageNoap=PhotoImage(file="Noap.png")
    life2=Button(topFrame,image=imageaud,bg="Black",border=0,activebackground="black",width=180,height=110,command=life2)
    life2.grid(row=0,column=1)

    #phone
    imagephone=PhotoImage(file="phone.png")
    noph=PhotoImage(file="noP.png")
    life3=Button(topFrame,image=imagephone,bg="Black",border=0,activebackground="black",width=180,height=110,command=life3)
    life3.grid(row=0,column=2)
    call=PhotoImage(file="ring.png")
    callimage=Button(root,image=call,bg="Black",bd=0,activebackground="black",cursor="hand2",command=click)

    #logo
    centerFrame=Frame(leftFrame,bg="Black")
    centerFrame.grid(row=1,column=0)

    logo=PhotoImage(file="thinQuiz.png")
    centerlogo=Label(centerFrame,image=logo,bg="Black",height=320)
    centerlogo.grid(row=0,column=2)


    #question
    bottomFrame=Frame(leftFrame)
    bottomFrame.grid(row=2,column=0)

    lay=PhotoImage(file="lay.png")
    layout=Label(bottomFrame,image=lay,bg="Black")
    layout.grid(row=0,column=0)


    question=Text(bottomFrame,font=('arial','16','bold'),width=34,height=1.3,wrap='word',bg="black",fg="white",bd=0)
    question.place(x=80,y=20)
    question.insert(END,questions[a[1]])

    labelA=Label(bottomFrame,text="A:",bg="black",fg="White",font=('arial','16','bold'))
    labelA.place(x=55,y=110)
    option1=Button(bottomFrame,text=first_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option1.place(x=100,y=105)

    labelb=Label(bottomFrame,text="B:",bg="black",fg="White",font=('arial','16','bold'))
    labelb.place(x=320,y=110)
    option2=Button(bottomFrame,text=second_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option2.place(x=370,y=105)

    labelc=Label(bottomFrame,text="C:",bg="black",fg="White",font=('arial','16','bold'))
    labelc.place(x=55,y=190)
    option3=Button(bottomFrame,text=third_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option3.place(x=100,y=185)

    labeld=Label(bottomFrame,text="D:",bg="black",fg="White",font=('arial','16','bold'))
    labeld.place(x=320,y=190)
    option4=Button(bottomFrame,text=fourth_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option4.place(x=370,y=185)

    option1.bind("<Button-1>",select)
    option2.bind("<Button-1>",select)
    option3.bind("<Button-1>",select)
    option4.bind("<Button-1>",select)

    pa=Progressbar(root,orient=VERTICAL,length=120)
    pb=Progressbar(root,orient=VERTICAL,length=120)
    pc=Progressbar(root,orient=VERTICAL,length=120)
    pd=Progressbar(root,orient=VERTICAL,length=120)

    #progressbar labels
    pla=Label(root,text="A",font=("Arial",20,"bold"),background="black",foreground="white")
    plb=Label(root,text="B",font=("Arial",20,"bold"),background="black",foreground="white")
    plc=Label(root,text="C",font=("Arial",20,"bold"),background="black",foreground="white")
    pld=Label(root,text="D",font=("Arial",20,"bold"),background="black",foreground="white")



    #Level
    rightFrame=Frame(root)
    rightFrame.grid(row=0,column=1)
    amount=PhotoImage(file="picture02.png")
    amountlogo=Label(rightFrame,image=amount,bg="yellow")
    amountlogo.grid()

    amount1=PhotoImage(file="picture1.png")
    amount2=PhotoImage(file="picture2.png")
    amount3=PhotoImage(file="picture3.png")
    amount4=PhotoImage(file="picture4.png")
    amount5=PhotoImage(file="picture5.png")
    amount6=PhotoImage(file="picture6.png")
    amount7=PhotoImage(file="picture7.png")
    amount8=PhotoImage(file="picture8.png")
    amount9=PhotoImage(file="picture9.png")
    amount10=PhotoImage(file="picture10.png")
    amount11=PhotoImage(file="picture11.png")
    amount12=PhotoImage(file="picture12.png")
    amount13=PhotoImage(file="picture13.png")
    amount14=PhotoImage(file="picture14.png")
    amount15=PhotoImage(file="picture15.png")

    amountpad = [amount1, amount2,amount3,amount4,amount5,amount6, amount7,amount8,amount9,amount10,amount11, amount12,
            amount13, amount14, amount15]

    root.mainloop()

# age group page 
def life1():
    # destroy start page 
    root1.destroy()
    global new_root
    new_root = Tk()
    new_root.geometry("1500x1500")
    new_root.title("new window")
    photo = PhotoImage(file = "thinQuiz.png")

    new_root.iconphoto(False, photo)
    new_root.config(bg="black")

    #lifelines


    #logo
    centerFrame=Frame(new_root,bg="Black")
    centerFrame.grid(row=0,column=0)
    a=Label(centerFrame,bg="Black",text="Select your age group",foreground="white",font=("Arial",20,"bold"),height=5,width=70)
    a.grid(row=0,column=2,padx=70)

    logo=PhotoImage(file="thinQuiz.png")
    centerlogo=Label(centerFrame,image=logo,bg="Black",height=320)
    centerlogo.grid(row=1,column=2)


    #ages grp


    topFrame=Frame(new_root,bg="Black")
    topFrame.grid(row=1,column=0,padx=70)
    option1=Button(topFrame,text="General",font=('arial','16','bold'),bg="black",fg="white",bd=3,activebackground="black",command=age1)
    option1.grid(row=0,column=0,padx=20)
    option2=Button(topFrame,text="Below 20",font=('arial','16','bold'),bg="black",fg="white",bd=3,activebackground="black",command=age2)
    option2.grid(row=0,column=1,padx=20)
    option3=Button(topFrame,text="Above 20",font=('arial','16','bold'),bg="black",fg="white",bd=3,activebackground="black",command=age3)
    option3.grid(row=0,column=2,padx=20)
    new_root.mainloop()

def home():
    global root1
    root1=Tk()
    root1.geometry("1500x1500")
    root1.title("Home")
    root1.config(bg="black")

    centerFrame=Frame(root1,bg="Black")
    centerFrame.grid(row=0,column=0,padx=160)
    logo=PhotoImage(file="thinQuiz.png")
    centerlogo=Label(centerFrame,image=logo,bg="Black",height=500, width=1000)
    centerlogo.grid()
    a=Label(root1,bg="Black",text="Press Start to begin the game",bd=5,foreground="white",font=("Arial",20,"bold"))
    a.grid(row=1,column=0)

    topFrame=Frame(root1,bg="Black")
    topFrame.grid(row=2,column=0,padx=160)
    image50=PhotoImage(file="start.png",)
    life=Button(topFrame,image=image50,bg="Black",border=0,activebackground="black",width=380,height=110, command=life1)
    life.grid(row=1,column=0)


    root1.mainloop()
def age3():
    new_root.destroy()


    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)

    mixer.init()


    a=list(range(0,14))
    random.shuffle(a)
    a.append(14)
    c=0
    def select(event):
        callimage.place_forget()

        pa.place_forget()
        pb.place_forget()
        pc.place_forget()
        pd.place_forget()

        pla.place_forget()
        plb.place_forget()
        plc.place_forget()
        pld.place_forget()

        b = event.widget
        value = b["text"]
        c=0

        for i in range(len(a)):
            if value == correct[a[i]]:
                if value == correct[14]:
                    def close1():
                        root.destroy()

                    def playa():
                        option1.bind("<Button-1>",select)
                        option2.bind("<Button-1>",select)
                        option3.bind("<Button-1>",select)
                        option4.bind("<Button-1>",select)
                        life1.config(state=NORMAL, image=image50)
                        life2.config(state=NORMAL, image=imageaud)
                        life3.config(state=NORMAL,  image=imagephone)

                        question.delete(1.0, END)
                        question.insert(END, questions[a[0]])
                        option1.config(text=first_option[a[0]])
                        option2.config(text=second_option[a[0]])
                        option3.config(text=third_option[a[0]])
                        option4.config(text=fourth_option[a[0]])

                        amountlogo.config(image=amount)
                        root2.destroy()

                    root2 = Toplevel()
                    root2.overrideredirect(True)
                    root2.config(bg="black")
                    root2.geometry("500x500+140+30")
                    root2.title("you won 0 pound")
                    imgLabel = Label(root2, image=logo, bd=0)
                    imgLabel.pack()
                    winLabel = Label(root2, text="you Won", font=('arail', 28, "bold"), bg="black", fg="white")
                    winLabel.pack()

                    playagain = Button(root2, text="Play Again", font=("arial", 16, "bold"), bg="black", fg="white",
                                    activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                    command=playa)
                    playagain.pack()

                    close = Button(root2, text="close", font=("arial", 16, "bold"), bg="black", fg="white",
                                activebackground="black", activeforeground="white", bd=0, cursor="hand2", command=close1)
                    close.pack()
                    happy = PhotoImage(file="happy.png")
                    happyLabel = Label(root2, image=happy, bg="black")
                    happyLabel.place(x=30, y=280)

                    happyLabel1 = Label(root2, image=happy, bg="black")
                    happyLabel1.place(x=400, y=280)

                    root2.mainloop()
                    break
                question.delete(1.0,END)
                question.insert(END,questions[a[i+1]])
                option1.config(text=first_option[a[i+1]])
                option2.config(text=second_option[a[i+1]])
                option3.config(text=third_option[a[i+1]])
                option4.config(text=fourth_option[a[i+1]])
                amountlogo.config(image=amountpad[c])
            c+=1
            if value not in correct:
                c=0
                option1.unbind("<Button-1>")
                option2.unbind("<Button-1>")
                option3.unbind("<Button-1>")
                option4.unbind("<Button-1>")

                def close1():
                    root.destroy()

                def trya():
                    option1.bind("<Button-1>",select)
                    option2.bind("<Button-1>",select)
                    option3.bind("<Button-1>",select)
                    option4.bind("<Button-1>",select)
                    life1.config(state=NORMAL,image=image50)
                    life2.config(state=NORMAL,image=imageaud)
                    life3.config(state=NORMAL, image=imagephone)
                    question.delete(1.0, END)
                    a.pop()
                    random.shuffle(a)
                    a.append(14)
                    question.insert(END,questions[a[0]])
                    option1.config(text=first_option[a[0]])
                    option2.config(text=second_option[a[0]])
                    option3.config(text=third_option[a[0]])
                    option4.config(text=fourth_option[a[0]])

                    amountlogo.config(image=amount)
                    root1.destroy()

                root1=Toplevel()
                root1.overrideredirect(True)
                root1.config(bg="black")
                root1.geometry("500x500+140+30")
                root1.title("you won 0 pound")
                imgLabel=Label(root1,image=logo,bd=0)
                imgLabel.pack()
                loseLabel=Label(root1,text="you lose",font=('arail',28,"bold"),bg="black",fg="white")
                loseLabel.pack()

                tryagain=Button(root1,text="try Again",font=("arial",16,"bold"),bg="black",fg="white",
                                activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=trya)
                tryagain.pack()

                close = Button(root1, text="close", font=("arial", 16, "bold"), bg="black", fg="white",
                                activebackground="black",activeforeground="white", bd=0, cursor="hand2",command=close1)
                close.pack()
                sad=PhotoImage(file="sad.png")
                sadLabel=Label(root1,image=sad,bg="black")
                sadLabel.place(x=30,y=280)

                sadLabel1 = Label(root1, image=sad, bg="black")
                sadLabel1.place(x=400, y=280)

                root1.mainloop()
                break
    def lifeo2():
        life1.config(image=imageNo50,state=DISABLED)
        if question.get(1.0,'end-1c')==questions[0]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[1]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[2]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[3]:
            option4.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[4]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[5]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[6]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[7]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[8]:
            option4.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[9]:
            option2.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[10]:
            option2.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[11]:
            option2.config(text='')
            option4.config(text='')
        if question.get(1.0,'end-1c')==questions[12]:
            option1.config(text='')
            option3.config(text='')
        if question.get(1.0,'end-1c')==questions[13]:
            option4.config(text='')
            option1.config(text='')
        if question.get(1.0,'end-1c')==questions[14]:
            option3.config(text='')
            option1.config(text='')


    def life2():
        life2.config(image=imageNoap, state=DISABLED)
        pa.place(x=580,y=190)
        pb.place(x=620, y=190)
        pc.place(x=660, y=190)
        pd.place(x=700, y=190)

        pla.place(x=580,y=320)
        plb.place(x=620, y=320)
        plc.place(x=660, y=320)
        pld.place(x=700, y=320)

        if question.get(1.0, 'end-1c') == questions[0]:
            pa.config(value=85)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[1]:
            pa.config(value=25)
            pb.config(value=10)
            pc.config(value=900)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[2]:
            pa.config(value=34)
            pb.config(value=68)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[3]:
            pa.config(value=85)
            pb.config(value=94)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[4]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=85)
        if question.get(1.0, 'end-1c') == questions[5]:
            pa.config(value=85)
            pb.config(value=30)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[6]:
            pa.config(value=25)
            pb.config(value=10)
            pc.config(value=90)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[7]:
            pa.config(value=34)
            pb.config(value=86)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[8]:
            pa.config(value=94)
            pb.config(value=12)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[9]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=85)
            pd.config(value=67)
        if question.get(1.0, 'end-1c') == questions[10]:
            pa.config(value=95)
            pb.config(value=10)
            pc.config(value=90)
            pd.config(value=53)
        if question.get(1.0, 'end-1c') == questions[11]:
            pa.config(value=98)
            pb.config(value=86)
            pc.config(value=67)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[12]:
            pa.config(value=64)
            pb.config(value=88)
            pc.config(value=30)
            pd.config(value=55)
        if question.get(1.0, 'end-1c') == questions[13]:
            pa.config(value=19)
            pb.config(value=30)
            pc.config(value=85)
            pd.config(value=67)
        if question.get(1.0, 'end-1c') == questions[14]:
            pa.config(value=19)
            pb.config(value=85)
            pc.config(value=30)
            pd.config(value=67)


    def life3():
        mixer.music.load("calling.mp3")
        mixer.music.play()
        callimage.place(x=70,y=260)
        life3.config(image=noph,state=DISABLED)

    def click():
        for i in range(15):
            if question.get(1.0,"end-1c")==questions[i]:
                engine.say(f"the rootwer is {correct[i]}")
                engine.runAndWait()


    questions= [
        "Berlin wall fall in:",
        "Capital of Canada?",
        "Author of 'The Shining'?",
        "Currency of Greece",
        "Largest Bone in Body",
        "Painter of 'Starry Night'",
        "Smallest US state?",
        "Writer of 'Pride and Prejudice'",
        "Symbol of potassium'?",
        "Longest river in Africa?",
        "First women in space",
        "Designer of Eiffel Tower",
        "Smallest Planet",
        "Beethoven's Nationality",
        "Inventor of light bulb"
    ]

    first_option=["1989","Toronto","Koontz","Drachma","Ulna","VanGogh","Texas","Bronte","K","Congo",
                "Tereshkova","Eiffel","Venus","Austria","Bell"]
    second_option=["1988","Vancouver","King","Euro","Humerus","Monet","Delware","Austen","P",
                "Niger","Ride","Gaudi","Mercury","French","Edison"]
    third_option=["1987","Ottawa","Barker","Lira","Tibia","Picasso","Rhodelsland","Dickens","Na","Nile",
                "Savitskaya","Saarinen","Mars","German","Tesla"]
    fourth_option=["1990","Montreal","Rice","Franc","Femur","Dali","Hawai","Eliot","Ca","Zambezi"
                ,"Kondakova","Wright","Earth","Italian","marconi"]
    correct=["1989","Ottawa","King","Euro","Femur","VanGogh","Rhodelsland","Austen","K","Nile",
            "Tereshkova","Eiffel","Mercury","German","Edison"]
    root=Tk()

    root.geometry("1570x1552")
    root.title("ThinQuiz")

    photo = PhotoImage(file = "thinQuiz.png")

    root.iconphoto(False, photo)

    #background
    root.config(bg="Black")

    #Question
    leftFrame=Frame(root,bg="black",padx=90)
    leftFrame.grid(row=0,column=0)

    #lifelines
    topFrame=Frame(leftFrame,bg="Black")
    topFrame.grid()
    #50:50
    image50=PhotoImage(file="image50.png")
    imageNo50=PhotoImage(file="No5050.png")
    life1=Button(topFrame,image=image50,bg="Black",border=0,activebackground="black",width=180,height=110,command=lifeo2)
    life1.grid(row=0,column=0)
    #audience
    imageaud=PhotoImage(file="people.png")
    imageNoap=PhotoImage(file="Noap.png")
    life2=Button(topFrame,image=imageaud,bg="Black",border=0,activebackground="black",width=180,height=110,command=life2)
    life2.grid(row=0,column=1)

    #phone
    imagephone=PhotoImage(file="phone.png")
    noph=PhotoImage(file="noP.png")
    life3=Button(topFrame,image=imagephone,bg="Black",border=0,activebackground="black",width=180,height=110,command=life3)
    life3.grid(row=0,column=2)
    call=PhotoImage(file="ring.png")
    callimage=Button(root,image=call,bg="Black",bd=0,activebackground="black",cursor="hand2",command=click)

    #logo
    centerFrame=Frame(leftFrame,bg="Black")
    centerFrame.grid(row=1,column=0)

    logo=PhotoImage(file="thinQuiz.png")
    centerlogo=Label(centerFrame,image=logo,bg="Black",height=320)
    centerlogo.grid(row=0,column=2)


    #question
    bottomFrame=Frame(leftFrame)
    bottomFrame.grid(row=2,column=0)

    lay=PhotoImage(file="lay.png")
    layout=Label(bottomFrame,image=lay,bg="Black")
    layout.grid(row=0,column=0)


    question=Text(bottomFrame,font=('arial','16','bold'),width=34,height=1.3,wrap='word',bg="black",fg="white",bd=0)
    question.place(x=80,y=20)
    question.insert(END,questions[a[1]])

    labelA=Label(bottomFrame,text="A:",bg="black",fg="White",font=('arial','16','bold'))
    labelA.place(x=55,y=110)
    option1=Button(bottomFrame,text=first_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option1.place(x=100,y=105)

    labelb=Label(bottomFrame,text="B:",bg="black",fg="White",font=('arial','16','bold'))
    labelb.place(x=320,y=110)
    option2=Button(bottomFrame,text=second_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option2.place(x=370,y=105)

    labelc=Label(bottomFrame,text="C:",bg="black",fg="White",font=('arial','16','bold'))
    labelc.place(x=55,y=190)
    option3=Button(bottomFrame,text=third_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option3.place(x=100,y=185)

    labeld=Label(bottomFrame,text="D:",bg="black",fg="White",font=('arial','16','bold'))
    labeld.place(x=320,y=190)
    option4=Button(bottomFrame,text=fourth_option[a[1]],font=('arial','16','bold'),bg="black",fg="white",bd=0,activebackground="black",cursor="hand2")
    option4.place(x=370,y=185)

    option1.bind("<Button-1>",select)
    option2.bind("<Button-1>",select)
    option3.bind("<Button-1>",select)
    option4.bind("<Button-1>",select)

    pa=Progressbar(root,orient=VERTICAL,length=120)
    pb=Progressbar(root,orient=VERTICAL,length=120)
    pc=Progressbar(root,orient=VERTICAL,length=120)
    pd=Progressbar(root,orient=VERTICAL,length=120)

    #progressbar labels
    pla=Label(root,text="A",font=("Arial",20,"bold"),background="black",foreground="white")
    plb=Label(root,text="B",font=("Arial",20,"bold"),background="black",foreground="white")
    plc=Label(root,text="C",font=("Arial",20,"bold"),background="black",foreground="white")
    pld=Label(root,text="D",font=("Arial",20,"bold"),background="black",foreground="white")



    #Level
    rightFrame=Frame(root)
    rightFrame.grid(row=0,column=1)
    amount=PhotoImage(file="picture02.png")
    amountlogo=Label(rightFrame,image=amount,bg="yellow")
    amountlogo.grid()

    amount1=PhotoImage(file="picture1.png")
    amount2=PhotoImage(file="picture2.png")
    amount3=PhotoImage(file="picture3.png")
    amount4=PhotoImage(file="picture4.png")
    amount5=PhotoImage(file="picture5.png")
    amount6=PhotoImage(file="picture6.png")
    amount7=PhotoImage(file="picture7.png")
    amount8=PhotoImage(file="picture8.png")
    amount9=PhotoImage(file="picture9.png")
    amount10=PhotoImage(file="picture10.png")
    amount11=PhotoImage(file="picture11.png")
    amount12=PhotoImage(file="picture12.png")
    amount13=PhotoImage(file="picture13.png")
    amount14=PhotoImage(file="picture14.png")
    amount15=PhotoImage(file="picture15.png")

    amountpad = [amount1, amount2,amount3,amount4,amount5,amount6, amount7,amount8,amount9,amount10,amount11, amount12,
            amount13, amount14, amount15]

    root.mainloop()

# home function called to start the game
home()
