# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


import sqlite3
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

header_row = ['age','sex','pain','BP','chol','fbs','ecg','maxhr','eiang','eist','slope','vessels','thal','class']
df=pd.read_csv('processed.cleveland.data',names=header_row)
df.replace('?',-99999, inplace=True)
#df.drop(['id'], 1, inplace=True)
a=0
for i in df['class']: 
    if i>0:
        df.set_value(a,['class'],1)
    a=a+1


con=sqlite3.connect(r'users.db')
cur=con.cursor()
class Ui_Dialog(object):
    def delete(self):
        stuff=self.listWidget_2.currentItem().text()
        cur.execute('delete from patients where IDno="'+stuff+'"')
        self.listWidget_3.clear()
        con.commit()
        self.load()
        
    def predict(self):
        self.listWidget_4.clear()
        stuff=self.listWidget_2.currentItem().text()
        cur.execute('select age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal from patients where IDno="'+stuff+'"')
        da=cur.fetchall()
        for x in da:
            print(x)
            X = np.array(df.drop(['class'], 1))
            y = np.array(df['class'])

            X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.6)

            clf = neighbors.KNeighborsClassifier()
            clf.fit(X_train, y_train)
            accuracy = clf.score(X_test, y_test)
            x=list(map(float,x))
            example=np.array(x)
            example=example.reshape(1,-1)
            print(accuracy)

            chance=accuracy*100
            prediction=clf.predict(example)
            print(prediction[0])
            if prediction[0]==1:
                self.listWidget_4.addItem("Patient has coronary heart disease.")
            if prediction[0]==0:
                self.listWidget_4.addItem("Patient does not have coronary heart disease.")
        
        
    def select(self,stuff):
        self.listWidget_3.clear()
        stuff=self.listWidget_2.currentItem().text()
        cur.execute('select * from patients where IDno="'+stuff+'"')
        dat=cur.fetchall()
        for x in dat:
            for i in x:
                self.listWidget_3.addItem(i)
                
        
        
    def load(self):
        self.listWidget_2.clear()
        self.listWidget.clear()

        
        cur.execute('select fname from patients')
        data=cur.fetchall()
        for i in data:
            for x in i:
                self.listWidget.addItem(x)
        cur.execute('select IDno from patients')
        data=cur.fetchall()
        for i in data:
            for x in i:
                self.listWidget_2.addItem(x)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(805, 581)
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 181, 441))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget_2 = QtGui.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(220, 70, 191, 441))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 47, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget_3 = QtGui.QListWidget(Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(570, 70, 221, 351))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.listWidget_2.itemClicked.connect(self.select)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(570, 40, 47, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.listWidget_4 = QtGui.QListWidget(Dialog)
        self.listWidget_4.setGeometry(QtCore.QRect(470, 470, 321, 41))
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(470, 450, 47, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 540, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.predict)
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 540, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.delete)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(500, 40, 47, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(520, 70, 47, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(520, 90, 47, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(520, 130, 47, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(520, 110, 47, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(520, 180, 47, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(506, 160, 61, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(520, 190, 47, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(520, 150, 47, 13))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(520, 310, 47, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(520, 230, 47, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(520, 220, 47, 13))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(520, 290, 47, 13))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(520, 250, 47, 13))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(520, 270, 47, 13))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(520, 210, 47, 13))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(520, 330, 47, 13))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(520, 350, 47, 13))
        self.label_22.setObjectName(_fromUtf8("label_22"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.load()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Patients", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.label_2.setText(_translate("Dialog", "ID", None))
        self.label_3.setText(_translate("Dialog", "Data", None))
        self.label_4.setText(_translate("Dialog", "Prediction", None))
        self.pushButton_2.setText(_translate("Dialog", "Predict", None))
        self.pushButton_3.setText(_translate("Dialog", "Delete", None))
        self.label_5.setText(_translate("Dialog", "Features", None))
        self.label_6.setText(_translate("Dialog", "Fname", None))
        self.label_7.setText(_translate("Dialog", "Lname", None))
        self.label_8.setText(_translate("Dialog", "Age", None))
        self.label_9.setText(_translate("Dialog", "IDno", None))
        self.label_10.setText(_translate("Dialog", "cp", None))
        self.label_11.setText(_translate("Dialog", "Medical_aid", None))
        self.label_12.setText(_translate("Dialog", "trestbps", None))
        self.label_13.setText(_translate("Dialog", "sex", None))
        self.label_14.setText(_translate("Dialog", "slope", None))
        self.label_15.setText(_translate("Dialog", "restecg", None))
        self.label_16.setText(_translate("Dialog", "fbs", None))
        self.label_17.setText(_translate("Dialog", "oldpeak", None))
        self.label_18.setText(_translate("Dialog", "thalac", None))
        self.label_19.setText(_translate("Dialog", "exang", None))
        self.label_20.setText(_translate("Dialog", "chol", None))
        self.label_21.setText(_translate("Dialog", "ca", None))
        self.label_22.setText(_translate("Dialog", "thal", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

