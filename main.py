# -*- coding: UTF-8 -*-
from tkinter import messagebox, ttk
from tkinter.ttk import Treeview

import os
import pymysql
from tkinter import *

import win32gui

teachername = None
studentname = None
adminname = None
xiugai = 0
#数据库连接
def mysql(sql):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='sports_meeting', charset='utf8')
    except:
        messagebox.showinfo('警告','数据库链接失败！')
    cur = conn.cursor()
    cur.execute(sql)
    redate = cur.fetchall()

    conn.close()

    return redate

# main = Tk()

# 进入消息循环
# main.title("登录")
# main.geometry('400x300')
# main.resizable(width=False, height=False)
#
# l = Label(main, text = "运动会管理系统登录",font=('',15))
# l.pack()
# frm = Frame(main)
# #left
# frm_L = Frame(frm)
# Label(frm_L, text='账号：', font=('', 15)).pack(side=TOP)
# frm_L.pack(side=TOP)
#
# #right
# frm_R = Frame(frm)
#
# frm_R.pack(side=TOP)
#
#
# frm.pack()
# main.mainloop()


# def sign_to_Mofan_Python():
#     np = new_pwd.get()
#     npf = new_pwd_confirm.get()
#     nn = new_name.get()
#     with open('usrs_info.pickle', 'rb') as usr_file:
#         exist_usr_info = pickle.load(usr_file)
#     if np != npf:
#         tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
#     elif nn in exist_usr_info:
#         tk.messagebox.showerror('Error', 'The user has already signed up!')
#     else:
#         exist_usr_info[nn] = np
#         with open('usrs_info.pickle', 'wb') as usr_file:
#             pickle.dump(exist_usr_info, usr_file)
#         tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
#         window_sign_up.destroy()

# def main():
#     window_sign_up.destroy()
#     main = Tk()
#     Label(main,text="hello").pack()
#     main.mainloop()

def loginyn():
    global teachername,studentname,adminname
    date = mysql("SELECT * FROM admin")
    username = entry_new_name.get()
    passwrod = entry_usr_pwd.get()
    # if username == date[][1]:
    if not username or not passwrod:
        messagebox.showinfo('提示','账号密码不能为空！')
    else:
        upy = 0
        for alldate in date:
          if alldate[1] == username:
              if alldate[2] == passwrod:
                  upy = 1
                  break
              else:
                  upy = 3
                  break
                  # messagebox.askokcancel('提示', '密码输入错误')
          else:
              upy = 2
              # messagebox.askokcancel('提示', '账号输入错误')
        if upy == 3:
            messagebox.showinfo('提示', '密码输入错误')
        if upy == 1:
            messagebox.showinfo('提示', '欢迎管理员'+username)
            adminname = username
            window_sign_up.destroy()
        if upy == 2:
            # messagebox.askokcancel('提示', '账号输入错误')
            #判断是不是管理员以外的人员登录

            date2 = mysql("SELECT * FROM student")

            # if username == date[][1]:
            spy = 0
            for alldate2 in date2:


                if alldate2[1] == int(username):

                    if alldate2[4] == passwrod:
                        spy = 1
                        name1 = alldate2[2]
                        break
                    else:
                        spy = 3
                        break
                        # messagebox.askokcancel('提示', '密码输入错误')
                else:
                    spy = 2
                    # messagebox.askokcancel('提示', '账号输入错误')
            if spy == 3:
                messagebox.showinfo('提示', '密码输入错误')
            if spy == 1:
                messagebox.showinfo('提示', '欢迎学生' + name1)
                studentname = username
                window_sign_up.destroy()
            if spy == 2:
                # messagebox.askokcancel('提示', '账号输入错误')
                # 判断是不是管理员以外的人员登录

                date3 = mysql("SELECT * FROM teacher")
                # if username == date[][1]:
                tpy = 0
                for alldate3 in date3:
                    if alldate3[1] == int(username):
                        if alldate3[3] == passwrod:
                            tpy = 1
                            name2 = alldate3[2]
                            break
                        else:
                            tpy = 3
                            break
                            # messagebox.askokcancel('提示', '密码输入错误')
                    else:
                        tpy = 2
                        # messagebox.askokcancel('提示', '账号输入错误')
                if tpy == 3:
                    messagebox.showinfo('提示', '密码输入错误')
                if tpy == 1:
                    messagebox.showinfo('提示', '欢迎老师' + name2)
                    teachername = username
                    window_sign_up.destroy()
                if tpy == 2:
                    messagebox.showinfo('提示', '账号输入错误')

            # messagebox.askokcancel('提示', '账号输入错误')
            # 判断是不是管理员以外的人员登录










def baoming(a):
    b = messagebox.askyesno('提示', '确定要报名该项目吗')
    if b == True:
        e = mysql("SELECT upid FROM pc WHERE uid = " + str(studentname))
        t = 0
        for ee in e:
            if ee[0] == a:
                t = 1
                messagebox.showinfo('提示','你当前已经报了该项目了，换个项目参加吧！')
        if t == 0:
            print(a)
            c = mysql("INSERT INTO `pc`(`uid`, `upid`) VALUES ("+studentname+","+str(a)+")")
            d = tree.get_children()
            for itme in d:
                tree.delete(itme)
            mydate()
def baoming2(a):
    b = messagebox.askyesno('提示', '确定要报名该项目吗')
    if b == True:
        e = mysql("SELECT upid FROM pc WHERE uid = " + str(teachername))
        t = 0
        for ee in e:
            if ee[0] == a:
                t = 1
                messagebox.showinfo('提示','你当前已经报了该项目了，换个项目参加吧！')
        if t == 0:
            print(a)
            c = mysql("INSERT INTO `pc`(`uid`, `upid`) VALUES ("+teachername+","+str(a)+")")
            d = tree.get_children()
            for itme in d:
                tree.delete(itme)
            mydate2()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def exit():
    sys.exit()

def adupstu():
    global xiugai
    xiugai = 0
    v.set("学生报名信息(双击信息可修改)")
    d = tree.get_children()
    for itme in d:
        tree.delete(itme)
    myadda()
def aduptea():
    global xiugai
    xiugai = 1
    v.set("教师报名信息(双击信息可修改)")
    d = tree.get_children()
    for itme in d:
        tree.delete(itme)
    myadda2()











def addadmin():
    def adddate():
        user = usernamea.get()
        passw = password.get()
        if not user or not passw:
            messagebox.showinfo('提示', '账号或密码不能为空')
            addadminv.destroy()
        else:
            ychongfu = None
            chongfu = mysql("SELECT * FROM `admin` WHERE 1")
            for chongfus in chongfu:
                if user == chongfus[1]:
                    ychongfu = 1

            if ychongfu == 1:
                messagebox.showinfo('提示','账号已经存在了')
                addadminv.destroy()
            else:

                mysql("INSERT INTO `admin`(`username`, `password`) VALUES ('"+user+"','"+passw+"')")
                messagebox.showinfo('提示','添加成功')
                addadminv.destroy()
    addadminv = Toplevel()

    sw = addadminv.winfo_screenwidth()

    sh = addadminv.winfo_screenheight()
    x = (sw - 350) / 2

    y = (sh - 200) / 2

    addadminv.geometry("%dx%d+%d+%d" % (350, 200, x, y))

    addadminv.title('添加管理员')

    addadminv.resizable(width=False, height=False)

    frame = Frame(addadminv)
    frame.place(x=0, y=0, width=350, height=200)



    Label(frame,text="账号").place(x=20,y=20,width=100,height=50)
    Label(frame, text="密码").place(x=20, y=60, width=100, height=50)
    usernamea = StringVar()
    text = Entry(frame,textvariable=usernamea)

    text.place(x=120, y=33, width=150, height=20)

    password = StringVar()
    text = Entry(frame,textvariable=password)

    text.place(x=120, y=75, width=150, height=20)

    ttk.Button(frame, text="添加",command=adddate).place(x=50, y=130, width=100, height=40)
    ttk.Button(frame, text="取消",command=addadminv.destroy).place(x=200, y=130, width=100, height=40)



    addadminv.mainloop()
def nowadmin():
    global adminname
    adminx = mysql("SELECT * FROM `admin` WHERE username='"+adminname+"'")
    def adddate():
        passw = password.get()
        if not passw:
            messagebox.showinfo('提示', '密码不能为空')
            addadminv.destroy()
        else:
            mysql("UPDATE `admin` SET `password`='"+passw+"' WHERE username='"+adminname+"'")
            messagebox.showinfo('提示','修改成功')
            addadminv.destroy()
    addadminv = Toplevel()

    sw = addadminv.winfo_screenwidth()

    sh = addadminv.winfo_screenheight()
    x = (sw - 350) / 2

    y = (sh - 200) / 2

    addadminv.geometry("%dx%d+%d+%d" % (350, 200, x, y))

    addadminv.title('修改管理员信息')

    addadminv.resizable(width=False, height=False)

    frame = Frame(addadminv)
    frame.place(x=0, y=0, width=350, height=200)



    Label(frame,text="账号").place(x=20,y=20,width=100,height=50)
    Label(frame, text="密码").place(x=20, y=60, width=100, height=50)
    usernamea = StringVar()

    text = Entry(frame,textvariable=usernamea)
    text.delete(0, 100)
    text.insert(0, adminx[0][1])
    text.place(x=120, y=33, width=150, height=20)
    text.config(state='disabled')

    password = StringVar()
    text = Entry(frame,textvariable=password)
    text.delete(0, 100)
    text.insert(0, adminx[0][2])


    text.place(x=120, y=75, width=150, height=20)

    ttk.Button(frame, text="修改",command=adddate).place(x=50, y=130, width=100, height=40)
    ttk.Button(frame, text="取消",command=addadminv.destroy).place(x=200, y=130, width=100, height=40)
    addadminv.mainloop()





def delel():

    def deldate2(event):
        yon = messagebox.askyesno('提示','确定删除该条信息？')
        if yon == True:
            for item in tree.selection():
                item_text = tree.item(item, "values")
            mysql("DELETE FROM `admin` WHERE username='"+item_text[1]+"'")
            messagebox.showinfo('提示','删除成功')
            d = tree.get_children()
            for itme in d:
                tree.delete(itme)
            myadda4()

        addadminv.destroy()
        delel()






    addadminv = Toplevel()

    sw = addadminv.winfo_screenwidth()

    sh = addadminv.winfo_screenheight()
    x = (sw - 350) / 2

    y = (sh - 200) / 2

    addadminv.geometry("%dx%d+%d+%d" % (350, 200, x, y))

    addadminv.title('修改管理员信息')

    addadminv.resizable(width=False, height=False)
    Label(addadminv,text="(双击信息可删除)").pack()
    frame = Frame(addadminv)
    frame.place(x=0, y=20, width=350, height=200)



    tree = Treeview(frame, columns=('c1', 'c2', 'c3'), show="headings",
                    yscrollcommand=scrollBar.set)

    def myadda4():
        tree.column('c1', width=116, anchor='center')

        tree.column('c2', width=116, anchor='center')
        tree.column('c3', width=116, anchor='center')

        tree.heading('c1', text='编号')

        tree.heading('c2', text='账号')
        tree.heading('c3', text='密码')


        tree.pack(side=LEFT, fill=Y)

        scrollBar.config(command=tree.yview)

        i = 1
        con = mysql("SELECT * FROM `admin` WHERE 1")
        for co in con:
            tree.insert('', i, values=(i, co[1], co[2]))
            i = i + 1

    myadda4()
    tree.bind('<Double-Button-1>', deldate2)










    addadminv.mainloop()










def addxiangmu():
    lastpid = None

    allxiangmu = mysql("SELECT * FROM `project` WHERE 1")
    for allxiangmus in allxiangmu:
        lastpid = allxiangmus[1]

    def adddate():
        doubleo = None
        user = usernamea.get()
#项目是否重复
        for allxiangm2 in allxiangmu:
            if user == allxiangm2[2]:
                doubleo = 1
        if doubleo == 1:
            messagebox.showinfo('提示','项目名已经存在了！')
            addadminv.destroy()
        else:

            if not user:
                messagebox.showinfo('提示', '项目名不能为空')
                addadminv.destroy()
            else:
                newlastpid = lastpid + 1
                mysql("INSERT INTO `project`(`pid`, `pname`) VALUES ('"+str(newlastpid)+"','"+user+"')")
                messagebox.showinfo('提示','添加成功')
                addadminv.destroy()
    addadminv = Toplevel()

    sw = addadminv.winfo_screenwidth()

    sh = addadminv.winfo_screenheight()
    x = (sw - 350) / 2

    y = (sh - 200) / 2

    addadminv.geometry("%dx%d+%d+%d" % (350, 200, x, y))

    addadminv.title('添加项目')

    addadminv.resizable(width=False, height=False)

    frame = Frame(addadminv)
    frame.place(x=0, y=0, width=350, height=200)



    Label(frame,text="项目名").place(x=20,y=20,width=100,height=50)
    usernamea = StringVar()
    text = Entry(frame,textvariable=usernamea)

    text.place(x=120, y=33, width=150, height=20)


    ttk.Button(frame, text="添加",command=adddate).place(x=50, y=130, width=100, height=40)
    ttk.Button(frame, text="取消",command=addadminv.destroy).place(x=200, y=130, width=100, height=40)



    addadminv.mainloop()









def delxiangmu():



    def deldate2(event):
        yon = messagebox.askyesno('提示','确定删除该条信息？')
        if yon == True:
            for item in tree.selection():
                item_text = tree.item(item, "values")
            mysql("DELETE FROM `project` WHERE pname = '"+item_text[1]+"'")
            messagebox.showinfo('提示','删除成功')
            d = tree.get_children()
            for itme in d:
                tree.delete(itme)
            myadda4()

        addadminv.destroy()
        delxiangmu()






    addadminv = Toplevel()

    sw = addadminv.winfo_screenwidth()

    sh = addadminv.winfo_screenheight()
    x = (sw - 350) / 2

    y = (sh - 200) / 2

    addadminv.geometry("%dx%d+%d+%d" % (350, 200, x, y))

    addadminv.title('删除项目信息')

    addadminv.resizable(width=False, height=False)
    Label(addadminv,text="(双击信息可删除)").pack()
    frame = Frame(addadminv)
    frame.place(x=0, y=20, width=350, height=200)



    tree = Treeview(frame, columns=('c1', 'c2'), show="headings",
                    yscrollcommand=scrollBar.set)

    def myadda4():
        tree.column('c1', width=175, anchor='center')

        tree.column('c2', width=175, anchor='center')



        tree.heading('c1', text='编号')

        tree.heading('c2', text='项目名')


        tree.pack(side=LEFT, fill=Y)

        scrollBar.config(command=tree.yview)

        i = 1
        con = mysql("SELECT * FROM `project` WHERE 1")
        for co in con:
            tree.insert('', i, values=(i, co[2]))
            i = i + 1

    myadda4()
    tree.bind('<Double-Button-1>', deldate2)










    addadminv.mainloop()


























if __name__ == '__main__':

    window_sign_up = Tk()
    # window_sign_up.geometry('350x200')


    sw = window_sign_up.winfo_screenwidth()

    sh = window_sign_up.winfo_screenheight()
    x = (sw - 350) / 2

    y = (sh - 200) / 2

    window_sign_up.geometry("%dx%d+%d+%d" % (350, 200, x, y))

    window_sign_up.title('校际运动会管理系统登录')

    window_sign_up.resizable(width=False,height=False)
#窗体定义
    new_name = StringVar()
    Label(window_sign_up, text='账号/学号/教师编号: ').place(x=10, y=10)
    entry_new_name = Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = StringVar()
    Label(window_sign_up, text='密码: ').place(x=60, y=50)
    entry_usr_pwd = Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    btn_confirm_sign_up = ttk.Button(window_sign_up, text='登录', command = loginyn)
    btn_confirm_sign_up2 = ttk.Button(window_sign_up, text='退出', command=window_sign_up.destroy)

    btn_confirm_sign_up.place(x=50, y=130, width=100,height=40)
    btn_confirm_sign_up2.place(x=200, y=130,width=100,height=40)
    window_sign_up.mainloop()


#---------------------------------------------------------------学生窗口
    if studentname != None:
        stuwin = Tk()

        sw = stuwin.winfo_screenwidth()

        sh = stuwin.winfo_screenheight()
        x = (sw - 1200) / 2

        y = (sh - 500) / 2

        stuwin.geometry("%dx%d+%d+%d" % (1200, 500, x, y))

        stuwin.title('学生报名')

        stuwin.resizable(width=False, height=False)


        frame = Frame(stuwin)
        frame.place(x=0,y=25,width = 1200,height = 500)

        scrollBar = Scrollbar(frame)

        scrollBar.pack(side=RIGHT, fill=Y)

        tree = Treeview(frame,columns=('c1', 'c2','c3','c4','c5','c6'),show="headings",yscrollcommand=scrollBar.set)

        tree.column('c1', width=200, anchor='center')

        tree.column('c2', width=200, anchor='center')
        tree.column('c3', width=200, anchor='center')
        tree.column('c4', width=200, anchor='center')
        tree.column('c5', width=200, anchor='center')
        tree.column('c6', width=200, anchor='center')

        tree.heading('c1', text='编号')

        tree.heading('c2', text='学号')
        tree.heading('c3', text='姓名')
        tree.heading('c4', text='班级')
        tree.heading('c5', text='项目')
        tree.heading('c6', text='成绩')


        tree.pack(side=LEFT, fill=Y)

        scrollBar.config(command=tree.yview)


        # 定义并绑定Treeview组件的鼠标单击事件






        Label(stuwin,text="已经报名项目以及成绩:").pack()
        def mydate():
            pc = mysql("SELECT * FROM pc")
            i=1
            for pc1 in pc:
                if pc1[1] == int(studentname):

                    name = mysql("SELECT * FROM student WHERE sid = "+studentname)
                    xm = mysql("SELECT * FROM project WHERE pid = "+str(pc1[2]))
                    cj = ""
                    if pc1[4] == 0:
                        cj = "未通过管理员审核"
                    if pc1[4] == 1:
                        cj = pc1[3]
                    tree.insert('',i,values=(i,studentname,name[0][2],name[0][3],xm[0][2],cj))
                    i=i+1


        mydate()


        #菜单







        menu = Menu(stuwin)
        pro = mysql("SELECT * FROM project")
        # fmenu1 = Menu(stuwin)
        # fmenu1.add_command(label="当前可报项目")
        fmenu2 = Menu(menu, tearoff=0)
        fmenu3 = Menu(menu,tearoff=0)
        # j=0
        for project in pro:

            fmenu2.add_command(label=project[2],command=lambda x=project[1]: baoming(x))
            # j=j+1
            # fmenu2.add_separator()
            # Button(stuwin,text = project[2]).place(x = 50, y = 50,width = 60, height = 40)
        fmenu3.add_command(label="退出登录",command = restart_program)
        fmenu3.add_command(label="关闭程序",command = exit)

        menu.add_cascade(label="当前可报项目",menu=fmenu2)
        menu.add_cascade(label="退出", menu=fmenu3)
        stuwin['menu'] = menu
        stuwin.config(menu=menu)
        stuwin.mainloop()









    if adminname != None:
        adminwin = Tk()

        sw = adminwin.winfo_screenwidth()

        sh = adminwin.winfo_screenheight()
        x = (sw - 1200) / 2

        y = (sh - 500) / 2

        adminwin.geometry("%dx%d+%d+%d" % (1200, 500, x, y))

        adminwin.title('管理员界面')

        adminwin.resizable(width=False, height=False)

        frame = Frame(adminwin)
        frame.place(x=0, y=25, width=1200, height=500)
        menu = Menu(adminwin)


        fm1 = Menu(menu, tearoff=0)
        fm2 = Menu(menu, tearoff=0)
        fm3 = Menu(menu, tearoff=0)
        fm4 = Menu(menu, tearoff=0)

        fm1.add_command(label="退出登录", command=restart_program)
        fm1.add_command(label="关闭程序", command=exit)

        fm2.add_command(label="学生报名管理",command=adupstu)
        fm2.add_command(label="教师报名管理",command=aduptea)

        fm3.add_command(label="添加管理员",command=addadmin)
        fm3.add_command(label="修改当前管理员信息",command=nowadmin)
        fm3.add_command(label="删除管理员", command=delel)

        fm4.add_command(label="增加运动会项目", command = addxiangmu)
        fm4.add_command(label="删除运动会项目", command = delxiangmu)

        menu.add_cascade(label="运动会报名管理", menu=fm2)
        menu.add_cascade(label="运动会项目管理", menu=fm4)
        menu.add_cascade(label="管理员信息", menu=fm3)
        menu.add_cascade(label="退出", menu=fm1)
        adminwin['menu'] = menu
        adminwin.config(menu=menu)

        # Button(adminwin,text="学生报名管理").place(x=10,y=25,width=100,height=30)
        # Button(adminwin, text="教师报名管理").place(x=10, y=75, width=100, height=30)


        scrollBar = Scrollbar(frame)

        scrollBar.pack(side=RIGHT, fill=Y)
        v = StringVar()
        v.set("学生报名信息(双击信息可修改)")
        Label(adminwin, textvariable=v).pack()
        tree = Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'), show="headings",
                        yscrollcommand=scrollBar.set)
        def myadda():


            tree.column('c1', width=200, anchor='center')

            tree.column('c2', width=200, anchor='center')
            tree.column('c3', width=200, anchor='center')
            tree.column('c4', width=200, anchor='center')
            tree.column('c5', width=200, anchor='center')
            tree.column('c6', width=200, anchor='center')

            tree.heading('c1', text='编号')

            tree.heading('c2', text='学号')
            tree.heading('c3', text='姓名')
            tree.heading('c4', text='班级')
            tree.heading('c5', text='项目')
            tree.heading('c6', text='成绩')

            tree.pack(side=LEFT, fill=Y)

            scrollBar.config(command=tree.yview)


            # 定义并绑定Treeview组件的鼠标单击事件


            def treeviewClick(event):
                global xiugai
                item_text = None









                if xiugai == 0:

                    def adminexitnewtop():
                        newtop.destroy()
                    for item in tree.selection():
                        item_text = tree.item(item, "values")
                       # print(item_text[1])  # 输出所选行的第一列的值
                    alldate = mysql("SELECT * FROM pc,project,student WHERE uid = sid and upid = pid and uid = "+item_text[1]+" and pname = '"+ item_text[4]+"'")

                    def submit():
                        xuehao = xh.get()
                        xiangmuname = xmu.get()

                        shenhe = sh.get()

                        if shenhe == '1':

                            xmcj = cj.get()
                            mypid = mysql("SELECT * FROM project WHERE pname = '"+xiangmuname+"'")
                            #pid = mypid[0][1]
                            mysql("UPDATE `pc` SET `cj`="+xmcj+",`sh`="+shenhe+" WHERE uid = "+xuehao+" and upid = "+ str(mypid[0][1]))
                            messagebox.showinfo('提示','修改成功')
                            adminexitnewtop()
                            adupstu()
                        else:
                            adminexitnewtop()
                            messagebox.showinfo('提示', '修改失败')

                    def del1():
                        xuehao = xh.get()
                        xiangmuname = xmu.get()
                        mypid = mysql("SELECT * FROM project WHERE pname = '" + xiangmuname + "'")
                        mysql("DELETE FROM `pc` WHERE uid = "+xuehao+" and upid = "+ str(mypid[0][1]))
                        messagebox.showinfo('提示', '删除成功')
                        adminexitnewtop()
                        adupstu()

                    newtop = Toplevel()

                    sw = newtop.winfo_screenwidth()

                    sh = newtop.winfo_screenheight()
                    x = (sw - 600) / 2

                    y = (sh - 500) / 2

                    newtop.geometry("%dx%d+%d+%d" % (600, 500, x, y))

                    newtop.title('管理员界面')

                    newtop.resizable(width=False, height=False)

                    frame = Frame(newtop)
                    frame.place(x=0, y=0, width=600, height=500)
                    Label(frame,text="学号：").place(x=40,y=30,width=100,height=30)
                    Label(frame, text="姓名：").place(x=40, y=60, width=100, height=30)
                    Label(frame, text="班级：").place(x=40, y=90, width=100, height=30)
                    Label(frame, text="项目：").place(x=40, y=120, width=100, height=30)
                    Label(frame, text="成绩：").place(x=40, y=150, width=100, height=30)
                    Label(frame, text="是否通过审核：").place(x=40, y=180, width=100, height=60)


                    xh = StringVar()
                    text = Entry(frame, textvariable=xh)
                    text.place(x=120,y=33,width=100,height=20)
                    text.delete(0, 100)
                    text.insert(0,item_text[1])
                    text.config(state='disabled')

                    xm = StringVar()
                    text = Entry(frame, textvariable=xm)
                    text.place(x=120, y=65, width=100, height=20)
                    text.delete(0, 100)
                    text.insert(0, item_text[2])
                    text.config(state='disabled')

                    bj = StringVar()
                    text = Entry(frame, textvariable=bj,)
                    text.place(x=120, y=97, width=130, height=20)
                    text.delete(0, 100)
                    text.insert(0, item_text[3])
                    text.config(state = 'disabled')

                    xmu = StringVar()
                    text = Entry(frame, textvariable=xmu)
                    text.place(x=120, y=127, width=100, height=20)
                    text.delete(0, 100)
                    text.insert(0, item_text[4])
                    text.config(state='disabled')

                    cj = StringVar()
                    text = Entry(frame, textvariable=cj)
                    text.place(x=120, y=156, width=100, height=20)
                    if alldate[0][4] == 1:
                        text.delete(0, 100)
                        text.insert(0, alldate[0][3])


                    sh = StringVar()

                    #text = Entry(frame, textvariable=sh)
                    text = ttk.Combobox(frame, width=12, textvariable=sh)
                    text['values'] = (0,1)  # 设置下拉列表的值
                    #numberChosen.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
                    text.current(0)


                    text.place(x=150, y=198, width=100, height=20)
                    text.delete(0, 100)
                    text.insert(0, alldate[0][4])

                    Label(frame, text="注意：只有当审核通过时，你打的成绩才能被显示（0为审核不通过，1为审核通过）").place(x=20, y=226, width=600, height=20)

                    ttk.Button(frame,text="提交修改",command=submit).place(x=60, y=270, width=100, height=40)
                    ttk.Button(frame, text="删除该条信息", command=del1).place(x=220, y=270, width=100, height=40)
                    ttk.Button(frame, text="取消修改",command=adminexitnewtop).place(x=380, y=270, width=100, height=40)
                    #print(item_text[1])
                    newtop.mainloop()
                if xiugai == 1:
                    def adminexitnewtop2():
                        newtop2.destroy()

                    for item in tree.selection():
                        item_text = tree.item(item, "values")
                    # # print(item_text[1])  # 输出所选行的第一列的值
                    alldate = mysql("SELECT * FROM pc,project,teacher WHERE uid = tid and upid = pid and uid = " + item_text[1] + " and pname = '" + item_text[3] + "'")

                    def submit2():
                        teaid1 = teaid.get()
                        xmu21 = xmu2.get()

                        shenhe = sh.get()

                        if shenhe == '1':

                            xmcj2 = cj2.get()
                            mypid = mysql("SELECT * FROM project WHERE pname = '" + xmu21 + "'")
                            # pid = mypid[0][1]
                            mysql(
                                "UPDATE `pc` SET `cj`=" + xmcj2 + ",`sh`=" + shenhe + " WHERE uid = " + teaid1 + " and upid = " + str(
                                    mypid[0][1]))
                            messagebox.showinfo('提示', '修改成功')
                            adminexitnewtop2()
                            aduptea()
                        else:
                            adminexitnewtop2()
                            messagebox.showinfo('提示', '修改失败')

                    def del12():
                        teaid1 = teaid.get()
                        xmu21 = xmu2.get()
                        mypid = mysql("SELECT * FROM project WHERE pname = '" + xmu21 + "'")
                        mysql("DELETE FROM `pc` WHERE uid = " + teaid1 + " and upid = " + str(mypid[0][1]))
                        messagebox.showinfo('提示', '删除成功')
                        adminexitnewtop2()
                        aduptea()

                    newtop2 = Toplevel()

                    sw = newtop2.winfo_screenwidth()

                    sh = newtop2.winfo_screenheight()
                    x = (sw - 600) / 2

                    y = (sh - 500) / 2

                    newtop2.geometry("%dx%d+%d+%d" % (600, 500, x, y))

                    newtop2.title('管理员界面')

                    newtop2.resizable(width=False, height=False)

                    frame = Frame(newtop2)
                    frame.place(x=0, y=0, width=600, height=500)
                    Label(frame, text="教师编号：").place(x=40, y=30, width=100, height=30)
                    Label(frame, text="姓名：").place(x=40, y=60, width=100, height=30)
                    Label(frame, text="项目：").place(x=40, y=90, width=100, height=30)
                    Label(frame, text="成绩：").place(x=40, y=120, width=100, height=30)
                    Label(frame, text="是否通过审核：").place(x=40, y=150, width=100, height=60)

                    teaid = StringVar()
                    text = Entry(frame, textvariable=teaid)
                    text.place(x=120, y=33, width=100, height=20)
                    text.delete(0, 100)
                    text.insert(0, item_text[1])
                    text.config(state='disabled')

                    teaname = StringVar()
                    text = Entry(frame, textvariable=teaname)
                    text.place(x=120, y=65, width=100, height=20)
                    text.delete(0, 100)
                    text.insert(0, item_text[2])
                    text.config(state='disabled')

                    xmu2 = StringVar()
                    text = Entry(frame, textvariable=xmu2)
                    text.place(x=120, y=97, width=130, height=20)
                    text.delete(0, 100)
                    text.insert(0, item_text[3])
                    text.config(state='disabled')

                    cj2 = StringVar()
                    text = Entry(frame, textvariable=cj2)
                    text.place(x=120, y=127, width=100, height=20)
                    if alldate[0][4] == 1:
                        text.delete(0, 100)
                        text.insert(0, alldate[0][3])

                    sh = StringVar()
                    # text = Entry(frame, textvariable=sh)

                    text = ttk.Combobox(frame, width=12, textvariable=sh)
                    text['values'] = (0, 1)  # 设置下拉列表的值
                    # numberChosen.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
                    text.current(0)


                    text.place(x=150, y=170, width=100, height=20)
                    text.delete(0, 100)
                    text.insert(0, alldate[0][4])

                    Label(frame, text="注意：只有当审核通过时，你打的成绩才能被显示（0为审核不通过，1为审核通过）").place(x=20, y=226, width=600, height=20)

                    ttk.Button(frame, text="提交修改", command=submit2).place(x=60, y=270, width=100, height=40)
                    ttk.Button(frame, text="删除该条信息", command=del12).place(x=220, y=270, width=100, height=40)
                    ttk.Button(frame, text="取消修改", command=adminexitnewtop2).place(x=380, y=270, width=100, height=40)
                    # print(item_text[1])
                    newtop2.mainloop()


            tree.bind('<Double-Button-1>', treeviewClick)








            i = 1
            con = mysql("SELECT * FROM pc,project,student WHERE uid = sid and upid = pid")
            for co in con:
                cj = ""
                if co[4] == 0:
                    cj = "未通过管理员审核"
                if co[4] == 1:
                    cj = co[3]
                tree.insert('',i,values=(i,co[1],co[10],co[11],co[7],cj))
                i = i+1
        myadda()
        #教师信息管理

























        def myadda2():

            # tree.configure(columns=('c1', 'c2', 'c3', 'c4', 'c5'))
            tree.column('c1', width=200, anchor='center')

            tree.column('c2', width=200, anchor='center')
            tree.column('c3', width=200, anchor='center')
            tree.column('c4', width=200, anchor='center')
            tree.column('c5', width=200, anchor='center')
            tree.column('c6', width=200, anchor='center')

            tree.heading('c1', text='编号')

            tree.heading('c2', text='教师编号')
            tree.heading('c3', text='姓名')
            tree.heading('c4', text='项目')
            tree.heading('c5', text='成绩')
            tree.heading('c6', text='')

            tree.pack(side=LEFT, fill=Y)

            scrollBar.config(command=tree.yview)


            # 定义并绑定Treeview组件的鼠标单击事件








            i = 1
            con = mysql("SELECT * FROM pc,project,teacher WHERE uid = tid and upid = pid")
            for co in con:
                cj = ""
                if co[4] == 0:
                    cj = "未通过管理员审核"
                if co[4] == 1:
                    cj = co[3]
                tree.insert('',i,values=(i,co[1],co[10],co[7],cj))
                i = i+1













































        adminwin.mainloop()
    #------------------------------------------------------------------------------教师窗口
    if teachername != None:
        tcwin = Tk()

        sw = tcwin.winfo_screenwidth()

        sh = tcwin.winfo_screenheight()
        x = (sw - 1000) / 2

        y = (sh - 500) / 2

        tcwin.geometry("%dx%d+%d+%d" % (1000, 500, x, y))

        tcwin.title('教师报名')

        tcwin.resizable(width=False, height=False)

        frame = Frame(tcwin)
        frame.place(x=0, y=25, width=1000, height=500)

        scrollBar = Scrollbar(frame)

        scrollBar.pack(side=RIGHT, fill=Y)

        tree = Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5'), show="headings",
                        yscrollcommand=scrollBar.set)

        tree.column('c1', width=200, anchor='center')

        tree.column('c2', width=200, anchor='center')
        tree.column('c3', width=200, anchor='center')
        tree.column('c4', width=200, anchor='center')
        tree.column('c5', width=200, anchor='center')

        tree.heading('c1', text='编号')

        tree.heading('c2', text='教师编号')
        tree.heading('c3', text='姓名')
        tree.heading('c4', text='项目')
        tree.heading('c5', text='成绩')

        tree.pack(side=LEFT, fill=Y)

        scrollBar.config(command=tree.yview)


        # 定义并绑定Treeview组件的鼠标单击事件

        def treeviewClick(event):
            pass


        tree.bind('<Button-1>', treeviewClick)

        Label(tcwin, text="已经报名项目以及成绩:").pack()


        def mydate2():
            pc = mysql("SELECT * FROM pc")
            i = 1
            for pc1 in pc:
                if pc1[1] == int(teachername):

                    name = mysql("SELECT * FROM teacher WHERE tid = " + teachername)
                    xm = mysql("SELECT * FROM project WHERE pid = " + str(pc1[2]))
                    cj = ""
                    if pc1[4] == 0:
                        cj = "未通过管理员审核"
                    if pc1[4] == 1:
                        cj = pc1[3]
                    tree.insert('', i, values=(i, teachername, name[0][1], xm[0][2], cj))
                    i=i+1

        mydate2()

        # 菜单

        menu = Menu(tcwin)
        pro = mysql("SELECT * FROM project")
        # fmenu1 = Menu(stuwin)
        # fmenu1.add_command(label="当前可报项目")
        fmenu2 = Menu(menu, tearoff=0)
        fmenu3 = Menu(menu, tearoff=0)
        # j=0
        for project in pro:
            fmenu2.add_command(label=project[2], command=lambda x=project[1]: baoming2(x))
            # j=j+1
            # fmenu2.add_separator()
            # Button(stuwin,text = project[2]).place(x = 50, y = 50,width = 60, height = 40)
        fmenu3.add_command(label="退出登录", command=restart_program)
        fmenu3.add_command(label="关闭程序", command=exit)

        menu.add_cascade(label="当前可报项目", menu=fmenu2)
        menu.add_cascade(label="退出", menu=fmenu3)
        tcwin['menu'] = menu
        tcwin.config(menu=menu)

        tcwin.mainloop()


