# Importing modules
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib import database as db
from lib.crypting import Crypting
import lib.main_menu as main_menu
from lib.theme_engine import ThemeEngine


class LoginWindow(ttk.Frame, ThemeEngine):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # Initializing Theme Engine
        ThemeEngine.__init__(self)
        self.master = master
        
        # Setting Window Width and height        
        win_width, win_height = 700, 330
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (win_width/2))
        y_cordinate = int((screen_height/2) - (win_height/2)) - 15
        master.geometry("{}x{}+{}+{}".format(win_width, win_height,
                        x_cordinate, y_cordinate))
        master.resizable(0,0)       # Disabling resize
        # Setting Window Title
        master.title("Inventory Management System/ Login")
        # Adding icon to title menu
        master.iconbitmap("images/login_title_icon.ico")
        
        #===============  Background Frame / Master Frame ===============
        
        self.bg_frame = ttk.Frame(master, width=win_width, height=win_height)
        self.bg_frame.place(x=0,y=0)
        
        # Adding Title
        title = ttk.Label(self.bg_frame, text="USER LOGIN",
                          font="Arial 40 bold", foreground='#22d3fe')
        title.place(x=0,y=17, relx=0.3)

        # Adding Login logo in the Frame
        self.login_logo = tk.PhotoImage(file='images/login_logo.png')
        logo_label = ttk.Label(self.bg_frame, image=self.login_logo)
        logo_label.place(x=25,y=0, relheight=1)
        
        # Adding Username and Pasword's Entries 
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        # Username
        username_label = ttk.Label(self.bg_frame, text="Username",
                                    font="Arial 20 bold")
        username_label.place(x=225,y=120)
        self.username_entry = tk.Entry(self.bg_frame, textvariable=self.username,
                                        font="Arial 16 bold", bd=0,
                                         bg=self.entry_bg, fg=self.entry_fg)
        self.username_entry.place(x=400, y=120)
        self.username_entry.focus()
        # Adding line below entry widget to look modern
        line_label = tk.Label(self.bg_frame, text=("_")*(44), bg=self.entry_bg,
                             fg=self.entry_fg, bd=0)
        line_label.place(x=400, y=145)
        line_label.bind("<Button-1>", lambda e: self.username_entry.focus_set())
        # Password
        password_label = ttk.Label(self.bg_frame, text="Password",
                                     font="Arial 20 bold")
        password_label.place(x=225,y=190)
        self.password_entry = tk.Entry(self.bg_frame, textvariable=self.password,
                                    show="*", font="Arial 16 bold", bd=0,
                                    bg=self.entry_bg, fg=self.entry_fg)
        self.password_entry.place(x=400, y=190)
        # Adding line below entry widget to look modern
        line_label = tk.Label(self.bg_frame, text=("_")*(44),
                             bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label.place(x=400, y=215)
        line_label.bind("<Button-1>", lambda e: self.password_entry.focus_set())

        # Submit Button
        self.login_btn_img = tk.PhotoImage(file = r"images/login_button.png")
        self.login_button = tk.Button(self.bg_frame, image=self.login_btn_img,
                                     bg=self.button_bg, activebackground=self.button_bg,
                                     bd=0, command=self.validating_login)
        self.login_button.place(x=440, y=255)

        # Binding keys to entry widgets
        self.username_entry.bind("<Return>", self.validating_login)
        self.password_entry.bind("<Return>", self.validating_login)
        self.username_entry.bind("<Escape>", lambda e: e.widget.quit())
        self.password_entry.bind("<Escape>", lambda e: e.widget.quit())
        

    def validating_login(self, *args):
        db_obj = db.Database()
        # Decrypting the encrypted username & password fetched from database
        decrypted_username = Crypting.Decrypt(db_obj.get_login_data()[1])
        decrypted_password = Crypting.Decrypt(db_obj.get_login_data()[2])

        # Empty condition
        if self.username.get() == "" or self.password.get() == "":
            tk.messagebox.showwarning("Warning", "All fields are required")
        # Correct combination   '\' below is used to continue statement in the next line
        elif self.username.get() == decrypted_username and \
            self.password.get() == decrypted_password:
            tk.messagebox.showinfo("Successful", f"Welcome {self.username.get()}")
            self.master.switch_frame(main_menu.MainMenuWindow, self.bg_frame)
        # Incorrect condition
        else:
            tk.messagebox.showerror("Error", "Invalid username or password")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')


if __name__ == "__main__":
    master = tk.Tk()
    frame = LoginWindow(master)
    master.mainloop()