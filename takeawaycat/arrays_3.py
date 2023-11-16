import numpy as np

def convert_to_base_n(fraction, n, precision):
    lower_bound = np.array([0 for _ in range(precision)])
    upper_bound = np.array([n - 1 for _ in range(precision)])

    while True:
        digit = 0
        for i in range(len(lower_bound) - 1, -1, -1):
            midpoint = (lower_bound[i] + upper_bound[i]) / 2
            new_lower_bound = np.array([lower_bound[i] for _ in range(precision)])
            new_upper_bound = np.array([upper_bound[i] for _ in range(precision)])

            if fraction * n < midpoint:
                new_upper_bound[i] = midpoint
            else:
                new_lower_bound[i] = midpoint
                digit += 1

        lower_bound = new_lower_bound
        upper_bound = new_upper_bound

        if np.all(upper_bound - lower_bound <= 1):
            if lower_bound[-1] <= upper_bound[-1]:
                return lower_bound[-1]  # All digits are correct
            else:
                # The last digit is not fully accurate
                return lower_bound[-1] - 1

