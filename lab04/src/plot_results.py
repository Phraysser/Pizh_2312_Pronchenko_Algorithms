import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import os


def load_csv(csv_file: str = "lab04/src/lab04_results.csv"):
    data = defaultdict(list)
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            alg = row["algorithm"]
            size = int(row["size"])
            dtype = row["data_type"]
            time_ms = float(row["time_ms"])
            data[alg].append((size, dtype, time_ms))
    return data


def plot_time_vs_size(data, data_type: str = "random"):
    plt.figure()
    for alg, rows in data.items():
        xs = [r[0] for r in rows if r[1] == data_type]
        ys = [r[2] for r in rows if r[1] == data_type]
        if xs:
            plt.plot(sorted(xs), [y for _, y in sorted(zip(xs, ys))], label=alg)
    plt.xlabel("Size (n)")
    plt.ylabel("Time (ms)")
    plt.title(f"Time vs Size (data_type={data_type})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    save_path = os.path.join(os.path.dirname(__file__), f"time_vs_size_{data_type}.png")
    plt.savefig(save_path, dpi=300)
    plt.close()


def plot_time_vs_type(data, size: int = 5000):
    plt.figure()
    types = ["random", "sorted", "reversed", "almost_sorted"]
    for alg, rows in data.items():
        xs = []
        ys = []
        for t in types:
            found = [r[2] for r in rows if r[0] == size and r[1] == t]
            xs.append(t)
            ys.append(found[0] if found else float('nan'))
        plt.plot(types, ys, marker='o', label=alg)
    plt.xlabel("Data type")
    plt.ylabel("Time (ms)")
    plt.title(f"Time vs Data Type (size={size})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    save_path = os.path.join(os.path.dirname(__file__), f"time_vs_type_size{size}.png")
    plt.savefig(save_path, dpi=300)
    plt.close()


if __name__ == "__main__":
    data = load_csv()
    plot_time_vs_size(data, data_type="random")
    plot_time_vs_type(data, size=5000)
