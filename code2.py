# Import the pandas library, renamed as pd 
import pandas as pd 
  
# Read IND_data.csv into a DataFrame, assigned to df 
df = pd.read_csv("IND_data.csv") 
  
# Prints the first 5 rows of a DataFrame as default 
df.head() 
  
# Prints no. of rows and columns of a DataFrame 
df.shape 
