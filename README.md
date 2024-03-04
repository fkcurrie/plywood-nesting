# Plywood Panel Placement Optimizer

This project provides a tools for optimizing the placement of rectangular panels on standard-sized sheets of plywood. It aims to minimize waste by efficiently arranging panels of various dimensions on plywood sheets, taking into consideration the possibility of rotating panels for a better fit. Additionally, the project generates SVG (Scalable Vector Graphics) files to visually represent the planned layout of panels on each sheet.

There are tools designed to calculate the most efficient method for arranging and cutting out panels from a sheet of plywood, a process known as Nesting. However, there are few tools, often expensive, that offer the capability to export these layouts in Scalable Vector Graphics ([SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)) format. SVG is a file format for describing two-dimensional graphics in XML. This format is particularly useful because it allows for the designs to be imported into software applications that can transform the SVG files into G-code. G-code is a language used to instruct CNC ([Computer Numerical Control](https://en.wikipedia.org/wiki/Numerical_control)) machines how to move to achieve the desired cuts. CNC machines are automated milling devices that make industrial components without direct human assistance, using detailed instructions generated from G-code. This process streamlines the transition from digital design to physical production, enabling precise and efficient manufacturing of the panels for various applications, including custom beekeeping hives.

## Features

- **Panel and Sheet Dimension Input**: Reads panel dimensions and quantities from a `panels.csv` file and plywood sheet dimensions from a `sheets.csv` file.
- **Optimization Algorithm**: Implements an optimization algorithm to fit panels onto the fewest number of plywood sheets, including a gap between panels and from the edges of the sheets.
- **SVG Generation**: Produces SVG files showing the placement of panels on each sheet for easy visualization and planning.
- **Customizable Gaps**: Allows specifying custom gaps between panels and from the edges of the sheets to account for cutting tools or other requirements.

## Project Intent and Technology

This project aims to optimize the placement of panels for constructing insulated Layens hives, with a special focus on utilizing the cutting-edge capabilities of the upcoming [Maslow4 CNC](https://www.maslowcnc.com/about-maslow4). The Maslow4 CNC represents a significant advancement in CNC technology, offering precision cutting that is ideal for custom beekeeping hive construction. By designing with the Maslow4 CNC in mind, it ensures that the hive components are efficiently cut from plywood sheets, reducing waste and maximizing the use of materials.

The use of Maslow4 CNC technology in this project underscores our commitment to innovative, sustainable beekeeping practices. By leveraging precise, computer-aided cutting techniques, the aim is to create hives that not only support the health and productivity of bee colonies but also promote the use of sustainable materials and construction methods.

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
