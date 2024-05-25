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

# apply the euler integration on the given conditions
euler_method(r, v, accn, dt)

#find the point at which the earth is at its aphelion 
sizes= np.array([np.linalg.norm(position)for position in r])
position_aphelion = np.max(sizes)
arg_aphelion =np.argmax(sizes)
velocity_aphelion = np.linalg.norm(v[arg_aphelion])

print(position_aphelion/1e9, velocity_aphelion/1e3)