<<<<<<< HEAD
/*Tarea 2 métodos computacionales. Punto 2
  EDO: Un edificio en un sismo*/
=======
/*
*   TAREA 2 METODOS
*/
>>>>>>> b5b4b650952910833c596410b8fcada37410b6ea

#include <iostream>
#include <fstream>
#include <math.h>

double m=1000.0; //Masa de cada piso
double k=2000.0; //Cte de rigidez de la estructura
double y=0; //gamma, coeficiente de yción
double w=1.0*sqrt(k/m);
double dt=0.01;
double t_fin=10.0; //tiempo final del sistema
int n = int(t_fin/dt); //Numero de puntos

double *u1 = NULL,*u2 = NULL, *u3 = NULL, *v1 = NULL,*v2, *v3 = NULL;

//Ecuación 1: F(t) = sin(ωt)
double F( double w, double t )
{
    return sin(w*t);
}

//Sistema de ecuaciones diferenciales de segundo orden que describen el sismo
double d2u1(int i, double w){
    return (1/m)*(-y*v1[i] -2*k*u1[i] + k*u2[i] + F(w,dt*i));
}
double d2u2(int i)
{
    return (1/m)*(-y*v2[i]+k*u1[i]-2*k*u2[i]+k*u3[i]);
}
double d2u3(int i)
{
    return (1/m)*(-y*v3[i]+k*u2[i]-k*u3[i]);
}

int main(){
    u1  = new double[n];
    u2  = new double[n];
    u3  = new double[n];
    v1  = new double[n];
    v2  = new double[n];
    v3  = new double[n];

    u1[0] = 0;
    u2[0] = 0;
    u3[0] = 0;
    v1[0] = 0;
    v2[0] = 0;
    v3[0] = 0;


    //Método de LeapFrog
    for(int i=1; i<n; i++){
        double v11 = v1[i-1]+d2u1(i-1, w)*dt/2;
        double v22 = v2[i-1]+d2u2(i-1)*dt/2;
        double v33 = v3[i-1]+d2u3(i-1)*dt/2;

        u1[i] = u1[i-1] + v11*dt;
        u2[i] = u2[i-1] + v22*dt;
        u3[i] = u3[i-1] + v33*dt;

        v1[i] = v11+d2u1(i,w)*(dt/2);
        v2[i] = v22+d2u2(i)*(dt/2);
        v3[i] = v33+d2u3(i)*(dt/2);
    }

    return 0;
}
