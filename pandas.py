import pandas as pd

# Necessita do arquivo para ver o resultado 
manaus_df = pd.read_csv('/content/drive/MyDrive/base_cida/BaseManaus1.CSV', encoding='latin1', sep=';', decimal=",")
display(manaus_df)