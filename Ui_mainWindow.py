# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wechat_tools(object):
    def setupUi(self, wechat_tools):
        wechat_tools.setObjectName("wechat_tools")
        wechat_tools.resize(800, 600)
        wechat_tools.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/wechat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wechat_tools.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(wechat_tools)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 530, 621, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(38)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_analyze = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_analyze.setStyleSheet("font: 25 11pt \"Lantinghei\";")
        self.button_analyze.setObjectName("button_analyze")
        self.horizontalLayout.addWidget(self.button_analyze)
        self.button_delete_detection = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_delete_detection.setEnabled(True)
        self.button_delete_detection.setStyleSheet("font: 25 11pt \"Lantinghei\";")
        self.button_delete_detection.setObjectName("button_delete_detection")
        self.horizontalLayout.addWidget(self.button_delete_detection)
        self.button_withdraw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_withdraw.setStyleSheet("font: 25 11pt \"Lantinghei\";")
        self.button_withdraw.setObjectName("button_withdraw")
        self.horizontalLayout.addWidget(self.button_withdraw)
        self.button_robot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_robot.setStyleSheet("font: 25 11pt \"Lantinghei\";")
        self.button_robot.setObjectName("button_robot")
        self.horizontalLayout.addWidget(self.button_robot)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 761, 451))
        self.textBrowser.setStyleSheet("font: 25 12pt \"Microsoft YaHei\";")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 271, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_username = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_username.setObjectName("label_username")
        self.horizontalLayout_2.addWidget(self.label_username)
        self.login_name = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.login_name.setFont(font)
        self.login_name.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.login_name.setObjectName("login_name")
        self.horizontalLayout_2.addWidget(self.login_name)
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(690, 530, 91, 61))
        self.button_login.setMinimumSize(QtCore.QSize(0, 0))
        self.button_login.setStyleSheet("font: 63 13pt \"Lantinghei\";")
        self.button_login.setObjectName("button_login")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(360, 10, 424, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_file_folder = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.open_file_folder.setStyleSheet("font: 63 13pt \"Lantinghei\";")
        self.open_file_folder.setObjectName("open_file_folder")
        self.horizontalLayout_3.addWidget(self.open_file_folder)
        self.button_background = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_background.setStyleSheet("font: 63 13pt \"Lantinghei\";")
        self.button_background.setObjectName("button_background")
        self.horizontalLayout_3.addWidget(self.button_background)
        self.clear_display = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.clear_display.setStyleSheet("font: 63 13pt \"Lantinghei\";")
        self.clear_display.setObjectName("clear_display")
        self.horizontalLayout_3.addWidget(self.clear_display)
        wechat_tools.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wechat_tools)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.setting = QtWidgets.QMenu(self.menubar)
        self.setting.setObjectName("setting")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        wechat_tools.setMenuBar(self.menubar)
        self.file_quit = QtWidgets.QAction(wechat_tools)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_quit.setIcon(icon1)
        self.file_quit.setObjectName("file_quit")
        self.action_2 = QtWidgets.QAction(wechat_tools)
        self.action_2.setObjectName("action_2")
        self.help_about = QtWidgets.QAction(wechat_tools)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/fav.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_about.setIcon(icon2)
        self.help_about.setObjectName("help_about")
        self.help_guide = QtWidgets.QAction(wechat_tools)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_guide.setIcon(icon3)
        self.help_guide.setObjectName("help_guide")
        self.help_register = QtWidgets.QAction(wechat_tools)
        self.help_register.setObjectName("help_register")
        self.help_contact = QtWidgets.QAction(wechat_tools)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/mail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_contact.setIcon(icon4)
        self.help_contact.setObjectName("help_contact")
        self.setting_file_storage_path = QtWidgets.QAction(wechat_tools)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_file_storage_path.setIcon(icon5)
        self.setting_file_storage_path.setObjectName("setting_file_storage_path")
        self.menu.addAction(self.file_quit)
        self.setting.addAction(self.setting_file_storage_path)
        self.menu_3.addAction(self.help_about)
        self.menu_3.addAction(self.help_guide)
        self.menu_3.addAction(self.help_contact)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.setting.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(wechat_tools)
        QtCore.QMetaObject.connectSlotsByName(wechat_tools)

    def retranslateUi(self, wechat_tools):
        _translate = QtCore.QCoreApplication.translate
        wechat_tools.setWindowTitle(_translate("wechat_tools", "WechatTools"))
        self.button_analyze.setText(_translate("wechat_tools", "微信好友分析"))
        self.button_delete_detection.setText(_translate("wechat_tools", "好友删除检测"))
        self.button_withdraw.setText(_translate("wechat_tools", "开启消息防撤回"))
        self.button_robot.setText(_translate("wechat_tools", "开启自动回复机器人"))
        self.label_username.setText(_translate("wechat_tools", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">登录用户名：</span></p></body></html>"))
        self.login_name.setText(_translate("wechat_tools", "<html><head/><body><p>未登陆</p></body></html>"))
        self.button_login.setText(_translate("wechat_tools", "登录"))
        self.open_file_folder.setText(_translate("wechat_tools", "打开撤回文件目录"))
        self.button_background.setText(_translate("wechat_tools", "后台运行"))
        self.clear_display.setText(_translate("wechat_tools", "清除显示"))
        self.menu.setTitle(_translate("wechat_tools", "文件"))
        self.setting.setTitle(_translate("wechat_tools", "设置"))
        self.menu_3.setTitle(_translate("wechat_tools", "帮助"))
        self.file_quit.setText(_translate("wechat_tools", "退出"))
        self.action_2.setText(_translate("wechat_tools", "退出"))
        self.help_about.setText(_translate("wechat_tools", "关于"))
        self.help_guide.setText(_translate("wechat_tools", "使用说明"))
        self.help_register.setText(_translate("wechat_tools", "注册"))
        self.help_contact.setText(_translate("wechat_tools", "联系我们"))
        self.setting_file_storage_path.setText(_translate("wechat_tools", "设置撤回文件存放目录"))


import icon_rc
