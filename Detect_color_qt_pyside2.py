# -*- coding: utf-8 -*-

# Реализация формы сгенерирована при чтении файла пользовательского интерфейса 'process.ui'
#
# Создано: PyQt5 UI code generator 5.11.3
#
# ПРЕДУПРЕЖДЕНИЕ! Все изменения, внесенные в этот файл, будут потеряны!
#
# Подпишитесь на канал PyShine Youtube, чтобы узнать подробности!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import numpy as np

#global height_img, width_img

class Ui_MainWindow(object):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.height_img = 110
        self.width_img = 110


    #print(object.__dict__)

    def setupUi(self, MainWindow):





        global height_img, width_img

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 571) # размеры окна

        self.centralwidget = QtWidgets.QWidget(MainWindow) # присвоить класс главного окна
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        #size_QtWidget= QtWidgets.QWidget
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3 = QtWidgets.QWidget
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")




        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setStyleSheet("border: 10px solid green;")
        self.label.resize(10, 10)
        # self.label.setPixmap(QtGui.QPixmap("images/2.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()


       # self.horizontalLayout_4 = QtWidgets.QHBoxLayout()  #
       # self.horizontalLayout_4.setObjectName("horizontalLayout_4")
       # self.label1 = QtWidgets.QLabel(self.centralwidget)
       # self.label.setText("")
        ## self.label.setPixmap(QtGui.QPixmap("images/2.jpg"))
       # self.label.setObjectName("label")
       # self.horizontalLayout_3.addWidget(self.label)
        #self.horizontalLayout = QtWidgets.QHBoxLayout()
       # self.horizontalLayout_4.addWidget(self.label)

       # self.horizontalLayout.setObjectName("horizontalLayout")
        #self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        #self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        #self.verticalSlider.setObjectName("verticalSlider")
        #self.horizontalLayout.addWidget(self.verticalSlider)

        self.verticalSlider_1 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_1.setObjectName("verticalSlider_1") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_1) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута


        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_2.setObjectName("verticalSlider_2") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_2) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута


        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_3.setObjectName("verticalSlider_3") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_3) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут *добавить ещё надо
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута и позиционирование


        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_4.setObjectName("verticalSlider_4") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_4) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут *добавить ещё надо
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута и позиционирование


        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_5.setObjectName("verticalSlider_5") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_5) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут *добавить ещё надо
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута и позиционирование


        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_6.setObjectName("verticalSlider_6") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_6) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут *добавить ещё надо
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута и позиционирование




        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
#        self.verticalSlider.setRange(0, 255)  # дипазон значений слайдера
#        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)

        self.verticalSlider_1.setRange(0, 255)  # дипазон значений слайдера
        self.verticalSlider_1.setValue(0)
        self.verticalSlider_1.valueChanged['int'].connect(self.h1) # передает значение value в функцию

        self.verticalSlider_2.setRange(0, 255)  # дипазон значений слайдера
        self.verticalSlider_2.setValue(0)
        self.verticalSlider_2.valueChanged['int'].connect(self.s1) # передает значение value в функцию

        self.verticalSlider_3.setRange(0, 255)  # дипазон значений слайдера
        self.verticalSlider_3.setValue(0)
        self.verticalSlider_3.valueChanged['int'].connect(self.v1) # передает значение value в функцию

        self.verticalSlider_4.setRange(0, 255)  # дипазон значений слайдера
        self.verticalSlider_4.setValue(0)
        self.verticalSlider_4.valueChanged['int'].connect(self.h2) # передает значение value в функцию


        self.verticalSlider_5.setRange(0, 255)  # дипазон значений слайдера
        self.verticalSlider_5.setValue(0)
        self.verticalSlider_5.valueChanged['int'].connect(self.s2) # передает значение value в функцию

        self.verticalSlider_6.setRange(0, 255)  # дипазон значений слайдера
        self.verticalSlider_6.setValue(0)
        self.verticalSlider_6.valueChanged['int'].connect(self.v2) # передает значение value в функци


        #self.verticalSlider_2.valueChanged['int'].connect(self.blur_value) # 4 - отдает значение из изменяет obj.valueChanged, в функцию , значение ( вызов функции)
        self.pushButton_2.clicked.connect(self.loadImage)
        self.pushButton.clicked.connect(self.savePhoto)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Добавлен код сюда
        self.filename = None  # Будет содержать адрес изображения
        self.tmp = None  # Будет удерживать временное изображение для отображения
        self.brightness_value_now = 0  # Обновлено значение яркости
        self.blur_value_now = 0  # Обновлено значение размытия


        # надпись
        self.verticalLabel1 = QtWidgets.QLabel(self.centralwidget) # создать ЭкземплярКласса QLabel
        self.verticalLabel1.setText("0")# задать текст
       # self.verticalLabel.setOrientation(QtCore.Qt.Vertical)  # QLabel не имеет орентацию
        self.verticalLabel1.setObjectName("verticalLabel1")  # добавить слайдер ( задать имя )
        self.horizontalLayout_3.addWidget(self.verticalLabel1) # при добавлении надписи нужно указывать лайаут

        # надпись
        self.verticalLabel2 = QtWidgets.QLabel(self.centralwidget)  # создать ЭкземплярКласса QLabel
        self.verticalLabel2.setText("0")  # задать текст
        # self.verticalLabel.setOrientation(QtCore.Qt.Vertical)  # QLabel не имеет орентацию
        self.verticalLabel2.setObjectName("verticalLabel2")  # добавить слайдер ( задать имя )
        self.horizontalLayout_3.addWidget(self.verticalLabel2)  # при добавлении надписи нужно указывать лайаут


        # надпись
        self.verticalLabel3 = QtWidgets.QLabel(self.centralwidget)  # создать ЭкземплярКласса QLabel
        self.verticalLabel3.setText("0")  # задать текст
        # self.verticalLabel.setOrientation(QtCore.Qt.Vertical)  # QLabel не имеет орентацию
        self.verticalLabel3.setObjectName("verticalLabel3")  # добавить слайдер ( задать имя )
        self.horizontalLayout_3.addWidget(self.verticalLabel3)  # при добавлении надписи нужно указывать лайаут


        # надпись
        self.verticalLabel4 = QtWidgets.QLabel(self.centralwidget)  # создать ЭкземплярКласса QLabel
        self.verticalLabel4.setText("0")  # задать текст
        # self.verticalLabel.setOrientation(QtCore.Qt.Vertical)  # QLabel не имеет орентацию
        self.verticalLabel4.setObjectName("verticalLabel4")  # добавить слайдер ( задать имя )
        self.horizontalLayout_3.addWidget(self.verticalLabel4)  # при добавлении надписи нужно указывать лайаут



        # надпись
        self.verticalLabel5 = QtWidgets.QLabel(self.centralwidget)  # создать ЭкземплярКласса QLabel
        self.verticalLabel5.setText("0")  # задать текст
        # self.verticalLabel.setOrientation(QtCore.Qt.Vertical)  # QLabel не имеет орентацию
        self.verticalLabel3.setObjectName("verticalLabel5")  # добавить слайдер ( задать имя )
        self.horizontalLayout_3.addWidget(self.verticalLabel5)  # при добавлении надписи нужно указывать лайаут


        # надпись
        self.verticalLabel6 = QtWidgets.QLabel(self.centralwidget)  # создать ЭкземплярКласса QLabel
        self.verticalLabel6.setText("0")  # задать текст
        # self.verticalLabel.setOrientation(QtCore.Qt.Vertical)  # QLabel не имеет орентацию
        self.verticalLabel4.setObjectName("verticalLabel6")  # добавить слайдер ( задать имя )
        self.horizontalLayout_3.addWidget(self.verticalLabel6)  # при добавлении надписи нужно указывать лайаут



        #self.verticalLabel('0', self)  # 3 - присваивает изначальное  , задает тип виджета метка базовый класс  QLabel
        #self.verticalLabel.addWidget(self.verticalLabel)  # добавить виджет


        ##self.label = QtWidgets.QLabel(self.centralwidget)
        ##self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("images/2.jpg"))
        ##self.label.setObjectName("label")
        ##self.horizontalLayout_3.addWidget(self.label)




    def loadImage(self):
        """ Эта функция загрузит выбранное пользователем изображение
             и установите для него метку с помощью функции setPhoto
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        self.height_img, self.width_img = self.image.shape[:2]
        #self.loadImage.height_img= height_img
        #self.loadImage.width_img = width_img
        print(self.height_img, self.width_img)
        #print( height_img, width_img)





    def setPhoto(self, image):


        """ Эта функция принимает изображение и изменяет его размер.
             только для отображения и преобразовать его в QImage
             установить на этикетке.
        """
        #self.Timer()
        #print('setPhoto')
        self.tmp = image


        #frame = image
        #image = imutils.resize(image, width=640)
        #frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #cv2.imshow('result', frame)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #№- нужно
        #QtGui.QColor.
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        #print(height_img, width_img)
        #print(dir(self.loadImage))
#        print(self.height_img, self.width_img)
        #открыть hsv
        self.hsv_image = cv2.imread('hsv.png')
        hsv_mask = self.hsv_image
        #print(self.height_img, self.width_img)
        #test = 300
        #height_img, width_img = self.image.shape[:2]
        #hsv_mask  = imutils.resize(hsv_mask, width=1280) - вызывает глюки
        #hsv_mask = cv2.cvtColor(hsv_mask, cv2.COLOR_BGR2RGB) - ошибка
        hsv_mask = QImage(hsv_mask , hsv_mask.shape[1], hsv_mask.shape[0], hsv_mask.strides[0],QImage.Format_RGB888) #QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(hsv_mask))


    """
    def brightness_value(self, value):
        "" Эта функция будет принимать значение от ползунка
             для яркости от 0 до 99
        ""

        self.brightness_value_now = value
        print('Brightness: ', value)
        self.update()
    """
    def blur_value(self, value):
        """ Эта функция будет принимать значение от ползунка
             для размытия от 0 до 99 """
        # value принимает готовое значение слайдера
        self.verticalLabel.setText(str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.blur_value_now = value
        print('Blur: ', value)
        self.update() # вызов обновления экрана

    def changeBrightness(self, img, value):
        """ Эта функция принимает изображение (img) и яркость
             ценить. Он выполнит изменение яркости с помощью OpenCv
             и после разделения объединит img и вернет его.
        """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_BGR2HSV)
        #img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def changeBlur(self, img, value):
        """ Эта функция принимает в качестве входных данных изображение img и значения размытия.
             После выполнения операции размытия с использованием функции opencv он возвращает
             изображение img.
        """
       # print(value)
        kernel_size = (value + 1, value + 1)  # +1 is to avoid 0
        img = cv2.blur(img, kernel_size)
        return img


    def h1(self, value=0):
        self.verticalLabel1.setText("h1 :" + str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.hsv_h1 = value
        #print(self.hsv_h1)
        self.update()  # вызов обновления экрана

    def s1(self, value=0):
        self.verticalLabel2.setText("s1 :" + str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.hsv_s1 = value
       # print(self.hsv_s1)
        self.update()  # вызов обновления экрана

    def v1(self, value=0):
        self.verticalLabel3.setText("v1 :" + str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.hsv_v1 = value
       # print(self.hsv_v1)
        self.update()  # вызов обновления экрана

    def h2(self, value=255):
        self.verticalLabel4.setText("h2 :" + str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.hsv_h2 = value
        self.update()  # вызов обновления экрана
       # print(self.hsv_h2)


    def s2(self, value=255):
        self.verticalLabel5.setText("s2 :" + str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.hsv_s2 = value
        #print(self.hsv_s2)
        self.update()  # вызов обновления экрана

    def v2(self, value=255):
        self.verticalLabel6.setText("v2 :" + str(value))  # 2 - изменяет значение ползунка изменяет текст надписи
        self.hsv_v2 = value
        #print(self.hsv_v2)
        self.update()  # вызов обновления экрана


    def update(self):
        #print(self.img.__dict__)
        #hsv = cv2.cvtColor(self.tmp, cv2.COLOR_BGR2HSV)
        try:
            h_min = np.array((self.hsv_h1, self.hsv_s1, self.hsv_v1), np.uint8)
        except AttributeError:
            self.hsv_h1 = 0
            self.hsv_s1 = 0
            self.hsv_v1 = 0
            self.hsv_h2 = 0
            self.hsv_s2 = 0
            self.hsv_v2 = 0
        """ Эта функция обновит фото в соответствии с
             текущие значения размытия и яркости и установите для фото метки.
             пременит маску hsv
        """
        #print("hsv_h1" ,self.hsv_h1)
        #print("hsv_s1", self.hsv_s1)
        #print("hsv_v1", self.hsv_v1)

        #print("hsv_h2" ,self.hsv_h2)
        #print("hsv_s2", self.hsv_s2)
        #print("hsv_v2", self.hsv_v2)

        # формируем начальный и конечный цвет фильтра
        self.h_min = np.array((self.hsv_h1, self.hsv_s1, self.hsv_v1), np.uint8)
        self.h_max = np.array((self.hsv_h2, self.hsv_s2, self.hsv_v2), np.uint8)
       # print(self.h_min,self.h_max)
        #h_max = np.array((self.hsv_h2, self.hsv_s2, self.hsv_v2), np.uint8)

        # накладываем фильтр на кадр в модели HSV
        hsv_image = self.tmp
        thresh = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV) # преобразовать для inRange
        thresh = cv2.inRange(thresh, self.h_min, self.h_max)
        #thresh_img = cv2.inRange(self.tmp, (0, 160, 100), (255, 255, 255))
        cv2.imwrite('hsv.png', thresh) # записать результат в картинку
        #self.tmp = cv2.imread('hsv.png') # открыть картинку
        #hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        #final_hsv = hsv
        #img = cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)

        self.setPhoto(self.image)


        #rgbimg = cv2.cvtColor(thresh, cv2.COLOR_HSV2RGB)
        #self.setPhoto(rgbimg )

        #img = self.changeBrightness(self.image, self.brightness_value_now)
        #img = self.changeBlur(img, self.blur_value_now)
        #self.setPhoto(img)

    def savePhoto(self):
        """Эта функция сохранит изображение"""
        # здесь укажите имя выходного файла
        # допустим, мы хотим сохранить вывод как отметку времени
        # раскомментируйте две строки ниже

        # время импорта
        # filename = 'Snapshot' + str (time.strftime ("% Y-% b-% d at% H.% M.% S% p")) + '. png'

        # Или мы можем дать любое имя, например output.jpg или output.png
        # filename = 'Snapshot.png'

        # Или гораздо лучший вариант - позволить пользователю определять местоположение и расширение
        # используя файловый диалог.

        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]

        cv2.imwrite(filename, self.tmp)
        print('Изображение сохранено как:', self.filename)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyshine photo editor"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton.setText(_translate("MainWindow", "Save"))


# Подпишитесь на канал PyShine Youtube, чтобы узнать подробности!

# САЙТ: www.pyshine.com


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
