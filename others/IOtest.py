import time

from tobiiresearch.interop import interop
import numpy as np
import csv
import pandas as pd
import datetime
data_list = []


def store():
    tmp = list()
    timestamp = int(interop.get_system_time_stamp())
    tmp.append(timestamp)

    tmp.append(np.random.randint(1, 6))
    tmp.append(np.random.randint(1, 6))
    data_list.append(tmp)


for i in range(10):
    store()

with open('../data/IOtest.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'left gaze point', 'right gaze point'])
    writer.writerows(data_list)

data = pd.read_csv('../data/IOtest.csv')
print(data)

