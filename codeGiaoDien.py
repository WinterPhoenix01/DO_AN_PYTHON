import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Import kết nối CSDL từ tệp codeCSDL.py
from codeCSDL import connect_db, init_database


# ==========================================
# 1. FRAME TRANG CHỦ / GIỚI THIỆU ĐỒ ÁN
# ==========================================
class TrangChuFrame(tk.Frame):
    """Trang chủ thân thiện, dễ sử dụng cho giáo viên."""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f3f6fb")
        self.controller = controller

        # Thanh tiêu đề
        header = tk.Frame(self, bg="#174a7e", height=105)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="TRƯỜNG HỌC SỐ", bg="#174a7e", fg="#ffffff",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=32, pady=(17, 2))
        tk.Label(
            header, text="HỆ THỐNG QUẢN LÝ HỌC SINH",
            bg="#174a7e", fg="#ffffff", font=("Segoe UI", 20, "bold")
        ).pack(anchor="w", padx=32)
        tk.Label(
            header, text="Đơn giản hóa công việc quản lý lớp học và kết quả học tập",
            bg="#174a7e", fg="#dbeafe", font=("Segoe UI", 10)
        ).pack(anchor="w", padx=33, pady=(2, 0))

        # Nội dung trang chủ
        content = tk.Frame(self, bg="#f3f6fb")
        content.pack(fill="both", expand=True, padx=32, pady=22)

        intro = tk.Frame(content, bg="#f3f6fb")
        intro.pack(fill="x", pady=(0, 16))
        tk.Label(
            intro, text="Xin chào, Thầy/Cô!", bg="#f3f6fb", fg="#172b4d",
            font=("Segoe UI", 19, "bold")
        ).pack(anchor="w")
        tk.Label(
            intro, text="Chọn chức năng bên dưới để bắt đầu công việc của mình.",
            bg="#f3f6fb", fg="#64748b", font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(4, 0))

        # Thẻ trạng thái
        status_card = tk.Frame(content, bg="#ffffff", highlightbackground="#dce5f0",
                               highlightthickness=1)
        status_card.pack(fill="x", pady=(0, 18))
        status_left = tk.Frame(status_card, bg="#ffffff")
        status_left.pack(side="left", fill="x", expand=True, padx=18, pady=15)
        tk.Label(
            status_left, text="TRẠNG THÁI TÀI KHOẢN", bg="#ffffff",
            fg="#64748b", font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")
        self.lbl_status = tk.Label(
            status_left, text="Chưa đăng nhập · Thầy/Cô vui lòng đăng nhập để sử dụng chức năng quản lý",
            bg="#ffffff", fg="#b45309", font=("Segoe UI", 10), anchor="w",
            justify="left", wraplength=650
        )
        self.lbl_status.pack(anchor="w", pady=(5, 0))

        self.btn_login_main = tk.Button(
            status_card, text="Đăng nhập", font=("Segoe UI", 10, "bold"),
            bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8",
            activeforeground="#ffffff", bd=0, cursor="hand2",
            padx=22, pady=10, command=self.controller.show_login_dialog
        )
        self.btn_login_main.pack(side="right", padx=18, pady=16)

        tk.Label(
            content, text="CHỨC NĂNG QUẢN LÝ", bg="#f3f6fb", fg="#334155",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 10))

        # Các lối tắt được trình bày thành thẻ dễ nhận biết
        cards = tk.Frame(content, bg="#f3f6fb")
        cards.pack(fill="x")
        cards.grid_columnconfigure((0, 1), weight=1, uniform="feature")

        features = [
            ("01", "Hồ sơ học sinh", "Quản lý thông tin cá nhân, lớp học và danh sách học sinh.",
             "#2563eb", lambda: self.controller.show_frame("HocSinhFrame")),
            ("02", "Nhập điểm", "Cập nhật điểm kiểm tra và theo dõi điểm trung bình.",
             "#0f766e", lambda: self.controller.show_frame("NhapDiemFrame")),
            ("03", "Thống kê & báo cáo", "Xem số liệu tổng quan và kết quả học tập.",
             "#7c3aed", lambda: self.controller.show_frame("ThongKeFrame")),
            ("04", "Danh mục lớp học", "Quản lý lớp học và thông tin danh mục liên quan.",
             "#b45309", lambda: self.controller.open_danhmuc_tab(0)),
        ]

        for index, (number, title, description, accent, command) in enumerate(features):
            r, c = divmod(index, 2)
            card = tk.Frame(cards, bg="#ffffff", highlightbackground="#dce5f0",
                            highlightthickness=1)
            card.grid(row=r, column=c, sticky="nsew", padx=(0, 9) if c == 0 else (9, 0),
                      pady=(0, 14), ipadx=8, ipady=8)
            tk.Label(
                card, text=number, bg=accent, fg="#ffffff",
                font=("Segoe UI", 10, "bold"), padx=10, pady=5
            ).pack(anchor="w", padx=15, pady=(13, 8))
            tk.Label(
                card, text=title, bg="#ffffff", fg="#172b4d",
                font=("Segoe UI", 12, "bold")
            ).pack(anchor="w", padx=15)
            tk.Label(
                card, text=description, bg="#ffffff", fg="#64748b",
                font=("Segoe UI", 9), justify="left", wraplength=420
            ).pack(anchor="w", padx=15, pady=(5, 12))
            tk.Button(
                card, text="Mở chức năng  →", font=("Segoe UI", 9, "bold"),
                bg="#eef4ff", fg=accent, activebackground="#dbeafe",
                bd=0, cursor="hand2", padx=12, pady=7, command=command
            ).pack(anchor="w", padx=15, pady=(0, 10))

        footer = tk.Frame(content, bg="#f3f6fb")
        footer.pack(fill="x", pady=(2, 0))
        tk.Label(
            footer, text="Gợi ý: Đăng nhập để mở khóa các chức năng quản lý.",
            bg="#f3f6fb", fg="#64748b", font=("Segoe UI", 9, "italic")
        ).pack(anchor="w")

    def update_status(self):
        """Cập nhật trạng thái đăng nhập trên trang chủ."""
        if self.controller.is_logged_in:
            self.lbl_status.config(
                text=f"Đã đăng nhập với tài khoản: {self.controller.current_user}",
                fg="#15803d"
            )
            self.btn_login_main.config(
                text="Đăng xuất", bg="#dc2626", activebackground="#b91c1c",
                command=self.controller.do_logout
            )
        else:
            self.lbl_status.config(
                text="Chưa đăng nhập · Thầy/Cô vui lòng đăng nhập để sử dụng chức năng quản lý",
                fg="#b45309"
            )
            self.btn_login_main.config(
                text="Đăng nhập", bg="#2563eb", activebackground="#1d4ed8",
                command=self.controller.show_login_dialog
            )


# ==========================================
# 2. FRAME QUẢN LÝ HỌC SINH (NGHIỆP VỤ HỒ SƠ)
# ==========================================
class HocSinhFrame(tk.Frame):
    """Giao diện quản lý thông tin chi tiết học sinh"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg="#F3F6FA")
        self.controller = controller
        self.action_mode = ''

        self.create_widgets()
        self.load_combobox_data()
        self.set_input_state('disabled')

    def create_widgets(self):
        lbl_title = tk.Label(self, text="QUẢN LÝ HỌC SINH", font=("Arial", 17, "bold"), fg="#173F67", bg="#F3F6FA")
        lbl_title.pack(pady=10)

        frame_form = tk.LabelFrame(self, text=" Thông tin chi tiết học sinh ", font=("Arial", 10, "bold"), fg="#173F67", bg="#FFFFFF")
        frame_form.pack(padx=20, pady=5, fill="x", ipadx=10, ipady=5)

        frame_form.columnconfigure(1, weight=1)
        frame_form.columnconfigure(3, weight=1)

        # Hàng 1
        tk.Label(frame_form, text="Mã học sinh:", font=("Times New Roman", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=6)
        self.entry_mahs = tk.Entry(frame_form, width=32, font=("Arial", 10))
        self.entry_mahs.grid(row=0, column=1, sticky="w", padx=(5, 30), pady=6)

        tk.Label(frame_form, text="Họ tên:", font=("Times New Roman", 10)).grid(row=0, column=2, sticky="w", padx=10, pady=6)
        self.entry_hoten = tk.Entry(frame_form, width=42, font=("Arial", 10))
        self.entry_hoten.grid(row=0, column=3, sticky="w", padx=(5, 10), pady=6)

        # Hàng 2
        tk.Label(frame_form, text="Giới tính:", font=("Times New Roman", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=6)
        frame_gender = tk.Frame(frame_form)
        frame_gender.grid(row=1, column=1, sticky="w", padx=(5, 30), pady=6)
        self.var_gioitinh = tk.StringVar(value="Nam")
        self.rad_nam = tk.Radiobutton(frame_gender, text="Nam", variable=self.var_gioitinh, value="Nam", font=("Times New Roman", 10))
        self.rad_nu = tk.Radiobutton(frame_gender, text="Nữ", variable=self.var_gioitinh, value="Nữ", font=("Times New Roman", 10))
        self.rad_nam.pack(side="left", padx=(0, 20))
        self.rad_nu.pack(side="left")

        tk.Label(frame_form, text="Ngày sinh:", font=("Times New Roman", 10)).grid(row=1, column=2, sticky="w", padx=10, pady=6)
        self.entry_ngaysinh = DateEntry(
            frame_form, 
            width=39, 
            font=("Times New Roman", 10), 
            date_pattern='dd/mm/yyyy', 
            background='darkblue', 
            foreground='white', 
            headersbackground='lightgray'
        )
        self.entry_ngaysinh.grid(row=1, column=3, sticky="w", padx=(5, 10), pady=6)

        # Hàng 3
        tk.Label(frame_form, text="Nơi sinh:", font=("Times New Roman", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=6)
        self.entry_noisinh = tk.Entry(frame_form, width=32, font=("Arial", 10))
        self.entry_noisinh.grid(row=2, column=1, sticky="w", padx=(5, 30), pady=6)

        tk.Label(frame_form, text="Dân tộc:", font=("Times New Roman", 10)).grid(row=2, column=2, sticky="w", padx=10, pady=6)
        self.cbo_dantoc = ttk.Combobox(frame_form, width=40, font=("Arial", 10), state="readonly")
        self.cbo_dantoc.grid(row=2, column=3, sticky="w", padx=(5, 10), pady=6)

        # Hàng 4
        tk.Label(frame_form, text="Tôn giáo:", font=("Times New Roman", 10)).grid(row=3, column=0, sticky="w", padx=10, pady=6)
        self.cbo_tongiao = ttk.Combobox(frame_form, width=30, font=("Times New Roman", 10), state="readonly")
        self.cbo_tongiao.grid(row=3, column=1, sticky="w", padx=(5, 30), pady=6)

        tk.Label(frame_form, text="Lớp học:", font=("Times New Roman", 10)).grid(row=3, column=2, sticky="w", padx=10, pady=6)
        self.cbo_lophoc = ttk.Combobox(frame_form, width=40, font=("Times New Roman", 10), state="readonly")
        self.cbo_lophoc.grid(row=3, column=3, sticky="w", padx=(5, 10), pady=6)

        # Nút thao tác
        frame_action_search = tk.Frame(self, bg="#F3F6FA")
        frame_action_search.pack(padx=20, pady=10, fill="x")

        frame_buttons = tk.Frame(frame_action_search, bg="#F3F6FA")
        frame_buttons.pack(side="left")

        self.btn_them = tk.Button(frame_buttons, text="Thêm", width=8, font=("Times New Roman", 9, "bold"), bg="#e8f8f5", command=self.cmd_them)
        self.btn_them.pack(side="left", padx=2)

        self.btn_sua = tk.Button(frame_buttons, text="Sửa", width=8, font=("Times New Roman", 9, "bold"), bg="#fef9e7", command=self.cmd_sua)
        self.btn_sua.pack(side="left", padx=2)

        self.btn_xoa = tk.Button(frame_buttons, text="Xóa", width=8, font=("Times New Roman", 9, "bold"), bg="#fadbd8", command=self.cmd_xoa)
        self.btn_xoa.pack(side="left", padx=2)

        self.btn_luu = tk.Button(frame_buttons, text="Lưu", width=8, font=("Times New Roman", 9, "bold"), bg="#eafaf1", command=self.cmd_luu, state="disabled")
        self.btn_luu.pack(side="left", padx=2)

        self.btn_huy = tk.Button(frame_buttons, text="Hủy", width=8, font=("Times New Roman", 9, "bold"), command=self.cmd_huy, state="disabled")
        self.btn_huy.pack(side="left", padx=2)

        btn_thongke = tk.Button(frame_buttons, text="Thống kê", width=9, font=("Times New Roman", 9, "bold"), bg="#ebdef0", fg="#512e5f", command=lambda: self.controller.show_frame("ThongKeFrame"))
        btn_thongke.pack(side="left", padx=5)

        self.btn_trangchu = tk.Button(frame_buttons, text="Trang chủ", width=9, font=("Times New Roman", 9, "bold"), command=lambda: self.controller.show_frame("TrangChuFrame"))
        self.btn_trangchu.pack(side="left", padx=2)

        # Tìm kiếm
        frame_search = tk.Frame(frame_action_search, bg="#F3F6FA")
        frame_search.pack(side="right")

        tk.Label(frame_search, text="Tìm kiếm:", font=("Times New Roman", 10)).pack(side="left", padx=(0, 5))
        self.entry_search = tk.Entry(frame_search, width=20, font=("Times New Roman", 10))
        self.entry_search.pack(side="left", padx=(0, 5))
        self.entry_search.bind("<KeyRelease>", lambda event: self.load_data())

        btn_search = tk.Button(frame_search, text="Tìm", width=6, font=("Times New Roman", 9), command=self.load_data)
        btn_search.pack(side="left", padx=2)

        btn_show_all = tk.Button(frame_search, text="Tất cả", width=6, font=("Times New Roman", 9), command=self.cmd_show_all)
        btn_show_all.pack(side="left", padx=2)

        # Bảng hiển thị
        lbl_list = tk.Label(self, text="Danh sách học sinh", font=("Times New Roman", 11, "bold"), fg="#1b4f72")
        lbl_list.pack(anchor="w", padx=20, pady=(5, 2))

        columns = ("mahs", "hoten", "phai", "ngaysinh", "noisinh", "dantoc", "tongiao", "malop")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=13)

        self.tree.heading("mahs", text="Mã HS")
        self.tree.heading("hoten", text="Họ tên")
        self.tree.heading("phai", text="Phái")
        self.tree.heading("ngaysinh", text="Ngày sinh")
        self.tree.heading("noisinh", text="Nơi sinh")
        self.tree.heading("dantoc", text="Dân tộc")
        self.tree.heading("tongiao", text="Tôn giáo")
        self.tree.heading("malop", text="Lớp")

        self.tree.column("mahs", width=90, anchor="center")
        self.tree.column("hoten", width=200, anchor="w")
        self.tree.column("phai", width=70, anchor="center")
        self.tree.column("ngaysinh", width=110, anchor="center")
        self.tree.column("noisinh", width=150, anchor="w")
        self.tree.column("dantoc", width=90, anchor="center")
        self.tree.column("tongiao", width=100, anchor="w")
        self.tree.column("malop", width=80, anchor="center")

        self.tree.pack(padx=20, pady=(0, 15), fill="both", expand=True)
        self.tree.tag_configure("oddrow", background="#FFFFFF")
        self.tree.tag_configure("evenrow", background="#F4F8FC")
        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

    def load_combobox_data(self):
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("SELECT tendantoc FROM dantoc")
            self.cbo_dantoc['values'] = [r[0] for r in c.fetchall()]

            c.execute("SELECT tentongiao FROM tongiao")
            self.cbo_tongiao['values'] = [r[0] for r in c.fetchall()]

            c.execute("SELECT malop FROM lophoc")
            self.cbo_lophoc['values'] = [r[0] for r in c.fetchall()]
            conn.close()
        except Exception:
            pass

    def set_input_state(self, state):
        self.entry_mahs.config(state=state)
        self.entry_hoten.config(state=state)
        self.rad_nam.config(state=state)
        self.rad_nu.config(state=state)
        self.entry_ngaysinh.config(state=state)
        self.entry_noisinh.config(state=state)
        
        combo_state = "readonly" if state == "normal" else "disabled"
        self.cbo_dantoc.config(state=combo_state)
        self.cbo_tongiao.config(state=combo_state)
        self.cbo_lophoc.config(state=combo_state)

    def clear_inputs(self):
        self.set_input_state('normal')
        self.entry_mahs.delete(0, tk.END)
        self.entry_hoten.delete(0, tk.END)
        self.var_gioitinh.set("Nam")
        self.entry_ngaysinh.delete(0, tk.END)
        self.entry_noisinh.delete(0, tk.END)
        self.cbo_dantoc.set('')
        self.cbo_tongiao.set('')
        self.cbo_lophoc.set('')

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        search_kw = getattr(self, 'entry_search', None)
        keyword = search_kw.get().strip() if search_kw else ''

        try:
            conn = connect_db()
            c = conn.cursor()
            if keyword:
                sql = """SELECT mahs, hoten, phai, ngaysinh, noisinh, dantoc, tongiao, malop
                         FROM hocsinh
                         WHERE CAST(mahs AS TEXT) LIKE ? OR hoten LIKE ? OR malop LIKE ?
                         ORDER BY CAST(mahs AS INTEGER) ASC, mahs ASC"""
                param = f"%{keyword}%"
                c.execute(sql, (param, param, param))
            else:
                c.execute("""SELECT mahs, hoten, phai, ngaysinh, noisinh, dantoc, tongiao, malop
                           FROM hocsinh
                           ORDER BY CAST(mahs AS INTEGER) ASC, mahs ASC""")
            for row in c.fetchall():
                self.tree.insert("", tk.END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Lỗi CSDL", f"Không thể tải dữ liệu: {e}")

    def cmd_show_all(self):
        if hasattr(self, 'entry_search'):
            self.entry_search.delete(0, tk.END)
        self.load_data()
        
    def fill_form_from_selection(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            vals = item['values']
            self.clear_inputs()
            self.entry_mahs.insert(0, vals[0])
            self.entry_hoten.insert(0, vals[1])
            self.var_gioitinh.set(vals[2])
            try:
                date_obj = datetime.strptime(str(vals[3]), "%d/%m/%Y").date()
                self.entry_ngaysinh.set_date(date_obj)
            except Exception:
                pass
            self.entry_noisinh.insert(0, vals[4])
            self.cbo_dantoc.set(vals[5] if vals[5] else '')
            self.cbo_tongiao.set(vals[6] if vals[6] else '')
            self.cbo_lophoc.set(vals[7] if vals[7] else '')

    def on_select_row(self, event):
        if self.action_mode != '':
            return
        self.fill_form_from_selection()
        self.set_input_state('disabled')

    def cmd_them(self):
        self.action_mode = 'them'
        self.clear_inputs()
        self.entry_mahs.focus()
        self.btn_them.config(state='disabled')
        self.btn_sua.config(state='disabled')
        self.btn_xoa.config(state='disabled')
        self.btn_luu.config(state='normal')
        self.btn_huy.config(state='normal')

    def cmd_sua(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn 1 học sinh trong bảng để sửa!")
            return
        self.action_mode = 'sua'
        self.set_input_state('normal')
        self.entry_mahs.config(state='disabled')
        self.entry_hoten.focus()
        self.btn_them.config(state='disabled')
        self.btn_sua.config(state='disabled')
        self.btn_xoa.config(state='disabled')
        self.btn_luu.config(state='normal')
        self.btn_huy.config(state='normal')

    def cmd_luu(self):
        ma_hs = self.entry_mahs.get().strip()
        ho_ten = self.entry_hoten.get().strip()
        gioi_tinh = self.var_gioitinh.get()
        ngay_sinh = self.entry_ngaysinh.get().strip()
        noi_sinh = self.entry_noisinh.get().strip()
        dan_toc = self.cbo_dantoc.get().strip()
        ton_giao = self.cbo_tongiao.get().strip()
        ma_lop = self.cbo_lophoc.get().strip()

        if not ma_hs or not ho_ten:
            messagebox.showwarning("Cảnh báo", "Mã học sinh và Họ tên không được để trống!")
            return

        try:
            conn = connect_db()
            c = conn.cursor()
            if self.action_mode == 'them':
                c.execute("SELECT * FROM hocsinh WHERE mahs = ?", (ma_hs,))
                if c.fetchone():
                    messagebox.showerror("Lỗi", "Mã học sinh này đã tồn tại!")
                    conn.close()
                    return
                sql = """INSERT INTO hocsinh (mahs, hoten, phai, ngaysinh, noisinh, dantoc, tongiao, malop)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                c.execute(sql, (ma_hs, ho_ten, gioi_tinh, ngay_sinh, noi_sinh, dan_toc, ton_giao, ma_lop))
                messagebox.showinfo("Thành công", "Thêm học sinh mới thành công!")
            elif self.action_mode == 'sua':
                sql = """UPDATE hocsinh 
                         SET hoten = ?, phai = ?, ngaysinh = ?, noisinh = ?, dantoc = ?, tongiao = ?, malop = ?
                         WHERE mahs = ?"""
                c.execute(sql, (ho_ten, gioi_tinh, ngay_sinh, noi_sinh, dan_toc, ton_giao, ma_lop, ma_hs))
                messagebox.showinfo("Thành công", "Cập nhật thông tin thành công!")
            conn.commit()
            conn.close()
            self.cmd_huy()
            self.load_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Thao tác thất bại: {e}")

    def cmd_huy(self):
        self.action_mode = ''
        self.clear_inputs()
        self.set_input_state('disabled')
        self.btn_them.config(state='normal')
        self.btn_sua.config(state='normal')
        self.btn_xoa.config(state='normal')
        self.btn_luu.config(state='disabled')
        self.btn_huy.config(state='disabled')

    def cmd_xoa(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn 1 học sinh cần xóa!")
            return
        item = self.tree.item(selected[0])
        ma_hs = item['values'][0]
        ho_ten = item['values'][1]
        confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa học sinh:\n{ho_ten} (Mã: {ma_hs})?")
        if confirm:
            try:
                conn = connect_db()
                c = conn.cursor()
                c.execute("DELETE FROM hocsinh WHERE mahs = ?", (ma_hs,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công", "Xóa học sinh thành công!")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể xóa dữ liệu: {e}")


# ==========================================
# 3. FRAME QUẢN LÝ DANH MỤC (LỚP, DÂN TỘC, TÔN GIÁO)
# ==========================================
class DanhMucFrame(tk.Frame):
    """Màn hình Quản lý các Bảng Danh mục hệ thống theo Tab"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg="#F3F6FA")
        self.controller = controller

        lbl_title = tk.Label(self, text="QUẢN LÝ DANH MỤC HỆ THỐNG", font=("Arial", 17, "bold"), fg="#173F67", bg="#F3F6FA")
        lbl_title.pack(pady=10)

        # Tab Control
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=20, pady=10, fill="both", expand=True)

        # Tab 1: Lớp học
        self.tab_lophoc = tk.Frame(self.notebook)
        self.notebook.add(self.tab_lophoc, text=" Danh mục Lớp học ")
        self.setup_tab_lophoc()

        # Tab 2: Dân tộc
        self.tab_dantoc = tk.Frame(self.notebook)
        self.notebook.add(self.tab_dantoc, text=" Danh mục Dân tộc ")
        self.setup_tab_dantoc()

        # Tab 3: Tôn giáo
        self.tab_tongiao = tk.Frame(self.notebook)
        self.notebook.add(self.tab_tongiao, text=" Danh mục Tôn giáo ")
        self.setup_tab_tongiao()

    # --- TAB LỚP HỌC ---
    def setup_tab_lophoc(self):
        f_top = tk.LabelFrame(self.tab_lophoc, text=" Thông tin Lớp học ", font=("Arial", 10, "bold"), fg="#173F67", bg="#FFFFFF")
        f_top.pack(padx=10, pady=10, fill="x")

        tk.Label(f_top, text="Mã lớp:", font=("Times New Roman", 10)).grid(row=0, column=0, padx=5, pady=5)
        self.ent_malop = tk.Entry(f_top, width=15)
        self.ent_malop.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(f_top, text="Tên lớp:", font=("Times New Roman", 10)).grid(row=0, column=2, padx=5, pady=5)
        self.ent_tenlop = tk.Entry(f_top, width=20)
        self.ent_tenlop.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(f_top, text="Năm học:", font=("Times New Roman", 10)).grid(row=1, column=0, padx=5, pady=5)
        self.ent_namhoc = tk.Entry(f_top, width=15)
        self.ent_namhoc.grid(row=1, column=1, padx=5, pady=5)
        self.ent_namhoc.insert(0, "2025-2026")

        tk.Label(f_top, text="GVCN:", font=("Times New Roman", 10)).grid(row=1, column=2, padx=5, pady=5)
        self.ent_gvcn = tk.Entry(f_top, width=20)
        self.ent_gvcn.grid(row=1, column=3, padx=5, pady=5)

        f_btn = tk.Frame(self.tab_lophoc)
        f_btn.pack(pady=5)
        tk.Button(f_btn, text="Thêm Lớp", font=("Times New Roman", 9, "bold"), bg="#e8f8f5", command=self.add_lop).pack(side="left", padx=5)
        tk.Button(f_btn, text="Xóa Lớp", font=("Times New Roman", 9, "bold"), bg="#fadbd8", command=self.delete_lop).pack(side="left", padx=5)

        cols = ("malop", "tenlop", "namhoc", "gvcn")
        self.tree_lop = ttk.Treeview(self.tab_lophoc, columns=cols, show="headings", height=8)
        self.tree_lop.heading("malop", text="Mã Lớp")
        self.tree_lop.heading("tenlop", text="Tên Lớp")
        self.tree_lop.heading("namhoc", text="Năm Học")
        self.tree_lop.heading("gvcn", text="Giáo Viên Chủ Nhiệm")
        self.tree_lop.pack(padx=10, pady=5, fill="both", expand=True)

    def load_lophoc(self):
        for item in self.tree_lop.get_children():
            self.tree_lop.delete(item)
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("SELECT malop, tenlop, namhoc, gvcn FROM lophoc")
            for r in c.fetchall():
                self.tree_lop.insert("", tk.END, values=r)
            conn.close()
        except Exception:
            pass

    def add_lop(self):
        ml = self.ent_malop.get().strip()
        tl = self.ent_tenlop.get().strip()
        nh = self.ent_namhoc.get().strip()
        gv = self.ent_gvcn.get().strip()
        if not ml or not tl:
            messagebox.showwarning("Cảnh báo", "Mã lớp và Tên lớp không được để trống!")
            return
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO lophoc VALUES (?, ?, ?, ?)", (ml, tl, nh, gv))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành công", "Thêm lớp học thành công!")
            self.load_lophoc()
            self.controller.refresh_all_comboboxes()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm lớp: {e}")

    def delete_lop(self):
        sel = self.tree_lop.selection()
        if not sel:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn 1 lớp để xóa!")
            return
        ml = self.tree_lop.item(sel[0])['values'][0]
        if messagebox.askyesno("Xác nhận", f"Xóa lớp {ml}?"):
            try:
                conn = connect_db()
                c = conn.cursor()
                c.execute("DELETE FROM lophoc WHERE malop = ?", (ml,))
                conn.commit()
                conn.close()
                self.load_lophoc()
                self.controller.refresh_all_comboboxes()
            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

    # --- TAB DÂN TỘC ---
    def setup_tab_dantoc(self):
        f_top = tk.Frame(self.tab_dantoc)
        f_top.pack(pady=10)
        tk.Label(f_top, text="Tên Dân tộc:", font=("Times New Roman", 10)).pack(side="left", padx=5)
        self.ent_dantoc = tk.Entry(f_top, width=25)
        self.ent_dantoc.pack(side="left", padx=5)
        tk.Button(f_top, text="Thêm", font=("Times New Roman", 9, "bold"), bg="#e8f8f5", command=self.add_dantoc).pack(side="left", padx=5)
        tk.Button(f_top, text="Xóa", font=("Times New Roman", 9, "bold"), bg="#fadbd8", command=self.delete_dantoc).pack(side="left", padx=5)

        self.tree_dt = ttk.Treeview(self.tab_dantoc, columns=("id", "ten"), show="headings", height=8)
        self.tree_dt.heading("id", text="STT")
        self.tree_dt.heading("ten", text="Tên Dân tộc")
        self.tree_dt.pack(padx=10, pady=5, fill="both", expand=True)

    def load_dantoc(self):
        for item in self.tree_dt.get_children():
            self.tree_dt.delete(item)
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("SELECT madantoc, tendantoc FROM dantoc")
            for r in c.fetchall():
                self.tree_dt.insert("", tk.END, values=r)
            conn.close()
        except Exception:
            pass

    def add_dantoc(self):
        dt = self.ent_dantoc.get().strip()
        if not dt:
            return
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO dantoc (tendantoc) VALUES (?)", (dt,))
            conn.commit()
            conn.close()
            self.ent_dantoc.delete(0, tk.END)
            self.load_dantoc()
            self.controller.refresh_all_comboboxes()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def delete_dantoc(self):
        sel = self.tree_dt.selection()
        if not sel:
            return
        dt_id = self.tree_dt.item(sel[0])['values'][0]
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("DELETE FROM dantoc WHERE madantoc = ?", (dt_id,))
            conn.commit()
            conn.close()
            self.load_dantoc()
            self.controller.refresh_all_comboboxes()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # --- TAB TÔN GIÁO ---
    def setup_tab_tongiao(self):
        f_top = tk.Frame(self.tab_tongiao)
        f_top.pack(pady=10)
        tk.Label(f_top, text="Tên Tôn giáo:", font=("Times New Roman", 10)).pack(side="left", padx=5)
        self.ent_tongiao = tk.Entry(f_top, width=25)
        self.ent_tongiao.pack(side="left", padx=5)
        tk.Button(f_top, text="Thêm", font=("Times New Roman", 9, "bold"), bg="#e8f8f5", command=self.add_tongiao).pack(side="left", padx=5)
        tk.Button(f_top, text="Xóa", font=("Times New Roman", 9, "bold"), bg="#fadbd8", command=self.delete_tongiao).pack(side="left", padx=5)

        self.tree_tg = ttk.Treeview(self.tab_tongiao, columns=("id", "ten"), show="headings", height=8)
        self.tree_tg.heading("id", text="STT")
        self.tree_tg.heading("ten", text="Tên Tôn giáo")
        self.tree_tg.pack(padx=10, pady=5, fill="both", expand=True)

    def load_tongiao(self):
        for item in self.tree_tg.get_children():
            self.tree_tg.delete(item)
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("SELECT matongiao, tentongiao FROM tongiao")
            for r in c.fetchall():
                self.tree_tg.insert("", tk.END, values=r)
            conn.close()
        except Exception:
            pass

    def add_tongiao(self):
        tg = self.ent_tongiao.get().strip()
        if not tg:
            return
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("INSERT INTO tongiao (tentongiao) VALUES (?)", (tg,))
            conn.commit()
            conn.close()
            self.ent_tongiao.delete(0, tk.END)
            self.load_tongiao()
            self.controller.refresh_all_comboboxes()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def delete_tongiao(self):
        sel = self.tree_tg.selection()
        if not sel:
            return
        tg_id = self.tree_tg.item(sel[0])['values'][0]
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("DELETE FROM tongiao WHERE matongiao = ?", (tg_id,))
            conn.commit()
            conn.close()
            self.load_tongiao()
            self.controller.refresh_all_comboboxes()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def load_data(self):
        self.load_lophoc()
        self.load_dantoc()
        self.load_tongiao()

    def select_tab(self, tab_index):
        self.notebook.select(tab_index)


# ==========================================
# 4. FRAME NHẬP ĐIỂM HỌC SINH (NGHIỆP VỤ)
# ==========================================
class NhapDiemFrame(tk.Frame):
    """Giao diện Quản lý và Nhập điểm chi tiết cho Học sinh"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg="#F3F6FA")
        self.controller = controller
        self.action_mode = ''
        self.selected_madiem = None

        self.create_widgets()
        self.set_input_state('disabled')

    def create_widgets(self):
        lbl_title = tk.Label(self, text="QUẢN LÝ NHẬP ĐIỂM HỌC SINH", font=("Arial", 17, "bold"), fg="#173F67", bg="#F3F6FA")
        lbl_title.pack(pady=10)

        frame_form = tk.LabelFrame(self, text=" Thông tin chi tiết bảng điểm ", font=("Arial", 10, "bold"), fg="#173F67", bg="#FFFFFF")
        frame_form.pack(padx=20, pady=5, fill="x", ipadx=10, ipady=5)

        frame_form.columnconfigure(1, weight=1)
        frame_form.columnconfigure(3, weight=1)

        # Hàng 1
        tk.Label(frame_form, text="Học sinh:", font=("Times New Roman", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=6)
        self.cbo_hocsinh = ttk.Combobox(frame_form, width=38, font=("Arial", 10), state="readonly")
        self.cbo_hocsinh.grid(row=0, column=1, sticky="w", padx=(5, 30), pady=6)

        tk.Label(frame_form, text="Môn học:", font=("Times New Roman", 10)).grid(row=0, column=2, sticky="w", padx=10, pady=6)
        self.cbo_monhoc = ttk.Combobox(frame_form, values=[
            "Toán", "Ngữ văn", "Tiếng Anh", "Vật lý", "Hóa học", "Sinh học", "Lịch sử", "Địa lý", "Tin học", "GDCD"
        ], width=38, font=("Arial", 10), state="readonly")
        self.cbo_monhoc.grid(row=0, column=3, sticky="w", padx=(5, 10), pady=6)
        self.cbo_monhoc.set("Toán")

        # Hàng 2
        tk.Label(frame_form, text="Học kỳ:", font=("Times New Roman", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=6)
        self.cbo_hocky = ttk.Combobox(frame_form, values=["1", "2"], width=38, font=("Arial", 10), state="readonly")
        self.cbo_hocky.grid(row=1, column=1, sticky="w", padx=(5, 30), pady=6)
        self.cbo_hocky.set("1")

        tk.Label(frame_form, text="Năm học:", font=("Times New Roman", 10)).grid(row=1, column=2, sticky="w", padx=10, pady=6)
        self.cbo_namhoc = ttk.Combobox(frame_form, values=["2025-2026", "2026-2027"], width=38, font=("Arial", 10))
        self.cbo_namhoc.grid(row=1, column=3, sticky="w", padx=(5, 10), pady=6)
        self.cbo_namhoc.set("2025-2026")

        # Hàng 3
        tk.Label(frame_form, text="Điểm miệng:", font=("Times New Roman", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=6)
        self.entry_mieng = tk.Entry(frame_form, width=20, font=("Arial", 10))
        self.entry_mieng.grid(row=2, column=1, sticky="w", padx=(5, 30), pady=6)

        tk.Label(frame_form, text="Điểm 15 phút:", font=("Times New Roman", 10)).grid(row=2, column=2, sticky="w", padx=10, pady=6)
        self.entry_15p = tk.Entry(frame_form, width=20, font=("Arial", 10))
        self.entry_15p.grid(row=2, column=3, sticky="w", padx=(5, 10), pady=6)

        # Hàng 4
        tk.Label(frame_form, text="Điểm 1 tiết:", font=("Times New Roman", 10)).grid(row=3, column=0, sticky="w", padx=10, pady=6)
        self.entry_1tiet = tk.Entry(frame_form, width=20, font=("Arial", 10))
        self.entry_1tiet.grid(row=3, column=1, sticky="w", padx=(5, 30), pady=6)

        tk.Label(frame_form, text="Điểm thi:", font=("Times New Roman", 10)).grid(row=3, column=2, sticky="w", padx=10, pady=6)
        frame_thi_dtb = tk.Frame(frame_form)
        frame_thi_dtb.grid(row=3, column=3, sticky="w", padx=(5, 10), pady=6)

        self.entry_thi = tk.Entry(frame_thi_dtb, width=15, font=("Arial", 10))
        self.entry_thi.pack(side="left", padx=(0, 20))

        tk.Label(frame_thi_dtb, text="Điểm TB:", font=("Arial", 10, "bold"), fg="#173F67", bg="#FFFFFF").pack(side="left", padx=(0, 5))
        self.lbl_dtb_val = tk.Label(frame_thi_dtb, text="0.0", font=("Arial", 11, "bold"), fg="#c0392b")
        self.lbl_dtb_val.pack(side="left")

        # Nút thao tác
        frame_action_search = tk.Frame(self, bg="#F3F6FA")
        frame_action_search.pack(padx=20, pady=10, fill="x")

        frame_buttons = tk.Frame(frame_action_search, bg="#F3F6FA")
        frame_buttons.pack(side="left")

        self.btn_them = tk.Button(frame_buttons, text="Thêm", width=8, font=("Times New Roman", 9, "bold"), bg="#e8f8f5", command=self.cmd_them)
        self.btn_them.pack(side="left", padx=2)

        self.btn_sua = tk.Button(frame_buttons, text="Sửa", width=8, font=("Times New Roman", 9, "bold"), bg="#fef9e7", command=self.cmd_sua)
        self.btn_sua.pack(side="left", padx=2)

        self.btn_xoa = tk.Button(frame_buttons, text="Xóa", width=8, font=("Times New Roman", 9, "bold"), bg="#fadbd8", command=self.cmd_xoa)
        self.btn_xoa.pack(side="left", padx=2)

        self.btn_luu = tk.Button(frame_buttons, text="Lưu", width=8, font=("Times New Roman", 9, "bold"), bg="#eafaf1", command=self.cmd_luu, state="disabled")
        self.btn_luu.pack(side="left", padx=2)

        self.btn_huy = tk.Button(frame_buttons, text="Hủy", width=8, font=("Times New Roman", 9, "bold"), command=self.cmd_huy, state="disabled")
        self.btn_huy.pack(side="left", padx=2)

        btn_calc = tk.Button(frame_buttons, text="Tính ĐTB", width=9, font=("Times New Roman", 9, "bold"), bg="#d4efdf", command=self.calculate_dtb)
        btn_calc.pack(side="left", padx=5)

        self.btn_trangchu = tk.Button(frame_buttons, text="Trang chủ", width=9, font=("Times New Roman", 9, "bold"), command=lambda: self.controller.show_frame("TrangChuFrame"))
        self.btn_trangchu.pack(side="left", padx=2)

        # Tìm kiếm
        frame_search = tk.Frame(frame_action_search, bg="#F3F6FA")
        frame_search.pack(side="right")

        tk.Label(frame_search, text="Tìm theo Mã/Tên/Môn:", font=("Times New Roman", 10)).pack(side="left", padx=(0, 5))
        self.entry_search = tk.Entry(frame_search, width=18, font=("Times New Roman", 10))
        self.entry_search.pack(side="left", padx=(0, 5))
        self.entry_search.bind("<KeyRelease>", lambda event: self.load_data())

        btn_search = tk.Button(frame_search, text="Tìm", width=5, font=("Times New Roman", 9), command=self.load_data)
        btn_search.pack(side="left", padx=2)

        # Bảng
        lbl_list = tk.Label(self, text="Bảng điểm chi tiết học sinh", font=("Times New Roman", 11, "bold"), fg="#1b4f72")
        lbl_list.pack(anchor="w", padx=20, pady=(5, 2))

        columns = ("madiem", "mahs", "hoten", "tenmon", "hocky", "namhoc", "mieng", "p15", "t1iet", "thi", "dtb")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=11)

        self.tree.heading("madiem", text="STT")
        self.tree.heading("mahs", text="Mã HS")
        self.tree.heading("hoten", text="Họ tên học sinh")
        self.tree.heading("tenmon", text="Môn học")
        self.tree.heading("hocky", text="HK")
        self.tree.heading("namhoc", text="Năm học")
        self.tree.heading("mieng", text="Miệng")
        self.tree.heading("p15", text="15P")
        self.tree.heading("t1iet", text="1 Tiết")
        self.tree.heading("thi", text="Thi")
        self.tree.heading("dtb", text="ĐTB")

        self.tree.column("madiem", width=50, anchor="center")
        self.tree.column("mahs", width=90, anchor="center")
        self.tree.column("hoten", width=180, anchor="w")
        self.tree.column("tenmon", width=110, anchor="w")
        self.tree.column("hocky", width=50, anchor="center")
        self.tree.column("namhoc", width=100, anchor="center")
        self.tree.column("mieng", width=60, anchor="center")
        self.tree.column("p15", width=60, anchor="center")
        self.tree.column("t1iet", width=60, anchor="center")
        self.tree.column("thi", width=60, anchor="center")
        self.tree.column("dtb", width=70, anchor="center")

        self.tree.pack(padx=20, pady=(0, 15), fill="both", expand=True)
        self.tree.tag_configure("oddrow", background="#FFFFFF")
        self.tree.tag_configure("evenrow", background="#F4F8FC")
        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

    def load_students_combobox(self):
        try:
            conn = connect_db()
            c = conn.cursor()
            c.execute("SELECT mahs, hoten FROM hocsinh ORDER BY mahs ASC")
            students = [f"{r[0]} - {r[1]}" for r in c.fetchall()]
            self.cbo_hocsinh['values'] = students
            if students:
                self.cbo_hocsinh.set(students[0])
            conn.close()
        except Exception:
            pass

    def set_input_state(self, state):
        combo_state = "readonly" if state == "normal" else "disabled"
        self.cbo_hocsinh.config(state=combo_state)
        self.cbo_monhoc.config(state=combo_state)
        self.cbo_hocky.config(state=combo_state)
        self.cbo_namhoc.config(state="normal" if state == "normal" else "disabled")

        self.entry_mieng.config(state=state)
        self.entry_15p.config(state=state)
        self.entry_1tiet.config(state=state)
        self.entry_thi.config(state=state)

    def clear_inputs(self):
        self.set_input_state('normal')
        self.entry_mieng.delete(0, tk.END)
        self.entry_15p.delete(0, tk.END)
        self.entry_1tiet.delete(0, tk.END)
        self.entry_thi.delete(0, tk.END)
        self.lbl_dtb_val.config(text="0.0")
        self.selected_madiem = None

    def calculate_dtb(self):
        try:
            m = float(self.entry_mieng.get().strip() or 0)
            p = float(self.entry_15p.get().strip() or 0)
            t = float(self.entry_1tiet.get().strip() or 0)
            thi = float(self.entry_thi.get().strip() or 0)

            for score in (m, p, t, thi):
                if not (0 <= score <= 10):
                    messagebox.showwarning("Cảnh báo", "Điểm số phải từ 0 đến 10!")
                    return None

            dtb = round((m + p + (t * 2) + (thi * 3)) / 7.0, 1)
            self.lbl_dtb_val.config(text=str(dtb))
            return dtb
        except ValueError:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đúng định dạng số!")
            return None

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        search_kw = getattr(self, 'entry_search', None)
        keyword = search_kw.get().strip() if search_kw else ''

        try:
            conn = connect_db()
            c = conn.cursor()
            sql = """
                SELECT b.madiem, b.mahs, h.hoten, b.tenmon, b.hocky, b.namhoc, 
                       b.diem_mieng, b.diem_15p, b.diem_1tiet, b.diem_thi, b.diem_tb
                FROM bangdiem b
                JOIN hocsinh h ON b.mahs = h.mahs
            """
            if keyword:
                sql += " WHERE b.mahs LIKE ? OR h.hoten LIKE ? OR b.tenmon LIKE ?"
                param = f"%{keyword}%"
                c.execute(sql + " ORDER BY b.madiem DESC", (param, param, param))
            else:
                c.execute(sql + " ORDER BY b.madiem DESC")

            for row in c.fetchall():
                self.tree.insert("", tk.END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Lỗi CSDL", f"Không thể tải bảng điểm: {e}")

    def fill_form_from_selection(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            vals = item['values']

            self.clear_inputs()
            self.selected_madiem = vals[0]
            student_str = f"{vals[1]} - {vals[2]}"
            if student_str in self.cbo_hocsinh['values']:
                self.cbo_hocsinh.set(student_str)

            self.cbo_monhoc.set(vals[3])
            self.cbo_hocky.set(str(vals[4]))
            self.cbo_namhoc.set(str(vals[5]))

            self.entry_mieng.insert(0, str(vals[6]))
            self.entry_15p.insert(0, str(vals[7]))
            self.entry_1tiet.insert(0, str(vals[8]))
            self.entry_thi.insert(0, str(vals[9]))
            self.lbl_dtb_val.config(text=str(vals[10]))

    def on_select_row(self, event):
        if self.action_mode != '':
            return
        self.fill_form_from_selection()
        self.set_input_state('disabled')

    def cmd_them(self):
        self.action_mode = 'them'
        self.clear_inputs()
        self.cbo_hocsinh.focus()

        self.btn_them.config(state='disabled')
        self.btn_sua.config(state='disabled')
        self.btn_xoa.config(state='disabled')
        self.btn_luu.config(state='normal')
        self.btn_huy.config(state='normal')

    def cmd_sua(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn 1 dòng trong bảng điểm để sửa!")
            return

        self.action_mode = 'sua'
        self.set_input_state('normal')

        self.btn_them.config(state='disabled')
        self.btn_sua.config(state='disabled')
        self.btn_xoa.config(state='disabled')
        self.btn_luu.config(state='normal')
        self.btn_huy.config(state='normal')

    def cmd_luu(self):
        student_val = self.cbo_hocsinh.get().strip()
        if not student_val:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn học sinh!")
            return

        ma_hs = student_val.split(" - ")[0]
        ten_mon = self.cbo_monhoc.get().strip()
        hoc_ky = int(self.cbo_hocky.get().strip())
        nam_hoc = self.cbo_namhoc.get().strip()

        dtb = self.calculate_dtb()
        if dtb is None:
            return

        m = float(self.entry_mieng.get().strip())
        p = float(self.entry_15p.get().strip())
        t = float(self.entry_1tiet.get().strip())
        thi = float(self.entry_thi.get().strip())

        try:
            conn = connect_db()
            c = conn.cursor()

            if self.action_mode == 'them':
                sql = """INSERT INTO bangdiem (mahs, tenmon, hocky, namhoc, diem_mieng, diem_15p, diem_1tiet, diem_thi, diem_tb)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                c.execute(sql, (ma_hs, ten_mon, hoc_ky, nam_hoc, m, p, t, thi, dtb))
                messagebox.showinfo("Thành công", "Thêm điểm học sinh thành công!")

            elif self.action_mode == 'sua':
                if not self.selected_madiem:
                    messagebox.showwarning("Cảnh báo", "Không xác định được bản ghi điểm!")
                    conn.close()
                    return

                sql = """UPDATE bangdiem 
                         SET mahs = ?, tenmon = ?, hocky = ?, namhoc = ?, diem_mieng = ?, diem_15p = ?, diem_1tiet = ?, diem_thi = ?, diem_tb = ?
                         WHERE madiem = ?"""
                c.execute(sql, (ma_hs, ten_mon, hoc_ky, nam_hoc, m, p, t, thi, dtb, self.selected_madiem))
                messagebox.showinfo("Thành công", "Cập nhật điểm thành công!")

            conn.commit()
            conn.close()

            self.cmd_huy()
            self.load_data()

        except Exception as e:
            messagebox.showerror("Lỗi", f"Thao tác thất bại: {e}")

    def cmd_huy(self):
        self.action_mode = ''
        self.clear_inputs()
        self.set_input_state('disabled')

        self.btn_them.config(state='normal')
        self.btn_sua.config(state='normal')
        self.btn_xoa.config(state='normal')
        self.btn_luu.config(state='disabled')
        self.btn_huy.config(state='disabled')

    def cmd_xoa(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn 1 bản ghi điểm cần xóa!")
            return

        item = self.tree.item(selected[0])
        madiem = item['values'][0]
        ho_ten = item['values'][2]
        ten_mon = item['values'][3]

        confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa điểm môn {ten_mon} của học sinh:\n{ho_ten}?")
        if confirm:
            try:
                conn = connect_db()
                c = conn.cursor()
                c.execute("DELETE FROM bangdiem WHERE madiem = ?", (madiem,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Thành công", "Xóa bản ghi điểm thành công!")
                self.clear_inputs()
                self.load_data()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể xóa dữ liệu: {e}")


# ==========================================
# 5. FRAME THỐNG KÊ & BÁO CÁO
# ==========================================
class ThongKeFrame(tk.Frame):
    """Giao diện Thống kê và Báo cáo dữ liệu"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg="#F3F6FA")
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="THỐNG KÊ & BÁO CÁO DỮ LIỆU", font=("Arial", 17, "bold"), fg="#173F67", bg="#F3F6FA")
        lbl_title.pack(pady=15)

        frame_summary = tk.LabelFrame(self, text=" Tổng quan hệ thống ", font=("Arial", 10, "bold"), fg="#173F67", bg="#FFFFFF")
        frame_summary.pack(padx=20, pady=5, fill="x", ipadx=10, ipady=5)

        self.lbl_tong_hs = tk.Label(frame_summary, text="Tổng số học sinh: 0", font=("Times New Roman", 11, "bold"), fg="#2874a6")
        self.lbl_tong_hs.pack(anchor="w", padx=10, pady=3)

        self.lbl_nam_nu = tk.Label(frame_summary, text="Phân bổ giới tính: Nam: 0 | Nữ: 0", font=("Times New Roman", 10))
        self.lbl_nam_nu.pack(anchor="w", padx=10, pady=3)

        frame_control = tk.Frame(self, bg="#F3F6FA")
        frame_control.pack(padx=20, pady=10, fill="x")

        lbl_chon = tk.Label(frame_control, text="Chọn nội dung thống kê:", font=("Times New Roman", 11, "bold"), fg="#1b4f72")
        lbl_chon.pack(side="left", padx=(0, 10))

        self.combo_type = ttk.Combobox(frame_control, values=[
            "Thống kê theo Nơi sinh", 
            "Thống kê sĩ số theo Lớp học", 
            "Thống kê theo Dân tộc", 
            "Thống kê theo Tôn giáo"
        ], state="readonly", width=30, font=("Times New Roman", 10))
        self.combo_type.pack(side="left", padx=5)
        self.combo_type.current(0)
        self.combo_type.bind("<<ComboboxSelected>>", lambda e: self.load_statistics())

        self.lbl_table_title = tk.Label(self, text="Chi tiết thống kê", font=("Times New Roman", 11, "bold"), fg="#1b4f72")
        self.lbl_table_title.pack(anchor="w", padx=20, pady=(5, 2))

        self.tree_tk = ttk.Treeview(self, show="headings", height=11)
        self.tree_tk.pack(padx=20, pady=5, fill="both", expand=True)

        btn_trangchu = tk.Button(self, text="Trở về Trang chủ", width=16, font=("Times New Roman", 10, "bold"), bg="#ebdef0", command=lambda: self.controller.show_frame("TrangChuFrame"))
        btn_trangchu.pack(pady=10)

    def load_statistics(self):
        try:
            conn = connect_db()
            c = conn.cursor()

            c.execute("SELECT COUNT(*) FROM hocsinh")
            total = c.fetchone()[0]
            self.lbl_tong_hs.config(text=f"Tổng số học sinh trong hệ thống: {total}")

            c.execute("SELECT phai, COUNT(*) FROM hocsinh GROUP BY phai")
            gender_data = dict(c.fetchall())
            nam_count = gender_data.get('Nam', 0)
            nu_count = gender_data.get('Nữ', 0)
            self.lbl_nam_nu.config(text=f"Phân bổ giới tính: Nam: {nam_count} học sinh  |  Nữ: {nu_count} học sinh")

            selected_option = self.combo_type.get()
            
            for item in self.tree_tk.get_children():
                self.tree_tk.delete(item)

            if selected_option == "Thống kê theo Nơi sinh":
                self.lbl_table_title.config(text="Thống kê số lượng học sinh theo Nơi sinh")
                self.tree_tk.configure(columns=("col1", "col2"))
                self.tree_tk.heading("col1", text="Nơi sinh")
                self.tree_tk.heading("col2", text="Số lượng học sinh")
                self.tree_tk.column("col1", width=500, anchor="w")
                self.tree_tk.column("col2", width=300, anchor="center")

                c.execute("SELECT noisinh, COUNT(*) FROM hocsinh GROUP BY noisinh ORDER BY COUNT(*) DESC")
                for row in c.fetchall():
                    self.tree_tk.insert("", tk.END, values=row)

            elif selected_option == "Thống kê sĩ số theo Lớp học":
                self.lbl_table_title.config(text="Thống kê sĩ số và thông tin lớp học")
                self.tree_tk.configure(columns=("malop", "tenlop", "gvcn", "siso"))
                self.tree_tk.heading("malop", text="Mã lớp")
                self.tree_tk.heading("tenlop", text="Tên lớp")
                self.tree_tk.heading("gvcn", text="Giáo viên chủ nhiệm")
                self.tree_tk.heading("siso", text="Sĩ số học sinh")
                
                self.tree_tk.column("malop", width=120, anchor="center")
                self.tree_tk.column("tenlop", width=200, anchor="w")
                self.tree_tk.column("gvcn", width=280, anchor="w")
                self.tree_tk.column("siso", width=150, anchor="center")

                c.execute("""
                    SELECT l.malop, l.tenlop, l.gvcn, COUNT(h.mahs) AS siso
                    FROM lophoc l
                    LEFT JOIN hocsinh h ON l.malop = h.malop
                    GROUP BY l.malop, l.tenlop, l.gvcn;
                """)
                for row in c.fetchall():
                    self.tree_tk.insert("", tk.END, values=row)

            elif selected_option == "Thống kê theo Dân tộc":
                self.lbl_table_title.config(text="Thống kê số lượng học sinh theo Dân tộc")
                self.tree_tk.configure(columns=("col1", "col2"))
                self.tree_tk.heading("col1", text="Dân tộc")
                self.tree_tk.heading("col2", text="Số lượng học sinh")
                self.tree_tk.column("col1", width=500, anchor="w")
                self.tree_tk.column("col2", width=300, anchor="center")

                c.execute("SELECT dantoc, COUNT(*) FROM hocsinh GROUP BY dantoc ORDER BY COUNT(*) DESC")
                for row in c.fetchall():
                    self.tree_tk.insert("", tk.END, values=row)

            elif selected_option == "Thống kê theo Tôn giáo":
                self.lbl_table_title.config(text="Thống kê số lượng học sinh theo Tôn giáo")
                self.tree_tk.configure(columns=("col1", "col2"))
                self.tree_tk.heading("col1", text="Tôn giáo")
                self.tree_tk.heading("col2", text="Số lượng học sinh")
                self.tree_tk.column("col1", width=500, anchor="w")
                self.tree_tk.column("col2", width=300, anchor="center")

                c.execute("SELECT tongiao, COUNT(*) FROM hocsinh GROUP BY tongiao ORDER BY COUNT(*) DESC")
                for row in c.fetchall():
                    self.tree_tk.insert("", tk.END, values=row)

            conn.close()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải dữ liệu thống kê: {e}")

# ==========================================
# 6. FRAME GIỚI THIỆU
# ==========================================
class GioiThieuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F3F6FA")
        self.controller = controller

        # Tiêu đề trang
        header = tk.Frame(self, bg="#174A7E", height=130)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="GIỚI THIỆU PHẦN MỀM",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#174A7E"
        ).pack(anchor="w", padx=32, pady=(28, 8))

        tk.Label(
            header,
            text="Hệ thống quản lý học sinh",
            font=("Segoe UI", 11),
            fg="#DBEAFE",
            bg="#174A7E"
        ).pack(anchor="w", padx=33)

        # Nội dung giới thiệu
        content = tk.Frame(
            self,
            bg="white",
            highlightbackground="#D9E4F2",
            highlightthickness=1
        )
        content.pack(fill="both", expand=True, padx=32, pady=28)

        tk.Label(
            content,
            text="MỤC ĐÍCH",
            font=("Segoe UI", 14, "bold"),
            fg="#174A7E",
            bg="white"
        ).pack(anchor="w", padx=24, pady=(22, 10))

        tk.Label(
            content,
            text=(
                "Phần mềm hỗ trợ giáo viên quản lý hồ sơ học sinh, "
                "lớp học, kết quả học tập và thống kê báo cáo."
            ),
            font=("Segoe UI", 11),
            fg="#475569",
            bg="white",
            wraplength=900,
            justify="left"
        ).pack(anchor="w", padx=24, pady=(0, 20))

        tk.Frame(
            content, bg="#D9E4F2", height=1
        ).pack(fill="x", padx=24)

        tk.Label(
            content,
            text="CÁC CHỨC NĂNG CHÍNH",
            font=("Segoe UI", 14, "bold"),
            fg="#174A7E",
            bg="white"
        ).pack(anchor="w", padx=24, pady=(20, 12))

        features = [
            (
                "Hồ sơ học sinh",
                "Quản lý thông tin cá nhân và danh sách học sinh."
            ),
            (
                "Quản lý lớp học",
                "Theo dõi danh sách và thông tin các lớp."
            ),
            (
                "Nhập và theo dõi điểm",
                "Cập nhật điểm và theo dõi kết quả học tập."
            ),
            (
                "Thống kê và báo cáo",
                "Tổng hợp số liệu phục vụ công tác quản lý."
            )
        ]

        for title, description in features:
            row = tk.Frame(content, bg="white")
            row.pack(fill="x", padx=28, pady=8)

            tk.Label(
                row,
                text="●",
                font=("Segoe UI", 12),
                fg="#2563EB",
                bg="white"
            ).pack(side="left", padx=(0, 12))

            detail = tk.Frame(row, bg="white")
            detail.pack(side="left", fill="x", expand=True)

            tk.Label(
                detail,
                text=title,
                font=("Segoe UI", 11, "bold"),
                fg="#173F67",
                bg="white"
            ).pack(anchor="w")

            tk.Label(
                detail,
                text=description,
                font=("Segoe UI", 10),
                fg="#64748B",
                bg="white"
            ).pack(anchor="w")

        tk.Label(
            content,
            text="Phiên bản: 1.0  |  Đối tượng sử dụng: Giáo viên",
            font=("Segoe UI", 10),
            fg="#64748B",
            bg="white"
        ).pack(anchor="w", padx=24, pady=(24, 18))


# ==========================================
# 7. CỬA SỔ CHÍNH & PHÂN QUYỀN ĐĂNG NHẬP
# ==========================================
class QuanLyHocSinhApp(tk.Tk):
    """Cửa sổ ứng dụng chính chứa Thanh Menu bar và kiểm tra quyền truy cập"""
    def __init__(self):
        super().__init__()
        # Chỉ hiển thị cửa sổ đăng nhập khi khởi động.
        self.withdraw()
        self.title("Hệ thống quản lý học sinh")
        self.geometry("1250x780")
        self.minsize(1050, 680)
        self.resizable(True, True)
        self.configure(bg="#F3F6FA")
        self.setup_visual_theme()

        self.is_logged_in = False
        self.current_user = None

        self.create_menu_bar()

        # Khung chứa màn hình chính
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TrangChuFrame, HocSinhFrame, DanhMucFrame, NhapDiemFrame, ThongKeFrame, GioiThieuFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Chưa hiện trang chủ. Yêu cầu đăng nhập trước.
        self.after(150, self.show_login_dialog)

    def setup_visual_theme(self):
        """Thiết lập phong cách thống nhất cho các màn hình nghiệp vụ."""
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Treeview",
                        background="#FFFFFF",
                        fieldbackground="#FFFFFF",
                        foreground="#243447",
                        rowheight=29,
                        font=("Arial", 10))
        style.configure("Treeview.Heading",
                        background="#E7EEF7",
                        foreground="#173F67",
                        font=("Arial", 10, "bold"),
                        padding=(8, 7))
        style.map("Treeview",
                  background=[("selected", "#D5E8FA")],
                  foreground=[("selected", "#173F67")])
        style.configure("TCombobox", padding=5, font=("Arial", 10))
        style.configure("TNotebook", background="#F3F6FA", borderwidth=0)
        style.configure("TNotebook.Tab",
                        padding=(14, 8),
                        font=("Arial", 10, "bold"))
        style.map("TNotebook.Tab",
                  background=[("selected", "#FFFFFF"), ("active", "#E7EEF7")],
                  foreground=[("selected", "#173F67")])
        style.configure("TScrollbar", background="#E7EEF7")

    def create_menu_bar(self):
        self.menubar = tk.Menu(self)

        # Menu 1: Chương trình
        self.menu_program = tk.Menu(self.menubar, tearoff=0)
        self.menu_program.add_command(label="Trang chủ", command=lambda: self.show_frame("TrangChuFrame"))
        
        if self.is_logged_in:
            self.menu_program.add_command(label=f"Đăng xuất ({self.current_user})", command=self.do_logout)
        else:
            self.menu_program.add_command(label="Đăng nhập", command=self.show_login_dialog)

        self.menu_program.add_separator()
        self.menu_program.add_command(label="Thoát", command=self.quit)
        self.menubar.add_cascade(label="Hệ thống", menu=self.menu_program)

        # Menu 2: Quản lý Hồ sơ
        menu_hocsinh = tk.Menu(self.menubar, tearoff=0)
        menu_hocsinh.add_command(label="Hồ sơ Học sinh", command=lambda: self.show_frame("HocSinhFrame"))
        self.menubar.add_cascade(label="Quản lý Hồ sơ", menu=menu_hocsinh)

        # Menu 3: Danh mục (Quản lý các Bảng Danh mục)
        menu_category = tk.Menu(self.menubar, tearoff=0)
        menu_category.add_command(label="Lớp học", command=lambda: self.open_danhmuc_tab(0))
        menu_category.add_command(label="Dân tộc", command=lambda: self.open_danhmuc_tab(1))
        menu_category.add_command(label="Tôn giáo", command=lambda: self.open_danhmuc_tab(2))
        self.menubar.add_cascade(label="Danh mục", menu=menu_category)

        # Menu 4: Nghiệp vụ
        menu_task = tk.Menu(self.menubar, tearoff=0)
        menu_task.add_command(label="Nhập điểm học sinh", command=lambda: self.show_frame("NhapDiemFrame"))
        self.menubar.add_cascade(label="Quản lý điểm", menu=menu_task)

        # Menu 5: Báo cáo
        menu_report = tk.Menu(self.menubar, tearoff=0)
        menu_report.add_command(label="Thống kê & Báo cáo", command=lambda: self.show_frame("ThongKeFrame"))
        self.menubar.add_cascade(label="Báo cáo", menu=menu_report)

        # Menu 6: Giúp đỡ
        menu_help = tk.Menu(self.menubar, tearoff=0)
        menu_help.add_command(label="Giới thiệu", command=lambda: self.show_frame("GioiThieuFrame"))
        self.menubar.add_cascade(label="Thông tin", menu=menu_help)

        self.config(menu=self.menubar)

    def update_menu_bar(self):
        """Cập nhật trạng thái hiển thị trên Menu Bar"""
        self.create_menu_bar()

    def open_danhmuc_tab(self, tab_index):
        if not self.is_logged_in:
            messagebox.showwarning("Yêu cầu đăng nhập", "Bạn chưa đăng nhập hệ thống!\nVui lòng đăng nhập để quản lý Danh mục.")
            self.show_login_dialog()
            return
        self.show_frame("DanhMucFrame")
        self.frames["DanhMucFrame"].select_tab(tab_index)

    def refresh_all_comboboxes(self):
        """Tự động làm mới Combobox danh mục ở các màn hình khác"""
        if "HocSinhFrame" in self.frames:
            self.frames["HocSinhFrame"].load_combobox_data()
        if "NhapDiemFrame" in self.frames:
            self.frames["NhapDiemFrame"].load_students_combobox()

    def show_frame(self, page_name):
        """Khóa chuyển đổi giao diện nếu chưa đăng nhập"""
        if page_name != "TrangChuFrame" and not self.is_logged_in:
            messagebox.showwarning("Yêu cầu đăng nhập", "Bạn chưa đăng nhập hệ thống!\nVui lòng đăng nhập để thực hiện các chức năng này.")
            self.show_login_dialog()
            return

        frame = self.frames[page_name]
        frame.tkraise()

        if hasattr(frame, 'load_data'):
            frame.load_data()
        if hasattr(frame, 'load_combobox_data'):
            frame.load_combobox_data()
        if hasattr(frame, 'load_students_combobox'):
            frame.load_students_combobox()
        if hasattr(frame, 'load_statistics'):
            frame.load_statistics()

    def show_login_dialog(self):
        """Hiển thị giao diện đăng nhập hiện đại."""
        # Nếu cửa sổ đăng nhập đang mở thì đưa lên trước.
        # Phải kiểm tra None vì sau khi đăng nhập/đóng cửa sổ,
        # self.login_win được gán None.
        current_login = getattr(self, "login_win", None)
        if current_login is not None:
            try:
                if current_login.winfo_exists():
                    current_login.lift()
                    current_login.focus_force()
                    return
            except tk.TclError:
                self.login_win = None

        login_win = tk.Toplevel(self)
        self.login_win = login_win
        login_win.title("Đăng nhập hệ thống")
        login_win.geometry("760x460")
        login_win.resizable(False, False)
        login_win.configure(bg="#F3F6FA")
        # Cửa sổ chính đang ẩn nên đăng nhập là cửa sổ độc lập.
        login_win.grab_set()

        # Căn giữa màn hình.
        login_win.update_idletasks()
        x = (login_win.winfo_screenwidth() - 760) // 2
        y = (login_win.winfo_screenheight() - 460) // 2
        login_win.geometry(f"+{max(x, 0)}+{max(y, 0)}")

        # ==============================
        # KHU VỰC GIỚI THIỆU BÊN TRÁI
        # ==============================
        left_panel = tk.Frame(login_win, bg="#174A7E", width=285)
        left_panel.pack(side="left", fill="y")
        left_panel.pack_propagate(False)

        tk.Label(
            left_panel, text="✦", font=("Segoe UI", 42, "bold"),
            fg="#FFFFFF", bg="#174A7E"
        ).pack(pady=(65, 12))

        tk.Label(
            left_panel, text="TRƯỜNG HỌC SỐ",
            font=("Segoe UI", 11, "bold"),
            fg="#BFDBFE", bg="#174A7E"
        ).pack()

        tk.Label(
            left_panel, text="QUẢN LÝ\nHỌC SINH",
            font=("Segoe UI", 22, "bold"),
            fg="#FFFFFF", bg="#174A7E",
            justify="center"
        ).pack(pady=(12, 10))

        tk.Label(
            left_panel,
            text="Đồng hành cùng giáo viên\ntrong công tác quản lý và\ntheo dõi kết quả học tập.",
            font=("Segoe UI", 10),
            fg="#DBEAFE", bg="#174A7E",
            justify="center"
        ).pack(pady=8)

        tk.Label(
            left_panel, text="PHIÊN BẢN 1.0",
            font=("Segoe UI", 8, "bold"),
            fg="#BFDBFE", bg="#174A7E"
        ).pack(side="bottom", pady=22)

        # ==============================
        # KHU VỰC NHẬP THÔNG TIN BÊN PHẢI
        # ==============================
        right_panel = tk.Frame(login_win, bg="#FFFFFF")
        right_panel.pack(side="right", fill="both", expand=True)

        form = tk.Frame(right_panel, bg="#FFFFFF")
        form.pack(fill="both", expand=True, padx=48, pady=38)

        tk.Label(
            form, text="Chào mừng trở lại!",
            font=("Segoe UI", 21, "bold"),
            fg="#173F67", bg="#FFFFFF"
        ).pack(anchor="w", pady=(12, 4))

        tk.Label(
            form, text="Đăng nhập để tiếp tục sử dụng hệ thống.",
            font=("Segoe UI", 9),
            fg="#64748B", bg="#FFFFFF"
        ).pack(anchor="w", pady=(0, 25))

        tk.Label(
            form, text="TÀI KHOẢN",
            font=("Segoe UI", 9, "bold"),
            fg="#334155", bg="#FFFFFF"
        ).pack(anchor="w", pady=(0, 7))

        ent_user = tk.Entry(
            form, font=("Segoe UI", 11), bd=1, relief="solid",
            bg="#F8FAFC", fg="#172B4D",
            insertbackground="#172B4D"
        )
        ent_user.pack(fill="x", ipady=9, pady=(0, 17))

        tk.Label(
            form, text="MẬT KHẨU",
            font=("Segoe UI", 9, "bold"),
            fg="#334155", bg="#FFFFFF"
        ).pack(anchor="w", pady=(0, 7))

        password_row = tk.Frame(form, bg="#FFFFFF")
        password_row.pack(fill="x")

        ent_pass = tk.Entry(
            password_row, font=("Segoe UI", 11), bd=1,
            relief="solid", bg="#F8FAFC", fg="#172B4D",
            show="*", insertbackground="#172B4D"
        )
        ent_pass.pack(side="left", fill="x", expand=True, ipady=9)

        def toggle_password():
            if ent_pass.cget("show") == "*":
                ent_pass.config(show="")
                btn_toggle.config(text="Ẩn")
            else:
                ent_pass.config(show="*")
                btn_toggle.config(text="Hiện")

        btn_toggle = tk.Button(
            password_row, text="Hiện", font=("Segoe UI", 9),
            bg="#EAF1F8", fg="#174A7E", activebackground="#DCE8F5",
            bd=0, cursor="hand2", command=toggle_password,
            padx=12
        )
        btn_toggle.pack(side="right", padx=(7, 0), ipady=9)

        def do_login():
            u = ent_user.get().strip()
            p = ent_pass.get()

            if not u or not p:
                messagebox.showwarning(
                    "Thiếu thông tin",
                    "Vui lòng nhập đầy đủ tài khoản và mật khẩu.",
                    parent=login_win
                )
                return

            try:
                conn = connect_db()
                c = conn.cursor()
                c.execute(
                    "SELECT fullname FROM taikhoan "
                    "WHERE username = ? AND password = ?",
                    (u, p)
                )
                res = c.fetchone()
                conn.close()

                if res:
                    self.is_logged_in = True
                    self.current_user = res[0]

                    self.update_menu_bar()
                    self.frames["TrangChuFrame"].update_status()

                    login_win.grab_release()
                    login_win.destroy()
                    self.login_win = None

                    # Hiện cửa sổ chính sau khi đăng nhập thành công.
                    self.deiconify()
                    self.show_frame("TrangChuFrame")
                    self.lift()
                    self.focus_force()

                    messagebox.showinfo(
                        "Đăng nhập thành công",
                        f"Chào mừng {self.current_user}!",
                        parent=self
                    )
                else:
                    messagebox.showerror(
                        "Đăng nhập thất bại",
                        "Tài khoản hoặc mật khẩu không chính xác.",
                        parent=login_win
                    )
                    ent_pass.delete(0, tk.END)
                    ent_pass.focus_set()

            except Exception as e:
                messagebox.showerror(
                    "Lỗi CSDL",
                    f"Không thể kết nối cơ sở dữ liệu: {e}",
                    parent=login_win
                )

        # Nút đăng nhập
        tk.Button(
            form, text="ĐĂNG NHẬP",
            font=("Segoe UI", 10, "bold"),
            bg="#2563EB", fg="#FFFFFF",
            activebackground="#1D4ED8",
            activeforeground="#FFFFFF",
            bd=0, cursor="hand2",
            command=do_login
        ).pack(fill="x", pady=(25, 10), ipady=11)

        def close_login():
            # Chưa đăng nhập mà đóng cửa sổ thì thoát chương trình.
            try:
                login_win.grab_release()
            except tk.TclError:
                pass
            self.login_win = None
            self.destroy()

        tk.Button(
            form, text="Thoát chương trình",
            font=("Segoe UI", 9),
            bg="#FFFFFF", fg="#64748B",
            activebackground="#F1F5F9",
            bd=0, cursor="hand2",
            command=close_login
        ).pack(pady=3)

        # Phím tắt và nút đóng cửa sổ
        login_win.protocol("WM_DELETE_WINDOW", close_login)
        login_win.bind("<Return>", lambda event: do_login())
        login_win.bind("<Escape>", lambda event: close_login())
        ent_user.focus_set()

    def do_logout(self):
        """Đăng xuất và mở lại hộp thoại đăng nhập mà không đóng ứng dụng."""
        if not messagebox.askyesno(
            "Đăng xuất",
            "Bạn có chắc chắn muốn đăng xuất khỏi hệ thống?",
            parent=self
        ):
            return

        self.is_logged_in = False
        self.current_user = None
        self.update_menu_bar()
        self.frames["TrangChuFrame"].update_status()

        # Tạo và hiển thị cửa sổ đăng nhập trước, sau đó mới ẩn cửa sổ chính.
        # Như vậy luôn có một cửa sổ Tk đang hiển thị, tránh kết thúc mainloop.
        self.show_login_dialog()
        self.withdraw()


# ==========================================
# KHỞI CHẠY CHƯƠNG TRÌNH
# ==========================================
if __name__ == "__main__":
    init_database()  # Tạo CSDL nếu chưa có
    app = QuanLyHocSinhApp()
    app.mainloop()