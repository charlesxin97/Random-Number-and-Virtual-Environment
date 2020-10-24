#%%
import random
import json
import matplotlib.pyplot as plt
sample_a = []
for i in range(1000):
    sample_a.append(random.randint(0,100))
json_a = json.dumps(sample_a)

w = open('output/random_set_1.json', 'w')
w.write(json_a)
w.close()
print(sample_a)
# %%
