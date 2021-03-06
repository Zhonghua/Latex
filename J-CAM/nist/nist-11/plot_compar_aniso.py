# import libraries
import numpy, pylab
from pylab import *

# plot DOF convergence graph
axis('equal')
pylab.title("Error convergence")
pylab.xlabel("Degrees of freedom")
pylab.ylabel("Error [%]")
data = numpy.loadtxt("conv_dof_est_hp_anisoh.dat")
x = data[:, 0]
y = data[:, 1]
loglog(x, y, "-s", label="hp-FEM")

data = numpy.loadtxt("conv_dof_est_h2_aniso.dat")
x = data[:, 0]
y = data[:, 1]
loglog(x, y, "-s", label="h-FEM (p=2)")

data = numpy.loadtxt("conv_dof_est_h1_aniso.dat")
x = data[:, 0]
y = data[:, 1]
loglog(x, y, "-s", label="h-FEM (p=1)")

legend()

# initialize new window
pylab.figure()

axis('equal')
pylab.title("Error convergence")
pylab.xlabel("CPU time (s)")
pylab.ylabel("Error [%]")
data = numpy.loadtxt("conv_cpu_est_hp_anisoh.dat")
x = data[:, 0]
y = data[:, 1]
loglog(x, y, "-s", label="hp-FEM")

data = numpy.loadtxt("conv_cpu_est_h2_aniso.dat")
x = data[:, 0]
y = data[:, 1]
loglog(x, y, "-s", label="h-FEM (p=2)")

data = numpy.loadtxt("conv_cpu_est_h1_aniso.dat")
x = data[:, 0]
y = data[:, 1]
loglog(x, y, "-s", label="h-FEM (p=1)")

legend()


# finalize
show()
