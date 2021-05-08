import mysql.connector
import tkinter as tk  
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
from mysql.connector import Error
from tkinter import messagebox
from tkinter import filedialog
from decimal import *
from datetime import datetime
from datetime import date
#import matplot.pyplot as plot
try:
    connection = mysql.connector.connect(host='localhost',database='shopping',user='root',password='2000')
    cursor = connection.cursor()
except mysql.connector.Error as Error:
    print("Failed to connect to database {}".format(error))
finally:
    if (connection.is_connected()):
        print("Connected to database")
class Image_Module:
    def resize(self,path):
        basewidth = 300
        img = Image.open(path)
        hsize=300
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(path)
    def initialimageposition(self,root):
        text = Text(root, wrap="none")#,bg='#EEE8AA')
        vsb = Scrollbar(orient="vertical", command=text.yview)
        text.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        text.pack(fill="both", expand=True)
        text.insert("end", "\n\n\t")
        return text
    def finalimageposition(self,text,a):
        text.window_create("end", window=a)
        text.insert("end", "\n\n\n\t")
    def finalimagetabposition(self,text,a):
        text.window_create("end", window=a)
        text.insert("end", "\t\t\t\t\t")
    def productposition(self,text,var):
        text.insert(END,var)
        text.insert("end", "\n\n")
    def rooticon(self,root):
        root.title("E-ZONE ELECTRONIC SHOPPING")
        p1 = ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\shopping\category\shopping.jfif"))#(r'C:\Users\admin\Desktop\shopping\category\shopping1.jpg')) 
        root.iconphoto(False,p1)        
class Admin_Module:
    def Search(self,search, tree):
        if search.get() != "":
            tree.delete(*tree.get_children())
            print(search.get())
            values = (("%" + search.get() + "%"),("%" + search.get() + "%"),("%" + search.get() + "%"),)
            print("values : ", values)
            cursor.execute("SELECT PRODUCT_ID, BRD_NAME, category,P_NAME, A_PRICE, S_PRICE, quantity FROM product,brand where product.BRD_ID=brand.BRD_ID and (( P_NAME like %s or category like %s) or brand.BRD_NAME like %s )order by PRODUCT_ID",values)
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
    def ViewForm(self):
        obj = Admin_Module()
        viewform = Toplevel()
        viewform.geometry("700x320")
        viewform.resizable(0, 0)
        TopViewForm = Frame(viewform,width=600, bd=1, relief=SOLID)
        TopViewForm.pack(side=TOP, fill=X)
        LeftViewForm = Frame(viewform,width=600)
        LeftViewForm.pack(side=LEFT, fill=Y)
        MidViewForm = Frame(viewform,width=600)
        MidViewForm.pack(side=RIGHT)
        lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
        lbl_text.pack(fill=X)
        lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
        lbl_txtsearch.pack(side=TOP, anchor=W)
        search = Entry(LeftViewForm, font=('arial', 12), width=10)
        search.pack(side=TOP, padx=10, fill=X)
        obj = Admin_Module()
        btn_search = Button(LeftViewForm, text="Search", command=lambda: obj.Search(search, tree))
        btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
        btn_update = Button(LeftViewForm, text="Update", command=lambda: obj.Update(tree))
        btn_update.pack(side=TOP, padx=10, pady=10, fill=X)
        btn_add = Button(LeftViewForm, text="Add", command=lambda: obj.add_product())
        btn_add.pack(side=TOP, padx=10, pady=10, fill=X)
        btn_delete = Button(LeftViewForm, text="Delete", command=lambda: obj.Delete(tree))
        btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
        btn_reset = Button(LeftViewForm, text="Home", command=lambda: obj.Reset(tree))
        btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        element_header = ['1st', '2nd', '3rd', '4th', '5th', '6th','7th']
        tree = ttk.Treeview(MidViewForm, columns=element_header,
                            selectmode="extended", yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("1st", text="PRO_ID")
        tree.heading("2nd", text="BRAND_NAME")
        tree.heading("3rd", text="CATEGORY")
        tree.heading("4th", text="P_NAME")
        tree.heading("5th", text="A_PRICE")
        tree.heading("6th", text="S_PRICE")
        tree.heading("7th",text="QUANTITY")
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=50)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=150)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.column('#5', stretch=NO, minwidth=0, width=100)
        tree.column('#6', stretch=NO, minwidth=0, width=100)
        tree.column('#7', stretch=NO, minwidth=0, width=100)
        tree.pack()
        obj.DisplayData(tree)
    def update_into_product(self,num, frame, pro_id):
        list = frame.pack_slaves()
        for l in list:
            l.destroy()
        if num == 1:
            Label(frame, text="Actual price : ", font=('arial', 14), bd=15).grid(row=5, column=1)  # ,sticky="e")
            Label(frame, text="Selling price : ", font=('arial', 14), bd=15).grid(row=10, column=1)  # ,sticky="e")
            A_price = Entry(frame, font=(14))
            A_price.grid(row=5, column=2)
            S_price = Entry(frame, font=(14))
            S_price.grid(row=10, column=2)

            def productprice(A_price, S_price, pro_id):
                query = """update product set A_PRICE = %s,S_PRICE =%s  where PRODUCT_ID=%s"""
                svalues = ((A_price.get()), (S_price.get()), (pro_id))
                print(query, svalues)
                MsgBox = messagebox.askquestion('Update Product', 'Are you sure you want to update this product',
                                                icon='warning')
                if MsgBox == 'yes':
                    cursor.execute(query, svalues)
                    connection.commit()
                    messagebox.showinfo('Update Product', 'PRODUCT UPDATED SUCCESSFULLY')

            Button(frame, text="Update Product ", font=(12), width=25, activebackground="pink", activeforeground="blue",
                   command=lambda: productprice(A_price, S_price, pro_id)).grid(pady=25, row=12, columnspan=4)

        else:
            Label(frame, text="Quantity : ", font=('arial', 14), bd=15).grid(row=5, column=1)  # ,sticky="e")
            quantity = Entry(frame, font=(14))
            quantity.grid(row=5, column=2)

            def productquantity(quantity, pro_id):
                query = """update product set quantity=%s  where PRODUCT_ID=%s"""
                svalues = (quantity.get(), (pro_id))
                print(query, svalues)
                MsgBox = messagebox.askquestion('Update Product', 'Are you sure you want to update this product',
                                                icon='warning')
                if MsgBox == 'yes':
                    cursor.execute(query, svalues)
                    connection.commit()
                    messagebox.showinfo('Update Product', 'PRODUCT UPDATED SUCCESSFULLY')

            Button(frame, text="Update Product ", font=(12), width=25, activebackground="pink", activeforeground="blue",
                   command=lambda: productquantity(quantity, pro_id)).grid(pady=25, row=12, columnspan=4)
    def Update(self,tree):
        obj = Admin_Module()
        if not tree.selection():
            print("ERROR")
        else:
            root = Tk()
            frame1 = Frame(root, bg='skyblue')  # bg='pink',
            frame1.pack(side=BOTTOM, fill=BOTH, expand=True)
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            b1 = Button(frame1, text="Update Price ", font=(12), width=25, activebackground="pink",
                        activeforeground="blue", command=lambda: obj.update_into_product(1, frame1, selecteditem[0]))
            b1.pack(padx=25, pady=25)
            b2 = Button(frame1, text="Update Quantity ", font=(12), width=25, activebackground="pink",
                        activeforeground="blue", command=lambda: obj.update_into_product(2, frame1, selecteditem[0]))
            b2.pack(padx=25, pady=25)
        root.mainloop()
    def DisplayData(self,tree):
        cursor.execute("SELECT PRODUCT_ID, BRD_NAME,category, P_NAME, A_PRICE, S_PRICE, quantity FROM product,brand where product.BRD_ID=brand.BRD_ID order by PRODUCT_ID")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
    def Reset(self,tree):
        obj = Admin_Module()
        tree.delete(*tree.get_children())
        obj.DisplayData(tree)
    def Delete(self,tree):
        obj = Admin_Module()
        if not tree.selection():
            print("ERROR")
        else:
            result = messagebox.askquestion('Simple Inventory System', 'Are you sure you want to delete this record?',
                                            icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                cursor.execute("DELETE FROM product WHERE PRODUCT_ID = %s", (selecteditem[0],))
                connection.commit()
        obj.Reset(tree)
    def add(self,frame, pro, Ap, Sp, dtls, brd, cat, pro_img, quantity):
        def insert(id, cty, img):
            insert_query = """insert into category(BRD_ID,category,cat_img) values(%s,%s,%s)"""
            query = (id, cty, img)
            cursor.execute(insert_query, query)
            connection.commit()
            messagebox.showinfo("INFORMATION", "CATEGORY ADDED SUCCESSFULLY")

        cursor.execute("select * from brand")
        rows = cursor.fetchall()
        insert_query = """insert into brand(BRD_ID,BRD_NAME) values(%s,%s)"""
        flag = 0
        max = 0
        for row in rows:
            print(row[0], row[1])
            if (max < row[0]):
                max = row[0]
            if (row[1] == (brd.get())):
                brd_id = row[0]
                flag = 1
        if (brd.get() == ""):
            messagebox.showwarning("INFORMATION", "INVALID BRAND NAME")
        if (flag == 0 and brd.get() != ""):
            brd_count = (max + 1)
            brd_id = brd_count
            query = (brd_count, (brd.get()))
            cursor.execute(insert_query, query)
            connection.commit()
            messagebox.showinfo("INFORMATION", "BRAND ADDED SUCCESSFULLY")
        flag1 = 0
        no = 0
        flag2 = 0
        cursor.execute("select * from category")
        rows = cursor.fetchall()
        for row in rows:
            if ((row[0] == brd_id) and row[1] == (cat.get())):
                no = 1
            if ((row[0] == brd_id)):  # and row[1]== (cat.get())):
                flag1 = 1
            if (row[1] == (cat.get())):
                flag2 = 1
                c_img = row[2]
        if (no == 0):
            if (flag1 == 1 and flag2 == 1):
                insert(brd_id, cat.get(), c_img)
            elif (flag1 == 0 and flag2 == 1):
                insert(brd_id, cat.get(), c_img)
            else:
                def open():
                    filename = filedialog.askopenfilename(initialdir="/Users/admin/Desktop", title="Select A file",
                                                          filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),
                                                                     ("all files", "*.*")))
                    cat_img.insert(0, filename)

                Label(frame, text="Category Image : ", font=('arial', 14), bd=15).grid(row=9, sticky="e")
                cat_img = Entry(frame, font=(14))  # width=12)#, textvariable=number1)
                cat_img.grid(column=1, row=9)
                Button(frame, text="choose file", font=(14), command=open).grid(column=2, row=9)
                Button(frame, text="ADD CATEGORY", width=45, command=lambda: insert(brd_id, cat.get(), cat_img.get()),
                       activebackground="pink", activeforeground="blue").grid(pady=25, row=10, columnspan=2)
        insert_product = """ insert into product(PRODUCT_ID,BRD_ID,P_NAME,A_PRICE,S_PRICE,DETALIS,pro_img,quantity,category)
                                                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute("select * from product")
        rows = cursor.fetchall()
        max = 0
        for row in rows:
            print(row[0], row[1], row[2])
            if (max < row[0]):
                max = row[0]
        pro_id = max + 1
        print(pro_id, brd_id, pro.get(), Ap.get(), Sp.get(), dtls.get("1.0", "end-1c"), pro_img.get(), quantity.get())
        pro_query = (
        pro_id, brd_id, pro.get(), Ap.get(), Sp.get(), dtls.get("1.0", "end-1c"), pro_img.get(), quantity.get(),
        cat.get())  # (pro_id,brd_id,product.get(),A_price.get(),S_price.get(),details.get(),pro_img.get())
        cursor.execute(insert_product, pro_query)
        connection.commit()
        messagebox.showinfo("INFORMATION", "PRODUCT ADDED SUCCESSFULLY")


    def add_product(self):
        win3 = Tk()
        win3.title("ADD PRODUCT")
        frame = Frame(win3, height=200)  # bg='pink',
        frame.pack(side=TOP, pady=20)
        cursor.execute("select distinct BRD_NAME from brand")
        rows = cursor.fetchall()
        brdvalues = []
        for row in rows:
            brdvalues.append(row[0])
        cursor.execute("select distinct category from category")
        rows = cursor.fetchall()
        catvalues = []
        for row in rows:
            catvalues.append(row[0])
        Label(frame, text="Product Name:", font=('arial', 14), bd=15).grid(row=0, sticky="e")
        Label(frame, text="Actual price : ", font=('arial', 14), bd=15).grid(row=1, sticky="e")
        Label(frame, text="Selling price : ", font=('arial', 14), bd=15).grid(row=2, sticky="e")
        Label(frame, text="Details: ", font=('arial', 14), bd=15).grid(row=3, sticky="e")  # ,width=15,height=5)
        Label(frame, text="Brand :", font=('arial', 14), bd=15).grid(row=4, sticky="e")
        Label(frame, text="Category : ", font=('arial', 14), bd=15).grid(row=5, sticky="e")
        Label(frame, text="Product Image : ", font=('arial', 14), bd=15).grid(row=6, sticky="e")
        Label(frame, text="Quantity : ", font=('arial', 14), bd=15).grid(row=7, sticky="e")

        lbl_text = Label(frame)
        lbl_text.grid(row=10, columnspan=2)

        product = Entry(frame, font=(14), width=20)
        product.grid(row=0, column=1)

        A_price = Entry(frame, font=(14))
        A_price.grid(row=1, column=1)

        S_price = Entry(frame, font=(14))
        S_price.grid(row=2, column=1)

        details = Text(frame, font=(14), height=5, width=25)  # Entry(frame, font=(14))
        details.grid(row=3, column=1)

        brd = ttk.Combobox(frame, font=(14))  # width=12)#, textvariable=number)
        brd['values'] = brdvalues
        brd.grid(column=1, row=4)

        cat = ttk.Combobox(frame, font=(14))  # width=12)#, textvariable=number1)
        cat['values'] = catvalues
        cat.grid(column=1, row=5)

        pro_img = Entry(frame, font=(14))
        pro_img.grid(row=6, column=1)

        quantity = Entry(frame, font=(14))
        quantity.grid(row=7, column=1)

        def open():
            filename = filedialog.askopenfilename(initialdir="/Users/admin/Desktop", title="Select A file", filetypes=(
            ("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
            pro_img.insert(0, filename)
        obj = Admin_Module()
        Button(frame, text="choose file", font=(14), command=open).grid(column=3, row=6)
        btn = Button(frame, text="ADD", width=45,
                     command=lambda: obj.add(frame, product, A_price, S_price, details, brd, cat, pro_img, quantity),
                     activebackground="pink",
                     activeforeground="blue")  # , command = lambda : key.add_product(key1,frame,product,A_price,S_price,details,brd,cat,pro_img))
        btn.grid(pady=25, row=8, columnspan=2)
        win3.mainloop()
    def analysis(self):
        pass
    
        import matplotlib.pyplot as plt

        # Data to plot
        cursor.execute("""select count(p1.PRODUCT_ID),p2.P_NAME,b.BRD_NAME,o.DATE_OF_ORDER
                        from pro_in_order p1,product p2,brand b,s_order o where p1.PRODUCT_ID = p2.PRODUCT_ID and p2.BRD_ID=b.BRD_ID and p1.ORDER_ID = o.ORDER_ID
                        group by p1.PRODUCT_ID having o.DATE_OF_ORDER > date_add(current_timestamp(),interval -200 day)
                        order by count(p1.PRODUCT_ID) desc""")
        rows = cursor.fetchall()
        labels =[]
        sizes = []
        explode =[]
        k = 1
        value=0
        count = cursor.rowcount
        print(count)
        for row in rows:
            if k<=5:
                labels.append((row[2] + " - "+row[1]).upper())
                sizes.append(row[0])
                if k==1:
                    explode.append(0.1)
                else:
                    explode.append(0)            
            else:
                value = value + row[0]
                if k==count:
                    labels.append("Remaining products")
                    sizes.append(value)
                    explode.append(0.1)
            k = k+1
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink','tan']
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Weekly analysis of product sale\n\n')
        plt.axis('equal')
        plt.show()
    def gotomenu(self):
        win = Tk()
        win.geometry('500x300')
        obj_img = Image_Module()
        obj_img.rooticon(win)
        frame = Frame(win)  # ,bg='skyblue')
        frame.pack(fill=BOTH, expand=True, anchor='center')
        key = Admin_Module()
        Button(frame,text = 'VIEW PRODUCT',width=25,font=('verdana',14),command = lambda : key.ViewForm(),activebackground = "pink", activeforeground = "blue").pack(padx=20,pady=10)
        Button(frame,text = 'VIEW ANALYSIS',width=25,font=('verdana',14),command = lambda : key.analysis(),activebackground = "pink", activeforeground = "blue").pack(padx=20,pady=10)
        Button(frame, text='QUIT', width=25, font=('verdana', 14), command=lambda: win.destroy(),
               activebackground="pink", activeforeground="blue").pack(padx=20, pady=10)
        win.resizable(width=False, height=False)
        win.mainloop()
class User:
    def update_quantity(self,w,pro_list,ord_id,cust_id,master,root,cart_id):#w,pro_id,ord_id,cust_id,master,root,cart_id
            master.destroy()
            cost = 0
            for pro_id in pro_list:
                print(w,pro_id,ord_id,cust_id)
                query = """UPDATE product SET quantity = quantity - %s  WHERE PRODUCT_ID = %s"""
                svalues = (w,pro_id,)
                cursor.execute(query,svalues)
                cursor.execute(("select S_PRICE from product where PRODUCT_ID = %s"),(pro_id,))
                for row in cursor:
                    price = row[0]
                cost = cost+price
                print("CUSTOMER : PRODUCT : quantity : ",cust_id,pro_id,w)
                pro_query = """insert into pro_in_order (PRODUCT_ID, ORDER_ID, quantity) values (%s,%s,%s)"""
                pro_value = (pro_id,ord_id,w)
                cursor.execute(pro_query,pro_value)
                connection.commit()
            obj=User()
            obj.invoice_generate(cust_id,ord_id,cost,root,cart_id)
    def invoice_generate(self,cust_id,ord_id,cost,root,cart_id):
            print(cust_id,ord_id,cost)
            invoice = 0
            cursor.execute("select max(INVOICE_ID) from invoice")
            rows=cursor.fetchall()
            for row in rows:
                if row[0] == None:
                    invoice = 1
                else:
                    print(row[0])
                    invoice = row[0]+1
            print("invoice id :",invoice)
            invoice_query = """insert into invoice(INVOICE_ID, D_O_B, price, ORDER_ID, CUST_ID) values (%s,%s,%s,%s,%s)"""
            invoice_value = (invoice,datetime.now(),cost,ord_id,cust_id)
            cursor.execute(invoice_query,invoice_value)
            connection.commit()
            obj = User()
            obj.print_invoice(invoice,cust_id,cart_id,root)
    def print_invoice(self,invoice,cust_id,cart_id,root):
        viewform = Toplevel()
        viewform.geometry("700x300")
        viewform.resizable(0, 0)
        TopViewForm = Frame(viewform, bd=1, relief=SOLID)
        TopViewForm.pack(side=TOP, fill=X)
        LeftViewForm = Frame(viewform, width=600)
        LeftViewForm.pack(side=LEFT, fill=Y)
        MidViewForm = Frame(viewform, width=600)
        MidViewForm.pack(side=BOTTOM)
        lbl_text = Label(TopViewForm, text="INVOICE DETAILS", font=('arial', 18), width=600)
        lbl_text.pack(fill=X)
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        element_header = ['1st', '2nd', '3rd', '4th', '5th']
        tree = ttk.Treeview(MidViewForm, columns=element_header,
                            selectmode="extended", yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("1st", text="PRO_ID")
        tree.heading("2nd", text="P_NAME")
        tree.heading("3rd", text="A_PRICE")
        tree.heading("4th", text="S_PRICE")
        tree.heading("5th", text="QUANTITY")
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=50)
        tree.column('#2', stretch=NO, minwidth=0, width=150)
        tree.column('#3', stretch=NO, minwidth=0, width=75)
        tree.column('#4', stretch=NO, minwidth=0, width=75)
        tree.column('#5', stretch=NO, minwidth=0, width=75)
        tree.pack()
        cursor.execute("""select i.INVOICE_ID,i.CUST_ID,c.FNAME,c.LNAME,i.D_O_B,pro.P_NAME,pro.A_PRICE,pro.S_PRICE,i.price,p.PRODUCT_ID,p.quantity,s.mode 
                        from invoice i,s_order s,pro_in_order p,product pro,customer c 
                        where i.ORDER_ID=s.ORDER_ID and i.ORDER_ID = p.ORDER_ID and p.PRODUCT_ID=pro.PRODUCT_ID and i.CUST_ID=c.CUST_ID and 
                        i.INVOICE_ID = %s""",(invoice,))
        rows = cursor.fetchall()
        k = 1
        for row in rows:
            if k==1:
                invoice_id = ("Invoice Id :"+str(row[0]))
                Label(LeftViewForm, text=(invoice_id), font=('arial', 12)).pack(side=TOP, anchor=W)
                Cust_id = ("Customer Id : "+str(row[1]))
                Label(LeftViewForm, text=(Cust_id), font=('arial', 12)).pack(side=TOP, anchor=W)
                Name = ("Customer Name : "+str(row[2]))
                Label(LeftViewForm, text=(Name), font=('arial', 12)).pack(side=TOP, anchor=W)
                D_O_B = ("Date Of Order : "+str(row[4]))
                Label(LeftViewForm, text=(D_O_B), font=('arial', 12)).pack(side=TOP, anchor=W)
                cost = ("Total Price : "+str(row[8]))
                Label(LeftViewForm, text=(cost), font=('arial', 12)).pack(side=TOP, anchor=W)
                cost = ("Mode of payment : "+str(row[11]))
                Label(LeftViewForm, text=(cost), font=('arial', 12)).pack(side=TOP, anchor=W)
                k=0
        open_opt = BooleanVar()
        for row in rows:
            data = (row[9],row[5],row[6],row[7],row[10])
            tree.insert('', 'end', values=(data) )
    
    #        key = Login()
     #       key.customer(root,cart_id,cust_id)
    def order_generate(self,cust_id,pro_id,w,root,cart_id):#cust_id,root):
        master = Tk()
        master.title("Payment Options")
        master.geometry("500x500") 
        v = StringVar(master)
        v.set("0")
        values = {"C O D" ,"Dedit card"}
        obj = User()
        frame = Frame(master,bg='pink')  # bg='pink',
        frame.pack(anchor='center',fill = BOTH,expand=True)
        master.geometry("300x200")
        def show(mode,master,root):
            print("payment is : ",mode)
            cursor.execute("select max(ORDER_ID) from s_order")
            rows=cursor.fetchall()
            ord_id = 0
            for row in rows:
                if row[0] == None:
                    ord_id = 1
                else:
                    print(row[0])
                    ord_id = row[0]+1
            master.counter = master.counter +1
            if master.counter==1:
                if mode =="Dedit card":
                        print(mode)
                        master.destroy()
                        root1 = Tk()
                        root1.geometry("500x400")
                        frame = Frame(root1,bg='pink')  # bg='pink',
                        frame.pack(anchor='center',fill = BOTH,expand=True)
                        Label(frame, text="Card Number:", font=('arial', 14),bg='pink', bd=15).grid(row=4)#, sticky="e")
                        Label(frame, text="Valid thru : ", font=('arial', 14),bg='pink', bd=15).grid(row=6)#, sticky="e")
                        Label(frame, text="CVV : ", font=('arial', 14),bg='pink', bd=15).grid(row=8)#, sticky="e")

                        lbl_text = Label(frame)
                        lbl_text.grid(row=10, columnspan=2)
                        cursor.execute("select card_number from card where CUS_ID = %s",(cust_id,))
                        rows = cursor.fetchall()
                        cards = []
                        for row in rows:
                            cards.append(row[0])
                        card = ttk.Combobox(frame, font=(14))  # width=12)#, textvariable=number)
                        card['values'] = cards
                        card.grid(column=1, row=4)
                        
                        var = StringVar(root1)
                        var.set("MM") # initial value
                        list = []
                        for i in range(1,13,1):
                            list.append(i)
                        MM = ttk.OptionMenu(frame, var,*list) 
                        MM.grid(row=6, column=1)
                        var1 = StringVar(root1)
                        var1.set("YY") 
                        yy = date.today().year
                        print(yy)
                        list1=[]
                        for i in range(yy,yy+15,1):
                            list1.append(i)
                        YY = ttk.OptionMenu(frame, var1,*list1) #"one", "two", "three", "four")
                        YY.grid(row=6, column=2)
                        
                        cvv = Entry(frame, font=(14))
                        cvv.grid(row=8, column=1)
                        Button(frame,text='Proceed',command = lambda:ok()).grid(row=10, column=1)
                        def ok():
                            ord_query = """insert into s_order (ORDER_ID, CUST_ID, DATE_OF_ORDER,mode) values(%s,%s,%s,%s)"""
                            print(ord_id,cust_id,datetime.now())
                            ord_value =(ord_id,cust_id,datetime.now(),mode)
                            cursor.execute(ord_query,ord_value)
                            connection.commit()
                            cursor.execute("select * from card where CUS_ID = %s",(cust_id,))
                            rows = cursor.fetchall()
                            flag=0
                            print(rows)
                            for row in rows:
                                print(row)
                                print(row[1],card.get())
                                if (str(row[1])==str(card.get())):
                                    print("is snvsknkvk")
                                    flag=1
                                    print(row[1])
                            print(flag)
                            if flag==0:
                                cursor.execute("insert into card(CUS_ID, card_number, mm, yy, cvv) values(%s,%s,%s,%s,%s)",(cust_id,card.get(),var.get(),var1.get(),cvv.get()))
                            print(card.get(),cvv.get())
                            print ("value is", var.get(),var1.get())
                            connection.commit()
                            obj.update_quantity(w,pro_id,ord_id,cust_id,root1,root,cart_id)
                else:
                        ord_query = """insert into s_order (ORDER_ID, CUST_ID, DATE_OF_ORDER,mode) values(%s,%s,%s,%s)"""
                        print(ord_id,cust_id,datetime.now())
                        ord_value =(ord_id,cust_id,datetime.now(),mode)
                        cursor.execute(ord_query,ord_value)
                        connection.commit()
                        obj.update_quantity(w,pro_id,ord_id,cust_id,master,root,cart_id)
                master.mainloop()
        master.counter = 0
        for text in values: 
            Button(frame, text = text, width = 30,command= lambda i = text: show(i,master,root)).pack(anchor='center', padx = 10,ipadx=5,pady=20)        
    def add_into_order(self,cust_id,pro_id,quantity,root,cart_id):
        print("product id : ",pro_id)
        w = int(quantity.get())
        print("CUSTOMER : PRODUCT : quantity : ",cust_id,pro_id,w)
        MsgBox = tk.messagebox.askquestion ('ORDER PLACEMENT','Confirm "yes" to place order ')
        if MsgBox == 'yes' and w !=0:
            if cart_id == 0:
                cursor.execute("select * from cart")
                rows=cursor.fetchall()
                flag = 0
                max=0
                for row in rows:
                    print("cart id: ",row[0],"cust id : ",row[1])
                    if(max<row[0]):
                        max = row[0]
                    if(cust_id==row[1]):
                        print("THE SAME CUSTomer\t",'cart Id is :  ',row[0],'\t\tcust id : ',cust_id)
                        cart_id = row[0]
                        flag = 1
                if(flag==0):
                    cart_id = max + 1
                    print('\n\ncart Id is :  ',cart_id,'\t\tcust id : ',cust_id)
                    cart_query = """insert into cart(CART_ID, CUST_ID) values (%s,%s)"""
                    cursor.execute(cart_query,(cart_id,cust_id))
                    connection.commit()
            print('\n\ncart Id is :  ',cart_id,'\t\tcust id : ',cust_id)
            pro_list=[]
            pro_list.append(pro_id)
            obj = User()
            obj.order_generate(cust_id,pro_list,w,root,cart_id)#cust_id,root)
        else:
            if(w==0):
                print("Invalid quantity entry")
                messagebox.showinfo('Order Placement','Invalid quantity entry')
    def place_order(self,cust_id,pro_id,root,cart_id):
        print("product buyed by the customer")
        w = Spinbox(root,from_ = 0, to = 10, width=5) #create a Spinbox widget and we pass the from_ and to parameters to specify the numbers range for the Spinbox.
        w.pack(padx=10,pady=10)
        obj = User()
        print("product id : ",pro_id)
        Button(root,text='Place order',command = lambda : obj.add_into_order(cust_id,pro_id,w,root,cart_id)).pack(padx=10,pady=10)
    def add_into_product(self,cust_id,pro_id,root,cart_id):
        if cart_id==0:
            max=0
            cursor.execute("select * from cart")
            rows=cursor.fetchall()
            flag = 0
            for row in rows:
                if(max<row[0]):
                    max = row[0]
                if(cust_id==row[1]):
                    cart_id = row[0]
                    flag = 1
            if(flag==0):
                cart_id = max + 1
                cart_query = """insert into cart(CART_ID, CUST_ID) values (%s,%s)"""
                cursor.execute(cart_query,(cart_id,cust_id))
                connection.commit()
        work = 1
        if cart_id !=0 or work ==1:
            cursor.execute("select * from added_to")
            rows=cursor.fetchall()
            flag = 0
            for row in rows:
                if( pro_id == row[0] and (cart_id)==row[1]):
                    flag=1
            if(flag==0):
                pro_query = """insert into added_to(PRODUCT_ID, CART_ID) values (%s,%s)"""
                cursor.execute(pro_query,(pro_id,cart_id))
                connection.commit()
        messagebox.showinfo("INFORMATION","PRODUCT ADDED TO CART SUCCESSFULLY")
        key = Login()
        key.customer(root,cart_id,cust_id)

    def orders(self,cust_id,pro_id,pro_win,cart_id):
        print("its working")
    def user_check(self,username,password,pro_id,pro_win,num,root1,cart_id,cust_id):
        cursor.execute("select * from customer")
        rows = cursor.fetchall()
        print("user : ",username.get(),"password : ",password.get())
        flag=0
        obj=User()
        for row in rows:
            if((username.get())==row[6] and (password.get())==row[7]):
                flag = 1
                cust_id = row[0]
        if flag != 0:
            messagebox.showinfo("INFORMATION",'LOGIN SUCCESSFULL!!!!')
            if num==1:
                root1.destroy()
                obj.add_into_product(cust_id,pro_id,pro_win,cart_id)#,root1)#cust_id,pro_id,root,win
            elif num==2:
                root1.destroy()
                print(cust_id,pro_id,pro_win,cart_id)
                obj.place_order(cust_id,pro_id,pro_win,cart_id)
            elif num==3:
                root1.destroy()
                obj.cart(cust_id,pro_id,pro_win,cart_id)
            else:
                root1.destroy()
                obj.orders(cust_id,pro_id,pro_win,cart_id)
        else:
            messagebox.showerror("ERROR","INCORRECT USERNAME OR PASSWORD")
    def cart(self,cust_id,product_id,pro_win,cart_id):
        pro_win.destroy()
        print("cart_id",cart_id)
        query =(""" select p.PRODUCT_ID,p.P_NAME,p.pro_img,p.category,c.CART_ID from added_to a,cart c,product p where a.CART_ID = c.CART_ID and a.PRODUCT_ID=p.PRODUCT_ID and c.CUST_ID= %s""")
        cursor.execute(query,(cust_id,))
        rows = cursor.fetchall()
        print("cart invoked")
        root = Tk()
        obj_img = Image_Module()
        obj_img.rooticon(root)
        cust_obj = Customer_Module()
        obj_user=User()
        frame = cust_obj.search_frame(root)#search(win4,frame[1],cart_id,cust_id)
        Button(frame[0],width=30,compound=LEFT,image =frame[4],activebackground = "pink", activeforeground = "blue",command = lambda key = Login(): key.customer(root,cart_id,cust_id)).grid(row=0,column=0)
        Button(frame[0],width=70,text='SEARCH',compound=LEFT,image =frame[2],activebackground = "pink", activeforeground = "blue",command = lambda : cust_obj.search(root,frame[1],cart_id,cust_id)).grid(row=0,column=15)
        Button(frame[0],width=60,text='CART',compound=LEFT,command = lambda : obj_user.login_window(0,root,3,cart_id,cust_id),image =frame[3],activebackground = "pink", activeforeground = "blue").grid(row=0,column=20)
        Button(frame[0],text = 'ORDERS',width=70,compound=LEFT,image =frame[5],activebackground = "pink", activeforeground = "blue").grid(row=0,column=30)
        text = obj_img.initialimageposition(root)#pro_id,pro_win,num,cart_id,cust_id
        list1=[]
        k=1
        pro_list = []
        if rows !=[]:
            for row in rows:
                cart_id = row[4]
                pro_list.insert(k,row[0])
                obj_img.resize(row[2])
                photo= ImageTk.PhotoImage(Image.open(row[2]))
                list1.insert(k,photo)
                a = Button(root, text = row[1].upper(),image=photo,width=300,compound=TOP,font=('verdana',12),activebackground = "skyblue", activeforeground = "pink",command = lambda i=row[0]:cust_obj.product_details(root,i,cart_id,cust_id))
                if k%2==0:
                    obj_img.finalimageposition(text,a)
                else:
                    obj_img.finalimagetabposition(text,a)
                k = k+1
            b = Button(root,text = 'Buy All',command = lambda : buy_now(pro_list,cust_id,cart_id))
            obj_img.finalimageposition(text,b)
            text.configure(state="disabled")
        else:
            a = Label(root, text = "Your cart is empty")
            obj_img.finalimageposition(text,a)
            b = Button(root,text = 'Add products to carts',width=50,bg='yellow',command = lambda key = Login():key.customer(root,cart_id,cust_id))
            obj_img.finalimageposition(text,b)
        def buy_now(pro_list,cust_id,cart_id):
            obj = User()
            cursor.execute("delete from added_to where CART_ID = %s",(cart_id,))
            connection.commit()
            obj.order_generate(cust_id,pro_list,1,pro_win,cart_id)#cust_id,root)
            print("am checking")
            
        root.geometry("800x400")
        root.resizable(width=False, height=False)
        root.mainloop()
    def login_window(self,pro_id,pro_win,num,cart_id,cust_id):#0,root,3,cart_id,cust_id
        if cart_id == 0 and cust_id == 0:
            root = Tk()
            obj_user=User()
            frame = Frame(root,height=300)#bg='pink',
            frame.pack(side=TOP, pady=20) 
            Label(frame, text = "User Name:", font=('arial', 14), bd=15).grid(row=0, sticky="e")
            Label(frame, text = "Password : ", font=('arial', 14), bd=15).grid(row=1, sticky="e")
            username = Entry(frame, font=(14))
            username.grid(row=0, column=1)#,ipadx=25,ipady=25)
            password = Entry(frame, font=(14))
            password.grid(row=1, column=1)#,ipadx=25,ipady=25)
            btn1 = Button(frame, text="Login" ,command = lambda : obj_user.user_check(username,password,pro_id,pro_win,num,root,cart_id,cust_id),activebackground = "pink", activeforeground = "blue")
            btn1.grid(pady=25, row=4, columnspan=1)
            btn2 = Button(frame, text="New user ?" ,command = lambda : obj_user.new_user(pro_id,pro_win,num,root,cart_id,cust_id),activebackground = "pink", activeforeground = "blue")#, command = lambda : key.add_product(key1,frame,product,A_price,S_price,details,brd,cat,pro_img))
            btn2.grid(pady=25, row=4, columnspan=2)
            root.mainloop()
        else:
            obj=User()
            if num == 1:
                print("add to cart")
                obj.add_into_product(cust_id,pro_id,pro_win,cart_id)
            elif num == 2:
                obj.place_order(cust_id,pro_id,pro_win,cart_id)
                print("buy now")
            else:
                print("view cart")
                obj.cart(cust_id,pro_id,pro_win,cart_id)
    def add_user(self,fname,lname,email,phone,address,username,password,pro_id,pro_win,num,root1,cart_id,cust_id):
        obj=User()
        cursor.execute("select * from customer")
        rows = cursor.fetchall()
        max =0
        flag=0
        for row in rows:
            print(row[0],row[1],row[2])
            if(max<row[0]):
                max=row[0]
            if(row[6]==username.get()):
                messagebox.showerror("ERROR","USER NAME ALREADY EXISTS!!!!")
                flag=1
        if flag== 0:
            add_query=""" insert into customer(CUST_ID, FNAME, LNAME, EMAIL, PHONE, ADDRESS,USER_NAME,PASSWORD) values(%s,%s,%s,%s,%s,%s,%s,%s)"""
            svalues=((max+1),fname.get(),lname.get(),email.get(),phone.get(),address.get("1.0","end-1c"),username.get(),password.get())
            cursor.execute(add_query,svalues)
            connection.commit()
            messagebox.showinfo("INFORMATION","INFORMATION ADDED SUCCESSFULLY")
            if num==1:
                root1.destroy()
                cust_id = max+1
                obj.add_into_product(cust_id,pro_id,pro_win,cart_id)
            elif num == 2:
                root1.destroy()
                print("product buyed")
                cust_id = max+1
                obj.place_order(cust_id,pro_id,pro_win,cart_id)
            else:
                obj.cart(cust_id,pro_id,pro_win,cart_id)
    def new_user(self,pro_id,pro_win,num,root1,cart_id,cust_id):
        root1.destroy()
        win3=Tk()
        win3.title("NEW USER")
        obj_user = User()
        frame = Frame(win3,height=200)#bg='pink',
        frame.pack(side=TOP, pady=20) 
        Label(frame, text = "First Name:", font=('arial', 14), bd=15).grid(row=0, sticky="e")
        Label(frame, text = "Last Name : ", font=('arial', 14), bd=15).grid(row=1, sticky="e")
        Label(frame, text = "Email Id : ", font=('arial', 14), bd=15).grid(row=2, sticky="e")
        Label(frame, text = "Phone: ", font=('arial', 14), bd=15).grid(row=3, sticky="e")#,width=15,height=5)
        Label(frame, text = "Address :", font=('arial', 14), bd=15).grid(row=4, sticky="e")
        Label(frame, text = "User Name: ", font=('arial', 14), bd=15).grid(row=5, sticky="e")#,width=15,height=5)
        Label(frame, text = "Password:", font=('arial', 14), bd=15).grid(row=6, sticky="e")
        
        lbl_text = Label(frame)
        lbl_text.grid(row=10, columnspan=2)

        fname= Entry(frame,font=(14),width=20)
        fname.grid(row=0, column=1)

        lname =Entry(frame, font=(14))
        lname . grid(row=1, column=1)

        email=Entry(frame, font=(14))
        email. grid(row=2, column=1)
        
        phone = Entry(frame, font=(14))
        phone.grid(row=3, column=1)
        
        address = Text(frame, font=(14),height=5,width=25)
        address.grid(row=4, column=1)

        username = Entry(frame, font=(14))
        username.grid(row=5, column=1)

        password = Entry(frame, font=(14))
        password.grid(row=6, column=1)
        btn = Button(frame, text="ADD USER(Submit)" ,width=45,command = lambda : obj_user.add_user(fname,lname,email,phone,address,username,password,pro_id,pro_win,num,win3,cart_id,cust_id),activebackground = "pink", activeforeground = "blue")#, command = lambda : key.add_product(key1,frame,product,A_price,S_price,details,brd,cat,pro_img))
        btn.grid(pady=25, row=8, columnspan=2)
        win3.mainloop()
        del obj_user
    
class Customer_Module:
        def search_frame(self,root):
            frame = Frame(root,bg='#bebdb8')
            frame.pack(fill = BOTH,expand=True,side=TOP)
            s=Entry(frame,width=60, font=(14))
            s.grid(row=0,column=1)#pack(side=LEFT)
            search = ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\shopping\search.png"))
            cart = ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\shopping\cart1.jpg"))
            menu = ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\shopping\menu.png"))
            order = ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\shopping\order.png"))
            return frame,s,search,cart,menu,order
        def search_result(self,rows,cart_id,cust_id):
            win4 = Tk()
            obj_img = Image_Module()
            obj_img.rooticon(win4)
            cust_obj = Customer_Module()
            frame = cust_obj.search_frame(win4)
            obj_user = User()
            Button(frame[0],width=30,compound=LEFT,image =frame[4],activebackground = "pink", activeforeground = "blue",command = lambda key = Login(): key.customer(win4,cart_id,cust_id)).grid(row=0,column=0)
            Button(frame[0],width=70,text='SEARCH',compound=LEFT,image =frame[2],activebackground = "pink", activeforeground = "blue",command = lambda : cust_obj.search(win4,frame[1],cart_id,cust_id)).grid(row=0,column=15)
            Button(frame[0],width=60,text='CART',compound=LEFT,command = lambda : obj_user.login_window(0,win4,3,cart_id,cust_id),image =frame[3],activebackground = "pink", activeforeground = "blue").grid(row=0,column=20)
            Button(frame[0],text = 'ORDERS',width=70,compound=LEFT,image =frame[5],activebackground = "pink", activeforeground = "blue").grid(row=0,column=30)
            text = obj_img.initialimageposition(win4)
            list1 =[]
            k=1
            for row in rows:
                obj_img.resize(row[6])
                photo= ImageTk.PhotoImage(Image.open(row[6]))
                list1.insert(k,photo)
                a = Button(win4, text = row[2].upper(),image=photo,width=300,command = lambda i=row[0]:cust_obj.product_details(win4,i,cart_id,cust_id),font=('verdana',12),compound=TOP,activebackground = "skyblue", activeforeground = "pink")#,command = lambda i=row[2].upper():del_pro(i))#,command = lambda i=pro_name.upper(): action(i))#.grid(row=rowsize, column=10, padx=padxsize, pady=padysize)
                if k%2==0:
                    obj_img.finalimageposition(text,a)
                else:
                    obj_img.finalimagetabposition(text,a)
                k = k+1
            text.configure(state="disabled")
            win4.geometry("800x400")
            win4.resizable(width=False, height=False)
            win4.mainloop()
            del list1
        def search(self,win,var,cart_id,cust_id):
            variable = var.get()
            query="""select * from product p,brand b WHERE p.BRD_ID=b.BRD_ID and ((p.P_NAME LIKE  %s or p.category like %s) or (b.BRD_NAME like %s))"""
            values=(("%"+variable+"%"),("%"+variable+"%"),("%"+variable+"%"),)
            cursor.execute(query,values)
            rows = cursor.fetchall()
            if rows !=[]:
                win.destroy()
                cust_obj = Customer_Module()
                cust_obj.search_result(rows,cart_id,cust_id)
            else:
                messagebox.showinfo('INFORMATION',"YOUR SEARCH DID NOT MATCH ANY PRODUCTS")
        def category_view(self,root,cart_id,cust_id):
            obj_img = Image_Module()
            obj_img.rooticon(root)
            text = obj_img.initialimageposition(root)
            cursor.execute("""select distinct category,cat_img from category""")
            rows = cursor.fetchall()
            list1=[]
            k=1
            cust_obj = Customer_Module()
            for row in rows:
                obj_img.resize(row[1])
                photo= ImageTk.PhotoImage(Image.open(row[1]))                                                                                                          
                list1.insert(k,photo)
                a = Button(root, text = row[0].upper(),relief = RIDGE,image=photo,width=300,compound=TOP,font=('verdana',12),activebackground = "skyblue", activeforeground = "pink",command = lambda i=row[0].upper():cust_obj.cat_specific(i,root,cart_id,cust_id))
                if k%2==0:
                    obj_img.finalimageposition(text,a)
                else:
                    obj_img.finalimagetabposition(text,a)
                k = k+1
            text.configure(state="disabled")
            root.geometry("800x400")
            root.resizable(width=False, height=False)
            root.mainloop()
        def product_details(self,win,pro_id,cart_id,cust_id):
            cursor.execute("""select * from product""")
            rows = cursor.fetchall()
            flag = 0
            for row in rows:
                if(pro_id==row[0] and row[7]!=0):
                    win.destroy()
                    root = Tk()
                    flag=1
                    cust_obj = Customer_Module()
                    obj_img = Image_Module()
                    obj_img.rooticon(root)
                    frame = cust_obj.search_frame(root)
                    Button(frame[0],width=30,compound=LEFT,image =frame[4],activebackground = "pink", activeforeground = "blue",command = lambda key = Login(): key.customer(root,cart_id,cust_id)).grid(row=0,column=0)
                    Button(frame[0],width=80,text='SEARCH',compound=LEFT,image =frame[2],activebackground = "pink", activeforeground = "blue",command = lambda : cust_obj.search(root,frame[1],cart_id,cust_id)).grid(row=0,column=15)
                    Button(frame[0],width=80,text='CART',compound=LEFT,command = lambda : obj_user.login_window(0,root,3,cart_id,cust_id),image =frame[3],activebackground = "pink", activeforeground = "blue").grid(row=0,column=20)
                    Button(frame[0],text = 'ORDERS',width=90,compound=LEFT,image =frame[5],activebackground = "pink", activeforeground = "blue").grid(row=0,column=30)
                    print("THE SELECTED PRODUCT IS : ",row[2])
                    obj_img.resize(row[6])
                    photo= ImageTk.PhotoImage(Image.open(row[6]))

                    bottomframe = Frame(root)
                    bottomframe.pack(side=BOTTOM)
                    obj_user = User()
                    Button(bottomframe, text="ADD TO CART", bg="orange",width=60,command = lambda : obj_user.login_window(pro_id,root,1,cart_id,cust_id)).pack(side=LEFT)
                    Button(bottomframe, text="BUY NOW", bg="orangered",width=60,command = lambda : obj_user.login_window(pro_id,root,2,cart_id,cust_id)).pack(side=RIGHT)#obj_user.cart(pro_id,root,1)

                    leftframe = Frame(root,bg='skyblue')
                    leftframe.pack(side=LEFT)
                    Label(leftframe,text=row[2].upper(),image=photo,compound=TOP).pack(side=LEFT)    

                    text2 = tk.Text(root, height=20, width=50)
                    scroll = tk.Scrollbar(root, command=text2.yview)
                    text2.configure(yscrollcommand=scroll.set)
                    text2.pack(side=tk.LEFT)
                    ap=row[3]
                    scroll.pack(side=tk.RIGHT, fill=tk.Y)
                    obj_img.productposition(text2,"PRODUCT NAME : "+row[2])
                    obj_img.productposition(text2,"PRODUCT DETAILS :\n "+row[5])
                    text2.insert(tk.END,"ACTUAL PRODUCT PRICE : \t")
                    text2.insert(tk.END, '\t\t')                                                
                    text2.insert(tk.END,row[3])
                    text2.insert(tk.END, '\n\n')
                    text2.insert(tk.END,"SELLING PRODUCT PRICE : \t")
                    text2.insert(tk.END, '\t\t')                                                
                    text2.insert(tk.END,row[4])
                    text2.insert(tk.END, '\n\n')
                    obj_img.productposition(text2,"PRODUCT CATEGORY : "+row[8])
                    cursor.execute("select * from brand where BRD_ID = %s",(row[1],))
                    brd = cursor.fetchall()
                    print(brd)
                    for i in brd:
                        obj_img.productposition(text2,"BRAND : "+i[1])
                    r_query=("""select p.PRODUCT_ID,p.P_NAME,c.FNAME,c.LNAME,r.details from customer c,reviews r,product p
                                    where r.CUST_ID=c.CUST_ID and r.PRODUCT_ID=p.PRODUCT_ID and p.PRODUCT_ID= %s""" )
                    cursor.execute(r_query,(pro_id,))
                    reviews = cursor.fetchall()
                    print(reviews)
                    a = Label(root,text="Reviews",bg='tan',width=50)
                    obj_img.finalimageposition(text2,a)
                    for i in reviews:
                        text2.insert(tk.END,(i[2]))
                        text2.insert(tk.END, '\t\t')                                                
                        text2.insert(tk.END,i[4])
                        text2.insert(tk.END, '\n\n')
                        
            if flag==0:
                messagebox.showinfo('INFORMATION','PRODUCT OUT OF STOCK')
                #root = Tk()
                key = Login()
                key.customer(win)
            else:
                text2.configure(state="disabled")
                root.geometry("850x380")
                root.resizable(width=False, height=False)
                root.mainloop()
        def cat_specific(self,cat_name,win,cart_id,cust_id):
            win.destroy()
            root = Tk()
            obj_img = Image_Module()
            obj_img.rooticon(root)
            cust_obj = Customer_Module()
            obj_user=User()
            frame = cust_obj.search_frame(root)
            Button(frame[0],width=30,compound=LEFT,image =frame[4],activebackground = "pink", activeforeground = "blue",command = lambda key = Login(): key.customer(root,cart_id,cust_id)).grid(row=0,column=0)
            Button(frame[0],width=70,text='SEARCH',compound=LEFT,image =frame[2],activebackground = "pink", activeforeground = "blue",command = lambda : cust_obj.search(root,frame[1],cart_id,cust_id)).grid(row=0,column=15)
            Button(frame[0],width=60,text='CART',compound=LEFT,command = lambda : obj_user.login_window(0,root,3,cart_id,cust_id),image =frame[3],activebackground = "pink", activeforeground = "blue").grid(row=0,column=20)
            Button(frame[0],text = 'ORDERS',width=70,compound=LEFT,image =frame[5],activebackground = "pink", activeforeground = "blue").grid(row=0,column=30)
            text = obj_img.initialimageposition(root)
            list1=[]
            k=1
            query =(""" select p.PRODUCT_ID,p.P_NAME,p.pro_img from product p,category c where p.BRD_ID = c.BRD_ID and p.category=c.category and p.category = %s  """)
            cursor.execute(query,(cat_name,))
            rows = cursor.fetchall()
            for row in rows:
                obj_img.resize(row[2])
                photo= ImageTk.PhotoImage(Image.open(row[2]))
                list1.insert(k,photo)
                a = Button(root, text = row[1].upper(),image=photo,width=300,compound=TOP,font=('verdana',12),activebackground = "skyblue", activeforeground = "pink",command = lambda i=row[0]:cust_obj.product_details(root,i,cart_id,cust_id))
                if k%2==0:
                    obj_img.finalimageposition(text,a)
                else:
                    obj_img.finalimagetabposition(text,a)
                k = k+1
            text.configure(state="disabled")
            root.geometry("800x400")
            root.resizable(width=False, height=False)
            root.mainloop()    
            print("category specific products",cat_name)

class Login:
    def show(self,key,password,win):
                value=password.get()
                if(value=='admin'):
                    messagebox.showinfo("INFORMATION","Login Successfull!!!")
                    win.destroy()
                    del key
                    key1= Admin_Module()
                    key1.gotomenu()
                else:
                    messagebox.showwarning("WARNING","WRONG PASSWORD!!!!")   
    def admin(self,key,root):
            root.destroy()
            win = Tk()
            obj_img = Image_Module()
            obj_img.rooticon(win)
            frame = Frame(win)#,bg='skyblue')
            Label(frame,text='Password',font=('verdana',12),width=20).pack(padx=25,pady=25)
            e1 = Entry(frame,show ="*",width=20)
            e1.pack(padx=10,pady=10)
            frame.pack(fill = BOTH,expand=True,anchor='center')
            Button(frame,text='SUBMIT',command = lambda : key.show(key,e1,win),activebackground = "pink", activeforeground = "blue").pack(padx=10,pady=10)
            win.mainloop()
  
    def customer(self,key,cart_id,cust_id):
            key.destroy()
            print("customer")
            print(cart_id,cust_id)
            root = Tk()
            obj = Customer_Module()
            obj_user = User()
            frame = obj.search_frame(root)
            Button(frame[0],width=30,compound=LEFT,image =frame[4],activebackground = "pink", activeforeground = "blue",command = lambda key = Login(): key.customer(root,cart_id,cust_id)).grid(row=0,column=0)
            Button(frame[0],width=70,text='SEARCH',compound=LEFT,image =frame[2],activebackground = "pink", activeforeground = "blue",command = lambda : obj.search(root,frame[1],cart_id,cust_id)).grid(row=0,column=15)
            Button(frame[0],width=60,text='CART',compound=LEFT,command = lambda : obj_user.login_window(0,root,3,cart_id,cust_id),image =frame[3],activebackground = "pink", activeforeground = "blue").grid(row=0,column=20)
            Button(frame[0],text = 'ORDERS',width=70,compound=LEFT,command = lambda : obj_user.login_window(0,root,4,cart_id,cust_id),image =frame[5],activebackground = "pink", activeforeground = "blue").grid(row=0,column=30)
            obj.category_view(root,cart_id,cust_id)           
root = Tk()
obj_img = Image_Module()
obj_img.rooticon(root)
frame = Frame(root,bg='pink')
frame.pack(anchor='center',fill = BOTH,expand=True,side=TOP)
Label(frame,text="WELCOME TO E-ZONE ELECTRONICS SHOPPING ",font=('Lucida Calligraphy',14,'bold')).pack(padx=10,pady=10)
photo= ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\shopping\shoppingicon.png"))
key = Login()
cart_id = 0
cust_id = 0
b = Frame(root,bg='pink')
b.pack(anchor='center',fill = BOTH,expand=True,side=BOTTOM)
Label(frame,image=photo).pack(anchor='center')
Button(b,text='ADMIN',width=20,command = lambda : key.admin(key,root),activebackground = "pink", activeforeground = "blue",font=('verdana',12,'bold')).pack(padx=10,pady=10)
Button(b,text='CUSTOMER',width=20,command= lambda : key.customer(root,cart_id,cust_id),font=('verdana',12,'bold'),activebackground = "pink", activeforeground = "blue").pack(padx=10,pady=10)#,pady=10)#,pady=20)
root.geometry('700x520')
root.resizable(width=False, height=False)
mainloop()
if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


