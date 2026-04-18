# Computational Fluid Dynamics (CFD) Flow Simulator

A Python-based numerical simulation tool for solving incompressible flow problems using simplified Navier-Stokes equations on a structured grid.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Navier-Stokes Solver**: Solves simplified incompressible Navier-Stokes equations
- **Finite Difference Method**: Uses explicit finite difference scheme for spatial and temporal discretization
- **Boundary Conditions**: Supports inlet, outlet, and wall boundary conditions
- **Visualization**: Real-time velocity field visualization using Matplotlib
- **Customizable Parameters**: Easily adjustable grid size, time step, and viscosity

## 📦 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/cherry-git999/Computational-Fluid-Dynamics.git
cd Computational-Fluid-Dynamics
```

### 2. Create a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install numpy matplotlib
```

## 📖 Usage

Run the flow simulator:

```bash
python flow_simulator.py
```

The script will:
1. Initialize a 60×60 structured grid with velocity fields
2. Run 500 iterations of the Navier-Stokes solver
3. Apply boundary conditions at inlet, outlet, and walls
4. Display the velocity field visualization

### Customization

Edit the parameters at the beginning of `flow_simulator.py`:

```python
# Grid configuration
nx, ny = 60, 60           # Grid dimensions
dx, dy = 1.0, 1.0         # Grid spacing

# Time stepping
dt = 0.05                 # Time step size

# Fluid properties
viscosity = 0.1           # Kinematic viscosity

# Simulation
n_iterations = 500        # Number of time steps
```

## 📁 Project Structure

```
Computational-Fluid-Dynamics/
├── flow_simulator.py    # Main CFD simulator
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .git/               # Git repository
```

## ⚙️ Configuration

### Key Parameters Explained

| Parameter | Default | Description |
|-----------|---------|-------------|
| `nx, ny` | 60, 60 | Grid resolution in x and y directions |
| `dx, dy` | 1.0, 1.0 | Grid spacing |
| `dt` | 0.05 | Time step size (smaller = more stable but slower) |
| `viscosity` | 0.1 | Kinematic viscosity coefficient |

### Tips for Better Results

- **Stability**: Keep `dt` small relative to `dx²/viscosity` (CFL condition)
- **Grid**: Increase `nx` and `ny` for higher resolution (slower computation)
- **Convergence**: Increase iterations for more developed flow

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License. See LICENSE file for more details.

## 🔗 Repository

- GitHub: [Computational-Fluid-Dynamics](https://github.com/cherry-git999/Computational-Fluid-Dynamics)

## 📧 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Happy Simulating!** 🌊
