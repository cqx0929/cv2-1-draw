#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :cv2-1-draw.py
# @Time      :2023/9/26 21:54
# @Author    :CQX0929
import cv2
import numpy as np


class Drawer(object):
    def __init__(self):
        self.h, self.w, self.channel = 1000, 1000, 3
        self.center = np.asarray((self.h / 2, self.w / 2), int)
        self.matrix_shape = (self.h, self.w, self.channel)
        self.bgr_matrix = np.ones(shape=self.matrix_shape)
        self.color_b = np.array((0, 0, 0)) / 255
        self.color_bfhl = np.array((78, 24, 146)[::-1]) / 255  # 柏坊灰藍 rgb
        self.points = []
        self.init_phase = 6 * np.pi
        self.times = 20
        self.edges = 6

    def __draw_polygon(self, points: np.array):
        for i in range(len(points)-1):
            pt1, pt2 = points[i], points[i+1]
            self.__line(pt1, pt2)

    def __draw_regular_polygon(self, edges: int, initial_phase: float, circum_radius: int):
        points = np.linspace(0, 2*np.pi, edges+1)+initial_phase
        x, y = (np.asarray(np.cos(points)*circum_radius+self.center[0], int),
                np.asarray(np.sin(points)*circum_radius+self.center[1], int))
        points = np.column_stack((x, y))
        self.__draw_polygon(points)

    def __line(self, pt1: np.array, pt2: np.array):
        cv2.line(self.bgr_matrix, pt1, pt2, self.color_bfhl, 1, 0, 0)

    def __show(self):
        cv2.imshow('img', self.bgr_matrix)
        if cv2.waitKey(1) > 0:
            cv2.destroyAllWindows()

    def main(self):
        n = self.times
        edges = self.edges
        for i in range(n):
            self.__draw_regular_polygon(edges,
                                        self.init_phase / n * i,
                                        int(i * self.h / n / 2))
            self.__show()
        if cv2.waitKey(0) > 0:
            cv2.destroyAllWindows()

        cv2.imwrite('img.jpg', np.asarray(self.bgr_matrix*255, dtype=int), [cv2.IMWRITE_JPEG_QUALITY, 100])


if __name__ == "__main__":
    gd = Drawer()
    gd.main()
