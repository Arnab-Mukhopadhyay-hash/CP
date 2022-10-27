#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int a, b, c;
		cin>>a>>b>>c;
		int maxx = max(a, max(b, c));
		int minn = min(a, min(b, c));
		int secondMax;
		if(maxx == a) secondMax = max(b, c);
		else if(maxx == b) secondMax = max(a, c);
		else secondMax = max(a, b);
		cout<<maxx+secondMax<<endl;
	}
	return 0;
}
