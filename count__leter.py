import pandas as pd

def count_letter(string:str) -> tuple:
    try:
        workhorse = string.upper()
        workhorse = list(dict(pd.Series(list(workhorse)).value_counts()).items()) # в этой строке используя функцию value_counts из модуля pandas мы получаем объект состоящий из значения и колличества вохождений
        return max(workhorse)
    except TypeError:
        print('object must be string')
    return None 


if __name__ == '__main__':
    print(count_letter('frefdsgdfsafg'))
    print(count_letter('DAFasdafafsaSSDAFSFA'))
