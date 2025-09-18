// ======================================
// Mandelbrot Kernel in OpenCL
// ======================================
//
// This kernel computes the Mandelbrot set using GPU parallelism.
// Each thread (work-item) corresponds to a single pixel in the image.
// For each pixel, we iterate the formula z = z^2 + c and determine
// how many iterations it takes for the value to escape.
//
// Inputs:
//   output   - array of ints storing iteration counts (one per pixel)
//   width    - image width in pixels
//   height   - image height in pixels
//   x_min    - minimum x coordinate of the viewport
//   x_max    - maximum x coordinate of the viewport
//   y_min    - minimum y coordinate of the viewport
//   y_max    - maximum y coordinate of the viewport
//   max_iter - maximum iterations before bailout
//
// Outputs:
//   output[j * width + i] = number of iterations before escape
//
__kernel void mandelbrot(
    __global int *output,
    const int width,
    const int height,
    const float x_min,
    const float x_max,
    const float y_min,
    const float y_max,
    const int max_iter)
{
    // Get pixel coordinates for this thread
    int i = get_global_id(0); // column index
    int j = get_global_id(1); // row index

    // Bounds check to avoid extra threads writing out of range
    if (i >= width || j >= height) return;

    // Map pixel (i, j) to complex plane (x0 + iy0)
    float x0 = x_min + i * (x_max - x_min) / (width - 1);
    float y0 = y_min + j * (y_max - y_min) / (height - 1);

    // Start iteration from z = 0
    float x = 0.0f;
    float y = 0.0f;
    int iter = 0;

    // Mandelbrot iteration loop
    while (x*x + y*y <= 4.0f && iter < max_iter) {
        float xt = x*x - y*y + x0; // real part
        y = 2.0f*x*y + y0;         // imag part
        x = xt;
        iter++;
    }

    // Store result (number of iterations before escape)
    output[j * width + i] = iter;
}
