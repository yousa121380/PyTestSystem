import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtCore import QTimer, QDateTime
from PyTestSystemPreparationUI import *
from main import *

class MyPreparationWindow(QMainWindow,Ui_PreMainWindow):
	def  __init__(self,parent=None):
		super(MyPreparationWindow,self).__init__(parent)
		self.setupUi(self)
		self.initUi()
	#初始化准备界面的功能
	def initUi(self):
		self.timer = QTimer()
		self.timer.start()
		self.timer.timeout.connect(self.update_time)
		self.timeTextBrowser.setStyleSheet("font: 12pt \"宋体\";")
		self.noteTextBrowser.setText(self.open_note_file())
		self.logoutButton.clicked.connect(self.logout_func)

	#计时器的槽函数
	def update_time(self):
		#print(QDateTime.currentDateTime().toString('hh:mm:ss'))
		self.timeTextBrowser.setText(QDateTime.currentDateTime().toString('hh:mm:ss'))
	
	#打开注意事项文本文件
	def open_note_file(self):
		textFile=open('./Doc/note.txt','r',encoding='utf-8')
		fo=textFile.read()
		textFile.close()
		return fo
	#通过传入参数来设置右上角的用户信息
	def set_information(self,stuName,stuGrade):
		self.preStuNameLabel.setText(stuName)
		self.preStuGradeLabel.setText(stuGrade)

	def logout_func(self):
		self.close()
		self.myWin=MyMainWindow()
		self.myWin.show()
if __name__=='__main__':
	app=QApplication(sys.argv)
	myWin=MyPreparationWindow()
	myWin.show()
	sys.exit(app.exec())