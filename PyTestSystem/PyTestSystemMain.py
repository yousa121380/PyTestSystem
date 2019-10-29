import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QStackedWidget
from PyQt5.QtCore import QTimer, QDateTime,Qt
from PyTestSystemMainUI import *
#from main import *

class MyMainWindow(QMainWindow,Ui_MainTestWindow):
	def  __init__(self,parent=None):
		super(MyMainWindow,self).__init__(parent)
		self.setupUi(self)
		self.initUi()
		self.setQSS()
	#初始化准备界面的功能

	def initUi(self):
		self.selectRadioButton.clicked.connect(lambda:self.change_to_select(0))
		self.fillRadioButton.clicked.connect(lambda:self.change_to_select(1))
		self.selectRadioButton.setChecked(True)

		#初始化buttongroup的groupid
		for i in range(1,16):
			for j in range(1,5):
				self.setGroupId(eval("self.select_"+str(i)+"_ButtonGroup"),
					eval("self.checkBox_"+str(i)+"_"+str(j)),j) 
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_func)
		self.INICIO=2701
		self.timer.start(1000)

		#self.tabWidget.currentChanged.connect(lambda: print(self.tabWidget.currentIndex()))
		#print(self.select_1_ButtonGroup.id(self.checkBox_1_3))
	def change_to_select(self,index):
		self.stackedWidget.setCurrentIndex(index)
		
	def setQSS(self):
		pass

	def setGroupId(self,Group,button,id):
		Group.setId(button,id)
	def update_func(self):
		self.INICIO -= 1
		text = "%d:%02d" % (self.INICIO/60, self.INICIO % 60)
		text = self.leftTimeTextBrowser.setText(text)
		if self.INICIO == 0:
			self.timer.stop()
			# todo
            # 时间到了之后，播放按键恢复，时间恢复。
			self.INICIO = 2700
			text = "%d:%02d" % (INICIO/60, INICIO % 60)
			text = self.leftTimeTextBrowser.setText(text)
if __name__=='__main__':
	app=QApplication(sys.argv)
	myWin=MyMainWindow()
	eval("myWin.show()")
	sys.exit(app.exec())