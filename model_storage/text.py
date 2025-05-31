import torch

# 检查 CUDA 是否可用
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using CUDA")
else:
    device = torch.device("cpu")
    print("Using CPU")


print(torch.cuda.is_available())  # 应输出True
print(torch.cuda.device_count())   # 应输出GPU数量（至少1）
print(torch.cuda.get_device_name(0))  # 显示GPU名称
