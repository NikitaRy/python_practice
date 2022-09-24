#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #библиотека для математики
import numpy #чисто для массива
import matplotlib.pyplot as mpp #графики

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1) #график
    mpp.plot(
        arguments,
        [math.cos(a) * math.sin(math.sin(a**2/20.0)) for a in arguments] #функция
    )
    mpp.show() #показываем
