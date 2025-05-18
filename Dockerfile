# Use a slim Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY . /app

COPY hf_model_cache/ /root/.cache/huggingface/hub/

# Install Python dependencies
RUN pip install --upgrade pip

RUN pip install --resume-retries 10 --timeout 60 -r requirements.txt

# Copy cached Hugging Face model into the container
COPY hf_model_cache/ /root/.cache/huggingface/hub/

# Expose FastAPI default port
EXPOSE 8000