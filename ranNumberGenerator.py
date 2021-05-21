from random import randrange
import json
import matplotlib.pyplot as plt

i = 0
numList = []
labels = []
while i < 1000:
    numList.append(randrange(0, 100, 1))
    i += 1
    labels.append(i)

print(numList)
print(len(numList))

with open('data.json', 'w') as outfile:
    json.dump(numList, outfile)

plt.bar(labels, numList)
plt.savefig('bar_out.png', dpi=400)
plt.show()

