#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  vector<int> arr = vector<int>();
  int t, a, b;
  while(cin >> t) arr.push_back(t);
  sort(arr.begin(), arr.end());
  // Part 1
  for (int i : arr) {
    for (int j : arr) {
      if (i + j == 2020) {
        a = i;
        b = j;
        break;
      }
    }
  }
  // Part 2
  int c;
  for (int i : arr) {
    for (int j : arr) {
      for (int k : arr) {
        if (i + j + k == 2020) {
          a = i;
          b = j;
          c = k;
          break;
        }
      }
    }
  }
  cout << a * b * c;
}
