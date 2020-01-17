import pandas as pd
import Columns as CL


def vw_aggr(group, col_name):
    """ function calculates volume weighted  average for column
    :param group - GroupByDataframe  -rows split by aggregation key
    :param col_name -  name of column to use in volume weighted averaging
    :return -  result of calculation
    """
    value = group[col_name]
    weight = group[CL.WEIGHT]
    wv = (value * weight).sum()
    return wv


