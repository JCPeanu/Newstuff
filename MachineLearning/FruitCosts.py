import numpy as np
import torch

inputs = np.array([[2, 4, 5, 5, 0], 
                   [0, 2, 7, 3, 3], 
                   [6, 3, 1, 7, 1], 
                   [3, 0, 6, 1, 4], 
                   [5, 5, 3, 8, 2]], dtype='float32')

target = np.array([ [627],
                    [870],
                    [587],
                    [853],
                    [857]], dtype = 'float32')

inputs = torch.from_numpy(inputs)
target = torch.from_numpy(target)

w = torch.randn(1, 5, requires_grad=True)

def model(x):
    return x @ w.t()

def mse(t1, t2):
    diff = t1 - t2
    return torch.sum(diff * diff) / diff.numel()

preds = model(inputs)
loss = mse(preds, target)
loss.backward()
for i in range(100000):
    preds = model(inputs)
    loss = mse(preds, target)
    loss.backward()
    with torch.no_grad():
        w -= w.grad * 1e-3
        w.grad.zero_()

preds = model(inputs)
loss = mse(preds, target)
print(w)
print(preds)
print(loss)
for i in w[0]:
    print(round(i.item()))

