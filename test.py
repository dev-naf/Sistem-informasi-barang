import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget,QDialog,QTableWidgetItem
from PyQt5.QtCore import QSize
from PyQt5.uic import loadUi
from datetime import datetime
class testingWindow1(QDialog):
    def __init__(self):
        super(testingWindow1, self).__init__()
        loadUi("template/menu_tambahBarang.ui", self)
        data =  {
        "Kategori": self.cb_kategori.currentText(),
        "Nama" : self.le_nama.text(),
        "Supplier":self.le_supplier.text(),
        "Info":{"Berat":self.le_berat.text(),
                "Harga Jual":self.le_hargaJual.text(),
                "Harga Pokok":self.le_hargaPokok.text(),
                "Persediaan":self.le_persediaan.text(),
                "Terjual":0
                },
        "Waktu dibuat":str(datetime.now.strftime("%d-%m-%y | %H:%M:%S")),
        "Waktu update":str(datetime.now.strftime("%d-%m-%y | %H:%M:%S")),

    }
        self.btn_Lanjut.clicked.connect(self.nextPage(data))

    def nextPage(self,data):
        TestingWindows2 = testingWindow2()
        stackLayout.addWidget(TestingWindows2)
        stackLayout.setCurrentIndex(stackLayout.currentIndex()+1)
        stackLayout.show()


class testingWindow2(QDialog):
    def __init__(self,data):
        super(testingWindow2, self).__init__()
        loadUi("template/menu_tambahBarangLanjut.ui", self)

app = QApplication(sys.argv)
LoginPage =  testingWindow1()
stackLayout = QStackedWidget()
stackLayout.addWidget(LoginPage)
stackLayout.setFixedSize(QSize(800,550))
stackLayout.show()
app.exec()