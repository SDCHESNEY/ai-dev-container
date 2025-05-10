#Simple program to validate the container

import torch
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("Number of GPUs:", torch.cuda.device_count())
print("Current device:", torch.cuda.current_device())
print("Device name:", torch.cuda.get_device_name(0))
print("Device properties:", torch.cuda.get_device_properties(0))
print("Device count:", torch.cuda.device_count())
print("Current device name:", torch.cuda.get_device_name(torch.cuda.current_device()))

for i in range(1, 11):
    print(i)
