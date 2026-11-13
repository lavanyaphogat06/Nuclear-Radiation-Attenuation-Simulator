import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq


# ============================================================
#       NUCLEAR RADIATION ATTENUATION & SHIELDING SIMULATOR
# ============================================================

materials = {
    "Lead": 1.20,
    "Concrete": 0.15,
    "Steel": 0.45,
    "Water": 0.07,
    "Aluminum": 0.17
}


# ============================================================
#                     DISPLAY FUNCTIONS
# ============================================================

def print_header():
    print("\n")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║        ☢  NUCLEAR RADIATION ATTENUATION SIMULATOR       ║")
    print("║            Radiation Shielding Analysis Tool             ║")
    print("╚══════════════════════════════════════════════════════════╝")


def print_section(title):
    print("\n╔══════════════════════════════════════════════════════════╗")
    print(f"║  {title:<54}║")
    print("╚══════════════════════════════════════════════════════════╝")


def pause():
    input("\nPress ENTER to return to the main menu...")


# ============================================================
#                     CALCULATION FUNCTIONS
# ============================================================

def transmitted_intensity(I0, mu, x):
    """
    Calculate transmitted radiation intensity using:
    
        I = I0 * exp(-mu*x)
    """
    return I0 * np.exp(-mu * x)


def calculate_hvl(mu):
    """
    Half Value Layer:
    
        HVL = ln(2) / mu
    """
    return np.log(2) / mu


def calculate_tvl(mu):
    """
    Tenth Value Layer:
    
        TVL = ln(10) / mu
    """
    return np.log(10) / mu


def calculate_required_thickness(I0, target, mu):
    """
    Find thickness required to reduce intensity
    to the target value using scipy.optimize.brentq.
    """

    def equation(x):
        return I0 * np.exp(-mu * x) - target

    return brentq(equation, 0, 1000)


# ============================================================
#                     INPUT FUNCTIONS
# ============================================================

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("  ✗ Please enter a value greater than zero.")

        except ValueError:
            print("  ✗ Invalid input. Please enter a number.")


def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value

            print("  ✗ Please enter zero or a positive value.")

        except ValueError:
            print("  ✗ Invalid input. Please enter a number.")


def choose_material():
    print("\nAvailable Shielding Materials")
    print("────────────────────────────────────────")

    material_names = list(materials.keys())

    for i, material in enumerate(material_names, start=1):
        print(f"  [{i}] {material:<12}  μ = {materials[material]:.3f} cm⁻¹")

    while True:
        try:
            choice = int(input("\n  Select material ──► "))

            if 1 <= choice <= len(material_names):
                return material_names[choice - 1]

            print("  ✗ Please select a valid material number.")

        except ValueError:
            print("  ✗ Please enter a number.")


# ============================================================
#                   MATERIAL INFORMATION
# ============================================================

def show_material_information():

    print_section("SHIELDING MATERIAL DATABASE")

    print()
    print("┌──────────────┬────────────┬────────────┬────────────┐")
    print("│ Material     │ μ (cm⁻¹))  │ HVL (cm)   │ TVL (cm)   │")
    print("├──────────────┼────────────┼────────────┼────────────┤")

    for material, mu in materials.items():

        hvl = calculate_hvl(mu)
        tvl = calculate_tvl(mu)

        print(
            f"│ {material:<12} │ "
            f"{mu:<10.3f} │ "
            f"{hvl:<10.3f} │ "
            f"{tvl:<10.3f} │"
        )

    print("└──────────────┴────────────┴────────────┴────────────┘")

    print("\nμ   = Linear attenuation coefficient")
    print("HVL = Half Value Layer")
    print("TVL = Tenth Value Layer")

    pause()


# ============================================================
#                   MAIN CALCULATION
# ============================================================

def perform_calculation():

    print_section("RADIATION ATTENUATION CALCULATION")

    print("\nEnter the simulation parameters:\n")

    I0 = get_positive_number(
        "  Initial radiation intensity ──► "
    )

    material = choose_material()
    mu = materials[material]

    x = get_non_negative_number(
        "\n  Shield thickness (cm) ─────────► "
    )

    while True:

        target = get_positive_number(
            "  Target intensity ──────────────► "
        )

        if target < I0:
            break

        print("  ✗ Target intensity must be less than initial intensity.")

    # --------------------------------------------------------
    # CALCULATIONS
    # --------------------------------------------------------

    I = transmitted_intensity(I0, mu, x)

    reduction = ((I0 - I) / I0) * 100

    hvl = calculate_hvl(mu)
    tvl = calculate_tvl(mu)

    required_thickness = calculate_required_thickness(
        I0, target, mu
    )

    # --------------------------------------------------------
    # INPUT DISPLAY
    # --------------------------------------------------------

    print_section("INPUT PARAMETERS")

    print(f"║  Initial Intensity       : {I0:<25.4f}║")
    print(f"║  Shield Material         : {material:<25}║")
    print(f"║  Attenuation Coefficient : {mu:<25.4f}║")
    print(f"║  Shield Thickness        : {x:<25.4f} cm ║")
    print(f"║  Target Intensity        : {target:<25.4f}║")

    # --------------------------------------------------------
    # RESULT DISPLAY
    # --------------------------------------------------------

    print_section("CALCULATION RESULTS")

    print(f"║  Transmitted Intensity : {I:<28.4f}║")
    print(f"║  Radiation Reduction   : {reduction:<27.2f}%║")
    print(f"║  Half Value Layer      : {hvl:<28.4f} cm ║")
    print(f"║  Tenth Value Layer     : {tvl:<28.4f} cm ║")
    print(f"║  Required Thickness    : {required_thickness:<28.4f} cm ║")

    # --------------------------------------------------------
    # VISUAL ATTENUATION BAR
    # --------------------------------------------------------

    remaining = (I / I0) * 100

    bar_length = 40
    filled = int((remaining / 100) * bar_length)

    if filled > bar_length:
        filled = bar_length

    bar = "█" * filled + "░" * (bar_length - filled)

    print("\n  Radiation remaining")
    print(f"  [{bar}] {remaining:.2f}%")

    print("\n  ✓ Calculation completed successfully.")

    pause()


# ============================================================
#                     ATTENUATION GRAPH
# ============================================================

def attenuation_graph():

    print_section("ATTENUATION GRAPH GENERATOR")

    print("\nEnter graph parameters:\n")

    I0 = get_positive_number(
        "  Initial radiation intensity ──► "
    )

    material = choose_material()
    mu = materials[material]

    max_thickness = get_positive_number(
        "\n  Maximum thickness (cm) ───────► "
    )

    print("\n  Generating attenuation data...")

    # Same NumPy approach
    x_values = np.linspace(0, max_thickness, 200)

    intensity_values = transmitted_intensity(
        I0,
        mu,
        x_values
    )

    # --------------------------------------------------------
    # GRAPH
    # --------------------------------------------------------

    plt.figure(figsize=(9, 6))

    plt.plot(
        x_values,
        intensity_values,
        linewidth=2,
        label=material
    )

    plt.xlabel("Shield Thickness (cm)")
    plt.ylabel("Transmitted Intensity")

    plt.title(
        f"Radiation Attenuation - {material}"
    )

    plt.grid(True)
    plt.legend()

    filename = material.replace(" ", "_") + "_attenuation_graph.png"

    plt.savefig(
    filename,
    dpi=300,
    bbox_inches="tight"
    )

    print("\n  ✓ Graph generated successfully.")
    print(f"  ✓ Saved as: {filename}")
    print("\n  Opening graph...")

    plt.show()

    plt.close()
    
    print("\n  Returning to main menu...")
    


# ============================================================
#                   MATERIAL COMPARISON
# ============================================================


def comparison_graph():

    print_section("SHIELDING MATERIAL COMPARISON")

    print("\nSelect comparison type:")
    print("  [1] Compare all materials")
    print("  [2] Compare any two materials")

    while True:
        comparison_choice = input("\n  Select an option ──► ").strip()
        if comparison_choice in ["1", "2"]:
            break
        print("  ✗ Invalid option. Please select 1 or 2.")

    if comparison_choice == "1":
        selected_materials = list(materials.keys())
        filename = "all_materials_comparison.png"
        graph_title = "Radiation Attenuation Comparison of All Materials"
    else:
        print("\nSelect the first material:")
        first_material = choose_material()

        while True:
            print("\nSelect the second material:")
            second_material = choose_material()
            if second_material != first_material:
                break
            print("  ✗ Please select a different material.")

        selected_materials = [first_material, second_material]
        filename = "two_materials_comparison.png"
        graph_title = f"Radiation Attenuation: {first_material} vs {second_material}"

    print("\nEnter comparison parameters:\n")

    I0 = get_positive_number(
        "  Initial radiation intensity ──► "
    )

    max_thickness = get_positive_number(
        "  Maximum thickness (cm) ───────► "
    )
    x_values = np.linspace(
        0,
        max_thickness,
        200
    )

    print("\n  Generating comparison data...")

    plt.figure(figsize=(10, 6))

    for material in selected_materials:
        mu = materials[material]

        intensity_values = transmitted_intensity(
            I0,
            mu,
            x_values
        )

        plt.plot(
            x_values,
            intensity_values,
            linewidth=2,
            label=material
        )

    plt.xlabel("Shield Thickness (cm)")
    plt.ylabel("Transmitted Intensity")
    plt.title(graph_title)

    plt.grid(True)
    plt.legend()

    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    print("\n  ✓ Graph generated successfully.")
    print(f"  ✓ Saved as: {filename}")
    print("\n  Opening graph...")

    plt.show()

    plt.close()

    print("\n  Returning to main menu...")

    def view_saved_graphs():

        print_section("VIEW SAVED GRAPHS")

        print("\n  [1] View Attenuation Graph")
        print("  [2] View All-Materials Comparison")
        print("  [3] View Two-Materials Comparison")
        print("  [4] Return to Main Menu")

        choice = input("\n  Select an option ──► ").strip()

        if choice == "1":

            material = choose_material()

            filename = material.replace(" ", "_") + "_attenuation_graph.png"

            try:
                img = plt.imread(filename)

                plt.figure(figsize=(9, 6))
                plt.imshow(img)
                plt.axis("off")
                plt.title(f"{material} Attenuation Graph")
                plt.show()
                plt.close()

            except FileNotFoundError:
                print("\n  ✗ No saved graph found for this material.")
                print("  Please generate the graph first.")

        elif choice == "2":

            filename = "all_materials_comparison.png"

            try:
                img = plt.imread(filename)

                plt.figure(figsize=(10, 6))
                plt.imshow(img)
                plt.axis("off")
                plt.title("All Materials Comparison")
                plt.show()
                plt.close()

            except FileNotFoundError:
                print("\n  ✗ All-materials comparison graph has not been generated yet.")

        elif choice == "3":

            filename = "two_materials_comparison.png"

            try:
                img = plt.imread(filename)

                plt.figure(figsize=(10, 6))
                plt.imshow(img)
                plt.axis("off")
                plt.title("Two-Materials Comparison")
                plt.show()
                plt.close()

            except FileNotFoundError:
                print("\n  ✗ Two-materials comparison graph has not been generated yet.")

        elif choice == "4":
            return

        else:
            print("\n  ✗ Invalid option.")

        pause()





# ============================================================
#                         ABOUT
# ============================================================

def about_project():

    print_section("ABOUT THE PROJECT")

    print("""
  Nuclear Radiation Attenuation & Shielding Simulator

  This program models the attenuation of radiation as it
  passes through different shielding materials.

  Main equation:

      I = I₀ e^(-μx)

  where:

      I₀ = Initial radiation intensity
      I  = Transmitted radiation intensity
      μ  = Linear attenuation coefficient
      x  = Shield thickness

  The simulator calculates:

      • Transmitted intensity
      • Radiation reduction
      • Half Value Layer (HVL)
      • Tenth Value Layer (TVL)
      • Required shielding thickness

  Numerical Method:
      scipy.optimize.brentq

  Graphical Analysis:
      Matplotlib

  Numerical Computation:
      NumPy
    """)

    pause()


# ============================================================
#                       MAIN MENU
# ============================================================

def main():
    while True:
        print("\n        ┌────────────────────────────────────┐")
        print("        │  [1]  Radiation Attenuation        │")
        print("        │  [2]  Material Database            │")
        print("        │  [3]  Generate Attenuation Graph   │")
        print("        │  [4]  Compare All Materials        │")
        print("        │  [5]  View Saved Graphs            │")
        print("        │  [6]  About Project                │")
        print("        │  [7]  Exit Simulator               │")
        print("        └────────────────────────────────────┘")

        choice = input("\n        Select an option ──► ").strip()

        if choice == "1":
            perform_calculation()

        elif choice == "2":
            show_material_information()

        elif choice == "3":
            attenuation_graph()

        elif choice == "4":
            comparison_graph()

        elif choice == "5":
            view_saved_graphs()

        elif choice == "6":
            about_project()

        elif choice == "7":
            print("\n")
            print("╔══════════════════════════════════════════════════════════╗")
            print("║       Thank you for using the Radiation Simulator!       ║")
            print("║                    ☢  Simulation Ended                  ║")
            print("╚══════════════════════════════════════════════════════════╝")
            print()
            break

        else:
            print("\n        ✗ Invalid option. Please select 1–7.")


# ============================================================
#                    PROGRAM START
# ============================================================
main()
