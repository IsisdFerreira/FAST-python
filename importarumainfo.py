import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')
print(df_pokemon.loc['Legendary'] == True)