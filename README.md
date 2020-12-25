# INVENTORY MANAGEMENT SYSTEM
Inventory Management System is a full-fledged GUI application for maintenance of inventory and to generate sales invoices with keeping records of every sales.
Consists of following Pages:
* Login
* Sales
* Inventory
* Extras : Includes Theme Switch, Password Changer
* Invoice/ Bill

## Features

#### Fully Functioning Inventory Management System
###### Fully Functioning Inventory Page
* Insertion of new product
* Updating product values
* Deleting Product
###### Fully Functioning Sales Page
* Instant updation of values : Entering quantity updates total price instantly.
* Categorised Product Selection : Divided into category, sub-category and product Selection boxes.
* Cart
* Invoice 

#### Secured
* Encrypted Login : Database shows encrypted username and password in the login table.
* Secured Entries : In integers entry-boxes only integers allowed(eg: Quantity of product) and in floats entry-boxes only floats alowed(eg: Price of product) and sometimes entries gets disabled untill all data are ready to call that function.
* Secured Buttons : Some buttons gets disabled untill all data are ready to call that function
* Secured Sales : Temporary clone database is created upon adding of a product so the quantity doesnt gets vanished upon force-closing of application; Quantity entered always greater than 0 but less than or equal to  max quantity available (0 < quantity_entered > max_quantity+1).
* Invoice Creation with Backing up records of sales : Backup includes Screenshots and csv file at the datetime of sale and person name.

#### Modern GUI
* Mordernised GUI : Traditional Tkinter buttons and UI is old Windows 98-like, so many widgets are designed using Photoshop to get more stylish GUI; Most Entry boxes modernised too.
* Dark and Light Mode Switch
#### Optimised Database
* Eliminated Junk Categories and Sub-Categories entries upon deletion of a product which has unique category and sub category, they gets deleted too.
* Cloning of temporary in-memory database at sales time so that force close of application doesn't corrupt the product quantity value.


## Scope
Inventory Management System can be used by an organization or an individual who needs to manage their sales and inventory records.

## Technologies
Project is created with:
* Python 3.9
* OOPS Concept.
* Tkinter(tk) module for GUI.
* PILLOW and pyscreenshot external module for Screenshots.
* Sqlite3 For database.


## Installation
1. Download the project to your Device using one of the ways listed below
   1. git clone the project:
git clone https://github.com/vishakhg98/Inventory-Management-System.git
   1. Download Zip using : [Download](https://github.com/vishakhg98/Inventory-Management-System/archive/master.zip)
	 
1. (Optional) If want to use virtual environment:
		
		venv\Scripts\activate

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to download the necessary modules using one of the ways listed below.
   1. To install all necessary modules

			pip install -r requirements.txt
   1. To install individually

			pip install Pillow==8.0.1
			pip install pyscreenshot==2.2

## How To Run
(Optional) Use virtual Environment
Run main.py file

	venv\Scripts\activate
	python3 main.py

Username : admin
Password : password


## Screenshots 📸
![Login](https://github.com/vishakhg98/Inventory-Management-System/blob/master/Screenshots/Dark%20Mode/Login.png)
![Main Menu](https://github.com/vishakhg98/Inventory-Management-System/blob/master/Screenshots/Dark%20Mode/Main%20Menu.png)
![Sales](https://github.com/vishakhg98/Inventory-Management-System/blob/master/Screenshots/Dark%20Mode/Sales.png)
![Inventory](https://github.com/vishakhg98/Inventory-Management-System/blob/master/Screenshots/Dark%20Mode/Inventory.png)
![Extras](https://github.com/vishakhg98/Inventory-Management-System/blob/master/Screenshots/Dark%20Mode/Extras.png)

for more screenshots visit [Screenshots](https://github.com/vishakhg98/Inventory-Management-System/tree/master/Screenshots) folder in the main branch.


## Bugs
None, if found any bugs please open an issue.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
