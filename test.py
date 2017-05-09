import pickle
import json

d = dict(name='Bob', age = 20)
d=json.dumps(d)

f= open('dump.txt','wb')
pickle.dump(d,f)
f.close()


