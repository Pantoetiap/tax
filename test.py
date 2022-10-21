
def tax():
    i1 = int(input("price :" ))
    i2 = float(input("tax :"))
    # i1 = 800
    # i2 = 4.40

    i3 = ((i1 / 100) * i2)


    i6 =0

    while True:


        i6 = i6 + 0.01
        i5 = i1 +((i1 / 100) * i2) + i6
        i7 = i5-(i5/100)*i2

        if i1+0.02 < i7:

            break


    print("ต้องตั้งราคา :",i1+i3+i6)
    print("ส่วนต่างที่เพิ่มขึ้น :", (i1 -i1+i3+i6 ))





if __name__ == '__main__':
    tax()