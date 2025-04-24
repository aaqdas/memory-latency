import matplotlib.pyplot as plt
import csv

# Data file
data_file = "latency_data.csv"

# Lists to store data
mem_sizes = []
latencies = []

# Read data from the CSV file
with open(data_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        mem_sizes.append(float(row[1]))  # Memory size (MiB)
        latencies.append(float(row[2]))  # Access latency (ns)

# Plot the data
plt.figure(figsize=(10, 6))
plt.semilogx(mem_sizes, latencies, marker="o", linestyle="-", color="b", label="Latency")

# Add labels and title
plt.xlabel("Memory Size (MiB)")
plt.ylabel("Access Latency (ns)")
plt.title("Memory Access Latency vs Memory Size")
plt.grid(True)
plt.legend()

# Save the plot as a PNG file
plt.savefig("latency_plot.png")
plt.show()