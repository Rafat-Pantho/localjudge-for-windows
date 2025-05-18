#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define f(i,a,b) for(ll i=a;i<b;i++)

void bubbleSortNormal(ll *arr, ll n){
    f(i,0,n-1){
        int flag = 0;
        f(j,0,n-i-1){
            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
                flag = 1;
            }
        }
        if(flag == 0) break;
    }
}

void bubbleSortReverse(ll *arr, ll n){
    f(i,0,n-1){
        int flag = 0;
        f(j,0,n-i-1){
            if(arr[j]<arr[j+1]){
                swap(arr[j],arr[j+1]);
                flag = 1;
            }
        }
        if(flag == 0) break;
    }
}

void bubbleSortAbs(ll *arr, ll n){
    f(i,0,n-1){
        int flag = 0;
        f(j,0,n-i-1){
            if((abs(arr[j])>abs(arr[j+1])) || ((abs(arr[j]) == abs(arr[j+1])) && (arr[j]>arr[j+1]))){
                swap(arr[j],arr[j+1]);
                flag = 1;
            }
        }
        if(flag == 0) break;
    }
}

int main(){
    ll n;
    cin>>n;
    ll arr[n];
    f(i,0,n) cin>>arr[i];
    bubbleSortNormal(arr,n);
    f(i,0,n) cout<<arr[i]<<" ";
    cout<<endl;
    bubbleSortReverse(arr, n);
    f(i,0,n) cout<<arr[i]<<" ";
    cout<<endl;
    bubbleSortAbs(arr,n);
    f(i,0,n) cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}