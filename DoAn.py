import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

itf = tk.Tk()
itf.title("Trình đọc dữ liệu giấc ngủ")
itf.geometry("1280x720")
itf.resizable(False, False)

fp=None

# Khung bên trái
left_background = tk.Frame(itf, width=300, bg="#b6dafa")
left_background.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Khung bên phải
right_background = tk.Frame(itf, width=600, bg="#858585")
right_background.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Thanh cuộn 
tree = ttk.Treeview(right_background, show="headings")
scrollbar_y = ttk.Scrollbar(right_background, orient="vertical", command=tree.yview)

scrollbar_x = ttk.Scrollbar(right_background, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")
tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Hàm chọn file
def choose_file():
    global fb
    file_path = filedialog.askopenfilename(title="Chọn tập dữ liệu", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))) 
    if file_path:
        if file_path.endswith(('.xls', '.xlsx')):
            try:
                fp = pd.read_excel(file_path)
                show_data(fp)
                messagebox.showinfo('Successful', "Đã đọc tệp tin thành công")
            except Exception as error:
                messagebox.showerror('Error', f"Lỗi: {error}")
        elif file_path.endswith('.csv'):
            try:
                fp = pd.read_csv(file_path)
                show_data(fp)
                messagebox.showinfo('Successful', "Đã đọc tệp tin thành công")
            except Exception as error:
                messagebox.showerror('Error', f"Không thể đọc được tệp, lỗi: {error}")
        else:
            messagebox.showerror('Lỗi định dạng', 'Định dạng file không hợp lệ, chỉ hỗ trợ file excel hoặc csv')

# Hàm hiển thị dữ liệu
def show_data(fp):
    tree.delete(*tree.get_children())
    tree["columns"] = list(fp.columns)
    
    # Chiều rộng tối thiểu cho Treeview
    min_column_width = 150  # Đặt chiều rộng tối thiểu
    for col in fp.columns:
        tree.heading(col, text=col)
        # Tự động tính toán chiều rộng dựa trên nội dung cột
        max_width = max(fp[col].astype(str).map(len).max(), len(col)) * 10
        tree.column(col, anchor="w", width=max(max_width, min_column_width))  # Chiều rộng tối thiểu
    for row in fp.itertuples(index=False):
        tree.insert("", "end", values=list(row))
    
    # Đảm bảo thanh cuộn ngang hiển thị nếu tổng chiều rộng cột > Treeview
    total_width = sum(tree.column(c)["width"] for c in tree["columns"])
    tree["show"] = "headings"

# Nút Chọn tập dữ liệu
box1 = tk.Button(left_background, text="Chọn tập dữ liệu", command=choose_file, font=("Arial", 12, "bold"), bg='#37d451', width=20, height=2)
box1.pack(padx=10, pady=3)
# Nút xóa dữ liệu cũ
box2 = tk.Button(left_background, text="Xóa dòng dữ liệu", font=("Arial", 12, "bold"), bg='#c94949', width=20, height=2)
box2.pack(padx=10, pady=3)
# Nút chỉnh sửa dữ liệu
box3 = tk.Button(left_background, text="Chỉnh sửa", font=("Arial", 12, "bold"), bg='#e0ff45', width=20, height=2)
box3.pack(padx=10, pady=3)
# Sample 1
box4 = tk.Button(left_background, text="Thống kê số người ngủ đủ ở độ tuổi của mình", font=("Arial", 12, "bold"), bg='#36bab4', width=50, height=2)
box4.pack(padx=10, pady=3)
# Sample 2
box5 = tk.Button(left_background, text="Thống kê những người đang có sức khỏe mức báo động", font=("Arial", 12, "bold"), bg='#36bab4', width=50, height=2)
box5.pack(padx=10, pady=3)
# Sample 3
box6 = tk.Button(left_background, text="Tỉ lệ những người gặp vấn đề về giấc ngủ", font=("Arial", 12, "bold"), bg='#36bab4', width=50, height=2)
box6.pack(padx=10, pady=3)
# Sample 4
box7 = tk.Button(left_background, text="Tỉ lệ người duy trì chất lượng cuộc sống ở các mức độ", font=("Arial", 12, "bold"), bg='#36bab4', width=50, height=2)
box7.pack(padx=10, pady=3)

itf.mainloop()
