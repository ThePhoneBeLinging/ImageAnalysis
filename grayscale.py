from skimage import color, io, measure
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom

# Directory containing data and images
in_dir = "Images/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)
print(im_org.shape)
print(im_org.dtype)

io.imshow(im_org)
plt.title('Metacarpal image')
io.show()

io.imshow(im_org, cmap="hot")
plt.title('Metacarpal image (with colormap)')
io.show()


io.imshow(im_org, vmin=im_org.min(), vmax=im_org.max())
plt.title('Metacarpal image (with gray level scaling)')
io.show()

plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()

h = plt.hist(im_org.ravel(), bins=256)

bin_no = 100
count = h[0][bin_no]
print(f"There are {count} pixel values in bin {bin_no}")

bin_left = h[1][bin_no]
bin_right = h[1][bin_no + 1]
print(f"Bin edges: {bin_left} to {bin_right}")
y, x, _ = plt.hist(im_org.ravel(), bins=256)
print(f"Biggest one = {y.max()}")
print(f"Value at point (110,50): = {im_org[110,50]}")

im_org[:30] = 0
io.imshow(im_org)
io.show()

mask = im_org > 150
io.imshow(mask)
io.show()

im_org[mask] = 255
io.imshow(im_org)
io.show()