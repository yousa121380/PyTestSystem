import sys
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtNetwork import QNetworkAccessManager


class QueryDataBase():
	def __init__(self):
		self.db = None
		self.db_connect()
		
	def db_connect(self):
		#self.db = QSqlDatabase.addDatabase('QSQLITE')  
		if (QSqlDatabase.contains("qt_sql_default_connection")):
			self.db = QSqlDatabase.database("qt_sql_default_connection");
		else:
			self.db = QSqlDatabase.addDatabase('QSQLITE');
		self.db.setDatabaseName('./DataBase/StudentInformation.db')             # 2
		if not self.db.open():                           # 3
			QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())
	def closeEvent(self):                   # 4
		self.db.close()
		#self.db = QSqlDatabase.removeDatabase('QSQLITE')
	def query_table(self):
		query = QSqlQuery("SELECT * FROM SItable",self.db)
		#query.exec_("SELECT * FROM SItable")                # 4
		while query.next():
			stu_name = query.value(0)
			stu_class = query.value(1)
			stu_score = query.value(2)
			print(stu_name, stu_class, stu_score)
	#查询学生密码,返回一个所有学生密码的字典
	def query_stu_password(self):
		query=QSqlQuery('SELECT StuNum,StuPassword FROM SItable',self.db)
		#query.exec_('SELECT StuNum,StuPassword FROM SItable')
		stupassword={}
		while query.next():
			stupassword[query.value(0)]=query.value(1)
		#print(stupassword)
		return stupassword
	#查询学生信息，返回一个包含所有学生信息的字典
	def query_stu_information(self):
		query=QSqlQuery('SELECT StuNum,StuName FROM SItable',self.db)
		#query.exec_('SELECT StuNum,StuName FROM SItable')
		stuInformation={}
		while query.next():
			stuInformation[query.value(0)]=query.value(1)
		return stuInformation
if __name__ == '__main__':
	demo = QueryDataBase()
	demo.query_table()
	demo.query_stu_information()
	demo.closeEvent()