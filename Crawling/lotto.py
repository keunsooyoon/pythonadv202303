# 로또 번호 조회 앱

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup as bs

form_class = uic.loadUiType("lotto.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 단추를 누르면
        self.pushButton.clicked.connect(self.btnclicked)


    # 조회 후 칸에 출력
    def btnclicked(self):
        url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin"
        txt = requests.get(url)
        html = bs(txt.text)
        lottery = html.select("span.ball_645")
        when = html.select("p.desc")[0].text

        self.date_label.setText(when)

        self.num1.setText(lottery[0].text)    
        self.num2.setText(lottery[1].text)  
        self.num3.setText(lottery[2].text)   
        self.num4.setText(lottery[3].text)   
        self.num5.setText(lottery[4].text)   
        self.num6.setText(lottery[5].text)    
        self.num7.setText(lottery[6].text)  

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()