#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		float s, a, b, c;
		cin>>s>>a>>b>>c;
		float mktPrice = s + (s*(c/100));
		cout<<mktPrice<<endl;
		if(a <= mktPrice && mktPrice <= b) cout<<"Yes"<<endl;
		else cout<<"No"<<endl;
	}
	return 0;
}
