from lsb import LSBSteg
import cv2

######### TEXT ENCODER    ##########
# steg = LSBSteg(cv2.imread("lion.png"))
# img_encoded = steg.encode_text("FUCK YOU USA")
# cv2.imwrite("lion_encoded.png", img_encoded)

# im = cv2.imread("lion_encoded.png")
# steg = LSBSteg(im)
# print("Text value:",steg.decode_text())

steg = LSBSteg(cv2.imread("nature.png"))
new_im = steg.encode_image(cv2.imread("leaf.png"))
cv2.imwrite("nature_encoded.png", new_im)

