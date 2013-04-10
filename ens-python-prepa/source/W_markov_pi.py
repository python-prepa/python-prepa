from random import uniform
def markov_pi(delta, N):
    x, y = 1., 1.
    N_hits = 0
    for i in range(N):
        del_x,del_y=uniform(-delta,delta),uniform(-delta,delta)
        if abs(x + del_x) < 1 and abs(y + del_y) < 1:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1:
            N_hits += 1
    return 4 * N_hits / float(N)

for k in range(10):
   print k, markov_pi(0.3,100000)
   print k, markov_pi(0.1,100000)
   print
