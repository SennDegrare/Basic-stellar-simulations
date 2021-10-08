from vpython import *
#GlowScript 3.1 VPython
from vpython import *
graph(fast=False)
e_graph = gcurve(color=color.black)
def gforce(p1,p2):
    G = 1
    r_vec = p1.pos-p2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    force_mag = G*p1.mass*p2.mass/r_mag**2
    force_vec = -force_mag*r_hat
    
    return force_vec
    
star1 = sphere( pos=vector(0,0,0), radius=100, color=color.yellow,
               mass = 10**5, momentum=vector(0,0,0), make_trail=True )
               
particle1 = sphere( pos=vector(500,0,0), radius=1, color=color.white,
                  mass = 1, momentum=vector(-1000,0,0), make_trail=True)
                  
particle2 = sphere( pos=vector(1000,0,0), radius=1, color=color.white,
                  mass = 1, momentum=vector(-1000,0,0), make_trail=True)              

print("Distance = ",particle1.pos-particle2.pos)
               
dt = 0.0001
t = 0
while (mag(particle1.pos-star1.pos)>star1.radius):
    rate(1000)
    
    # Calculate forces.
    star1.force = gforce(star1,particle1)+gforce(star1,particle2)
    particle1.force = gforce(particle1,star1)+gforce(particle1,particle2)
    particle2.force = gforce(particle2,star1)+gforce(particle2,particle1)

    # Update momenta.
    star1.momentum = star1.momentum + star1.force*dt
    particle1.momentum = particle1.momentum + particle1.force*dt
    particle2.momentum = particle2.momentum + particle2.force*dt
    
    # Update positions.
    star1.pos = star1.pos + star1.momentum/star1.mass*dt
    particle1.pos = particle1.pos + particle1.momentum/particle1.mass*dt
    particle2.pos = particle2.pos + particle2.momentum/particle2.mass*dt
    
    dist = mag(particle2.pos-particle1.pos)
    print("Inter-particle distance = ",dist)
    
    t = t + dt