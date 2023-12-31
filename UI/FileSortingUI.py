import os
from PySide6.QtCore import Qt, QCoreApplication, QMetaObject, QSize, QRect
from PySide6.QtGui import QIcon, QPixmap, QPalette, QBrush, QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 266)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(0, 45, 79, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Dialog.setPalette(palette)
        Dialog.setAcceptDrops(False)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(80, 141, 171, 22))
        self.lineEdit.setText("Press to sort files in folders    >")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(260, 140, 41, 24))
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(100, 10, 201, 81))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 175, 171, 22))
        self.lineEdit_2.setText("Press to set backup directory >")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 175, 41, 24))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 210, 171, 22))
        self.lineEdit_3.setText("move files in backup directory>")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(260, 210, 41, 24))
        palette1 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        self.label.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Georgia"])
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label_image = QLabel(Dialog)
        self.label_image.setGeometry(QRect(30, -1, 370, 150))
        self.label_image.setScaledContents(True)
        icon_path = os.path.join(os.getcwd(), 'Assets', 'ButtonPurple')
        icon = QIcon(icon_path)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setStyleSheet("background-color: transparent; border: none;")
        icon_path_2 = os.path.join(os.getcwd(), 'Assets', 'ButtonPurple.png')
        icon_2 = QIcon(icon_path_2)
        self.pushButton_2.setIcon(icon_2)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_2.setStyleSheet("background-color: transparent; border: none;")
        icon_path_3 = os.path.join(os.getcwd(), 'Assets', 'ButtonPurple.png')
        icon_3 = QIcon(icon_path_3)
        self.pushButton_3.setIcon(icon_3)
        self.pushButton_3.setIconSize(QSize(32, 32))
        self.pushButton_3.setStyleSheet("background-color: transparent; border: none;")


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", None))
        icon1_path = os.path.join(os.getcwd(), 'Assets', 'logo.png')
        pixmap = QPixmap(icon1_path)
        self.label_image.setPixmap(pixmap)

        QMetaObject.connectSlotsByName(Dialog)

class CustomDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = CustomDialog()
    window.show()
    app.exec()