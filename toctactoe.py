import tkinter as tk
from tkinter import messagebox

def check_win():
    for  i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[i[0]]["text"]==buttons[i[1]]["text"]==buttons[i[2]]["text"]!="":
            buttons[i[0]].config(bg="green")
            buttons[i[2]].config(bg="green")
            buttons[i[1]].config(bg="green")
            messagebox.showinfo("tic-tac-toe",f"player {buttons[i[0]]["text"]} wins!")
        
            
            
        # elif is_draw():
        #     label.config(text=" its a draw")
            
            root.quit()
            
def button_click(index):
    if buttons[index]["text"]=="" and not winner:
        buttons[index]["text"]= current_player
        check_win()
        change_player()
        # is_draw()


# def is_draw():  
#     for i in range(0,9):  
#         sum=0
#         sum=sum+i
#         if all(buttons[i]!="") and not winner:
#             if sum==36:
#                 messagebox.showinfo("tic-tac-toe ","match draw!")
        
#         root.quit()
    #     return False
    # else:
        # label.config(text="it's a draw ")
        # check_win()
        
        
        
def change_player():
    global current_player
    current_player="x" if current_player=="o" else "o"
    label.config(text=f"player{current_player}'s turn")
    
root=tk.Tk()
root.title=("Tic-Tac-Toe")

buttons=[tk.Button(root,text="",font=("normal",25),width=6,height=2,command=lambda i=i: button_click(i)) for i in range(9)]

for i , button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player="x"
winner=False
label=tk.Label(root,text=f"player { current_player}'s turn" ,font=("normal",15))
label.grid(row=3,column=0, columnspan=3)




# def is_draw(buttons):
#     if(buttons["text"] !=""):
#         return True
        
        
root.mainloop()