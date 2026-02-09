import cv2

source = "Santorini.jpg"
destination = "New_Image.jpg"

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("Hello", res)

# Percent by which image is resized
scale_percent = 50

# Calculate scale_percent of original dimensions
new_height = int(src.shape[0] * scale_percent / 100)
new_width = int(src.shape[1] * scale_percent / 100)

# Resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)
