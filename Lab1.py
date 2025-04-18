import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def plot_individual_algorithm(path, algorithm_name, obstacle_verts):
    plt.figure(figsize=(8, 6))
    ax = plt.gca()

    # Draw obstacle
    obstacle = Polygon(obstacle_verts, closed=True,
                      alpha=0.3, edgecolor='black', facecolor='gray')
    ax.add_patch(obstacle)

    # Plot path
    x, y = zip(*path)
    plt.plot(x, y, 'b-', marker='o', markersize=8,
            label=f'{algorithm_name} Path')

    # Mark start and goal
    plt.scatter(*start, s=200, c='green', edgecolor='black',
                marker='*', label='Start (0,0)')
    plt.scatter(*goal, s=200, c='red', edgecolor='black',
                marker='X', label='Goal (8,8)')

    # Configuration
    plt.title(f'{algorithm_name} Navigation', fontsize=14)
    plt.xlabel('X Coordinate', fontsize=12)
    plt.ylabel('Y Coordinate', fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.axis('equal')
    plt.xlim(0, 9)
    plt.ylim(0, 9)
    plt.tight_layout()
    plt.show()

# Environment configuration
start = (0, 0)
goal = (8, 8)
obstacle_vertices = [(2, 2), (2, 5), (5, 5), (5, 2)]

# Updated Bug1 path to avoid entering the obstacle
bug1_path = [
    (0, 0),       # Start
    (2, 2.1),     # Hits the obstacle just above bottom-left
    (2, 5),       # Move along the left edge
    (5, 5),       # Top edge
    (5, 2),       # Right edge
    (5, 5),       # (Backtrack to point closest to goal)
    (8, 8)        # Goal
]

# bug1_path = [(0,0), (2,2), (2,5), (5,5), (5,2), (2,2), (5,5), (8,8)]



# Other algorithms for reference
bug2_path = [(0, 0), (2, 2.1), (5, 2), (5, 5), (8, 8)]
tangent_path = [(0, 0), (2, 2.1), (2, 5), (8, 8)]

# Plot all three separately
plot_individual_algorithm(bug1_path, "BUG1", obstacle_vertices)
plot_individual_algorithm(bug2_path, "BUG2", obstacle_vertices)
plot_individual_algorithm(tangent_path, "Tangent Bug", obstacle_vertices)
