import sys
import time
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow,QMessageBox,QLineEdit
from PyTestSystem1 import *
from QueryDataBase import *
from Preparation import *
from QSSTool import QSSTool
#USER_PWD = {
#        'a': 'b'
#    }

class MyMainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None):
		super(MyMainWindow,self).__init__(parent)
		stu=QueryDataBase()
		self.USER_INF=stu.query_stu_information()
		self.USER_PWD=stu.query_stu_password()
		stu.closeEvent()
		self.setupUi(self)
		self.initUi()
		self.setQSS()
		
	#初始化UI的signal和初始状态
	def initUi(self):
		self.pushButton.clicked.connect(self.show_message)
		self.pushButton.setEnabled(False)
		self.pushButton_2.clicked.connect(self.close)
		self.lineEdit.textChanged.connect(self.check_input_status)
		self.lineEdit_2.setEchoMode(QLineEdit.Password)
		self.lineEdit_2.textChanged.connect(self.check_input_status)
		self.lineEdit.setPlaceholderText("输入你的学号")
		self.lineEdit_2.setPlaceholderText("输入你的密码")
	#根据信息是否正确来调取messagebox
	def show_message(self):
		massage=self.check_message()   #调用数据库
		if massage==True:
			choice = QMessageBox.question(self, '登录成功！', 
								 '欢迎你,'+self.USER_INF.get(self.lineEdit.text())+'同学,是否进入考试界面？',  
                             QMessageBox.Yes | QMessageBox.No)
			if choice==QMessageBox.Yes:
				self.enter_test_system()
			else:
				pass
		else:
			choice = QMessageBox.warning(self, '登录错误！', '你可能输入了错误的学号或者密码，是否重新输入？',  
                             QMessageBox.Yes | QMessageBox.No)
			if choice==QMessageBox.Yes:
				self.lineEdit.clear()
				self.lineEdit_2.clear()
			else:
				pass

	#调用密码字典，检查是否信息正确
	def check_message(self):
		if self.USER_PWD.get(self.lineEdit.text())==self.lineEdit_2.text():
			return True
		else:
			return False
	
	#检查输入栏，如果输入栏都有信息则启用登录按钮
	def check_input_status(self):
		if self.lineEdit.text() and self.lineEdit_2.text()!='':
			self.pushButton.setEnabled(True)
		else:
			self.pushButton.setEnabled(False)

	
	def enter_test_system(self):
		self.close()
		self.myWin=MyPreparationWindow()
		self.myWin.set_information(self.USER_INF.get(self.lineEdit.text()),'2017')
		self.myWin.show()

	def setQSS(self):
		QSSTool.setQssToObj('./QSS/LoginUISheetStyle.QSS',self)
if __name__=='__main__':
	app=QApplication(sys.argv)
	myWin=MyMainWindow()
	myWin.show()
	sys.exit(app.exec())