#include <bits/stdc++.h>
using namespace std;

#define ll long long int

void CustomSwap(ll &a, ll &b){
    int temp= a;
    a=b;
    b=temp;
}

int main(){
    ll a,b;
    cin>>a>>b;
    CustomSwap(a,b);
    cout<<a<<" "<<b;
    return 0;
}