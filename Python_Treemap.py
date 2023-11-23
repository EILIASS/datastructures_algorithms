class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has a left child
        if self.left is not None:
            self.left.display_keys(space, level + 1)

        # If the node has a right child
        if self.right is not None:
            self.right.display_keys(space, level + 1)

        print(space * level + str(self.key))
           
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

print(tree_tuple)

tree = TreeNode.parse_tuple(tree_tuple)

print(tree)

print(tree.display_keys('  '))

print(tree.height())

print(tree.size())

print(tree.traverse_in_order())

print(tree.to_tuple())

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key

# The following tree is not a BST 
# (because a node with the key 3 
# appears in the left subtree of a node with the key é
tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))

print(is_bst(tree1))

# Let's create this tree and verify that it is a BST. 
# Note that the TreeNode class also supports 
# using strings as keys, as strings support 
# the comparison operators < and > too
tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))

print(is_bst(tree2))

# Storing Key-Value Pairs using BSTs

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has a left child
        if self.left is not None:
            self.left.display_keys(space, level + 1)

        # If the node has a right child
        if self.right is not None:
            self.right.display_keys(space, level + 1)

        print(space * level + str(self.key))
        
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def tree_height(self):
        return self.height()

# Let's try to recreate this BST
# with usernames as keys and user objects as values:

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        

# Create a User instance
users = [User(username='aakash', name='Aakash Rai', email='aakash@example.com'),
 User(username='biraj', name='Biraj Das', email='biraj@example.com'),
 User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com'),
 User(username='jadhesh', name='Jadhesh Verma', email='jadhesh@example.com'),
 User(username='siddhant', name='Siddhant Sinha', email='siddhant@example.com'),
 User(username='sonaksh', name='Sonaksh Kumar', email='sonaksh@example.com'),
 User(username='vishal', name='Vishal Goel', email='vishal@example.com')]

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# Level 0
tree = BSTNode(jadhesh.username, jadhesh)


# View Level 0
print(tree.key, repr(tree.value))

# Level 1
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)

# View Level 1
output = (tree.left.key, tree.left.value, tree.right.key, tree.right.value)


# View Level 1
print(output)

# We can use the same display_keys function 
# we defined earlier to visualize our tree
 
# View Level 1
output1  = (tree.left.key, repr(tree.left.value), tree.right.key, repr(tree.right.value))

# View Level 1
print(output1)

# Utilisez la fonction display_keys sur l'instance tree

print(tree.display_keys())

# Here's a recursive implementation of insert.
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

# To create the first node, we can use 
# the insert function with None as the target tree.
tree = insert(None, jadhesh.username, jadhesh)

insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

print(tree.display_keys())

# Note, however, that the order of insertion 
# of nodes change the structure of the resulting tree.
tree2 = insert(None, aakash.username, aakash)

insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)

print(tree2.display_keys())

print(tree2.height())

# ecursive strategy similar to insertion to find 
# the node with a given key within a BST
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    
node = find(tree, 'hemanth')

print(node.key, node.value)

# Updating a value in a BST

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
        
update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))

node = find(tree, 'hemanth')

print(node.value)

# List the nodes
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
print(list_all(tree))

# Balanced Binary Trees
def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

print(is_balanced(tree))

print(is_balanced(tree2))

# Balanced Binary Search Trees

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root

data = [(user.username, user) for user in users]
print(data)

tree = make_balanced_bst(data)
print(tree.display_keys())

# Balancing an Unbalanced BST

def balance_bst(node):
    return make_balanced_bst(list_all(node))

tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)

print(tree1.display_keys())

tree2 = balance_bst(tree1)

print(tree2.display_keys())


class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self.root is None:
            print(space * level + '∅')
            return   

        # If the node is a leaf 
        if self.root.left is None and self.root.right is None:
            print(space * level + str(self.root.key))
            return

        # If the node has a left child
        if self.root.left is not None:
            self.root.left.display_keys(space, level + 1)

        # If the node has a right child
        if self.root.right is not None:
            self.root.right.display_keys(space, level + 1)

        print(space * level + str(self.root.key))

    def size(self):
        return TreeNode.size(self.root)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return self.size()

    def display(self):
        self.display_keys()

print(users)

treemap = TreeMap()

print(treemap.display())

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

print(treemap.display())

print(treemap['jadhesh'])

print(len(treemap))

treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal

print(treemap.display())

for key, value in treemap:
    print(key, value)
    
print(list(treemap))

treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')

print(treemap['aakash'])