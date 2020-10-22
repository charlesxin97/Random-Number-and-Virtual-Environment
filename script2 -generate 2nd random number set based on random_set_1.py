#%%
import random
import json
with open("a_json.json",'r') as load_f:
    sample_a=json.load(load_f)

sample_b = []
for num in sample_a:
    sample_b.append(num*3+6)
json_b = json.dumps(sample_b)

w = open('random_set_2.json', 'w')
w.write(json_b)
w.close()
print(sample_b)
# %%
