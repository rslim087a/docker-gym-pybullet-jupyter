FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libgl1-mesa-dri \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libglu1-mesa-dev \
    freeglut3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy requirements and install Python dependencies
COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the gym_pybullet_drones package and setup.py
COPY gym_pybullet_drones/ ./gym_pybullet_drones/
COPY docker/setup.py .

# Install the package in development mode
RUN pip install -e .

# Create jupyter config directory
RUN mkdir -p /root/.jupyter

# Configure Jupyter to allow external connections
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.port = 8888" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# Create notebooks directory
RUN mkdir -p /workspace/notebooks

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter notebook
CMD ["jupyter", "notebook", "--notebook-dir=/workspace/notebooks", "--allow-root"]