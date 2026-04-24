"""Common optimizers."""


import numpy as np
from time import time

def gradient_descent(init, steps, grad, proj=lambda x: x, num_to_keep=None):
    """Projected gradient descent.
    
    Parameters
    ----------
        initial : array
            starting point
        steps : list of floats
            step size schedule for the algorithm
        grad : function
            mapping arrays to arrays of same shape
        proj : function, optional
            mapping arrays to arrays of same shape
        num_to_keep : integer, optional
            number of points to keep
        
    Returns
    -------
        List of points computed by projected gradient descent and the wall clock time it took to compute them. Length of the
        lists is determined by `num_to_keep`.
    """
    xs = [init]
    ts = [0]
    start = time()
    for step in steps:
        xs.append(proj(xs[-1] - step * grad(xs[-1])))
        ts.append(time() - start)
        if num_to_keep:
            xs = xs[-num_to_keep:]
            ts = ts[-num_to_kepp:]
    return xs, ts


def frank_wolfe(initial, update_oracle, num_steps, num_to_keep=None):
    """ Frank-Wolfe.
    
        Frank-Wolfe (Conditional gradient) for first-order optimization.
    
    Parameters:
    -----------
        initial: array,
            initial starting point
        update_oracle: function, mapping points to points, 
            computes the next iterate given the current iterate and iteration number
        num_steps: integer, 
            number of steps to run the algorithm for
    Returns:
    --------
        List of points computed by the algorithm and the wall clock time it took to compute them
    """
    xs = [initial]
    ts = [0]
    start = time()
    for step in range(num_steps):
        xs.append(update_oracle(xs[-1],step))
        ts.append(time() - start)
        if num_to_keep:
            xs = xs[-num_to_keep:]
            ts = ts[-num_to_kepp:]
    return xs, ts