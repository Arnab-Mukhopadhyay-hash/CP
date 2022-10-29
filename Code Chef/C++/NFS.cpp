#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int u, v, a, s;
		cin>>u>>v>>a>>s;
		int v2 = pow(v, 2);
		int u2 = pow(u, 2);
		if(v2 >= u2 - (2*a*s)) cout<<"Yes"<<endl;
		else cout<<"No"<<endl;
	}
	// here we need to consider deacceleration
	return 0;
}
