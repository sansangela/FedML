from fileinput import filename
import re
import matplotlib.pyplot as plt
import numpy as np

file_name = '0906.log'

t_array = []
train_loss_results = []

counter = 0
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        if 'Epoch: 9' in line:
            counter += 1
            m = re.match(r'(.*)Loss: (.*)', line)
            t_array.append(counter)
            train_loss_results.append((float)(m.group(2)))


print(train_loss_results)
plt.figure(1)
plt.plot(t_array,train_loss_results,'-')
# ax = plt.gca()
# ax.invert_yaxis()
# ax.axes.yaxis.set_ticklabels([])
# plt.yticks(np.arange(0, max(train_loss_results), 0.1))
plt.title('train loss vs round')
plt.savefig('train loss vs round.png')
