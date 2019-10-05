import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
first_list = np.array([5,7,4,7,5,8,4,2])
second_list = np.array([63, 8, 6, 7, 2, 4, 53, 53])
list = pd.read_csv('DSC IMSU.csv',index_col=None)
evaluate = list['GENDER']
# evaluate_again = list['STATE']
data = [x for x in evaluate]
np.array(data)
print(data)

two = np.vstack((first_list,second_list))
_ = plt.hist(data)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.gca().legend(('first_list','second_list'))
plt.margins(0.1)
plt.show()