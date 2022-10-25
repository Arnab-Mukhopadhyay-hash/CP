#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n, a, b, c;
		cin>>n>>a>>b>>c;
		if(b < n) cout<<"NO"<<endl;
		else if(a+c < n) cout<<"NO"<<endl;
		else cout<<"YES"<<endl;
	}
	return 0;
}
