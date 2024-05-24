import pandas as pd
import sqlite3

resized_df = pd.read_csv('/Users/prdeval/Desktop/Projects/openinnovation/src/data/resized_image_data.csv')

conn = sqlite3.connect('image_data.db')
cursor = conn.cursor()

columns = ['depth REAL'] + [f'col{i+1} REAL' for i in range(150)]
create_table_query = f"CREATE TABLE IF NOT EXISTS resized_images ({', '.join(columns)});"

cursor.execute(create_table_query)
resized_df.to_sql('resized_images', conn, if_exists='replace', index=False)

conn.commit()
print("*****")
query = "SELECT * FROM resized_images"
df_from_db = pd.read_sql_query(query, conn)
conn.close()

print("Data read from database:")
print(df_from_db)
