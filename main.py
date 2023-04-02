from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QLabel, QTableWidgetItem
from firebase_admin import initialize_app
from firebase_admin import credentials
from  firebase_admin import firestore
from encrypt import Encrypt
from datetime import datetime


'''
    ADMINISTRATOR ROLE
        admin@naf.io
        admin -> sha256
        ADMINISTRATOR
    OWNER
        owner@naf.io
        owner -> sha256
        OWNER
    EMPLOYEE
        employ@naf.io
        employ -> sha256
        EMPLOYEE
'''
#  Login Page
class loginPage(QDialog):
    def __init__(self):
        super(loginPage, self).__init__()
        # Initialize Db and  authorization in firebase
        Credential = credentials.Certificate("credentialFile.json")
        initialize_app(Credential)
        self.database = firestore.client()

        # UI mechanism
        loadUi('template/login.ui',self)
        self.leEmail.setPlaceholderText('Contoh : Test@gmail.com')
        self.lePassword.setPlaceholderText('*****')
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnLogin.clicked.connect(self.loginProcess)
    def loginProcess(self):
        # Mekanisme LOGIN
        authenticationCollection = self.database.collection('authentication')
        authDocs = authenticationCollection.stream()
        emailInpUser = self.leEmail.text()  # Ambil data dari from input Email dan Password
        passwordInpUser = self.lePassword.text()

        for docs in authDocs:  # Cari  Email dan Password HASH SAMA
            if emailInpUser == docs.to_dict()['email']:
                print("EMAIL OK")
                if Encrypt.process(passwordInpUser).hexdigest() == docs.to_dict()['password']:
                    if docs.to_dict()['role'] == "ADMINISTRATOR":
                        Admin_Menu_Page = admin_Menu_Page()
                        stackLayout.addWidget(Admin_Menu_Page)
                        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
                        stackLayout.show()
                    elif docs.to_dict()['role'] == "OWNER":
                        Owner_Menu_Page = owner_Menu_Page()
                        stackLayout.addWidget(Owner_Menu_Page)
                        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
                        stackLayout.show()
                    else :
                        Employ_Menu_Page = employ_Menu_Page()
                        stackLayout.addWidget(Employ_Menu_Page)
                        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
                        stackLayout.show()

# Administrator Menu Page
class admin_Menu_Page(QDialog):
    def __init__(self):
        super(admin_Menu_Page, self).__init__()
        loadUi("template/menu_Administrator.ui",self)
        self.lblPengaturan.mousePressEvent = self.showPengaturanPage
        self.lblBarang.mousePressEvent = self.showMenuBarang
        self.lblKeuangan.mousePressEvent = self.showMenuKeuangan
        self.lbl_Exit.mousePressEvent = self.exitProcess
    def showPengaturanPage(self,event):
        # Logic to Show Page
        Pengaturan_Menu_Page = pengaturan_Menu_Page()
        stackLayout.addWidget(Pengaturan_Menu_Page)
        stackLayout.setCurrentIndex(stackLayout.currentIndex()+1)
        stackLayout.show()
    def showMenuBarang(self,event):
        Menu_Administrator_Barang = menu_Administrator_Barang()
        stackLayout.addWidget(Menu_Administrator_Barang)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def exitProcess(self,event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex()+1)
        stackLayout.show()
    def showMenuKeuangan(self,event):
        Menu_Administrator_Keuangan = menu_Administrator_Keuangan()
        stackLayout.addWidget(Menu_Administrator_Keuangan)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()

# Pengaturan Menu Page
class pengaturan_Menu_Page(QDialog):
    def __init__(self):
        super(pengaturan_Menu_Page, self).__init__()
        loadUi("template/menu_pengaturan_administrator.ui",self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lbl_tambahAkun.mousePressEvent = self.tambahAkunPage
    def exitProcess(self,event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex()+1)
        stackLayout.show()
    def backProcess(self,event):
        BackProcess = admin_Menu_Page()
        stackLayout.addWidget(BackProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def tambahAkunPage(self,event):
        TambahAkun_Page = tambahAkun_Page()
        stackLayout.addWidget(TambahAkun_Page)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()

# Tampilan Menu Pemilik
class owner_Menu_Page(QDialog):
    def __init__(self):
        super(owner_Menu_Page, self).__init__()
        loadUi("template/menu_Owner.ui",self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
    def exitProcess(self,event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex()+1)
        stackLayout.show()

# Tampilan Menu Pekerja
class employ_Menu_Page(QDialog):
    def __init__(self):
        super(employ_Menu_Page, self).__init__()
        loadUi("template/menu_Employee.ui",self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
    def exitProcess(self,event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex()+1)
        stackLayout.show()

# Tambah Akun
class tambahAkun_Page(QDialog):
    def __init__(self):
        super(tambahAkun_Page, self).__init__()
        loadUi("template/menu_tambahAkun.ui", self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.lbl_Back.mousePressEvent = self.backProcess
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_daftar.clicked.connect(self.registerProcess)
        self.lbl_warning.setText("")
    def exitProcess(self, event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def backProcess(self, event):
        Pengaturan_Menu_Page = pengaturan_Menu_Page()
        stackLayout.addWidget(Pengaturan_Menu_Page)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def registerProcess(self):
        if(self.le_nama.text()=="" or self.le_email.text()=="" or self.le_password.text()=="" or self.le_password2.text()==""):
            self.lbl_warning.setText("ISI SEMUA DATA !")
        elif(self.le_password.text()!=self.le_password2.text()):
            self.lbl_warning.setText("PASSWORD TIDAK SESUAI")
        else:
            self.lbl_warning.setText("")
            newUserData = {
                            "email":self.le_email.text(),
                            "name":self.le_nama.text(),
                            "password": Encrypt.process(self.le_password.text()).hexdigest(),
                            "role" : self.comboBox.currentText()
            }
        database = firestore.client()
        try:
            data =database.collection("authentication").document()
            data.set(newUserData)
        except Exception as e:
            print(e)
        tambahAkun_Sukses = menu_tambahAkun_sukses()
        stackLayout.addWidget(tambahAkun_Sukses)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()

# Mekanisme Exit
class exit_Page(QDialog):
    def __init__(self):
        super(exit_Page, self).__init__()
        loadUi('template/login.ui', self)
        self.leEmail.setPlaceholderText('Contoh : Test@gmail.com')
        self.lePassword.setPlaceholderText('*****')
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnLogin.clicked.connect(self.loginProcess)
    def loginProcess(self):
        # Mekanisme LOGIN
        self.database = firestore.client()
        authenticationCollection = self.database.collection('authentication')
        authDocs = authenticationCollection.stream()
        emailInpUser = self.leEmail.text()  # Ambil data dari from input Email dan Password
        passwordInpUser = self.lePassword.text()

        for docs in authDocs:  # Cari  Email dan Password HASH SAMA
            if emailInpUser == docs.to_dict()['email']:
                print("EMAIL OK")
                if Encrypt.process(passwordInpUser).hexdigest() == docs.to_dict()['password']:
                    if docs.to_dict()['role'] == "ADMINISTRATOR":
                        Admin_Menu_Page = admin_Menu_Page()
                        stackLayout.addWidget(Admin_Menu_Page)
                        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
                        stackLayout.show()
                    elif docs.to_dict()['role'] == "OWNER":
                        Owner_Menu_Page = owner_Menu_Page()
                        stackLayout.addWidget(Owner_Menu_Page)
                        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
                        stackLayout.show()
                    else:
                        Employ_Menu_Page = employ_Menu_Page()
                        stackLayout.addWidget(Employ_Menu_Page)
                        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
                        stackLayout.show()

# Halaman Buat Akun Berhasil
class menu_tambahAkun_sukses(QDialog):
    def __init__(self):
        super(menu_tambahAkun_sukses, self).__init__()
        loadUi('template/menu_TambahPenggunaSukses.ui',self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
    def exitProcess(self, event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()

# Halaman Menu Administrator Barang
class menu_Administrator_Barang(QDialog):
    def __init__(self):
        super(menu_Administrator_Barang, self).__init__()
        loadUi('template/menu_Administrator_Barang.ui',self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lblTambahBarang.mousePressEvent = self.tambahBarangPage
        self.lblTambahStokBarang.mousePressEvent = self.tambahStokBarangPage
    def exitProcess(self, event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def backProcess(self,event):
        BackProcess = admin_Menu_Page()
        stackLayout.addWidget(BackProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def tambahBarangPage(self,event):
        Menu_Administrator_TambahBarangBaru = menu_Administrator_TambahBarangBaru()
        stackLayout.addWidget(Menu_Administrator_TambahBarangBaru)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def tambahStokBarangPage(self,event):
        Menu_TambahStokBarang = menu_TambahStokBarang()
        stackLayout.addWidget(Menu_TambahStokBarang)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
# Halaman Menu Administrator Keuangan
class menu_Administrator_Keuangan(QDialog):
    def __init__(self):
        super(menu_Administrator_Keuangan, self).__init__()
        loadUi('template/menu_Administrator_Keuangan.ui',self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.lbl_Back.mousePressEvent = self.backProcess
    def exitProcess(self, event):
            ExitProcess = exit_Page()
            stackLayout.addWidget(ExitProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def backProcess(self, event):
            BackProcess = admin_Menu_Page()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
# Halaman Menu Administrator Keuangan
class menu_Administrator_TambahBarangBaru(QDialog):
    def __init__(self):
        super(menu_Administrator_TambahBarangBaru, self).__init__()
        loadUi('template/menu_Administrator_Tambahbarangbaru.ui',self)
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lblSemuaData.mousePressEvent = self.semuaDataBarangPage
        self.lblTambahData.mousePressEvent = self.tambahDataBarangPage
    def exitProcess(self, event):
            ExitProcess = exit_Page()
            stackLayout.addWidget(ExitProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def backProcess(self, event):
            BackProcess = menu_Administrator_Barang()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def semuaDataBarangPage(self,event):
        Menu_Administrator_SemuaBarang = menu_Administrator_SemuaBarang()
        stackLayout.addWidget(Menu_Administrator_SemuaBarang)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def tambahDataBarangPage(self,event):
        Menu_TambahBarang = menu_TambahBarang()
        stackLayout.addWidget(Menu_TambahBarang)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
# Halaman Page Semua Barang
class menu_Administrator_SemuaBarang(QDialog):
    def __init__(self):
        super(menu_Administrator_SemuaBarang, self).__init__()
        loadUi('template/menu_Administrator_SemuaBarang.ui', self)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Retrive Data
        database = firestore.client()
        data = database.collection('Barang')
        temp = data.stream()
        data = data.stream()
        baris = 0
        # Counting Data
        count = 0
        for Data in temp:
            count = count + 1
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1, 160)

        # Add Data to Table
        for Data in data:
            dataFinal = Data.to_dict()
            print('{} ==>>{}\n'.format(Data.id,dataFinal))
            self.tableWidget.setItem(baris,0,QTableWidgetItem(dataFinal['Nama']))
            self.tableWidget.setItem(baris,1, QTableWidgetItem(dataFinal['Kategori']))
            self.tableWidget.setItem(baris,2, QTableWidgetItem(str(dataFinal['Info']['Persediaan'])))
            self.tableWidget.setItem(baris,3, QTableWidgetItem(str(dataFinal['Info']['Terjual'])))
            self.tableWidget.setItem(baris,4, QTableWidgetItem(str(dataFinal['Info']['Harga Pokok'])))
            self.tableWidget.setItem(baris,5, QTableWidgetItem(str(dataFinal['Info']['Harga Jual'])))
            baris = baris+1

        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.lbl_Back.mousePressEvent = self.backProcess
    def exitProcess(self, event):
            ExitProcess = exit_Page()
            stackLayout.addWidget(ExitProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def backProcess(self, event):
            BackProcess = menu_Administrator_TambahBarangBaru()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
# Halaman Page tambah barang
class menu_TambahBarang(QDialog):
    def __init__(self):
        super(menu_TambahBarang, self).__init__()
        loadUi('template/menu_tambahBarang.ui', self)
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.btn_Lanjut.clicked.connect(self.tambahBarangLanjut)
        self.Time = datetime.now()
    def exitProcess(self, event):
            ExitProcess = exit_Page()
            stackLayout.addWidget(ExitProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def backProcess(self, event):
            BackProcess = menu_Administrator_TambahBarangBaru()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def tambahBarangLanjut(self,event):
        self.dataBarang = {
            "Nama": self.le_nama.text(),
            "Kategori": self.cb_kategori.currentText(),
            "Supplier": self.le_supplier.text(),
            "Waktu dibuat" :self.Time.strftime("%d-%m-%y | %H:%M:%S"),
            "Waktu update" :self.Time.strftime("%d-%m-%y | %H:%M:%S")
        }
        tambahBarangLanjut = menu_TambahBarangLanjut(self.dataBarang)
        stackLayout.addWidget(tambahBarangLanjut)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
# Halaman Page tambah barang Lanjut
class menu_TambahBarangLanjut(QDialog):
    def __init__(self,dataBarang):
        super(menu_TambahBarangLanjut, self).__init__()
        self.DataBarang = dataBarang
        print(self.DataBarang)

        loadUi('template/menu_tambahBarangLanjut.ui', self)
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.btn_tambah.clicked.connect(self.addDataProcess)
    def exitProcess(self, event):
            ExitProcess = exit_Page()
            stackLayout.addWidget(ExitProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def backProcess(self, event):
            BackProcess = menu_Administrator_TambahBarangBaru()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    def addDataProcess(self):
        self.DataBarang['Info'] = {
            "Berat" : self.le_berat.text(),
            "Harga Jual" :self.le_hargaJual.text(),
            "Harga Pokok" : self.le_hargaPokok.text(),
            "Terjual" : 0,
            "Persediaan" : self.le_persediaan.text()
        }
        db = firestore.client()
        dbData = db.collection('Barang').document()
        dbData.set(self.DataBarang)
        TambahBarangSukses = menu_TambahBarangSukses()
        stackLayout.addWidget(TambahBarangSukses)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
# Halaman Page tambah barang sukses
class menu_TambahBarangSukses(QDialog):
    def __init__(self):
        super(menu_TambahBarangSukses, self).__init__()
        loadUi('template/menu_TambahBarangSukses.ui',self)
        self.lbl_Back.mousePressEvent = self.backProcess

    def backProcess(self, event):
            BackProcess = menu_Administrator_TambahBarangBaru()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
# Halaman Page tambah stok barang
class menu_TambahStokBarang(QDialog):
    def __init__(self):
        self.status = False
        super(menu_TambahStokBarang, self).__init__()
        loadUi('template/menu_Administrator_TambahStokBarang.ui',self)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.selectionModel().selectionChanged.connect(self.checkSelection)
        # Retrive Data
        database = firestore.client()
        data = database.collection('Barang')
        temp = data.stream()
        data = data.stream()
        baris = 0
        # Counting Data
        count = 0
        self.dataID = []
        for Data in temp:
            count = count + 1
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 160)
        # Add Data to Table
        for Data in data:
            dataFinal = Data.to_dict()
            self.dataID.append(Data.id)
            self.tableWidget.setItem(baris, 0, QTableWidgetItem(dataFinal['Nama']))
            self.tableWidget.setItem(baris, 1, QTableWidgetItem(dataFinal['Kategori']))
            self.tableWidget.setItem(baris, 2, QTableWidgetItem(str(dataFinal['Info']['Persediaan'])))
            self.tableWidget.setItem(baris, 3, QTableWidgetItem(str(dataFinal['Info']['Terjual'])))
            self.tableWidget.setItem(baris, 4, QTableWidgetItem(str(dataFinal['Info']['Harga Pokok'])))
            self.tableWidget.setItem(baris, 5, QTableWidgetItem(str(dataFinal['Info']['Harga Jual'])))
            baris = baris + 1
        self.btnPilih.clicked.connect(self.retriveID)
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lbl_Exit.mousePressEvent = self.exitProcess
    # Fungsi Mengambil ID
    def retriveID(self):
        if(self.status):
            tableIndex = self.tableWidget.currentRow()
            self.retriveDatabyID(self.dataID[tableIndex])
        # memberikan warning pada user
    # Fungsi melakukan Cek Table yang sudah ter-select
    def checkSelection(self,selected,deselected):
        if(selected):
            self.status = True
    # Fungsi mengembalikan ke halaman sebelumya.
    def backProcess(self, event):
            BackProcess = menu_Administrator_Barang()
            stackLayout.addWidget(BackProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    # Fungsi mengembalikan ke halaman Login
    def exitProcess(self, event):
            ExitProcess = exit_Page()
            stackLayout.addWidget(ExitProcess)
            stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
            stackLayout.show()
    # Fungsi mengambil data berdasarkan ID
    def retriveDatabyID(self,id):
        database = firestore.client()
        data = database.collection('Barang')
        result = data.stream()
        for Data in result:
            if id == Data.id:
                retriveData = Data.to_dict()

        FormStokBarang = menu_FormTambahStokBarang(retriveData,id)
        stackLayout.addWidget(FormStokBarang)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()

# Menu Form Tambah Stok Barang
class menu_FormTambahStokBarang(QDialog):
    def __init__(self,data,id):
        self.Id = id
        self.Data = data
        super(menu_FormTambahStokBarang, self).__init__()
        loadUi('template/menu_FormTambahStokBarang.ui',self)
        self.le_nama.setText(self.Data['Nama'])
        self.le_nama.setEnabled(False)
        self.le_kategori.setText(self.Data['Kategori'])
        self.le_kategori.setEnabled(False)
        self.lbl_Back.mousePressEvent = self.backProcess
        self.lbl_Exit.mousePressEvent = self.exitProcess
        self.btn_tambahStok.clicked.connect(self.tambahStokProcess)
    def backProcess(self, event):
        BackProcess = menu_TambahStokBarang()
        stackLayout.addWidget(BackProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
        # Fungsi mengembalikan ke halaman Login
    def exitProcess(self, event):
        ExitProcess = exit_Page()
        stackLayout.addWidget(ExitProcess)
        stackLayout.setCurrentIndex(stackLayout.currentIndex() + 1)
        stackLayout.show()
    def tambahStokProcess(self):
        db = firestore.client()
        data = db.reference('Barang').child(self.Id)
        result = data.stream()
        print(result)


app = QApplication([])
LoginPage =  loginPage()
stackLayout = QStackedWidget()
stackLayout.addWidget(LoginPage)
stackLayout.setFixedSize(QSize(800,550))
stackLayout.show()
app.exec()


# LOGIN,REGISTER, TAMBAH BARANG,