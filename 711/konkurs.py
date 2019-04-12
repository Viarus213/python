import time
t1 = time.time()

def func():
    item1 = item2 = item3 = divs[0]
    item2_ind = item3_ind = 0
    item1_ind = len(divs) - 1
    iterations = 0

    while (item1_ind >= 0):
        item1 = divs[item1_ind]
        item2 = item1
        while (item1 + item2 <= 711 and item2_ind <= item1_ind):
            item2 = divs[item2_ind]
            item3 = item2
            while (item1 + item2 + item3 <= 711 and item3_ind <= item2_ind):
                iterations += 1
                item3 = divs[item3_ind]
                item4 = 711 - (item1 + item2 + item3)
                if item4 <= item3:
                    
                    if ((item1 * item2 * item3 * item4) == 711000000):
                        print ("Ceny towarów [$]:", \
                               item1/100.0, item2/100.0, item3/100.0, item4/100.0)
                        print ("Liczba iteracji:", iterations)
                        return 1
                    
                item3_ind += 1
                
            item2_ind += 1
            item3_ind = 0

        item1_ind -= 1
        item2_ind = 0

    return 0

divs = []
for x in range (1, 711):
    if (711000000 % x == 0):
        divs.append(x)

if (func()):
    t2 = time.time()
    print ("Czas wykonania programu [s]:", t2 - t1)
else:
    print ("Error")
