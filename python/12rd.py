from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

def func_open():
    filepath = askopenfilename(
        title="gif 이미지 로드",
        filetypes=(("GIF 이미지", "*.gif"),)
    )

    if filepath:
        tk_img = PhotoImage(file=filepath)

        image_label.config(image=tk_img)
        image_label.image = tk_img

def func_exit():
    window.quit()
    window.destroy()


window = Tk()
window.title("Gif 뷰어")
window.geometry("600x500")

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

viewMenu = Menu(mainMenu)
mainMenu.add_cascade(label="보기", menu=viewMenu)
viewMenu.add_command(label="축소")
viewMenu.add_separator()
viewMenu.add_command(label="확대")

homeMenu = Menu(mainMenu)
mainMenu.add_cascade(label="홈", menu=homeMenu)
homeMenu.add_command(label="저장")
homeMenu.add_separator()
homeMenu.add_command(label="선택")
homeMenu.add_command(label="찾기")


image_label = Label(window)
image_label.pack(expand=True)

window.mainloop()
