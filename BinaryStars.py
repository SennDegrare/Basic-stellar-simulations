from vpython import *
#GlowScript 3.1 VPython
e_graph = gcurve(color=color.blue)
def gforce(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1 # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos-p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*p1.mass*p2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_hat
    
    return force_vec
    
star1 = sphere( pos=vector(-5,0,0), radius=0.2, color=color.yellow,
               mass = 1000, momentum=vector(0,5000,0), make_trail=True )
               
star2 = sphere( pos=vector(10,0,0), radius=0.18, color=color.white,
                  mass = 998, momentum=vector(0,-5000,0), make_trail=True )

               
dt = 0.0001
t = 0
while (True):
    rate(1000)
    
    # Calculate forces.
    star1.force = gforce(star1,star2)
    star2.force = gforce(star2,star1)

    # Update momenta.
    star1.momentum = star1.momentum + star1.force*dt
    star2.momentum = star2.momentum + star2.force*dt

    # Update positions.
    star1.pos = star1.pos + star1.momentum/star1.mass*dt
    star2.pos = star2.pos + star2.momentum/star2.mass*dt
    
    t = t + dt
