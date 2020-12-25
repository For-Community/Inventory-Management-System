# importing modules
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import time
import os
import sys
# print(sys.path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lib.main_menu as main_menu
from lib import database as db
from lib.crypting import Crypting
from lib.theme_engine import ThemeEngine


class ExtrasWindow(ttk.Frame, ThemeEngine):
    """Settings / Extras Page"""
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # Initializing Theme Engine
        ThemeEngine.__init__(self)

        self.master = master
        # Setting Window Title
        master.title("Inventory Management System\ Extras")
        # Connecting to Database
        self.db_obj = db_obj = db.Database()   
        
        #=========================  Main Background Frame =====================#
        
        win_width, win_height = 1340, 680
        self.bg_frame = ttk.Frame(master, width=win_width, height=win_height,
                                 style="mainframe.TFrame")
        self.bg_frame.place(x=0, y=0)

        #========================  Title Frame  ===============================#

        title_frame = ttk.Frame(self.bg_frame)
        title_frame.place(x=20, y=20, relwidth=0.97)
        # Back Button
        self.back_btn_img = tk.PhotoImage(file='images/back_button.png')
        back_btn = tk.Button(title_frame, image=self.back_btn_img, bd=0,
                             bg=self.button_bg, activebackground=self.button_bg,
                            command=lambda: master.switch_frame(main_menu.MainMenuWindow, self.bg_frame))
        back_btn.place(relwidth=0.15, relheight=1)
        # Title Label
        title_label = ttk.Label(title_frame, text="EXTRAS", font="Arial 60 bold",
                                 foreground='#22d3fe')
        title_label.pack()
        # Date and Time Label
        date_string = time.strftime("%a,%d/%b/%y")
        time_string = time.strftime("%I:%M %p")
        date_label = ttk.Label(title_frame, text=date_string, font="Arial 18 bold")
        date_label.place(x=1090, y=15)
        time_label = ttk.Label(title_frame, text=time_string, font="Arial 18 bold")
        time_label.place(x=1115, y=50)

        #===============  Password Frame / Left Frame 1 =======================#

        ch_pass_frame = ttk.Frame(self.bg_frame, border=1)
        ch_pass_frame.place(x=20, y=135, width=930, height=300)
        
        # Heading Label
        heading_label = ttk.Label(ch_pass_frame, text="CHANGE PASSWORD",
                                 font="Arial 20 bold", foreground='#4eacfe')
        heading_label.pack(side='top', pady=25)
        # Current Password
        current_password_label = ttk.Label(ch_pass_frame, text="Current Password",
                                            font="Arial 17 bold")
        current_password_label.place(x=90, y=100) #
        self.current_password_entry = tk.Entry(ch_pass_frame, font="Arial 17 bold", show="*",
                                             width=23, bg=self.entry_bg, fg=self.entry_fg, bd=0)
        self.current_password_entry.place(x=90,y=150)
        # Adding line below entry widget to look modern
        line_label_half = tk.Label(ch_pass_frame, text=("_")*(61),
                                    bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=89, y=180)
        # Binding Line label to focus on entry widget
        line_label_half.bind("<Button-1>", lambda e: self.current_password_entry.focus_set())

        # New Password
        new_password_label = ttk.Label(ch_pass_frame, text="New Password",
                                         font="Arial 17 bold")
        new_password_label.place(x=530, y=100)
        self.new_password_entry = tk.Entry(ch_pass_frame, show="*", font="Arial 17 bold",
                                         bg=self.entry_bg, fg=self.entry_fg, bd=0, width=23)
        self.new_password_entry.place(x=530, y=150)
        # Adding line below entry widget to look modern
        line_label_half = tk.Label(ch_pass_frame, text=("_")*(61),
                                     bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=529, y=180)
        # Binding Line label to focus on entry widget
        line_label_half.bind("<Button-1>", lambda e: self.new_password_entry.focus_set())
        # Change Password Button
        self.changepass_btn_img = tk.PhotoImage(file='images/changepass_btn.png')
        self.change_password_button = tk.Button(ch_pass_frame , image=self.changepass_btn_img,
                                                bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                                command=self.change_password)
        self.change_password_button.pack(side='bottom', pady=30)


        #===============  THEME Frame / Right Frame 1  ======================

        theme_frame = ttk.Frame(self.bg_frame, border=1)
        theme_frame.place(x=970, y=135, width=350, height=300)
        
        heading_label = ttk.Label(theme_frame, text="CHANGE THEME",
                                 font="Arial 20 bold", foreground='#4eacfe')
        heading_label.pack(side='top', pady=25)
        
        # Fetching theme value from db
        theme_value = db_obj.get_theme_value()[1]
        # print(theme_value)
        
        # If theme value fetched from is dark mode
        # then set button for dark theme implementation and vice-versa
        if theme_value == "Light Mode":
            theme_button_value = "Dark Mode"
            self.theme_btn_img = tk.PhotoImage(file='images/dark_theme.png')
            # print(theme_button_value)
        else:
            theme_button_value = "Light Mode"
            self.theme_btn_img = tk.PhotoImage(file='images/light_theme.png')
            # print(theme_button_value)
        
        self.change_theme_button = tk.Button(theme_frame, text=theme_button_value,
                                         image=self.theme_btn_img, bd=0 ,
                                         bg=self.button_bg, activebackground=self.button_bg,
                                        command=self.change_theme)
        self.change_theme_button.pack()

        # #===============  Extra Frame 1 / Left Frame 2  ======================
        
        # extra_frame1 = ttk.Frame(self.bg_frame, border=1)
        # extra_frame1.place(x=20, y=455, width=930, height=205)
    

        # #===============  Extra Frame 2 / Right Frame 2  ======================
        
        # extra_frame2 = ttk.Frame(self.bg_frame, border=1)
        # extra_frame2.place(x=970, y=455, width=350, height=205)

    
    #======================  OTHER METHODS ==========================================#

    def change_theme(self):
        """ Fetch Theme value from button text.
            Two Theme Modes : Dark Mode & Light Mode
            Destroys Current Frame and recreate it
            to Fetch fresh buttonbg, self.entry_bg, self.entry_fg
        """
        # Current Theme = Dark
        if self.change_theme_button["text"] == "Light Mode":
            # Changing Theme value in the Db
            self.db_obj.change_theme("Light Mode")
            # Destroying current bg_frame and all widget with it
            self.bg_frame.destroy()
            # Recreating bg_frame and all widgets with it implementing Light theme
            self.__init__(self.master)
            # print("Light Mode activated")

        # Current Theme = Light
        elif self.change_theme_button["text"] == "Dark Mode":
            # Changing Theme value in the Db
            self.db_obj.change_theme("Dark Mode")
            # Destroying current bg_frame and all widget with it
            self.bg_frame.destroy()
            # Recreating bg_frame and all widgets with it implementing Dark theme
            self.__init__(self.master)
            # print("Dark Mode activated")
    
    def change_password(self):
        """ Fetches Current pass from Database and decrypts it to Verify 
            Encrypts and Changes Login Password in the Database
        """
        # Fetching new and current box entries
        new_password_fetch = self.new_password_entry.get().replace(" ","")
        current_password_fetch = self.current_password_entry.get()
        # Decrypting password
        decrypted_password = Crypting.Decrypt(self.db_obj.get_login_data()[2])

        if new_password_fetch != "":
            if current_password_fetch == decrypted_password:
                if current_password_fetch == new_password_fetch:
                    tk.messagebox.showwarning("Warning", "Current password Same as New Password")
                    self.new_password_entry.delete(0, 'end')
                else:
                    new_password = Crypting.Encrypt(new_password_fetch)
                    self.db_obj.change_password(new_password)
                    tk.messagebox.showinfo("Successful", "Succesfully Changed Password")
                    self.current_password_entry.delete(0, 'end')
                    self.new_password_entry.delete(0, 'end')
            else:
                tk.messagebox.showerror("Error", "Current Password is Incorrect")
                self.current_password_entry.delete(0, 'end')
                # self.new_password_entry.delete(0, 'end')
        else:
            tk.messagebox.showerror("Error", "New Password Cannot Be Empty!")

                                

if __name__ == "__main__":
    master = tk.Tk()
    # Setting Window Width and height        
    win_width, win_height = 1340, 680
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = int((screen_width/2) - (win_width/2))
    y = int((screen_height/2) - (win_height/2)) - 15
    master.geometry(f'{win_width}x{win_height}+{x}+{y}')
    master.resizable(0,0) # Disabling resize
    
    frame = ExtrasWindow(master).pack()
    master.mainloop()