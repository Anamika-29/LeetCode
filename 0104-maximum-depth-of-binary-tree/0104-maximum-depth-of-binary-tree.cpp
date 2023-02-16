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
    int maxDepth(TreeNode* root) {
        return maxDepthUtil(root, 0);
    }
    
    int maxDepthUtil(TreeNode* root, int count) {
        if (root==NULL) return count;
        count++;
        int countLeft = count, countRight = count;
        
        countLeft = maxDepthUtil(root->left, countLeft++);
        countRight = maxDepthUtil(root->right, countRight++);
        return max(countLeft, countRight);
        
    }    
};