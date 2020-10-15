class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

#include<queue>

class Solution {
public:
    Node* connect(Node* root) {
    	
    	Node* temp_node;
    	
			queue<Node* >temp;
			temp.push(root);
			
			while(*temp.front()!=NULL){
				
				if(temp.size()==1){
					temp.front()->next=NULL;
				}else{
					temp.front()->next=temp[1];
				}
				temp.push(temp.front()->left);
				temp.push(temp.front()->right);
                temp.pop()
			}
			
		}
    }
};
