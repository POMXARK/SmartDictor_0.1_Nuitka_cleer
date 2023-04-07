import os
import json
import cv2
import numpy as np
import win32gui
from PyQt5.QtWidgets import QFileDialog
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
# https://github.com/kivy/plyer/blob/master/examples/filechooser/main.py
from plyer import filechooser
import shutil

Window.minimum_height = 400
Window.minimum_width = 400


class Container(BoxLayout):
    original_img = None
    cv2_params = {'h1': 0, 's1': 0, 'v1': 0, 'h2': 0, 's2': 0, 'v2': 0}
    cv2_img = 'hsv.png'
    result_img = None
    h_min = None
    h_max = None
    hsv_image = None

    def touch(self, val: str = 'h1: 0'):
        """ Отслеживание показателей слайдера"""
        slider_name, value = val[0:2], val[3::]
        self.cv2_params[slider_name] = int(value)

        # формируем начальный и конечный цвет фильтра
        h_min = np.array((self.cv2_params['h1'], self.cv2_params['s1'], self.cv2_params['v1']), np.uint8)
        h_max = np.array((self.cv2_params['h2'], self.cv2_params['s2'], self.cv2_params['v2']), np.uint8)

        try:
            self.hsv_image = cv2.imread(self.original_img)
            self.result_img = cv2.cvtColor(self.hsv_image, cv2.COLOR_BGR2HSV)  # преобразовать для inRange
            self.result_img = cv2.inRange(self.result_img, h_min, h_max)
            #cv2.imshow('image', self.result_img) # тестовое окно просмотра
            cv2.imwrite(self.cv2_img, self.result_img)  # записать результат в картинку
            self.ids.image_wrapper.source = self.cv2_img
            self.ids.image_wrapper.reload()
        except Exception as e:
            print(e)

    def open_file(self):
        """Открыть диалог открытия файла"""
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        """Вставить изображение"""
        if selection:
            self.original_img = selection[0]
            self.touch()

    def save_file(self):
        # save_path = win32gui.GetSaveFileNameW(File='file_name')[0]
        try:
            save_path = filechooser.save_file()[0]
            with open(save_path, 'w') as file:
                file.write('{ "cv2_params" : ' + str(list(self.cv2_params.items()))
                                      .replace("(", "[").replace(")", "]").replace("'", '"') + "}")
            print(json.load(open(save_path)))
        except Exception as e:
            print(e)


class MyApp(App):

    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()





