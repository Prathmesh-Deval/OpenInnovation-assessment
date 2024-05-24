import pandas as pd
from skimage.transform import resize

original_df = pd.read_csv('/Users/prdeval/Desktop/Projects/openinnovation/src/data/img.csv')

print(original_df.head(), "\n")
print(f"Original image data shape: {original_df.shape}")


def resize_image_row(row, target_width=150):
    return resize(row, (target_width,), anti_aliasing=True)


pixel_columns = original_df.columns[1:]
resized_pixels = original_df[pixel_columns].apply(lambda row: resize_image_row(row.values), axis=1)

resized_pixels_df = pd.DataFrame(resized_pixels.tolist(), columns=[f'col{i+1}' for i in range(150)])
resized_df = pd.concat([original_df[['depth']], resized_pixels_df], axis=1)

resized_df.dropna(inplace=True)

print(f"Resized image data shape: {resized_df.shape}")

resized_df.to_csv('data/resized_image_data.csv', index=False)
