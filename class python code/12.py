import torch
import torch.nn as nn
import torch.optim as optim

# 一个简单的前馈神经网络模型
class SimpleModel(nn.Module):
    # 初始化模型的层
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # 第一层全连接层
        self.fc2 = nn.Linear(5, 1)    # 第二层全连接层

    # 定义模型的前向传播过程
    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 在第一层后应用ReLU激活函数
        x = self.fc2(x)               # 从第二层输出
        return x

# 实例化模型
model = SimpleModel()

# 生成随机的输入数据
input_data = torch.randn(1, 10)  # 创建一个大小为(1, 10)的随机输入

# 将输入数据传递给模型
output = model(input_data)

# 打印输出结果
print(output)
