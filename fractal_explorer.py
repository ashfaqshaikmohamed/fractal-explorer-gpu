"""
======================================
Interactive Fractal Explorer (PyQt5)
======================================

This script creates a simple GUI to explore Mandelbrot fractals.
The fractal is computed on the GPU via OpenCL (using render_opencl.py),
and displayed in a PyQt5 window with interactive features.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
from render_opencl import render_mandelbrot_opencl

class FractalExplorer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractal Explorer (OpenCL GPU)")
        self.setGeometry(100, 100, 900, 900)

        # Initial viewport of Mandelbrot set (complex plane)
        self.x_min, self.x_max = -2.0, 1.0
        self.y_min, self.y_max = -1.5, 1.5
        self.width, self.height = 800, 800
        self.max_iter = 500

        # UI Elements
        self.label = QLabel()  # Display fractal image
        self.button_reset = QPushButton("Reset Zoom")  # Reset view button
        self.button_reset.clicked.connect(self.reset_view)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_reset)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initial render
        self.render_fractal()

    def render_fractal(self):
        """Call OpenCL renderer and display fractal image."""
        arr = render_mandelbrot_opencl(
            self.width, self.height,
            self.x_min, self.x_max,
            self.y_min, self.y_max,
            self.max_iter
        )

        # Normalize iteration values to 8-bit grayscale for display
        arr8 = (255 * arr / arr.max()).astype(np.uint8)

        # Create QImage from numpy array
        img = QImage(arr8.data, self.width, self.height, self.width, QImage.Format_Grayscale8)

        # Display fractal in the QLabel
        self.label.setPixmap(QPixmap.fromImage(img))

    def reset_view(self):
        """Reset zoom to original Mandelbrot viewport."""
        self.x_min, self.x_max = -2.0, 1.0
        self.y_min, self.y_max = -1.5, 1.5
        self.render_fractal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FractalExplorer()
    window.show()
    sys.exit(app.exec_())
