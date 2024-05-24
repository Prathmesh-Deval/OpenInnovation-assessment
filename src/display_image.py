# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def display_image(df):
#     pixel_values = df.drop(columns=['depth'])
#
#     pixel_array = pixel_values.to_numpy()
#
#     pixel_array = pixel_array.astype(np.uint8)
#
#     plt.imshow(pixel_array, cmap='gray', aspect='auto')
#     plt.colorbar()
#     plt.title('Image Display from CSV Data')
#     plt.show()
#
#
# data_original = pd.read_csv('/Users/prdeval/Desktop/Projects/openinnovation/src/data/img.csv')
# data_resized = pd.read_csv('/Users/prdeval/Desktop/Projects/openinnovation/src/data/resized_image_data.csv')
#
# display_image(data_resized)
# display_image(data_original)
#
