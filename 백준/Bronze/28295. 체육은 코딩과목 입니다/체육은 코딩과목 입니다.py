lst = []
for _ in range(10):
    lst.append(int(input()))
woo = lst.count(1) * 90
back = lst.count(2) * 180
jua = lst.count(3) * (-90)
total = (woo + back + jua) % 360
if total == 90 or total == -270:
    print("E")
elif total == 180 or total == -180:
    print("S")
elif total == 270 or total == -90:
    print("W")
else:
    print("N")