import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def main():
    file_path = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\AusApparalSales4thQrt2020.csv'
    load_data()

if __name__ == "__main__":
    main()
