# -*- coding: utf-8 -*-
"""village.ipynb-Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SI1LetlgvY3rly-fxE-POvyThZOomFp1
"""

!git clone https://github.com/utkarshraaz/DataScience.git

import pandas as pd

district=pd.read_csv('/content/DataScience/census_village_data_at_district_level_Explorin.csv')

district.head()

district.shape

x=district[["state_name","total_population"]]
x

y=district[district["state_name"]=="BIHAR"]
y

district.iloc[202:238, 0:4]

district.loc[202:238,'district_name':'total_population_female']

district.info()

district.isnull().sum()

district.describe()

sex_ratio_district=district.total_population_female/district.total_population_male
sex_ratio_district.describe()

import matplotlib.pyplot as plt
plt.hist(sex_ratio_district,color='pink', bins=10)

district_with_less_ratio=sex_ratio_district.index[sex_ratio_district<=0.8].tolist()
print(district_with_less_ratio)

district_with_less_ratio=district.iloc[district_with_less_ratio]
district_with_less_ratio.head()