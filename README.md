# Library-Management-System
----------------------------
This project is soely for teaching purpose only. Other uses of this project should be restricted.

<h4> To Run the Project directly without installing aything </h4>(all you need is only the <kbd>run</kbd> folder)
<h4> Goto run folder --> double click on run.exe (with books icon)</h4>

This project requires some additional packages for python to run.

1. PyQt5 - to install run  <kbd>pip install PyQt5</kbd> in command prompt
2. sqlite3 - to install run  <kbd>pip install pysqlite</kbd>  in command prompt
3. optionally you can install DB browser for sqlite to see the database structure and data

Default Users
--------------
Here some Users are already created like
1. Username - Test Admin<br>
   User id - 100<br>
   Password - admin@123<br>
2. Username - Test Librarian<br>
   User id - 101<br>
   Password - library@123<br>
3. Username - Test Member<br>
   User id - 102<br>
   Password - member@123<br>

How to create other Users
-------------------------
For creating any Type of User First you have to create a new user by register option.
By default the user will be created as member only.
Then by logging in as admin (or default admin) you can change the user type as admin or librarian.

only admin can give different access to users and check the feedbacks
only librarian can add book, manage book, issue book to members and return books from user

where as members can search for books and see their history of issued books, also they can submit feedback

To change the notice
--------------------
1. write the notice in notice.txt
present in notice folder
2. save the file
3. restart the program

Database
--------
The database for the project is present in <kbd>database</kbd> folder called app.db
The database can be visualised using <kbd>DB browser for Sqlite</kbd> or any other sqlite browser applications.

UI files
--------
All the GUI files are present in the <kbd>Ui pages</kbd> folder

