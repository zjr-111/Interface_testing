import tkinter as tk
import os

root = tk.Tk()
root.title("计数窗口")

# 纵向窗口大小
root.geometry("190x180+1710+0")
'''
# 横向窗口大小
root.geometry("700x30+600+0")
'''
root.wm_attributes("-topmost", 1)

def save_text(name, text):
    with open(name, 'w', encoding='utf-8') as file:
        file.write(text)

def delete_file(name):
    if os.path.exists(name):
        os.remove(name)

def load_text(name):
    with open(name, 'r', encoding='utf-8') as file:
        text = file.read()
        return text
def jiancha(name):
    path_obs = os.path.dirname(os.path.abspath(__file__))
    path_txt = path_obs + '\\' + name
    obs_result = os.path.exists(path_txt)
    return obs_result
# 开始的数量
if jiancha("巨须裂腹鱼数量.txt") == True:
    a = int(load_text("巨须裂腹鱼数量.txt"))
else:
    a = 0

if jiancha("异齿裂腹鱼数量.txt") == True:
    b = int(load_text("异齿裂腹鱼数量.txt"))
else:
    b = 0

if jiancha("拉萨裂腹鱼数量.txt") == True:
    c = int(load_text("拉萨裂腹鱼数量.txt"))
else:
    c = 0

if jiancha("尖裸鲤数量.txt") == True:
    d = int(load_text("尖裸鲤数量.txt"))
else:
    d = 0

if jiancha("拉萨裸裂尻数量.txt") == True:
    e = int(load_text("拉萨裸裂尻数量.txt"))
else:
    e = 0
# 定义增加的函数
def fish_add(fish) :
    global a, b, c, d, e
    if fish == "a":
        a += 1
        save_text("巨须裂腹鱼数量.txt", str(a))
        label1.config(text=a)
    elif fish == "b":
        b += 1
        save_text("异齿裂腹鱼数量.txt", str(b))
        label2.config(text=b)
    elif fish == "c":
        c += 1
        save_text("拉萨裂腹鱼数量.txt", str(c))
        label3.config(text=c)
    elif fish == "d":
        d += 1
        save_text("尖裸鲤数量.txt", str(d))
        label4.config(text=d)
    elif fish == "e":
        e += 1
        save_text("拉萨裸裂尻数量.txt", str(e))
        label5.config(text=e)

# 定义清空的函数
def clear_num():
    global a, b, c, d, e
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    if jiancha("巨须裂腹鱼数量.txt") == True:
        delete_file("巨须裂腹鱼数量.txt")
    if jiancha("异齿裂腹鱼数量.txt") == True:
        delete_file("异齿裂腹鱼数量.txt")
    if jiancha("拉萨裂腹鱼数量.txt") == True:
        delete_file("拉萨裂腹鱼数量.txt")
    if jiancha("尖裸鲤数量.txt") == True:
        delete_file("尖裸鲤数量.txt")
    if jiancha("拉萨裸裂尻数量.txt") == True:
        delete_file("拉萨裸裂尻数量.txt")
    label1.config(text=a)
    label2.config(text=b)
    label3.config(text=c)
    label4.config(text=d)
    label5.config(text=e)

# 增加按钮和标签
button1 = tk.Button(root, text="巨须裂腹鱼", command=lambda: fish_add("a"))
button2 = tk.Button(root, text="异齿裂腹鱼", command=lambda: fish_add("b"))
button3 = tk.Button(root, text="拉萨裂腹鱼", command=lambda: fish_add("c"))
button4 = tk.Button(root, text="尖裸鲤", command=lambda: fish_add("d"))
button5 = tk.Button(root, text="拉萨裸裂尻", command=lambda: fish_add("e"))
button6 = tk.Button(root, text="清空数据，慎点！！", command=lambda: clear_num())
label1 = tk.Label(root, text=a)
label2 = tk.Label(root, text=b)
label3 = tk.Label(root, text=c)
label4 = tk.Label(root, text=d)
label5 = tk.Label(root, text=e)

# 纵向布局
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)
button5.grid(row=4, column=0)
button6.grid(row=5, column=1)
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
label3.grid(row=2, column=1)
label4.grid(row=3, column=1)
label5.grid(row=4, column=1)
'''
# 横向布局
button1.grid(row=0, column=0)
button2.grid(row=0, column=2)
button3.grid(row=0, column=4)
button4.grid(row=0, column=6)
button5.grid(row=0, column=8)
button6.grid(row=0, column=10)
label1.grid(row=0, column=1)
label2.grid(row=0, column=3)
label3.grid(row=0, column=5)
label4.grid(row=0, column=7)
label5.grid(row=0, column=9)
'''
# 展示
root.mainloop()