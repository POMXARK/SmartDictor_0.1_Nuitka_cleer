# -*- coding: utf-8 -*-

# www.pyshine.com
# Реализация формы сгенерирована при чтении файла пользовательского интерфейса 'process.ui'
# PyShine Youtube

import sys
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
        self.tmp = None
        self.filename = None
        self.push_button = None
        self.push_button_2 = None
        self.horizontal_layout_2 = None
        self.horizontal_layout = None
        self.img = None
        self.horizontal_layout_3 = None
        self.grid_layout = None
        self.grid_layout_2 = None
        self.central_widget = None
        self.height_img = 110
        self.width_img = 110

    def setup_ui(self, window):
        window.resize(536, 571)  # размеры окна

        self.central_widget = QtWidgets.QWidget(window)  # присвоить класс главного окна
        self.grid_layout_2 = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout = QtWidgets.QGridLayout()
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.img = QtWidgets.QLabel(self.central_widget)
        self.img.setStyleSheet("border: 1px solid green;")

        self.horizontal_layout_3.addWidget(self.img)
        self.horizontal_layout = QtWidgets.QHBoxLayout()

        for widget in range(1, 6 + 1):
            slider_obj = 'vertical_slider_' + str(widget)  # генерируем имя переменной
            setattr(self, slider_obj, QtWidgets.QSlider(self.central_widget))  # слайдер
            current_slider = getattr(self, slider_obj)
            self.horizontal_layout.addWidget(current_slider)  # добавить виджет
            current_slider.setOrientation(QtCore.Qt.Vertical)  # ориентация слайдера
            current_slider.setRange(0, 255)  # диапазон значений слайдера
            current_slider.setValue(0)

        self.horizontal_layout_3.addLayout(self.horizontal_layout)  # добавить layout
        self.grid_layout.addLayout(self.horizontal_layout_3, 0, 0, 1, 2)  # добавление layout

        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()

        self.push_button_2 = QtWidgets.QPushButton(self.central_widget)

        self.horizontal_layout_2.addWidget(self.push_button_2)
        self.push_button = QtWidgets.QPushButton(self.central_widget)

        self.horizontal_layout_2.addWidget(self.push_button)
        self.grid_layout.addLayout(self.horizontal_layout_2, 1, 0, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 1, 1, 1, 1)
        self.grid_layout_2.addLayout(self.grid_layout, 0, 0, 1, 1)
        window.setCentralWidget(self.central_widget)

        self.retranslation_ui(window)

        self.push_button_2.clicked.connect(self.load_image)
        self.push_button.clicked.connect(self.save_photo)
        QtCore.QMetaObject.connectSlotsByName(window)

        for widget in range(1, 6 + 1):
            label_obj = 'vertical_label_' + str(widget)  # генерируем имя переменной
            setattr(self, label_obj, QtWidgets.QLabel(self.central_widget))  # создать ЭкземплярКласса QLabel
            current_label = getattr(self, label_obj)
            current_label.setText("0")  # задать текст
            self.horizontal_layout_3.addWidget(current_label)  # при добавлении надписи нужно указывать layout

        self.vertical_slider_1.valueChanged['int'].connect(self.h1)  # передает значение value в функцию
        self.vertical_slider_2.valueChanged['int'].connect(self.s1)  # передает значение value в функцию
        self.vertical_slider_3.valueChanged['int'].connect(self.v1)  # передает значение value в функцию
        self.vertical_slider_4.valueChanged['int'].connect(self.h2)  # передает значение value в функцию
        self.vertical_slider_5.valueChanged['int'].connect(self.s2)  # передает значение value в функцию
        self.vertical_slider_6.valueChanged['int'].connect(self.v2)  # передает значение value в функцию

    def load_image(self):
        """ Эта функция загрузит выбранное пользователем изображение
             и установите для него метку с помощью функции set_photo
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
        hsv_mask_scaled = hsv_mask.scaled(hsv_mask.width() / 1.2, hsv_mask.height() / 1.2)
        self.img.setPixmap(QtGui.QPixmap.fromImage(hsv_mask_scaled))

    # коллекция подключенных методов на изменение
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
        """ Эта функция обновит фото в соответствии с
             текущие значения размытия и яркости и установите для фото метки.
             применит маску hsv
        """
        try:
            self.h_min = np.array((self.hsv_h1, self.hsv_s1, self.hsv_v1), np.uint8)
        except AttributeError:
            self.hsv_h1 = 0
            self.hsv_s1 = 0
            self.hsv_v1 = 0
            self.hsv_h2 = 0
            self.hsv_s2 = 0
            self.hsv_v2 = 0

        # формируем начальный и конечный цвет фильтра
        self.h_min = np.array((self.hsv_h1, self.hsv_s1, self.hsv_v1), np.uint8)
        self.h_max = np.array((self.hsv_h2, self.hsv_s2, self.hsv_v2), np.uint8)

        # накладываем фильтр на кадр в модели HSV
        hsv_image = self.tmp
        thresh = cv2.cvtColor(hsv_image, cv2.COLOR_BGR2HSV)  # преобразовать для inRange
        thresh = cv2.inRange(thresh, self.h_min, self.h_max)

        cv2.imwrite('hsv.png', thresh)  # записать результат в картинку

        self.set_photo(self.image)

    def save_photo(self):
        """Эта функция сохранит изображение. Зачем?"""
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        cv2.imwrite(filename, self.tmp)
        print('Изображение сохранено как:', self.filename)

    def retranslation_ui(self, main_window):
        """Задать название элементам"""
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Pyshine photo editor"))
        self.push_button_2.setText(_translate("main_window", "Open"))
        self.push_button.setText(_translate("main_window", "Save"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
