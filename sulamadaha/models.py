from sulamadaha import db

# =======================
# TABEL PENGUNJUNG
# =======================
class TPengguna(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"TPengguna('{self.nama}', '{self.email}', '{self.password}')"

# =======================
# TABEL PENJUAL
# =======================
class TPenjual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"TPenjual('{self.nama}', '{self.email}', '{self.password}')"

# =======================
# TABEL ADMIN
# =======================
class TAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"TAdmin('{self.nama}', '{self.email}', '{self.password}')"

# =======================
# TABEL PAKET WISATA
# =======================
class TPaketWisata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pengunjung = db.Column(db.Integer, db.ForeignKey('t_pengguna.id'))
    id_penjual = db.Column(db.Integer, db.ForeignKey('t_penjual.id'))
    nama_paket = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    harga = db.Column(db.Float, nullable=False)
    durasi = db.Column(db.Integer, nullable=False)

    pengunjung = db.relationship('TPengguna', backref='paket_wisata_dibuat', lazy=True)
    penjual = db.relationship('TPenjual', backref='paket_wisata', lazy=True)

    def __repr__(self):
        return f"TPaketWisata('{self.nama_paket}', '{self.deskripsi}', '{self.harga}', '{self.durasi}')"

# =======================
# TABEL BOOKING
# =======================
class TBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pengguna = db.Column(db.Integer, db.ForeignKey('t_pengguna.id'), nullable=False)
    id_paket = db.Column(db.Integer, db.ForeignKey('t_paket_wisata.id'), nullable=False)
    tanggal_booking = db.Column(db.Date, nullable=False)
    status_booking = db.Column(db.String(20), nullable=False, default='menunggu')  # ENUM disimulasikan

    pengunjung = db.relationship('TPengguna', backref='bookings', lazy=True)
    paket = db.relationship('TPaketWisata', backref='bookings', lazy=True)

    def __repr__(self):
        return f"TBooking(Paket={self.tanggal_booking}, '{self.status_booking}')"

# =======================
# TABEL PEMBAYARAN
# =======================
class TPembayaran(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_booking = db.Column(db.Integer, db.ForeignKey('t_booking.id'), nullable=False)
    metode = db.Column(db.String(50))
    total_pembayaran = db.Column(db.Float)
    status_pembayaran = db.Column(db.String(20), nullable=False, default='belum')  # ENUM disimulasikan
    tanggal_bayar = db.Column(db.Date)

    booking = db.relationship('TBooking', backref='pembayaran', lazy=True)

    def __repr__(self):
        return f"TPembayaran('{self.metode}', '{self.total_pembayaran}', '{self.status_pembayaran}', '{self.tanggal_bayar}')"
