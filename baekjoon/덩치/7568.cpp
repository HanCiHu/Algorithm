#include <iostream>
#include <utility>
#include<vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	vector<pair<int,int> > people;
	for (int i = 0; i < N; i++){
		int a,b;
		cin >> a >> b;
		people.push_back(make_pair(a,b));
	}
	for (int i = 0; i < N; i++){
		int rank = 1;
		for (int j = 0; j < N; j++){
			if (people[i].first < people[j].first && people[i].second < people[j].second){
				rank++;
			}
		}
		cout << rank << " ";
	}
}