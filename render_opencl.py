# ==========================================
# OpenCL Renderer for Mandelbrot Fractals
# ==========================================
#
# This module sets up the OpenCL context, compiles the Mandelbrot kernel,
# executes it on the GPU, and retrieves the result into a NumPy array.
#

import pyopencl as cl
import numpy as np


def render_mandelbrot_opencl(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Render a Mandelbrot set image using OpenCL GPU acceleration.

    Parameters:
        width (int): Width of the output image in pixels
        height (int): Height of the output image in pixels
        x_min, x_max (float): Range of x coordinates (real axis)
        y_min, y_max (float): Range of y coordinates (imag axis)
        max_iter (int): Max iterations for Mandelbrot computation

    Returns:
        numpy.ndarray: 2D array of iteration counts for each pixel
    """

    # Select first available OpenCL platform and device (e.g., AMD GPU)
    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]

    # Create context (GPU execution environment) and command queue
    ctx = cl.Context([device])
    queue = cl.CommandQueue(ctx)

    # Load kernel source from external .cl file
    with open("mandelbrot_kernel.cl", "r") as f:
        kernel_src = f.read()

    # Build (compile) the kernel program
    program = cl.Program(ctx, kernel_src).build()

    # Allocate memory buffer on the GPU for output image
    output_np = np.zeros((height * width,), dtype=np.int32)
    output_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, output_np.nbytes)

    # Define global work size = image dimensions
    global_size = (width, height)

    # Execute kernel (each pixel computed in parallel on GPU)
    program.mandelbrot(
        queue, global_size, None,
        output_buf,
        np.int32(width),
        np.int32(height),
        np.float32(x_min),
        np.float32(x_max),
        np.float32(y_min),
        np.float32(y_max),
        np.int32(max_iter)
    )

    # Copy results back from GPU into NumPy array
    cl.enqueue_copy(queue, output_np, output_buf)

    # Reshape 1D array into 2D image
    output_np = output_np.reshape((height, width))
    return output_np
