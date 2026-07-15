//Maximum Depth of Binary Tree

#include <iostream>
#include <stdlib.h>
#include <algorithm>

struct TreeNode
{
    int value;
    TreeNode* leftchild;
    TreeNode* rightchild;

    //Default constructor
    TreeNode(): value(), leftchild(nullptr), rightchild(nullptr){};
    //Parameterized constructor
    TreeNode(int x): value(x), leftchild(nullptr), rightchild(nullptr){};
};


class Solution:
{
    public:
        int MaxDepth(TreeNode*root)
        {
        // Zoals bij InvertBinary Tree ga je dus recursief naar beneden en voer je 
        // per keer naar beneden de operatie uit (daar swap), hier dus tellen.
        // Er moet ook een maximum bijgehouden worden

        // Als boom leeg is, dan is diepte nul (dus ook als je helemaal onderaan bent)
        // En je gaat dus recursief weer naar boven?
        // Want iedere node heeft wegens recursie zijn eigen root?
        // Zoals bij andere opgave zetten we eerst de basecase neer en daarna
        // initialiseren we pas. Check of dat klopt
        if(root==nullptr)
        {
            return 0;
        }

        return max(maxDepth(root->linkerkinder), maxDepth(root->rechterkind));


};


int main()
{
    //Nodes bouwen
    TreeNode* root = new TreeNode(1);
    root->leftchild = new TreeNode(2);
    root->rightchild = new TreeNode(3);
    root->rightchild->leftchild = new TreeNode(4);

    // Hier oplossing oproepen
    Solution sol;
    cout<<sol.maxDepth(root)<< endl;

    return 0;


}


