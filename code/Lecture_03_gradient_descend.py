import matplotlib.pyplot as plt

x = [1 , 2 , 3]
y = [2 , 4 , 6]

def forward(w , x):
    return w * x

def cost(w , x_s , y_s):
    cost = 0
    for _x , _y in zip(x,y):
        y_pred = forward(w , _x)
        cost += (y_pred - _y) ** 2
    
    return cost / len(x_s)

def gradient(w , x_s , y_s):
    
    grad = 0
    for _x , _y in zip(x,y):
        grad += 2 * _x * (w * _x - _y)
    
    grad /= len(x_s)
    return grad

w = 0
a = 0.1 # 学习率

for epoch in range(0 , 100):
    
    cost_val = cost(w , x , y)
    grad = gradient(w , x , y)
    w -= a * grad


print('w = ' , w)
