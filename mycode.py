import os
import pandas as pd

data = {
    "name" : ["Aniq","Ali", "Ahad"],
    "City" : ["FSD","Lahore", "Multan"],
    "Age" : [13,15,16]
}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok = True)

file_path = os.path.join(data_dir, "sample.csv")
df.to_csv(file_path,index = False)