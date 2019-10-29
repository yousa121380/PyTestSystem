INICIO = 2700
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        # 设置托盘图标及菜单
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon(':/icon/Time_32px.png'))
        self.trayIcon.setToolTip(u'番茄时钟')
        self.trayIcon.activated.connect(self.trayClick)
            
        trayMenu = QtGui.QMenu(QtGui.QApplication.desktop())
        exitAction = trayMenu.addAction(u'退出')
        exitAction.triggered.connect(self.exit)
        self.trayIcon.setContextMenu(trayMenu)
        
        # 设置倒计时时长
        self.timer = QtCore.QTimer()
        text = "%d:%02d" % (2700/60,2700 % 60)
        self.lcdNumber.display(text)
        self.timer.timeout.connect(self.updateTimerDisplay)
    
    # 开始
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap((":/icon/pause_524px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton.setIcon(icon)
        
        # 设置播放按钮为不可用
        self.pushButton.setEnabled(False)
        # 设置暂停键可用
        self.pushButton_2.setEnabled(True)
        # self.inicio = INICIO
        self.timer.start(1000)
    
    def updateTimerDisplay(self):
        global INICIO
        INICIO -= 1
        text = "%d:%02d" % (INICIO/60, INICIO % 60)
        text = self.lcdNumber.display(text)
        if INICIO == 0:
            self.timer.stop()
            # todo
            # 时间到了之后，播放按键恢复，时间恢复。
            INICIO = 2700
            text = "%d:%02d" % (INICIO/60, INICIO % 60)
            text = self.lcdNumber.display(text)
            self.pushButton.setEnabled(True)
            self.trayIcon.hide()
            self.showNormal()
    
    
    # 暂停 
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.timer.stop()


    @pyqtSignature("")
    # 重置
    def on_pushButton_3_clicked(self):
        global INICIO
        INICIO = 2700
        self.pushButton_2.setEnabled(True)
        text = "%d:%02d" % (INICIO/60, INICIO % 60)
        text = self.lcdNumber.display(text)
        self.timer.start(1000)
    def changeEvent(self, event):
        '''改变事件'''
        # 判断是否为最小化事件
        if event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized():
            # 设置隐藏窗体 
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.Tool)
            # 显示托盘图标
            self.trayIcon.show()
            
    def exit(self):
        # 不设置Visible为False，退出后TrayIcon不会刷新
        self.trayIcon.setVisible(False)
        sys.exit(0)
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 
            u'警告!', u'你是否真的退出?', 
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, 
            QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            self.trayIcon.show()
            self.hide()
            event.ignore()
        # self.trayIcon.setVisible(False)
        # sys.exit(0)
        
    def trayClick(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.trayIcon.hide()
            self.showNormal()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())