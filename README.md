# GPU Fractal Explorer

An **interactive Mandelbrot & Julia fractal explorer** accelerated with **OpenCL GPU computing** and built with Python.  
This project highlights how **parallel programming** can transform computationally heavy problems into **real-time, interactive experiences**.

---

## 🚀 Project Overview

Fractals like the Mandelbrot and Julia sets are beautiful but computationally expensive.  
Each pixel in the image requires hundreds or thousands of iterations to determine whether it belongs to the fractal set.  

This project leverages:
- **OpenCL** for GPU parallelism  
- **NumPy & Matplotlib** for data handling and visualization  
- **PyQt5 GUI (planned)** for interactive exploration  

---

## 🎯 Purpose

- Showcase **GPU programming skills** using OpenCL.  
- Demonstrate how **parallel computing** delivers real-world performance gains (~20× faster than CPU).  
- Provide a **visual, interactive, and engaging project** that blends math, computer science, and engineering.  

---

## 🔑 Features

- Render **Mandelbrot and Julia sets** at arbitrary resolutions.  
- Support for **zooming** into regions of interest (e.g., Seahorse Valley).  
- **Performance benchmarking** comparing CPU vs GPU.  
- Ready for extension into an **interactive GUI**.  

---

## 📊 Results

See results.md for more specific information.  
Sample images include:  
- Default Mandelbrot

- <img width="723" height="723" alt="mandelbrot_default" src="https://github.com/user-attachments/assets/afef228d-d5c9-45da-9608-5ece110bfc50" />

- Zoomed-in Mandelbrot regions  

- <img width="723" height="723" alt="mandelbrot_zoom1" src="https://github.com/user-attachments/assets/f08b0ed0-87fb-454e-8013-e0af83408850" />

- Julia sets with different parameters  

- <img width="723" height="723" alt="julia_c_-0 7+0 27015i" src="https://github.com/user-attachments/assets/da90d1a2-d21b-4ad1-8a9c-7b6b70dd20b5" />

- Benchmark plots comparing CPU vs GPU  

- <img width="923" height="709" alt="performance_plot" src="https://github.com/user-attachments/assets/66ad1263-cb22-44ec-b310-deff066ccaa5" />

---

## 🌍 Potential Applications

- **Education:** Teaching parallel programming, numerical stability, and fractals in computer science.  
- **Visualization:** Generating mathematical art for creative industries.  
- **Performance Demonstration:** A clear case study of why GPU acceleration matters in engineering.  
- **Portfolio Value:** Strong demonstration of technical depth in **computer engineering, HPC, and visualization**.  

---

## 🛠️ Tech Stack

- **Python 3**  
- **OpenCL (via PyOpenCL)**  
- **NumPy & Matplotlib**  
- (Optional) **PyQt5 for GUI**  

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/gpu-fractal-explorer.git
cd gpu-fractal-explorer
pip install -r requirements.txt
