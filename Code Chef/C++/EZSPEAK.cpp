#include <iostream>

using namespace std;



int main() {

	int t;

	cin>>t;

	while(t--){

	    int n;cin>>n;

	    string s;cin>>s;

	    int cnt=0;

	    int mx=0;

	    for(auto i:s){

	        if(i=='a' || i=='i' || i=='o' ||i=='u' ||i=='e'){

	            cnt=0;

	        }else{

	            cnt++;

	            if(cnt>mx){

	                mx=cnt;

	            }

	        }

	    }

	    (mx>3) ?cout<<"NO"<<endl:cout<<"YES"<<endl;

	}

	return 0;

}


