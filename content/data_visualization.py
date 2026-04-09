import numpy as np
import matplotlib.pyplot as plt
import argparse
import yaml


def generateData(config):
    n = config["n"]
    a = config["a"]
    b = config["b"]
    begin = config["begin"]
    end = config["end"]
    x = np.linspace(begin, end, n)
    y = np.polyval([a, b], x)
    y = y + 3 * np.random.randn(n)
    return (x, y)


def customPlot(data, config):
    x, y = data
    select_index = np.random.choice(range(len(x)), size=config["sample_size"])
    select_x = x[select_index]
    select_y = y[select_index]

    plt.scatter(select_x, select_y, c="green", edgecolors="k")
    plt.grid(True)
    plt.show()


def main(config):
    data = generateData(config=config)
    customPlot(data, config=config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default="./configs/data.yaml",
        help="Path to the config file",
    )
    args = parser.parse_args()
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)
    main(config)
