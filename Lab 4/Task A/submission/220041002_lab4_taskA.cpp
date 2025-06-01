#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <limits>

using namespace std;

#define ll long long
#define vvp vector<vector<pair<ll,ll>>>

class heap_pair{
    public :
        ll node, distance;
        heap_pair(ll a,ll b): node(a),distance(b){}
        bool operator < (const heap_pair &next) const{
            return distance>next.distance;
        }
};

void my_custome_dijkastra(vvp  &adjency_list,ll n){
    ll dist[n+1];
    bool visited[n+1];
    dist[0]=dist[1]=0;
    fill(dist+2,dist+n+1,numeric_limits<ll>::max());
    fill(visited,visited+n+1,false);

    priority_queue<heap_pair> q;
    q.push({1,0});
    
    while(!q.empty()){
        heap_pair contasiner_temporary = q.top();
        q.pop();
        ll u = contasiner_temporary.node;
        if (visited[u]) continue;
        visited[u] = true;

        for (auto &a: adjency_list[u]){
            ll v= a.first;
            ll w = a.second;
            if(dist[v]>dist[u]+w){
                dist[v] = dist[u]+w;
                if(!visited[v]) q.push({v,dist[v]});
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