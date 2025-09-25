# Gym PyBullet Drones Docker Setup

This setup packages the gym-pybullet-drones library into a Docker container with Jupyter notebook support for easy development and experimentation.

## Quick Start

### 1. Build and Run with Docker Compose (Recommended)

```bash
# From the docker directory
cd docker
docker-compose up --build
```

### 2. Build and Run with Docker Commands

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

## Usage Examples

### Basic Environment Creation
```python
import gym_pybullet_drones
from gym_pybullet_drones.envs import HoverAviary
from gym_pybullet_drones.utils.enums import DroneModel, Physics

# Create environment
env = HoverAviary(drone_model=DroneModel.CF2X, num_drones=1, physics=Physics.PYB)

# Reset environment
obs, info = env.reset()

# Take random actions
for _ in range(100):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()

env.close()
```

### Using PID Control
```python
from gym_pybullet_drones.control.DSLPIDControl import DSLPIDControl
from gym_pybullet_drones.envs import CtrlAviary
import numpy as np

env = CtrlAviary()
ctrl = DSLPIDControl(drone_model=DroneModel.CF2X)

obs, info = env.reset()
for i in range(500):
    # Hover at position [0, 0, 1]
    target_pos = np.array([0, 0, 1])
    action = ctrl.computeControlFromState(
        control_timestep=env.CTRL_TIMESTEP,
        state=obs[0],
        target_pos=target_pos
    )
    obs, _, _, _, _ = env.step([action])
```

## File Structure

```
docker/
├── Dockerfile              # Main Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup
├── notebooks/            # Your Jupyter notebooks (mounted volume)
├── shared/               # Shared files between host and container
└── README.md            # This file
```

## Available Environments

- `HoverAviary` - Single/multi-agent hovering task
- `MultiHoverAviary` - Multi-agent hovering
- `VelocityAviary` - Velocity control environment
- `CtrlAviary` - Low-level control environment
- `BetaAviary` - Advanced control environment

## Container Management

### Stop the container
```bash
docker-compose down
```

### Restart with fresh build
```bash
docker-compose up --build --force-recreate
```

### Execute commands in running container
```bash
docker exec -it gym-pybullet-jupyter bash
```

### View logs
```bash
docker-compose logs -f
```

## Troubleshooting

### If Jupyter doesn't start
Check container logs:
```bash
docker-compose logs gym-pybullet-jupyter
```

### If port 8888 is busy
Change the port in docker-compose.yml:
```yaml
ports:
  - "8889:8888"  # Use port 8889 instead
```

### GPU Support (Optional)
To enable GPU support for PyBullet, modify the docker-compose.yml to include GPU access:
```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
```