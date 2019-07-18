#!/usr/bin/python3
# Main with Threading
import sys
import time
from time import strftime
import RPi.GPIO as GPIO
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from bluetooth import *
# This is our window from QtCreator
import mainwindow_auto
import SmartGrid_auto
 
triggered = 0
swOpen = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.OUT)

GPIO.output(12, True)
GPIO.output(16, True)
GPIO.output(20, True)
GPIO.output(21, True)
GPIO.output(19, True)

class btObject(QtCore.QThread):
  btSignal = QtCore.pyqtSignal(str)

  def run(self):
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]


    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "SampleServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )

                       
    print("Waiting for connection on RFCOMM channel %d "% (port))

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        while True:
            data = client_sock.recv(1024)
            newD = data.decode('utf-8')
            self.btSignal.emit(newD)
    except IOError:
        pass

    client_sock.close()
    server_sock.close()


class blackoutObject(QtCore.QThread):
  blackoutSignal = QtCore.pyqtSignal()
  onSignal1 = QtCore.pyqtSignal()
  onSignal2 = QtCore.pyqtSignal()
  onSignal3 = QtCore.pyqtSignal()

  
  def turnOn(self, x, y, z):
      time.sleep(5)
      GPIO.output(x, True)
      self.onSignal1.emit()
      time.sleep(3)
      GPIO.output(y, True)
      self.onSignal2.emit()
      time.sleep(3)
      GPIO.output(z, True)
      self.onSignal3.emit()

  def emitSignal(self):
      self.blackoutSignal.emit()

  def blackout(self, state):
      GPIO.output(12, False)
      GPIO.output(16, False)
      GPIO.output(20, False)
      GPIO.output(21, False)
      if(state == 0):
          self.turnOn(16,20,21)
      if(state == 1):
          self.turnOn(16,21,20)
      if(state == 2):
          self.turnOn(20,16,21)
      if(state == 3):
          self.turnOn(20,21,16)
      if(state == 4):
          self.turnOn(21,16,20)
      if(state == 5):
          self.turnOn(21,20,16)

  def __init__(self,parent=None):
    super(self.__class__, self).__init__(parent)
    global triggered
    triggered = 0  
    state = 0


  def run(self):
      global triggered
      state = 0
      print("RUNNING")
      while True:
          if((triggered == 0) and (GPIO.input(26) == False)):     # Trigger blackout activity
              falSteady = 0
              dbnCounter = 0
              while dbnCounter < 1000:
                if GPIO.input(26) == False:
                  falSteady+=1
                dbnCounter+=1
              if(falSteady > 950):
                triggered = 1
                self.emitSignal()
                self.blackout(state%6)
                state+= 1
          elif((triggered == 1) and (GPIO.input(26))):
              time.sleep(1)
              truSteady = 0
              dbnCounter = 0
              while dbnCounter < 1000:
                if GPIO.input(26) == True:
                  truSteady+=1
                dbnCounter+=1
              if(truSteady > 950):
                GPIO.output(12, True)
                triggered = 0

class timerThread(QtCore.QThread):
	timeElapsed = QtCore.pyqtSignal(int)

	def __init__(self, parent=None):
		super(timerThread, self).__init__(parent)
		self.timeStart = None

	def start(self, timeStart):
		self.timeStart = timeStart

		return super(timerThread, self).start()

	def run(self):
		while self.parent().isRunning():
			self.timeElapsed.emit(time.time() - self.timeStart)
			time.sleep(1)

class myThread(QtCore.QThread):
	timeElapsed = QtCore.pyqtSignal(int)
	def __init__(self, parent=None):
            super(myThread, self).__init__(parent)
            self.timerThread = timerThread(self)
            self.timerThread.timeElapsed.connect(self.timeElapsed.emit)

	def run(self):
            global triggered
            self.timerThread.start(time.time())
            while triggered == 1:
              x = 1
            self.parent().lcdCustomerOut.display(0)

class SmartGridWindow(QMainWindow, SmartGrid_auto.Ui_MainWindow):
  
  def lcdCustomerOut(self):
  	self.lcdCustomerOut = PyQt5.QtWidgets(self)

  def lcdTotalCustomer(self):
  	self.lcdTotalCustomer = PyQt5.QtWidgets(self)

  def handlepushButton(self):
        global triggered
        global swOpen
        if(triggered == 0):
          self.close()
          swOpen = 0

  def lcdtimer(self):
  	self.lcdtimer = PyQt5.QtWidgets(self)

  def btnStart(self):
    self.btnStart = PyQt5.QtWidgets(self)

  @QtCore.pyqtSlot(int)
  def on_myThread_timeElapsed(self, seconds):
    self.lcdtimer.display("{0}".format(seconds))

  @QtCore.pyqtSlot()
  def on_myThread_finished(self):
    print("Done")

  	
  def __init__(self, parent=None):
    super(self.__class__, self).__init__(parent)
    self.setupUi(self) 
    self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    self.lcdCustomerOut.display(0)
    self.lcdTotalCustomer.display(5000)
    self.pushButton.clicked.connect(self.handlepushButton)
    self.myThread = myThread(self)
    self.myThread.timeElapsed.connect(self.on_myThread_timeElapsed)
    self.myThread.finished.connect(self.on_myThread_finished)
  
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
   
 # access variables inside of the UI's file
 def lcdBostonNeed(self):
 	self.lcdBostonNeed = PyQt5.QtWidgets(self)

 def lcdRenewable(self):
 	self.lcdRenewable = PyQt5.QtWidgets(self)

 def lcdPercentGreen(self):
 	self.lcdPercentGreen = PyQt5.QtWidgets(self)

 def handleSmartGridButton(self):
        global swOpen
        self.window = SmartGridWindow(self)
        self.window.showFullScreen()
        swOpen = 1
 @QtCore.pyqtSlot()
 def blackout_start(self):
        global swOpen
        if swOpen == 0:
          self.window = SmartGridWindow(self)
          self.window.showFullScreen()
          self.window.myThread.start()
          self.window.lcdCustomerOut.display(5000)
          swOpen = 1
        else:
          print("ATTEMPT")
          self.window.lcdCustomerOut.display(5000)
          self.window.myThread.start()
          
 @QtCore.pyqtSlot()
 def turnOn1(self):
   self.window.lcdCustomerOut.display(3750)

 @QtCore.pyqtSlot()
 def turnOn2(self):
   self.window.lcdCustomerOut.display(2500)

 @QtCore.pyqtSlot()
 def turnOn3(self):
   self.window.lcdCustomerOut.display(1250)
 

 @QtCore.pyqtSlot(str)
 def bluetoothStart(self, data):
          value = float(data)
          self.lcdRenewable.display(value)
          self.lcdPercentGreen.display(value/50)
          

 def __init__(self, parent=None):
 	super(self.__class__, self).__init__(parent)
 	#self.setGeometry(0, 0, 650, 550)
 	self.setupUi(self) # gets defined in the UI file
 	self.lcdBostonNeed.display(5000)
 	self.lcdRenewable.display(0)
 	self.lcdPercentGreen.display(0)
 	self.SmartGridButton.clicked.connect(self.handleSmartGridButton)
 	self.blackoutObject = blackoutObject(self)
 	self.blackoutObject.blackoutSignal.connect(self.blackout_start)
 	self.blackoutObject.onSignal1.connect(self.turnOn1)
 	self.blackoutObject.onSignal2.connect(self.turnOn2)
 	self.blackoutObject.onSignal3.connect(self.turnOn3)
 	self.blackoutObject.start()
 	self.btObject = btObject(self)
 	self.btObject.btSignal.connect(self.bluetoothStart)
 	self.btObject.start()

# I feel better having one of these
def main():
  # a new app instance
  app = QApplication(sys.argv)
  #screen_resolution = app.desktop().screenGeometry()
  #width, height = screen_resolution.width(), screen_resolution.height()
  form = MainWindow()
  form.showFullScreen()
  # without this, the script exits immediately.
  sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
 main()






