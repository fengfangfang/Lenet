#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import cPickle  
import gzip  
import numpy as np  
import matplotlib.pyplot as plt  
f = gzip.open('mnist.pkl.gz', 'rb')  
train_set, valid_set, test_set = cPickle.load(f)  
f.close()  
tx,ty=train_set;  
  
#查看训练样本  
print np.shape(tx)#可以看到tx大小为（50000,28*28）的二维矩阵  
print np.shape(ty)#可以看到ty大小为（50000,1）的矩阵  
#图片显示  
A=tx[8].reshape(28,28)#第八个训练样本  
Y=ty[8]  
print Y  
plt.imshow(A,cmap='gray')#显示手写字体图片</span>  
#plt.show()