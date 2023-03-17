import torch
from torch import nn
X = torch.rand(size=(2,4))
class net(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(4, 8),nn.ReLU(),nn.Linear(8, 2))
        self.linear = nn.Linear(32, 16)
    def forword(self, X):
        return self.net(X)
net_ = net()
print(net_.forword(X))
print(net_)
