import cv2
img = cv2.imread("image/accesdenied.png", cv2.IMREAD_COLOR)
cv2.imshow("Acces Denied!", img)
cv2.waitKey(0)
cv2.destroyAllWindows()