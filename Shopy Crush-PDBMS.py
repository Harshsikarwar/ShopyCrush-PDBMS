from tkinter import*
import os
import csv
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import DBMS_Graph

w=Tk()

w.title("Shopy Crush")
w.minsize(height=550,width=850)

data=[]

dic=os.path.dirname(__file__)
dic.replace("\\","\\\\")

icon=PhotoImage(file=dic+"\\icon.png")
w.iconphoto(True,icon)

file_path=dic+"\\shopy crush prod.csv"
csv_file_r=open(file_path,'r')
csv_read=csv.reader(csv_file_r)

for row in csv_read:
    if row != [] and row != ['', '', '', '', '', '', '', '']:
        data.append(row)
menu_lbl=Label(w,text="Main Menu",font=("Helvatica",24,"bold"),fg="#633974",bg="#ffffff",bd=0)
menu_lbl.pack(side=TOP, fill=BOTH)

#Add Products
def add_products():
    adding_data=[]
    def back_command():
        menu_lbl.config(text="Main Menu")
        row_frame.destroy()
        data_frame.destroy()
        Main_menu()
    def add_command():
        
        adding_data=[Sno_box.get(),pname_box.get(),type_box.get(),material_box.get(),supplier_box.get(),sup_price_box.get(),sell_price_box.get(),profit_box.get()]
        if "" in adding_data:
            messagebox.showwarning("Shopy Crush - Product Adding","Any entry is not fill!")
            adding_data.clear()
        else:
            csv_file_a=open(file_path,'a+')
            csvwrite=csv.writer(csv_file_a)
            csvwrite.writerow(adding_data)
            csv_file_r=open(file_path,'r')
            csv_read=csv.reader(csv_file_r)
            data.clear()
            for row in csv_read:
                if row !=[] and row != ['', '', '', '', '', '', '', '']:
                    data.append(row)
            adding_data.clear()
            Sno_box.delete(0,END),pname_box.delete(0,END),type_box.delete(0,END),material_box.delete(0,END),supplier_box.delete(0,END),sup_price_box.delete(0,END),sell_price_box.delete(0,END),profit_box.delete(0,END)
            index=int(len(data))+1
            Sno_box.insert(0,str(index))
            messagebox.showinfo("Shopy Crush - Product Adding","Product data added succesfully.")

    menu_lbl.config(text="Add Product")
    row_frame=Frame(w,bd=0,container=False)
    row_frame.pack(side=LEFT,fill=BOTH)

    data_frame=Frame(w,bd=0,container=False)
    data_frame.pack(side=TOP,fill=BOTH,padx=10)

    #TITLE AND ACTION BUTTONS OF ADDING

    sno_lbl=Label(row_frame,text="Sno.",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    sno_lbl.pack(side=TOP,fill=X,pady=10)

    p_name_lbl=Label(row_frame,text="Product Name",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    p_name_lbl.pack(side=TOP,fill=X,pady=5)

    type_lbl=Label(row_frame,text="Type",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    type_lbl.pack(side=TOP,fill=X,pady=10)

    material_lbl=Label(row_frame,text="Material",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    material_lbl.pack(side=TOP,fill=X,pady=5)

    supplier_lbl=Label(row_frame,text="Supplier",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    supplier_lbl.pack(side=TOP,fill=X,pady=10)
    
    sup_price_lbl=Label(row_frame,text="Supplier Price",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    sup_price_lbl.pack(side=TOP,fill=X,pady=5)

    sell_price_lbl=Label(row_frame,text="Selling Price",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    sell_price_lbl.pack(side=TOP,fill=X,pady=10)

    profit_lbl=Label(row_frame,text="Profit",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    profit_lbl.pack(side=TOP,fill=X,pady=5)

    back_btn=Button(row_frame,text="Back",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=back_command)
    back_btn.pack(side=BOTTOM,fill=X,pady=10)

    add_btn=Button(row_frame,text="Add",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=add_command)
    add_btn.pack(side=BOTTOM,fill=X,pady=10)

    #DATA ENTRY OF ADDING

    Sno_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    Sno_box.pack(side=TOP,fill=X,pady=8)
    index=int(len(data))
    Sno_box.insert(0,str(index))

    pname_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    pname_box.pack(side=TOP,fill=X,pady=3)

    type_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    type_box.pack(side=TOP,fill=X,pady=8)

    material_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    material_box.pack(side=TOP,fill=X,pady=3)

    supplier_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    supplier_box.pack(side=TOP,fill=X,pady=8)

    sup_price_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    sup_price_box.pack(side=TOP,fill=X,pady=3)

    sell_price_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    sell_price_box.pack(side=TOP,fill=X,pady=8)

    profit_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    profit_box.pack(side=TOP,fill=X,pady=3)

#edit Products
def edit_products():
    def back_command():
        menu_lbl.config(text="Main Menu")
        row_frame.destroy()
        data_frame.destroy()
        sno_frame.destroy()
        Main_menu()
    def ok_command():
        sno=Sno_box.get()
        if sno==str:
            messagebox.showwarning("Shopy Crush - Edit Products","Sno should be numeric!")
        elif sno=="":
            messagebox.showwarning("Shopy Crush - Edit Products","Enter Sno!")
        #elif sno>str(len(data)-1):
        #    messagebox.showwarning("Shopy Crush - Edit Products","Invalid serial number!")
        else:
            try:
                show_data=data[int(sno)]
                pname_box.delete(0,END),type_box.delete(0,END),material_box.delete(0,END),supplier_box.delete(0,END),sup_price_box.delete(0,END),sell_price_box.delete(0,END),profit_box.delete(0,END)
                pname_box.insert(0,show_data[1]),type_box.insert(0,show_data[2]),material_box.insert(0,show_data[3]),supplier_box.insert(0,show_data[4]),sup_price_box.insert(0,show_data[5]),sell_price_box.insert(0,show_data[6]),profit_box.insert(0,show_data[7])
            except IndexError:
                messagebox.showwarning("Shopy Crush - Edit Products","Invalid serial number!")
    def edit_command():
        sno=Sno_box.get()
        if sno==str:
            messagebox.showwarning("Shopy Crush - Edit Products","Sno should be numeric!")
        elif sno=="":
            messagebox.showwarning("Shopy Crush - Edit Products","Enter Sno!")
        else:
            editing_data=[Sno_box.get(),pname_box.get(),type_box.get(),material_box.get(),supplier_box.get(),sup_price_box.get(),sell_price_box.get(),profit_box.get()]
            data.pop(int(sno))
            data.insert(int(sno),editing_data)
            csv_file_w=open(file_path,"w")
            csvwriter=csv.writer(csv_file_w)
            csvwriter.writerows(data)
            pname_box.delete(0,END),type_box.delete(0,END),material_box.delete(0,END),supplier_box.delete(0,END),sup_price_box.delete(0,END),sell_price_box.delete(0,END),profit_box.delete(0,END)
    menu_lbl.config(text="Edit Product")
    row_frame=Frame(w,bd=0,container=False)
    row_frame.pack(side=LEFT,fill=BOTH)
    sno_frame=Frame(w,bd=0,container=False)
    sno_frame.pack(side=TOP,fill=BOTH,padx=10)
    data_frame=Frame(w,bd=0,container=False)
    data_frame.pack(side=TOP,fill=BOTH,padx=10)

    #TITLE AND ACTION BUTTONS OF EDIT
    
    sno_lbl=Label(row_frame,text="Enter Sno.",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    sno_lbl.pack(side=TOP,fill=X,pady=10)

    p_name_lbl=Label(row_frame,text="Product Name",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    p_name_lbl.pack(side=TOP,fill=X,pady=5)

    type_lbl=Label(row_frame,text="Type",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    type_lbl.pack(side=TOP,fill=X,pady=10)

    material_lbl=Label(row_frame,text="Material",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    material_lbl.pack(side=TOP,fill=X,pady=5)

    supplier_lbl=Label(row_frame,text="Supplier",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    supplier_lbl.pack(side=TOP,fill=X,pady=10)
    
    sup_price_lbl=Label(row_frame,text="Supplier Price",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    sup_price_lbl.pack(side=TOP,fill=X,pady=5)

    sell_price_lbl=Label(row_frame,text="Selling Price",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    sell_price_lbl.pack(side=TOP,fill=X,pady=10)

    profit_lbl=Label(row_frame,text="Profit",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
    profit_lbl.pack(side=TOP,fill=X,pady=5)

    back_btn=Button(row_frame,text="Back",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=back_command)
    back_btn.pack(side=BOTTOM,fill=X,pady=10)

    edit_btn=Button(row_frame,text="Edit",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=edit_command)
    edit_btn.pack(side=BOTTOM,fill=X,pady=10)

    #DATA ENTRY OF EDIT

    Sno_box=Entry(sno_frame,bd=2,font=("Helvatica",18,"bold"))
    Sno_box.pack(side=LEFT,fill=X,pady=8)
    ok_btn=Button(sno_frame,text="Ok",font=("Helvatica",16,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=ok_command)
    ok_btn.pack(side=LEFT,fill=X,pady=3)

    pname_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    pname_box.pack(side=TOP,fill=X,pady=3)

    type_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    type_box.pack(side=TOP,fill=X,pady=8)

    material_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    material_box.pack(side=TOP,fill=X,pady=3)

    supplier_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    supplier_box.pack(side=TOP,fill=X,pady=8)

    sup_price_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    sup_price_box.pack(side=TOP,fill=X,pady=3)

    sell_price_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    sell_price_box.pack(side=TOP,fill=X,pady=8)

    profit_box=Entry(data_frame,bd=2,font=("Helvatica",18,"bold"))
    profit_box.pack(side=TOP,fill=X,pady=3)

#Products Sheet
def products_sheet():
    sorting=data
    def back_command():
        menu_lbl.config(text="Main Menu")
        sheet_frame.destroy()
        btn_frame.destroy()
        Main_menu()
    def bar_graph_command():
        DBMS_Graph.bar_graph()
    def pie_chart_command():
        DBMS_Graph.pie_chart()
    def histo_graph_command():
        DBMS_Graph.histo_graph()

    menu_lbl.config(text="Product Sheet")
    sheet_frame=Frame(w,bd=0,bg="#633974",container=False)
    sheet_frame.pack(fill=BOTH,padx=20,pady=20)
    tree_frame=Frame(sheet_frame,bd=0,bg="#633974",container=False)
    tree_frame.pack(side=TOP,fill=BOTH,padx=10,pady=10)
    scrl_frame=Frame(sheet_frame,bd=0,bg="#f3f3f3",container=False)
    scrl_frame.pack(side=TOP,fill=BOTH,padx=10,pady=10)
    btn_frame=Frame(w,bd=0,bg="#633974",container=False)
    btn_frame.pack(fill=BOTH,padx=20,pady=20)

    prod_data_sheet=ttk.Treeview(tree_frame,selectmode='browse')
    prod_data_sheet.pack(side=TOP,fill=BOTH)
    scrlbar=ttk.Scrollbar(scrl_frame,orient='horizontal',command=prod_data_sheet.yview)
    scrlbar.pack(side=TOP,fill=X,padx=5,pady=5)
    prod_data_sheet.config(xscrollcommand=scrlbar.set)
    style=ttk.Style()
    style.theme_use("default")
    style.configure('Treeview',background="white",rowheight=30)
    prod_data_sheet.tag_configure('evenrow',background="lightblue")
    prod_data_sheet.tag_configure('oddrow',background="white")

    prod_data_sheet["columns"]=("1","2","3","4","5","6","7","8")
    prod_data_sheet['show']='headings'

    prod_data_sheet.column("1",width=90,anchor='c'),prod_data_sheet.column("2",width=90,anchor='c'),prod_data_sheet.column("3",width=90,anchor='c'),prod_data_sheet.column("4",width=90,anchor='c'),prod_data_sheet.column("5",width=90,anchor='c'),prod_data_sheet.column("6",width=90,anchor='c'),prod_data_sheet.column("7",width=90,anchor='c'),prod_data_sheet.column("8",width=90,anchor='c')
    prod_data_sheet.heading("1",text="Sno."),prod_data_sheet.heading("2",text="Product Name"),prod_data_sheet.heading("3",text="Type"),prod_data_sheet.heading("4",text="Material"),prod_data_sheet.heading("5",text="Supplier"),prod_data_sheet.heading("6",text="Supplier Price"),prod_data_sheet.heading("7",text="Selling Price"),prod_data_sheet.heading("8",text="Profit")

    row_no=1
    n=1
    count=0
    for insertor in range(len(sorting)-1):
        if count%2==0:
            prod_data_sheet.insert("",'end',text="L"+str(n),values=(sorting[row_no][0],sorting[row_no][1],sorting[row_no][2],sorting[row_no][3],sorting[row_no][4],sorting[row_no][5],sorting[row_no][6],sorting[row_no][7]),tags=('evenrow',))
        else:
            prod_data_sheet.insert("",'end',text="L"+str(n),values=(sorting[row_no][0],sorting[row_no][1],sorting[row_no][2],sorting[row_no][3],sorting[row_no][4],sorting[row_no][5],sorting[row_no][6],sorting[row_no][7]),tags=('oddrow',))
        row_no+=1
        n+=1
        count+=1
    
    bar_graph_btn=Button(btn_frame,text="Bar Graph",font=("Helvatica",18,"bold"),bg="#f3f3f3",fg="#633974",bd=0,activebackground="#CBC3E3",activeforeground="white",command=bar_graph_command)
    bar_graph_btn.pack(side=LEFT,pady=10,padx=10)

    pie_graph_btn=Button(btn_frame,text="Pie Chart",font=("Helvatica",18,"bold"),bg="#f3f3f3",fg="#633974",bd=0,activebackground="#CBC3E3",activeforeground="white",command=pie_chart_command)
    pie_graph_btn.pack(side=LEFT,pady=10,padx=10)

    histo_graph_btn=Button(btn_frame,text="Histogram Graph",font=("Helvatica",18,"bold"),bg="#f3f3f3",fg="#633974",bd=0,activebackground="#CBC3E3",activeforeground="white",command=histo_graph_command)
    histo_graph_btn.pack(side=LEFT,pady=10,padx=10)

    back_btn=Button(btn_frame,text="Back",font=("Helvatica",18,"bold"),bg="#f3f3f3",fg="#633974",bd=0,activebackground="#CBC3E3",activeforeground="white",command=back_command)
    back_btn.pack(side=RIGHT,pady=10,padx=10)
    
#Visit_Website
def visit_website():
    webbrowser.Chrome()
    webbrowser.open("https:\\shopycrush.com")

#Visit_Website
def visit_shopify_website():
    webbrowser.Chrome()
    webbrowser.open("https://admin.shopify.com/store/c42d1d-2?new_store_login=true")

#Main Menu Options
def Main_menu():
    def add_products_command():
        add_prod.destroy()
        edit_prod.destroy()
        prod_sheet.destroy()
        visit_site.destroy()
        visit_shopify_btn.destroy()
        add_products()

    def edit_products_command():
        add_prod.destroy()
        edit_prod.destroy()
        prod_sheet.destroy()
        visit_site.destroy()
        visit_shopify_btn.destroy()
        edit_products()

    def products_sheet_command():
        add_prod.destroy()
        edit_prod.destroy()
        prod_sheet.destroy()
        visit_site.destroy()
        visit_shopify_btn.destroy()
        products_sheet()

    def visit_site_command():
        visit_website()

    def visit_shopify_command():
        visit_shopify_website()

    add_prod=Button(w,text="Add Product",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=add_products_command)
    add_prod.pack(side=TOP,fill=BOTH,padx=100,pady=50)

    edit_prod=Button(w,text="Edit Product",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=edit_products_command)
    edit_prod.pack(side=TOP,fill=BOTH,padx=100)

    prod_sheet=Button(w,text="Product Sheet",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=products_sheet_command)
    prod_sheet.pack(side=TOP,fill=BOTH,padx=100,pady=50)

    visit_site=Button(w,text="Visit Site",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=visit_site_command)
    visit_site.pack(side=TOP,fill=BOTH,padx=100)

    visit_shopify_btn=Button(w,text="Visit Shopify",font=("Helvatica",18,"bold"),bg="#633974",fg="#f3f3f3",bd=0,activebackground="#CBC3E3",activeforeground="white",command=visit_shopify_command)
    visit_shopify_btn.pack(side=TOP,fill=BOTH,padx=100,pady=50)

#developer
dev_lbl=Label(w,text="HRS Developer's, all copyright reserved.",font=("Helvatica",16,"bold"),bg="#633974",fg="#f3f3f3",bd=0)
dev_lbl.pack(side=BOTTOM,fill=X)

Main_menu()
w.mainloop()