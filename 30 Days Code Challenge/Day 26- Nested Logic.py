n = [1, 1, 2010]
nn = [31, 12, 2009]
#
# n = [31, 12, 2009]
# nn = [1, 1, 2010]

day_diff = n[0] - nn[0]
month_diff = n[1] - nn[1]
year_diff = n[2] - nn[2]

if day_diff > 0 and n[1:] == nn[1:]:
    print(day_diff * 15)
elif month_diff > 0 and n[2] == nn[2]:
    print(month_diff * 500)
elif year_diff > 0:
    print(10000)
else:
    print(0)
