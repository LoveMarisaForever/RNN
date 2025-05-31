import torch

# 检查 CUDA 是否可用
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using CUDA")
else:
    device = torch.device("cpu")
    print("Using CPU")

# 在后续代码中使用 device
# 例如：
# classifier = classifier.to(device)
# dataset.class_weights = dataset.class_weights.to(device)