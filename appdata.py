from tkinter import *
import sqlite3 as sq

root = Tk()
root.geometry("250x400")
root.title("database cek")

conek = sq.connect("deldata.db")
cur = conek.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS baru(
#     Name text,
#     Age int,
#     Hometown text
# )""")
def mengisidata():
        conek = sq.connect("deldata.db")
        cur =  conek.cursor()
        cur.execute("SELECT *, oid FROM baru")
        rec = cur.fetchall()
        cetak1 = ''
        cetak2 = ''
        for i in rec:
            cetak1 += str(i[3])+'\n'
            cetak2 += str(i[0])+'\n'
        global rec_display
        global rec_display2

        rec_display = Label(root,text=cetak1)
        rec_display.grid(row=10,column=0)
        rec_display2 = Label(root,text=cetak2)
        rec_display2.grid(row=10,column=1)

        conek.commit()
        conek.close()


exist_data = True
def display_database():
   
    global exist_data
    
    if exist_data == True:
        mengisidata()
        exist_data = False
    
    else: 
        rec_display.grid_forget()
        rec_display2.grid_forget()
        exist_data = True
        

def menghapus():
    conek = sq.connect("deldata.db")
    cur =  conek.cursor()
    # if ent_rev in 
    cur.execute("DELETE from baru where oid ="+ent_rev.get())
    ent_rev.delete(0,END)
    conek.commit()
    conek.close()
    # display_database()


def submit():
    conek = sq.connect("deldata.db")
    cur =  conek.cursor()
    cur.execute("INSERT INTO baru VALUEs(:nama,:umur,:asal)",{
    "nama": en1.get(),
    "umur" : en2.get(),
    "asal":en3.get()
    })
    conek.commit()
    conek.close()

    # display_database()

    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)


def tampil():
    conek = sq.connect("deldata.db")
    cur =  conek.cursor()
    judul_cetak = 'Name has been record'

    display_database()
 
    conek.commit()
    conek.close()

lbl_judul = Label(root,text="DATABASE USER")
lbl_judul.grid(row=0,columnspan=2)

lbl1 = Label(root,text="nama")
lbl2 = Label(root,text="umur")
lbl3 = Label(root,text="asal")
lbl1.grid(row=1,column=0)
lbl2.grid(row=2,column=0)
lbl3.grid(row=3,column=0)

en1 = Entry()
en2 = Entry(width=10)
en3 = Entry()
en1.grid(row=1,column=1,sticky="W",padx=10)
en2.grid(row=2,column=1,sticky="W",padx=10)
en3.grid(row=3,column=1,sticky="W",padx=10)

btn = Button(root,text="submit",command=submit,padx=40)
btn.grid(row=7,columnspan=2,pady=10)

btn2 = Button(root,text="display data",command=tampil,padx=30)
btn2.grid(row =9,columnspan=2,pady=10)

enet_defval = StringVar()
enet_defval.set("id ")
ent_rev = Entry(root,textvariable=enet_defval,width=4)
ent_rev.grid(row=8,column=0,padx=10)

btn3 = Button(root,text="remove item", command=menghapus)
btn3.grid(row =8,column=1)


conek.commit()
conek.close()

root.mainloop()
