# importing modules
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import time
import os
import sys
import subprocess
# print(sys.path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lib.main_menu as main_menu
from lib import database as db
from lib.bill import BillWindow
from lib.theme_engine import ThemeEngine



class SalesWindow(tk.Frame, ThemeEngine):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # Initializing Theme Engine
        ThemeEngine.__init__(self)

        self.master = master
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
        title_label = ttk.Label(title_frame, text="SALES", font="Arial 60 bold",
                                foreground='#22d3fe')
        title_label.pack(side="left", padx=320)
        # Date and Time Label
        date_string = time.strftime("%a,%d/%b/%y")
        time_string = time.strftime("%I:%M %p")
        date_label = ttk.Label(title_frame, text=date_string, font="Arial 18 bold")
        date_label.place(x=1030, y=15)
        time_label = ttk.Label(title_frame, text=time_string, font="Arial 18 bold")
        time_label.place(x=1055, y=50)
        
        #=====================  Customer Details Frame / Left Frame 1  ======================
        customer_details_frame = ttk.Frame(bg_frame, border=1)
        customer_details_frame.place(x=20, y=130, width=895, height=82)

        # Heading Label
        heading_label = ttk.Label(customer_details_frame, text="Customer Details",
                                 font="Arial 15 bold", foreground='#4eacfe')
        heading_label.grid(row=0, column=0, padx=30, pady=10) 
        # Customer Name Label and Entry
        cname_label = ttk.Label(customer_details_frame, text="Customer Name",
                                 font="Arial 16 bold")
        cname_label.place(x=50, y=40)
        
        self.cname_entry = tk.Entry(customer_details_frame, font="Arial 16",
                                     width=17, bg=self.entry_bg, fg=self.entry_fg, bd=0)
        self.cname_entry.place(x=244,y=35)
        # Binding Keyrelease to check length of Name shouldnt be > 25 
        self.cname_entry.bind("<KeyRelease>", self.customer_validity_check)
        # Inserting Line label below to make entry widget look modern
        line_label = tk.Label(customer_details_frame, text=("_")*(38),
                                 bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label.place(x=243, y=60)
        # Binding Line-Label to Focus on Entry widget when clicked upon
        line_label.bind("<Button-1>", lambda e: self.cname_entry.focus_set())

        # Customer Contact Number. Label and Entry
        cno_label = ttk.Label(customer_details_frame, text="Contact No.",
                                 font="Arial 16 bold")
        cno_label.place(x=480,y=40)
        
        self.cno_entry = tk.Entry(customer_details_frame,font="Arial 16",
                                 width=17, bg=self.entry_bg, fg=self.entry_fg, bd=0)
        self.cno_entry.place(x=650,y=35)
        # Binding Keyrelease to check length of No. shouldnt be > 10 and should be Integer only 
        self.cno_entry.bind("<KeyRelease>", self.customer_validity_check)
        # Inserting Line label to make entry widget look modern
        line_label = tk.Label(customer_details_frame, text=("_")*(38), bg=self.entry_bg, fg=self.entry_fg, bd=0)
        line_label.place(x=649, y=60)
        # Binding Line-Label to Focus on Entry widget when clicked upon
        line_label.bind("<Button-1>", lambda e: self.cno_entry.focus_set())


        #=====================  OPTIONS Frame / Right Frame 1  ======================
        
        options_frame = ttk.Frame(bg_frame, border=1)
        options_frame.place(x=930, y=130, width=390, height=82)

        # Customer Details Heading Label
        heading_label = ttk.Label(options_frame, text="Options", font=("Arial", 15, "bold"), foreground='#4eacfe')
        heading_label.grid(row=0, column=0, padx=30, pady=10) 

        # Clear all button
        # Clear All Entries, Cart, Selection => Reset everything
        self.clear_all_btn_img = tk.PhotoImage(file="images/clearall_btn.png")
        clear_all_btn = tk.Button(options_frame, image=self.clear_all_btn_img,
                                 bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                command=self.clear_all)
        clear_all_btn.grid(row=1, column=0)

        # Bill Records Button
        # Opens File Explorer to Show Directory in which all transaction/sales records
        # Records are saved in png and .txt formats
        self.bill_records_btn_img = tk.PhotoImage(file="images/bill_records_btn.png")
        bill_records_btn = tk.Button(options_frame, image=self.bill_records_btn_img,
                                    bd=0, bg=self.button_bg, activebackground=self.button_bg,
                                    command=self.bill_records)
        bill_records_btn.place(x=140, y=10)


        #===============  Product Selection Frame / Left Frame 2  ======================
        
        selection_frame = ttk.Frame(bg_frame, border=1)
        selection_frame.place(x=20, y=225, width=405, height=435)
        
        # Heading Label
        heading_label = ttk.Label(selection_frame, text="Product Selection",
                                 font="Arial 15 bold", foreground='#4eacfe')
        heading_label.grid(row=0, column=0, padx=30, pady=10)
             
        # Category 
        category_label = ttk.Label(selection_frame, text="Category",
                                     font="Arial 16 bold")
        category_label.grid(row=1, column=0, padx=(20,0), pady= 10, sticky="W")
        
        self.category_cb = ttk.Combobox(selection_frame, state="readonly", width=27)
        self.category_cb.place(x=200, y=60)
        # Binding mouse left click
        self.category_cb.bind('<Button-1>', self.get_category_values)

        # Sub Category
        sub_category_label = ttk.Label(selection_frame, text="Sub-Category",
                                     font="Arial 16 bold")
        sub_category_label.grid(row=2, column=0, padx=(20,0), pady=10, sticky="W")

        self.sub_category_cb = ttk.Combobox(selection_frame, state="readonly", width=27)
        self.sub_category_cb.place(x=200, y=108)
        # Binding mouse left click
        self.sub_category_cb.bind('<Button-1>', self.get_sub_category_values)

        # Product / Item
        product_label = ttk.Label(selection_frame, text="Product",
                                 font="Arial 16 bold")
        product_label.grid(row=3, column=0, padx=(20,0), pady=10, sticky="W")

        self.product_cb = ttk.Combobox(selection_frame, state='readonly', width=27)
        self.product_cb.place(x=200, y=156)
        # Binding Mouse Left Click
        self.product_cb.bind('<Button-1>', self.get_product_values)
        # Binding Selecting item calls the function
        self.product_cb.bind("<<ComboboxSelected>>", self.get_product_details)

        # Quantity
        qty_label = ttk.Label(selection_frame, text="Quantity",
                             font="Arial 16 bold")
        qty_label.grid(row=4, column=0, padx=(20,0), pady=10, sticky="W")

        self.quantity = tk.StringVar()
        self.qty_entry = tk.Entry(selection_frame, width=30, state='readonly')
        self.qty_entry.place(x=200, y=204)
        # self.qty_entry.grid(row=3, column=1)
        self.qty_entry.bind("<KeyRelease>", self.get_quantity_entered)

        # Remaining Quantity
        stock_label = ttk.Label(selection_frame, text="Stock",
                                 font="Arial 16 bold")
        stock_label.grid(row=5, column=0, padx=(20,0), pady=10, sticky="W")

        self.stock_value = ttk.Label(selection_frame, font="Arial 16 bold")
        self.stock_value.grid(row=5, column=1, padx=15, sticky="NSEW")
        # self.stock_value.place(x=250, y=252)

        # Price Per Unit
        price_label = ttk.Label(selection_frame, text="Unit Price",
                                 font="Arial 16 bold")
        price_label.grid(row=6, column=0, padx=(20,0), pady=10, sticky="W")

        self.unit_price = ttk.Label(selection_frame, font="Arial 16 bold")
        self.unit_price.grid(row=6, column=1, pady=10, sticky="NSEW")

        # Total Price
        tprice_label = ttk.Label(selection_frame, text="Total Price",
                                 font="Arial 16 bold")
        tprice_label.grid(row=7, column=0, padx=(20,0), pady=10, sticky="W")

        self.total_price = ttk.Label(selection_frame, font="Arial 16 bold")
        self.total_price.grid(row=7, column=1, pady=10, sticky="NSEW")
        

        # Add to cart button
        self.add_to_cart_btn_img = tk.PhotoImage(file='images/add_to_cart_btn.png')
        self.add_to_cart_btn = tk.Button(selection_frame, state='disabled',
                             image=self.add_to_cart_btn_img, bd=0, bg=self.button_bg,
                              activebackground=self.button_bg, command=self.add_to_cart)
        self.add_to_cart_btn.place(x=210,y=390)


        #===================  Cart Frame / Right Frame 2  ===========================

        cart_frame = ttk.Frame(bg_frame, border=1)
        cart_frame.place(x=440, y=225, width=880, height=435)

        # Cart Heading Label
        self.add_to_cart_img = tk.PhotoImage(file='images/shopping_cart.png')
        heading_label = ttk.Label(cart_frame, image=self.add_to_cart_img,
                                 text="CART", font="Arial 15 bold",
                                  foreground='#4eacfe', compound='left')
        heading_label.grid(row=0, column=0, padx=60, pady=10, sticky='W')
        
        # Cart Treeview
        self.cart = ttk.Treeview(cart_frame,
                                 columns=("one","two","three","four"),
                                 selectmode ='browse', show='headings')
        self.cart.grid(row=1,column=0, padx=(35,0), ipady=43)

        self.cart.heading('one', text='Product Name')
        self.cart.column('one', minwidth=520, width=520, anchor="w", stretch=False)

        self.cart.heading('two', text='Quantity')
        self.cart.column('two', minwidth=90, width=90, anchor="c", stretch=False)

        self.cart.heading('three', text='Unit Price')
        self.cart.column('three', minwidth=90, width=90, anchor="c", stretch=False)

        self.cart.heading('four', text='Total Price')
        self.cart.column('four', minwidth=90, width=90, anchor="c", stretch=False)

        # Attaching Vertical Scrollbars 
        verscrlbar = ttk.Scrollbar(cart_frame, orient ="vertical",
                                 command=self.cart.yview)
        verscrlbar.grid(row=1, column=5, ipady=130)
        self.cart.configure(yscrollcommand = verscrlbar.set)
        # Attaching Horizontal Scrollbars
        horscrlbar = ttk.Scrollbar(cart_frame, orient ="horizontal",
                                command=self.cart.xview)
        horscrlbar.grid(row=3, column=0, padx=(35,0), ipadx=370)
        self.cart.configure(xscrollcommand=horscrlbar.set)

        # Remove from cart button
        self.remove_from_cart_btn_img = tk.PhotoImage(file='images/remove_selected_btn.png')
        self.remove_from_cart_btn = tk.Button(cart_frame,
                                        image=self.remove_from_cart_btn_img, bd=0,
                                         bg=self.button_bg, activebackground=self.button_bg,
                                          command=self.remove_from_cart)
        self.remove_from_cart_btn.place(x=150, y=390)
        self.gen_bill_btn_img = tk.PhotoImage(file='images/generate_bill_btn.png')
        gen_bill_btn = tk.Button(cart_frame, image=self.gen_bill_btn_img, bd=0,
                                 bg=self.button_bg, activebackground=self.button_bg,
                                  command=self.generate_bill)
        gen_bill_btn.place(x=570, y=390)


    #=======================  Other METHODS ===================================#

    def clear_all(self):
        self.cname_entry.delete(0, 'end')
        self.cno_entry.delete(0, 'end')
        self.category_cb.set('')
        self.get_category_values()
        self.cart.delete(*self.cart.get_children())
    
    def bill_records(self):
        """ Opens File Explorer, Directory where Sales/Bill Records are saved
            Records/Invoices are saved in .png and .txt formats.
        """
        tk.messagebox.showinfo("Wait", "Please wait for File Explorer to Open")
        try:
            subprocess.Popen('explorer "Bill Records"')
        except Exception as e:
            print(e)
            # subprocess.Popen(['xdg-open', path]) 
            # subprocess.Popen(['open', path])

    def customer_validity_check(self, *args):
        """Secures the Customer entries : Name and Number
            Checks if name length <= 25
            Checks if number length = 10
            Allow number only as integer
        """
        self.fetch_cno = self.cno_entry.get().strip()
        self.fetch_cname = self.cname_entry.get().strip()
        # print(self.fetch_cno)
        # print(self.fetch_cname)
        
        # Int only for Phone number
        if not self.fetch_cno == "":
            try:
                self.fetch_cno = int(self.fetch_cno)
            except ValueError as e:
                tk.messagebox.showwarning("Warning", "Only Enter Integers")
                self.cno_entry.delete(0,'end')
        if not len(str(self.fetch_cno)) <= 10:
            tk.messagebox.showwarning("Warning", "Invalid Phone Number")
            self.cno_entry.delete(10,'end')
        if not len(self.fetch_cname) <= 25:
            tk.messagebox.showwarning("Warning", "Only 25 characters allowed in a Name\nOnly input first name.")
            self.cname_entry.delete(25,'end')


    def get_category_values(self, *args):
        """ Fetches Category Values and enables Sub-Cat Combobox widget.
            And disables rest bottom selection widgets
        """
        # db_obj = db.Database()
        data = self.db_obj.get_category()
        cat_names = []
        for cat_name in data:
            cat_names.append(cat_name)
        self.category_cb.config(values=cat_names)
        # print(cat_names)
        self.sub_category_cb.set('')
        self.stock_value.config(text="")
        self.unit_price.config(text="")
        self.total_price.config(text="")
        self.add_to_cart_btn.config(state='disabled')
        self.qty_entry.delete(0, 'end')
        self.qty_entry.config(state='disabled')
        self.product_cb.set('')
        # self.add_to_cart_btn.config(state='disabled')
        # return cat_names

    
    def get_sub_category_values(self, *args):
        """ Fetches Sub-Category Values and enables Product Combobox widget.
            And disables rest bottom selection widgets
        """
        category_selected = self.category_cb.get()
        # print(category_selected)
        # db_obj = db.Database()
        data = self.db_obj.get_sub_category(category_selected)
        sub_cat_names = []
        for sub_cat_name, cat_name in data:
            sub_cat_names.append(sub_cat_name)
        # print(sub_cat_names)
        self.sub_category_cb.config(values=sub_cat_names)
        self.product_cb.set('')
        self.qty_entry.delete(0, 'end')
        self.add_to_cart_btn.config(state='disabled')
        self.stock_value.config(text="")
        self.unit_price.config(text="")
        self.total_price.config(text="")
        self.qty_entry.config(state='disabled')
        
    
    def get_product_values(self, *args):
        """ Fetches all Product Values of the sub-cat selected."""
        sub_category_selected = self.sub_category_cb.get()
        # print(sub_category_selected)
        # db_obj = db.Database()
        data= self.db_obj.get_products(sub_category_selected)
        # print(data)
        product_names = []
        for prod_name, prod_price, prod_qty, sub_cat_name, cat_name in data:
            product_names.append(prod_name)

        self.product_cb.config(values=product_names)

    def get_product_details(self, *args):
        """ Fetches Product info/Values of the productselected.
            and enables Quantity Entry widgets
            Update stock and price Labels
            If cart empty Data is fetch from Original Database.
            Else Data is set to fetch from Temporary in Memory DB.
            ie., Stock values should be updated from Temprorat memory DB.
            Implemented To prevent data loss when force close.
        """
        product_selected = self.product_cb.get()
        # print(product_selected)
        
        # db_obj = db.Database()
        if  len(self.cart.get_children()) == 0:
            self.db_obj.create_replica()
        else:
            pass
        # Connecting to Bak Replica Db and fetching values
        # db_obj = db.Database()
        # data = db_obj.get_product_details(product_selected)
        data = self.db_obj.get_bak_prod_details(product_selected)
        # print(data)
        self.qty_entry.config(state='normal')
        self.stock_value.config(text=data[0][2])
        self.unit_price.config(text=f"\u20B9 {data[0][1]}")
        self.qty_entry.delete(0, 'end')
        self.add_to_cart_btn.config(state='disabled')
        self.total_price.config(text="")
        
    def get_quantity_entered(self, *args):
        """ Fetches Quantity Entered and calculates total price.
            Only integers allowed.
            Enables Add to Cart Button
        """
        quantity_entered = self.qty_entry.get().replace(" ","")
        # print(type(quantity_entered))

        if self.qty_entry.get().replace(" ","") == '':
            self.total_price.config(text="")
            self.add_to_cart_btn.config(state='disabled')
        else:
            try:
                quantity_entered = int(quantity_entered)
                # print(type(quantity_entered))
                unit_price = self.unit_price.cget("text").split("\u20B9")
                unit_price = float(unit_price[1])
                # print(unit_price)
                total_price = 0
                total_price = quantity_entered*unit_price

                self.total_price.config(text=f"\u20B9 {total_price}")
                existing_stock = int(self.stock_value.cget("text"))
                if quantity_entered > existing_stock:
                    tk.messagebox.showwarning("Warning", "Stock not available")
                    self.qty_entry.delete(0, 'end')
                else:
                    self.add_to_cart_btn.config(state='normal')

            except ValueError as e:
                print(e)
                # print('Please enter an integer') #
                tk.messagebox.showwarning("Warning", "Only Enter Integers")
                self.qty_entry.delete(0, 'end')
        
    def add_to_cart(self):
        """ Adds the Selected product and quantity to Cart.
            Reset Quantity.
        """
        product_selected = self.product_cb.get()
        unit_price = self.unit_price.cget("text")
        total_price = self.total_price.cget("text")

        quantity_entered = int(self.qty_entry.get().replace(" ",""))

        if quantity_entered < 1:
            self.qty_entry.delete(0, 'end')
            tk.messagebox.showwarning("Warning", "Atleast 1 unit is required")
        else:
            self.cart.insert("", 'end', text ="", values =(product_selected, quantity_entered, unit_price, total_price))

            # Connecting to temporary backup replica db then removing quantity added to cart from it
            # db_obj = db.Database()
            self.db_obj.update_deduct_bak_prod_quantity(quantity_entered, product_selected)
            # print(self.db_obj.get_bak_prod_details(product_selected))
            # Fetching data from replica product table and updating stocks label
            data = self.db_obj.get_bak_prod_details(product_selected)
            self.stock_value.config(text=data[0][2])
            self.qty_entry.delete(0, 'end')
            self.total_price.config(text="")
            self.add_to_cart_btn.config(state='disabled')

        
            
    def remove_from_cart(self):
        """Removes from cart and adds the stock value to product"""
        try:
            # Getting current item from Cart
            cur_item = self.cart.focus()
    
            # Fetching Product Name, Quantity from cart
            selected_prod_name = self.cart.item(cur_item)['values'][0]
            selected_prod_qty = self.cart.item(cur_item)['values'][1]
            # print(selected_prod_name, selected_prod_qty)
            
            # Connecing to Bak Replica Db to add quantity removed from cart
            # db_obj = db.Database()
            self.db_obj.update_add_bak_prod_quantity(selected_prod_qty, selected_prod_name)
            # print(self.db_obj.get_bak_prod_details(selected_prod_name))
            
            # Deleting Selected item from cart
            selected_item = self.cart.selection()[0]
            self.cart.delete(selected_item)

            # Fetching data from replica product table and updating stocks label
            data = self.db_obj.get_bak_prod_details(selected_prod_name)
            self.stock_value.config(text=data[0][2])
            
        
        except IndexError as e:
            # print(e)
            tk.messagebox.showwarning("Warning", "Select an item to delete")

   
    def generate_bill(self):
        """Items list is fetched from cart and Bill Window is called"""
        items = []
        for line in self.cart.get_children():
            # print("\n")
            items.append(self.cart.item(line)['values'])
        # print(items)
        customer_name = self.cname_entry.get().strip()
        customer_number = self.cno_entry.get().strip()
        # print(customer_name)
        # print(customer_number)
        
        
        
        # Cart empty check
        if not items == []:
            # Customer name empty check
            if not customer_name == "":
                # Customer number empty check
                if not customer_number == "":
                    if not len(customer_number) < 10:
                        for i in range(len(items)):
                            item = items[i]
                            # print(item[0], item[1])
                            self.db_obj.update_deduct_product_quantity(deduct_prod_quantity=item[1], prod_name=item[0])
                        BillWindow(customer_name, customer_number,items, self.master)
                        self.clear_all()
                    else:
                        self.cno_entry.focus_set()
                        tk.messagebox.showwarning("Warning", "Invalid Customer Contact Number.")    
                else:
                    self.cno_entry.focus_set()
                    tk.messagebox.showwarning("Warning", "Customer Contact Number missing.")
            else:
                self.cname_entry.focus_set()
                tk.messagebox.showwarning("Warning", "Customer Name missing.")
        else:    
            tk.messagebox.showwarning("Warning", "Cart is empty")

    

if __name__ == "__main__":
    master = tk.Tk()
    win_width, win_height = 1340, 680
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = int((screen_width/2) - (win_width/2)) - 7
    y = int((screen_height/2) - (win_height/2)) - 35
    master.geometry(f'{win_width}x{win_height}+{x}+{y}')
    master.resizable(0,0)
    frame = SalesWindow(master).pack()
    master.mainloop()
