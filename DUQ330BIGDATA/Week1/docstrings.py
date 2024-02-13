from typing import Union
import pandas as pd


def add (a: int or float, b: int or float) -> Union[int, float]:
    """
    args:
    a: number 1
    b: number 2

    :return:
    Ouput of addition of numbers 1 and 2
    """
    return a + b

def create_new_dataframe() -> pd.DataFrame:
    """
    returns:
    pd.DataFrame: dataframe containing dummy data
    """
    return pd.DataFrame([1,2,3], [4,5,6], [7,8,9], [10,11,12])

