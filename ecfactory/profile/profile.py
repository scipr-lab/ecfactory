import ecfactory.cocks_pinch as cp
import ecfactory.dupont_enge_morain as dem
import time

bits = [50,75,100,110,125,150,175,200,250,300,350,400,450,500]
eds = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] #, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

num_times = 10
def call_dem(n,k):
    start = time.time();
    dem.run(n,k)
    return time.time()-start

def call_cp(n,k):
    r,k,D = cp.gen_params_from_bits(n,k)
    start = time.time();
    cp.run(r,k,D)
    return time.time()-start
    
def profile(p):
    if p == "dem":
        f = call_dem
    if p == "cp":
        f = call_cp
    for k in eds:
        file = open("logs/" + p + "/k" + str(k) + ".csv", 'w')
        file.write("Number of bits, Time in seconds\n")
        for n in bits:
            print(n,k)
            total_time = 0
            for i in range(0,num_times):
                total_time += f(n,k)
                print(total_time)
            file.write(str(n) + ", %.4f\n" %(total_time/num_times))
        file.close()

profile("dem")
profile("cp")

