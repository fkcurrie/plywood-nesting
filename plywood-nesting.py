#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
<Your Python File Name>.py: Description of what the script does.

Author: Frank Currie
Date: March 3rd, 2024
Version: 0.1
License: Apache License 2.0
"""

# Apache License 2.0
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import svgwrite
from typing import List, Dict
import csv

# Function to read panel data from a CSV file
def read_panel_data_from_csv(file_path):
    panels = []
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            panels.append({
                "name": row["Name"],
                "quantity": int(row["Quantity"]),
                "length": float(row["Length"]),
                "width": float(row["Width"])
            })
    return panels

# Function to read Plywood dimensions in millimeters
def read_sheet_dimensions_from_csv(file_path: str) -> (float, float):
    with open(file_path, mode='r', newline='') as csvfile:
        # Filter out lines starting with '#'
        filtered_lines = (line for line in csvfile if not line.strip().startswith('#'))
        reader = csv.DictReader(filtered_lines)
        
        for row in reader:  # Assuming only one row for sheet dimensions
            return float(row["Length"]), float(row["Width"])
    return None, None  # Return None if no dimensions were found or file is improperly formatted

# Load sheet dimensions from CSV
plywood_length_mm, plywood_width_mm = read_sheet_dimensions_from_csv("sheets.csv")

# Validate sheet dimensions were loaded
if plywood_length_mm is None or plywood_width_mm is None:
    raise ValueError("Sheet dimensions could not be loaded from 'sheets.csv'.")

# Load panel data from CSV
panels = read_panel_data_from_csv("panels.csv")


def optimize_panel_placement(panels, plywood_length, plywood_width):
    best_solution = None
    best_solution_metric = float('inf')  # Can be the number of sheets used or another efficiency metric

    # Define sorting strategies
    sorting_strategies = [
        lambda p: (-max(p['length'], p['width']), min(p['length'], p['width'])),  # Sort by longest side
        lambda p: (-p['length']*p['width']),  # Sort by area
        lambda p: (-min(p['length'], p['width']), max(p['length'], p['width'])),  # Sort by shortest side
    ]

    # Try each sorting strategy
    for strategy in sorting_strategies:
        sorted_panels = sorted(panels, key=strategy)
        solution = fit_panels_to_sheets(sorted_panels, plywood_length, plywood_width)
        solution_metric = len(solution)  # Example metric: number of sheets used

        if solution_metric < best_solution_metric:
            best_solution = solution
            best_solution_metric = solution_metric

    return best_solution


def fit_panels_to_sheets(panels: List[Dict], plywood_length: float, plywood_width: float) -> List[Dict]:
    """
    Attempt to fit panels onto the minimum number of plywood sheets. Panels can be rotated by 90 degrees.
    Returns a list of sheets with details of the panels placed on each sheet.
    """
    sheets = []
    for panel in sorted(panels, key=lambda x: (x['length']*x['width'], 2*(x['length'] + x['width'])), reverse=True):  # Sort by Shortest Side
        for _ in range(panel['quantity']):
            added = False
            for sheet in sheets:
                if place_panel_on_sheet(sheet, panel, plywood_length, plywood_width):
                    added = True
                    break
            if not added:  # Create a new sheet if panel couldn't be added to existing sheets
                new_sheet = {'panels': [], 'current_x': 0, 'current_y': 0, 'next_y_level': 0}
                if place_panel_on_sheet(new_sheet, panel, plywood_length, plywood_width):
                    sheets.append(new_sheet)
    return sheets

def place_panel_on_sheet(sheet, panel, plywood_length, plywood_width, edge_gap=50, panel_gap=20):
    for rotation in [False, True]:  # Try both orientations
        # Adjust panel dimensions for rotation
        p_length, p_width = (panel['length'], panel['width']) if not rotation else (panel['width'], panel['length'])

        # Including panel_gap in dimensions for spacing between panels, not edge gap
        adjusted_length = p_length + panel_gap
        adjusted_width = p_width + panel_gap

        # Check for fit within sheet dimensions, considering edge gaps
        if (sheet['current_x'] + adjusted_length <= plywood_length - edge_gap and
            sheet['current_y'] + adjusted_width <= plywood_width - edge_gap):

            # Ensure starting position respects edge gap
            actual_x = max(sheet['current_x'], edge_gap)
            actual_y = max(sheet['current_y'], edge_gap)

            # Update sheet with panel placement
            sheet['panels'].append({
                'name': panel['name'], 'x': actual_x, 'y': actual_y,
                'length': p_length, 'width': p_width,
                'rotated': rotation
            })

            # Move current_x to the right for the next panel, including the panel gap, but not beyond the plywood edge
            sheet['current_x'] = actual_x + adjusted_length

            # Adjust next_y_level for the potential next row, ensuring we include the panel gap
            next_y_potential = actual_y + adjusted_width
            if next_y_potential > sheet['next_y_level']:
                sheet['next_y_level'] = next_y_potential

            return True  # Panel placed successfully

        # If it doesn't fit, attempt to move to the next row, respecting edge gaps
        if sheet['current_x'] + adjusted_length > plywood_length - edge_gap:
            sheet['current_x'] = 0  # Reset X to start position, considering next row
            sheet['current_y'] = sheet['next_y_level']  # Move Y to next potential row level

    return False  # If panel can't be placed in any orientation






def generate_svg(sheets: List[Dict], plywood_length: float, plywood_width: float, filename_prefix: str = "sheet"):
    """
    Generate SVG files for each sheet showing the panel placements.
    """
    for index, sheet in enumerate(sheets, start=1):
        dwg = svgwrite.Drawing(f"{filename_prefix}_{index}.svg", profile='tiny', size=(plywood_length, plywood_width))
                # Draw the outline of the plywood sheet
        dwg.add(dwg.rect(insert=(0, 0), size=(plywood_length, plywood_width), fill='lightgrey'))

        # Draw each panel on the sheet
        for panel in sheet['panels']:
            # Different color for rotated panels for easy distinction
            fill_color = "lightblue" if panel['rotated'] else "white"
            # Add the panel rectangle to the drawing
            # Inside the loop where panels are drawn:
            dwg.add(dwg.rect(insert=(panel['x'], panel['y']), size=(panel['length'], panel['width']), fill=fill_color, stroke='black', stroke_width="1mm"))
            # Add the panel name text to the drawing
            text_insert = (panel['x'] + 10, panel['y'] + 20)  # Adjust text position slightly within the panel
            dwg.add(dwg.text(panel['name'], insert=text_insert, fill='black'))

        dwg.save()  # Save the SVG file

# Use the defined functions to fit panels to sheets and generate the corresponding SVG files
sheets_with_panels = fit_panels_to_sheets(panels, plywood_length_mm, plywood_width_mm)
generate_svg(sheets_with_panels, plywood_length_mm, plywood_width_mm)

