# -*- coding: utf-8 -*-

# www.pyshine.com
# Реализация формы сгенерирована при чтении файла пользовательского интерфейса 'process.ui'
# PyShine Youtube

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog

global height_img, width_img

class UiMainWindow(object):
    """Программа для определения параметров маски OpenCV на изображении"""

    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.verticalLabel = None
        self.hsv_image = None
        self.image = None
        self.vertical_label_6 = None
        self.vertical_label_5 = None
        self.vertical_label_4 = None
        self.vertical_label_3 = None
        self.vertical_label_2 = None
        self.vertical_label_1 = None
        self.blur_value_now = None
        self.brightness_value_now = None
        self.tmp = None
        self.filename = None
        self.statusbar = None
        self.push_button = None
        self.push_button_2 = None
        self.horizontal_layout_2 = None
        self.vertical_slider_6 = None
        self.vertical_slider_5 = None
        self.vertical_slider_4 = None
        self.vertical_slider_3 = None
        self.vertical_slider_2 = None
        self.vertical_slider_1 = None
        self.horizontal_layout = None
        self.label = None
        self.horizontal_layout_3 = None
        self.grid_layout = None
        self.grid_layout_2 = None
        self.central_widget = None
        self.height_img = 110
        self.width_img = 110

    def setup_ui(self, main_window):

        main_window.setObjectName("MainWindow")
        main_window.resize(536, 571)  # размеры окна

        self.central_widget = QtWidgets.QWidget(main_window)  # присвоить класс главного окна
        self.central_widget.setObjectName("central_widget")
        self.grid_layout_2 = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setText("")
        self.label.setStyleSheet("border: 10px solid green;")
        self.label.resize(10, 10)
        self.label.setObjectName("label")
        self.horizontal_layout_3.addWidget(self.label)
        self.horizontal_layout = QtWidgets.QHBoxLayout()

        self.vertical_slider_1 = QtWidgets.QSlider(self.central_widget)  # слайдер
        self.vertical_slider_1.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
        self.vertical_slider_1.setObjectName("vertical_slider_1")  # добавить слайдер
        self.horizontal_layout.addWidget(self.vertical_slider_1)  # добавить виджет
        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить лай аут
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление лай аута

        self.vertical_slider_2 = QtWidgets.QSlider(self.central_widget)  # слайдер
        self.vertical_slider_2.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
        self.vertical_slider_2.setObjectName("vertical_slider_2")  # добавить слайдер
        self.horizontal_layout.addWidget(self.vertical_slider_2)  # добавить виджет
        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить лай аут
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление лай аута

        self.vertical_slider_3 = QtWidgets.QSlider(self.central_widget)  # слайдер
        self.vertical_slider_3.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
        self.vertical_slider_3.setObjectName("vertical_slider_3")  # добавить слайдер
        self.horizontal_layout.addWidget(self.vertical_slider_3)  # добавить виджет
        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить лай аут *добавить ещё надо
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление лай аута и позиционирование

        self.vertical_slider_4 = QtWidgets.QSlider(self.central_widget)  # слайдер
        self.vertical_slider_4.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
        self.vertical_slider_4.setObjectName("vertical_slider_4")  # добавить слайдер
        self.horizontal_layout.addWidget(self.vertical_slider_4)  # добавить виджет
        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить лай аут *добавить ещё надо
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление лай аута и позиционирование

        self.vertical_slider_5 = QtWidgets.QSlider(self.central_widget)  # слайдер
        self.vertical_slider_5.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
        self.vertical_slider_5.setObjectName("vertical_slider_5")  # добавить слайдер
        self.horizontal_layout.addWidget(self.vertical_slider_5)  # добавить виджет
        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить лай аут *добавить ещё надо
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление лай аута и позиционирование

        self.vertical_slider_6 = QtWidgets.QSlider(self.central_widget)  # слайдер
        self.vertical_slider_6.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
        self.vertical_slider_6.setObjectName("vertical_slider_6")  # добавить слайдер
        self.horizontal_layout.addWidget(self.vertical_slider_6)  # добавить виджет
        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить лай аут *добавить ещё надо
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление лай аута и позиционирование

        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.push_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_2.setObjectName("push_button_2")
        self.horizontal_layout_2.addWidget(self.push_button_2)
        self.push_button = QtWidgets.QPushButton(self.central_widget)
        self.push_button.setObjectName("push_button")
        self.horizontal_layout_2.addWidget(self.push_button)
        self.grid_layout.addLayout(self.horizontal_layout_2, 1, 0, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 1, 1, 1, 1)
        self.grid_layout_2.addLayout(self.grid_layout, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslation_ui(main_window)

        self.vertical_slider_1.setRange(0, 255)  # дипазон значений слайдера
        self.vertical_slider_1.setValue(0)
        self.vertical_slider_1.valueChanged['int'].connect(self.h1)  # передает значение value в функцию

        self.vertical_slider_2.setRange(0, 255)  # диапазон значений слайдера
        self.vertical_slider_2.setValue(0)
        self.vertical_slider_2.valueChanged['int'].connect(self.s1)  # передает значение value в функцию

        self.vertical_slider_3.setRange(0, 255)  # диапазон значений слайдера
        self.vertical_slider_3.setValue(0)
        self.vertical_slider_3.valueChanged['int'].connect(self.v1)  # передает значение value в функцию

        self.vertical_slider_4.setRange(0, 255)  # дипазон значений слайдера
        self.vertical_slider_4.setValue(0)
        self.vertical_slider_4.valueChanged['int'].connect(self.h2)  # передает значение value в функцию

        self.vertical_slider_5.setRange(0, 255)  # диапазон значений слайдера
        self.vertical_slider_5.setValue(0)
        self.vertical_slider_5.valueChanged['int'].connect(self.s2)  # передает значение value в функцию

        self.vertical_slider_6.setRange(0, 255)  # диапазон значений слайдера
        self.vertical_slider_6.setValue(0)
        self.vertical_slider_6.valueChanged['int'].connect(self.v2)  # передает значение value в функцию

        self.push_button_2.clicked.connect(self.load_image)
        self.push_button.clicked.connect(self.savePhoto)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # Добавлен код сюда
        self.filename = None  # Будет содержать адрес изображения
        self.tmp = None  # Будет удерживать временное изображение для отображения
        self.brightness_value_now = 0  # Обновлено значение яркости
        self.blur_value_now = 0  # Обновлено значение размытия

        # надпись
        self.vertical_label_1 = QtWidgets.QLabel(self.central_widget)  # создать ЭкземплярКласса QLabel
        self.vertical_label_1.setText("0")  # задать текст

        self.vertical_label_1.setObjectName("vertical_label_1")  # добавить слайдер (задать имя )
        self.horizontal_layout_3.addWidget(self.vertical_label_1)  # при добавлении надписи нужно указывать лайаут

        # надпись
        self.vertical_label_2 = QtWidgets.QLabel(self.central_widget)  # создать ЭкземплярКласса QLabel
        self.vertical_label_2.setText("0")  # задать текст

        self.vertical_label_2.setObjectName("vertical_label_2")  # добавить слайдер (задать имя )
        self.horizontal_layout_3.addWidget(self.vertical_label_2)  # при добавлении надписи нужно указывать лайаут

        # надпись
        self.vertical_label_3 = QtWidgets.QLabel(self.central_widget)  # создать ЭкземплярКласса QLabel
        self.vertical_label_3.setText("0")  # задать текст

        self.vertical_label_3.setObjectName("vertical_label_3")  # добавить слайдер (задать имя )
        self.horizontal_layout_3.addWidget(self.vertical_label_3)  # при добавлении надписи нужно указывать лайаут

        # надпись
        self.vertical_label_4 = QtWidgets.QLabel(self.central_widget)  # создать ЭкземплярКласса QLabel
        self.vertical_label_4.setText("0")  # задать текст

        self.vertical_label_4.setObjectName("vertical_label_4")  # добавить слайдер (задать имя )
        self.horizontal_layout_3.addWidget(self.vertical_label_4)  # при добавлении надписи нужно указывать лайаут

        # надпись
        self.vertical_label_5 = QtWidgets.QLabel(self.central_widget)  # создать ЭкземплярКласса QLabel
        self.vertical_label_5.setText("0")  # задать текст

        self.vertical_label_3.setObjectName("vertical_label_5")  # добавить слайдер (задать имя )
        self.horizontal_layout_3.addWidget(self.vertical_label_5)  # при добавлении надписи нужно указывать лайаут

        # надпись
        self.vertical_label_6 = QtWidgets.QLabel(self.central_widget)  # создать ЭкземплярКласса QLabel
        self.vertical_label_6.setText("0")  # задать текст

        self.vertical_label_4.setObjectName("vertical_label_6")  # добавить слайдер (задать имя )
        self.horizontal_layout_3.addWidget(self.vertical_label_6)  # при добавлении надписи нужно указывать лайаут

    def load_image(self):
        """ Эта функция загрузит выбранное пользователем изображение
             и установите для него метку с помощью функции setPhoto
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.set_photo(self.image)
        self.height_img, self.width_img = self.image.shape[:2]

    def set_photo(self, image):

        """ Эта функция принимает изображение и изменяет его размер.
             Только для отображения и преобразовать его в QImage
             установить на этикетке.
        """
        self.tmp = image

        # открыть hsv
        self.hsv_image = cv2.imread('hsv.png')
        hsv_mask = self.hsv_image

        hsv_mask = QImage(hsv_mask, hsv_mask.shape[1], hsv_mask.shape[0], hsv_mask.strides[0],
                          QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(hsv_mask))

    def blur_value(self, value):
        """ Эта функция будет принимать значение от ползунка
             для размытия от 0 до 99 """
        # value принимает готовое значение слайдера
        self.verticalLabel.setText(str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.blur_value_now = value
        print('Blur: ', value)
        self.update()  # вызов обновления экрана

    @staticmethod
    def change_brightness(img, value):
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

        return img

    @staticmethod
    def change_blur(img, value):
        """ Эта функция принимает в качестве входных данных изображение img и значения размытия.
             После выполнения операции размытия с использованием функции opencv он возвращает
             изображение img.
        """
        kernel_size = (value + 1, value + 1)  # +1 is to avoid 0
        img = cv2.blur(img, kernel_size)
        return img

    def h1(self, value=0):
        self.vertical_label_1.setText("h1 :" + str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.hsv_h1 = value
        self.update()  # вызов обновления экрана

    def s1(self, value=0):
        self.vertical_label_2.setText("s1 :" + str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.hsv_s1 = value
        self.update()  # вызов обновления экрана

    def v1(self, value=0):
        self.vertical_label_3.setText("v1 :" + str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.hsv_v1 = value
        self.update()  # вызов обновления экрана

    def h2(self, value=255):
        self.vertical_label_4.setText("h2 :" + str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.hsv_h2 = value
        self.update()  # вызов обновления экрана

    def s2(self, value=255):
        self.vertical_label_5.setText("s2 :" + str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.hsv_s2 = value
        self.update()  # вызов обновления экрана

    def v2(self, value=255):
        self.vertical_label_6.setText("v2 :" + str(value))  # 2 - изменяет значение ползунка, изменяет текст надписи
        self.hsv_v2 = value
        self.update()  # вызов обновления экрана

    def update(self):
        try:
            self.h_min = np.array((self.hsv_h1, self.hsv_s1, self.hsv_v1), np.uint8)
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
        # формируем начальный и конечный цвет фильтра
        self.h_min = np.array((self.hsv_h1, self.hsv_s1, self.hsv_v1), np.uint8)
        self.h_max = np.array((self.hsv_h2, self.hsv_s2, self.hsv_v2), np.uint8)

        # накладываем фильтр на кадр в модели HSV
        hsv_image = self.tmp
        thresh = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)  # преобразовать для inRange
        thresh = cv2.inRange(thresh, self.h_min, self.h_max)

        cv2.imwrite('hsv.png', thresh)  # записать результат в картинку

        self.set_photo(self.image)

    def savePhoto(self):
        """Эта функция сохранит изображение"""
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        cv2.imwrite(filename, self.tmp)
        print('Изображение сохранено как:', self.filename)

    def retranslation_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Pyshine photo editor"))
        self.push_button_2.setText(_translate("main_window", "Open"))
        self.push_button.setText(_translate("main_window", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
