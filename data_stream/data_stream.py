import time
import numpy as np
from config import config as cfg


class DataStream:
    """
    A class to simulate a data stream of temperature readings.

    Attributes
    ----------
    average_temperature : float
       Initial average temperature from which the temperature will fluctuate.
    temperature_deviation : float
       The standard deviation used to generate temperature variations.
    noise_deviation : float
       The standard deviation for generating random noise.
    sin_amplitude : float
       The amplitude of the sinusoidal wave added to the temperature readings to simulate seasonal changes.
    day : int
       A counter to track the current day in the data stream.
    delay : float
       Delay in seconds between consecutive data readings.

    Methods
    -------
    start_data_stream() -> generator:
       Initiates the data stream and yields generated temperature readings.
    _generate_sin_wave() -> float:
       Generates a sinusoidal variation based on the current day.
    _generate_temperature() -> float:
       Generates a temperature value using a normal distribution.
    _generate_random_noise() -> float:
       Generates random noise using a normal distribution.
    """
    def __init__(self, average_temperature: float=cfg.AVERAGE_TEMPERATURE,
                 temperature_deviation: float=cfg.TEMPERATURE_DEVIATION, noise_deviation: float=cfg.NOISE_DEVIATION,
                 sin_amplitude: float=cfg.SIN_AMPLITUDE, delay: float=cfg.DELAY):
        if temperature_deviation < 0:
            raise ValueError("temperature_deviation must be non-negative.")
        if noise_deviation < 0:
            raise ValueError("noise_deviation must be non-negative.")
        if sin_amplitude < 0:
            raise ValueError("sin_amplitude must be non-negative.")
        self.average_temperature = average_temperature
        self.temperature_deviation = temperature_deviation
        self.noise_deviation = noise_deviation
        self.sin_amplitude = sin_amplitude
        self.day = 0
        self.delay = delay

    def start_data_stream(self):
        """
        Starts generating a continuous data stream of temperature readings.

        Yields
        -------
        float
            The generated temperature reading influenced by sinusoidal variation, random noise, and a normally
            distributed temperature.
        """
        try:
            # Data stream is continuous, therefore it never ends.
            while True:

                # Generate temperature using all variables.
                random_value = self._generate_sin_wave() + self._generate_temperature() + self._generate_random_noise()

                # Yield said value, which makes this function a generator.
                yield random_value

                # Wait the specified delay until next point is calculated.
                time.sleep(self.delay)

                # Simulate all days in a year
                self.day += 1
                if self.day >= cfg.MAX_NUMBER_OF_VALUES:
                    self.day = 0
        except Exception as e:
            print(f"Something went wrong starting the data stream. More information: {e}")

    def _generate_sin_wave(self) -> float:
        """
        Generates a sinusoidal variation based on the current day.

        Returns
        -------
        float
            The value of the sinusoidal component for the current day.
        """
        if cfg.MAX_NUMBER_OF_VALUES <= 0:
            raise ValueError("MAX_NUMBER_OF_VALUES inside file config.py must be greater than zero.")
        max_radian_value = np.pi * 2
        radians_per_day = max_radian_value / cfg.MAX_NUMBER_OF_VALUES / 2
        result = self.sin_amplitude * np.sin(radians_per_day * self.day)
        return result

    def _generate_temperature(self) -> float:
        """
        Generates a temperature value using a normal distribution.

        Returns
        -------
        float
            A temperature value sampled from a normal distribution centered around the
            average temperature with specified deviation.
        """
        temperature = np.random.normal(self.average_temperature, self.temperature_deviation)
        return temperature

    def _generate_random_noise(self) -> float:
        """
        Generates random noise using a normal distribution.

        Returns
        -------
        float
            A noise value sampled from a normal distribution with a mean of 0
            and the specified deviation.
        """
        noise = np.random.normal(0, self.noise_deviation)
        return noise
