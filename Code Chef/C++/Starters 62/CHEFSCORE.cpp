#include<bits/stdc++.h>
using namespace std;
int main(){
	// n*x >=y
	int t;
	cin>>t;
	while(t--){
		int n, x, y;
		cin>>n>>x>>y;
		if(n*x >= y && y%x == 0) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}
