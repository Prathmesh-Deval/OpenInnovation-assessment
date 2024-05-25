import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt

csv_file = "/Users/prdeval/Desktop/Projects/openinnovation/app/data/img.csv"
df = pd.read_csv(csv_file)
df = df.dropna()

depth = df["depth"]
pixels = df.drop(columns=["depth"])

new_width = 150
resized_pixels = []

for idx, row in pixels.iterrows():
    img_array = row.values.astype('uint8')
    img_reshaped = img_array.reshape(1, -1)

    resized_img = cv2.resize(img_reshaped, (new_width, 1), interpolation=cv2.INTER_CUBIC)
    resized_pixels.append(resized_img)

resized_np_array = np.vstack(resized_pixels)

resized_image_data = pd.DataFrame(np.hstack((depth.values.reshape(-1, 1), resized_np_array)))

resized_csv_file = "/Users/prdeval/Desktop/Projects/openinnovation/app/data/resized_image_data.csv"
resized_image_data.to_csv(resized_csv_file, index=False, header=['depth'] + [f'col{i}' for i in range(resized_np_array.shape[1])])

print(resized_image_data)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(pixels.values, cmap='gray', aspect='auto', extent=[0, len(pixels.columns), depth.iloc[-1], depth.iloc[0]])
axs[0].set_title('Original Image')
axs[0].set_xlabel('Pixel Value')
axs[0].set_ylabel('Depth')

axs[1].imshow(resized_np_array, cmap='gray', aspect='auto')
axs[1].set_title('Resized Image')
axs[1].set_xlabel('Pixel Value')
axs[1].set_ylabel('Depth')

plt.tight_layout()
plt.show()
