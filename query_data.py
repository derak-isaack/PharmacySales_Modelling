import sqlite3  
from IPython.display import display  
import pandas as pd


conn2 = sqlite3.connect('hospi_sales.db')
c2 = conn2.cursor()
data = c2.execute("SELECT * FROM sales").fetchall()
df = pd.DataFrame(data)
display(df) 
