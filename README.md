
# Nuclear Radiation Attenuation & Shielding Simulator

## Project Overview

The Nuclear Radiation Attenuation & Shielding Simulator is a Python-based application designed to study how radiation intensity decreases as it passes through different shielding materials.

The project uses the exponential attenuation law to calculate transmitted radiation intensity and evaluate the shielding performance of materials such as Lead, Concrete, Steel, Water, and Aluminum.

It also provides graphical comparisons to help users understand the effectiveness of different shielding materials.

## Objectives

- Calculate transmitted radiation intensity through a shielding material.
- Determine the percentage reduction in radiation intensity.
- Calculate Half Value Layer (HVL) and Tenth Value Layer (TVL).
- Estimate the shielding thickness required to achieve a specified target intensity.
- Generate attenuation graphs for individual materials.
- Compare the attenuation performance of all materials or any two selected materials.

## Theoretical Background

The simulator uses the exponential radiation attenuation equation:

**I = I₀ × e^(-μx)**

Where:

- I₀ = Initial radiation intensity
- I = Transmitted radiation intensity
- μ = Linear attenuation coefficient (cm⁻¹)
- x = Shield thickness (cm)

The Half Value Layer is calculated using:

**HVL = ln(2) / μ**

The Tenth Value Layer is calculated using:

**TVL = ln(10) / μ**

## Materials Used

The simulator includes five shielding materials with predefined linear attenuation coefficients:

| Material | Attenuation Coefficient (cm⁻¹) |
|---|---:|
| Lead | 1.20 |
| Concrete | 0.15 |
| Steel | 0.45 |
| Water | 0.07 |
| Aluminum | 0.17 |

These coefficients are predefined values used for the educational simulation.

## Features

1. **Radiation Attenuation Calculation**  
   Calculates transmitted intensity, radiation reduction, HVL, TVL, and required shielding thickness.

2. **Material Database**  
   Displays the attenuation coefficient, HVL, and TVL of all available materials.

3. **Individual Attenuation Graph**  
   Generates a graph showing the decrease in radiation intensity with increasing shield thickness for a selected material.

4. **All-Material Comparison**  
   Generates a combined graph comparing the attenuation behaviour of all five materials.

5. **Two-Material Comparison**  
   Allows users to select any two different materials and compare their attenuation curves on the same graph.

6. **View Saved Graphs**  
   Allows users to view previously generated attenuation and comparison graphs.

## Python Libraries Used

- **NumPy:** Used for numerical calculations, exponential functions, and generating thickness values.
- **Matplotlib:** Used for plotting, displaying, and saving graphs.
- **SciPy:** The `scipy.optimize.brentq` function is used to calculate the required shielding thickness numerically.

## Installation and Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install numpy matplotlib scipy
```

## How to Run the Program

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run the following command:

```bash
python "Nuclear Attenuation.py"
```

4. The main menu will appear.
5. Select the required option by entering its corresponding number.
6. Follow the instructions displayed by the program.

## Numerical Method

The program uses the **Brent's method**, implemented through `scipy.optimize.brentq`, to determine the shielding thickness required to reduce the initial radiation intensity to a specified target value.

## Output and Visualizations

The program generates and saves the following graphs:

- Individual material attenuation graphs.
- `all_materials_comparison.png`
- `two_materials_comparison.png`

The graphs illustrate the relationship between shield thickness and transmitted radiation intensity.

## Project Limitations

- The attenuation coefficients are predefined for this educational simulation.
- The model assumes exponential attenuation through a uniform shielding material.
- The simulation does not account for complex effects such as radiation scattering, buildup factors, or changes in material properties.

## Conclusion

This project demonstrates the application of Python programming and numerical methods to a radiation shielding problem. It combines mathematical modelling, user-defined functions, input validation, numerical computation, and graphical visualization to analyse the attenuation behaviour of different shielding materials.

The simulator provides an interactive way to study and compare shielding materials using the exponential attenuation law.
