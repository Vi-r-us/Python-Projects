import requests
import pickle

r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
r_text = r.text
r_splited = r_text.splitlines()
final_obj = [[i] for i in r_splited]

with open('Pickled_File.pkl' , 'wb') as f:
    pickle.dump(final_obj,f)

with open('Pickled_File.pkl' , 'rb') as f:
    extracted_data = pickle.load(f)
    print(extracted_data)