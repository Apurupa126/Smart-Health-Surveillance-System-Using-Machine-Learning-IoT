import pandas as pd
df = pd.read_csv("helath_dataset_multilable_5000.csv")
print(df[df['temperature'] < 99.5]['fever_status'].value_counts())
