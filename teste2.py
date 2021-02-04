
import numpy as np
import cv2 as cv

import sys

def main():
    fn = 'gas1.jpg'

    src = cv.imread(fn)
    img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 5)
    cimg = src.copy() 

    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 69, 21, 9, 26)

    counter = 1
    if circles is not None: 
        _a, b, _c = circles.shape
        for i in range(b):
            cv.circle(cimg, 
            (circles[0][i][0], circles[0][i][1]), 5, (244,246,249), 0, cv.LINE_AA) 
            counter += 1

        print(f'counter ;', counter)
        cv.putText(cimg, "Total de brejas {}".format(counter), (150, 400),
            cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
        cv.imshow("Cervejas na caixa", cimg)

    #cv.imshow("Cervejas na caixa", src)
    cv.waitKey(0)
    print('Done')


if __name__ == '__main__':
    main()
    cv.destroyAllWindows()