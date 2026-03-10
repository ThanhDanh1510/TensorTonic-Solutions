def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for step in range(steps-1):
        f = 2*a*x0+b
        x0 = x0 - lr*f
    return x0
    pass