t = (0, 4, 132.42222, 10000, 12345.67)

day = str(t[0]).zfill(2)
ex = str(t[1]).zfill(2)
n1 = round(t[2], 2)
n2 = format(t[3], ".2e")
n3 = format(t[4], ".2e")

print(f"day_{day}, ex_{ex} : {n1}, {n2}, {n3}")
