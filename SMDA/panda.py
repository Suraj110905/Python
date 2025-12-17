import matplotlib.pyplot as plt
from matplotlib import style
job_data=['12','23','52','28','85','58']
labels='it','finance','marketing','admin','hr','operations'
explode=(0.05,0,0,0,0,0)
plt.pie(job_data,labels=labels,explode=explode)
plt.show()
