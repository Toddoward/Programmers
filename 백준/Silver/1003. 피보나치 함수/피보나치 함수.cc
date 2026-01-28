#include <iostream>

using namespace std;

struct M {
    long long d[2][2];
};

M mul(M a, M b) {
    M res = {0, 0, 0, 0};
    for (int i = 0; i < 2; i++)
        for (int k = 0; k < 2; k++)
            for (int j = 0; j < 2; j++)
                res.d[i][j] += a.d[i][k] * b.d[k][j];
    return res;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        if (n == 0) { cout << "1 0\n"; continue; }
        
        M r = {1, 0, 0, 1}, b = {1, 1, 1, 0};
        while (n) {
            if (n % 2) r = mul(r, b);
            b = mul(b, b);
            n /= 2;
        }
        cout << r.d[1][1] << " " << r.d[0][1] << "\n";
    }
    return 0;
}