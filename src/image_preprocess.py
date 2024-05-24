# import pandas as pd
# from skimage.transform import resize
# import sqlite3
#
# original_df = pd.read_csv('/Users/prdeval/Desktop/Projects/openinnovation/src/data/img.csv')
#
# print(original_df.head(), "\n")
# print(f"Original image data shape: {original_df.shape}")
#
#
# def resize_image_row(row, target_width=150):
#     return resize(row, (target_width,), anti_aliasing=True)
#
#
# pixel_columns = original_df.columns[1:]
# resized_pixels = original_df[pixel_columns].apply(lambda row: resize_image_row(row.values), axis=1)
#
# resized_pixels_df = pd.DataFrame(resized_pixels.tolist(), columns=[f'col{i+1}' for i in range(150)])
# resized_df = pd.concat([original_df[['depth']], resized_pixels_df], axis=1)
#
# resized_df.dropna(inplace=True)
#
# print(f"Resized image data shape: {resized_df.shape}")
#
# resized_df.to_csv('resized_image_data.csv', index=False)
#
# conn = sqlite3.connect('image_data.db')
# cursor = conn.cursor()
#
# columns = ['depth REAL'] + [f'col{i+1} REAL' for i in range(150)]
# create_table_query = f"CREATE TABLE IF NOT EXISTS resized_images ({', '.join(columns)});"
#
# cursor.execute(create_table_query)
# resized_df.to_sql('resized_images', conn, if_exists='replace', index=False)
#
# # Commit the changes and close the connection
# conn.commit()
# print("*****")
# query = "SELECT * FROM resized_images"
# df_from_db = pd.read_sql_query(query, conn)
# conn.close()
#
# print("Data read from database:")
# print(df_from_db)
