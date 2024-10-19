import numpy as np


def calculate(list):
    if (len(list) < 9):
        raise ValueError("List must contain nine numbers.")

    list_to_array = np.array(list).reshape(3, 3)

    # Mean
    axis1_mean = np.mean(list_to_array, axis=0).tolist()
    axis2_mean = np.mean(list_to_array, axis=1).tolist()
    flattened_mean = np.mean(list_to_array).tolist()

    # Variance
    axis1_variance = np.var(list_to_array, axis=0).tolist()
    axis2_variance = np.var(list_to_array, axis=1).tolist()
    flattened_variance = np.var(list_to_array).tolist()

    # Standard Deviation
    axis1_std = np.std(list_to_array, axis=0).tolist()
    axis2_std = np.std(list_to_array, axis=1).tolist()
    flattened_std = np.std(list_to_array).tolist()

    # Max
    axis1_max = np.max(list_to_array, axis=0).tolist()
    axis2_max = np.max(list_to_array, axis=1).tolist()
    flattened_max = np.max(list_to_array).tolist()

    # Min
    axis1_min = np.min(list_to_array, axis=0).tolist()
    axis2_min = np.min(list_to_array, axis=1).tolist()
    flattened_min = np.min(list_to_array).tolist()

    # Sum
    axis1_sum = np.sum(list_to_array, axis=0).tolist()
    axis2_sum = np.sum(list_to_array, axis=1).tolist()
    flattened_sum = np.sum(list_to_array).tolist()

    calculations = {
        'mean': [axis1_mean, axis2_mean, flattened_mean],
        'variance': [axis1_variance, axis2_variance, flattened_variance],
        'standard deviation': [axis1_std, axis2_std, flattened_std],
        'max': [axis1_max, axis2_max, flattened_max],
        'min': [axis1_min, axis2_min, flattened_min],
        'sum': [axis1_sum, axis2_sum, flattened_sum]
    }

    return calculations
