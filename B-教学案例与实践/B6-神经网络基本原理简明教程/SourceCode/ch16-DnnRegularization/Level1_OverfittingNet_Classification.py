# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import numpy as np
import matplotlib.pyplot as plt

from MiniFramework.NeuralNet41 import *
from MiniFramework.ActivatorLayer import *
from MiniFramework.ClassificationLayer import *
from MnistImageDataReader import *

train_image_file = '../../Data/train-images-10'
train_label_file = '../../Data/train-labels-10'
test_image_file = '../../Data/test-images-10'
test_label_file = '../../Data/test-labels-10'

def LoadData():
    mdr = MnistImageDataReader(train_image_file, train_label_file, test_image_file, test_label_file, "vector")
    mdr.ReadLessData(1000)
    #mdr.ReadData()
    mdr.Normalize()
    mdr.GenerateDevSet(k=10)
    return mdr

def Net(dataReader, num_input, num_hidden, num_output, params, show_history=True):
    net = NeuralNet41(params, "mnist_overfitting")

    fc1 = FcLayer(num_input, num_hidden, params)
    net.add_layer(fc1, "fc1")
    relu1 = ActivatorLayer(Relu())
    net.add_layer(relu1, "relu1")
    
    fc2 = FcLayer(num_hidden, num_hidden, params)
    net.add_layer(fc2, "fc2")
    relu2 = ActivatorLayer(Relu())
    net.add_layer(relu2, "relu2")

    fc3 = FcLayer(num_hidden, num_hidden, params)
    net.add_layer(fc3, "fc3")
    relu3 = ActivatorLayer(Relu())
    net.add_layer(relu3, "relu3")

    fc4 = FcLayer(num_hidden, num_hidden, params)
    net.add_layer(fc4, "fc4")
    relu4 = ActivatorLayer(Relu())
    net.add_layer(relu4, "relu4")
    
    fc5 = FcLayer(num_hidden, num_output, params)
    net.add_layer(fc5, "fc5")
    softmax = ClassificationLayer(Softmax())
    net.add_layer(softmax, "softmax")

    net.train(dataReader, checkpoint=1, need_test=True)
    if show_history:
        net.ShowLossHistory()
    
    return net


if __name__ == '__main__':

    dataReader = LoadData()
    num_feature = dataReader.num_feature
    num_example = dataReader.num_example
    num_input = num_feature
    num_hidden = 30
    num_output = 10
    max_epoch = 200
    batch_size = 100
    learning_rate = 0.1
    eps = 0.08

    params = HyperParameters41(
        learning_rate, max_epoch, batch_size, eps,                        
        net_type=NetType.MultipleClassifier,
        init_method=InitialMethod.Xavier)

    Net(dataReader, num_input, num_hidden, num_output, params)
