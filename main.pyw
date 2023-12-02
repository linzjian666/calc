# -*- coding: UTF-8 -*-
'''
Author: Linzjian666
Date: 2023-12-02 21:02:50
LastEditors: Linzjian666
LastEditTime: 2023-12-02 22:03:55
'''
import tkinter as tk

def button_click(event):
    # 获取按钮上的文本
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            # 计算结果
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        # 删除最后一个字符
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        # 在输入框中添加按钮上的文本
        entry.insert(tk.END, text)

# 创建窗口
window = tk.Tk()
window.title("计算器")

# 创建输入框
entry = tk.Entry(window, bd=4, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# 创建按钮
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "←"  # 添加退格按钮
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(window, text=button, bd=4,font=("Arial", 15), padx=10, pady=10)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 运行窗口主循环
window.mainloop()
