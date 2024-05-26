#imports
import matplotlib.pyplot as plt
import numpy as np

# constants 
G = 6.6743e-11
M_sun = 1.989e30

# initial position and vector 
r_0 = np.array([147.1e9,0])
v_0 = np.array([0, -30.29e3])

# time step and total time for simulation 
dt = 3600 
t_max = 3.154e7
method_integration = 'euler'

# time array to be used in the numerical solution  
t = np.arange(0, t_max, dt)
print(t.astype('int32'))

# initialize arrays to store position and velocities at all the time steps
r= np.empty(shape=(len(t),2 ))
v= np.empty(shape=(len(t),2 ))

#set the initial conditions for positions and velocities 
r[0], v[0] =r_0 , v_0 

# defining acceleration
def accn(r):
    return (-G*M_sun / np.linalg.norm(r)**3 ) *r

# Euler integrrration 
def euler_method(r, v, accn, dt):
    
    for i in range(1, len(t)):
        r[i] = r[i-1]+ v[i-1]*dt
        v[i] = v[i-1] + accn(r[i-1]) *dt

# using another method rk4 method 
def rk4_method (r, v, accn, dt):  
 for i in range (1, len(r)):
    k1v = accn(r[i-1]) 
    k1r = v[i-1]
      
    k2v = accn(r[i-1]+ k1r * dt/2) 
    k2r = v[i-1] + k1v * dt/2  
    
    k3v =  accn(r[i-1]+ k2r * dt/2) 
    k3r = v[i-1] + k2v * dt/2  
    
    k4v =  accn(r[i-1]+ k3r * dt/2) 
    k4r = v[i-1] + k3v * dt/2  
    
    #update the r and v
    v[i]= v[i-1]+ dt/6*(k1v+ 2*k2v +2*k3v +k4v)
    r[i]= r[i-1]+ dt/6*(k1r+ 2*k2r +2*k3r +k4r)
    
    
# applicatio of numerical integration based on the chosen method 
def numerical_integration (r, v, accn, dt, method ):
    if method == 'euler':
        euler_method (r, v, accn, dt)
    elif method == 'rk4':
        rk4_method(r, v, accn, dt)
    else:
     raise Exception(f'You can either choose "euler" or "rk4". Your current input method is:- {method}')    

numerical_integration (r, v, accn, dt, method= method_integration )   

sizes= np.array([np.linalg.norm(position)for position in r])
position_aphelion = np.max(sizes)
arg_aphelion =np.argmax(sizes)
velocity_aphelion = np.linalg.norm(v[arg_aphelion])

# plotting the simulated ata on the 3d axes 
plt.style.use('dark_background')
plt.figure(figsize=(7,12))
plt.subplot(projection='3d')
suptitle_str = "RK4" if method_integration == 'rk4' else "Euler"
plt.suptitle(suptitle_str + ' Method', color='r', fontsize=18, weight='bold')
plt.title(f'At Aphelion, the Earth is {round(position_aphelion/1e9,1)}Million Kilometer away from the Sun \n Moving at the speed of {round(velocity_aphelion/1e3,1)}Km/s.', fontsize=14, color='orange')
plt.plot(r[:,0],r[:,1], color= 'tab:purple', lw=2, label='Orbit')
plt.scatter(0,0, color='yellow', s=1000, label='sun')
plt.scatter(r[0,0],r[0,1],s=200, label='Earth at its perihelion')
plt.scatter(r[arg_aphelion,0],r[arg_aphelion,1],s=200, label='Earth at its aphelion',color= 'blue')
legend = plt.legend(loc='lower right', frameon= False)
legend.legend_handles[1]._sizes =[150]
legend.legend_handles[2]._sizes =[80]
legend.legend_handles[3]._sizes =[80]
plt.axis('off')
plt.show( )

