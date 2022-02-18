#include <iostream>
#include <queue>

using namespace std;

struct cmp {
  bool operator()(int a, int b){
    if (abs(a) == abs(b)) return a > b;
    return abs(a) > abs(b);
  }
};

int main(){
  int n, num;
  cin >> n;

  priority_queue<int, vector<int>, cmp> pq;

  for (int i = 0; i < n; i++){
    cin >> num;

    if (num == 0) {
      if (pq.empty()) {
        cout << '0' << '\n';
        continue;
      }
      cout << pq.top() << '\n';
      pq.pop();
    }
    else pq.push(num);
  }
}