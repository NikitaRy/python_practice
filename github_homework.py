#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импортируем математику для синуса -- почему бы не юзать from math import sin ))
import numpy #нампай для массивчика для графика -- почему они не могли сделать для обычных структур?
import matplotlib.pyplot as mpp #для графиков

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1) #массив
    mpp.plot(
        arguments,
        [math.cos(a) * math.sin(math.sin(a**2/20.0)) for a in arguments] #строим график
    )
    mpp.show() #показываем
