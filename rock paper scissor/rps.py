from tkinter import *
import random

comp_score = 0
player_score = 0


choice_list =["rock " , "paper","scissor"]

def set_comp_image(comp_inp):
        if comp_inp == "rock":
            comp_label.config(image=rock_image)
        elif comp_inp =="paper":
            comp_label.config(image=paper_image)
        elif comp_inp == "scissor":
            comp_label.config(image=scissor_image)

def rock_input():
    global player_score
    global comp_score
    player_input = "rock"
    player_label.config(image=rock_image)
    comp_input = random.choice(choice_list)
    set_comp_image(comp_input)
    if comp_input == "paper":
        comp_score += 1
    elif comp_input == "scissor":
        player_score += 1

    player_name_label.config(text=f"player:{player_score}")
    comp_name_label.config(text=f"computer :{comp_score}")

def paper_input():
     global player_score
     global comp_score
     player_input ="paper"
     player_label.config(image=paper_image)
     comp_input =random.choice(choice_list)
     set_comp_image(comp_input)
     if comp_input=="rock":
         player_score +=1
     elif comp_input=="scissor":
         comp_score +=1          

     player_name_label.config(text=f"player:{player_score}")
     comp_name_label.config(text=f"computer :{comp_score}")

def scissor_input():
     global player_score
     global comp_score
     player_input ="scissor"
     player_label.config(image=scissor_image)
     comp_input =random.choice(choice_list)
     set_comp_image(comp_input)
     if comp_input=="paper":
         player_score +=1
     elif comp_input=="rock":
         comp_score +=1          

     player_name_label.config(text=f"player:{player_score}")
     comp_name_label.config(text=f"computer :{comp_score}") 

game_window = Tk()
game_window.title("rock paper scissor")

game_window.config(bg="#4509FC")

rock_image=PhotoImage(file="rock.jpeg")
scissor_image=PhotoImage(file="scissor.jpeg")
paper_image=PhotoImage(file="paper.jpeg")
comp_label=Label(game_window,bg="green",image=rock_image)
comp_label.place(x=190,y=180)

player_label = Label(game_window,bg="red", image= paper_image)
player_label.place(x=670,y=180)

paper_button=Button(game_window , text="PAPER",bg="#21FEC7" ,command=paper_input , width=25,height=5)
paper_button.place(x=274,y=600)

rock_button=Button(game_window , text="ROCK" ,bg="#21FEC7" ,command=rock_input , width=25,height=5)
rock_button.place(x=574,y=600)

scissor_button=Button(game_window , text="SCISSOR" ,bg="#21FEC7" ,command=scissor_input , width=25,height=5)
scissor_button.place(x=874,y=600)

comp_name_label=Label(game_window,text=f"COMPUTER:{comp_score}",width=25,height=5,bg="#F7A8FE")
comp_name_label.place(x=1200 , y=300)

player_name_label=Label(game_window,text=f"PLAYER:{player_score}",width=25,height=5 ,bg="#F7A8FE")
player_name_label.place(x=1200 , y=400)

game_window.mainloop()


