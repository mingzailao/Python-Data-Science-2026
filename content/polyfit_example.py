import time
import argparse
import numpy as np
from data_visualization import generateData
import yaml


def main(config):
    with open(config["data_config"], "r") as f:
        data_config = yaml.safe_load(f)
        methods = config["methods"]
    x, y = generateData(data_config)

    t1 = time.time()
    if methods == "numpy.polyfit":
        (ar, br) = np.polyfit(x, y, 1)
    elif methods == "stats.linregress":
        from scipy import stats

        (ar, br, r_value, p_value, std_err) = stats.linregress(x, y)
    else:
        raise ValueError("Unsupported method: {}".format(methods))
    y_estimate = np.polyval([ar, br], x)
    # compute the mean square erro

    err = np.sqrt(sum((y_estimate - y) ** 2) / len(y))
    t2 = time.time()
    t_polyfit = float(t2 - t1)

    print("Linear regression using polyfit")
    print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))
    print("Time taken: {} seconds".format(t_polyfit))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        default="./configs/polyfit.yaml",
        help="Path to the config file",
    )
    args = parser.parse_args()
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)
    main(config)
