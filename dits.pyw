# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dits.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import subprocess as sp
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import sqlite3
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
import threading
def success(self):
    sp.call("c:\python34\pythonw.exe success.pyw")
class Ui_Dialog(object):
    def start(self):
        if self.checkBox.isChecked()==True:
            sex="1"
        elif self.checkBox_2.isChecked()==True:
            sex="0"
        if self.cp.currentText()=="typical angina":
            cp="1"
        elif self.cp.currentText()=="atypical angina":
            cp="2"
        elif self.cp.currentText()=="non-anginal pain":
            cp="3"
        elif self.cp.currentText()=="asymptomatic":
            cp="4"
        if self.restecg.currentText()=="normal":
            restecg="0"
        elif self.restecg.currentText()=="having ST-T wave abnormality":
            restecg="1"
        elif self.restecg.currentText()=="showing probable or definite left ventricular hypertrophy":
            restecg="2"
        if self.checkBox_3.isChecked()==True:
            exang="1"
        elif self.checkBox_4.isChecked()==True:
            exang="0"
        if self.slope.currentText()=="upslopping":
            slope="1"
        elif self.slope.currentText()=="flat":
            slope="2"
        elif self.slope.currentText()=="downslopping":
            slope="3"
        if self.thal.currentText()=="normal":
            thal="3"
        elif self.thal.currentText()=="fixed defect":
            thal="6"
        elif self.thal.currentText()=="reversable defect":
            thal="7"
        con=sqlite3.connect(r'users.db')
        cur=con.cursor()
        #cur.execute('Create table patients(fname text,lname text,IDno text,age text,sex text,medical_aid text,cp text,trestbps text,chol text,fbs text,restecg text,thalach text,exang text,oldpeak text,slope text,ca text,thal text,num text)')
        cur.execute('insert into patients(fname,lname,IDno,age,sex,medical_aid,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal) values("'+self.fname.text()+'","'+self.lname.text()+'","'+self.idno.text()+'","'+self.age.text()+'","'+sex+'","'+self.meno.text()+'","'+cp+'","'+self.rbp.text()+'","'+self.chol.text()+'","'+self.fbs.text()+'","'+restecg+'","'+self.thalac.text()+'","'+exang+'","'+self.oldpeak.text()+'","'+slope+'","'+self.ca.currentText()+'","'+thal+'")')
        con.commit()
        cur.execute('select * from patients')
        data=cur.fetchall()
        print(data)
        sp.call("c:\python34\pythonw.exe success.pyw")
        exit()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(805, 581)
        self.fname = QtGui.QLineEdit(Dialog)
        self.fname.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.fname.setObjectName(_fromUtf8("fname"))
        self.lname = QtGui.QLineEdit(Dialog)
        self.lname.setGeometry(QtCore.QRect(320, 50, 121, 20))
        self.lname.setObjectName(_fromUtf8("lname"))
        self.idno = QtGui.QLineEdit(Dialog)
        self.idno.setGeometry(QtCore.QRect(110, 100, 113, 20))
        self.idno.setObjectName(_fromUtf8("idno"))
        self.meno = QtGui.QLineEdit(Dialog)
        self.meno.setGeometry(QtCore.QRect(110, 150, 113, 20))
        self.meno.setObjectName(_fromUtf8("meno"))
        self.age = QtGui.QLineEdit(Dialog)
        self.age.setGeometry(QtCore.QRect(110, 200, 71, 20))
        self.age.setObjectName(_fromUtf8("age"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(110, 250, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 250, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(26, 100, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(6, 150, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(46, 210, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(46, 250, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cp = QtGui.QComboBox(Dialog)
        self.cp.setGeometry(QtCore.QRect(110, 320, 121, 22))
        self.cp.setObjectName(_fromUtf8("cp"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(26, 320, 61, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 380, 61, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rbp = QtGui.QLineEdit(Dialog)
        self.rbp.setGeometry(QtCore.QRect(110, 380, 71, 20))
        self.rbp.setObjectName(_fromUtf8("rbp"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 430, 91, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.chol = QtGui.QLineEdit(Dialog)
        self.chol.setGeometry(QtCore.QRect(110, 430, 71, 20))
        self.chol.setObjectName(_fromUtf8("chol"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(500, 50, 101, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.fbs = QtGui.QLineEdit(Dialog)
        self.fbs.setGeometry(QtCore.QRect(620, 50, 71, 20))
        self.fbs.setObjectName(_fromUtf8("fbs"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(380, 110, 171, 41))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.restecg = QtGui.QComboBox(Dialog)
        self.restecg.setGeometry(QtCore.QRect(560, 120, 241, 22))
        self.restecg.setObjectName(_fromUtf8("restecg"))
        self.thalac = QtGui.QLineEdit(Dialog)
        self.thalac.setGeometry(QtCore.QRect(620, 170, 71, 20))
        self.thalac.setObjectName(_fromUtf8("thalac"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(450, 170, 151, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(466, 230, 121, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(620, 230, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(690, 230, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(550, 280, 47, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.oldpeak = QtGui.QLineEdit(Dialog)
        self.oldpeak.setGeometry(QtCore.QRect(620, 270, 71, 20))
        self.oldpeak.setObjectName(_fromUtf8("oldpeak"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(560, 330, 47, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.slope = QtGui.QComboBox(Dialog)
        self.slope.setGeometry(QtCore.QRect(620, 320, 121, 22))
        self.slope.setObjectName(_fromUtf8("slope"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(480, 380, 121, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(490, 390, 121, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.ca = QtGui.QComboBox(Dialog)
        self.ca.setGeometry(QtCore.QRect(620, 380, 121, 22))
        self.ca.setObjectName(_fromUtf8("ca"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(570, 430, 51, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.thal = QtGui.QComboBox(Dialog)
        self.thal.setGeometry(QtCore.QRect(620, 430, 121, 22))
        self.thal.setObjectName(_fromUtf8("thal"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 530, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.start)
        self.cp.addItem("typical angina")
        self.cp.addItem("atypical angina")
        self.cp.addItem("non-anginal pain")
        self.cp.addItem("asymptomatic")
        self.restecg.addItem("normal ")
        self.restecg.addItem("having ST-T wave abnormality")
        self.restecg.addItem("showing probable or definite left ventricular hypertrophy")
        self.slope.addItem("upslopping")
        self.slope.addItem("flat")
        self.slope.addItem("downslopping")
        self.ca.addItem("0")
        self.ca.addItem("1")
        self.ca.addItem("2")
        self.ca.addItem("3")
        self.thal.addItem("normal")
        self.thal.addItem("fixed defect")
        self.thal.addItem("reversable defect")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "User Details", None))
        self.checkBox.setText(_translate("Dialog", "Male", None))
        self.checkBox_2.setText(_translate("Dialog", "Female", None))
        self.label.setText(_translate("Dialog", "First Name", None))
        self.label_2.setText(_translate("Dialog", "Last Name", None))
        self.label_3.setText(_translate("Dialog", "ID number", None))
        self.label_4.setText(_translate("Dialog", "Medical Aid Number", None))
        self.label_5.setText(_translate("Dialog", "age", None))
        self.label_6.setText(_translate("Dialog", "Sex", None))
        self.label_7.setText(_translate("Dialog", "Chest Pain", None))
        self.label_8.setText(_translate("Dialog", "Resting Bp", None))
        self.label_9.setText(_translate("Dialog", "Serum Cholesterol", None))
        self.label_10.setText(_translate("Dialog", "Fasting Blood Sugar", None))
        self.label_11.setText(_translate("Dialog", "resting electrocardiographic results", None))
        self.label_12.setText(_translate("Dialog", "maximum heart rate achieved", None))
        self.label_13.setText(_translate("Dialog", "exercise induced angina", None))
        self.checkBox_3.setText(_translate("Dialog", "Yes", None))
        self.checkBox_4.setText(_translate("Dialog", "No", None))
        self.label_14.setText(_translate("Dialog", "oldpeak", None))
        self.label_15.setText(_translate("Dialog", "slope", None))
        self.label_16.setText(_translate("Dialog", " number of major vessels ", None))
        self.label_17.setText(_translate("Dialog", "colored by flourosopy  ", None))
        self.label_18.setText(_translate("Dialog", "thal", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

