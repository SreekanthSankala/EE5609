import numpy as np
import matplotlib.pyplot as plt
import math
x1=np.array(list(range(-500,500,1)))
x2=np.array(list(range(-500,500,1)))
y1=(-9/7.0)*x1-1
y2=(-3/2.0)*x2+3.0
plt.plot(x1,y1,"r",label="(9 7)x=7")
plt.legend(loc="upper left")
plt.plot(x2,y2,"b",label="(3 2)x=-6")
plt.legend(loc="upper left")
a1=9.0 ;b1=7.0 ; c1=-7.0 ; a2=3.0 ; b2=2.0 ; c2=6.0;
a3=((a1/math.sqrt((a1*a1)+(b1*b1)))) + ((a2/math.sqrt((a2*a2)+(b2*b2))))
b3=((b1/math.sqrt((a1*a1)+(b1*b1)))) + ((b2/math.sqrt((a2*a2)+(b2*b2))))
c3=((c1/math.sqrt((a1*a1)+(b1*b1)))) + ((c2/math.sqrt((a2*a2)+(b2*b2))))
x3=np.array(list(range(-500,500,1)))
y3=(-a3/b3)*x3+(-c3/b3)
plt.plot(x3,y3,"g",label="Result")
plt.legend(loc="upper left")
plt.show()
