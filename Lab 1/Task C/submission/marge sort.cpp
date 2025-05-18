#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define f(i,a,b) for(ll i=a;i<b;i++)

void margeSortNormal(ll *arr, ll s, ll e){
    if(s>=e) return;
    ll mid = (s+e)/2;
    margeSortNormal(arr,s,mid);
    margeSortNormal(arr,mid+1,e);
    ll temp[e-s+1];
    ll i=s,j=mid+1,k=0;
    while(i<=mid && j<=e){
        if(arr[i]<arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while(i<=mid) temp[k++] = arr[i++];
    while(j<=e) temp[k++] = arr[j++];
    f(i,s,e+1) arr[i] = temp[i-s];
}

void margeSortReverse(ll *arr, ll s, ll e){
    if(s>=e) return;
    ll mid = (s+e)/2;
    margeSortReverse(arr,s,mid);
    margeSortReverse(arr,mid+1,e);
    ll temp[e-s+1];
    ll i=s,j=mid+1,k=0;
    while(i<=mid && j<=e){
        if(arr[i]>arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while(i<=mid) temp[k++] = arr[i++];
    while(j<=e) temp[k++] = arr[j++];
    f(i,s,e+1) arr[i] = temp[i-s];
}

void margeSortAbs(ll *arr, ll s, ll e){
    if(s>=e) return;
    ll mid = (s+e)/2;
    margeSortAbs(arr,s,mid);
    margeSortAbs(arr,mid+1,e);
    ll temp[e-s+1];
    ll i=s,j=mid+1,k=0;
    while(i<=mid && j<=e){
        if((abs(arr[i])<abs(arr[j])) || ((abs(arr[i]) == abs(arr[j])) && (arr[i]<arr[j]))) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while(i<=mid) temp[k++] = arr[i++];
    while(j<=e) temp[k++] = arr[j++];
    f(i,s,e+1) arr[i] = temp[i-s];
}

int main(){
    ll n;
    cin>>n;
    ll arr[n];
    f(i,0,n) cin>>arr[i];
    margeSortNormal(arr,0,n-1);
    f(i,0,n) cout<<arr[i]<<" ";
    cout<<endl;
    margeSortReverse(arr,0,n-1);
    f(i,0,n) cout<<arr[i]<<" ";
    cout<<endl;
    margeSortAbs(arr,0,n-1);
    f(i,0,n) cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}