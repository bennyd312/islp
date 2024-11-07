import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

college = pd.read_csv('College.csv')
college2 = pd.read_csv('College.csv', index_col=0)

college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')

college = college3


#numerical summary of a dataset
college.describe()

#print(college[['Top10perc','Apps','Enroll']])
#print(type(college[['Top10perc','Apps','Enroll']]))

pd.plotting.scatter_matrix(college[['Top10perc','Apps','Enroll']])
plt.show()
