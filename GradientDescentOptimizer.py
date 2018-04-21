
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# build data
points_num  = 100
vectors=[]

# 用Numpy的状态随机分布函数生成100个点
for i in range(points_num):
    x1=np.random.normal(0.0,0.66)
    y1=x1*0.1+0.2+np.random.normal(0,0.06)
    vectors.append([x1,y1])

# true x position
x_data=[v[0] for v in vectors]
y_data=[v[1] for v in vectors]

# 图像 1：展示所有（100个）的随机数据
plt.plot(x_data,y_data,'r*',label='Original data')
plt.title('Linear Regression using Gradient Descent')
plt.legend()
plt.show()

# 构建线性回归模型
W=tf.Variable(tf.random_uniform([1],-1.0,1.0)) # 初始化weight
b=tf.Variable(tf.zeros([1])) # 初始化 Bias
y=W*x_data+b              # 模型计算出来的 y

# 定义 loss function (损失函数) or cost function (代价函数)
# 对 Tensor 的所有维度计算 （y-y_data)^2之和 除以 数据数量 100

loss = tf.reduce_mean(tf.square(y-y_data))

# 梯度下降的优化器来优化我们的 loss function ()
optimizer = tf.train.GradientDescentOptimizer(0.5) # 设置学习率 0.5
train = optimizer.minimize(loss) # 最小化损失函数

# 创建会话
sess = tf.Session()

# 初始化数据流图中的所有变量
init = tf.global_variables_initializer()
sess.run(init)

# 训练
for step in range(20):
    # 优化每一步
    sess.run(train)
    # 打印出每一步的损失，权重和偏差
    print("Step=%d,Loss=%f,[Weight=%f Bias=%f]" % (step,sess.run(loss),sess.run(W),sess.run(b)))

# 图像 2 ： 绘制所有的点并且绘制出的到的最佳拟合的曲线
plt.plot(x_data,y_data,'r*',label='Original data')
plt.title('Linear Regression using Gradient Descent')
plt.plot(x_data,sess.run(W)*x_data+sess.run(b),label='Fitted line') # 拟合的线段
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 关闭会话
sess.close()

