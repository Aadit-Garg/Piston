import math
import matplotlib.pyplot as plt
xy=[]
x_,y_ = [],[]
x_y = []
ang_ = []
nx = []
########################################
# 2 ARM PISTON LOCKED TO LINEAR MOTION #
########################################
#   CIRCULAR MOTION TO LINEAR MOTION   #
########################################
def val(a=0,l=0,r=0):
    if a == 0:
        while True:
            r = float(input("Radius: "))
            l = float(input("Length of Arm: "))
            if l<2*r:
                print("[VALUE ERROR!]arm length must be less than radius")
            else:
                a = float(input("Angle: "))
                spe = float(input("Speed: "))
                break
    return a,l,r

a,l,r = val()
factor = l-r
for i in range(0,int(3600+a*10),int(a*10)):
    i = i/10
    rad = (i)*math.pi/180
    x,y = (math.sin(rad))*r, (math.cos(rad))*r
    # x,y = y,x
    x = (int(x*1000)/1000)
    y = (int(y*1000)/1000)+factor
    # print(int(x*1000)/1000,int(y*1000)/1000)
    xy.append([x,y])
    x_.append(x)
    y_.append(y)
    print(int(x*1000)/1000,int(y*1000)/1000,":",(l**2-int(y*y))**(1/2)+x)
    # print(l**2,"-",y*y,"=",l**2-int(y*y))
    n = (-(l**2-int(x*x))**(1/2)+y)
    # print((l**2-int(y*y))**(1/2),"+",x,"=", n,"\n\n")
    x_y.append([0,n])
    ang_.append(i)
    nx.append(n)
    print(((n-y)**2+(x)**2)**(1/2))

fig, ax = plt.subplots(1,2)
ax[1].set(xlabel='Angle', ylabel='X of hand')
# ax[1,0].set_ylim(-l-r,l+r) 

ax[0].grid(which="both")
ax[1].grid(which="both")
# plt.gca().set_aspect("auto")
ax[0].set_aspect('equal')
# ax[1,0].set_aspect('equal')
ann = 0
points, = ax[0].plot(x_,y_, marker='o')
points2, = ax[1].plot(ang_,nx, marker='o')

for i in range(20):
    for t in range(0,int(360+a),int(a)):
        if t == 0 or t ==360+a:
            # points, = ax[0].plot(x_,y_, marker='o')
            points, = ax[0].plot(x_,y_, marker='o',color="orange")
            points2, = ax[1].plot(ang_,nx, marker='o', color="red")

            # ax[0].set_xlim(-100,100) 
            ax[0].set_xlim(int(-(r+l+2)/2), int((r+l+2)/2)) 
            ax[0].set_ylim(-(2*r+2), int(l+2)) 
            # ax[0].set_ylim(-100,100) 

        else:
            new_x = [xy[int(t/a)][0],x_y[int(t/a)][0]]
            new_y = [xy[int(t/a)][1],x_y[int(t/a)][1]]
            points.set_data(new_x, new_y)
            points2.set_data(ang_[int(t/a)],nx[int(t/a)])
        plt.pause(1/600)
    ann+=int(a)
    
