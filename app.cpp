#include <bits/stdc++.h>
using namespace std;

int findLIS(const vector<int>& seq, int n, int k) {
    vector<int> dp(n, 1);
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (seq[j] < seq[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int lis = *max_element(dp.begin(), dp.end());
    return max(0, lis - (k - 1));
}

int findLDS(const vector<int>& seq, int n, int k) {
    vector<int> dp(n, 1);
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (seq[j] > seq[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int lds = *max_element(dp.begin(), dp.end());
    return max(0, lds - (k - 1));
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> b(n);
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    
    int changes_LIS = findLIS(b, n, k);
    int changes_LDS = findLDS(b, n, k);
    int m = max(changes_LIS, changes_LDS);
    
    vector<int> a = b;
    for (int i = 0; i < m; ++i) {
        a[i] = 0;
    }
    
    cout << m << endl;
    for (int num : a) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}