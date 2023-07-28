from plotter import plot
from scan import vary_z_size, vary_y_size, vary_z_pos, vary_y_pos, vary_VUV_E, vary_UNB_E

var, matches, n_hit, n_ion, x, y, xp, yp = vary_z_pos()
plot(matches, var, "z position (m)", n_hit, n_ion, x, y, xp, yp) 

var, matches, n_hit, n_ion, x, y, xp, yp = vary_y_pos()
plot(matches, var, "y position (m)", n_hit, n_ion, x, y, xp, yp) 

var, matches, n_hit, n_ion, x, y, xp, yp = vary_z_size()
plot(matches, var, "z beam size (m)", n_hit, n_ion, x, y, xp, yp) 

var, matches, n_hit, n_ion, x, y, xp, yp = vary_y_size()
plot(matches, var, "y beam size (m)", n_hit, n_ion, x, y, xp, yp) 

#var, matches, n_hit, n_ion, x, y, xp, yp = vary_VUV_E()
#plot(matches, var, "VUV Energy", n_hit, n_ion, x, y, xp, yp) 

#var, matches, n_hit, n_ion, x, y, xp, yp = vary_UNB_E()
#plot(matches, var, "UNB Energy", n_hit, n_ion, x, y, xp, yp) 




