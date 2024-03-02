import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Load data from INFILE into a numpy array
    data = np.loadtxt(INFILE, delimiter=',')

    # Modify the input data so that it has a mean of 0
    mean_centered_data = data - np.mean(data)

    # Modify the zero mean data so that it has a standard deviation of 1
    standardized_data = mean_centered_data / np.std(mean_centered_data)

    processed = standardized_data

    np.savetxt(OUTFILE, processed, delimiter=',')
