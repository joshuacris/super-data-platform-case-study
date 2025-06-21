# .py file combining the code used to complete the challenge from "solution_joshua_crisologo.ipynb"

import pandas as pd
from io import StringIO
import regex as re

# Stringified table from challenge
data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

# Reading into a Pandas Dataframe using StringIO
df = pd.read_csv(StringIO(data), delimiter=';')

# Using df.iterrows() to edit the current FlightCodes value based on the last + 10, skipping the first row
for i, row in df.iterrows():
    if i > 0:
        df.loc[i, 'FlightCodes'] = df.loc[i - 1]['FlightCodes'] + 10

# Setting the column to an integer column
df['FlightCodes'] = df['FlightCodes'].astype(int)

# Splitting To_From column into two separate columns, "To" and "From", splitting on '_' and converting it to capital case
df['To'] = df['To_From'].apply(lambda x: x.upper().split('_')[0])
df['From'] = df['To_From'].apply(lambda x: x.upper().split('_')[1])

# Drop original column
df = df.drop(columns=['To_From'])

# Lastly, use regex to clean the Airline Codes to have no punctuation except spaces in the middle. 
# We clean so that "\<Air France\> (12)" becomes Air France
df['Airline Code'] = df['Airline Code'].apply(lambda x: re.sub(r'[^A-Za-z]+', ' ', x).strip())

# Final dataframe results, both as a pandas dataframe and in the original stringified table form
print(df.to_csv(sep=';', index=False))