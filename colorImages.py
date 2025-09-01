from skimage import color, io, measure
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom

from grayscale import im_name

in_dir = "Images/"
im_name = "ardeche.jpg"

im_org = io.imread(in_dir + im_name)
print(im_org.shape)
print(im_org.dtype)

io.imshow(im_org)
io.show()