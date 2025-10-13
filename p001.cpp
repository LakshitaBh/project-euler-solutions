#include <bits/stdc++.h>
using namespace std;

const int limit = 1000;

int solve(){
    int sum = 0;
    for(int i=1;i<limit;i++){
        sum += (i%3==0||i%5==0)?i:0;
    }
    return sum;
}

int main(){
    cout<<solve()<<endl;
}
