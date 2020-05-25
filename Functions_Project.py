#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv
import numpy as np


# In[ ]:


def getimgbalance(img):
    rows,cols = img.shape
    total = 0
    for i in range(rows):
        for j in range(cols):
            total += img[i,j]
    prom = total/(rows*cols)
    return prom


# In[ ]:


def dinamicpow(img):
    val = getimgbalance(img)
    THR = 150
    gamma = val/THR
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') 
    return gamma_corrected

