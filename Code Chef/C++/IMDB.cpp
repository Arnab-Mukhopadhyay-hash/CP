#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n, x, r=0;
		cin>>n>>x;
		while(n--){
			int si, ri;
			cin>>si>>ri;
			if(si<=x && ri>r){
				r = ri;
			}
		}
		cout<<r<<endl;
	}
	
	return 0;
}
