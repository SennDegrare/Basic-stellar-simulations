from vpython import *
#GlowScript 3.1 VPython
e_graph = gcurve(color=color.black)
def gforce(p1,p2):
    G = 1 # Change to 6.67e-11 to use real-world values.
    r_vec = p1.pos-p2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    force_mag = G*p1.mass*p2.mass/r_mag**2
    force_vec = -force_mag*r_hat
    
    return force_vec
    
star = sphere( pos=vector(0,0,0), radius=0.2, color=color.yellow,
               mass = 1000, momentum=vector(0,0,0), make_trail=True )
               
planet1 = sphere( pos=vector(1,0,0), radius=0.05, color=color.orange,
                  mass = 1, momentum=vector(0,30,0), make_trail=True )

planet2 = sphere( pos=vector(0,3,0), radius=0.075, color=color.blue,
                  mass = 2, momentum=vector(-35,0,0), make_trail=True )

dplanet = sphere( pos=vector(-0.2,3,0), radius=0.015, color=color.gray(0.5),
                  mass = 0.01, momentum=vector(-0.1,-0.1,0), make_trail=True )
                  
planet3 = sphere( pos=vector(0,-4,0), radius=0.1, color=color.green,
                  mass = 10, momentum=vector(160,0,0), make_trail=True )
               
dt = 0.0001
t = 0
while (True):
    rate(1000)
    
    # Calculate forces.
    star.force = gforce(star,planet1)+gforce(star,planet2)+gforce(star,planet3)+gforce(star,dplanet)
    planet1.force = gforce(planet1,star)+gforce(planet1,planet2)+gforce(planet1,planet3)+gforce(planet1,dplanet)
    planet2.force = gforce(planet2,star)+gforce(planet2,planet1)+gforce(planet2,planet3)+gforce(planet2,dplanet)
    planet3.force = gforce(planet3,star)+gforce(planet3,planet1)+gforce(planet3,planet2)+gforce(planet3,dplanet)
    dplanet.force = gforce(dplanet,planet1)+gforce(dplanet,planet2)+gforce(dplanet,planet3)+gforce(dplanet,star)
    # Dwarf dplanet and Planet planet2 start from approximately the same coordinate in this three planet system.
    # dplanet is not captured by the star and escapes after a while.

    # Update momenta.
    star.momentum = star.momentum + star.force*dt
    planet1.momentum = planet1.momentum + planet1.force*dt
    planet2.momentum = planet2.momentum + planet2.force*dt
    planet3.momentum = planet3.momentum + planet3.force*dt
    dplanet.momentum = dplanet.momentum + dplanet.force*dt

    # Update positions.
    star.pos = star.pos + star.momentum/star.mass*dt
    planet1.pos = planet1.pos + planet1.momentum/planet1.mass*dt
    planet2.pos = planet2.pos + planet2.momentum/planet2.mass*dt
    planet3.pos = planet3.pos + planet3.momentum/planet3.mass*dt
    dplanet.pos = dplanet.pos + dplanet.momentum/dplanet.mass*dt
    
    t = t + dt