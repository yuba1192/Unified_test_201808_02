import tkinter

# 移動先のチェック
def check_move (x):
    global mario_x
    if x>=1 and x * mario_walk_x + 10 <= 830:
        mario_x = x
        canvas.delete("mario")
        canvas.create_image(mario_x * mario_walk_x + 10, 454 - 40, image=images[mario - 1], tag="mario")
        canvas.coords("mario", mario_x * mario_walk_x + 10, 454 - 40)
    elif x <= 0:
        canvas.delete("mario")
        canvas.create_image(1 * mario_walk_x + 10, 454 - 40, image=images[mario - 1], tag="mario")
    else:
        canvas.delete("mario")
        canvas.create_image(mario_x * mario_walk_x + 10, 454 - 40, image=images[mario - 1], tag="mario")

# 左ボタンが押された
def click_button_left(event):
    global mario
    if mario == 4:
        mario = 5
        check_move(mario_x - 1)
    elif mario == 5:
        mario = 6
        check_move(mario_x - 1)
    elif mario == 6:
        mario = 4
        check_move(mario_x - 1)
    else:
        mario = 4
        check_move(mario_x)

# 右ボタンが押された
def click_button_right(event):
    global mario
    if mario == 1:
        mario = 2
        check_move(mario_x + 1)
    elif mario == 2:
        mario = 3
        check_move(mario_x + 1)
    elif mario == 3:
        mario = 1
        check_move(mario_x + 1)
    else:
        mario = 1
        check_move(mario_x)

# ウィンドウの作成
root = tkinter.Tk()
root.title("マリオ")
root.minsize(860, 454)
root.maxsize(860, 454)

# 矢印
frame = tkinter.Frame(root, width=860, height=454)
frame.bind("<Left>", click_button_left)
frame.bind("<Right>", click_button_right)
frame.focus_set()
frame.pack()

#キャンバス作成
canvas =tkinter.Canvas(width=860, height=454)
canvas.place(x=0, y=0)
canvas.create_rectangle(0, 0, 860, 454, fill="white",tag="drawField")


# 画像データ読み込み
images = [tkinter.PhotoImage(file="img/mario_1.png"),
          tkinter.PhotoImage(file="img/mario_2.png"),
          tkinter.PhotoImage(file="img/mario_3.png"),
          tkinter.PhotoImage(file="img/mario_4.png"),
          tkinter.PhotoImage(file="img/mario_5.png"),
          tkinter.PhotoImage(file="img/mario_6.png"),]

mario = 1
mario_x = 1
mario_walk_x = 20

canvas.create_image(mario_x * mario_walk_x + 10, 454 - 40, image=images[0], tag="mario")
root.mainloop()