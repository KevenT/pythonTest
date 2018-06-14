# encoding: UTF-8
import requests
import json
#import os
#import time
from tkinter import *
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
#from multiprocessing import Process, Pool
import threading
from tkinter import messagebox

global control
control = 1


def removeBom(file):
    '''移除UTF-8文件的BOM字节'''
    BOM = b'\xef\xbb\xbf'
    existBom = lambda s: True if s == BOM else False

    f = open(file, 'rb')
    if existBom(f.read(3)):
        fbody = f.read()
        # f.close()
        with open(file, 'wb') as f:
            f.write(fbody)

#从官网下载json文件到目录下
urlJson = 'http://pvp.qq.com/web201605/js/herolist.json'
JsonFile = requests.get(urlJson).content
JsonFile = JsonFile.decode('utf-8-sig')
with open('herolist.json','wb') as f:
    f.write(JsonFile.encode())
    #f.write(JsonFile)


# 读取json文件
with open('herolist.json', 'r', encoding='utf-8') as ff:  # read
    jsonFile = json.load(ff)

def download():#下载皮肤
    heroname=ent.get()
    skiname=numberChosen.get()
    for m in range(len(jsonFile)):
        ename = jsonFile[m]['ename']
        cname = jsonFile[m]['cname']
        print(cname)
        skinName = jsonFile[m]['skin_name'].split('|')
        skinNumber = len(skinName)
        if cname == heroname:
            for bigskin in range(1, skinNumber + 1):
                if skiname == skinName[bigskin - 1]:
                    urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(bigskin) + '.jpg'
                    #    获取图片信息  图片都是二进制  content就是获取二级制信息
                    picture = requests.get(urlPicture).content
                    # 保存信息 保存图片
                    filename = tkinter.filedialog.asksaveasfilename(filetypes = [('','.jpg')],initialfile = skiname)
                    if filename:
                        with open(filename + '.jpg', 'wb') as f:
                            f.write(picture)
                        messagebox.showinfo(title='提示', message='下载成功！')
                    break
            break

def downloadskin():#下载皮肤
    heroname=ent.get()
    #skiname=numberChosen.get()
    for m in range(len(jsonFile)):
        ename = jsonFile[m]['ename']
        cname = jsonFile[m]['cname']
        print(cname)
        skinName = jsonFile[m]['skin_name'].split('|')
        skinNumber = len(skinName)
        if cname == heroname:
            bigskin =skinNumber + 1
            urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(bigskin) + '.jpg'
            #    获取图片信息  图片都是二进制  content就是获取二级制信息
            getpicture = requests.get(urlPicture)
            picture = getpicture.content
            picturer = getpicture.status_code
            if picturer == 404:
                messagebox.showinfo(title='提示', message='没有找到隐藏皮肤！')
                break
            else :
                # 保存信息 保存图片
                hideskin=str(cname)+'隐藏皮肤'
                filename = tkinter.filedialog.asksaveasfilename(filetypes=[('', '.jpg')], initialfile=hideskin)
                if filename:
                    with open(filename + '.jpg', 'wb') as f:
                        f.write(picture)
                    messagebox.showinfo(title='提示', message='下载成功！')
                    break

def fun_timer():#刷新下拉列表用的
    global timer
    print('Hello Timer!')
    k=len(jsonFile)
    for m in range(0,k):
        s=0
        cname = jsonFile[m]['cname']
        if cname ==ent.get():
            s=1
            numberChosen['values'] = jsonFile[m]['skin_name'].split('|')
            break
    if s==0:
        numberChosen['values'] = ('英雄不存在！')
    if control:
        timer = threading.Timer(0.5, fun_timer)
        timer.start()



#创建一个窗口
root = Tk()
root.title('英雄皮肤下载')
root.geometry('250x100+1000+500')

#标题
ttk.Label(root, text="输入英雄名字：",width=12).grid()      # 设置其在界面中出现的位置  column代表列   row 代表行
#ttk.Label(root, text="列表中没有？", width=12).grid(column = 2,row = 2)  # 设置其在界面中出现的位置  column代表列   row 代表行

#输入框
ent = Entry(root,width=14)
ent.grid()
ent.delete(0,END)

#下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(root, width=12, textvariable=number)
#numberChosen['values'] = (0,1,2,3)  # 设置下拉列表的值
numberChosen.grid()  # 设置其在界面中出现的位置  column代表列   row 代表行

#按钮
btn_download = Button(root,text=' 下 载 ',command=download)
btn_download.grid(column = 0,row = 4)

btn_download = Button(root,text=' 下载隐藏皮肤 ',command=downloadskin)
btn_download.grid(column = 1,row = 4)

timer = threading.Timer(0.5, fun_timer)
timer.start()

root.mainloop()

control = 0
timer.cancel()
print("关闭")
