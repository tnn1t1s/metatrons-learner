import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def artful_metatron_cube():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor("#1e1e1e")  # Dark background
    ax.axis("off")  # No axis

    # Circle and line colors
    circle_color = "#DAA520"  # Gold color
    line_color = "#DAA520"  # Same color for consistency

    # Positions for outer hexagon nodes
    radius_outer = 4
    radius_inner = 2
    positions = {}

    # Place outer hexagon nodes
    for i in range(6):
        angle = np.radians(i * 60)
        x, y = radius_outer * np.cos(angle), radius_outer * np.sin(angle)
        positions[f"Outer{i + 1}"] = (x, y)

    # Place inner hexagon nodes
    for i in range(6):
        angle = np.radians(i * 60)
        x, y = radius_inner * np.cos(angle), radius_inner * np.sin(angle)
        positions[f"Inner{i + 1}"] = (x, y)

    # Center node
    positions["Center"] = (0, 0)

    # Draw all connections
    for node_a, (x1, y1) in positions.items():
        for node_b, (x2, y2) in positions.items():
            ax.plot([x1, x2], [y1, y2], color=line_color, linewidth=0.5, alpha=0.7)

    # Draw concentric circles for nodes
    for x, y in positions.values():
        # Outer circle
        circle = patches.Circle((x, y), radius=0.4, edgecolor=circle_color, facecolor="none", linewidth=1)
        ax.add_patch(circle)
        # Inner circle
        inner_circle = patches.Circle((x, y), radius=0.2, edgecolor=circle_color, facecolor="none", linewidth=1)
        ax.add_patch(inner_circle)

    # Draw the center node with larger concentric circles
    center_x, center_y = positions["Center"]
    for r in [0.6, 0.3]:
        circle = patches.Circle((center_x, center_y), radius=r, edgecolor=circle_color, facecolor="none", linewidth=1.5)
        ax.add_patch(circle)

    plt.title("Artful Metatron's Cube", color="white", fontsize=16)
    plt.show()

# Call the function to visualize
artful_metatron_cube()

