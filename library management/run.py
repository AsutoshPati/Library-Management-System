#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtWidgets, uic, QtCore
import sqlite3 as sql
import datetime


# In[2]:


curr_id = None
curr_name = None
login_time = None
des = ""
utype = ""
fine_per_extra_day = 2
f = open(r"notices/notice.txt")
notice = f.read()
if notice == "":
    notice = "No new notices"
f.close()


# In[3]:


#clear inputs all pages

def clear_login():
    login.label_7.setText("")
    login.lineEdit.setText("")
    login.lineEdit_2.setText("")

def clear_reg():
    reg.lineEdit.setText("")
    reg.lineEdit_2.setText("")
    reg.lineEdit_3.setText("")
    reg.lineEdit_4.setText("")
    reg.radioButton.setChecked(False)
    reg.radioButton_2.setChecked(False)
    reg.radioButton_3.setChecked(False)
    reg.textEdit.setText("")
    reg.checkBox.setChecked(False)
    reg.checkBox_2.setChecked(False)
    reg.checkBox_3.setChecked(False)
    reg.checkBox_4.setChecked(False)
    reg.checkBox_5.setChecked(False)
    
def clear_forgot():
    forgot.lineEdit.setText("")
    forgot.lineEdit_2.setText("")
    forgot.lineEdit_3.setText("")
    forgot.label_6.setText("")
    
def clear_admin_add_user():
    admin_add_user.lineEdit.setText("")
    admin_add_user.radioButton_2.setChecked(False)
    admin_add_user.label_7.setText("")
    
def clear_lib_add_bk():
    lib_add_bk.lineEdit.setText("")
    lib_add_bk.lineEdit_2.setText("")
    lib_add_bk.lineEdit_3.setText("")
    lib_add_bk.lineEdit_4.setText("")
    lib_add_bk.lineEdit_5.setText("")
    lib_add_bk.comboBox.setCurrentIndex(0)
    lib_add_bk.label_13.setText("")
    
def clear_lib_rm_bk():
    lib_rm_bk.lineEdit.setText("")
    lib_rm_bk.label_11.setText("")
    
def clear_lib_isu_bk():
    lib_isu_bk.lineEdit.setText("")
    lib_isu_bk.lineEdit_2.setText("")
    lib_isu_bk.label_11.setText("")
    
def clear_lib_add_un():
    lib_add_un.lineEdit.setText("")
    lib_add_un.lineEdit_2.setText("")
    lib_add_un.label_11.setText("")
    
def clear_lib_ret_bk():
    lib_ret_bk.lineEdit.setText("")
    lib_ret_bk.label_11.setText("")

def clear_lib_chng_rk():
    lib_chng_rk.lineEdit.setText("")
    lib_chng_rk.label_11.setText("")
    
def clear_mem_srch_bk():
    mem_srch_bk.radioButton_2.setChecked(True)
    mem_srch_bk.lineEdit.setText("")
    mem_srch_bk.lineEdit_2.setText("")
    mem_srch_bk.label_4.setText("")
    mem_srch_bk.tableWidget.setRowCount(0)
    
def clear_mem_chk_bk():
    mem_chk_bk.radioButton.setChecked(True)
    mem_chk_bk.lineEdit.setText("")
    mem_chk_bk.label_4.setText("")
    mem_chk_bk.tableWidget.setRowCount(0)
    
def clear_mem_fbk():
    mem_fbk.textEdit.setText("")
    mem_fbk.label_4.setText("")
    
def clear_admin_feedbacks():
    admin_feedbacks.radioButton_2.setChecked(True)
    admin_feedbacks.label_6.setText("")
    admin_feedbacks.tableWidget.setRowCount(0)
    
def clear_edit_details():
    edit_details.lineEdit.setText("")
    edit_details.lineEdit_2.setText("")
    edit_details.lineEdit_3.setText("")
    edit_details.lineEdit_4.setText("")
    edit_details.radioButton.setChecked(False)
    edit_details.radioButton_2.setChecked(False)
    edit_details.radioButton_3.setChecked(False)
    edit_details.textEdit.setText("")
    edit_details.checkBox.setChecked(False)
    edit_details.checkBox_2.setChecked(False)
    edit_details.checkBox_3.setChecked(False)
    edit_details.checkBox_4.setChecked(False)
    edit_details.checkBox_5.setChecked(False)
    
def logout():
    global curr_id, curr_name, login_time, des, utype
    curr_id = None
    curr_name = None
    login_time = None
    des = ""
    utype = ""
    clear_login()
    login.show()


# In[4]:


# All functions related to login page
def do_login():
    login.label_7.setText("")
    global curr_id, curr_name, login_time, des, utype
    
    uid = login.lineEdit.text()
    pwd = login.lineEdit_2.text()
    conn = sql.connect(r"database/app.db")
    query = """SELECT full_name, mobile_no, isActive, type, gender FROM Users WHERE mobile_no = '{}'
    AND password = '{}'""".format(uid, pwd)
    ret = conn.execute(query)
    data = ret.fetchone()
    conn.close()
    if type(data) != type(None):
        if len(data) == 5:
            if data[2] == 1:
                curr_id = data[1]
                curr_name = data[0]
                utype = data[3]
                login_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                if data[4] == "M":
                    des = "Mr."
                elif data[4] == "F":
                    des = "Mrs./ Miss"
                elif data[4] == "T":
                    des = "Sister"
                if data[3] == "A":
                    admin_home.label_7.setText(des+" "+curr_name)
                    admin_home.label_5.setText("   Logged in by "+curr_name)
                    admin_home.label_3.setText("Logged in at {}   ".format(login_time))
                    login.close()
                    admin_home.show()
                elif data[3] == "L":
                    lib_home.label_7.setText(des+" "+curr_name)
                    lib_home.label_5.setText("   Logged in by "+curr_name)
                    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
                    login.close()
                    lib_home.show()
                elif data[3] == "M":
                    mem_home.label_7.setText(des+" "+curr_name)
                    mem_home.label_5.setText("   Logged in by "+curr_name)
                    mem_home.label_3.setText("Logged in at {}   ".format(login_time))
                    mem_home.textBrowser.setText(notice)
                    login.close()
                    mem_home.show()
                clear_login()
            else:
                login.label_7.setText("You are not an active member!! please go to forget password")
        else:
            login.label_7.setText("technical error!! call for help")
    else:
        login.label_7.setText("invalid user id or password")
    
def open_registration():
    clear_reg()
    login.close()
    reg.show()
    
def forget_pwd():
    clear_forgot()
    forgot.lineEdit.setText(login.lineEdit.text())
    login.close()
    forgot.show()


# In[5]:


#All functions related to Forgot password page
def from_forgot_to_login():
    clear_login()
    forgot.close()
    login.show()
    
def verify_proceed():
    forgot.label_6.setText("")
    uid = forgot.lineEdit.text()
    aid = forgot.lineEdit_2.text()
    pwd = forgot.lineEdit_3.text()
    conn = sql.connect(r"database/app.db")
    query = """SELECT full_name, mobile_no, isActive FROM Users WHERE mobile_no = '{}'
    AND aadhaar_no = '{}'""".format(uid, aid)
    ret = conn.execute(query)
    data = ret.fetchone()
    if type(data) != type(None):
        query = """UPDATE Users SET password = '{}', isActive = 1  WHERE mobile_no = '{}'
        AND aadhaar_no = '{}'""".format(pwd, uid, aid)
        conn.execute(query)
        conn.commit()
        if data[2] == 0:
            forgot_suc.label_2.setText("Your account has been activated")
            clear_login()
            forgot.close()
            forgot_suc.show()
        else:
            forgot_suc.label_2.setText("Your password has been updated")
            clear_login()
            forgot.close()
            forgot_suc.show()
        
    else:
        forgot.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        forgot.label_6.setText("Userid and aadhaar doesn't match")
    conn.close()
    


# In[6]:


#All functions related to Forgot password success page
def from_forgot_suc_to_login():
    clear_login()
    forgot_suc.close()
    login.show()


# In[7]:


#All functions related to registration
def from_reg_to_login():
    clear_login()
    reg.close()
    login.show()
    
def do_register():
    name = reg.lineEdit.text()
    mob = reg.lineEdit_2.text()
    pwd = reg.lineEdit_3.text()
    uidai = reg.lineEdit_4.text()
    gen = None
    des = ""
    if reg.radioButton.isChecked():
        gen = "M"
        des = "Mr."
    elif reg.radioButton_.isChecked():
        gen = "F"
        des = "Mrs./Miss"
    elif reg.radioButton_3.isChecked():
        gen = "T"
        des = "Sister"
    add = reg.textEdit.toPlainText()
    pref = []
    if reg.checkBox.isChecked():
        pref.append("Education")
    if reg.checkBox_2.isChecked():
        pref.append("Horror")
    if reg.checkBox_3.isChecked():
        pref.append("Romantic")
    if reg.checkBox_4.isChecked():
        pref.append("Cooking")
    if reg.checkBox_5.isChecked():
        pref.append("Life Style")
    if name!="" and mob!="" and pwd!="" and uidai!="" and add!="":
        conn = sql.connect(r"database/app.db")
        query = """SELECT full_name FROM Users WHERE mobile_no = '{}'""".format(mob)
        ret = conn.execute(query)
        data = ret.fetchone()
        if type(data) == type(None):
            query = """SELECT full_name FROM Users WHERE
            aadhaar_no = '{}'""".format(uidai)
            ret = conn.execute(query)
            data = ret.fetchone()
            if type(data) == type(None):
                try:
                    query = '''INSERT INTO Users(full_name, mobile_no, password, aadhaar_no,
                    gender, address, preferences) VALUES("{}", "{}", "{}", "{}",
                    "{}", "{}", "{}")'''.format(name, mob, pwd, uidai, gen, add, pref)
                    conn.execute(query)
                    conn.commit()
                    reg_suc.label_2.setText("For creating an acoount {} {}".format(des, name))
                    reg.close()
                    reg_suc.show()
                    clear_reg()
                except:
                    reg_error.label.setText("Oops!! Unable to register due to")
                    reg_error.label_2.setText("Technical erorr!! Please try again later")
                    reg_error.show()
            else:
                reg_error.label.setText("Oops!! Unable to register due to")
                reg_error.label_2.setText("User already exist with same mobile number")
                reg_error.show()
        else:
            reg_error.label.setText("Oops!! Unable to register due to")
            reg_error.label_2.setText("User already exist with same mobile number")
            reg_error.show()
    else:
        reg_error.label.setText("Oops!! Unable to register due to")
        reg_error.label_2.setText("All mandatory fields needs to be completed")
        reg_error.show()


# In[8]:


#All functions related to registration error page
def close_reg_error():
    reg_error.close()


# In[9]:


#All functions related to registration error page
def from_reg_error_to_login():
    clear_login()
    reg_suc.close()
    login.show()


# In[10]:


#All functions related to admin home page
def from_admin_home_logout():
    admin_home.close()
    logout()
    
def from_admin_home_to_member():
    mem_home.label_7.setText(des+" "+curr_name)
    mem_home.label_5.setText("   Logged in by "+curr_name)
    mem_home.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.textBrowser.setText(notice)
    admin_home.close()
    mem_home.show()
    
def from_admin_home_to_admin_add_user():
    clear_admin_add_user()
    admin_add_user.label_5.setText("   Logged in by "+curr_name)
    admin_add_user.label_3.setText("Logged in at {}   ".format(login_time))
    admin_home.close()
    admin_add_user.show()
    
def from_admin_home_to_admin_feedbacks():
    clear_admin_feedbacks()
    admin_feedbacks.label_5.setText("   Logged in by "+curr_name)
    admin_feedbacks.label_3.setText("Logged in at {}   ".format(login_time))
    admin_home.close()
    admin_feedbacks.show()
    clear_admin_feedbacks()


# In[11]:


#All functions related to admin add user page
def from_admin_add_user_logout():
    admin_add_user.close()
    logout()
    clear_admin_add_user()

def from_admin_add_user_to_admin_home():
    admin_home.label_7.setText(des+" "+curr_name)
    admin_home.label_5.setText("   Logged in by "+curr_name)
    admin_home.label_3.setText("Logged in at {}   ".format(login_time))
    admin_add_user.close()
    admin_home.show()
    clear_admin_add_user()
    
def from_admin_add_user_to_admin_feedbacks():
    clear_admin_feedbacks()
    admin_feedbacks.label_5.setText("   Logged in by "+curr_name)
    admin_feedbacks.label_3.setText("Logged in at {}   ".format(login_time))
    admin_add_user.close()
    admin_feedbacks.show()
    clear_admin_add_user()
    
def update_user():
    uid = admin_add_user.lineEdit.text()
    utype = None
    if admin_add_user.radioButton.isChecked():
        utype = "A"
    elif admin_add_user.radioButton_2.isChecked():
        utype = "L"
    conn = sql.connect(r"database/app.db")
    query = "SELECT full_name FROM Users WHERE mobile_no='{}'".format(uid)
    ret = conn.execute(query)
    data = ret.fetchone()
    if type(data)!=type(None):
        query = "UPDATE Users SET type = '{}' WHERE mobile_no='{}'".format(utype, uid)
        conn.execute(query)
        conn.commit()
        admin_add_user.label_7.setStyleSheet("color: rgb(0, 255, 0);")
        admin_add_user.label_7.setText("User type updated")
        admin_add_user.lineEdit.setText("")
        admin_add_user.radioButton_2.setChecked(False)
    else:
        admin_add_user.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        admin_add_user.label_7.setText("No such user with this ID")
    conn.close()


# In[12]:


#All functions related to library home page
def from_lib_home_logout():
    lib_home.close()
    logout()
    
def from_lib_home_to_member():
    mem_home.label_7.setText(des+" "+curr_name)
    mem_home.label_5.setText("   Logged in by "+curr_name)
    mem_home.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.textBrowser.setText(notice)
    lib_home.close()
    mem_home.show()
    
def from_lib_home_to_lib_add_bk():
    clear_lib_add_bk()
    lib_add_bk.label_5.setText("   Logged in by "+curr_name)
    lib_add_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_home.close()
    lib_add_bk.show()
    
def from_lib_home_to_lib_rm_bk():
    clear_lib_rm_bk()
    lib_rm_bk.label_5.setText("   Logged in by "+curr_name)
    lib_rm_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_home.close()
    lib_rm_bk.show()
    
def from_lib_home_to_lib_isu_bk():
    clear_lib_isu_bk()
    lib_isu_bk.label_5.setText("   Logged in by "+curr_name)
    lib_isu_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_home.close()
    lib_isu_bk.show()


# In[13]:


#All functions related to library add book
def from_lib_add_bk_logout():
    lib_add_bk.close()
    logout()
    clear_lib_add_bk()

def from_lib_add_bk_to_lib_home():
    lib_home.label_7.setText(des+" "+curr_name)
    lib_home.label_5.setText("   Logged in by "+curr_name)
    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_bk.close()
    lib_home.show()
    clear_lib_add_bk()

def from_lib_add_bk_to_lib_rm_bk():
    clear_lib_rm_bk()
    lib_rm_bk.label_5.setText("   Logged in by "+curr_name)
    lib_rm_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_bk.close()
    lib_rm_bk.show()
    
def from_lib_add_bk_to_lib_isu_bk():
    clear_lib_isu_bk()
    lib_isu_bk.label_5.setText("   Logged in by "+curr_name)
    lib_isu_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_bk.close()
    lib_isu_bk.show()
    
def from_lib_add_bk_to_lib_add_un():
    clear_lib_add_un()
    lib_add_un.label_5.setText("   Logged in by "+curr_name)
    lib_add_un.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_bk.close()
    lib_add_un.show()
    
def add_book():
    isbn = lib_add_bk.lineEdit.text()
    name = lib_add_bk.lineEdit_2.text()
    price = lib_add_bk.lineEdit_3.text()
    auth = lib_add_bk.lineEdit_4.text()
    pub = lib_add_bk.lineEdit_5.text()
    gen = lib_add_bk.comboBox.currentText()
    conn = sql.connect(r"database/app.db")
    query = "SELECT * FROM Books WHERE ISBN = '{}'".format(isbn)
    ret = conn.execute(query)
    data = ret.fetchone()
    if type(data) == type(None):
        if isbn!="" and name!="" and auth!="" and pub!="" and gen!="":
            try:
                price = float(price)
                query = """INSERT INTO Books VALUES('{}', '{}',
                {}, '{}', '{}', '{}')""".format(isbn, name, price, auth, pub, gen)
                conn.execute(query)
                conn.commit()
                lib_add_bk.label_13.setStyleSheet("color: rgb(0, 130, 0);")
                lib_add_bk.label_13.setText("Book Added to List")
                clear_lib_add_bk()
            except:
                lib_add_bk.label_13.setStyleSheet("color: rgb(255, 0, 0);")
                lib_add_bk.label_13.setText("Enter price value correctly")
        else:
            lib_add_bk.label_13.setStyleSheet("color: rgb(255, 0, 0);")
            lib_add_bk.label_13.setText("All fields are mandatory to fill")
    else:
        lib_add_bk.label_13.setStyleSheet("color: rgb(255, 0, 0);")
        lib_add_bk.label_13.setText("This Book is already present")
    conn.close()


# In[14]:


#All functions related to library add units
def from_lib_add_un_logout():
    lib_add_un.close()
    logout()
    clear_lib_add_un()
    
def from_lib_add_un_to_lib_home():
    lib_home.label_7.setText(des+" "+curr_name)
    lib_home.label_5.setText("   Logged in by "+curr_name)
    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_un.close()
    lib_home.show()
    clear_lib_add_un()
    
def from_lib_add_un_to_lib_rm_bk():
    clear_lib_rm_bk()
    lib_rm_bk.label_5.setText("   Logged in by "+curr_name)
    lib_rm_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_un.close()
    lib_rm_bk.show()
    
def from_lib_add_un_to_lib_isu_bk():
    clear_lib_isu_bk()
    lib_isu_bk.label_5.setText("   Logged in by "+curr_name)
    lib_isu_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_un.close()
    lib_isu_bk.show()
    
def from_lib_add_un_to_lib_add_bk():
    clear_lib_add_bk()
    lib_add_bk.label_5.setText("   Logged in by "+curr_name)
    lib_add_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_add_un.close()
    lib_add_bk.show()
    
def add_units():
    isbn = lib_add_un.lineEdit.text()
    rack = lib_add_un.lineEdit_2.text()
    conn = sql.connect(r"database/app.db")
    query = "SELECT * FROM Books WHERE ISBN = '{}'".format(isbn)
    ret = conn.execute(query)
    data = ret.fetchone()
    if type(data) != type(None):
        query = """INSERT INTO lib_books(ISBN, rack)
        VALUES('{}', '{}')""".format(isbn, rack)
        conn.execute(query)
        conn.commit()
        clear_lib_add_un()
        query = """SELECT book_id FROM lib_books WHERE ISBN = '{}'
        ORDER BY book_id DESC""".format(isbn)
        ret = conn.execute(query)
        data = ret.fetchone()
        lib_add_un.label_11.setStyleSheet("color: rgb(0, 130, 0);")
        lib_add_un.label_11.setText("Book added..Generated id is " + str(data[0]))
    else:
        lib_add_un.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        lib_add_un.label_11.setText("This Book is not present in list!! Kindly add it")
    conn.close()


# In[15]:


#All functions related to library remove soiled books
def from_lib_rm_bk_logout():
    lib_rm_bk.close()
    logout()
    clear_lib_rm_bk()
    
def from_lib_rm_bk_to_lib_home():
    lib_home.label_7.setText(des+" "+curr_name)
    lib_home.label_5.setText("   Logged in by "+curr_name)
    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
    lib_rm_bk.close()
    lib_home.show()
    clear_lib_rm_bk()

def from_lib_rm_bk_to_lib_add_bk():
    clear_lib_add_bk()
    lib_add_bk.label_5.setText("   Logged in by "+curr_name)
    lib_add_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_rm_bk.close()
    lib_add_bk.show()
    
def from_lib_rm_bk_to_lib_isu_bk():
    clear_lib_isu_bk()
    lib_isu_bk.label_5.setText("   Logged in by "+curr_name)
    lib_isu_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_rm_bk.close()
    lib_isu_bk.show()
    
def remove_books():
    bid = lib_rm_bk.lineEdit.text()
    conn = sql.connect(r"database/app.db")
    query = "SELECT * FROM lib_books WHERE book_id={}".format(bid)
    ret = conn.execute(query)
    data = ret.fetchone()
    if type(data) != type(None):
        query = "UPDATE lib_books SET isSoiled = 1 WHERE book_id={}".format(bid)
        conn.execute(query)
        conn.commit()
        clear_lib_rm_bk()
        lib_rm_bk.label_11.setStyleSheet("color: rgb(0, 130, 0);")
        lib_rm_bk.label_11.setText("This Book has been set as soiled book")
    else:
        lib_rm_bk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        lib_rm_bk.label_11.setText("No book found with this ID")
    conn.close()


# In[16]:


#All functions related to library issue books
def from_lib_isu_bk_logout():
    lib_isu_bk.close()
    logout()
    clear_lib_isu_bk()
    
def from_lib_isu_bk_to_lib_home():
    lib_home.label_7.setText(des+" "+curr_name)
    lib_home.label_5.setText("   Logged in by "+curr_name)
    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
    lib_isu_bk.close()
    lib_home.show()
    clear_lib_isu_bk()

def from_lib_isu_bk_to_lib_add_bk():
    clear_lib_add_bk()
    lib_add_bk.label_5.setText("   Logged in by "+curr_name)
    lib_add_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_isu_bk.close()
    lib_add_bk.show()
    clear_lib_isu_bk()
    
def from_lib_isu_bk_to_lib_rm_bk():
    clear_lib_rm_bk()
    lib_rm_bk.label_5.setText("   Logged in by "+curr_name)
    lib_rm_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_isu_bk.close()
    lib_rm_bk.show()
    clear_lib_isu_bk()
    
def from_lib_isu_bk_to_lib_ret_bk():
    clear_lib_ret_bk()
    lib_ret_bk.label_5.setText("   Logged in by "+curr_name)
    lib_ret_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_isu_bk.close()
    lib_ret_bk.show()
    clear_lib_isu_bk()
    
def from_lib_isu_bk_to_lib_chng_rk():
    clear_lib_chng_rk()
    lib_chng_rk.label_5.setText("   Logged in by "+curr_name)
    lib_chng_rk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_isu_bk.close()
    lib_chng_rk.show()
    clear_lib_isu_bk()
    
def issue_book():
    bid = lib_isu_bk.lineEdit.text()
    mid = lib_isu_bk.lineEdit_2.text()
    conn = sql.connect(r"database/app.db")
    query = "SELECT isbn FROM lib_books WHERE book_id={} AND isIssued=0 AND isSoiled=0".format(bid)
    ret = conn.execute(query)
    data = ret.fetchone()
    if type(data) != type(None):
        isbn = data[0]
        query = "SELECT full_name FROM Users WHERE mobile_no='{}'".format(mid)
        ret = conn.execute(query)
        data = ret.fetchone()
        if type(data) != type(None):
            mem_name = data[0]
            query = "SELECT book_name FROM Books WHERE ISBN='{}'".format(isbn)
            ret = conn.execute(query)
            data = ret.fetchone()
            bk_name = data[0]
            curr_dt = datetime.datetime.now()
            ret_dt = curr_dt + datetime.timedelta(days=7)
            curr_dt = curr_dt.strftime("%d-%m-%Y")
            ret_dt = ret_dt.strftime("%d-%m-%Y")
            query = """INSERT INTO book_log(book_id, member_no, issued_on, issued_by,
            return_date) VALUES({},'{}', '{}', '{}', '{}')""".format(bid, mid, curr_dt,
                            curr_id, ret_dt)
            conn.execute(query)
            conn.commit()
            query = """UPDATE lib_books SET isIssued=1 WHERE book_id={}""".format(bid)
            conn.execute(query)
            conn.commit()
            clear_lib_isu_bk()
            lib_isu_bk.label_11.setStyleSheet("color: rgb(0, 130, 0);")
            lib_isu_bk.label_11.setText("{} ({}) is issued to {} ({})".format(bid,
                        bk_name, mid, mem_name))
        else:
            lib_isu_bk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
            lib_isu_bk.label_11.setText("No members found with this ID")
    else:
        lib_isu_bk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        lib_isu_bk.label_11.setText("No book found with this ID or already issued")
    conn.close()


# In[17]:


#All functions related to library return books
def from_lib_ret_bk_logout():
    lib_ret_bk.close()
    logout()
    clear_lib_isu_bk()
    
def from_lib_ret_bk_to_lib_home():
    lib_home.label_7.setText(des+" "+curr_name)
    lib_home.label_5.setText("   Logged in by "+curr_name)
    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
    lib_ret_bk.close()
    lib_home.show()
    clear_lib_ret_bk()

def from_lib_ret_bk_to_lib_add_bk():
    clear_lib_add_bk()
    lib_add_bk.label_5.setText("   Logged in by "+curr_name)
    lib_add_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_ret_bk.close()
    lib_add_bk.show()
    clear_lib_ret_bk()
    
def from_lib_ret_bk_to_lib_rm_bk():
    clear_lib_rm_bk()
    lib_rm_bk.label_5.setText("   Logged in by "+curr_name)
    lib_rm_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_ret_bk.close()
    lib_rm_bk.show()
    clear_lib_ret_bk()
    
def from_lib_ret_bk_to_lib_isu_bk():
    clear_lib_isu_bk()
    lib_isu_bk.label_5.setText("   Logged in by "+curr_name)
    lib_isu_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_ret_bk.close()
    lib_isu_bk.show()
    clear_lib_ret_bk()
    
def from_lib_ret_bk_to_lib_chng_rk():
    clear_lib_chng_rk()
    lib_chng_rk.label_5.setText("   Logged in by "+curr_name)
    lib_chng_rk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_ret_bk.close()
    lib_chng_rk.show()
    clear_lib_ret_bk()
    
def return_book():
    bid = lib_ret_bk.lineEdit.text()
    conn = sql.connect(r"database/app.db")
    try:
        bid = int(bid)
        query = """SELECT ISBN, isIssued FROM lib_books WHERE book_id={}""".format(bid)
        ret = conn.execute(query)
        data = ret.fetchone()
        if type(data) != type(None):
            if data[1] == 1:
                isbn = data[0]
                query = "SELECT book_name FROM Books WHERE ISBN='{}'".format(isbn)
                ret = conn.execute(query)
                data = ret.fetchone()
                bk_name = data[0]
                query = """SELECT member_no, return_date FROM book_log
                WHERE book_id={} AND returned_on IS NULL """.format(bid)
                ret = conn.execute(query)
                data = ret.fetchone()
                mid = data[0]
                issue = data[1]
                issue = issue.split("-")
                issue = datetime.datetime(int(issue[2]), int(issue[1]), int(issue[0]))
                ret_dt = datetime.datetime.now()
                days_kept = ret_dt - issue
                days_kept = days_kept.days
                if days_kept > 0:
                    fine = float(fine_per_extra_day * days_kept)
                else:
                    fine = 0.00
                ret_dt = ret_dt.strftime("%d-%m-%Y")
                query = "SELECT full_name FROM Users WHERE mobile_no='{}'".format(mid)
                ret = conn.execute(query)
                data = ret.fetchone()
                mem_name = data[0]
                query="""UPDATE book_log SET returned_on='{}', returned_by='{}',
                fine={} WHERE book_id={} AND returned_on IS NULL """.format(ret_dt,
                                    curr_id, fine, bid)
                conn.execute(query)
                conn.commit()
                query="""UPDATE lib_books SET isIssued=0 WHERE book_id={}""".format(bid)
                conn.execute(query)
                conn.commit()
                clear_lib_ret_bk()
                lib_ret_bk.label_11.setStyleSheet("color: rgb(0, 130, 0);")
                lib_ret_bk.label_11.setText("{} ({}) is returnrd from {} ({}) with fine rs.{}".format(bid,
                        bk_name, mid, mem_name, fine))
            else:
                lib_ret_bk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
                lib_ret_bk.label_11.setText("This book is not issued by any one")
        else:
            lib_ret_bk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
            lib_ret_bk.label_11.setText("No book found with this ID")
    except Exception as e:
        lib_ret_bk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        lib_ret_bk.label_11.setText("Fill Book id properly")
        #print(type(e),":",e)
    conn.close()


# In[18]:


#All functions related to library change rack
def from_lib_chng_rk_logout():
    lib_chng_rk.close()
    logout()
    clear_lib_chng_rk()
    
def from_lib_chng_rk_to_lib_home():
    lib_home.label_7.setText(des+" "+curr_name)
    lib_home.label_5.setText("   Logged in by "+curr_name)
    lib_home.label_3.setText("Logged in at {}   ".format(login_time))
    lib_chng_rk.close()
    lib_home.show()
    clear_lib_chng_rk()

def from_lib_chng_rk_to_lib_add_bk():
    clear_lib_add_bk()
    lib_add_bk.label_5.setText("   Logged in by "+curr_name)
    lib_add_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_chng_rk.close()
    lib_add_bk.show()
    clear_lib_chng_rk()
    
def from_lib_chng_rk_to_lib_rm_bk():
    clear_lib_rm_bk()
    lib_rm_bk.label_5.setText("   Logged in by "+curr_name)
    lib_rm_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_chng_rk.close()
    lib_rm_bk.show()
    clear_lib_chng_rk()
    
def from_lib_chng_rk_to_lib_isu_bk():
    clear_lib_isu_bk()
    lib_isu_bk.label_5.setText("   Logged in by "+curr_name)
    lib_isu_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_chng_rk.close()
    lib_isu_bk.show()
    clear_lib_chng_rk()
    
def from_lib_chng_rk_to_lib_ret_bk():
    clear_lib_ret_bk()
    lib_ret_bk.label_5.setText("   Logged in by "+curr_name)
    lib_ret_bk.label_3.setText("Logged in at {}   ".format(login_time))
    lib_chng_rk.close()
    lib_ret_bk.show()
    clear_lib_chng_rk()
    
def change_rack():
    bid = lib_chng_rk.lineEdit.text()
    new_rack = lib_chng_rk.lineEdit_2.text()
    conn = sql.connect(r"database/app.db")
    try:
        bid = int(bid)
        if new_rack!="":
            query = "SELECT rack FROM lib_books WHERE book_id={}".format(bid)
            ret = conn.execute(query)
            data = ret.fetchone()
            if type(data) != type(None):
                query = "UPDATE lib_books SET rack = '{}' WHERE book_id={}".format(new_rack, bid)
                conn.execute(query)
                conn.commit()
                clear_lib_chng_rk()
                lib_chng_rk.label_11.setStyleSheet("color: rgb(0, 130, 0);")
                lib_chng_rk.label_11.setText("shelf changed from {} to {}".format(data[0], new_rack))
            else:
                lib_chng_rk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
                lib_chng_rk.label_11.setText("No book found with this ID")
        else:
            lib_chng_rk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
            lib_chng_rk.label_11.setText("Enter Rack name")
    except:
        lib_chng_rk.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        lib_chng_rk.label_11.setText("Fill Book id properly")
    conn.close()


# In[19]:


#All functions related to member home
def from_mem_home_logout():
    mem_home.close()
    logout()
    
def from_mem_home_to_mem_srch_bk():
    clear_mem_srch_bk()
    mem_srch_bk.label_5.setText("   Logged in by "+curr_name)
    mem_srch_bk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.close()
    mem_srch_bk.show()
    
def from_mem_home_to_mem_chk_bk():
    clear_mem_chk_bk()
    mem_chk_bk.label_5.setText("   Logged in by "+curr_name)
    mem_chk_bk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.close()
    mem_chk_bk.show()
    
def from_mem_home_to_mem_fbk():
    clear_mem_fbk()
    mem_fbk.label_5.setText("   Logged in by "+curr_name)
    mem_fbk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.close()
    mem_fbk.show()


# In[20]:


#All functions related to member search book
def from_mem_srch_bk_logout():
    mem_srch_bk.close()
    logout()
    clear_mem_srch_bk()
    
def from_mem_srch_bk_to_mem_home():
    mem_home.label_7.setText(des+" "+curr_name)
    mem_home.label_5.setText("   Logged in by "+curr_name)
    mem_home.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.textBrowser.setText(notice)
    mem_srch_bk.close()
    mem_home.show()
    clear_mem_srch_bk()
    
def from_mem_srch_bk_to_mem_chk_bk():
    clear_mem_chk_bk()
    mem_chk_bk.label_5.setText("   Logged in by "+curr_name)
    mem_chk_bk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_srch_bk.close()
    mem_chk_bk.show()
    clear_mem_srch_bk()
    
def from_mem_srch_bk_to_mem_fbk():
    clear_mem_fbk()
    mem_fbk.label_5.setText("   Logged in by "+curr_name)
    mem_fbk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_srch_bk.close()
    mem_fbk.show()
    clear_mem_srch_bk()
    
def search_book():
    mem_srch_bk.tableWidget.setRowCount(0)
    conn = sql.connect(r"database/app.db")
    if mem_srch_bk.radioButton.isChecked():
        isbn = mem_srch_bk.lineEdit.text()
        if isbn!="":
            query = """SELECT ISBN, book_name, author, genre FROM Books
            WHERE ISBN='{}'""".format(isbn)
            ret =  conn.execute(query)
            data = ret.fetchone()
            if type(data)!=type(None):
                clear_mem_srch_bk()
                mem_srch_bk.tableWidget.insertRow(mem_srch_bk.tableWidget.rowCount())
                mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(isbn))
                mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(data[1]))
                mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(data[2]))
                mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(data[3]))
                query = """SELECT rack FROM lib_books
                WHERE ISBN='{}' AND isIssued=0 AND isSoiled=0""".format(isbn)
                ret =  conn.execute(query)
                data = ret.fetchall()
                if type(data)!=type(None):
                    available = len(data)
                    racks = set()
                    for i in data:
                        racks.add(i[0])
                    rack_text = ""
                    for i in racks:
                        rack_text+=(","+i)
                    rack_text = rack_text[1:]
                    msg = "{} books at {}".format(available, rack_text)
                    mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                        4,QtWidgets.QTableWidgetItem(msg))
                else:
                    mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                        4,QtWidgets.QTableWidgetItem("Currently unavailable"))
            else:
                mem_srch_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
                mem_srch_bk.label_4.setText("No book found with ISBN "+isbn)
        else:
            mem_srch_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            mem_srch_bk.label_4.setText("Enter ISBN number of the book")
    elif mem_srch_bk.radioButton_2.isChecked():
        bname = mem_srch_bk.lineEdit_2.text()
        if bname!="":
            query = """SELECT ISBN, book_name, author, genre FROM Books
            WHERE book_name LIKE '%{}%'""".format(bname)
            ret =  conn.execute(query)
            books = ret.fetchall()
            if len(books)>0:
                clear_mem_srch_bk()
                for i in books:
                    mem_srch_bk.tableWidget.insertRow(mem_srch_bk.tableWidget.rowCount())
                    mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(i[0]))
                    mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(i[1]))
                    mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(i[2]))
                    mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(i[3]))
                    query = """SELECT rack FROM lib_books
                    WHERE ISBN='{}' AND isIssued=0 AND isSoiled=0""".format(i[0])
                    ret =  conn.execute(query)
                    data = ret.fetchall()
                    if type(data)!=type(None):
                        available = len(data)
                        racks = set()
                        for j in data:
                            racks.add(j[0])
                        rack_text = ""
                        for j in racks:
                            rack_text+=(","+j)
                        rack_text = rack_text[1:]
                        msg = "{} books at {}".format(available, rack_text)
                        mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                        4,QtWidgets.QTableWidgetItem(msg))
                    else:
                        mem_srch_bk.tableWidget.setItem(mem_srch_bk.tableWidget.rowCount()-1,
                        4,QtWidgets.QTableWidgetItem("Currently unavailable"))
            else:
                mem_srch_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
                mem_srch_bk.label_4.setText("No books found having "+bname)
        else:
            mem_srch_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            mem_srch_bk.label_4.setText("Enter the book name or a phrase from the name")
    conn.close()


# In[21]:


#All functions related to member issued books
def from_mem_chk_bk_logout():
    mem_chk_bk.close()
    logout()
    clear_mem_chk_bk()
    
def from_mem_chk_bk_to_mem_home():
    mem_home.label_7.setText(des+" "+curr_name)
    mem_home.label_5.setText("   Logged in by "+curr_name)
    mem_home.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.textBrowser.setText(notice)
    mem_chk_bk.close()
    mem_home.show()
    clear_mem_chk_bk()
    
def from_mem_chk_bk_to_mem_srch_bk():
    clear_mem_srch_bk()
    mem_srch_bk.label_5.setText("   Logged in by "+curr_name)
    mem_srch_bk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_chk_bk.close()
    mem_srch_bk.show()
    clear_mem_chk_bk()
    
def from_mem_chk_bk_to_mem_fbk():
    clear_mem_fbk()
    mem_fbk.label_5.setText("   Logged in by "+curr_name)
    mem_fbk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_chk_bk.close()
    mem_fbk.show()
    clear_mem_chk_bk()
    
def issued_books():
    mem_srch_bk.tableWidget.setRowCount(0)
    conn = sql.connect(r"database/app.db")
    if mem_chk_bk.radioButton.isChecked():
        query = """SELECT book_name, issued_on, return_date FROM book_log
        JOIN lib_books on book_log.book_id = lib_books.book_id 
        JOIN Books on lib_books.ISBN = Books.ISBN
        WHERE member_no = '{}' and returned_on IS NULL""".format(curr_id)
        ret = conn.execute(query)
        books = ret.fetchall()
        if len(books)>0:
            clear_mem_chk_bk()
            for i in books:
                mem_chk_bk.tableWidget.insertRow(mem_chk_bk.tableWidget.rowCount())
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(i[0]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(i[1]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(i[2]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(""))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                4,QtWidgets.QTableWidgetItem(""))
        else:
            mem_chk_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            mem_chk_bk.label_4.setText("No books are issued currently")
    elif mem_chk_bk.radioButton_2.isChecked():
        year = mem_chk_bk.lineEdit.text()
        if year!="":
            try:
                year = int(year)
                curr_year = datetime.datetime.now().year
                if year<=curr_year:
                    query = """SELECT book_name, issued_on, return_date, returned_on,
                    fine FROM book_log JOIN lib_books ON
                    book_log.book_id = lib_books.book_id JOIN Books ON
                    lib_books.ISBN = Books.ISBN WHERE member_no = '{}'
                    AND (issued_on LIKE '%{}' OR 
                    returned_on LIKE '%{}')""".format(curr_id,year, year)
                    ret = conn.execute(query)
                    books = ret.fetchall()
                    if len(books)>0:
                        clear_mem_chk_bk()
                        for i in books:
                            mem_chk_bk.tableWidget.insertRow(mem_chk_bk.tableWidget.rowCount())
                            mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(i[0]))
                            mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(i[1]))
                            mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(i[2]))
                            mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(i[3]))
                            mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                4,QtWidgets.QTableWidgetItem(str(i[4])))
                    else:
                        mem_chk_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
                        mem_chk_bk.label_4.setText("No records found in year "+str(year))
                else:
                    mem_chk_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
                    mem_chk_bk.label_4.setText("We dont have records after "+str(curr_year))
            except:
                mem_chk_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
                mem_chk_bk.label_4.setText("Fill the year properly")
        else:
            mem_chk_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            mem_chk_bk.label_4.setText("Enter the year of which you want see records")
    elif mem_chk_bk.radioButton_3.isChecked():
        query = """SELECT book_name, issued_on, return_date, returned_on, fine
        FROM book_log JOIN lib_books on book_log.book_id = lib_books.book_id 
        JOIN Books on lib_books.ISBN = Books.ISBN
        WHERE member_no = '{}'""".format(curr_id)
        ret = conn.execute(query)
        books = ret.fetchall()
        if len(books)>0:
            clear_mem_chk_bk()
            for i in books:
                mem_chk_bk.tableWidget.insertRow(mem_chk_bk.tableWidget.rowCount())
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(i[0]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(i[1]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(i[2]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(i[3]))
                mem_chk_bk.tableWidget.setItem(mem_chk_bk.tableWidget.rowCount()-1,
                                4,QtWidgets.QTableWidgetItem(str(i[4])))
        else:
            mem_chk_bk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            mem_chk_bk.label_4.setText("Books were never issued..Kindly issue some books")
    conn.close()


# In[22]:


#All functions related to member submit feedback
def from_mem_fbk_logout():
    mem_fbk.close()
    logout()
    clear_mem_fbk()
    
def from_mem_fbk_to_mem_home():
    mem_home.label_7.setText(des+" "+curr_name)
    mem_home.label_5.setText("   Logged in by "+curr_name)
    mem_home.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.textBrowser.setText(notice)
    mem_fbk.close()
    mem_home.show()
    clear_mem_fbk()
    
def from_mem_fbk_to_mem_srch_bk():
    clear_mem_srch_bk()
    mem_srch_bk.label_5.setText("   Logged in by "+curr_name)
    mem_srch_bk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_fbk.close()
    mem_srch_bk.show()
    clear_mem_fbk()
    
def from_mem_fbk_to_mem_chk_bk():
    clear_mem_chk_bk()
    mem_chk_bk.label_5.setText("   Logged in by "+curr_name)
    mem_chk_bk.label_3.setText("Logged in at {}   ".format(login_time))
    mem_fbk.close()
    mem_chk_bk.show()
    clear_mem_fbk()
    
def submit_feedback():
    conn = sql.connect(r"database/app.db")
    comment = mem_fbk.textEdit.toPlainText().strip()
    if comment!="":
        query = """SELECT on_date FROM Feedbacks WHERE member_no='{}'
        AND feedback='{}'""".format(curr_id, comment)
        ret = conn.execute(query)
        data = ret.fetchall()
        if len(data) == 0:
            curr_dt = datetime.datetime.now().strftime("%d-%m-%Y")
            query = """INSERT INTO Feedbacks(member_no, feedback, on_date)
            VALUES('{}', '{}', '{}')""".format(curr_id, comment, curr_dt)
            conn.execute(query)
            conn.commit()
            clear_mem_fbk()
            mem_fbk.label_4.setStyleSheet("color: rgb(0, 130, 0);")
            mem_fbk.label_4.setText("Feedback submitted")
        else:
            mem_fbk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
            mem_fbk.label_4.setText("Same feedback already submitted on "+data[0][0])
    else:
        mem_fbk.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        mem_fbk.label_4.setText("Write some comments to submit feedback")
    conn.close()


# In[23]:


#All functions related to admin see feedbacks
def from_admin_feedbacks_logout():
    admin_feedbacks.close()
    logout()
    clear_admin_feedbacks()

def from_admin_feedbacks_to_admin_home():
    admin_home.label_7.setText(des+" "+curr_name)
    admin_home.label_5.setText("   Logged in by "+curr_name)
    admin_home.label_3.setText("Logged in at {}   ".format(login_time))
    mem_home.textBrowser.setText(notice)
    admin_feedbacks.close()
    admin_home.show()
    clear_admin_feedbacks()
    
def from_admin_feedbacks_to_admin_add_user():
    clear_admin_add_user()
    admin_add_user.label_5.setText("   Logged in by "+curr_name)
    admin_add_user.label_3.setText("Logged in at {}   ".format(login_time))
    admin_feedbacks.close()
    admin_add_user.show()
    clear_admin_feedbacks()
    
def show_feedbacks():
    admin_feedbacks.tableWidget.setRowCount(0)
    conn = sql.connect(r"database/app.db")
    if admin_feedbacks.radioButton.isChecked():
        query = """SELECT full_name, mobile_no, on_date, feedback,
        substr(on_date,7,4)||"-"||substr(on_date,4,2)||"-"||substr(on_date,1,2) as date
        FROM Feedbacks JOIN Users ON Feedbacks.member_no = Users.mobile_no
        ORDER BY date DESC;"""
        ret = conn.execute(query)
        data = ret.fetchall()
        if len(data)>0:
            clear_admin_feedbacks()
            for i in data:
                admin_feedbacks.tableWidget.insertRow(admin_feedbacks.tableWidget.rowCount())
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(i[0]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(i[1]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(i[2]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(i[3]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                4,QtWidgets.QTableWidgetItem(i[4]))
            query = "UPDATE Feedbacks SET isShown=1 WHERE isShown=0"
            conn.execute(query)
            conn.commit()
        else:
            admin_feedbacks.label_6.setStyleSheet("color: rgb(255, 0, 0);")
            admin_feedbacks.label_6.setText("No feedbacks are submitted yet.")
    elif admin_feedbacks.radioButton_2.isChecked():
        query = """SELECT full_name, mobile_no, on_date, feedback,
        substr(on_date,7,4)||"-"||substr(on_date,4,2)||"-"||substr(on_date,1,2) as date
        FROM Feedbacks JOIN Users ON Feedbacks.member_no = Users.mobile_no
        WHERE isShown=0 ORDER BY date DESC;"""
        ret = conn.execute(query)
        data = ret.fetchall()
        if len(data)>0:
            clear_admin_feedbacks()
            for i in data:
                admin_feedbacks.tableWidget.insertRow(admin_feedbacks.tableWidget.rowCount())
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                0,QtWidgets.QTableWidgetItem(i[0]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                1,QtWidgets.QTableWidgetItem(i[1]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                2,QtWidgets.QTableWidgetItem(i[2]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                3,QtWidgets.QTableWidgetItem(i[3]))
                admin_feedbacks.tableWidget.setItem(admin_feedbacks.tableWidget.rowCount()-1,
                                4,QtWidgets.QTableWidgetItem(i[4]))
            query = "UPDATE Feedbacks SET isShown=1 WHERE isShown=0"
            conn.execute(query)
            conn.commit()
        else:
            admin_feedbacks.label_6.setStyleSheet("color: rgb(255, 0, 0);")
            admin_feedbacks.label_6.setText("No new feedbacks are available")
    conn.close()


# In[24]:


#All functions related to edit details
def open_edit_details():
    admin_home.close()
    lib_home.close()
    mem_home.close()
    
    conn = sql.connect(r"database/app.db")
    query = "SELECT * FROM Users WHERE mobile_no='{}'".format(curr_id)
    ret = conn.execute(query)
    data = ret.fetchone()
    edit_details.lineEdit.setText(data[0])
    edit_details.lineEdit_2.setText(data[1])
    edit_details.lineEdit_3.setText(data[2])
    edit_details.lineEdit_4.setText(data[3])
    gen = data[4]
    if gen == None:
        edit_details.radioButton.setChecked(False)
        edit_details.radioButton_2.setChecked(False)
        edit_details.radioButton_3.setChecked(False)
    elif gen == "M":
        edit_details.radioButton.setChecked(True)
    elif gen == "F":
        edit_details.radioButton_2.setChecked(True)
    elif gen == "T":
        edit_details.radioButton_3.setChecked(True)
    edit_details.textEdit.setText(data[5])
    pref = data[6][1:-1]
    if pref == "":
        edit_details.checkBox.setChecked(False)
        edit_details.checkBox_2.setChecked(False)
        edit_details.checkBox_3.setChecked(False)
        edit_details.checkBox_4.setChecked(False)
        edit_details.checkBox_5.setChecked(False)
    else:
        for i in pref.split(","):
            if i.strip()[1:-1] == "Education":
                edit_details.checkBox.setChecked(True)
            if i.strip()[1:-1] == "Horror":
                edit_details.checkBox_2.setChecked(True)
            if i.strip()[1:-1] == "Romantic":
                edit_details.checkBox_3.setChecked(True)
            if i.strip()[1:-1] == "Cooking":
                edit_details.checkBox_4.setChecked(True)
            if i.strip()[1:-1] == "Life Style":
                edit_details.checkBox_5.setChecked(True)
    edit_details.show()
    conn.close()
    
def do_edit():
    global curr_id
    mob = edit_details.lineEdit_2.text()
    pwd = edit_details.lineEdit_3.text()
    gen = None
    if edit_details.radioButton.isChecked():
        gen = "M"
    elif edit_details.radioButton_2.isChecked():
        gen = "F"
    elif edit_details.radioButton_3.isChecked():
        gen = "T"
    add = edit_details.textEdit.toPlainText()
    pref = []
    if edit_details.checkBox.isChecked():
        pref.append("Education")
    if edit_details.checkBox_2.isChecked():
        pref.append("Horror")
    if edit_details.checkBox_3.isChecked():
        pref.append("Romantic")
    if edit_details.checkBox_4.isChecked():
        pref.append("Cooking")
    if edit_details.checkBox_5.isChecked():
        pref.append("Life Style")
    if mob!="" and pwd!="" and add!="":
        conn = sql.connect(r"database/app.db")
        query = '''UPDATE Users SET mobile_no="{}", password="{}", address="{}",
        gender="{}", preferences="{}" WHERE mobile_no="{}"'''.format(mob, pwd, add,
                            gen, pref,curr_id)
        conn.execute(query)
        conn.commit()
        print("updated user")
        query = """UPDATE Feedbacks SET member_no='{}' WHERE member_no='{}'""".format(mob,
                                            curr_id)
        conn.execute(query)
        conn.commit()
        print("updated feedback")
        query1 = """UPDATE book_log SET member_no='{}' WHERE member_no='{}'""".format(mob,
                                            curr_id)
        query2 = """UPDATE book_log SET issued_by='{}'
        WHERE issued_by='{}'""".format(mob, curr_id)
        query3 = """UPDATE book_log SET returned_by='{}'
        WHERE returned_by='{}'""".format(mob, curr_id)
        conn.execute(query1)
        conn.execute(query2)
        conn.execute(query3)
        conn.commit()
        print("updated book_log")
        curr_id = mob
        edit_details.close()
        update_suc.show()
        conn.close()
    else:
        reg_error.label.setText("Oops!! Unable to update due to")
        reg_error.label_2.setText("Mandatory fields can not be left empty")
        reg_error.show()
        
def close_account():
    conn = sql.connect(r"database/app.db")
    query = """UPDATE Users SET isActive=0 WHERE mobile_no='{}'""".format(curr_id)
    conn.execute(query)
    conn.commit()
    edit_details.close()
    logout()
    update_suc.label.setText("""Your Account have been deactivated.
To activate again goto forgot password
this window will be closed automatically after 5 seconds""")
    update_suc.show()
    timer.start(5000)
    conn.close()


# In[25]:


#All functions related to successfull update
def goto_home():
    if utype == "A":
        admin_home.label_7.setText(des+" "+curr_name)
        admin_home.label_5.setText("   Logged in by "+curr_name)
        admin_home.label_3.setText("Logged in at {}   ".format(login_time))
        update_suc.close()
        admin_home.show()
    elif utype == "L":
        lib_home.label_7.setText(des+" "+curr_name)
        lib_home.label_5.setText("   Logged in by "+curr_name)
        lib_home.label_3.setText("Logged in at {}   ".format(login_time))
        update_suc.close()
        lib_home.show()
    elif utype == "M":
        mem_home.label_7.setText(des+" "+curr_name)
        mem_home.label_5.setText("   Logged in by "+curr_name)
        mem_home.label_3.setText("Logged in at {}   ".format(login_time))
        mem_home.textBrowser.setText(notice)
        update_suc.close()
        mem_home.show()
        
def close_update_suc():
    update_suc.close()


# In[26]:


# create App
app = QtWidgets.QApplication([])

# load ui files
login = uic.loadUi(r"ui pages/login.ui")
reg = uic.loadUi(r"ui pages/register.ui")
forgot = uic.loadUi(r"ui pages/forgot_password.ui")
forgot_suc = uic.loadUi(r"ui pages/success_forgot.ui")
reg_error = uic.loadUi(r"ui pages/error_register.ui")
reg_suc = uic.loadUi(r"ui pages/success_register.ui")
admin_home = uic.loadUi(r"ui pages/admin_home.ui")
lib_home = uic.loadUi(r"ui pages/librarian_home.ui")
mem_home = uic.loadUi(r"ui pages/member_home.ui")
admin_add_user = uic.loadUi(r"ui pages/admin_add_user.ui")
lib_add_bk = uic.loadUi(r"ui pages/librarian_add_new_book.ui")
lib_rm_bk = uic.loadUi(r"ui pages/librarian_remove_books.ui")
lib_isu_bk = uic.loadUi(r"ui pages/librarian_issue_book.ui")
lib_add_un = uic.loadUi(r"ui pages/librarian_add_new_units.ui")
lib_ret_bk = uic.loadUi(r"ui pages/librarian_return_book.ui")
lib_chng_rk = uic.loadUi(r"ui pages/librarian_change_rack.ui")
mem_srch_bk = uic.loadUi(r"ui pages/member_search_books.ui")
mem_chk_bk = uic.loadUi(r"ui pages/member_issued_books.ui")
mem_fbk = uic.loadUi(r"ui pages/member_feedback.ui")
admin_feedbacks = uic.loadUi(r"ui pages/admin_see_feedbacks.ui")
edit_details = uic.loadUi(r"ui pages/edit_details.ui")
update_suc = uic.loadUi(r"ui pages/success_update.ui")

#connect buttons to functions [login]
login.pushButton.clicked.connect(do_login)
login.pushButton_2.clicked.connect(open_registration)
login.pushButton_3.clicked.connect(forget_pwd)

#connect buttons to functions [forgot password]
forgot.pushButton.clicked.connect(verify_proceed)
forgot.pushButton_2.clicked.connect(from_forgot_to_login)

#connect buttons to functions [success forgot]
forgot_suc.pushButton.clicked.connect(from_forgot_suc_to_login)

#connect buttons to functions [registartion page]
reg.pushButton.clicked.connect(from_reg_to_login)
reg.pushButton_2.clicked.connect(do_register)

#connect buttons to functions [registration error page]
reg_error.pushButton.clicked.connect(close_reg_error)

#connect buttons to functions [registration success page]
reg_suc.pushButton.clicked.connect(from_reg_error_to_login)

#connect buttons to functions [admin home]
admin_home.pushButton_5.clicked.connect(from_admin_home_logout)
admin_home.pushButton.clicked.connect(from_admin_home_to_member)
admin_home.pushButton_2.clicked.connect(from_admin_home_to_admin_add_user)
admin_home.pushButton_3.clicked.connect(from_admin_home_to_admin_feedbacks)
admin_home.pushButton_6.clicked.connect(open_edit_details)

#connect buttons to functions [admin add user]
admin_add_user.pushButton_5.clicked.connect(from_admin_add_user_logout)
admin_add_user.pushButton_6.clicked.connect(from_admin_add_user_to_admin_home)
admin_add_user.pushButton_3.clicked.connect(from_admin_add_user_to_admin_feedbacks)
admin_add_user.pushButton.clicked.connect(update_user)

#connect buttons to functions [librarian home]
lib_home.pushButton_5.clicked.connect(from_lib_home_logout)
lib_home.pushButton.clicked.connect(from_lib_home_to_member)
lib_home.pushButton_2.clicked.connect(from_lib_home_to_lib_add_bk)
lib_home.pushButton_3.clicked.connect(from_lib_home_to_lib_rm_bk)
lib_home.pushButton_4.clicked.connect(from_lib_home_to_lib_isu_bk)
lib_home.pushButton_6.clicked.connect(open_edit_details)

#connect buttons to functions [librarian add book]
lib_add_bk.pushButton_5.clicked.connect(from_lib_add_bk_logout)
lib_add_bk.pushButton_2.clicked.connect(from_lib_add_bk_to_lib_home)
lib_add_bk.pushButton_3.clicked.connect(from_lib_add_bk_to_lib_rm_bk)
lib_add_bk.pushButton_4.clicked.connect(from_lib_add_bk_to_lib_isu_bk)
lib_add_bk.pushButton_6.clicked.connect(from_lib_add_bk_to_lib_add_un)
lib_add_bk.pushButton_7.clicked.connect(add_book)

#connect buttons to functions [librarian add book units]
lib_add_un.pushButton_5.clicked.connect(from_lib_add_un_logout)
lib_add_un.pushButton_2.clicked.connect(from_lib_add_un_to_lib_home)
lib_add_un.pushButton_3.clicked.connect(from_lib_add_un_to_lib_rm_bk)
lib_add_un.pushButton_4.clicked.connect(from_lib_add_un_to_lib_isu_bk)
lib_add_un.pushButton.clicked.connect(from_lib_add_un_to_lib_add_bk)
lib_add_un.pushButton_7.clicked.connect(add_units)

#connect buttons to functions [librarian remove book]
lib_rm_bk.pushButton_5.clicked.connect(from_lib_rm_bk_logout)
lib_rm_bk.pushButton_2.clicked.connect(from_lib_rm_bk_to_lib_home)
lib_rm_bk.pushButton_4.clicked.connect(from_lib_rm_bk_to_lib_isu_bk)
lib_rm_bk.pushButton_3.clicked.connect(from_lib_rm_bk_to_lib_add_bk)
lib_rm_bk.pushButton_7.clicked.connect(remove_books)

#connect buttons to functions [librarian issue book]
lib_isu_bk.pushButton_5.clicked.connect(from_lib_isu_bk_logout)
lib_isu_bk.pushButton_2.clicked.connect(from_lib_isu_bk_to_lib_home)
lib_isu_bk.pushButton_3.clicked.connect(from_lib_isu_bk_to_lib_add_bk)
lib_isu_bk.pushButton_4.clicked.connect(from_lib_isu_bk_to_lib_rm_bk)
lib_isu_bk.pushButton_6.clicked.connect(from_lib_isu_bk_to_lib_ret_bk)
lib_isu_bk.pushButton_8.clicked.connect(from_lib_isu_bk_to_lib_chng_rk)
lib_isu_bk.pushButton_7.clicked.connect(issue_book)

#connect buttons to functions [librarian return book]
lib_ret_bk.pushButton_5.clicked.connect(from_lib_ret_bk_logout)
lib_ret_bk.pushButton_2.clicked.connect(from_lib_ret_bk_to_lib_home)
lib_ret_bk.pushButton_3.clicked.connect(from_lib_ret_bk_to_lib_add_bk)
lib_ret_bk.pushButton_4.clicked.connect(from_lib_ret_bk_to_lib_rm_bk)
lib_ret_bk.pushButton.clicked.connect(from_lib_ret_bk_to_lib_isu_bk)
lib_ret_bk.pushButton_8.clicked.connect(from_lib_ret_bk_to_lib_chng_rk)
lib_ret_bk.pushButton_7.clicked.connect(return_book)

#connect buttons to functions [librarian change rack]
lib_chng_rk.pushButton_5.clicked.connect(from_lib_chng_rk_logout)
lib_chng_rk.pushButton_2.clicked.connect(from_lib_chng_rk_to_lib_home)
lib_chng_rk.pushButton_3.clicked.connect(from_lib_chng_rk_to_lib_add_bk)
lib_chng_rk.pushButton_4.clicked.connect(from_lib_chng_rk_to_lib_rm_bk)
lib_chng_rk.pushButton.clicked.connect(from_lib_chng_rk_to_lib_isu_bk)
lib_chng_rk.pushButton_6.clicked.connect(from_lib_chng_rk_to_lib_ret_bk)
lib_chng_rk.pushButton_7.clicked.connect(change_rack)

#connect buttons to functions [member home]
mem_home.pushButton_5.clicked.connect(from_mem_home_logout)
mem_home.pushButton_2.clicked.connect(from_mem_home_to_mem_srch_bk)
mem_home.pushButton_3.clicked.connect(from_mem_home_to_mem_chk_bk)
mem_home.pushButton_4.clicked.connect(from_mem_home_to_mem_fbk)
mem_home.pushButton_6.clicked.connect(open_edit_details)

#connect buttons to functions [member search book]
mem_srch_bk.pushButton_5.clicked.connect(from_mem_srch_bk_logout)
mem_srch_bk.pushButton_2.clicked.connect(from_mem_srch_bk_to_mem_home)
mem_srch_bk.pushButton_3.clicked.connect(from_mem_srch_bk_to_mem_chk_bk)
mem_srch_bk.pushButton_4.clicked.connect(from_mem_srch_bk_to_mem_fbk)
mem_srch_bk.pushButton.clicked.connect(search_book)

#connect buttons to functions [member issued books]
mem_chk_bk.pushButton_5.clicked.connect(from_mem_chk_bk_logout)
mem_chk_bk.pushButton_2.clicked.connect(from_mem_chk_bk_to_mem_home)
mem_chk_bk.pushButton_3.clicked.connect(from_mem_chk_bk_to_mem_srch_bk)
mem_chk_bk.pushButton_4.clicked.connect(from_mem_chk_bk_to_mem_fbk)
mem_chk_bk.pushButton.clicked.connect(issued_books)

#connect buttons to functions [member give feedback]
mem_fbk.pushButton_5.clicked.connect(from_mem_fbk_logout)
mem_fbk.pushButton_2.clicked.connect(from_mem_fbk_to_mem_home)
mem_fbk.pushButton_3.clicked.connect(from_mem_fbk_to_mem_srch_bk)
mem_fbk.pushButton_4.clicked.connect(from_mem_fbk_to_mem_chk_bk)
mem_fbk.pushButton.clicked.connect(submit_feedback)

#connect buttons to functions [admin see feedback]
admin_feedbacks.pushButton_5.clicked.connect(from_admin_feedbacks_logout)
admin_feedbacks.pushButton_6.clicked.connect(from_admin_feedbacks_to_admin_home)
admin_feedbacks.pushButton_3.clicked.connect(from_admin_feedbacks_to_admin_add_user)
admin_feedbacks.pushButton.clicked.connect(show_feedbacks)

#connect buttons to functions [edit details]
edit_details.pushButton_2.clicked.connect(do_edit)
edit_details.pushButton.clicked.connect(close_account)

#connect buttons to functions [Successfull update]
update_suc.pushButton.clicked.connect(goto_home)

timer = QtCore.QTimer()
timer.timeout.connect(close_update_suc)

#show the file 
clear_login()
login.show()

# execute application
app.exec()

# del application
del app


# In[ ]:




