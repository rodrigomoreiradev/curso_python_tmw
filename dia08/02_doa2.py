# %%
import requests
import pandas as pd

url = 'https://api.opendota.com/api/heroes'

resp = requests.get(url)

df = pd.DataFrame(resp.json())
df.to_csv('heros_dota_2.csv',sep=';',index=False)