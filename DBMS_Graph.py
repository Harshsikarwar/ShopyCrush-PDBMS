from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt
import os
import csv

data=[]

dic=os.path.dirname(__file__)
dic.replace("\\","\\\\")

file_path=dic+"\\shopy crush prod.csv"
csv_file_r=open(file_path,'r')
csv_read=csv.reader(csv_file_r)

for row in csv_read:
    if row != [] and row != ['', '', '', '', '', '', '', '']:
        data.append(row)

def bar_graph():
    screen=Tk()
    screen.geometry("600x320")
    screen.resizable(width=False,height=False)
    screen.title("Shopy Crush - PDBMS - Graph Screen")

    graph_lbl=Label(screen,text="Bar Graph",fg="#633974",bg="#ffffff",bd=0,font=("Helvaica",20,"bold"))
    graph_lbl.pack(side=TOP,fill=X)

    def create_command():
        x=[]
        data_x=[]
        y=[]
        n=1
        x_get=x_values_box.get()
        y_get=y_values_box.get()
        if x_get == "Suppliers" and y_get == "Products Quantity From Per Suppliers":
            x.clear()
            data_x.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][4] not in x:
                    x.append(data[n][4])
                data_x.append(data[n][4])
                n+=1
            for j in range(len(x)):
                y.append(data_x.count(x[j]))
            plt.bar(x,y,color="#633974",width=0.72,label="Quantity")
            plt.xlabel("Suppliers Name")
            plt.ylabel("Product Quantity")
            plt.title("Products Per Supplier Graph")
            plt.legend()
            plt.show()
        
        elif x_get == "Material" and y_get == "Material Quantity":
            x.clear()
            data_x.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][3] not in x:
                    x.append(data[n][3])
                data_x.append(data[n][3])
                n+=1
            for j in range(len(x)):
                y.append(data_x.count(x[j]))
            plt.bar(x,y,color="#633974",width=0.72,label="Quantity")
            plt.xlabel("Material Name")
            plt.ylabel("Material Quantity")
            plt.title("Products Per Supplier Graph")
            plt.legend()
            plt.show()
        elif x_get == "Product Type" and y_get == "Product Type Quantity":
            x.clear()
            data_x.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][2] not in x:
                    x.append(data[n][2])
                data_x.append(data[n][2])
                n+=1
            for j in range(len(x)):
                y.append(data_x.count(x[j]))
            plt.bar(x,y,color="#633974",width=0.72,label="Quantity")
            plt.xlabel("Product Type Name")
            plt.ylabel("Product Type Quantity")
            plt.title("Products Per Supplier Graph")
            plt.legend()
            plt.show()
        
        else:
            messagebox.showwarning("Shopy Crush - PDBMS - Graph","Unable to plot graph with this data.")
    plot_frame=Frame(screen,bg="#633974",bd=0,container=False)
    plot_frame.pack(side=TOP,fill=X,padx=10,pady=10)

    x_values_lbl=Label(plot_frame,text="Select X-axis value",font=("Helvatica",12,"bold"),bg="#f3f3f3",fg="#633974",bd=0)
    x_values_lbl.pack(side=TOP,padx=10,pady=10,fill=X)

    x_values_box=ttk.Combobox(plot_frame,value=["Suppliers","Material","Product Type"],font=("Helvatica",12,"bold"))
    x_values_box.pack(side=TOP,padx=10,pady=10,fill=X)

    y_values_lbl=Label(plot_frame,text="Select Y-axis value",font=("Helvatica",12,"bold"),bg="#f3f3f3",fg="#633974",bd=0)
    y_values_lbl.pack(side=TOP,padx=10,pady=10,fill=X)

    y_values_box=ttk.Combobox(plot_frame,value=["Products Quantity From Per Suppliers","Material Quantity","Product Type Quantity"],font=("Helvatica",12,"bold"))
    y_values_box.pack(side=TOP,padx=10,pady=10,fill=X)

    create_graph_btn=Button(plot_frame,text="Create Graph",font=("Helvatica",12,"bold"),fg="#633974",bg="#f3f3f3",activebackground="#CBC3E3",activeforeground="white",bd=0,command=create_command)
    create_graph_btn.pack(side=BOTTOM,fill=X,padx=10,pady=30)


    screen.mainloop()

def pie_chart():
    screen=Tk()
    screen.geometry("600x320")
    screen.resizable(width=False,height=False)
    screen.title("Shopy Crush - PDBMS - Graph Screen")

    graph_lbl=Label(screen,text="Pie Chart",fg="#633974",bg="#ffffff",bd=0,font=("Helvaica",20,"bold"))
    graph_lbl.pack(side=TOP,fill=X)

    def create_command():
        l=[]
        data_l=[]
        s=[]
        n=1
        label_get=x_values_box.get()
        size_get=y_values_box.get()
        if label_get == "Suppliers" and size_get == "Products Quantity From Per Suppliers":
            l.clear()
            data_l.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][4] not in l:
                    l.append(data[n][4])
                data_l.append(data[n][4])
                n+=1
            for j in range(len(l)):
                s.append(data_l.count(l[j]))
            plt.pie(s,labels=l,autopct="%1.1f%%",startangle=90)
            plt.title("Products Per Supplier Graph")
            plt.legend()
            plt.show()
        
        elif label_get == "Material" and size_get == "Material Quantity":
            l.clear()
            data_l.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][3] not in l:
                    l.append(data[n][3])
                data_l.append(data[n][3])
                n+=1
            for j in range(len(l)):
                s.append(data_l.count(l[j]))
            plt.pie(s,labels=l,autopct="%1.1f%%",startangle=90)
            plt.title("Products Per Supplier Graph")
            plt.legend()
            plt.show()
        elif label_get == "Product Type" and size_get == "Product Type Quantity":
            l.clear()
            data_l.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][2] not in l:
                    l.append(data[n][2])
                data_l.append(data[n][2])
                n+=1
            for j in range(len(l)):
                s.append(data_l.count(l[j]))
            plt.pie(s,labels=l,autopct="%1.1f%%",startangle=90)
            plt.title("Products Per Supplier Graph")
            plt.legend()
            plt.show()
        
        else:
            messagebox.showwarning("Shopy Crush - PDBMS - Graph","Unable to plot graph with this data.")
    plot_frame=Frame(screen,bg="#633974",bd=0,container=False)
    plot_frame.pack(side=TOP,fill=X,padx=10,pady=10)

    x_values_lbl=Label(plot_frame,text="Select label value",font=("Helvatica",12,"bold"),bg="#f3f3f3",fg="#633974",bd=0)
    x_values_lbl.pack(side=TOP,padx=10,pady=10,fill=X)

    x_values_box=ttk.Combobox(plot_frame,value=["Suppliers","Material","Product Type"],font=("Helvatica",12,"bold"))
    x_values_box.pack(side=TOP,padx=10,pady=10,fill=X)

    y_values_lbl=Label(plot_frame,text="Select size value",font=("Helvatica",12,"bold"),bg="#f3f3f3",fg="#633974",bd=0)
    y_values_lbl.pack(side=TOP,padx=10,pady=10,fill=X)

    y_values_box=ttk.Combobox(plot_frame,value=["Products Quantity From Per Suppliers","Material Quantity","Product Type Quantity"],font=("Helvatica",12,"bold"))
    y_values_box.pack(side=TOP,padx=10,pady=10,fill=X)

    create_graph_btn=Button(plot_frame,text="Create Graph",font=("Helvatica",12,"bold"),fg="#633974",bg="#f3f3f3",activebackground="#CBC3E3",activeforeground="white",bd=0,command=create_command)
    create_graph_btn.pack(side=BOTTOM,fill=X,padx=10,pady=30)


    screen.mainloop()

def histo_graph():
    screen=Tk()
    screen.geometry("600x320")
    screen.resizable(width=False,height=False)
    screen.title("Shopy Crush - PDBMS - Graph Screen")

    graph_lbl=Label(screen,text="Histogram Graph",fg="#633974",bg="#ffffff",bd=0,font=("Helvaica",20,"bold"))
    graph_lbl.pack(side=TOP,fill=X)

    def create_command():
        x=[]
        data_y=[]
        y=[]
        n=1
        x_get=x_values_box.get()
        y_get=y_values_box.get()
        if x_get == "Suppliers" and y_get == "Products Quantity From Per Suppliers":
            y.clear()
            data_y.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][4] not in y:
                    y.append(data[n][4])
                data_y.append(data[n][4])
                n+=1
            for j in range(len(y)):
                x.append(data_y.count(y[j]))
            plt.hist(x,color="#633974",label=y)
            plt.title("Products Per Supplier Graph")
            plt.legend(["bar"])
            plt.show()
        
        elif x_get == "Material" and y_get == "Material Quantity":
            y.clear()
            data_y.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][3] not in y:
                    y.append(data[n][3])
                data_y.append(data[n][3])
                n+=1
            for j in range(len(y)):
                x.append(data_y.count(y[j]))
            plt.hist(x,color="#633974",label=y)
            plt.title("Products Per Supplier Graph")
            plt.legend(["bar"])
            plt.show()
        elif x_get == "Product Type" and y_get == "Product Type Quantity":
            y.clear()
            data_y.clear()
            n=1
            for i in range(len(data)-1):
                if data[n][2] not in y:
                    y.append(data[n][2])
                data_y.append(data[n][2])
                n+=1
            for j in range(len(y)):
                x.append(data_y.count(y[j]))
            plt.hist(x,color="#633974",label=y)
            plt.title("Products Per Supplier Graph")
            plt.legend(["bar"])
            plt.show()
        
        else:
            messagebox.showwarning("Shopy Crush - PDBMS - Graph","Unable to plot graph with this data.")
    plot_frame=Frame(screen,bg="#633974",bd=0,container=False)
    plot_frame.pack(side=TOP,fill=X,padx=10,pady=10)

    x_values_lbl=Label(plot_frame,text="Select X-axis value",font=("Helvatica",12,"bold"),bg="#f3f3f3",fg="#633974",bd=0)
    x_values_lbl.pack(side=TOP,padx=10,pady=10,fill=X)

    x_values_box=ttk.Combobox(plot_frame,value=["Suppliers","Material","Product Type"],font=("Helvatica",12,"bold"))
    x_values_box.pack(side=TOP,padx=10,pady=10,fill=X)

    y_values_lbl=Label(plot_frame,text="Select Y-axis value",font=("Helvatica",12,"bold"),bg="#f3f3f3",fg="#633974",bd=0)
    y_values_lbl.pack(side=TOP,padx=10,pady=10,fill=X)

    y_values_box=ttk.Combobox(plot_frame,value=["Products Quantity From Per Suppliers","Material Quantity","Product Type Quantity"],font=("Helvatica",12,"bold"))
    y_values_box.pack(side=TOP,padx=10,pady=10,fill=X)

    create_graph_btn=Button(plot_frame,text="Create Graph",font=("Helvatica",12,"bold"),fg="#633974",bg="#f3f3f3",activebackground="#CBC3E3",activeforeground="white",bd=0,command=create_command)
    create_graph_btn.pack(side=BOTTOM,fill=X,padx=10,pady=30)


    screen.mainloop()