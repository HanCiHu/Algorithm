#include<stdio.h>

int arr[100001] = {0, };
int tree[400001] = {0, };
int N;

void init(int node, int start, int end) {
  if (start == end) tree[node] = start;
  else {
    init(node * 2, start, (start + end) / 2);
    init(node * 2 + 1, (start + end) / 2 + 1, end);

    if (arr[tree[node * 2]] <= arr[tree[node * 2 + 1]]) tree[node] = tree[node * 2];
    else tree[node] = tree[node * 2 + 1];
  }
}

int query(int node, int start, int end, int left, int right) {
  if (left > end || right < start) return -1;
  if (left <= start && right >= end) return tree[node];

  int a = query(node * 2, start, (start + end) / 2, left, right);
  int b = query(node * 2 + 1, (start + end) / 2 + 1, end, left, right);

  if (a == -1) return b;
  if (b == -1) return a;
  if (arr[a] <= arr[b]) return a;
  return b;
}

int max(int a, int b) {
  return a > b ? a : b;
}

int solved(int left, int right) {
  int m = query(1, 0, N - 1, left, right);
  int ans = (right - left + 1) * arr[m];

  if (m - 1 >= left) ans = max(ans, solved(left, m - 1));
  if (m + 1 <= right) ans = max(ans, solved(m + 1, right));

  return ans;
}

int main() {
  scanf("%d", &N);
  for (int i = 0; i < N; i++) scanf("%d", &arr[i]);
  init(1, 0, N - 1);
  printf("%d\n", solved(0, N - 1));
}