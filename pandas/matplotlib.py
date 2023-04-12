import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [1000, 1500, 2000, 2500, 3000]}
df = pd.DataFrame(data)

# Creating a bar chart of the data
plt.bar(df['Year'], df['Sales'])
plt.title('Sales by Year')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()
