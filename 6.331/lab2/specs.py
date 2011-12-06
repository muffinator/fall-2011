from math import *
Vin = range(8,17)
Vout = -10E0
Pout = 5E0
D=[]
for v in Vin:
	d = [Vout/(Vout-v)]
	D += d
	Rl = Vout**2/Pout
	Iout = Pout/Vout
	Il_avg = Iout/(1-d)
	dIl = 2*Il_avg
	Lmin = v*d*T/dIl
print D
