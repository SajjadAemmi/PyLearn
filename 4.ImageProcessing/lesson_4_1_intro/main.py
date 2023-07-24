import cv2

my_image = cv2.imread("nowruz.jpg")
my_image_2 = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

# print(my_image_2)
# print("ابعاد تصویر:", my_image_2.shape)
# print(my_image_2[10, 15])

# my_image_2[0:45, 0:768] = 0 # ضلع بالا
# my_image_2[0:432, 723:768] = 0 # ضلع راست
# my_image_2[0:432, 0:45] = 0 # ضلع چپ
# my_image_2[387:432, 0:768] = 0 # ضلع پایین

tea = my_image_2[270:400, 40:180]
my_image_2[290:420, 370:510] = tea

cv2.imshow("", my_image_2)
cv2.waitKey()
cv2.imwrite("nowruz.jpg", my_image_2)
