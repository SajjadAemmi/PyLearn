import pandas as pd


my_dict = {'name': ["Ali", "Benyamin", "Maryam"], 
           'age': [22, 24, 23]}

my_data_frame = pd.DataFrame.from_dict(my_dict)
print(my_data_frame)
