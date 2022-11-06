#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int arr[n];
		for(int i = 0; i<n;i++){
			cin>>arr[i];
		}
		unordered_map<int, int> map;
		for(auto i: arr){
			if(map.find(i) == map.end()){
				map.insert({i, 1});
			}
			else{
				map.at(i)++;
			}
		}
		for(auto t: map){
			if(t.second%2 != 0) cout<<t.first<<endl;
		}
	}
	return 0;
}
