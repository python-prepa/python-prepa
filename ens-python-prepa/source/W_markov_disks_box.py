from random import uniform as ran, choice
L = [(0.25,0.25),(0.75,0.25),(0.25,0.75),(0.75,0.75)]
sigma = 0.20
delta = 0.15
for iter in range(1000000):
   a = choice(L)
   L.remove(a)
   b = (a[0] + ran( -delta, delta),a[1] + ran(-delta , delta))
   min_dist = min((b[0]-x[0])**2 + (b[1]-x[1])**2 for x in L)
   box_cond = min(b[0],b[1]) < sigma or max(b[0],b[1]) >1-sigma
   if box_cond or min_dist < 4*sigma**2:
      L.append(a)
   else:
      L.append(b)
print L
