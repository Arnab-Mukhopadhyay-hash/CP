#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		string s;
		cin>>s;
		map<char, int> m;
		for(auto i: s){
			if(m.find(i) == m.end()){
				// element not found
				m.insert({i, 1});
			}
			else{
				// element is present in the array
				auto t = m.find(i);
				t->second++;
			}
		}
		string f = "YES";
		for(auto itr: m){
			if(itr.second%2 != 0) f="NO";
		}
		cout<<f<<endl;
	}
	return 0;
}
