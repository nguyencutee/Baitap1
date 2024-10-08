import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu

win = tk.Tk()
win.geometry("400x300")
win.title("Tính tổng tiền điện")

def tinhtong():
    try:
        so_dien = float(a.get())
        so_nuoc = float(b.get())
        so_gas = float(c.get())
        if (so_dien <= 0 or so_nuoc <= 0 or so_gas <= 0):
            messagebox.showwarning("Lỗi", "Vui lòng nhập giá trị lớn hơn 0")
            return 
        tong_dien = so_dien * 3000
        tong_nuoc = so_nuoc * 50000
        tong_gas = so_gas * 20000
        tinh_tong= so_dien+so_nuoc+so_gas
        messagebox.showinfo("Kết quả", f"Tổng tiền điện: {tong_dien} VND\n"
                                       f"Tổng tiền nước: {tong_nuoc} VND\n"
                                       f"Tổng tiền gas: {tong_gas} VND\n"
                                       f"Tổng tiền : {tinh_tong} VND\n")                    
    except ValueError:
        # Nếu người dùng nhập sai, hiển thị lỗi
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng giá trị số!")
def reset():
        a.set(0)
        b.set(0)
        c.set(0)
tong_dien = 0
tong_nuoc = 0
tong_gas = 0

def exit():
    win.quit()
    exit()
def readme():
    messagebox.showerror("Hướng dẫn", "Nhập đầy đủ và đúng số liệu với định dạng số, không nhập ký tự chữ cái hay ký tự đặc biệt. Sau khi nhập xong nhấn tính tổng, hệ thống sẽ tính từng số tiền điện, nước, gas cho bạn. Nhấn nút xoá kết quả để đưa có số liệu về 0 và nhập lại")

buttons_frame = ttk.LabelFrame(win, text='Nhập liệu tiêu thụ')
buttons_frame.grid(column=0, row=0, padx=10, pady=10)
ttk.Label(buttons_frame, text="Nhập số điện tiêu thụ:").grid(column=0, row=1)
a = tk.StringVar()
ttk.Entry(buttons_frame, width=12, textvariable=a).grid(column=1, row=1)
ttk.Label(buttons_frame, text="Nhập số nước tiêu thụ:").grid(column=0, row=2)
b = tk.StringVar()
ttk.Entry(buttons_frame, width=12, textvariable=b).grid(column=1, row=2)
ttk.Label(buttons_frame, text="Nhập số ga tiêu thụ:").grid(column=0, row=3)
c = tk.StringVar()
ttk.Entry(buttons_frame, width=12, textvariable=c).grid(column=1, row=3)
tinh_button = ttk.Button(win, text="Tính tổng", command=tinhtong)
tinh_button.grid(column=0, row=4, columnspan=3)  
reset_button = ttk.Button(win, text="Xoá kết quả", command=reset)
reset_button.grid(column=0, row=5 )

menu_bar = Menu(win) 
win.config(menu=menu_bar)
file_menu = Menu(menu_bar)
file_menu.add_command(label="Readme", command=readme) 
file_menu.add_command(label="Exit", command=exit) 
menu_bar.add_cascade(label="Menu", menu=file_menu)
win.mainloop()
