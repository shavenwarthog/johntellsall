<!-- f(x)= c*x**3 + a*x**2 + b*x + y0 -->
<!-- fit f(x) 'optimize.dat' via a,b,c,y0 -->
<!-- f(x)= a*x**2 + b*x + y0 -->
<!-- fit f(x) 'optimize.dat' via a,b,y0 -->
f(x)= a*x + y0
fit f(x) 'optimize.dat' via a,y0


plot "optimize.dat" with points lt rgb "#ff0000" title "Points", \
f(x) with lines lt rgb "#ff00ff" title "Approximation"
