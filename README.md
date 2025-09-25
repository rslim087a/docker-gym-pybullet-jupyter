# Gym PyBullet Drones Docker Setup

This setup packages the gym-pybullet-drones library into a Docker container with Jupyter notebook support for easy development and experimentation.

## Quick Start

### 1. Build and Run with Docker Commands

```bash
# Build the image
docker build -t gym-pybullet-jupyter -f docker/Dockerfile .

# Run the container
docker run -p 8888:8888 -v $(pwd)/docker/notebooks:/workspace/notebooks gym-pybullet-jupyter
```

### 3. Access Jupyter Notebook

Once the container is running, open your browser and go to:
```
http://localhost:8888
```
