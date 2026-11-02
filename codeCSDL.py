import sqlite3
import os

# Đường dẫn file CSDL SQLite
db_path = os.path.dirname(__file__) if '__file__' in locals() else '.'
db_file = os.path.join(db_path, 'qlhocsinh.db')

def connect_db():
    conn = sqlite3.connect(db_file)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_database():
    """Khởi tạo cấu trúc các bảng và dữ liệu mẫu nếu chưa tồn tại"""
    conn = connect_db()
    c = conn.cursor()

    # 1. Bảng Tài khoản
    c.execute("""
    CREATE TABLE IF NOT EXISTS taikhoan (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(50) NOT NULL,
        fullname VARCHAR(100),
        vaitro VARCHAR(20) DEFAULT 'Giáo viên'
    );
    """)

    # 2. Bảng Lớp học
    c.execute("""
    CREATE TABLE IF NOT EXISTS lophoc (
        malop VARCHAR(10) PRIMARY KEY,
        tenlop VARCHAR(50) NOT NULL,
        namhoc VARCHAR(20),
        gvcn VARCHAR(100)
    );
    """)

    # 3. Bảng Dân tộc
    c.execute("""
    CREATE TABLE IF NOT EXISTS dantoc (
        madantoc INTEGER PRIMARY KEY AUTOINCREMENT,
        tendantoc VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    # 4. Bảng Tôn giáo
    c.execute("""
    CREATE TABLE IF NOT EXISTS tongiao (
        matongiao INTEGER PRIMARY KEY AUTOINCREMENT,
        tentongiao VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    # 5. Bảng Học sinh
    c.execute("""
    CREATE TABLE IF NOT EXISTS hocsinh (
        mahs CHAR(10) PRIMARY KEY,
        hoten VARCHAR(100) NOT NULL,
        phai VARCHAR(10),
        ngaysinh VARCHAR(20),
        noisinh VARCHAR(100),
        dantoc VARCHAR(20),
        tongiao VARCHAR(20),
        malop VARCHAR(10),
        FOREIGN KEY (malop) REFERENCES lophoc(malop) ON DELETE SET NULL
    );
    """)

    # 6. Bảng Điểm
    c.execute("""
    CREATE TABLE IF NOT EXISTS bangdiem (
        madiem INTEGER PRIMARY KEY AUTOINCREMENT,
        mahs CHAR(10) NOT NULL,
        tenmon VARCHAR(50) NOT NULL,
        hocky INT,
        namhoc VARCHAR(20),
        diem_mieng REAL,
        diem_15p REAL,
        diem_1tiet REAL,
        diem_thi REAL,
        diem_tb REAL,
        FOREIGN KEY (mahs) REFERENCES hocsinh(mahs) ON DELETE CASCADE
    );
    """)

    # Chèn dữ liệu ban đầu nếu bảng trống
    c.execute("SELECT COUNT(*) FROM taikhoan")
    if c.fetchone()[0] == 0:
        c.execute("""
            INSERT INTO taikhoan (username, password, fullname, vaitro)
            VALUES ('admin', '123', 'Quản trị viên', 'Admin'),
                   ('giaovien1', '123456', 'Nguyễn Văn Quyền', 'Giáo viên'),
                   ('giaovien2', '456789', 'Trần Thị Mai', 'Giáo viên');
        """)

    c.execute("SELECT COUNT(*) FROM lophoc")
    if c.fetchone()[0] == 0:
        c.execute("""
            INSERT INTO lophoc (malop, tenlop, namhoc, gvcn)
            VALUES ('10A1', 'Lớp 10A1', '2025-2026', 'Nguyễn Văn Quyền'),
                   ('10A2', 'Lớp 10A2', '2025-2026', 'Trần Thị Mai');
        """)

    c.execute("SELECT COUNT(*) FROM dantoc")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO dantoc (tendantoc) VALUES (?)",
                      [('Kinh',), ('Tày',), ('Thái',), ('Mường',), ('Hoa',), ('Khơ-me',), ('Nùng',), ('HMông',), ('Dao',), 
                       ('Gia-rai',), ('Ê-đê',), ('Ba-na',), ('Sán Chay',), ('Chăm',), ('Xơ-đăng',), ('Sán Dìu',), ('Hrê',), 
                       ('Cơ-ho',), ('Ra-glai',), ('Mnông',), ('Thổ',), ('Xtiêng',), ('Khơmú',), ('Bru-Vân Kiều',), ('Giáy',), 
                       ('Cơ-tu',), ('Gié-Triêng',), ('Ta-ôi',), ('Mạ',), ('Co',), ('Chơ-ro',), ('Hà Nhì',), ('Xinh-mun',), 
                       ('Chu-ru',), ('Lào',), ('La-chí',), ('Phù Lá',), ('La Hủ',), ('Kháng',), ('Lự',), ('Pà thẻn',), 
                       ('LôLô',), ('Chứt',), ('Mảng',), ('Cờ lao',), ('Bố Y',), ('La Ha',), ('Cống',), ('Ngái',), ('Si La',), 
                       ('Pu Péo',), ('Brâu',), ('Rơ-măm',), ('Ơ-đu',)])

    c.execute("SELECT COUNT(*) FROM tongiao")
    if c.fetchone()[0] == 0:
        c.executemany("INSERT INTO tongiao (tentongiao) VALUES (?)",
                      [('Không',), ('Phật giáo',), ('Công giáo',), ('Tin lành',), ('Cao đài',), ('Phật giáo Hòa Hảo',), ('Hồi giáo',), 
                       ("Tôn giáo Baha'i",), ('Tịnh độ Cư sỹ Phật hội',), ('Cơ đốc Phục lâm',), ('Phật giáo Tứ Ân Hiếu nghĩa',), 
                       ('Minh Sư đạo',), ('Minh lý đạo - Tam Tông Miếu',), ('Bà-la-môn giáo',), ('Mặc môn',), 
                       ('Phật giáo Hiếu Nghĩa Tà Lơn',), ('Bửu Sơn Kỳ hương',)])

    c.execute("SELECT COUNT(*) FROM hocsinh")
    if c.fetchone()[0] == 0:
        sql_insert_hs = """
        INSERT INTO hocsinh (mahs, hoten, phai, ngaysinh, noisinh, dantoc, tongiao, malop)
        VALUES 
            ('HS325986', 'Đinh Hoàng Phúc', 'Nam', '16/07/2010', 'An Giang', 'Kinh', 'Công giáo', '10A1'),
            ('HS325987', 'Nguyễn Văn A', 'Nam', '20/08/2011', 'An Giang', 'Kinh', 'Phật giáo', '10A1'),
            ('HS325990', 'Đinh Hoàng Phú', 'Nam', '16/07/2011', 'An Giang', 'Kinh', 'Công giáo', '10A1'),
            ('HS325991', 'Nguyễn Thị N', 'Nữ', '22/08/2016', 'HCM', 'Kinh', 'Hồi giáo', '10A2'),
            ('HS325992', 'TRần Hoàng Phú', 'Nam', '16/02/2014', 'An Giang', 'Nùng', 'Công giáo', '10A2'),
            ('HS325993', 'Nguyễn Thị Út', 'Nữ', '20/08/2011', 'Đà Nẵng', 'Khơ-me', 'Phật giáo', '10A2'),
            ('HS325994', 'Trương Đình Hoàng', 'Nam', '11/09/2010', 'An Giang', 'Kinh', 'Công giáo', '10A1'),
            ('HS325995', 'Nguyễn Văn C', 'Nam', '29/04/2011', 'An Giang', 'Kinh', 'Phật giáo', '10A1');
        """
        c.execute(sql_insert_hs)

    # Chèn dữ liệu điểm cho các học sinh nếu bảng điểm trống
    c.execute("SELECT COUNT(*) FROM bangdiem")
    if c.fetchone()[0] == 0:
        c.execute("""
        INSERT INTO bangdiem (mahs, tenmon, hocky, namhoc, diem_mieng, diem_15p, diem_1tiet, diem_thi, diem_tb)
        VALUES 
            ('HS325986', 'Toán', 1, '2025-2026', 8.0, 7.5, 8.5, 8.0, 8.0),
            ('HS325986', 'Ngữ văn', 1, '2025-2026', 7.0, 6.5, 7.0, 7.5, 7.0),
            ('HS325987', 'Toán', 1, '2025-2026', 6.0, 5.5, 6.5, 6.0, 6.0),
            ('HS325987', 'Ngữ văn', 1, '2025-2026', 8.0, 8.0, 7.5, 8.0, 7.9),
            ('HS325990', 'Toán', 1, '2025-2026', 9.0, 8.5, 9.0, 9.5, 9.1),
            ('HS325991', 'Toán', 1, '2025-2026', 7.5, 7.0, 8.0, 7.5, 7.5),
            ('HS325992', 'Ngữ văn', 1, '2025-2026', 6.5, 6.0, 6.5, 7.0, 6.5),
            ('HS325993', 'Toán', 1, '2025-2026', 8.5, 9.0, 8.5, 9.0, 8.8);
        """)

    conn.commit()
    conn.close()

init_database()
print("Khởi tạo CSDL thành công!")