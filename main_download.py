from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from downloadvideo import DowloadVideo

class MenuWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = uic.loadUi('Gui/main_video_plus.ui')

        self.window.pushButton.clicked.connect(self.dow)

    def dow(self):
        link = self.window.lineEdit.text()


        if link == "":
            QMessageBox.critical(self.window, "Alerta", "Não Pode existir campos vasios")

        else:
            if self.window.radioButton.isChecked():
                file_name = QtWidgets.QFileDialog.getSaveFileName()[0]
                DowloadVideo(link, file_name).dowload_mp4()

            elif self.window.radioButton_2.isChecked():
                file_name = QtWidgets.QFileDialog.getSaveFileName()[0]
                DowloadVideo(link, file_name).dowload_mp3()

            else:
                QMessageBox.critical(self.window, "Alerta", "Selecione um formarto")

if __name__ == "__main__":
    mw = MenuWindow()
    mw.window.show()
    mw.app.exec_()