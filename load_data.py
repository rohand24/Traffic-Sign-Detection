from __future__ import division
import pickle as pkl

with open('/home/rnd7528/git/darkflow/data_raw_400x260.pkl', 'rb') as f:
	data = pkl.load(f)
	
print(data[2])