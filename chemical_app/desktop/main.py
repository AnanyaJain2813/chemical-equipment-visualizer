import sys, requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")

        self.btn = QPushButton("Upload CSV")
        self.btn.clicked.connect(self.upload)

        self.fig = Figure(figsize=(5,4))
        self.canvas = FigureCanvasQTAgg(self.fig)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def upload(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select CSV")
        if not path:
            return

        files = {"file": open(path, "rb")}
        r = requests.post("http://127.0.0.1:8000/api/upload/", files=files)
        data = r.json()

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.bar(
            data["type_distribution"].keys(),
            data["type_distribution"].values()
        )
        ax.set_title("Equipment Type Distribution")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec())

