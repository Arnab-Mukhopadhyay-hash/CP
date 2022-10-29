#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int w1, w2, x1, x2, M;
		cin>>w1>>w2>>x1>>x2>>M;
		int lw = w1 + x1*M;
		int hw = w1 + x2*M;
		if(lw <= w2 && w2 <= hw) cout<<1<<endl;
		else cout<<0<<endl;
	}
	return 0;
}
