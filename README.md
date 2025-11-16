# Python Test - Weaving Analyzer Program

## Overview

The **Weaving Analyzer Program** is designed for surface inspection, ensuring precise monitoring and synchronization of cameras, lighting, and surface movement. It collects velocity data, captures images, and sends this information to a server for analysis.

---

## Features

1. **Velocity and Displacement Measurement**:
   - Measures surface velocity using a simulated velocity sensor.
   - Applies a moving average filter to reduce noise.
   - Calculates surface displacement based on velocity.

2. **Camera Triggering**:
   - Captures images using two cameras with green and blue lighting.
   - Ensures minimal displacement between images of different light types.
   - Sends image batches to the server.

3. **Multithreading**:
   - Implements multithreading for efficient server communication.

4. **Logging System**:
   - Provides detailed logs for debugging and monitoring.

5. **Testing**:
   - Includes unit tests for core functionalities.

---

## System Requirements

- **Languages**: Python 3.13+
- **Dependencies**:
  - `numpy`
  - `Pillow`
  - `noise`
  - `requests`
  - `flask`
  - `pytest`
  - `flake8`
  - `isort`
  - `black`

---

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:mathelima/weaving-analyzer.git
   ```
2. Install dependencies:
   ```bash
   make install
   ```

---

## Usage

### Running the Application

1. Start the server:
   ```bash
   make server
   ```

2. Run the main application:
   ```bash
   make run
   ```

### Running Tests

To execute the unit tests:
```bash
make test
```

### Code Formatting and Linting

- Format the code:
  ```bash
  make format
  ```

- Check for linting errors:
  ```bash
  make lint
  ```

---

## API Endpoints

### `/ping`
- **Method**: GET
- **Response**: `204 No Content`

### `/pictures_batch`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "lights": [
      {
        "light": "blue_light",
        "creation_date": "2023-08-31 15:43:28.416324",
        "surface_velocity": 0.123,
        "surface_displacement": 1.152,
        "pictures": {
          "left": { "picture": "binary_data", "iso": 100, "exposure_time": 0.005, "diaphragm_opening": 2.8 },
          "right": { "picture": "binary_data", "iso": 200, "exposure_time": 0.01, "diaphragm_opening": 2.8 }
        }
      }
    ]
  }
  ```
- **Response**: `201 Created`

### `/surface_movement`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "velocity": 0.123,
    "displacement": 4.431
  }
  ```
- **Response**: `201 Created`

---

## Logging

The program uses a custom logging system with the following format:
```
[16/Nov/2025 20:19:29] - LoggerName - LogLevel - Message
```

Log levels:
- `DEBUG`: Detailed information for debugging.
- `INFO`: General information about program execution.
- `WARNING`: Alerts about potential issues.
- `ERROR`: Errors that occurred during execution.
- `CRITICAL`: Critical issues requiring immediate attention.

---