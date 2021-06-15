GlowScript 3.1 VPython
from vpython import *

scene = canvas(background=color.white)

G = 6.7e-11               #Newton's gravitational constant

sun = sphere(pos = vec(0,0,0), mass = 1.989e30, radius = 10*7e8, color = color.orange, make_trail = True)

earth = sphere(pos = vec(1.49e11,0,0), mass = 5.972e24, radius = 6*6.4e8, color = color.blue, make_trail = True)


sun.p = sun.mass * vec(0,0,0)
earth.p = earth.mass * vec(0,2.978e4,0) # initialize momentum

t = 0 # initialize time
dt = 60 * 60 # create time step of 60*60

gr_p = graph(title = 'Earth & Sun momentum diagram', xtitle = 'time (s)', ytitle = 'p')# create graph with title 'Earth & Sun momentum diagram', xtitle = 'time(s)', ytitle = 'p'

    
p_plot_E_x = gcurve(graph = gr_p, color = color.red) # make gcurve associated with gr_p and with color red
p_plot_E_y = gcurve(graph = gr_p, color = color.blue) # make gcurve associated with gr_p and with color blue
p_plot_E_z = gcurve(graph = gr_p, color = color.green) # make gcurve associated with gr_p and with color green

p_plot_S_x = gcurve(graph = gr_p, color = color.red) # make gcurve associated with gr_p and with color red
p_plot_S_y = gcurve(graph = gr_p, color = color.blue) # make gcurve associated with gr_p and with color blue
p_plot_S_z = gcurve(graph = gr_p, color = color.green) # make gcurve associated with gr_p and with color green

gr_pt = graph(title = 'Total p(t) diagram', xtitle = 'time (s)', ytitle = 'p')

p_plot_t_x = gcurve(graph = gr_pt, color = color.red) # make gcurve associated with gr_pt and with color red
p_plot_t_y = gcurve(graph = gr_pt, color = color.blue) # make gcurve associated with gr_pt and with color blue
p_plot_t_z = gcurve(graph = gr_pt, color = color.green) # make gcurve associated with gr_pt and with color green

gr_v = graph(title = 'Earth & Sun velocity diagram', xtitle = 'time (s)', ytitle = 'v') # create a graph with title 'Earth & Sun velocity diagram', xtitle = 'time (s), ytitle 'v' 


v_plot_E_x = gcurve(graph = gr_v, color = color.red) # make gcurve associated with gr_v and with color red
v_plot_E_y = gcurve(graph = gr_v, color = color.blue) # make gcurve associated with gr_v and with color blue
v_plot_E_z = gcurve(graph = gr_v, color = color.green) # make gcurve associated with gr_v and with color green

v_plot_S_x = gcurve(graph = gr_v, color = color.red) # make gcurve associated with gr_v and with color red
v_plot_S_y = gcurve(graph = gr_v, color = color.blue) # make gcurve associated with gr_v and with color blue
v_plot_S_z = gcurve(graph = gr_v, color = color.green) # make gcurve associated with gr_v and with color green

gr_cp = graph(title = 'Gravity vs Centripital', xtitle = 'time (s)', ytitle = 'F') # create a graph with title 'Gravity vs Centripital', xtitle 'time (s)', ytitle 'F'


cp_plot_gr = gcurve(graph = gr_cp, color = color.red)
cp_plot_cp = gcurve(graph = gr_cp, color = color.blue)

myrate = 1500

earth.old_p = earth.p
earth.T = 0

while t < 5*365*24*60*60:
    
    rate(myrate)
    
    R = earth.pos - sun.pos
    
    F_g = -G * earth.mass * sun.mass / R.mag2 * R.hat   # R = sun.pos - earth.pos, then F_g = G * earth.mass * sun.mass / R .mag2 * R.hat
    
         
    
    earth.p = earth.p + F_g * dt # calculate earth momentum using force
    earth.v = earth.p/earth.mass # calculate earth velocity
    earth.pos += earth.v * dt # caluclate earth position
    
    sun.p = sun.p + F_g * dt # calculate sun momentum using force
    sun.v = sun.p/sun.mass # calculate sun velocity
    sun.pos += sun.v * dt # caluclate sun position
    
    p_plot_E_x.plot(pos = (t, earth.p.x))
    p_plot_E_y.plot(pos = (t, earth.p.y))
    p_plot_E_z.plot(pos = (t, earth.p.z))
    
    p_plot_S_x.plot(pos = (t, sun.p.x))
    p_plot_S_y.plot(pos = (t, sun.p.y))
    p_plot_S_z.plot(pos = (t, sun.p.z))
    
    p_plot_t_x.plot(pos = (t, earth.p.x + sun.p.x)) # using the gcurves we defined above (the while loop), plot the total x, y, and z momenta of the Earth and Sun system as a function of time- 3 plots
    p_plot_t_y.plot(pos = (t, earth.p.y + sun.p.y)) # using the gcurves we defined above (the while loop), plot the total x, y, and z momenta of the Earth and Sun system as a function of time- 3 plots
    p_plot_t_z.plot(pos = (t, earth.p.z + sun.p.z)) # using the gcurves we defined above (the while loop), plot the total x, y, and z momenta of the Earth and Sun system as a function of time- 3 plots
    
    
    v_plot_E_x.plot(pos = (t, earth.v.x))
    v_plot_E_y.plot(pos = (t, earth.v.y))
    v_plot_E_z.plot(pos = (t, earth.v.z))
    
    v_plot_S_x.plot(pos = (t, sun.v.x))
    v_plot_S_y.plot(pos = (t, sun.v.y))
    v_plot_S_z.plot(pos = (t, sun.v.z))
    
    cp_plot_gr.plot(pos = (t, F_g.mag)) # using the gcurves we defined above (the while loop), plot the gravitational force and the centripetal force as functions of time of the Earth and Sun system. Remember cenrtipetal force  = m * v ^ 2 / r * rhat- 2 plots - only for earth
    cp_plot_cp.plot(pos = (t, earth.mass * earth.v.mag2 / R.mag)) # using the gcurves we defined above (the while loop), plot the gravitational force and the centripetal force as functions of time of the Earth and Sun system. Remember cenrtipetal force  = m * v ^ 2 / r * rhat- 2 plots - only for earth
    
    
    
    t = t + dt
    
    if earth.old_p.x > 0 and earth.p.x < 0:
        print('Year: ', earth.T/(60*60*24), ' days')
        earth.T = 0
        
    earth.old_p = earth.p
    earth.T = earth.T + dt
