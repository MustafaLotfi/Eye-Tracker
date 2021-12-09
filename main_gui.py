from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from codes.work import Worker
import os


PATH2ROOT = os.path.dirname(__file__) + "/"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 477)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowIcon(QtGui.QIcon(PATH2ROOT + "docs/images/logo.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.l_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_name.setFont(font)
        self.l_name.setObjectName("l_name")
        self.gridLayout.addWidget(self.l_name, 3, 0, 1, 1)
        self.cb_gf = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_gf.setFont(font)
        self.cb_gf.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_gf.setChecked(True)
        self.cb_gf.setObjectName("cb_gf")
        self.gridLayout.addWidget(self.cb_gf, 10, 4, 1, 3)
        self.le_age = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.le_age.setFont(font)
        self.le_age.setObjectName("le_age")
        self.gridLayout.addWidget(self.le_age, 4, 1, 1, 3)
        self.cb_clb = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_clb.setFont(font)
        self.cb_clb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_clb.setChecked(True)
        self.cb_clb.setObjectName("cb_clb")
        self.gridLayout.addWidget(self.cb_clb, 2, 0, 1, 3)
        self.cb_see_tst = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_see_tst.setFont(font)
        self.cb_see_tst.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_see_tst.setChecked(False)
        self.cb_see_tst.setObjectName("cb_see_tst")
        self.gridLayout.addWidget(self.cb_see_tst, 11, 4, 1, 4)
        self.cb_tst = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_tst.setFont(font)
        self.cb_tst.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_tst.setChecked(False)
        self.cb_tst.setObjectName("cb_tst")
        self.gridLayout.addWidget(self.cb_tst, 8, 4, 1, 2)
        self.cb_gp = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_gp.setFont(font)
        self.cb_gp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_gp.setChecked(True)
        self.cb_gp.setObjectName("cb_gp")
        self.gridLayout.addWidget(self.cb_gp, 10, 0, 1, 3)
        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.le_name.setFont(font)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 3, 1, 1, 7)
        self.cb_smp = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_smp.setFont(font)
        self.cb_smp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_smp.setChecked(True)
        self.cb_smp.setObjectName("cb_smp")
        self.gridLayout.addWidget(self.cb_smp, 8, 0, 1, 3)
        self.cb_mdl = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_mdl.setFont(font)
        self.cb_mdl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_mdl.setChecked(True)
        self.cb_mdl.setObjectName("cb_mdl")
        self.gridLayout.addWidget(self.cb_mdl, 9, 0, 1, 3)
        self.b_stop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.b_stop.setFont(font)
        self.b_stop.setObjectName("b_stop")
        self.gridLayout.addWidget(self.b_stop, 15, 0, 1, 3)
        self.te_dsc = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.te_dsc.setFont(font)
        self.te_dsc.setDocumentTitle("")
        self.te_dsc.setObjectName("te_dsc")
        self.gridLayout.addWidget(self.te_dsc, 6, 0, 1, 8)
        self.rb_m = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rb_m.setFont(font)
        self.rb_m.setChecked(True)
        self.rb_m.setObjectName("rb_m")
        self.gridLayout.addWidget(self.rb_m, 4, 7, 1, 1)
        self.l_gnd = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_gnd.setFont(font)
        self.l_gnd.setObjectName("l_gnd")
        self.gridLayout.addWidget(self.l_gnd, 4, 5, 1, 1)
        self.l_grd = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_grd.setFont(font)
        self.l_grd.setObjectName("l_grd")
        self.gridLayout.addWidget(self.l_grd, 7, 0, 1, 3)
        self.l_cam_id = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_cam_id.setFont(font)
        self.l_cam_id.setObjectName("l_cam_id")
        self.gridLayout.addWidget(self.l_cam_id, 0, 4, 1, 2)
        self.cb_cam = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_cam.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_cam.setFont(font)
        self.cb_cam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_cam.setChecked(True)
        self.cb_cam.setObjectName("cb_cam")
        self.gridLayout.addWidget(self.cb_cam, 1, 0, 1, 3)
        self.le_grd = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.le_grd.setFont(font)
        self.le_grd.setObjectName("le_grd")
        self.gridLayout.addWidget(self.le_grd, 7, 4, 1, 4)
        self.l_dsc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_dsc.setFont(font)
        self.l_dsc.setObjectName("l_dsc")
        self.gridLayout.addWidget(self.l_dsc, 5, 0, 1, 3)
        self.l_age = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_age.setFont(font)
        self.l_age.setObjectName("l_age")
        self.gridLayout.addWidget(self.l_age, 4, 0, 1, 1)
        self.cb_see_smp = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_see_smp.setFont(font)
        self.cb_see_smp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_see_smp.setChecked(False)
        self.cb_see_smp.setObjectName("cb_see_smp")
        self.gridLayout.addWidget(self.cb_see_smp, 11, 0, 1, 4)
        self.rb_f = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.rb_f.setFont(font)
        self.rb_f.setObjectName("rb_f")
        self.gridLayout.addWidget(self.rb_f, 4, 6, 1, 1)
        self.le_num = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.le_num.setFont(font)
        self.le_num.setObjectName("le_num")
        self.gridLayout.addWidget(self.le_num, 0, 2, 1, 2)
        self.b_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.b_start.setFont(font)
        self.b_start.setObjectName("b_start")
        self.gridLayout.addWidget(self.b_start, 14, 0, 1, 3)
        self.l_num = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.l_num.setFont(font)
        self.l_num.setObjectName("l_num")
        self.gridLayout.addWidget(self.l_num, 0, 0, 1, 2)
        self.le_cam_id = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.le_cam_id.setFont(font)
        self.le_cam_id.setObjectName("le_cam_id")
        self.gridLayout.addWidget(self.le_cam_id, 0, 6, 1, 2)
        self.cb_all_mns = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cb_all_mns.setFont(font)
        self.cb_all_mns.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_all_mns.setChecked(True)
        self.cb_all_mns.setObjectName("cb_all_mns")
        self.gridLayout.addWidget(self.cb_all_mns, 12, 0, 1, 3)
        self.l_monitor = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.l_monitor.setFont(font)
        self.l_monitor.setObjectName("l_monitor")
        self.gridLayout.addWidget(self.l_monitor, 14, 3, 2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.see_data_uncheck()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eye Tracker"))
        self.l_name.setText(_translate("MainWindow", "Name:"))
        self.cb_gf.setText(_translate("MainWindow", "Get Fixations"))
        self.le_age.setText(_translate("MainWindow", "25"))
        self.cb_clb.setText(_translate("MainWindow", "Calibration   "))
        self.cb_see_tst.setText(_translate("MainWindow", "See Testing Data"))
        self.cb_tst.setText(_translate("MainWindow", "Testing"))
        self.cb_gp.setText(_translate("MainWindow", "Get Pixels"))
        self.l_monitor.setText(_translate("MainWindow", "Press Start"))
        self.le_name.setText(_translate("MainWindow", "Mostafa Lotfi"))
        self.cb_smp.setText(_translate("MainWindow", "Sampling"))
        self.cb_mdl.setText(_translate("MainWindow", "Modeling"))
        self.b_stop.setText(_translate("MainWindow", "Stop"))
        self.te_dsc.setMarkdown(_translate("MainWindow", "Phone Number: +989368385420\n"
"\n"
""))
        self.rb_m.setText(_translate("MainWindow", "M"))
        self.l_gnd.setText(_translate("MainWindow", "Gender:"))
        self.l_grd.setText(_translate("MainWindow", "Calibration Grid:"))
        self.l_cam_id.setText(_translate("MainWindow", "Camera ID:"))
        self.cb_cam.setText(_translate("MainWindow", "See Camera"))
        self.le_grd.setText(_translate("MainWindow", "4, 200, 6, 100"))
        self.l_dsc.setText(_translate("MainWindow", "Descriptions:"))
        self.l_age.setText(_translate("MainWindow", "Age:"))
        self.cb_see_smp.setText(_translate("MainWindow", "See Sampling Data"))
        self.rb_f.setText(_translate("MainWindow", "F"))
        self.le_num.setText(_translate("MainWindow", "1"))
        self.b_start.setText(_translate("MainWindow", "Start"))
        self.l_num.setText(_translate("MainWindow", "Subject ID:"))
        self.le_cam_id.setText(_translate("MainWindow", "0"))
        self.cb_all_mns.setText(_translate("MainWindow", "Use All Monitors"))

    def do(self):
        self.b_start.clicked.connect(self.b_start_action)
        self.b_start.clicked.connect(lambda: self.b_start.setEnabled(False))
        self.b_stop.clicked.connect(self.b_stop_action)
        self.cb_clb.clicked.connect(self.clb_uncheck)
        self.cb_see_smp.clicked.connect(self.see_data_uncheck)
        self.cb_see_tst.clicked.connect(self.see_data_uncheck)
        
    def b_start_action(self):
        self.name = self.le_name.text()
        self.num = int(self.le_num.text())
        self.age = int(self.le_age.text())
        self.dsc = self.te_dsc.toPlainText()
        self.cam_id = int(self.le_cam_id.text())
        clb_grid_txt = self.le_grd.text()

        clb_grid_txt = " " + clb_grid_txt + " "
        sep = []
        sep.append(0)
        for pos, s in enumerate(clb_grid_txt):
            if s == ',':
                sep.append(pos)

        sep.append(len(clb_grid_txt)-1)
        grid_len = len(sep)
        self.clb_grid = []
        for i in range(grid_len-1):
            self.clb_grid.append(int(clb_grid_txt[sep[i]+1:sep[i+1]]))

        if self.rb_m.isChecked():
            self.gender = "M"
        else:
            self.gender = "F"

        self.worker = Worker()

        self.worker.num = self.num
        self.worker.camera_id = self.cam_id
        self.worker.info = (self.name, self.gender, self.age, self.dsc)
        self.worker.clb_grid = self.clb_grid

        if self.cb_cam.checkState() == 2:
            self.worker.cam = True
        if self.cb_clb.checkState() == 2:
            self.worker.clb = True
        if self.cb_smp.checkState() == 2:
            self.worker.smp = True
        if self.cb_tst.checkState() == 2:
            self.worker.tst = True
        if self.cb_mdl.checkState() == 2:
            self.worker.mdl = True
        if self.cb_gp.checkState() == 2:
            self.worker.gp = True
        if self.cb_gf.checkState() == 2:
            self.worker.gf = True
        if self.cb_see_smp.checkState() == 2:
            self.worker.see_smp = True
        if self.cb_see_tst.checkState() == 2:
            self.worker.see_tst = True

        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.do_work)

        self.thread.start()

        self.worker.finished.connect(self.thread.quit)
        self.worker.cam_started.connect(lambda: self.monitor("Camera"))
        self.worker.clb_started.connect(lambda: self.monitor("Calibration"))
        self.worker.smp_started.connect(lambda: self.monitor("Sampling"))
        self.worker.tst_started.connect(lambda: self.monitor("Testing"))
        self.worker.mdl_started.connect(lambda: self.monitor("Tuning params"))
        self.worker.gp_started.connect(lambda: self.monitor("Getting pixels"))
        self.worker.gf_started.connect(lambda: self.monitor("Getting fixations"))
        self.worker.see_smp_started.connect(lambda: self.monitor("Seeing sampling pixels"))
        self.worker.see_tst_started.connect(lambda: self.monitor("Seeing testing pixels"))
        
        self.worker.finished.connect(lambda: self.monitor("Eye Tracking finished!"))
        self.worker.finished.connect(lambda: self.b_start.setEnabled(True))


    def b_stop_action(self):
        self.worker.running = False

    def monitor(self, txt):
        self.l_monitor.setText(txt)

    def clb_uncheck(self):
        if self.cb_clb.checkState() == 2:
            self.le_name.setEnabled(True)
            self.le_age.setEnabled(True)
            self.rb_m.setEnabled(True)
            self.rb_f.setEnabled(True)
            self.te_dsc.setEnabled(True)
            self.le_grd.setEnabled(True)
        else:
            self.le_name.setEnabled(False)
            self.le_age.setEnabled(False)
            self.rb_m.setEnabled(False)
            self.rb_f.setEnabled(False)
            self.te_dsc.setEnabled(False)
            self.le_grd.setEnabled(False)

    def see_data_uncheck(self):
        if (self.cb_see_smp.checkState() == 0) and (self.cb_see_tst.checkState() == 0):
            self.cb_all_mns.setEnabled(False)
        else:
            self.cb_all_mns.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.do()
    MainWindow.show()
    sys.exit(app.exec_())
