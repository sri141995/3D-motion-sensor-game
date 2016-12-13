from visual import *
#import serial



MyScene=display(title='My Virtual World') 
 
MyScene.width=800  
MyScene.height= 800
MyScene.autoscale=False
MyScene.range = (12,12,12)
ball1=sphere(pos=vector(0,0,0),radius=1.25,material=materials.earth)
obj1=ellipsoid(length=4, width=2,height=.5, pos=(-12,0,0),color=color.cyan,material=materials.chrome)
lamp = local_light(pos=(20,20,-20), color=color.yellow)
sun=sphere(pos=(20,20,-20),radius=1.5,color=color.yellow,material=materials.emissive)
mars=sphere(pos=vector(0,0,0),radius=0.75,material=materials.blazed,color=color.red)
mars.visible=False
#sensorData= serial.Serial('com3',9600)
a=0

def ball():
    s=0
    i=0
    while i<100:
        
        z=-40
        x=random.randint(-12,12)
        y=0
        l=-12
        m=0
        n=0
        u=random.randint(-12,12)
        r=0
        t=-12
        
         
        
        rate(25)
            #ball1=sphere(pos=(x,y,z),radius=1,color=color.red)
        
        while z<20:
            

            rate(25)
            #textline = sensorData.readline()
            textline=15
            a=float(textline)
            print(textline)
            obj1.pos=vector(-12+a,0,0)
            if i==5:
                mars.visible=True
                mars.velocity=(0,0,3)
                mars.pos=(u,r,t)
                t=t+.5
                
                
            ball1.velocity=(0,0,5)
            ball1.pos=(x,y,z)
            z=z+1

      
            if (ball1.pos.z==-1):
                if((a-14)<=ball1.pos.x<=(a-10)):
                    label(pos=(0,0,0),text='YOU CRASHED!!!',color=color.red)
                    sleep(1.5)
                    label(pos=(0,-5,0),text='YOUR SCORE IS:%d'%s,color=color.green)
                    sleep(1.5)
                    exit()
            if (mars.pos.z==-1):
                if((a-14)<=mars.pos.x<=(a-10)):
                    s=s+100
                    label(pos=(10,8,0),text='BONUS!!!\nSCORE:%d'%s,color=color.green)
            if ball1.pos.z>obj1.pos.z:
                    s=s+1
                    label(pos=(6,8,0),text='SCORE:%d'%s,color=color.green)
                
                
            
        mars.visible=False   
        i=i+1
k=ball()





