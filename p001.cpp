#include <iostream>
using namespace std;

const int limit = 1000;

int solve(int div){
    int lastMultiple = (limit-1)/div;
    return div*(lastMultiple)*(lastMultiple+1)/2;
}

int main(){
    int sum = solve(3) + solve(5) - solve(15);
    cout<<sum;
}