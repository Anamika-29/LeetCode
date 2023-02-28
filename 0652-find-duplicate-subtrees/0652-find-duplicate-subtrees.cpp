/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
 public:
  vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
    vector<TreeNode*> ans;
    unordered_map<string, int> count;
    encode(root, count, ans);
    return ans;
  }

 private:
  string encode(TreeNode* root, unordered_map<string, int>& count,
                vector<TreeNode*>& ans) {
    if (root == nullptr)
      return "";

    const string encoded = to_string(root->val) + "#" +
                           encode(root->left, count, ans) + "#" +
                           encode(root->right, count, ans);
                           //# for encoding null left and right childs
    if (++count[encoded] == 2)//duplicate subtree
      ans.push_back(root);//add the roots
    return encoded;
  }
};