#include<iostream>
#include<conio.h>

using namespace std;

extern "C" float interpolation(float *x, float *f, int n, float value)
{
    float sum=0,mult;

    for(int j=0; j < n-1; j++)
    {
        for(int i=n-1; i > j; i--){
            f[i]=(f[i]-f[i-1])/(x[i]-x[i-j-1]);
		}
    }

    for(int i=n-1; i >= 0; i--)
    {
        mult=1;
        for(int j=0; j < i; j++){
            mult*=(value-x[j]);
		}
            
        mult*=f[i];
        sum+=mult;
    }

    return sum;
}