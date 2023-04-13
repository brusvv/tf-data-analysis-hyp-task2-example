import pandas as pd
import numpy as np


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    return anderson_ksamp([x, y]).significance_level < 0.06
