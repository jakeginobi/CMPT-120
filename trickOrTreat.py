candies = "55 15 98 "
st = 0
total = 0
for i in range (len(candies)):
      if candies[i] == " ":
        st = candies[i-2:i]
        total += int(st)

print total
