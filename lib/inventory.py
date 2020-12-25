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
from lib.theme_engine import ThemeEngine
from lib.add_product import AddProductTopWindow


class InventoryWindow(tk.Frame, ThemeEngine):
    """Inventory Window to Update or Delete Inventories and to add New product"""
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Initializing Theme Engine
        ThemeEngine.__init__(self)
        
        self.db_obj = db.Database()

        #===== Main Background Frame / Master Frame ===============

        win_width, win_height = 1340, 680
        bg_frame = ttk.Frame(master, width=win_width, height=win_height,
                             style="mainframe.TFrame")
        bg_frame.place(x=0, y=0)
        
        
        #========================  Title Frame  ==========================

        title_frame = ttk.Frame(bg_frame)
        title_frame.place(x=20, y=20, relwidth=0.97)
        # Back Button
        self.back_btn_img = tk.PhotoImage(file='images/back_button.png')
        back_btn = tk.Button(title_frame, image=self.back_btn_img, bd=0,
                            bg=self.button_bg, activebackground=self.button_bg,
                            command=lambda: master.switch_frame(main_menu.MainMenuWindow, bg_frame))
        back_btn.pack(side="left", padx=50)
        # Title Label
        title_label = ttk.Label(title_frame, text="INVENTORY ",
                                font="Arial 60 bold", foreground='#22d3fe')
        title_label.pack(side="left", padx=240)
        # Time Label
        date_string = time.strftime("%a,%d/%b/%y")
        time_string = time.strftime("%I:%M %p")
        date_label = ttk.Label(title_frame, text=date_string, font="Arial 18 bold")
        date_label.place(x=1030, y=15)
        time_label = ttk.Label(title_frame, text=time_string, font="Arial 18 bold")
        time_label.place(x=1060, y=50)


        #===============  Product List Frame / Left Frame  ======================
        
        product_list_frame = ttk.Frame(bg_frame, border=1)
        product_list_frame.place(x=20, y=135, width=930, height=525)
        
        # Heading Label
        heading_label = ttk.Label(product_list_frame, text="Product List",
                                 font="Arial 20 bold", foreground='#4eacfe', justify='left')
        heading_label.grid(row=0, column=0, padx=30, pady=15)

        # Product list Treeview
        self.product_list_treeview = ttk.Treeview(product_list_frame,
                                     columns=('zero',"one","two","three","four","five","six"),
                                      selectmode ='browse', show='headings')
        self.product_list_treeview.grid(row=1,column=0, padx=(25,0), ipady=65)

        self.product_list_treeview.heading('zero', text='No')
        self.product_list_treeview.column('zero', minwidth=60, width=60,
                                             anchor="c", stretch=False)

        self.product_list_treeview.heading('one', text='Product Name')
        self.product_list_treeview.column('one', minwidth=255, width=255,
                                             anchor="c", stretch=False)

        self.product_list_treeview.heading('two', text='Category')
        self.product_list_treeview.column('two', minwidth=150, width=150,
                                             anchor="c", stretch=False)

        self.product_list_treeview.heading('three', text='Sub-Category')
        self.product_list_treeview.column('three', minwidth=150, width=150,
                                             anchor="c", stretch=False)

        self.product_list_treeview.heading('four', text='Quantity')
        self.product_list_treeview.column('four', minwidth=80, width=80,
                                             anchor="c", stretch=False)

        self.product_list_treeview.heading('five', text='Unit Price')
        self.product_list_treeview.column('five', minwidth=82, width=82,
                                             anchor="c", stretch=False)
        
        self.product_list_treeview.heading('six', text='Total Price')
        self.product_list_treeview.column('six', minwidth=83, width=83,
                                             anchor="c", stretch=False)

        # Adding Vertical Scrollbar
        verscrlbar = ttk.Scrollbar(product_list_frame, orient ="vertical",
                                     command = self.product_list_treeview.yview)
        verscrlbar.grid(row=1, column=5, ipady=152)
        self.product_list_treeview.configure(yscrollcommand = verscrlbar.set)
        # Adding Horizontal Scrollbar
        horscrlbar = ttk.Scrollbar(product_list_frame, orient ="horizontal",
                                     command = self.product_list_treeview.xview)
        horscrlbar.grid(row=3, column=0, padx=(25,0), ipadx=405)
        self.product_list_treeview.configure(xscrollcommand=horscrlbar.set)


        # Product Name Search
        prod_name_label = ttk.Label(product_list_frame, text="Product Name",
                                     font="Arial 16 bold")
        prod_name_label.place(x=55, y=470)
        self.prod_search_entry = tk.Entry(product_list_frame, font="Arial 16",
                                         bg=self.entry_bg, fg=self.entry_fg, width=48, bd=0)
        self.prod_search_entry.place(x=230,y=470)
        # Binding Enter Key to Search Product
        self.prod_search_entry.bind("<Return>", self.search_product)
        # Adding line below entry widget to look modern
        line_label_full = tk.Label(product_list_frame, text=("_")*(115),
                                    bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_full.place(x=230, y=495)
        # Binding Line-Label to Focus on Entry widget when clicked upon
        line_label_full.bind("<Button-1>", lambda e: self.prod_search_entry.focus_set())
        
        # Search Button
        self.search_btn_img = tk.PhotoImage(file='images/search.png')
        search_button = tk.Button(product_list_frame, image=self.search_btn_img, bd=0, bg=self.button_bg, activebackground=self.button_bg, command=self.search_product)
        search_button.place(x=835, y=470)


        # Filling Product List at start of inventory window
        self.search_product()
        
        
        #===============  ADD Prodct Frame / Middle Frame Right 1  ======================
        
        add_product_frame = ttk.Frame(bg_frame, border=1)
        add_product_frame.place(x=970, y=135, width=350, height=100)

        self.add_product_btn_img = tk.PhotoImage(file='images/addprod_btn.png')
        add_product_btn = tk.Button(add_product_frame, image=self.add_product_btn_img, bd=0,
                                     bg=self.button_bg, activebackground=self.button_bg,
                                    text="Add Product", font=("Arial", 20, "bold"),
                                     command=lambda : AddProductTopWindow(self))
        # add_product_btn.grid(row=0, column=0, padx=35, pady=13)        
        add_product_btn.place(relwidth=1, relheight=1)
        

        #===============  Menu Frame / Middle Frame Right 2  ======================

        product_menu_frame = ttk.Frame(bg_frame, border=1)
        product_menu_frame.place(x=970, y=255, width=350, height=405)

        # Heading Label
        heading_label = ttk.Label(product_menu_frame, text="Menu",
                                 font="Arial 20 bold", foreground='#4eacfe')
        heading_label.place(x=140, y=15)

        # Product Name
        selected_prod_name_label = ttk.Label(product_menu_frame,
                                        text="Product Name", font="Arial 16 bold")
        selected_prod_name_label.place(x=102, y=70)

        self.selected_prod_name_txt = tk.Text(product_menu_frame, font="Arial 12 bold",
                                            bg=self.entry_bg, fg=self.entry_fg, bd=0,
                                            height=2, width=33, state='disabled')
        self.selected_prod_name_txt.place(x=25, y=110)
        
        # Product Quantity
        selected_prod_qty_label = ttk.Label(product_menu_frame, text="Quantity",
                                             font="Arial 16 bold")
        selected_prod_qty_label.place(x=45, y=170)

        self.selected_prod_qty_entry = tk.Entry(product_menu_frame, font="Arial 16 bold",
                        bg=self.entry_bg, fg=self.entry_fg, readonlybackground=self.entry_bg,
                        bd=0, width=10, justify='center', state='readonly')
        self.selected_prod_qty_entry.place(x=35, y=210)
        # Binding Key release to Call Secure Function to allow only Integers
        self.selected_prod_qty_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding Line label to make entry widget look modern
        line_label_half = tk.Label(product_menu_frame, text=("_")*(25),
                                 bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=35, y=240)
        # Binding Line-Label to Focus on Entry widget when clicked upon
        line_label_half.bind("<Button-1>", lambda e: self.selected_prod_qty_entry.focus_set())

        # Product Price
        selected_prod_price_label = ttk.Label(product_menu_frame,
                                     text="Price(\u20B9)", font="Arial 16 bold")
        selected_prod_price_label.place(x=215, y=170)

        self.selected_prod_price_entry = tk.Entry(product_menu_frame, font="Arial 16 bold",
                            bg=self.entry_bg, fg=self.entry_fg, readonlybackground=self.entry_bg,
                            bd=0, width=10, justify='center', state='readonly')
        self.selected_prod_price_entry.place(x=200, y=210)
        # Adding Line label to make entry widget look modern
        self.selected_prod_price_entry.bind("<KeyRelease>", self.secure_entries)
        # Adding Line label to make entry widget look modern
        line_label_half = tk.Label(product_menu_frame, text=("_")*(25), bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label_half.place(x=200, y=240)
        # Binding Line-Label to Focus on Entry widget when clicked upon
        line_label_half.bind("<Button-1>", lambda e: self.selected_prod_price_entry.focus_set())

        # Function Buttons

        # Select Product from list
        self.select_product_img = tk.PhotoImage(file='images/selectprod_btn.png')
        select_product_btn = tk.Button(product_menu_frame, image=self.select_product_img,
                                     bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                    command=self.select_product)
        select_product_btn.place(x=37, y=290)
        
        # View All Products in the List 
        self.view_all_product_img = tk.PhotoImage(file='images/viewall_prod_btn.png')
        viewall_product_btn = tk.Button(product_menu_frame, image=self.view_all_product_img,
                             bd=0, bg=self.button_bg, activebackground=self.button_bg,
                            command=lambda : [self.prod_search_entry.delete(0,'end'), self.search_product()])
        viewall_product_btn.place(x=204, y=290)

        # Update Product values: Price and Quantity
        self.update_product_img = tk.PhotoImage(file='images/updateprod_btn.png')
        self.update_product_btn = tk.Button(product_menu_frame, image=self.update_product_img,
                                     bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                    state='disabled', command=self.update_product)
        self.update_product_btn.place(x=37, y=350)
        
        # Delete selected product from db
        self.delete_product_img = tk.PhotoImage(file='images/deleteprod_btn.png')
        delete_product_btn = tk.Button(product_menu_frame, image=self.delete_product_img,
                                     bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                      command=self.delete_product)
        delete_product_btn.place(x=204, y=350)


##============================== OTHER METHODS ===================================================##

    def search_product(self, *args):
        # Clear all
        self.product_list_treeview.delete(*self.product_list_treeview.get_children())
    
        self.search_word = self.prod_search_entry.get()
        data= self.db_obj.get_product_details('%'+self.search_word+'%')
        # print(data)
        for i in range(len(data)):
            temp = data[i]
            self.prod_name = temp[0]
            self.prod_price = temp[1]
            self.prod_qty = temp[2]
            self.prod_cat = temp[4]
            self.prod_sub_cat = temp[3]

            self.product_list_treeview.insert("", 'end'
            , values =(i+1, self.prod_name, self.prod_cat, self.prod_sub_cat, self.prod_qty, f"\u20B9 {self.prod_price}", f"\u20B9 {self.prod_price * self.prod_qty}"))  
    

    def select_product(self):
        try:
            # Getting current item from product list
            cur_item = self.product_list_treeview.focus()
    
            # Inserting Product Name
            selected_prod_name = self.product_list_treeview.item(cur_item)['values'][1]
            self.selected_prod_name_txt.config(state='normal')
            self.selected_prod_name_txt.delete(1.0, 'end')
            self.selected_prod_name_txt.insert('end', selected_prod_name)
            self.selected_prod_name_txt.config(state='disabled')
            
            # Inserting Product Quantity
            selected_prod_qty = self.product_list_treeview.item(cur_item)['values'][4]
            self.selected_prod_qty_entry.config(state='normal')
            self.selected_prod_qty_entry.delete(0, 'end')
            self.selected_prod_qty_entry.insert('end', selected_prod_qty)
            
            # Inserting Product Price
            selected_prod_price = self.product_list_treeview.item(cur_item)['values'][5]
            selected_prod_price = selected_prod_price.split("\u20B9")[1]
            self.selected_prod_price_entry.config(state='normal')
            self.selected_prod_price_entry.delete(0, 'end')
            self.selected_prod_price_entry.insert('end', selected_prod_price)

            # Enabling Update Product Button
            self.update_product_btn.config(state="normal")

            # print(selected_prod_name, selected_prod_qty, selected_prod_price)
        except IndexError:
            tk.messagebox.showwarning("Warning", "Select a product from Product List")


    def secure_entries(self, *args):
        """ Checks Whether Product : Price & Quantity are -
            (1) not Empty.  (2) Price is Float.  (3) Quantity is Integer.
            If all Condition matches Update Product button enables.
        """
        self.fetch_qty = self.selected_prod_qty_entry.get()
        self.fetch_price = self.selected_prod_price_entry.get()
        
        # Int only for quantity
        if not self.fetch_qty == "":
            try:
                self.fetch_qty = int(self.fetch_qty)
            except ValueError as e:
                self.update_product_btn.config(state='disabled')
                tk.messagebox.showwarning("Warning", "Only Enter Integers")
                self.selected_prod_qty_entry.delete(0,'end')
                # print(e)

        # Float only for price
        if not self.fetch_price == "":
            try:
                self.fetch_price = float(self.fetch_price)
            except ValueError as e:
                self.update_product_btn.config(state='disabled')
                tk.messagebox.showwarning("Warning", "Only Enter Floats")
                self.selected_prod_price_entry.delete(0,'end')   
        
        # Enabling Update Button
        if not self.selected_prod_qty_entry.get() == "" and not self.selected_prod_price_entry.get() == "":
                self.update_product_btn.config(state='normal')     
        else:
            self.update_product_btn.config(state='disabled')
            

    def update_product(self):
        self.selected_prod = self.selected_prod_name_txt.get("1.0",'end').rstrip()
        self.fetch_qty = int(self.selected_prod_qty_entry.get())
        self.fetch_price = float(self.selected_prod_price_entry.get())
        # print(self.selected_prod, self.fetch_qty, self.fetch_price)
        self.db_obj.update_product_quantity(self.fetch_qty, self.selected_prod)
        self.db_obj.update_product_price(self.fetch_price, self.selected_prod)
        # Searching Again to update value in the Treeview/ Product List
        self.search_product()
        tk.messagebox.showinfo("Successful", f"\"{self.selected_prod}\" value updated in the database")


    def get_junk_sub_categories(self, *args):
        """ Sorts out the junk sub-categories present in the SUB-CATEGORY TABLE
            but not in the PRODUCT TABLE. ie., Product not availabe for that SUB-CAT
        """
        sub_categories = []
        for i in self.db_obj.get_sub_category('%'):
            sub_categories.append(i[0])
        # print(sub_categories)

        product_sub_categories = []
        for i in self.db_obj.get_product_details('%'):
            product_sub_categories.append(i[3])
        # print(set(product_sub_categories))
        
        junk_sub_categories = list((set(sub_categories) - set(product_sub_categories)))
        return junk_sub_categories


    def get_junk_categories(self, *args):
        """ Sorts out the junk categories present in the CATEGORY TABLE
            but not in the PRODUCT TABLE. ie., Product not availabe for that CAT
        """
        categories = []
        for i in self.db_obj.get_category():
            categories.append(i[0])
        # print(categories)

        product_categories = []
        for i in self.db_obj.get_product_details('%'):
            product_categories.append(i[4])
        # print(set(product_categories))
        
        junk_categories = list((set(categories) - set(product_categories)))
        return junk_categories


    def delete_product(self):
        # Fetching selected item
        cur_item = self.product_list_treeview.focus()
        # Selected Prod Name, Sub-Category , Category
        selected_prod_name = self.product_list_treeview.item(cur_item)['values'][1]
        selected_prod_subcategory = self.product_list_treeview.item(cur_item)['values'][3]
        selected_prod_category = self.product_list_treeview.item(cur_item)['values'][2]
        
        # Connecting to db to delete the product
        self.db_obj.delete_product(selected_prod_name)
        self.prod_search_entry.delete(0,'end')
        self.search_product()
        # Cleaning Junk Sub-Category
        # Deleting Sub-Category if no other products has that sub-category
        # Deleting Junk Sub-Categories first to avoid FOREIGN KEY constraint failed
        if selected_prod_subcategory in self.get_junk_sub_categories():
            self.db_obj.delete_sub_category(selected_prod_subcategory)
        # Cleaning Junk Category
        # Deleting Category if no other products has that category
        if selected_prod_category in self.get_junk_categories():
            self.db_obj.delete_category(selected_prod_category)
        
        

if __name__ == "__main__":
    master = tk.Tk()
    win_width, win_height = 1340, 680
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = int((screen_width/2) - (win_width/2))  - 7
    y = int((screen_height/2) - (win_height/2)) - 35
    master.geometry(f'{win_width}x{win_height}+{x}+{y}')
    master.resizable(0,0)
    frame = InventoryWindow(master).pack()
    master.mainloop()