from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

base_path = "./pcv_data/"
file_name = "empire.jpg"

im = np.array(Image.open(base_path + file_name))
plt.imshow(im)

print("Click 3 points")
x = plt.ginput(3)
print(f"Clicked 3 points {x}")
plt.show()