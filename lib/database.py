# importing modules
import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Database():
    """ Connects to Database
        Foreign Key Check=ON
        Key Arguments : None
    """
    def __init__(self):
        # Create a db or connect to one
        self.conn = sqlite3.connect("lib\Database.db")

        # Enabling foreign key constraints
        self.conn.execute("PRAGMA foreign_keys = 1")

        # Create cursor
        self.c = self.conn.cursor()
        
    ####=====================METHODS=========================####
            
    #==================== LOGIN ====================================#
        
    def create_login_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE login (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                PASSWORD TEXT NOT NULL
            )""")

    def insert_login_table(self):
        with self.conn:
            self.c.execute("INSERT INTO login VALUES (1, 'firns', 'ufxx|twi')")
    
    def change_password(self, new_password):
        """Changes Password value from the databse
        Key Arguments: new_password -- String
        """
        with self.conn:
            self.c.execute("UPDATE login SET password = ? WHERE id = 1", (new_password,)) 

    def get_login_data(self):
        with self.conn:
            self.c.execute("SELECT * FROM login")
            result = self.c.fetchone()
            return result   

    #======================== THEME =====================================#

    def create_theme_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE theme (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                theme_mode TEXT NOT NULL
            )""")
    
    def insert_theme_table(self):
        with self.conn:
            self.c.execute("INSERT INTO theme VALUES (1,'Light Mode')")
    
    def get_theme_value(self):
        with self.conn:
            self.c.execute("SELECT * FROM theme")
            result = self.c.fetchone()
            # print(result)
            return result
    
    def change_theme(self, theme_name):
        """Changes Theme value in Database
        Key Arguments: theme_name 
        theme_name allowed values = (1)Light Mode (2) Dark Mode
         """
        with self.conn:
            self.c.execute("UPDATE theme SET theme_mode = ? WHERE id = 1", (theme_name,))
    
    #======================== CATEGORY TABLE =====================================#

    def create_category_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE category (
                cat_name TEXT PRIMARY KEY  NOT NULL
            )""")
    
    def insert_category(self, cat_name):
        """Insert Category value in Database
        Key Arguments: cat_name -- String
        """
        with self.conn:
            self.c.execute("INSERT INTO category (cat_name) VALUES (?)", (cat_name,))
    
    def update_cateory(self, new_cat_name, old_cat_name):
        """Update Category name in Database
        Key Arguments: new_cat_name -- String
                       old_cat_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE category SET cat_name = ? WHERE cat_name = ?", (new_cat_name, old_cat_name))

    def delete_category(self, cat_name):
        """Delete Category value in Database
        Key Arguments: cat_name -- String
         """
        with self.conn:
            self.c.execute("DELETE FROM category WHERE cat_name = ?", (cat_name,))
    
    def get_category(self):
        """Fetches all Category name from Database
        Key Arguments: None
         """
        with self.conn:
            self.c.execute("SELECT * FROM category")
            result = self.c.fetchall()
            # print(result)
            return result
    
    #======================== SUB-CATEGORY TABLE =====================================#

    def create_sub_category_table(self):
        with self.conn:
            self.c.execute("""CREATE TABLE sub_category (
                sub_cat_name TEXT PRIMARY KEY  NOT NULL,
                cat_name TEXT NOT NULL,
                FOREIGN KEY(cat_name) REFERENCES category(cat_name)
            )""")
    
    def insert_sub_category(self, sub_cat_name, cat_name):
        """Insert Sub-Category value in Database
        Key Arguments: sub_cat_name -- String
                    cat_name -- String
        """
        with self.conn:
            self.c.execute("INSERT INTO sub_category VALUES (?,?)", (sub_cat_name, cat_name,))
    
    def update_sub_cateory(self, new_subcat_name, old_subcat_name):
        """Update Sub-Category name in Database
        Key Arguments: new_subcat_name -- String
                       old_subcat_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE sub_category SET sub_cat_name = ? WHERE sub_cat_name = ?", (new_subcat_name, old_subcat_name))

    def delete_sub_category(self, sub_cat_name):
        """Delete Category value in Database
        Key Arguments: cat_name -- String
         """
        with self.conn:
            self.c.execute("DELETE FROM sub_category WHERE sub_cat_name = ?", (sub_cat_name,))

    def get_sub_category(self, category_name):
        """Fetches all Category name from Database
        Key Arguments: category_name -- String
         """
        with self.conn:
            self.c.execute("SELECT * FROM sub_category WHERE cat_name LIKE (?)",(category_name,))
            result = self.c.fetchall()
            # print(result)
            return result

   #======================== PRODUCT TABLE =====================================#

    def create_product_table(self):
       with self.conn:
           self.c.execute("""CREATE TABLE product (
               prod_name TEXT PRIMARY KEY  NOT NULL,
               prod_price REAL  NOT NULL,
               prod_quantity INTEGER  NOT NULL,
               sub_cat_name TEXT  NOT NULL,
               cat_name TEXT NOT NULL,
               FOREIGN KEY(sub_cat_name) REFERENCES sub_category(sub_cat_name)
               FOREIGN KEY(cat_name) REFERENCES category(cat_name)
           )""")

    def insert_product(self, prod_name, prod_price, prod_quantity, sub_cat_name, cat_name):
        """Insert Product value in Database
        Key Arguments: prod_name -- String,
                        prod_price -- Float, prod_quantity -- Int,
                        sub_cat_name--String, cat_name--String.
        """
        with self.conn:
            self.c.execute("""INSERT INTO product (
                prod_name, prod_price, prod_quantity, sub_cat_name, cat_name)
                VALUES (?,?,?,?,?)""", (prod_name, prod_price, prod_quantity, sub_cat_name, cat_name))

    def update_product_price(self, prod_price, prod_name):
        """Update Product price in Database
        Key Arguments: prod_price -- Float
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_price = ? WHERE prod_name = ?", (prod_price, prod_name))

    def update_product_quantity(self, prod_quantity, prod_name):
        """Update Product price in Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_quantity=? WHERE prod_name=?", (prod_quantity, prod_name))

    # Add Amount from Backup Product Table
    def update_add_product_quantity(self, add_prod_quantity, prod_name):
        """Add Product Quantity in Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_quantity = prod_quantity + ? WHERE prod_name=?", (add_prod_quantity, prod_name))

    # Minus Amount from Backup Product Table
    def update_deduct_product_quantity(self, deduct_prod_quantity, prod_name):
        """Deduct/Minus Product Quantity in Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.conn:
            self.c.execute("UPDATE product SET prod_quantity = prod_quantity - ? WHERE prod_name=?", (deduct_prod_quantity, prod_name))    

    # Delete product from Product table            
    def delete_product(self, prod_name):
        """Delete Product value in Database
        Key Arguments: prod_name -- String
        """
        with self.conn:
            self.c.execute("DELETE FROM product WHERE prod_name = (?)",(prod_name,))
    
    def get_products(self, sub_category_name):
        """Fetches set/group of Product values which has a common Sub-Category
        Key Arguments: sub_category_name -- String
        """
        with self.conn:
            self.c.execute("SELECT * FROM product WHERE sub_cat_name=(?)",(sub_category_name,))
            result = self.c.fetchall()
            return result
    
    def get_product_details(self, prod_name):
        """Fetches all Product info/values of a single product.
        Key Arguments: prod_name -- String
        """
        with self.conn:
            self.c.execute("SELECT * FROM product WHERE prod_name LIKE (?)",(prod_name,))
            result = self.c.fetchall()
            return result



    #============================= BACKUP REPLICA TABLE ==============================================#

    def create_replica(self):
        """Creates a duplicate/replica of local disk Database to temp Memory Database.
        Volatile Database.
        Implemented To prevent data loss when force close.
        Key Arguments: None
        """
        # Create a Backup db in memory and copying 
        self.bak_db = sqlite3.connect(':memory:')

        # Copying data to bak.db
        queries = "".join(line for line in self.conn.iterdump())
        # print(queries)
        self.bak_db.executescript(queries)
        # print(self.bak_db)
        
        # Create cursor for bakup db
        self.bak_c = self.bak_db.cursor()
    
    def get_bak_prod_details(self, prod_name):
        """Fetches all Product info/values of a single product from the Temporary in Memory Db.
        Key Arguments: prod_name -- String
        """
        with self.bak_db:
            self.bak_c.execute("SELECT * FROM product WHERE prod_name LIKE (?)",(prod_name,))
            result = self.bak_c.fetchall()
            # print(result)
            return result

    # Add Amount from Backup Product Table
    def update_add_bak_prod_quantity(self, add_prod_quantity, prod_name):
        """Add Product Quantity in temporary in memory Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.bak_db:
            self.bak_c.execute("UPDATE product SET prod_quantity = prod_quantity + ? WHERE prod_name=?", (add_prod_quantity, prod_name))

    # Minus Amount from Backup Product Table
    def update_deduct_bak_prod_quantity(self, deduct_prod_quantity, prod_name):
        """Deduct Product Quantity in temporary in memory Database
        Key Arguments: prod_quantity -- Int
                       prod_name -- String
        """
        with self.bak_db:
            self.bak_c.execute("UPDATE product SET prod_quantity = prod_quantity - ? WHERE prod_name=?", (deduct_prod_quantity, prod_name))


############################################################################################################################################

    def drop_table(self, table_name):
        """Drops given table from the Database.
        Key Arguments: table_name -- String
        """
        with self.conn:
            self.c.execute(f"DROP TABLE {table_name}")




if __name__ == "__main__":
    
    db_obj = Database()
    
    #=================== LOGIN ===============================#
    # # Creating login table
    # db_obj.create_login_table()
    
    # # Inserting to login table
    # db_obj.insert_login_table()
    
    # # Changing Password
    # new_password = "ufxx|twi"
    # new_password = "password"
    # db_obj.change_password(new_password)
    
    # # Fetch Login Data
    # result = db_obj.get_login_data()
    # print(result)
    # print("ID :", result[0])
    # print("USERNAME :", result[1])
    # print("PASSSWORD :", result[2])
    
    #====================== THEME =====================================#
    # # Creating theme table
    # db_obj.create_theme_table()
    
    # # Insert to theme table
    # db_obj.insert_theme_table()

    # # Fetching theme data
    # result = db_obj.get_theme_value()
    # print("Theme Value :", result[1])

    # # Changing theme
    # db_obj.change_theme("Light Mode")


    #====================== Category =====================================#
    # # Creating category table
    # db_obj.create_category_table()
    
    # # Insert to Category table
    # db_obj.insert_category("Cat1")
    # try:
    #     db_obj.insert_category(cat_name=None)
    # except sqlite3.Error as e:
    #     print(e," <= CATEGORY TABLE")
        # if e.args[0].startswith('UNIQUE constraint failed:'):
        #     print("yes")
        # else:
        #     print("No")

    # # Update Category item value
    # db_obj.update_cateory(new_cat_name="Cat2", old_cat_name="Cat1")

    # # Deleting from Category table
    # db_obj.delete_category("Cat2")

    # # Fetch from Category table
    # print(db_obj.get_category())
    

    #====================== Sub-Category =====================================#
    # # Creating sub category table
    # db_obj.create_sub_category_table()

    # # Insert to Sub category table
    # try:
    #     db_obj.insert_sub_category(sub_cat_name="Hair", cat_name="Cosmetics")
    # except sqlite3.Error as er:
    #     print(er)

    # # Update Sub-Category item value
    # db_obj.update_sub_cateory(new_subcat_name="Sub Cat2", old_subcat_name="Sub Cat1")

    # # Deleting from Sub-Category table
    # db_obj.delete_sub_category(sub_cat_name="Sub Cat1")

    # # Fetching Sub cat values
    # print(db_obj.get_sub_category('%'))
    
   
    #====================== Products =====================================#
    # # Creating Products table
    # db_obj.create_product_table()

    # # Insert to products table
    # db_obj.insert_product("Fair & Lovely Women, 50g", 97.0, 50, "Face", "Cosmetics") #Produ name, prod price, prod qty, subcat name=(Hair, Face, Full-Body) , catname
    
    # # Updating product price
    # db_obj.update_product_price(prod_price=97, prod_name="Fair & Lovely Women, 50g")

    # # Updating product quantity 
    # db_obj.update_product_quantity(prod_quantity=60, prod_name="Fair & Lovely Women, 50g")

    # # Adding to the Backup product table quantity
    # db_obj.update_add_product_quantity(add_prod_quantity=10, prod_name="testing")

    # # Deduct from backup product table quantity
    # db_obj.update_deduct_product_quantity(deduct_prod_quantity=10, prod_name="testing")
    
    # # Delete a product from product table
    # db_obj.delete_product(prod_name="Fair & Lovely Women, 50g")
    
    # # Get all products list with help os sub cat name
    # print(db_obj.get_products('Hair'))
    
    # Get all products Details list
    # print(db_obj.get_product_details('%'))

    #====================== BACKUP REPLICA TABLE =====================================#
    # # Getting backup product details
    # db_obj.create_replica()
    # print(db_obj.get_bak_prod_details('%'))

    # # Adding to the Backup product table quantity
    # db_obj.update_add_bak_prod_quantity(add_prod_quantity=10, prod_name="testing")
    # print(db_obj.get_bak_prod_details('testing'))

    # # Deduct from backup product table quantity
    # db_obj.update_deduct_bak_prod_quantity(deduct_prod_quantity=10, prod_name="testing")
    # print(db_obj.get_bak_prod_details('testing'))


    #===========================================================#
    # Drop a table
    # db_obj.drop_table("products")
    
    # prod = "nprod"
    # scat = "cat2"
    # cat = "cat1"
    
    # db_obj.delete_product(prod)
    # db_obj.delete_sub_category(scat)
    # db_obj.delete_category(cat)
