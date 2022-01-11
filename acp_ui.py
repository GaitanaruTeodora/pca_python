# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acp_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from functii import tabelare_matrice
from geopandas import GeoDataFrame
import numpy as np
from grafice import plot_corelatii,corelograma
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import main_window as mw
import controller
import acp
from spatial import harta
import grafice
import sys
import functii


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(748, 789)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 381, 711))
        self.buton_citire = QPushButton(self.groupBox)
        self.buton_citire.setObjectName(u"buton_citire")
        self.buton_citire.setGeometry(QRect(0, 20, 341, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        self.buton_citire.setPalette(palette)
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(11)
        self.buton_citire.setFont(font)
        self.lista_selectie = QListWidget(self.groupBox)
        self.lista_selectie.setObjectName(u"lista_selectie")
        self.lista_selectie.setGeometry(QRect(10, 130, 331, 481))
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(0, 0, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lista_selectie.setPalette(palette1)
        self.lista_selectie.setFont(font)
        self.ckSelectie = QCheckBox(self.groupBox)
        self.ckSelectie.setObjectName(u"ckSelectie")
        self.ckSelectie.setGeometry(QRect(210, 620, 131, 20))
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(10)
        self.ckSelectie.setFont(font1)
        self.lb_varIndex = QLabel(self.groupBox)
        self.lb_varIndex.setObjectName(u"lb_varIndex")
        self.lb_varIndex.setGeometry(QRect(20, 80, 151, 16))
        self.lb_varIndex.setFont(font)
        self.cbIndex = QComboBox(self.groupBox)
        self.cbIndex.setObjectName(u"cbIndex")
        self.cbIndex.setGeometry(QRect(180, 70, 161, 41))
        self.cbIndex.setFont(font)
        self.lb_axe = QLabel(self.groupBox)
        self.lb_axe.setObjectName(u"lb_axe")
        self.lb_axe.setGeometry(QRect(30, 670, 55, 16))
        self.lb_axe.setFont(font)
        self.cbAxa1 = QComboBox(self.groupBox)
        self.cbAxa1.setObjectName(u"cbAxa1")
        self.cbAxa1.setGeometry(QRect(150, 660, 91, 31))
        self.cbAxa2 = QComboBox(self.groupBox)
        self.cbAxa2.setObjectName(u"cbAxa2")
        self.cbAxa2.setGeometry(QRect(250, 660, 91, 31))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(430, 10, 301, 711))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        self.groupBox_2.setPalette(palette2)
        self.btn_afVarianta = QPushButton(self.groupBox_2)
        self.btn_afVarianta.setObjectName(u"btn_afVarianta")
        self.btn_afVarianta.setGeometry(QRect(20, 20, 261, 41))
        palette3 = QPalette()
        brush5 = QBrush(QColor(85, 85, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(85, 85, 255, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_afVarianta.setPalette(palette3)
        self.btn_afVarianta.setFont(font)
        self.btn_Corelograma = QPushButton(self.groupBox_2)
        self.btn_Corelograma.setObjectName(u"btn_Corelograma")
        self.btn_Corelograma.setGeometry(QRect(20, 250, 261, 41))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_Corelograma.setPalette(palette4)
        self.btn_Corelograma.setFont(font)
        self.btn_afScoruri = QPushButton(self.groupBox_2)
        self.btn_afScoruri.setObjectName(u"btn_afScoruri")
        self.btn_afScoruri.setGeometry(QRect(20, 330, 261, 41))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_afScoruri.setPalette(palette5)
        self.btn_afScoruri.setFont(font)
        self.btn_plotScoruri = QPushButton(self.groupBox_2)
        self.btn_plotScoruri.setObjectName(u"btn_plotScoruri")
        self.btn_plotScoruri.setGeometry(QRect(20, 380, 261, 41))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_plotScoruri.setPalette(palette6)
        self.btn_plotScoruri.setFont(font)
        self.btn_harta = QPushButton(self.groupBox_2)
        self.btn_harta.setObjectName(u"btn_harta")
        self.btn_harta.setGeometry(QRect(20, 430, 261, 41))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_harta.setPalette(palette7)
        self.btn_harta.setFont(font)
        self.btn_plotVarianta = QPushButton(self.groupBox_2)
        self.btn_plotVarianta.setObjectName(u"btn_plotVarianta")
        self.btn_plotVarianta.setGeometry(QRect(20, 70, 261, 41))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_plotVarianta.setPalette(palette8)
        self.btn_plotVarianta.setFont(font)
        self.btn_afCorelatii = QPushButton(self.groupBox_2)
        self.btn_afCorelatii.setObjectName(u"btn_afCorelatii")
        self.btn_afCorelatii.setGeometry(QRect(20, 150, 261, 41))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_afCorelatii.setPalette(palette9)
        self.btn_afCorelatii.setFont(font)
        self.btn_plotCorelatii = QPushButton(self.groupBox_2)
        self.btn_plotCorelatii.setObjectName(u"btn_plotCorelatii")
        self.btn_plotCorelatii.setGeometry(QRect(20, 200, 261, 41))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_plotCorelatii.setPalette(palette10)
        self.btn_plotCorelatii.setFont(font)
        self.btn_cosinusuri = QPushButton(self.groupBox_2)
        self.btn_cosinusuri.setObjectName(u"btn_cosinusuri")
        self.btn_cosinusuri.setGeometry(QRect(20, 510, 261, 41))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_cosinusuri.setPalette(palette11)
        self.btn_cosinusuri.setFont(font)
        self.btn_contributii = QPushButton(self.groupBox_2)
        self.btn_contributii.setObjectName(u"btn_contributii")
        self.btn_contributii.setGeometry(QRect(20, 560, 261, 41))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_contributii.setPalette(palette12)
        self.btn_contributii.setFont(font)
        self.btn_comunalitati = QPushButton(self.groupBox_2)
        self.btn_comunalitati.setObjectName(u"btn_comunalitati")
        self.btn_comunalitati.setGeometry(QRect(20, 610, 261, 41))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_comunalitati.setPalette(palette13)
        self.btn_comunalitati.setFont(font)
        self.btn_corelogramaCom = QPushButton(self.groupBox_2)
        self.btn_corelogramaCom.setObjectName(u"btn_corelogramaCom")
        self.btn_corelogramaCom.setGeometry(QRect(20, 660, 261, 41))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_corelogramaCom.setPalette(palette14)
        self.btn_corelogramaCom.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 748, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Date", None))
        self.buton_citire.setText(QCoreApplication.translate("MainWindow", u"Citire date", None))
        self.ckSelectie.setText(QCoreApplication.translate("MainWindow", u"Selectie totala", None))
        self.lb_varIndex.setText(QCoreApplication.translate("MainWindow", u"Variabila index", None))
        self.lb_axe.setText(QCoreApplication.translate("MainWindow", u"Axe", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rezultate", None))
        self.btn_afVarianta.setText(QCoreApplication.translate("MainWindow", u"Afisare varianta", None))
        self.btn_Corelograma.setText(QCoreApplication.translate("MainWindow", u"Corelograma", None))
        self.btn_afScoruri.setText(QCoreApplication.translate("MainWindow", u"Afisare scoruri", None))
        self.btn_plotScoruri.setText(QCoreApplication.translate("MainWindow", u"Plot scoruri", None))
        self.btn_harta.setText(QCoreApplication.translate("MainWindow", u"Harta GeoPandas", None))
        self.btn_plotVarianta.setText(QCoreApplication.translate("MainWindow", u"Plot varianta", None))
        self.btn_afCorelatii.setText(QCoreApplication.translate("MainWindow", u"Afisare corelatii", None))
        self.btn_plotCorelatii.setText(QCoreApplication.translate("MainWindow", u"Plot corelatii", None))
        self.btn_cosinusuri.setText(QCoreApplication.translate("MainWindow", u"Cosinusuri", None))
        self.btn_contributii.setText(QCoreApplication.translate("MainWindow", u"Contributii", None))
        self.btn_comunalitati.setText(QCoreApplication.translate("MainWindow", u"Comunalitati", None))
        self.btn_corelogramaCom.setText(QCoreApplication.translate("MainWindow", u"Corelograma comunalitati", None))

    # retranslateUi


class Frame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Frame,self).__init__()
        self.setupUi(self)
        self.k_s = 2
        self.lista_variabile = self.lista_selectie
        self.buton_citire.clicked.connect(self.citire)
        self.btn_afVarianta.clicked.connect(self.afisare_varianta)
        self.btn_plotVarianta.clicked.connect(self.afisare_plot_varianta)
        self.lista_selectie.itemSelectionChanged.connect(self.selectionChanged)
        self.ckSelectie.clicked.connect(lambda x: controller.selectie_generala(self.lista_variabile))
        self.btn_harta.clicked.connect(self.afisare_harta)
        self.btn_afCorelatii.clicked.connect(self.afisare_corelatie)
        self.btn_plotCorelatii.clicked.connect(self.plot_corelatii)
        self.btn_Corelograma.clicked.connect(self.afisare_corelograma)
        self.btn_cosinusuri.clicked.connect(self.afisare_cosinusuri)
        self.btn_contributii.clicked.connect(self.afisare_contributii)
        self.btn_comunalitati.clicked.connect(self.afisare_comunalitati)
        self.btn_corelogramaCom.clicked.connect(self.afisare_corelograma_com)
        self.btn_afScoruri.clicked.connect(self.afisare_scoruri)
        self.btn_plotScoruri.clicked.connect(self.afisare_plot_scoruri)

    def afisare_plot_scoruri(self):
        self.t_r_xc = tabelare_matrice(
            self.model_acp.r_xc,
            self.variabile_selectate,
            self.model_acp.etichete_componente,
            "Output/r_xc.csv"
        )
        q = self.model_acp.nrcomp_p
        if self.model_acp.nrcomp_c is not None and self.model_acp.nrcomp_c < q:
            q = self.model_acp.nrcomp_c
        if self.model_acp.nrcomp_k is not None and self.model_acp.nrcomp_k < q:
            q = self.model_acp.nrcomp_k

        plot_corelatii(self.t_r_xc, "comp"+self.cbAxa1.currentText(),"comp"+self.cbAxa2.currentText(), aspect=1)

    def afisare_scoruri(self):

        self.t_scoruri = tabelare_matrice(
            self.model_acp.c / np.sqrt(self.model_acp.alfa),
            self.t.index, self.model_acp.etichete_componente,"Output/scoruri.csv")


        tabel = mw.Tabel(self.t_scoruri)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = QDialog()
        dialog.setWindowTitle("Scoruri")
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()
    def afisare_corelograma_com(self):
        corelograma(self.comm_t, vmin=0, titlu="Comunalitati")

    def afisare_comunalitati(self):
        r_xc2 = self.model_acp.r_xc * self.model_acp.r_xc
        comm = np.cumsum(r_xc2, axis=1)
        self.comm_t = tabelare_matrice(comm, self.variabile_selectate, self.model_acp.etichete_componente, "Output/comm.csv")
        tabel = mw.Tabel(self.comm_t)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = QDialog()
        dialog.setWindowTitle("Contributii")
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()

    def afisare_contributii(self):
        beta = self.c2 * 100 / np.sum(self.c2, axis=0)
        self.beta_t = tabelare_matrice(beta, self.t.index,
                                  self.model_acp.etichete_componente,
                                  "Output/contrib.csv")
        tabel = mw.Tabel(self.beta_t)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = QDialog()
        dialog.setWindowTitle("Contributii")
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()

    def afisare_cosinusuri(self):

        self.c2 = self.model_acp.c * self.model_acp.c
        cosin = np.transpose(self.c2.T / np.sum(self.c2, axis=1))
        self.cosin_t = tabelare_matrice(cosin, self.t.index,
                                   self.model_acp.etichete_componente, "Output/cosin.csv")
        tabel = mw.Tabel(self.cosin_t)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = QDialog()
        dialog.setWindowTitle("Cosinusuri")
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()
    def afisare_corelograma(self):
        corelograma(self.r_xc_t)
    def plot_corelatii(self):
        plot_corelatii(self.r_xc_t, "comp"+self.cbAxa1.currentText(),"comp"+self.cbAxa2.currentText(), aspect=1)


    def afisare_corelatie(self):
        self.r_xc_t = tabelare_matrice(self.model_acp.r_xc, self.variabile_selectate,
                                  self.model_acp.etichete_componente, "Output/r_xc.csv")
        tabel = mw.Tabel(self.r_xc_t)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = QDialog()
        dialog.setWindowTitle("Corelatii")
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()
    def afisare_harta(self):
        if self.model_creat is False:
            self.C = self.creare_model()

        if self.model_creat:
            shp = GeoDataFrame.from_file("Europa/Europa.shp")
            print(shp, list(shp), sep="\n")
            harta(shp, self.C[:, :7], 'Code', self.t.index)

            # plot_map(fisier_shp, self.C[:, 0:self.k_s], [i for i in range(36)])

    def selectionChanged(self):
        # variabile = controller.selectii_lista(self.lista_selectie)
    #         # controller.init_combo(self.cbAxa1, variabile)
    #         # controller.init_combo(self.cbAxa2, variabile)
    #         # self.cbAxa1.setCurrentIndex(0)
    #         # self.cbAxa2.setCurrentIndex(1)
        pass

    def citire(self):
        rezultat = controller.citire_fisier_variabile(self.cbIndex, self.lista_selectie)
        self.tabel_date = rezultat
        self.cbIndex.clear()
        if rezultat is not None:
            self.t = rezultat[0]
            functii.nan_replace(self.t)

    def afisare_plot_varianta(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            j_Cattel, j_Kaiser = self.model_acp.plot_varianta()
            self.k_s =min(j_Cattel, j_Kaiser)
            self.model_acp.show_grafice()

    def afisare_varianta(self):
        self.variabile_selectate = controller.selectii_lista(self.lista_selectie)

        self.m = len(self.variabile_selectate)

        if self.m < 2:
            msgBox = QMessageBox()
            msgBox.setText("Prea putine variabile selectate!")
            msgBox.exec()
            return

        self.model_acp = acp.acp(self.t, self.variabile_selectate)
        self.C = self.model_acp.creare_model(std=True, nlib=0)
        tabel_varianta = self.model_acp.tabelare_varianta()
        print(tabel_varianta)
        tabel = mw.Tabel(tabel_varianta)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        dialog = QDialog()
        dialog.setWindowTitle("Varianta componentelor")
        dialog.setLayout(layout1)
        dialog.setModal(True)
        dialog.exec_()

        for i in range(1, self.m + 1):
            self.cbAxa1.addItem(str(i))
            self.cbAxa2.addItem(str(i))
        self.cbAxa1.setCurrentIndex(0)
        self.cbAxa2.setCurrentIndex(1)
        self.model_creat = True



aplicatie = QApplication(sys.argv)
main_frame = Frame()
main_frame.show()
aplicatie.exec_()





