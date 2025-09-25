from setuptools import setup, find_packages

setup(
    name="gym-pybullet-drones",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "gymnasium>=0.27.0",
        "pybullet>=3.2.0",
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
        "Pillow>=8.0.0",
        "transforms3d>=0.3.1",
        "cycler>=0.11.0",
    ],
    python_requires=">=3.8",
)