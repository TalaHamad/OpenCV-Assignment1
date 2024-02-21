import cv2
from matplotlib import pyplot as plt
import numpy as np
import sys


def Open_OrginalImg():
    img1 = cv2.imread('BrightImage.jpg', 1)  # read image in the color mode
    cv2.imshow('Colored Image', img1)
    cv2.setWindowProperty('Colored Image', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)


# ----------------------------------------------------

def Grey_Scale():
    img2 = cv2.imread('BrightImage.jpg', 0)  # read the image in the grey scale mode
    cv2.imshow("Grey Scaled Image", img2)
    cv2.setWindowProperty('Grey Scaled Image', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)


# ----------------------------------------------------

def Show_Histo():
    img2 = cv2.imread('BrightImage.jpg', 0)  # read the image in the grey scale mode
    plt.hist(img2.ravel(), 256, [0, 255])  # get the histogram for the image in the gray scale mode
    plt.show()


# ----------------------------------------------------

def Get_HistoValues():
    img2 = cv2.imread('BrightImage.jpg', 0)  # read the image in the grey scale mode

    # we get the mode, mean, median, standard deviation
    # for Dark image mode<median<mean (& Positively skewed)
    # for Bright image mode>median>mean (& negatively skewed)
    # for low or high contract (symmetric skewed)
    # so we check the Std for it. if small (low => narrow range), if large (high => wide range)

    arr = [0 for i in range(256)]

    height = img2.shape[0]
    width = img2.shape[1]

    for x in range(height):  # I get the mode by this method because there is not a function for it.
        for y in range(width):
            index = img2[x, y]
            arr[index] = arr[index] + 1

    mode = arr.index(max(arr))

    mean = np.mean(img2)
    median = np.median(img2)
    std = np.std(img2)

    print("This is the mean value= ", mean)
    print("This is the median value= ", median)
    print("This is the mode value= ", mode)
    print("This is the standard deviation value= ", std)

    plt.hist(img2.ravel(), 256, [0, 255])  # then I polt them in the Histogram:
    plt.xlabel("Yellow= mean, Red= median, Blue= mode")

    plt.axvline(mean, color='y', linestyle='dashed')
    plt.axvline(median, color='r', linestyle='dashed')
    plt.axvline(mode, color='b', linestyle='dashed')
    plt.show()


# ----------------------------------------------------

def Enhance_Manual():
    # Gamma
    # when the Gamma coefficient larger than one, then the bright image will be Enhanced
    img2 = cv2.imread('BrightImage.jpg', 0)
    for gamma in [2.8, 3.4, 4, 4.8]: # the values more than 1
        gam = np.array(255 * (img2 / 255) ** gamma, dtype='uint8')
        cv2.imwrite('Enhance_Manual_Gamma ' + str(gamma) + '.jpg', gam)
        cv2.imshow('Enhance_Manual_Gamma with coefficient ' + str(gamma), gam)
        cv2.setWindowProperty('Enhance_Manual_Gamma with coefficient ' + str(gamma), cv2.WND_PROP_TOPMOST, 1)

    cv2.waitKey(0)


# ----------------------------------------------------
def Enhance_Auto():
    img2 = cv2.imread('BrightImage.jpg', 0)  # read the image in the grey scale mode
    img_enhauto = cv2.equalizeHist(img2)
    cv2.imwrite('Automatically Enhancement.jpg', img_enhauto)
    cv2.imshow('Automatically Enhancement', img_enhauto)
    cv2.setWindowProperty('Automatically Enhancement', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)


# ----------------------------------------------------
def Exit():
    sys.exit()


print("Tala Hamad 11926033 - Image Processing assignment #1")
print("Please choose one of the following methods to apply it on the input image:\n"
      "      - Open the image in color input image  ( expected input <= o )\n"
      "      - Converting image to grey-Scale ( expected input <= g ) \n"
      "      - Show the histogram of the image ( expected input <= s ) \n"
      "      - Print Features/values that can be useful to identify the shape of the histogram ( expected input <= p ) , \n"
      "      - Enhance the contrast of the image Manually ( expected input <= m ) \n"
      "      - Enhance the contrast of the image Automatically ( expected input <= a ) \n"
      "      - Exit ( expected input <= e) \n")

Methods = {
    'O': Open_OrginalImg,
    'G': Grey_Scale,
    'S': Show_Histo,
    'P': Get_HistoValues,
    'M': Enhance_Manual,
    'A': Enhance_Auto,
    'E': Exit
}

User_in = input("Please enter Your Choice: ").upper()
count = 0
flag = 0
while True:
    for x in Methods:
        if User_in == x:
            count = count + 1

    if count == 0 and flag == 0:
        User_in = input("Please enter a Valid Choice: ").upper()

    elif flag==1:
            count = 0
            flag = 0
            print("\n""Do you want to continue [Y/N] : ", end='')
            User_dec = input().upper()
            if (User_dec.__eq__('N')):
             print("Okay, thank you")
             sys.exit()

            elif (User_dec.__eq__('Y')):
                     User_in = input("Please enter Your Choice: ").upper()
            else:
                flag=1
                print("You have entered wrong input, Please try Again ..")

    elif flag == 0:
        count = 0
        Methods.get(User_in)()
        print("\n""Do you want to continue [Y/N] : ", end='')
        User_dec = input().upper()
        if (User_dec.__eq__('N')):
            print("Okay, thank you")
            sys.exit()

        elif (User_dec.__eq__('Y')):
            User_in = input("Please enter Your Choice: ").upper()
        else:
            flag = 1
            print("You have entered wrong input, Please try Again ..")


