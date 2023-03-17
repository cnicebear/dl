# matplotlib inline
import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l

def synthetic_data(w, b, num_examples):
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))
true_w = torch.tensor([2, -3.4])
true_b = 4.2
# features, labels = d2l.synthetic_data(true_w, true_b, 1000)
# print('features:', features[0], '\nlabel:', labels[0])
features, labels = d2l.synthetic_data(true_w, true_b, 10)
# print(features, labels)
# x = torch.zeros((2, 3, 4))
# print(x)
# print(x.shape)
# print(x.numel())
y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

x = torch.arange(12, dtype=torch.float32).reshape((3,4))
print(torch.cat((x, y), dim=0), torch.cat((x, y), dim=1))