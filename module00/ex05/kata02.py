t = (3, 30, 2019, 9, 25)

minuntes = str(t[1]).zfill(2)
hour = str(t[0]).zfill(2)
day = str(t[4]).zfill(2)
month = str(t[3]).zfill(2)
year = str(t[2])

print(f"{month}/{day}/{year} {hour}:{minutes}")
