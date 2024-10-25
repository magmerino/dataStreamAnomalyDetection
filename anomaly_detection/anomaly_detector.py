import numpy as np
import config.config as cfg


class AnomalyDetector:
    """
    A class to detect anomalies in a time series data using a z-score method.

    Attributes
    ----------
    window_size : int
        The number of recent data points to consider for calculating the moving mean and standard deviation.
    threshold : float
        The threshold value for the z-score to determine whether a data point is considered an anomaly or not.

    Methods
    -------
    is_anomaly(data: list) -> bool:
        Determines if the last value in the provided data list is an anomaly.
    """
    def __init__(self, window_size: int = cfg.WINDOW_SIZE, threshold: float = cfg.THRESHOLD):
        self.window_size = window_size
        self.threshold = threshold

    def is_anomaly(self, data: list) -> bool:
        """
        Determines whether the most recent value in the data list is an anomaly using a z-score method.

        Parameters
        ----------
        data : list
            A list of float values

        Returns
        -------
        bool
            True if the value is an anomaly, False otherwise
        """
        try:
            # At least two values are needed to generate a standard deviation.
            if len(data) < 2:
                return False
            else:

                # extract the last value of the data list.
                current_value = data[-1]

                # Calculate mean, standard deviation and deviation of current value using NumPy.
                moving_mean = np.mean(data[-self.window_size:])
                moving_std = np.std(data[-self.window_size:])
                deviation = current_value - moving_mean

                # Control division by zero
                if moving_std != 0:

                    # Generate z-score using its formula
                    z_score = deviation / moving_std

                    # Compare z-score against the threshold. If z-score is greater, we have an anomaly.
                    result = abs(z_score) > self.threshold
                    return result
                else:
                    return False
        except Exception as e:
            print(f"Something went wrong detecting anomalies. More information: {e}")
            return False