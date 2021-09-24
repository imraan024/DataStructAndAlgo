class Node:  
    def __init__(self,data):  
        #Assign data to the new node, set left and right children to None  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class SearchBinaryTree:  
    def __init__(self):  
        #Represent the root of binary tree  
        self.root = None;  
        self.flag = False;  
      
    #searchNode() will search for the particular node in the binary tree  
    def searchNode(self, temp, value):  
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
          
        else:  
            #If value is found in the given binary tree then, set the flag to true  
            if(temp.data == value):  
                self.flag = True;  
                return;  
              
            #Search in left subtree  
            if(self.flag == False and temp.left != None):  
                self.searchNode(temp.left, value);  
              
            #Search in right subtree  
            if(self.flag == False and temp.right != None):  
                self.searchNode(temp.right, value);  
   
bt = SearchBinaryTree();  
#Add nodes to the binary tree  
bt.root = Node(1);  
bt.root.left = Node(2);  
bt.root.right = Node(3);  
bt.root.left.left = Node(4);  
bt.root.right.left = Node(5);  
bt.root.right.right = Node(6);  
          
#Search for node 5 in the binary tree  
bt.searchNode(bt.root, 8);  
   
if(bt.flag):  
    print("Element is present in the binary tree");  
else:  
    print("Element is not present in the binary tree");  