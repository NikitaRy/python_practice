#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # библиотека для математики
import numpy  # тулза для серьезной математики ;)
import matplotlib.pyplot as mpp  # либа для построения графика

if __name__ == '__main__':  # запускаем программу
    arguments = numpy.arange(0, 200, 0.1)  # массив для графика
    mpp.plot(
        arguments,
        [math.cos(a) * math.sin(math.sin(a**2/20.0)) for a in arguments]  # график функции внутри
    )
    mpp.show()  # показываем график
