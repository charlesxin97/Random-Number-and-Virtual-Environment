#%%
import random
import json
import matplotlib.pyplot as plt
with open("a_json.json",'r') as load_f:
    sample_a=json.load(load_f)
with open("b_json.json",'r') as load_f:
    sample_b=json.load(load_f)

plt.plot(sample_a, sample_b, color='blue')
plt.title("visualization")
plt.xlabel("index")
plt.ylabel("value")
plt.savefig("c.png")
plt.show()
# %%
