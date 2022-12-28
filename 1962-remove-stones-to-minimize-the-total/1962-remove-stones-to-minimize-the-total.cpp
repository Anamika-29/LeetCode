class Solution {
public:
    int minStoneSum(vector<int>& p, int k) {
    make_heap(begin(p), end(p));
    while (--k >= 0) {
        pop_heap(begin(p), end(p));
        p.back() -= p.back() / 2;
        push_heap(begin(p), end(p));
    }
    return accumulate(begin(p), end(p), 0);
}
};