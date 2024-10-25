import matplotlib.pyplot as pypl
from config import config as cfg


class Visualization:
    """
    A class to handle the visualization of data points in a dynamic plot using Matplotlib.

    Attributes
    ----------
    max_points : int
        The maximum number of points to display on the plot at any given time.
    point_size : int
        The size of the points plotted on the graph.
    fig : matplotlib.figure.Figure
        The figure object for the plot.
    ax : matplotlib.axes.Axes
        The axes object for the plot.
    x_values : list
        A list to store x-coordinates of the points.
    y_values : list
        A list to store y-coordinates of the points.
    colors : list
        A list to store the color of each point. Blue means not anomaly. Red means anomaly.

    Methods
    -------
    update_value(x: float, y: int, is_anomaly: bool):
        Updates the plot with a new data point, redrawing the graph.
    show_plot():
        Displays the plot in a blocking manner.
    """
    def __init__(self, max_points=cfg.MAX_NUMBER_OF_VALUES, point_size=cfg.PLOT_POINT_SIZE):
        if not isinstance(max_points, int) or max_points <= 0:
            raise ValueError("MAX_NUMBER_OF_VALUES inside configuration file must be a positive integer.")
        if not isinstance(point_size, (int, float)) or point_size <= 0:
            raise ValueError("Point size inside configuration file must be a positive number.")
        self.max_points = max_points
        self.point_size = point_size
        self.fig, self.ax = pypl.subplots()
        self.ax.set_xlim(0, self.max_points)  # Assuming x range is known
        self.ax.set_ylim(cfg.Y_AXIS_MIN_VALUE, cfg.Y_AXIS_MAX_VALUE)
        self.x_values = list()
        self.y_values = list()

        self.colors = list()  # List to store the color of each point
        self.ax.set_xlabel(cfg.X_AXIS_LABEL)
        self.ax.set_ylabel(cfg.Y_AXIS_LABEL)

        pypl.ion()  # Enable interactive mode
        pypl.show()

    def update_value(self, x: float, y: int, is_anomaly: bool):
        """
        Updates the plot with a new data point, adjusting the colors based on whether
        the point is considered an anomaly.

        Parameters:
        ----------
        x : float
            The x-coordinate of the point to be added to the plot.
        y : int
            The y-coordinate of the point to be added to the plot.
        is_anomaly : bool
            A boolean indicating whether the point is an anomaly. If True, the point is colored red;
            otherwise, it is colored blue.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a numeric type.")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a numeric type.")

        # Append x and y values.
        self.x_values.append(x)
        self.y_values.append(y)

        # Assign the color based on the boolean condition.
        if is_anomaly:
            self.colors.append('red')
        else:
            self.colors.append('blue')

        # Keep the length of the plot within the max_points limit.
        if len(self.x_values) > self.max_points:
            self.x_values.pop(0)
            self.y_values.pop(0)
            self.colors.pop(0)

        # Re-plot with updated values.
        self.ax.cla()
        self.ax.set_xlim(0, self.max_points)
        self.ax.set_ylim(cfg.Y_AXIS_MIN_VALUE, cfg.Y_AXIS_MAX_VALUE)
        self.ax.set_xlabel(cfg.X_AXIS_LABEL)
        self.ax.set_ylabel(cfg.Y_AXIS_LABEL)

        # Scatter the points.
        try:
            self.ax.scatter(self.x_values, self.y_values, c=self.colors, s=self.point_size)
        except Exception as e:
            print(f"Error during plotting. More information: {e}")
        # Pause between drawings.
        pypl.pause(cfg.DELAY)

    def show_plot(self):
        try:
            pypl.show(block=True)
        except Exception as e:
            print(f"Error displaying the plot: {e}")