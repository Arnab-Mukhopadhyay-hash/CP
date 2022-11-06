#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		string s;
		if(n%2 == 0){
			for(int i = 0; i < n-2; i++){
				s += "0";
			}
			s = "1" + s + "1";
		}
		else{
			for(int i = 0; i < n/2; i++){
				s += "01";
			}
			s += "0";
		}
		cout<<s<<endl;
	}
	return 0;
}