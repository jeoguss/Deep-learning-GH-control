from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as canvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore,QtGui,QtSerialPort
from PyQt5.QtCore import QIODevice,pyqtSignal,QObject
import sys,time,threading,random

form_class = uic.loadUiType("window.ui")[0]     # UI프로그램을 작화한 파일을 로딩하여 사용하기위해 작성합니다. ( 클래스로 만들어요~! )

class MyWindow(QMainWindow,form_class):     # 위단에서 만든 클래스를 상속하여 사용함니다. ( QMainWindow 클래스와 다중 상속 사용 )

    btn_connection_name = {"connect":"연결하기","close":"연결끊기"}     # 사용되는 문자열을 딕셔너리 자료형을 이용하여 관리합니다.

    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 타이틀을 제거
        self.setupUi(self)  # ui파일로 구성한 자료를 화면으로 구성 _ 관련 객체 및 바인딩 실시.

        #콤보박스 속성 설정.
        self.combo_portName.addItems(["serial0","serial1"])     #serial0 : Rs232, serial1 : Rs485
        self.combo_baudRate.addItems(["9600","57600","115200"])     # 통신속도
        self.combo_target.addItems(["A0","A1","A2","A3","A4","A5","A6","A7"])   # 그래프로 표현할 소스

        #차트 영역 설정.
        plt.ion()   # 바로바로 그래프로 표현할 수 있도록 설정해줍니다.
        self.fig = plt.Figure()                 #figure 영역
        self._canvas = canvas(self.fig)   #canvas 설정
        self.layout_view.addWidget(self._canvas) # 캔버스를 레이아웃에 배치 --> 차트 출력목적.
        self.ax = self.fig.add_subplot(1,1,1)   # axes생성
        self.line_1 = self.ax.plot([random.random() * 1024 for i in range(0,26)],'b-')[0] # 그래프를 생성하며, 초기화면의 출력을 위해 랜덤값으로 그래프를 그립니다. ( 선색은 파랑색~! )


        #버튼 시그널 설정.
        self.btn_connection.clicked.connect(self.slot_connection)       # 시리얼 통신포트 연결
        self.btn_close.clicked.connect(self.slot_close)                         # 프로그램 종료

    def slot_connection(self):
        if self.btn_connection.text() == self.btn_connection_name["connect"]:       # connect : 연결하기
            #활성화할 포트정보를 읽어옵니다.
            baudRate = int(self.combo_baudRate.currentText())
            portName = '/dev/' + self.combo_portName.currentText()
            targetName = self.combo_target.currentText()

            #시리얼통신을 관장할 객체를 생성하며 설정합니다.
            self._comm = QtSerialPort.QSerialPort()
            self._comm.setPortName(portName)
            self._comm.setBaudRate(baudRate)

            #시리얼 통신을 활성화하며 시리얼 통신포트로부터 수신되는 값을 감시할 스레드를 생성합니다.
            self._comm.open(QIODevice.ReadWrite)
            self.serialThread = self.serialThreadClass(self._comm,self.fig,self.line_1,targetName)
            self.btn_connection.setText(self.btn_connection_name['close'])              # close : 연결끊기
            self.serialThread.start()   # 스레드를 실행합니다.
        else:
            #시리얼포트가 열려있다면, 관련 리소스를 종료합니다.
            if self._comm.isOpen() == True:
                self.serialThread.stop()
                self.serialThread.join()
                self._comm.close()
            self.btn_connection.setText(self.btn_connection_name["connect"])        # connect : 연결하기

    def slot_close(self):
            #시리얼 포트가 열려있다면, 관련 리소스를 반환하고 시리얼 포트를 비활성합니다.
        if self._comm.isOpen() == True:
            self.serialThread.stop()
            self.serialThread.join()
            self._comm.close()
        #화면을 닫습니다.
        self.close()

    class serialThreadClass(threading.Thread):
        def __init__(self,portObj,fig,line,targetName):
            super().__init__()
            self.isRun = False
            self.port = portObj
            self.fig = fig
            self.line = line
            self.targetName = targetName
            self.ydata = [0 for i in range(0,26)]
            self.plotEventMsg = self.SerialReceivedDataClass()  #시그널을 관리할 객체 생성.
            self.plotEventMsg.receiveAnalogValueEvent.connect(self.receivedAnalogData)      # 시그널 receivedAanalogData을 처리할 슬롯을 등록합니다.

        def run(self):
            while self.isRun == True:
                if int(self.port.bytesAvailable()) >= 4 :
                    time.sleep(0.05)    # 10ms 지연.
                    received_bytes = self.port.read(4)
                    targetName = received_bytes[0:2].decode('utf-8')
                    targetValue = int.from_bytes(received_bytes[2:4],'little')

                    # readAll 명령을 사용할 경우, bytes 자료타입이 아닌, qbytearray타입으로 처리되므로 아래와같이 사용해주셔야합니다.
                    # received_bytes = self.port.readAll()
                    #targetName = received_bytes.data()[0:2].decode('utf-8')
                    #targetValue = int.from_bytes(received_bytes.data()[2:4],'little')

                    if targetName == self.targetName:
                        self.plotEventMsg.receiveAnalogValueEvent.emit(targetValue)

        def start(self):
            self.isRun = True
            super().start()

        def stop(self):
            if self.isRun == True:
                self.isRun = False

        def receivedAnalogData(self,analogValue):

            #큐형식 사용
            del self.ydata[0]   #가장 오래된 데이터를 지웁니다.
            self.ydata.append(analogValue)  # 새로운 데이터를 추가합니다.

            self.line.set_ydata(self.ydata) #y값을 갱신합니다.
            self.fig.canvas.draw()              # 갱신된 상태의 그래프를 출력합니다.

        class SerialReceivedDataClass(QObject):
            signalHandle = pyqtSignal(bytes, name="receiveAnalogValueEvent")        # 시그널을 정의합니다. 해다 시그널을 처리할 슬롯은 반드시 bytes 매개변수를 받아야합니다.
            def __init__(self):
                super().__init__()

if __name__ == "__main__":  # 해당 스크립트이 main으로 동작할 경우에만 실행되도록해요~!
    app = QApplication(sys.argv)
    app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
