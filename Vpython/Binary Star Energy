GlowScript 3.1 VPython
from vpython import *

scene = canvas(backgrund = color.white)

G = 6.7e-11

Sun = sphere(pos = vec(-1.1e11, 0, 0), mass = 2e24, radius = 10*7e8, color = color.orange, make_trail = True)


Earth = sphere(pos = vec(1.5e11, 0, 0), mass = 1e24, radius = 6*6.4e8, color = color.blue, make_trail = True)


mu = 2e29

R = Earth.pos - Sun.pos

Earth.p = Earth.mass * vec(0,1e1,0)

Sun.p = -Earth.p

K_0 = (0.5 * (Earth.p.mag2)/Earth.mass) + (0.5 * (Sun.p.mag2)/Sun.mass)
P_0 = -G * Earth.mass * Sun.mass / R.mag

gr_p = graph(title = 'p(t) diagram', xtitle = 'time (s)', ytitle = 'p(t)')

p_plot_E_x = gcurve(graph = gr_p, color = color.red)
p_plot_E_y = gcurve(graph = gr_p, color = color.blue)
p_plot_E_z = gcurve(graph = gr_p, color = color.green)

p_plot_S_x = gcurve(graph = gr_p, color = color.red)
p_plot_S_y = gcurve(graph = gr_p, color = color.blue)
p_plot_S_z = gcurve(graph = gr_p, color = color.green)

gr_pt = graph(title = 'total p(t) diagram', xtitle = 'time (s)', ytitle = 'p(t)')
p_plot_t_x = gcurve(graph = gr_pt, color = color.red)
p_plot_t_y = gcurve(graph = gr_pt, color = color.blue)
p_plot_t_z = gcurve(graph = gr_pt, color = color.green)

bin_w = graph(title = 'Work-Energy diagram', xtitle = 'time (s)', ytitle = 'W')
DK_w = gcurve(graph = bin_w, color = color.red)
WI_w = gcurve(graph = bin_w, color = color.cyan)
DP_w = gcurve(graph = bin_w, color = color.blue)

bin_e = graph(title = 'Energy diagram', xtitle = 'time (s)', ytitle = 'E(t)')
K_e = gcurve(graph = bin_e, color = color.red)
P_e = gcurve(graph = bin_e, color = color.blue)
E_e = gcurve(graph = bin_e, color = color.green)

myrate = 2000

t = 0
dt = 2*30*24*60*60
work = 0

while t < 2000*365*24*60*60:
# while R.mag > Sun.radius + Earth.radius:
    
    rate(myrate)
    
    R = Earth.pos - Sun.pos
    
    F_g = -G * Earth.mass * Sun.mass / R.mag2 * R.hat
    #F_rad_Earth = (-mu * (F_g.mag / Earth.mass) ** 2) * Earth.p.hat
    #F_rad_Sun = (-mu * (F_g.mag / Sun.mass) ** 2) * Sun.p.hat
    
    Earth.p = Earth.p + (F_g  ) * dt # update momentum
    Earth.v = Earth.p / Earth.mass # calculate velocity
    Earth.pos += Earth.v * dt # update position
    
    Sun.p = Sun.p + (-F_g  ) * dt # update momentum
    Sun.v = Sun.p / Sun.mass # calculate velocity
    Sun.pos += Sun.v * dt # update position
    
    work =  work + dot(-F_g, Sun.v) * dt + dot(F_g, Earth.v) * dt # ASK ABOUT THIS
    
    p_plot_E_x.plot(pos = (t, Earth.p.x))
    p_plot_E_y.plot(pos = (t, Earth.p.y))
    p_plot_E_z.plot(pos = (t, Earth.p.z))
    
    p_plot_S_x.plot(pos = (t, Sun.p.x))
    p_plot_S_y.plot(pos = (t, Sun.p.y))
    p_plot_S_z.plot(pos = (t, Sun.p.z))
    
    p_plot_t_x.plot(pos = (t, Sun.p.x + Earth.p.x)) # plot x momentum of SUN EARTH system # ASK ABOUT THIS
    p_plot_t_y.plot(pos = (t, Sun.p.y + Earth.p.y)) # plot y momentum of SUN EARTH system
    p_plot_t_z.plot(pos = (t, Sun.p.z + Earth.p.z)) # plot z momentum of SUN EARTH system

    K = (0.5 * (Earth.p.mag2)/Earth.mass) + (0.5 * (Sun.p.mag2)/Sun.mass) # ask about this and the one on top
    P = -G * Earth.mass * Sun.mass / R.mag
    
    WI_w.plot(pos = (t, work))
    DK_w.plot(pos = (t, K - K_0))
    DP_w.plot(pos = (t, P - P_0))
    
    K_e.plot(pos = (t, K))
    P_e.plot(pos = (t, P))
    E_e.plot(pos = (t, K + P))
    
    t = t + dt
