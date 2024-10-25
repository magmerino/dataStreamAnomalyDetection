# Anomaly Detection in Temperature Data

![Screenshot 2024-10-25 185746](https://github.com/user-attachments/assets/ff4a2d9a-ae48-49f8-be6c-bab8f45ba0d1)

## Overview

This project implements an anomaly detection system that monitors simulated temperature data over time. The system uses a z-score method to identify anomalies based on recent temperature readings. It includes a data stream generator that simulates temperature variations, an anomaly detector that processes these readings, and a visualization component to dynamically display the results.

## Features

- **Simulated Data Stream**: Generates temperature readings influenced by sinusoidal seasonal changes, random noise, and normally distributed values.
- **Anomaly Detection**: Utilizes the z-score method to detect anomalies in the temperature data stream.
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
