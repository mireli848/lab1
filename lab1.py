import math
n = ((1.565*5)* math.sqrt(0.14* math.sin(1))/(0.8942*math.log(3)))**(1/4)
u = math.log((3/2)*math.sin(3)-3*math.sin(2))
if n-u<1:
  v = math.exp(2*math.atan(1/n)+3*math.atan(1/u))
else:
  v = math.log(n**2+u**2)
print(f"n = {n}")
print(f"u = {u}")
print(f"v = {v}")
