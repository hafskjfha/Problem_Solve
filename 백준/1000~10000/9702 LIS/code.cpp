#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define fastio ios::sync_with_stdio(false); cin.tie(0);cout.tie(0);

int main() {
    fastio;
    int t;
    cin >> t;
    for (int case_num = 1; case_num <= t; ++case_num) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        int c = 0;
        for (int i = 0; i < n; ++i) {
            vector<int> b;
            int l = 0;

            for (int j = i; j < n; ++j) {
                int v = a[j];
                if (b.empty() || b.back() < v) {
                    b.push_back(v);
                    l++;
                } else {
                    auto pos = lower_bound(b.begin(), b.end(), v);
                    *pos = v;
                }
                c += l;
            }
        }
        cout << "Case #" << case_num << ": " << c << '\n';
    }
    return 0;
}
