#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		string s;
		int i = 0;
		int f = 0;
		while(i < n){
			if(f == 0) {
				s += "01";
				f++
			}
			else if(f == 1){
				 s += "10";
				 f--;
			}
			i+=2;
		}
		string str;
		for(int i = 0; i<n;i++){
			str += s[i];
		}
		cout<<str<<endl;
	}
	return 0;
}