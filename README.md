# Plywood Panel Placement Optimizer

This project provides a set of tools for optimizing the placement of rectangular panels on standard-sized sheets of plywood. It aims to minimize waste by efficiently arranging panels of various dimensions on plywood sheets, taking into consideration the possibility of rotating panels for a better fit. Additionally, the project generates SVG (Scalable Vector Graphics) files to visually represent the planned layout of panels on each sheet.

## Features

- **Panel and Sheet Dimension Input**: Reads panel dimensions and quantities from a `panels.csv` file and plywood sheet dimensions from a `sheets.csv` file.
- **Optimization Algorithm**: Implements an optimization algorithm to fit panels onto the fewest number of plywood sheets, including a gap between panels and from the edges of the sheets.
- **SVG Generation**: Produces SVG files showing the placement of panels on each sheet for easy visualization and planning.
- **Customizable Gaps**: Allows specifying custom gaps between panels and from the edges of the sheets to account for cutting tools or other requirements.

## Getting Started

### Prerequisites

- Python 3.x
- Pip for installing Python packages

### Installation

1. Clone the repository or download the source code.
2. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. Prepare your panels.csv and sheets.csv files according to the project's specifications.

panels.csv format:
```sh
   Name,Quantity,Length,Width
   A,2,809.62,461.17
   B,1,809.62,349.25
```
sheets.csv format:
```sh
   Length,Width
   2438.4,1219.2
```
4. Run the main script

### Contributing
Contributions to improve the project are welcome. Please follow the standard fork-and-pull request workflow on GitHub.

### License
This project is licensed under the Apache License 2.0.

### Acknowledgments
- This project was inspired by and may incorporate ideas or techniques outlined in the plans for an insulated Layens hive available at [Horizontal Hive](https://www.horizontalhive.com/how-to-build/insulated-layens-hive.shtml). These detailed plans offer valuable insights into sustainable beekeeping practices and hive design.
- This project was inspired by the need for efficient use of materials in carpentry and manufacturing.
