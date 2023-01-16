import tkinter

import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x400")
app.resizable(False, False)
app.eval("tk::PlaceWindow . center")
app.title("Python Password Generator")


def print_test():
    print("password")


def combo_callback(choice):
    print(choice)


bg_img = ImageTk.PhotoImage(Image.open("bg.png"))
background = customtkinter.CTkLabel(master=app, image=bg_img)
background.pack()

frame = customtkinter.CTkFrame(master=background,
                               width=400, height=200, corner_radius=15, bg_color="#1b1b1b")
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

lb_password_bd = customtkinter.CTkLabel(master=frame,
                                        width=304, height=49, corner_radius=4,
                                        fg_color="gray50")
lb_password_bd.place(x=40, y=20)
lb_password = customtkinter.CTkLabel(master=frame, text="* * * * * * * *",
                                     width=300, height=45, corner_radius=4,
                                     fg_color="gray15", bg_color="gray50",
                                     font=("System", 25))
lb_password.place(x=42, y=22)

chk_upper = customtkinter.CTkCheckBox(master=frame, text="ABC")
chk_upper.place(x=50, y=100)

chk_lower = customtkinter.CTkCheckBox(master=frame, text="abc")
chk_lower.place(x=125, y=100)

chk_digit = customtkinter.CTkCheckBox(master=frame, text="123")
chk_digit.place(x=200, y=100)

chk_symbol = customtkinter.CTkCheckBox(master=frame, text="#&$")
chk_symbol.place(x=275, y=100)

lb_password_len = customtkinter.CTkLabel(master=frame, text="Pass Length")
lb_password_len.place(x=50, y=149)
cb_password_len = customtkinter.CTkComboBox(master=frame,
                                            width=120,
                                            values=["16", "32", "64", "128"],
                                            command=combo_callback)
cb_password_len.set("16")
cb_password_len.place(x=130, y=150)

copy_icon = customtkinter.CTkImage(Image.open("gen-icon.png").resize((25, 25)))
bt_generate_pass = customtkinter.CTkButton(master=frame, text="", image=copy_icon, width=25)
bt_generate_pass.place(x=260, y=150)

copy_icon = customtkinter.CTkImage(Image.open("copy-icon.png").resize((25, 25)))
bt_copy_pass = customtkinter.CTkButton(master=frame, text="", image=copy_icon, width=25)
bt_copy_pass.place(x=305, y=150)

app.mainloop()
