import numpy as np
import matplotlib.pyplot as plt


x = [1 , 2 , 3]
y = [2 , 4 , 6]

def forward(w , x):
    return w * x

def loss(w , x , y):
    y_pred = w * x

    return (y_pred - y) ** 2


w_list = []
loss_list = []
for w in np.arange(0 , 4.1 , 0.1):

    loss_sum = 0
    w_list.append(w)

    for _x , _y  in zip(x , y):
        loss_sum += loss(w , _x , _y)

    loss_list.append(loss_sum / len(x))

plt.plot(w_list , loss_list)
plt.ylabel('loss')
plt.xlabel('w')
plt.show()