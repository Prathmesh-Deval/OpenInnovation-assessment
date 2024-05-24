import pandas as pd
import cv2
import matplotlib.pyplot as plt

csv_file = "/Users/prdeval/Desktop/Projects/openinnovation/src/data/img.csv"
df = pd.read_csv(csv_file)
df = df.dropna()

depth = df["depth"]
pixels = df.drop(columns=["depth"])

new_width = 150
resized_pixels = []
for idx, row in pixels.iterrows():
    img_array = row.values.astype('uint8')
    img_reshaped = img_array.reshape(10, 20)

    resized_img = cv2.resize(img_reshaped, (new_width, 10), interpolation=cv2.INTER_CUBIC)
    resized_pixels.append(resized_img.flatten())

resized_df = pd.DataFrame(resized_pixels)
resized_image_data = pd.concat([depth, resized_df], axis=1)

resized_csv_file = "/Users/prdeval/Desktop/Projects/openinnovation/src/data/resized_image_data.csv"
resized_image_data.to_csv(resized_csv_file, index=False)

print(resized_image_data)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(pixels.values, cmap='gray', aspect='auto', extent=[0, 200, 9000.2, 9546.0])
axs[0].set_title('Original Image')
axs[0].set_xlabel('Pixel Value')
axs[0].set_ylabel('Depth')
axs[0].set_ylim([9000.2, 9546.0])

axs[1].imshow(resized_df.values, cmap='gray', aspect='auto', extent=[0, new_width, 9000.2, 9546.0])
axs[1].set_title('Resized Image')
axs[1].set_xlabel('Pixel Value')
axs[1].set_ylabel('Depth')
axs[1].set_ylim([9000.1, 9546.0])

plt.tight_layout()
plt.show()
