import customtkinter
from PIL import ImageTk, Image
import pyperclip
import random
import tkinter

# GUI WINDOW SETTINGS
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('500x400')
app.resizable(False, False)
app.eval('tk::PlaceWindow . center')
app.title('Python Password Generator')

# GLOBAL PASSWORD
password = ''


def get_char_types():
    # RETURN ARRAY OF USER SELECTED CHAR TYPES FROM GUI CHECKBOXES
    types = []
    if chk_upper.get() == 1:
        types.append(1)
    if chk_lower.get() == 1:
        types.append(2)
    if chk_digit.get() == 1:
        types.append(3)
    if chk_symbol.get() == 1:
        types.append(4)
    return types


def get_char(char_types):
    # CHOOSE A RANDOM USER SELECTED CHAR TYPE AND _
    # RETURN A DECIMAL IN THAT RANGE TO CONVERT TO ASCII
    match random.choice(char_types):
        # UPPERCASE
        case 1:
            return random.randint(65, 90)
        # LOWERCASE
        case 2:
            return random.randint(97, 122)
        # NUMBERS
        case 3:
            return random.randint(48, 57)
        # SYMBOLS
        case 4:
            rnd = random.randint(1, 4)
            match rnd:
                case 1:
                    return random.randint(33, 47)
                case 2:
                    return random.randint(58, 64)
                case 3:
                    return random.randint(91, 96)
                case 4:
                    return random.randint(123, 126)


def generate_password():
    global password
    password = ''
    password_len = int(cb_password_len.get())
    char_types = get_char_types()
    for i in range(password_len):
        # IF USER HAS NOT SELECTED ANY CHAR TYPES DO NOT GENERATE PASSWORD
        if len(char_types) > 0:
            password += chr(get_char(char_types))
        else:
            password = '* * * * * * * *'
    # NOT USING AN ENTRY COMPONENT - TRIM LABEL TO CONFINE TEXT TO BORDER
    lb_password.configure(text=password[:16])


def copy_password():
    # COPY PASSWORD TO OS CLIPBOARD
    global password
    if password != '* * * * * * * *':
        pyperclip.copy(password)


# GUI DESIGN LAYOUT
# BACKGROUND WALLPAPER
bg_img = ImageTk.PhotoImage(Image.open('bg.png'))
background = customtkinter.CTkLabel(master=app, image=bg_img)
background.pack()

# INNER FRAME FOR MAIN COMPONENTS
frame = customtkinter.CTkFrame(master=background,
                               width=400, height=200, corner_radius=15, bg_color='#1b1b1b')
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# PASSWORD DISPLAY BOX
lb_password_bd = customtkinter.CTkLabel(master=frame,
                                        width=304, height=49, corner_radius=4,
                                        fg_color='gray50')
lb_password_bd.place(x=40, y=20)
lb_password = customtkinter.CTkLabel(master=frame, text='* * * * * * * *',
                                     width=300, height=45, corner_radius=4,
                                     fg_color='gray15', bg_color='gray50',
                                     wraplength=0, font=('System', 25))
lb_password.place(x=42, y=22)

# CHAR TYPE CHECKBOXES
chk_upper = customtkinter.CTkCheckBox(master=frame, text='ABC')
chk_upper.place(x=50, y=100)

chk_lower = customtkinter.CTkCheckBox(master=frame, text='abc')
chk_lower.place(x=125, y=100)

chk_digit = customtkinter.CTkCheckBox(master=frame, text='123')
chk_digit.place(x=200, y=100)

chk_symbol = customtkinter.CTkCheckBox(master=frame, text='#&$')
chk_symbol.place(x=275, y=100)

# COMBOBOX FOR PASSWORD LENGTH
lb_password_len = customtkinter.CTkLabel(master=frame, text='Pass Length')
lb_password_len.place(x=50, y=149)
cb_password_len = customtkinter.CTkComboBox(master=frame,
                                            width=120,
                                            values=['16', '32', '64', '128'])
cb_password_len.set('16')
cb_password_len.place(x=130, y=150)

# BUTTONS TO GENERATE AND COPY PASSWORD
copy_icon = customtkinter.CTkImage(Image.open('gen-icon.png').resize((25, 25)))
bt_generate_pass = customtkinter.CTkButton(master=frame, text='',
                                           image=copy_icon, width=25,
                                           command=generate_password)
bt_generate_pass.place(x=260, y=150)

copy_icon = customtkinter.CTkImage(Image.open('copy-icon.png').resize((25, 25)))
bt_copy_pass = customtkinter.CTkButton(master=frame, text='',
                                       image=copy_icon, width=25,
                                       command=copy_password)
bt_copy_pass.place(x=305, y=150)


app.mainloop()
