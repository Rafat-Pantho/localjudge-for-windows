#include <iostream>
#include <queue>
#include <utility>
#include <limits>

using namespace std;

#define ll long long
#define vvp vector<vector<pair<ll,ll>>>

void my_custome_dijkastra(vvp  &adjency_list,ll n){
    ll dist[n+1];
    bool visited[n+1];
    dist[0]=dist[1]=0;
    fill(dist+2,dist+n+1,numeric_limits<int>::max());
    fill(visited,visited+n+1,false);

    queue <ll> q;
    q.push(1);
    visited[1] = true;
    
    while(!q.empty()){
        ll u = q.front();
        q.pop();
        visited[u] = false;

        for (auto &a: adjency_list[u]){
            ll v= a.first;
            ll w = a.second;
            if(dist[v]>dist[u]+w){
                dist[v] = dist[u]+w;
                if(!visited[v]){
                    q.push(v);
                    visited[v] = true;
                }
            }
        }
    }
    for(ll i=1;i<=n;i++){
        cout<<dist[i]<<" ";
    }
    cout<<endl;
}

int main(){
    ll n,m;cin>>n>>m;
    vvp adjency_list(n+1);

    for(ll i=0;i<m;i++){
        ll u,v,w;cin>>u>>v>>w;
        adjency_list[u].push_back({v,w});
    }

    my_custome_dijkastra(adjency_list,n);

    return 0;
}