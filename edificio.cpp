/*
*   TAREA 2 METODOS
*       Solución de la ecuación diferentcial x''(t)+w2*x(t)==0 mediante RK4
*
*   Para esto se divide la ecuación en un sistema de dos ecuaciones:
*                              x'(t)=v(t)                 (1)
*                            v'(t)=-w2*x(t)               (2)
*
*    Se usará RK2 para resolver (2) con valor inicial v(0)=v0 y luego para resolver
*    (1) con valor inicial x(0)=x0, iterativamente.
*
*    Sin embargo, el método está diseñado para solucionar cualesquiera sistemas de
*    ecuaciones (1) y (2), siempre que estas sean de la forma:
*
*                             x'(t)=f1(t,v)               (1)
*                             v'(t)=f2(t,x)               (2)
*
*/

#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double x0,v0,w2,tmax,dt;
double m=1000.0;
double y=0.0;
double k=2000;
double w0=sqrt((k/m));
int tsize;

//Función 1: F(t) = sin(ωt)
double eq1(double t_,double v_)
{
	return sin(v_);
}
//Función 2: ω = 1.0*􏰀(k/m)
double eq2(double t_,double x_)
{
	return -w0*x_;
}

//Implementación de los K de la función Runge Kutta
double k1( double t_, double arg, double(*f)(double,double) )
{
	return dt*f(t_,arg);
}
double k2( double t_, double arg, double(*f)(double,double), double K )
{
	return dt*f(t_+dt/2,arg+K/2);
}
double k3( double t_, double arg, double(*f)(double,double), double K )
{
	return dt*f(t_+dt/2,arg+K/2);
}
double k4( double t_, double arg, double(*f)(double,double), double K )
{
	return dt*f(t_+dt,arg+K);
}

//Función de Runge-Kutta
double RungeKuttaIncrement(double t_, double arg, double(*f)(double,double) )
{
	double K1=k1(t_,arg,f);
	double K2=k2(t_,arg,f,K1);
	double K3=k3(t_,arg,f,K2);
	double K4=k4(t_,arg,f,K3);
	return (1./6.)*(K1+2*K2+2*K3+K4);
}


int main()
{
	x0=1; w2=3; v0=-1; tmax=50; dt=0.01; tsize=(int)tmax/dt+1;   // definiciones
	double t[tsize]; t[0]=0;
	double v[tsize]; v[0]=v0;
	double x[tsize]; x[0]=x0;

	// Abre docuemento en el que se almacenarán los datos
  std::ofstream outfile ("edificio.txt");

	//cout << RungeKuttaIncrement(x[0],eq2) << endl << RungeKuttaIncrement(v[0],eq1) << endl;


	for(int i=1;i<tsize;i++)
	{
		v[i]=v[i-1]+RungeKuttaIncrement(t[i-1],x[i-1],eq2);  // Solucionar un paso para la ecuación (2)
		x[i]=x[i-1]+RungeKuttaIncrement(t[i-1],v[i],eq1);  // Solucionar un paso para la ecuación (1)
		t[i]=t[i-1]+dt; // llevar la cuenta del tiempo
	}

	for(int i=0;i<tsize;i++)
	{
		outfile << t[i] << " " << x[i] << endl;
	}

	std::cout << std::endl << "Condiciones iniciales (Caso 1) almacenadas en edificio.txt  " << std::endl;
	outfile.close ();

}
