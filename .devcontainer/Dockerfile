# Use NVIDIA CUDA base image with Python
FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04

# Set noninteractive for apt installs
ENV DEBIAN_FRONTEND=noninteractive

# System setup
RUN apt-get update && apt-get install -y \
    python3-pip python3-dev python-is-python3 \
    git wget curl nano vim build-essential \
    libssl-dev libffi-dev \
    && apt-get clean

# Create a non-root user
RUN useradd -ms /bin/bash vscode
USER vscode
WORKDIR /home/vscode

# Install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt
RUN pip install --no-cache-dir ipython
