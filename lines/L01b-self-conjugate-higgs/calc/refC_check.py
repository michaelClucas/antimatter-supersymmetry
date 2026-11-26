# Referee C check: one-loop beta_C on C = 0 (V = lam(|H|^2 - v^2/2)^2, m_h^2 = 2 lam v^2), standard SM one-loop betas.
import sympy as sp
g,gp,g3,y,lam=sp.symbols('g gp g3 y lam',positive=True)
C=6*lam+sp.Rational(9,4)*g**2+sp.Rational(3,4)*gp**2-6*y**2
b={g:-sp.Rational(19,6)*g**3, gp:sp.Rational(41,6)*gp**3, g3:-7*g3**3,
   y:y*(sp.Rational(9,2)*y**2-8*g3**2-sp.Rational(9,4)*g**2-sp.Rational(17,12)*gp**2),
   lam:24*lam**2-6*y**4+sp.Rational(3,8)*(2*g**4+(g**2+gp**2)**2)+lam*(12*y**2-9*g**2-3*gp**2)}
bC=sum(sp.diff(C,k)*v for k,v in b.items())
lam0=sp.solve(C,lam)[0]
print("16pi^2 beta_C|_{C=0} =",sp.expand(bC.subs(lam,lam0)))
claimed=33*g**4+sp.Rational(63,2)*g**2*gp**2-162*g**2*y**2+96*g3**2*y**2+17*gp**4-46*gp**2*y**2+126*y**4
print("difference from WORK.md S5:",sp.simplify(sp.expand(bC.subs(lam,lam0))-claimed))
# Tree-level C from measured masses (C = (3/v^2)(m_h^2+2MW^2+MZ^2-4mt^2)); pole masses, illustrative only
mh,MW,MZ,mt,v=125.20,80.3692,91.1876,172.57,246.22
print("tree C(pole masses) = %.3f"%(3/v**2*(mh**2+2*MW**2+MZ**2-4*mt**2)))
# CW/Gildener-Weinberg mass relation in a scale-invariant SM: spin-preserving symmetry fixing m_h^2 in terms of g^4, y_t^4
B=(6*MW**4+3*MZ**4-12*mt**4)/(64*sp.pi**2*v**4)
print("GW: m_h^2 = 8 B v^2 needs B>0; B = %.3e"%float(B))
