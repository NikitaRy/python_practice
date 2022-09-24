#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #����������� ���������� ��� ������ -- ������ �� �� ����� from math import sin ))
import numpy #������ ��� ���������� ��� ������� -- ������ ��� �� ����� ������� ��� ������� ��������?
import matplotlib.pyplot as mpp #��� ��������

# ��� ��������� ������ ������ �������, �������� ���������� ����

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1) #������
    mpp.plot(
        arguments,
        [math.cos(a) * math.sin(math.sin(a**2/20.0)) for a in arguments] #������ ������
    )
    mpp.show() #����������
