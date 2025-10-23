import pandas as pd
import numpy as np
data = {'Age': [25, np.nan, 30, 22, np.nan],'Locality': ['Dwarka', 'Rohini', np.nan, 'Azadpur', 'Mundka']}
df = pd.DataFrame(data)
print("Original Data:\n", df)
age_values = [x for x in df['Age'] if not pd.isnull(x)]
mean_age = sum(age_values) / len(age_values)
df['Age_Imputed'] = [x if not pd.isnull(x) else mean_age for x in df['Age']]
locality_values = [x for x in df['Locality'] if not pd.isnull(x)]
mode_locality = max(set(locality_values), key=locality_values.count)
df['Locality_Imputed'] = [x if not pd.isnull(x) else mode_locality for x in df['Locality']]
print("\nAfter Manual Imputation:\n", df)

