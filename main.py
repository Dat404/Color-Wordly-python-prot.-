#################################################
#                                               #
#       It like a wordly but with colors!       #
#       Made by Dat404(Daxya) v=0.0.2           #
#                                               #
#################################################

#IMPORTS start:
from tkinter import *
from random import choice
from PIL import Image, ImageTk
#IMPORTS end.


BOX_RADIUS = 64
KEY_MAP = {           
    "r":"red",
    "o":"orange",
    "y":"yellow",
    "g":"green",
    "s":"skyblue",
    "b":"blue",
    "p":"purple"
}

squares_list = []
guessed_order = [choice([KEY_MAP[c] for c in KEY_MAP]) for i in range(0,4)]
print(guessed_order)


#FUNCTIONS start:
def check_guess(guess_list):

    for i in range(4):
        guess_color = guess_list[i]
        target_color = guessed_order[i]


        x = squares_list[-4 + i]["x"]
        y = squares_list[-4 + i]["y"]

        if guess_color == target_color:
            label = "G"
        elif guess_color in guessed_order:
            label = "I"
        else:
            label = "N"

        canvas.create_text(x + BOX_RADIUS // 2, y + BOX_RADIUS // 2,
                           text=label, fill="white", font=("Fixedsys", 34, "bold"))
        
        if guess_list == guessed_order:
            img = Image.open("images/overlays/win_overlay.png").convert("RGBA")
            tk_img = ImageTk.PhotoImage(img)
            canvas.win_overlay = tk_img
            canvas.create_image(0, 0, anchor="nw", image=canvas.win_overlay)

        if guess_list != guessed_order and len(squares_list) >= 16:
            img = Image.open("images/overlays/lose_overlay.png").convert("RGBA")
            tk_img = ImageTk.PhotoImage(img)
            canvas.lose_overlay = tk_img
            canvas.create_image(0, 0, image=canvas.lose_overlay, anchor="nw")




def on_key_press(event):
    key = event.char.lower()
    if key in KEY_MAP:
        index = len(squares_list)
        col = index % 4
        row = index // 4


        x1 = col * BOX_RADIUS
        y1 = row * BOX_RADIUS
        x2 = x1 + BOX_RADIUS
        y2 = y1 + BOX_RADIUS


        square_id = canvas.create_rectangle(x1, y1, x2, y2, fill=KEY_MAP[key])
        canvas.tag_lower(square_id)

        squares_list.append({"x": x1, "y": y1, "color": KEY_MAP[key]})


        if len(squares_list) % 4 == 0:

            guess = [squares_list[i]["color"] for i in range(len(squares_list) - 4, len(squares_list))]
            check_guess(guess)




#FUNCTIONS end.


root = Tk()

window_size = 256
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{window_size}x{window_size}+{(screen_width // 2) - (window_size // 2)}+{(screen_height // 2) - (window_size // 2)}")
root.title("KULUR!")
root.resizable(False,False)
root.configure(bg="black")

root.bind("<Key>", on_key_press)
canvas = Canvas(root, width=window_size, height=window_size)
canvas.pack()

img = Image.open("images/overlays/game_overlay.png").convert("RGBA")
tk_img = ImageTk.PhotoImage(img)
canvas.game_overlay = tk_img
canvas.create_image(0, 0, image=canvas.game_overlay, anchor="nw")


root.mainloop()