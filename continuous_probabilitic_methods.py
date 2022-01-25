import pandas as pd
import numpy as np


def get_lower_and_upper_bounds(series,k):
    '''
    Function to define the lower and upper bounds of numpy series ('series'), multiplier k
    '''
    # set default multiplier. this code isn't working at the moment...
    # if k is None:
    #     k == 1.5
    # define upper and lower quartiles
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    # define interquartile range
    iqr = q3 - q1
    # calculate upper and lower limits for the whiskers
    inner_lower_fence = q1 - (k * iqr)
    inner_upper_fence = q3 + (k * iqr)
    # return the above variables to call in a notebook
    return inner_lower_fence, inner_upper_fence