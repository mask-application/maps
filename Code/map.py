import geojson
import os
import numpy as np
import cv2

CSVsPath = 'CSVs/'
OneLineCSVsPath = 'OneLineCSVs/'


def drawBorder(dst_cont):
    if not dst_cont.__contains__('.csv'):
        dst_cont += dst_cont

    x = 800
    y = 10
    pos = 0

    im = cv2.imread('pic.png')
    f = open(OneLineCSVsPath + dst_cont, 'r')
    lines = f.readlines()

    for ll in range(len(lines)):
        ln = lines[ll]
        sp = np.array(ln.split(',')[2:], dtype=float)
        mn = min(sp)
        if mn < 20:
            sp += (abs(mn) + 20)
        sp = np.array(sp, dtype=int) * 5
        for i in range(2, len(sp), 2):
            lineThickness = 2
            cv2.line(im, (sp[i - 2], sp[i - 1]), (sp[i], sp[i + 1]), (0, 255, 0), lineThickness)

        ##Write number
        y = 10 + pos * 15
        if y > im.shape[0] - 15:
            x += 30
            pos = 0
            y = 10 + (pos * 15)
        cv2.putText(im, str(ll + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .4, 255, thickness=2)
        pos += 1
        cv2.imshow("ss", im)
        cv2.waitKey()

    cv2.putText(im, 'FINISH', (int(im.shape[0] / 2), int(im.shape[1] / 2)), cv2.FONT_HERSHEY_SIMPLEX, 1, 255,
                thickness=2)
    cv2.imshow("ss", im)
    cv2.waitKey()


def findTheBestBorder():
    FILES = os.listdir(CSVsPath)
    for cntry in FILES:

        pth = CSVsPath + cntry

        # x = 800
        # y = 10
        # pos = 0

        # im = cv2.imread('pic.png')
        f = open(pth, 'r')
        lines = f.readlines()

        max_val = -1
        max_idx = -1
        for ll in range(len(lines)):
            ln = lines[ll]
            sp = np.array(ln.split(',')[2:], dtype=float)
            if len(sp) > max_val:
                max_val = len(sp)
                max_idx = ll

        fwr = open(OneLineCSVsPath + cntry, 'w')
        fwr.write(lines[max_idx])
        f.close()
        fwr.close()
        ##################Draw
        # mn = min(sp)
        # if mn < 20:
        #     sp += (abs(mn)+20)
        # sp = np.array(sp,dtype=int)*5
        # for i in range(2,len(sp),2):
        #     lineThickness = 2
        #     cv2.line(im, (sp[i-2], sp[i-1]), (sp[i], sp[i+1]), (0, 255, 0), lineThickness)
        # ##Write number
        # y = 10 + pos*15
        # if y > im.shape[0]-15:
        #     x+=30
        #     pos = 0
        #     y = 10 + (pos*15)
        # cv2.putText(im, str(ll+1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .4, 255, thickness=2)
        # pos+=1
        # cv2.imshow("ss", im)
        # cv2.waitKey()
        #
        # cv2.putText(im, 'FINISH', (int(im.shape[0]/2), int(im.shape[1]/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, thickness=2)
        # cv2.imshow("ss", im)
        # cv2.waitKey()


def makeCSVs():
    with open("countries.geojson") as f:
        gj = geojson.load(f)

    cn = 0
    # find = False
    for contry in gj['features']:
        cn += 1
        prop = contry['properties']
        f = open(CSVsPath + prop['ADMIN'] + '.csv', 'w')
        # if find:
        #     break
        # if prop['ADMIN']== dst_cont:
        #     find = True
        # f.write("l,p.lat,p.long,"+prop['ADMIN']+"size,color\n")
        cordinates = contry['geometry']['coordinates']

        for cors in cordinates:
            f.write("P,16777151")
            for cor in cors:
                if len(cor) > 2:
                    for cr in cor:
                        long = cr[0]
                        lat = cr[1]
                        f.write("," + str(lat) + "," + str(long))
                else:
                    long = cor[0]
                    lat = cor[1]
                    f.write("," + str(lat) + "," + str(long))
            f.write("\n")

        f.close()


def findUncolored():
    contry = '../contry_order.txt'
    f = open(contry, 'r')
    lines = f.readlines()

    cnt = 1
    FILES = os.listdir(CSVsPath)
    for cntry in FILES:
        if not lines.__contains__(cntry.replace(".csv","")+"\n"):
            print(cnt, cntry)
            cnt+=1






findUncolored()
# for f in os.listdir(CSVsPath):
#     drawBorder(f)
#     print(f)
