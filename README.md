# Anomaly Detection in Temperature Data

![Screenshot 2024-10-25 185746](https://github.com/user-attachments/assets/ff4a2d9a-ae48-49f8-be6c-bab8f45ba0d1)

## Overview

This project implements an anomaly detection system that monitors simulated temperature data over time. The system uses a z-score method to identify anomalies based on recent temperature readings. It includes a data stream generator that simulates temperature variations, an anomaly detector that processes these readings, and a visualization component to dynamically display the results.

## Features

- **Simulated Data Stream**: Generates temperature readings influenced by sinusoidal seasonal changes, random noise, and normally distributed values.
- **Anomaly Detection**: The Z-score method detects anomalies in temperature data streams by quantifying how far each data point deviates from the mean in terms of standard deviations. By identifying Z-scores above a specified threshold (typically between 2 and 3), this method effectively flags outliers. The Z-score assumes a normal distribution, making it most effective for datasets that adhere to this characteristic. Its straightforward implementation requires no external libraries, making it an ideal choice for this project.
- **Dynamic Visualization**: Visualizes the temperature readings and anomalies in real-time using Matplotlib. Red points represent an anomaly within the data series.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project-directory>
   ```

3. Install the required packages:

   ```bash
   pip install numpy matplotlib
   ```

## Docker Support

A `Dockerfile` has been added to facilitate easy deployment of the application in a containerized environment. To build and run the application using Docker, follow these steps:

1. **Build the Docker image**:

   ```bash
   docker build -t anomaly-detector .
   ```

2. **Run the Docker container**:

   ```bash
   docker run --rm anomaly-detector
   ```

This setup allows for a consistent environment and simplifies the deployment process across different systems.


## Configuration

The configuration parameters can be adjusted in the `config.py` file:

- `MAX_NUMBER_OF_VALUES`: Maximum number of temperature values to simulate.
- `WINDOW_SIZE`: Number of recent data points to consider for calculating the moving mean and standard deviation.
- `THRESHOLD`: Z-score threshold for detecting anomalies.
- Temperature-related parameters such as `AVERAGE_TEMPERATURE`, `TEMPERATURE_DEVIATION`, `NOISE_DEVIATION`, and `SIN_AMPLITUDE`.

## Usage

To start the anomaly detection process, run the `main.py` file:

```bash
python main.py
```

The program will continuously generate temperature readings and display them in a dynamic plot. Anomalous values will be highlighted in red, while normal values will be shown in blue.

## License

This project has no license, as this is a mock project for applying to GlassDoor.
