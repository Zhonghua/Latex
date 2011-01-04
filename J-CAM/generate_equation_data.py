from sympy import (var, exp, pprint, Eq, Symbol, Function, cos, pi, simplify,
        ccode, latex)

var("x y k d_n d_v sigma kappa")
lam = Symbol("lambda")

def eq1(u, v, f):
    return -d_n*(u.diff(x, 2) + u.diff(y, 2)) - f(u) + sigma*v

def eq2(u, v):
    return -d_v*(v.diff(x, 2) + v.diff(y, 2)) - u + v

u = Function("u")
v = Function("v")
print "Reaction-Diffusion Equations:"
def f(u):
    return lam*u-u**3-kappa
pprint(eq1(u(x, y), v(x, y), f))
pprint(eq2(u(x, y), v(x, y)))

print "\nSolution:"
u_hat = 1-(exp(k*x)+exp(-k*x))/(exp(k)+exp(-k))
pprint(Eq(Function("u_hat")(x), u_hat))

#test the Boundary Conditions:
assert u_hat.subs(x, -1) == 0
assert u_hat.subs(x, 1) == 0

u = cos(x*pi/2)*cos(y*pi/2)
v = u_hat*u_hat.subs(x, y)
print "u:"
pprint(u)
print "v:"
pprint(v)

print "-"*80
print "RHS, for f(u)=u:"
# delete this redefinition to get nonlinear f(u):
def f(u):
    return u
e1 = eq1(u, v, f)
e2 = eq2(u, v)
print "g1:"
pprint(e1)
print "g2:"
pprint(e2)
print
print "latex:"
print latex(e1)
print latex(e2)

print
print "C code:"
print "g1 =", ccode(e1)
print "g2 =", ccode(e2)
