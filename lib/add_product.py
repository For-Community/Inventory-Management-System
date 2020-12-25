# Importing Modules
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox 
import time
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib import database as db
from lib.theme_engine import ThemeEngine


class AddProductTopWindow(ThemeEngine):
    """ Adds New Product to the Database
        Keyword arguments:
        master -- master Level window
    """
    def __init__(self, master):
        # Initializing Theme Engine
        ThemeEngine.__init__(self)

        self.master = master
        # Creating Top-level window & Setting Window Width and height        
        self.add_prod_win = tk.Toplevel(master)
        win_width, win_height = 1280, 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = int((screen_width/2) - (win_width/2))  - 7
        y = int((screen_height/2) - (win_height/2)) - 35
        self.add_prod_win.geometry(f'{win_width}x{win_height}+{x}+{y}')
        self.add_prod_win.resizable(0,0) # Disabling resize
        # Forcing Top-level window to stay on Top
        self.add_prod_win.attributes('-topmost', 'true')
        # Setting Top Level Window Title
        self.add_prod_win.title("Inventory Management System\ Inventory \ Add Product")

        #============= Add Products Window Background Body Frame ==============#
        
        apw_bg_frame = ttk.Frame(self.add_prod_win, width=win_width,
                                 height=win_height, style="mainframe.TFrame")
        apw_bg_frame.place(x=0, y=0)

        #===================== Title Frame / TOP Frame ========================#

        title_frame = ttk.Frame(apw_bg_frame)
        title_frame.place(x=20, y=20, relwidth=0.97)
        # Title Label
        title_label = ttk.Label(title_frame, text="ADD PRODUCT",
                                 font="Arial 60 bold", foreground='#22d3fe')
        title_label.pack()
        # Date and Time Label
        date_string = time.strftime("%a,%d/%b/%y")
        time_string = time.strftime("%I:%M %p")
        date_label = ttk.Label(title_frame, text=date_string, font="Arial 18 bold")
        date_label.place(x=1030, y=15)
        time_label = ttk.Label(title_frame, text=time_string, font="Arial 18 bold")
        time_label.place(x=1060, y=50)

        #==================  Add Products Frame / Middle Frame 1  =============#

        apw_frame1 = ttk.Frame(apw_bg_frame, border=1)
        apw_frame1.place(x=20, y=135, width=930, height=445)

        # New Product Name
        nprod_name_label = ttk.Label(apw_frame1, text="Product Name", font="Arial 17 bold")
        nprod_name_label.place(x=70, y=40)

        self.nprod_name_entry = tk.Entry(apw_frame1, font="Arial 20", width=52,
                                        bd=0, bg=self.entry_bg, fg=self.entry_fg)
        self.nprod_name_entry.place(x=70, y=80)
        # Binding keyrelease to check whether the entry is blank or not
        self.nprod_name_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding line below entry widget to look modern
        line_label_full = tk.Label(apw_frame1, text=("_")*(156),
                                 bd=0, bg=self.entry_bg, fg=self.entry_fg)
        line_label_full.place(x=70, y=115)
        # Binding Line label to focus on entry widget
        line_label_full.bind("<Button-1>", lambda e: self.nprod_name_entry.focus_set())

        # New Product :  Category Name
        nprod_catname_label = ttk.Label(apw_frame1, text="Category Name", font="Arial 17 bold")
        nprod_catname_label.place(x=70, y=170)

        self.nprod_catname_entry = tk.Entry(apw_frame1, font="Arial 20", width=23,
                                            bd=0, bg=self.entry_bg, fg=self.entry_fg)
        self.nprod_catname_entry.place(x=70, y=210)
        # Binding keyrelease to check whether the entry is blank or not
        self.nprod_catname_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding line below entry widget to look modern
        line_label_half = tk.Label(apw_frame1, text=("_")*(69),
                                 bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=70, y=245)
        # Binding Line label to focus on entry widget
        line_label_half.bind("<Button-1>", lambda e: self.nprod_catname_entry.focus_set())

        # New Product : Sub Category Name
        nprod_subcatname_label = ttk.Label(apw_frame1, text="Sub-Category Name", font="Arial 17 bold")
        nprod_subcatname_label.place(x=505, y=170)

        self.nprod_subcatname_entry = tk.Entry(apw_frame1, font=('Arial',20), width=23,
                                                bd=0, bg=self.entry_bg, fg=self.entry_fg)
        self.nprod_subcatname_entry.place(x=505, y=210)
        # Binding keyrelease to check whether the entry is blank or not
        self.nprod_subcatname_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding line below entry widget to look modern
        line_label_half = tk.Label(apw_frame1, text=("_")*(69),
                                bd=0, bg=self.entry_bg, fg=self.entry_fg)
        line_label_half.place(x=505, y=245)
        # Binding Line label to focus on entry widget
        line_label_half.bind("<Button-1>", lambda e: self.nprod_subcatname_entry.focus_set())

        # New Product : Unit Price
        nprod_price_label = ttk.Label(apw_frame1, text="Unit Price", font="Arial 17 bold")
        nprod_price_label.place(x=70, y=300)

        self.nprod_price_entry = tk.Entry(apw_frame1, font="Arial 20", width=23,
                                        bd=0, bg=self.entry_bg, fg=self.entry_fg)
        self.nprod_price_entry.place(x=70, y=340)
        # Binding keyrelease to check whether the entry is blank/float or not
        self.nprod_price_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding line below entry widget to look modern
        line_label_half = tk.Label(apw_frame1, text=("_")*(69),
                                 bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=70, y=375)
        # Binding Line label to focus on entry widget
        line_label_half.bind("<Button-1>", lambda e: self.nprod_price_entry.focus_set())

        # New Product : Quantity
        nprod_qty_label = ttk.Label(apw_frame1, text="Quantity", font="Arial 17 bold")
        nprod_qty_label.place(x=505, y=300)

        self.nprod_qty_entry = tk.Entry(apw_frame1, font=('Arial',20), width=23,
                                         bg=self.entry_bg, fg=self.entry_fg, bd=0)
        self.nprod_qty_entry.place(x=505, y=340)
        # Binding keyrelease to check whether the entry is blank/integer or not
        self.nprod_qty_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding line below entry widget to look modern
        line_label_half = tk.Label(apw_frame1, text=("_")*(69),
                                     bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=505, y=375)
        # Binding Line label to focus on entry widget
        line_label_half.bind("<Button-1>", lambda e: self.nprod_qty_entry.focus_set())


        #===================  Menu Frame / Middle Frame 2  ====================#

        apw_frame2 = ttk.Frame(apw_bg_frame, border=1)
        apw_frame2.place(x=970, y=135, width=292, height=445)

        # Menu Heading Label
        heading_label = ttk.Label(apw_frame2, text="Menu", font="Arial 30 bold",
                                 foreground='#4eacfe')
        heading_label.pack(pady=15)

        # Add New Product Button
        self.addprod_btn_img = tk.PhotoImage(file='images/addprod_button.png')
        self.addprod_btn = tk.Button(apw_frame2, image=self.addprod_btn_img, bd=0,
                             bg=self.button_bg, activebackground=self.button_bg,
                            state='disabled', command=self.add_to_db)
        self.addprod_btn.place(x=47, y=100)

        # Clear All Entries Button
        self.clear_btn_img = tk.PhotoImage(file='images/clear_button.png')
        clear_btn = tk.Button(apw_frame2, image=self.clear_btn_img, bd=0,
                             bg=self.button_bg, activebackground=self.button_bg,
                            command=lambda : [self.nprod_name_entry.delete(0, 'end'),
                                            self.nprod_catname_entry.delete(0, 'end'),
                                            self.nprod_subcatname_entry.delete(0, 'end'),
                                            self.nprod_price_entry.delete(0, 'end'),
                                            self.nprod_qty_entry.delete(0, 'end')])
        clear_btn.place(x=47, y=270)

    ##============================ Other METHODS ===========================================##
    
    def secure_entries(self, *args):
        """ Checks Whether Product : Name, Cat, Sub-Cat, Price & Quantity are -
            (1) not Empty.  (2) Price is Float.  (3) Quantity is Integer.
            If all Condition matches Add Product button enables.
        """
        self.fetch_name = self.nprod_name_entry.get().strip()
        self.fetch_catname = self.nprod_catname_entry.get().strip()
        self.fetch_subcatname = self.nprod_subcatname_entry.get().strip()
        self.fetch_price = self.nprod_price_entry.get()
        self.fetch_qty = self.nprod_qty_entry.get()
        
        # Float only for price
        if not self.fetch_price == "":
            try:
                self.fetch_price = float(self.fetch_price)
            except ValueError as e:
                # Pop up message showing warning to write only decimals/floats
                tk.messagebox.showwarning("Warning", "Only Enter Floats",
                                            parent=self.add_prod_win)
                # If not decimal/ float price entry box  will be reset
                self.nprod_price_entry.delete(0,'end')
        
        # Int only for quantity
        if not self.fetch_qty == "":
            try:
                self.fetch_qty = int(self.fetch_qty)
            except ValueError as e:
                # Pop up message showing warning to write only integers
                tk.messagebox.showwarning("Warning", "Only  Enter Integers", parent=self.add_prod_win)
                # If not integer quantity entry box  will be reset
                self.nprod_qty_entry.delete(0,'end')

        # If all entries all filled Add Product button will enable else not
        if (self.fetch_name != "" and self.fetch_catname != "" and 
                    self.fetch_subcatname != "" and 
                    self.nprod_price_entry.get() != "" and 
                    self.nprod_qty_entry.get() != ""):
            # Enabling Add Product Button
            self.addprod_btn.config(state='normal')
        else:
            # Add Product Button stays disabled
            self.addprod_btn.config(state='disabled')


    def add_to_db(self):
        """Checks : (1) Cat already exists in the database or not.
        (2) Sub-Cat already exist or not. 
        (3) Product Name already exist or not.
        If All 3 exists everything is skipped.
        If All 3 doesn't exist new entry is added to database. 
        If Cat and Sub-cat exists write to database is of cat, sub-cat is skipped
        If Prod Name exist and new Cat, Sub-cat data is written to db,
                                         both entry is deleted from db
        
        Entry in the following order : Category -> Sub-Category ->Product Tables
                                        to match Foreign Key Policy
        
        """
        db_obj = db.Database()

        def insert_success_msg():
            # Deleting all entries from Top level/ Add Product window
            self.nprod_name_entry.delete(0, 'end')
            self.nprod_catname_entry.delete(0, 'end')
            self.nprod_subcatname_entry.delete(0, 'end')
            self.nprod_price_entry.delete(0, 'end')
            self.nprod_qty_entry.delete(0, 'end')

            # Showing success message as pop-up
            tk.messagebox.showinfo("Successful",
                                    f"\"{self.fetch_name}\" added to database",
                                     parent=self.add_prod_win)
            try:
                # Deleting master/ inventory windows search entry box 
                # Instant update of added product to Inventory Window Product List
                self.master.prod_search_entry.delete(0,'end')
                self.master.search_product()
            except:
                pass
       
       
       # INSERTING to CATEGORY SUB-CATEGORY PRODUCT TABLES in DATABASE
        try:
            db_obj.insert_category(cat_name=self.fetch_catname)
            # print("1")
            db_obj.insert_sub_category(sub_cat_name=self.fetch_subcatname,
                                         cat_name=self.fetch_catname)
            # print("2")
            db_obj.insert_product(prod_name=self.fetch_name,
                                 prod_price=self.fetch_price,
                                prod_quantity=self.fetch_qty,
                                sub_cat_name=self.fetch_subcatname,
                                cat_name=self.fetch_catname)
            # Cat Sub-Cat and Product doesnt exist and everything succesfull written to db
            insert_success_msg()
        # Exception to handle Foreign Key error if the Entry exist in the Cat, Sub-Cat or product table
        except Exception as e:
            # CATEGORY exists condition => Skip cat and try sub-cat, prod entries
            if "UNIQUE constraint failed: category.cat_name" in e.args[0]:
                # print(e.args[0]," <= CATEGORY EXISTS")
                try:
                    # New Entry for Sub-Category and Product Table
                    db_obj.insert_sub_category(sub_cat_name=self.fetch_subcatname,
                                                cat_name=self.fetch_catname)
                    # print("2.1")
                    db_obj.insert_product(prod_name=self.fetch_name,
                                        prod_price=self.fetch_price,
                                        prod_quantity=self.fetch_qty,
                                        sub_cat_name=self.fetch_subcatname,
                                        cat_name=self.fetch_catname)
                    # print("2.3")
                    insert_success_msg()
                except Exception as e:
                    # Category and Subcategory exists condition => skip both and try product entry
                    if "UNIQUE constraint failed: sub_category.sub_cat_name" in e.args[0]:
                        # print("Sub cat also exist")
                        try:
                            db_obj.insert_product(prod_name=self.fetch_name,
                                                prod_price=self.fetch_price,
                                                prod_quantity=self.fetch_qty,
                                                sub_cat_name=self.fetch_subcatname,
                                                cat_name=self.fetch_catname)

                            insert_success_msg()
                        except Exception as e:
                            # print(e)
                            # Everything exists => skip all-3 entry
                            if "UNIQUE constraint failed: product.prod_name" in e.args[0]:
                                # Pop-up warning : Everything exists 
                                tk.messagebox.showwarning("Warning",
                                                    f"\"{self.fetch_name}\" already exist in the database",
                                                     parent=self.add_prod_win)
                                self.nprod_name_entry.delete(0, 'end')
                                # print("everything exists so nothing happened")
                    # Cat and product exists, Sub-category doesnt exist so deleting sub category from db
                    elif "UNIQUE constraint failed: product.prod_name" in e.args[0]:
                        db_obj.delete_sub_category(self.fetch_subcatname)
                        tk.messagebox.showwarning("Warning",
                                                    f"\"{self.fetch_name}\" already exist in the database",
                                                     parent=self.add_prod_win)
                        self.nprod_name_entry.delete(0, 'end')
                        # print("SUB dont exist but product does")
                        # print("delete sub category")

            # SUB-CATEGORY exists condition => cat entered and try prod entries
            elif "UNIQUE constraint failed: sub_category.sub_cat_name" in e.args[0]:
                # print(e.args[0]," <= SUB-CATEGORY EXISTS")
                try:
                    db_obj.insert_product(prod_name=self.fetch_name,
                                        prod_price=self.fetch_price,
                                        prod_quantity=self.fetch_qty,
                                        sub_cat_name=self.fetch_subcatname,
                                        cat_name=self.fetch_catname)

                    insert_success_msg()
                # Sub-cat, Product exists so delete entered new category
                except Exception as e:
                    # print(e)
                    if "UNIQUE constraint failed: product.prod_name" in e.args[0]:
                        tk.messagebox.showwarning("Warning",
                                                 f"\"{self.fetch_name}\" already exist in the database",
                                                  parent=self.add_prod_win)
                        self.nprod_name_entry.delete(0, 'end')
                        # print("prod exists")
                        # print("deleting cat")
                        db_obj.delete_category(self.fetch_catname)
            # CATEGORY added, SUB-CATEGORY added but PRODUCT exists so delete newly added Cat Sub-Cat entries
            elif "UNIQUE constraint failed: product.prod_name" in e.args[0]:
                # print(e.args[0]," <= PRODUCT EXISTS")
                db_obj.delete_sub_category(self.fetch_subcatname)
                db_obj.delete_category(self.fetch_catname)
                # print("Delete SUB-Category")
                # print("Delete Category")
                tk.messagebox.showwarning("Warning",
                                        f"\"{self.fetch_name}\" already exist in the database",
                                        parent=self.add_prod_win)
                self.nprod_name_entry.delete(0, 'end')
            # If Out of the box error occurs
            else:
                pass
                # print(e)



if __name__ == "__main__":
    master = tk.Tk()
    master.attributes('-topmost', 'true')
    win_obj = AddProductTopWindow(master)    
    master.mainloop()
