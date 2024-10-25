from data_stream.data_stream import DataStream
from anomaly_detection.anomaly_detector import AnomalyDetector
from visualization.visualization import Visualization
from config import config as cfg

def start_process(size=cfg.MAX_NUMBER_OF_VALUES):
    data_stream = DataStream()
    stream = data_stream.start_data_stream()
    anomaly_detector = AnomalyDetector()
    data = list()
    value_plot = Visualization()
    for i in range(1, size + 1):
        current_value = next(stream)
        data.append(current_value)
        is_anomaly = anomaly_detector.is_anomaly(data)
        value_plot.update_value(x=i, y=current_value, is_anomaly=is_anomaly)
    value_plot.show_plot()

if __name__ == "__main__":
    start_process()


