#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n, s;
		cin>>n>>s;
		int t1 = n;
		int t2 = s - n;
		if(n>s) cout<<s<<endl;
		else if(t1 > t2) cout<<t1-t2<<endl;
		else cout<<t2-t1<<endl;
	}
	return 0;
}
