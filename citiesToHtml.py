import pandas as pd 

file = "Resources/cities.csv"
df = pd.read_csv(file)
df.to_html("citiesTable.html", index=False, justify="left")