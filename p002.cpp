#include<iostream>
using namespace std;
const int limit = 4000000;

long long solve(){
    /*
        every 3rd number in fibonacci is even
        0,1,1,2,3,5,8,13,21,34,55,89,144
        t_n = 4*t_(n-1) + t_(n-2)
    */
    long long t_0 = 2;
    long long t_1 = 8;
    long long sum = 0;
    
    sum += t_0;
    sum += t_1;

    while(true){
        long long t_2 = 4*t_1 + t_0;
        if(t_2 >= limit) 
            break;
        sum += t_2;
        t_0 = t_1;
        t_1 = t_2;
    }
    return sum; 
}

int main(){
    cout<<solve();
}