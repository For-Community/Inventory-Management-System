# importing modules
import tkinter as tk
import tkinter.ttk as ttk
import time
import os
import sys
# print(sys.path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.sales import *
from lib.inventory import *
from lib.login_system import LoginWindow
from lib.extras import *
# import lib.theme_engine


class MainMenuWindow(ttk.Frame, ThemeEngine):
    """ Main Menu for Inventory Management System"""
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # Initializing Theme Engine
        ThemeEngine.__init__(self)

        # Setting Window Width and height        
        win_width, win_height = 1340, 680
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (win_width/2))-5
        y_cordinate = int((screen_height/2) - (win_height/2)) - 15
        # print(x_cordinate, y_cordinate)
        master.geometry("{}x{}+{}+{}".format(win_width, win_height,
                                             x_cordinate, y_cordinate))
        master.resizable(0,0) # Disabling resize
        # Setting Window Title
        master.title("Inventory Management System")
        # Adding icon to title menu
        master.iconbitmap("images/stock_title_icon.ico")

        #======================== Background Frame / Master Frame ===============

        bg_frame = ttk.Frame(master, width=win_width, height=win_height,
                             style="mainframe.TFrame")
        bg_frame.place(x=0, y=0)

        #========================  Title Frame  =============================== #

        title_frame = ttk.Frame(bg_frame)
        title_frame.place(x=20, y=20, relwidth=0.97)
        # Back Button
        self.logout_btn_img = tk.PhotoImage(file='images/logout_button.png')
        logout_btn = tk.Button(title_frame, image=self.logout_btn_img, bd=0,
                            bg=self.button_bg, activebackground=self.button_bg,
                        command=lambda: master.switch_frame(LoginWindow, bg_frame))
        logout_btn.place(relwidth=0.155, relheight=1)
        # Title Label
        title_label = ttk.Label(title_frame, text="MAIN MENU",
                                 font="Arial 60 bold", foreground='#22d3fe')
        title_label.pack()
        # Date and Time Label
        date_string = time.strftime("%a,%d/%b/%y")
        time_string = time.strftime("%I:%M %p")
        date_label = ttk.Label(title_frame, text=date_string, font="Arial 18 bold")
        date_label.place(x=1090, y=15)
        time_label = ttk.Label(title_frame, text=time_string, font="Arial 18 bold")
        time_label.place(x=1115, y=50)
        
        #======================== Body Frame ===========================#

        body_frame = ttk.Frame(bg_frame)
        body_frame.place(x=20, y=140, relwidth=0.97, relheight=0.765)

        # Program Title
        program_title_label = ttk.Label(body_frame, text="INVENTORY MANAGEMENT SYSTEM",
                                     font="Arial 45 bold", foreground='#4eacfe')
        program_title_label.place(x=110, y=40)

        # Sales Button
        self.sales_btn_img = tk.PhotoImage(file = r"images/sales_button.png")
        sales_button = tk.Button(body_frame, text="Sales", image=self.sales_btn_img,
                                 bd=0, bg=self.button_bg, activebackground=self.button_bg,
                        command=lambda: master.switch_frame(SalesWindow, bg_frame))
        sales_button.grid(row=0, column=0, padx=(80,0), pady=200)

        # Inventory Button
        self.inventory_btn_img = tk.PhotoImage(file = r"images/inventory_button.png")
        inventory_button = tk.Button(body_frame , text="Inventory", image=self.inventory_btn_img,
                                 bd=0, bg=self.button_bg, activebackground=self.button_bg,
                        command=lambda: master.switch_frame(InventoryWindow, bg_frame))
        inventory_button.grid(row=0, column=1, padx=(60,30))

        # Extras Button
        self.extras_btn_img = tk.PhotoImage(file = r"images/extras_button.png")
        extras_button = tk.Button(body_frame , text="Extras", image=self.extras_btn_img,
                                 bd=0, bg=self.button_bg, activebackground=self.button_bg,
                        command=lambda: master.switch_frame(ExtrasWindow, bg_frame))
        extras_button.grid(row=0, column=2, padx=30)

        # Exit button
        self.exit_btn_img = tk.PhotoImage(file = r"images/exit_button.png")
        exit_button = tk.Button(body_frame , text="Exit", image=self.exit_btn_img,
                                 bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                command=master.quit)
        exit_button.grid(row=0, column=3, padx=30)



if __name__ == "__main__":
    master = tk.Tk()
    frame = MainMenuWindow(master).pack()
    master.mainloop()