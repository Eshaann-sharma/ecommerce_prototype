from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image   #for using imgs
import tkinter.messagebox       # for showing pop up msgs
from tkinter import ttk 
import random as ran            #random generation
import mysql.connector as my

db = my.connect(
    host = "localhost",
    user = "root",
    passwd = "12345678",
    database = "arcedia"
    )

cur=db.cursor()


#user data
def get_user():
    qry1="select * from user"
    cur.execute(qry1)
    data1=cur.fetchall()
    return data1

def get_pro():
    qry="select * from product"
    cur.execute(qry)
    data2=cur.fetchall()
    return data2
#UID Genrator
def uid_gen():
    qry2="select uid from user;"
    cur.execute(qry2)
    data3=cur.fetchall()
    while True:
        uid_temp=ran.randrange(1000,9999)
        if uid_temp not in data3:
            break
    return uid_temp

activeuser=[]

#Main Window Configuration

main_wd =Tk()
main_wd.title("ARC3DIA")
#main_wd.configure(bg='#ffffff')
root=tk.Toplevel(main_wd)

main_wd.withdraw() #makes it invisible but keeps it alive

photo_bg = PhotoImage(file = r'11.png')

image2 = Label(root , image = photo_bg)
image2.place(x=0 , y=0 , relwidth=1 , relheight=1)
main_wd.maxsize(1150,1100)

root.title("ARC3DIA")
root.configure(bg='#171717')

root.geometry("600x600")
root.maxsize(600,600)
root.minsize(600,600)

root.iconbitmap('icon.ico')

photo_logo = PhotoImage(file = r"logog_resized.png")

def regist():

    window_reg=tk.Toplevel(root)
    window_reg.title("Registration")
    #window_reg.geometry("300x300")
    #window_reg.configure(bg='#10100F')

    logo_frame = LabelFrame(window_reg , border=0 , padx=200 , bg='#000000')
    logo_frame.grid(column=0 , row = 0 , sticky='ns' ,)

    img = Label( logo_frame, image= photo_logo , bg= '#000000')
    img.grid(row=0 , column= 0 )

    label_name = Label( logo_frame , text='ARC3DIA' , border = 0 , bg= '#000000' , fg = '#CCC9DC' , font= Font_1 ,)
    label_name.grid(column=1 , row=0)

    frame_entry = LabelFrame(window_reg, border=0 )
    frame_entry.grid()

    
    label_1=Label(frame_entry,text='Full Name -')
    label_2=Label(frame_entry,text='Email -')
    label_3=Label(frame_entry,text='Username -')
    label_4=Label(frame_entry,text='Password -')
    label_5=Label(frame_entry,text='Confirm Password -')

    label_1.grid(row=1,column=0)
    label_2.grid(row=2,column=0)
    label_3.grid(row=3,column=0)
    label_4.grid(row=4,column=0)
    label_5.grid(row=5,column=0)

    

    #Name
    entry_1=Entry(frame_entry) 
    #Email
    entry_2=Entry(frame_entry)   
    #Username
    entry_3=Entry(frame_entry)           
    #Password
    entry_4=Entry(frame_entry,show='*')    
    #Confirm Password
    entry_5=Entry(frame_entry,show='*')

    entry_1.grid(row=1,column=1)
    entry_2.grid(row=2,column=1)
    entry_3.grid(row=3,column=1)
    entry_4.grid(row=4,column=1)
    entry_5.grid(row=5,column=1)
          
    entry_1.get()
    entry_2.get()
    entry_3.get()
    entry_4.get()
    entry_5.get()


    def reg_check(pass_1,pass_2,pass_3,o_pass,r_pass):

        data1=get_user()
        allow=True

        for i in range(len(data1)):

            if pass_2 in data1[i]:
                tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : EMAIL ALREADY REGISTERED " )
                allow=False

            if pass_3 in data1[i]:
                tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : USERNAME HAS BEEN TAKEN" )  
                allow=False

            if o_pass!=r_pass:
                tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : PASSWORD DOESNT MATCH EACH OTHER " )
                allow=False

        if allow!=False :
            
            uid=uid_gen()  

            l=(uid,entry_3.get(),entry_4.get(),entry_2.get(),entry_1.get())
            qry_reg='insert into user (uid, uname, pwd, eml,fullname) values (%s,%s,%s,%s,%s);'
            cur.execute(qry_reg,l)
            db.commit()

            tkinter.messagebox.showinfo( "ARC3DIA" , " ACCOUNT REGISTERED")
            window_reg.destroy()


    bcenter=Button(window_reg,text='Enter',padx=50,pady=10,command=lambda:reg_check(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get()),bg='#476072' ,fg='#EEEEEE')
    bcenter.grid(column=0)
      
def login():

    global window_log
    data1=get_user()


    window_log=tk.Toplevel(root)
    window_log.title("Login")
    #window_log.geometry("500x600")
    #window_log.configure(bg='#282828')

    
    logo_frame = LabelFrame(window_log , border=0 , padx=200 , bg='#000000')
    logo_frame.grid(column=0 , row = 0 , sticky='ns' ,)

    #photo_logo = PhotoImage(file = r"logog_resized.png")
    img = Label( logo_frame, image= photo_logo , bg= '#000000')
    img.grid(row=0 , column= 0 )

    label_name = Label( logo_frame , text='ARC3DIA' , border = 0 , bg= '#000000' , fg = '#CCC9DC' , font= Font_1 ,)
    label_name.grid(column=1 , row=0)


    frame=LabelFrame(window_log,bg='#EEEEEE',pady=50 , padx=20)
    frame.grid()#(OR)frame.place(x=100,y=100)

    #Username   
    eu=Entry(frame)
    eu.grid(row=1,column=1)
    
    #Password
    ep=Entry(frame,show='*')
    ep.grid(row=2,column=1)
    
    label_login=Label(frame,text='Log In',font=200)
    label_user=Label(frame,text='USERNAME -')
    label_pass=Label(frame,text='PASSWORD -')

    label_login.grid(row=0,columnspan=2)
    label_user.grid(row=1,column=0)
    label_pass.grid(row=2,column=0)

    def check():

        user_data=get_user()

        allow=False
        
        for i in range(len(user_data)):
            if eu.get()==user_data[i][1] and ep.get()==user_data[i][2]:
                allow =True
                logdata=list(eu.get())
                placeholder=""
                for i in logdata:
                    placeholder=placeholder + i
                if len(activeuser)!=0:
                    activeuser.pop()
                activeuser.append(placeholder)
                break
            else :
                allow=False

        if allow==False:
            tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : INCORRECT PASSWORD OR USERNAME !! " )

        if allow==True:          
            main()
            
    benter=Button(frame ,text='Enter' ,padx=50 ,pady=10 ,command=check,bg='#476072' ,fg='#EEEEEE',)
    benter.grid(column=1)

def main():
          
    main_wd.state('zoomed')

    #POP UP MSG
    tkinter.messagebox.showinfo( "ARC3DIA" , " LOGIN SUCCESFUL !! " )

    window_log.destroy()
    root.destroy()
    
    return

#========================================================================================================================

but_log=Button(root,text='LOG IN',padx=60,pady=10,command=login,bg='#DA0037',fg='#EEEEEE',font=13)
but_reg=Button(root,text='Create New Account',padx=44,pady=10,command=regist,bg='#DA0037',fg='#EEEEEE',font=13)

but_log.place(x=200 , y= 390 )
but_reg.place(x=160 , y =450)

options_hardware = [
    "Keyboards",
    "Mouses",
    "Headsets",
    "Graphic Cards",
]

options_software = [
    "Video games",
    "Softwares",
]

options_3 = [
    "Desks",
    "Chairs",
]

options_profile = [
    "Profile",
    "Change Details",
]

#------------------------------------------------------------------------------------
    #Display UDF
#------------------------------------------------------------------------------------

def profile_display(abc):

    qry=f"select * from user where uname='{abc}'"
    cur.execute(qry)

    userdata=cur.fetchall()
    fullname=userdata[0][4]
    username=userdata[0][1]
    email=userdata[0][3]        
    
    prof_frame=LabelFrame(x_frame,border=0)
    prof_frame.grid()

    pfp=Button(prof_frame,image= photo_pfp ,padx = 10 , pady =10 ,border = 0 )
    pfp.grid(row=0 , column=0, rowspan=2, columnspan=2 )

    #empty1= Label(prof_frame,text=" ")
    displaytitle= Label(prof_frame,text="ACCOUNT INFORMATION")
    fname= Label(prof_frame,text="FULL NAME:")
    fnamevar= Label(prof_frame,text=fullname)
    uname= Label(prof_frame,text="USER NAME:")
    unamevar= Label(prof_frame,text=username)
    eml= Label(prof_frame,text="EMAIL:")
    emlvar= Label(prof_frame,text=email)

    #empty1.grid(row=1,rowspan=2 )
    displaytitle.grid(row=2,column=0,columnspan=2 )
    fname.grid(row=3,column=0)
    fnamevar.grid(row=3,column=1)
    uname.grid(row=4,column=0)
    unamevar.grid(row=4,column=1)
    eml.grid(row=5,column=0)
    emlvar.grid(row=5,column=1)

    ph_title=Label(prof_frame,text="PURCHASE HISTORY(Last 5)")
    ph_title.grid(row=6, column=0, columnspan=2)
    qry=f"select * from purchase_log where uname='{username}'"
    cur.execute(qry)
    purchasehistory=cur.fetchall()
    if len(purchasehistory)==0:
        return
    p1=Label(prof_frame,text=f"1: Order ID:{purchasehistory[len(purchasehistory)-1][0]}, Product Name:{purchasehistory[len(purchasehistory)-1][2]}")
    p1.grid(row=7, column=0, columnspan=2)
    if len(purchasehistory)==1:
        return
    p2=Label(prof_frame,text=f"2: Order ID:{purchasehistory[len(purchasehistory)-2][0]}, Product Name:{purchasehistory[len(purchasehistory)-2][2]}")
    p2.grid(row=8, column=0, columnspan=2)
    if len(purchasehistory)==2:
        return
    p3=Label(prof_frame,text=f"3: Order ID:{purchasehistory[len(purchasehistory)-3][0]}, Product Name:{purchasehistory[len(purchasehistory)-3][2]}")
    p3.grid(row=9,column=0, columnspan=2)
    if len(purchasehistory)==3:
        return
    p4=Label(prof_frame,text=f"4: Order ID:{purchasehistory[len(purchasehistory)-4][0]}, Product Name:{purchasehistory[len(purchasehistory)-4][2]}")
    p4.grid(row=10,column=0, columnspan=2)
    if len(purchasehistory)==4:
        return
    p5=Label(prof_frame,text=f"5: Order ID:{purchasehistory[len(purchasehistory)-5][0]}, Product Name:{purchasehistory[len(purchasehistory)-5][2]}")
    p5.grid(row=11,column=0, columnspan=2)
    return

def renew_details():


    frame_entry2= LabelFrame(x_frame, border=0)
    frame_entry2.grid()

    pfp=Button(frame_entry2,image= photo_pfp ,padx = 10 , pady =10 ,border = 0 )
    pfp.grid(row=0 , column=0,columnspan=2 )

    def update_check(field):
        check_list=["email","full name","password"]

        #if len(change_type)!=0:
        #    change_type.pop()
        #change_type.append(field)

        if field not in check_list:
            tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : PLEASE ENTER FIELD PROPERLY !! " )
            for widgets in x_frame.winfo_children():
                widgets.destroy()
                renew_details()
                return
        for widgets in x_frame.winfo_children():
            widgets.destroy()
        renew_details2(field)

    
    label_a=Label(frame_entry2,text='What Do You Want To Change? [Email | Full Name | Password] -')
    label_a.grid(row=2,column=1)

    entry_a=Entry(frame_entry2)
    entry_a.grid(row=2,column=2)

    entry_a.get()

    #change_type=entry_a.get().lower()

    benter_trial=Button(frame_entry2 ,text='Confirm' ,padx=50 ,pady=10 ,command=lambda:update_check(entry_a.get().lower()),bg='#476072' ,fg='#EEEEEE',)
    benter_trial.grid(columnspan=2)

def renew_details2(change_type):
    frame_entry1=LabelFrame(x_frame,border=0)
    frame_entry1.grid()

    def update_data(new_data,current_user,password_check,field,):
        qry=f"select * from user where uname='{current_user}'"

        cur.execute(qry)

        userdata=cur.fetchall()

        if len(userdata)==0:
            tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : NO USER WITH GIVEN USERNAME. PLEASE ENTER ALL THE DETAILS AGAIN !! " )
            for widgets in x_frame.winfo_children():
                widgets.destroy()
            renew_details()
            return

        current_uid=int(userdata[0][0])

        if userdata[0][2]!=password_check:
            for widgets in x_frame.winfo_children():
                widgets.destroy()
            tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : PASSWORD AND USERNAME DON'T MATCH. !! " )
            renew_details()
            return
        if field=="email":
            if userdata[0][3]==new_data:
                for widgets in x_frame.winfo_children():
                    widgets.destroy()
                tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : PREVIOUS AND NEW EMAIL ARE SAME !! " )
                renew_details()
                return                
        if field=="full name":
            if userdata[0][4]==new_data:
                for widgets in x_frame.winfo_children():
                    widgets.destroy()
                tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : PREVIOUS AND NEW FULL NAME ARE SAME !! " )
                renew_details()
                return
        if field=="password":
            if userdata[0][2]==new_data:
                for widgets in x_frame.winfo_children():
                    widgets.destroy()
                tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : PREVIOUS AND NEW PASSWORD ARE SAME !! " )
                renew_details()
                return            

        if field=="email":
            qry=f"update user set eml='{new_data}' where uid={current_uid};"
        if field=="full name":
            qry=f"update user set fullname='{new_data}' where uid={current_uid};"
        if field=="password":
            qry=f"update user set pwd='{new_data}' where uid={current_uid};"
        cur.execute(qry)
        db.commit()
        for widgets in x_frame.winfo_children():
            widgets.destroy()
        tkinter.messagebox.showinfo( "ARC3DIA" , " SUCCESS : THE ENTERED DATA HAS BEEN CHANGED !! " )
        renew_details()

    #Changing Email
    if change_type=="email":
        label_1=Label(frame_entry1,text='New Email -')
        label_2=Label(frame_entry1,text='Confirm Username -')
        label_3=Label(frame_entry1,text='Password -')

        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        label_3.grid(row=3,column=0)

        entry_1=Entry(frame_entry1)
        entry_2=Entry(frame_entry1)
        entry_3=Entry(frame_entry1,show="*")

        entry_1.grid(row=1,column=1)
        entry_2.grid(row=2,column=1)
        entry_3.grid(row=3,column=1)

        entry_1.get()
        entry_2.get()
        entry_3.get()

        benter=Button(frame_entry1 ,text='Confirm' ,padx=50 ,pady=10 ,command=lambda:update_data(entry_1.get(),entry_2.get(),entry_3.get(),change_type),bg='#476072' ,fg='#EEEEEE',)
        benter.grid()

    #Changing Full Name
    if change_type=="full name":
        label_1=Label(frame_entry1,text='Full Name -')
        label_2=Label(frame_entry1,text='Confirm Username -')
        label_3=Label(frame_entry1,text='Password -')

        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        label_3.grid(row=3,column=0)

        entry_1=Entry(frame_entry1)
        entry_2=Entry(frame_entry1)
        entry_3=Entry(frame_entry1,show="*")

        entry_1.grid(row=1,column=1)
        entry_2.grid(row=2,column=1)
        entry_3.grid(row=3,column=1)

        entry_1.get()
        entry_2.get()
        entry_3.get()

        benter=Button(frame_entry1 ,text='Confirm' ,padx=50 ,pady=10 ,command=lambda:update_data(entry_1.get(),entry_2.get(),entry_3.get(),change_type),bg='#476072' ,fg='#EEEEEE',)
        benter.grid()


    #Changing Password
    if change_type=="password":
        label_0=Label(frame_entry1,text='Confirm Username -')
        label_1=Label(frame_entry1,text='Old Password -')
        label_2=Label(frame_entry1,text='New Password -')
        label_3=Label(frame_entry1,text='Confirm New Password -')

        label_0.grid(row=1,column=0)
        label_1.grid(row=2,column=0)
        label_2.grid(row=3,column=0)
        label_3.grid(row=4,column=0)

        entry_0=Entry(frame_entry1)
        entry_1=Entry(frame_entry1,show="*")
        entry_2=Entry(frame_entry1,show="*")
        entry_3=Entry(frame_entry1,show="*")

        entry_0.grid(row=1,column=1)
        entry_1.grid(row=2,column=1)
        entry_2.grid(row=3,column=1)
        entry_3.grid(row=4,column=1)

        entry_0.get()
        entry_1.get()
        entry_2.get()
        entry_3.get()

        if entry_2.get()!=entry_3.get():
            tkinter.messagebox.showinfo( "ARC3DIA" , " RETRY : NEW PASSWORDS DON'T MATCH. !! " )

        benter=Button(frame_entry1 ,text='Confirm' ,padx=50 ,pady=10 ,command=lambda:update_data(entry_2.get(),entry_0.get(),entry_1.get(),change_type),bg='#476072' ,fg='#EEEEEE',)
        benter.grid()

def info_win(cat):                                                                         
    qry=f"select * from product where cat='{cat}'" 

    cur.execute(qry)

    productdata=cur.fetchall()
    photo(productdata)

def win_hardware(a):

    if clicked1.get() =='Keyboards':

        clicked1.set( "HARDWARE" )
             
        #delete interior widgets from a frame
        for widgets in x_frame.winfo_children():
            widgets.destroy()
        
        info_win("Keyboard")

    if clicked1.get()=="Mouses":

        clicked1.set("HARDWARE")
        
        for widgets in x_frame.winfo_children():
            widgets.destroy()

        info_win("Mouse")

    if clicked1.get() == "Headsets":

        clicked1.set('HARDWARE')
                
        for widgets in x_frame.winfo_children():
            widgets.destroy()
        
        info_win("Headphone")

    if clicked1.get() == "Graphic Cards":

        clicked1.set('HARDWARE')

        for widgets in x_frame.winfo_children():
            widgets.destroy()

        info_win("GraphicCard")

def win_software(a):

    if clicked2.get() =='Video games':

        clicked2.set( "SOFTWARE" )
               
        for widgets in x_frame.winfo_children():
            widgets.destroy()

        info_win("Game")

    if clicked2.get() =='Softwares':

        clicked2.set( "SOFTWARE" )
               
        for widgets in x_frame.winfo_children():
            widgets.destroy()

        info_win("Software")

def win_furn(a):

    if clicked3.get() =='Desks':

        clicked3.set( "FURNITURE" )
                
        for widgets in x_frame.winfo_children():
            widgets.destroy()

        info_win("Desk")

    if clicked3.get() =='Chairs':

        clicked3.set( "FURNITURE" )
                
        for widgets in x_frame.winfo_children():
            widgets.destroy()

        info_win("Chair")

    return

def win_prof(a):
    if clicked4.get() =='Change Details':

        clicked4.set( "MY ACCOUNT" )
            
        for widgets in x_frame.winfo_children():
            widgets.destroy()
        renew_details()

    if clicked4.get() =='Profile':

        clicked4.set( "MY ACCOUNT" )
        
        for widgets in x_frame.winfo_children():
            widgets.destroy()
        profile_display(activeuser[0])

    return

def clean():
    for widgets in x_frame.winfo_children():
            widgets.destroy()

    home_pg()

def purchase(productid):
    qry=f"select * from product where pid={productid}"
    cur.execute(qry)
    productdata=cur.fetchall()
    qry=f"select * from user where uname='{activeuser[0]}'"
    cur.execute(qry)
    userdata=cur.fetchall()
    qry=f"insert into purchase_log (pid,pname,uname,uid) values (%s,%s,%s,%s)"
    reqdvalue=(productid,productdata[0][1],userdata[0][1],userdata[0][0])
    cur.execute(qry,reqdvalue)

    db.commit()

    tkinter.messagebox.showinfo( "ARC3DIA" , " SUCCESS : PRODUCT SUCCESFULLY PURCHASED !! " )

    clean()    
    return

def photo(productinfo):

    for widgets in x_frame.winfo_children():
            widgets.destroy()
    
    item_frame =LabelFrame(x_frame,border=0,)
    item_frame.grid()
    br=0
    a=0
    b=0
   
    for i in productinfo:    
        ok=l[i[4]]

        poke=Button(item_frame , image= ok ,padx = 10 , pady =10 , bg= '#EEEEEE' , border = 0 )
        poke.grid(row=0 , column=0+a, rowspan=3)
        
        label_item=Label(item_frame,text=i[1])
        label_item2=Label(item_frame, text=f"Price: {i[2]}")
        label_item3=Label(item_frame, text=f"Seller: {i[3]}")

        label_item.grid(row=0, column=1+b )
        label_item2.grid(row=1 , column=1+b )
        label_item3.grid(row=2 , column=1+b )

        purbut=Button(item_frame ,text='Purchase' ,padx=50 ,pady=10 ,command=lambda:purchase(i[0]),bg='#476072' ,fg='#EEEEEE',)
        purbut.grid(row=3,column=0+a ,columnspan=2)

        br=br+5
        a=a+2
        b=b+2
       
def home_pg():
    
    gallary_frame = LabelFrame(x_frame , border=0, )
    gallary_frame.grid(row=3)

    gal_item1=Button(gallary_frame , image= photo_gal1 ,command=lambda:info_win("Chair"), padx = 10 , pady =10 , bg= '#EEEEEE' , border = 0 )
    gal_item1.grid(row=0 , column=0 , rowspan = 2)

    gal_item2=Button(gallary_frame , image= photo_gal2 ,command=lambda:info_win("Desk"),padx = 10 , pady =10 , bg= '#EEEEEE' , border = 0 )
    gal_item2.grid(row=0 , column=1)

    discount_frame = LabelFrame(x_frame , text= "SUGGESTIONS FOR YOU " , border=0 , font= 15)
    discount_frame.grid(row=4 , )


    dis_item1=Button(discount_frame , text = 'ITEAM 1' , image = photo_item ,command=lambda:info_win("Headphone"), padx = 10 , pady =10 , bg= '#EEEEEE' , border = 0 )
    dis_item1.grid(row=0 , column=0)

    dis_item2=Button(discount_frame , text = 'ITEAM 2' , image= photo_item1 , command=lambda:info_win("Headphone"),padx = 10 , pady =10 , border = 0 )
    dis_item2.grid(row=0 , column=1)

    dis_item3=Button(discount_frame , text = 'ITEAM 3' , image=photo_item2 ,command=lambda:info_win("Headphone"), padx = 10 , pady =10 , border = 0)
    dis_item3.grid(row=0 , column=2)

    dis_item4=Button(discount_frame , text = 'ITEAM 4' , image= photo_item3,command=lambda:info_win("Headphone"), padx = 10 , pady =10 , border = 0 )
    dis_item4.grid(row=0 , column=3)

#------------------------------------------------------------------------------------

photo_gal1 = PhotoImage(file = r"g1.png")   #setups #using
photo_gal2 = PhotoImage(file = r"g2.png")

photo_item = PhotoImage(file = r"hd1.gif")  #headsets #using
photo_item1=PhotoImage(file = r'hd2.gif')
photo_item2=PhotoImage(file = r'hd3.gif')
photo_item3=PhotoImage(file = r'hd4.gif')

photo_game1=PhotoImage(file = r"gn1.gif")   #vd
photo_game2=PhotoImage(file = r"gn2.gif")
photo_game3=PhotoImage(file = r"gn3.gif")
photo_game4=PhotoImage(file = r"gn4.gif")
photo_game5=PhotoImage(file = r"gn5.gif")

photo_pfp=PhotoImage(file = r"pfp1.png")    #using

photo_soft1=PhotoImage(file = r"s1.gif")     #software
photo_soft2=PhotoImage(file = r"s2.gif")
photo_soft3=PhotoImage(file = r"s3.gif")

photo_chair1=PhotoImage(file = r"c1.gif")    #chair
photo_chair2=PhotoImage(file = r"c2.gif")
photo_chair3=PhotoImage(file = r"c3.gif")

photo_d1=PhotoImage(file = r"t1.gif")        #desk
photo_d2=PhotoImage(file = r"t2.gif")

photo_mouse1=PhotoImage(file = r"m1.gif")    #mouse
photo_mouse2=PhotoImage(file = r"m2.gif")
photo_mouse3=PhotoImage(file = r"m3.gif")


photo_gc1=PhotoImage(file = r"gc1.gif")
photo_gc2=PhotoImage(file = r"gc2.gif")       #graphics card
photo_gc3=PhotoImage(file = r"gc3.gif")

photo_key1=PhotoImage(file = r"kb1.gif")      #keyboards
photo_key2=PhotoImage(file = r"kb2.gif")
photo_key3=PhotoImage(file = r"kb3.gif")

l={'kb1.gif':photo_key1,'kb2.gif':photo_key2,'kb3.gif':photo_key3,'gc1.gif':photo_gc1,'gc2.gif':photo_gc2,'gc3.gif':photo_gc3,
'm1.gif':photo_mouse1,'m2.gif':photo_mouse2,'m3.gif':photo_mouse3 ,'t1.gif':photo_d1 ,'t2.gif':photo_d2,'c1.gif':photo_chair1,'c2.gif':photo_chair2,
'c3.gif':photo_chair3,'s1.gif':photo_soft1,'s2.gif':photo_soft2,'s3.gif':photo_soft3,'gn1.gif':photo_game1,'gn2.gif':photo_game2,
'gn3.gif':photo_game3,'gn4.gif':photo_game4,'gn5.gif':photo_game5,'hd1.gif':photo_item,
'hd2.gif':photo_item1,'hd3.gif':photo_item2,'hd4.gif':photo_item3,}


#FONT STYLES
Font_1 = ("Comic Sans MS", 20, "bold" )
Font_2 = ( "Roboto" , 18 )
Font_3 = ("", 18)

logo_frame = LabelFrame(main_wd , border=0 , padx=455 , bg='#000000')
logo_frame.grid(column=0 , row = 0 , sticky='n',columnspan=10)

photo_logo = PhotoImage(file = r"logog_resized.png")
img = Label( logo_frame, image= photo_logo , bg= '#000000')
img.grid(row=0 , column= 0 )

label_name = Button( logo_frame , text='ARC3DIA' , border = 0 , bg= '#000000' , fg = '#CCC9DC' , font= Font_1 ,command=clean)
label_name.grid(column=1 , row=0)


top_frame=LabelFrame(main_wd,border=0,)
top_frame.configure(bg='#000000')
top_frame.grid(column=0 ,row=1 ,)

# datatype of menu text
clicked1 = StringVar(top_frame)
clicked2 = StringVar(top_frame)
clicked3 = StringVar(top_frame)
clicked4 = StringVar(top_frame)
  
# initial menu text
clicked1.set( "HARDWARE " )
clicked2.set( "SOFTWARE " )
clicked3.set("FURNITURE ")
clicked4.set("MY ACCOUNT")

# Create Dropdown menu
drop_1 = OptionMenu( top_frame , clicked1, command=win_hardware , *options_hardware, )
drop_1.configure(bg='#000000',fg='#EEEEEE',border=0,padx=70 , )
drop_1.grid(row=0 , column=0 )

drop_2 = OptionMenu( top_frame ,  clicked2 , command=win_software , *options_software  )
drop_2.configure(bg='#000000',fg='#EEEEEE',border=0,padx=70 , )
drop_2.grid(row=0 , column=1)

drop_3 = OptionMenu( top_frame ,  clicked3 , command=win_furn , *options_3  )
drop_3.configure(bg='#000000' , fg='#EEEEEE' , border=0 , padx=70 , )
drop_3.grid(row=0 , column=2)

drop_4 = OptionMenu( top_frame ,  clicked4 , command=win_prof , *options_profile  )
drop_4.configure(bg='#000000' , fg='#EEEEEE' , border=0 , padx=70 ,)
drop_4.grid(row=0,column=3) 

x_frame = LabelFrame(main_wd , border = 0)
x_frame.grid()

home_pg()

main_wd.mainloop()

root.mainloop()
