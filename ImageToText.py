# import matplotlib.pyplot as plt
# import cv2
import easyocr
from pylab import rcParams
# from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])
output = reader.readtext('test.jpg')
for subout in output:
    print(subout[1])