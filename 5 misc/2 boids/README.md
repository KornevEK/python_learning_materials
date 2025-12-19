An implementation of the boids algorithm with varying optimizations, refinement, complexity.

The number of boids is specified in arg, default is 20.

ver1 is the most basic.
ver2 introduces jit for the lenght computation.
ver3 jits the whole update step, therefore the fastest.
ver4 allows for live varying parameters, slower than ver3.
