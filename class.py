class Tree:
    def __init__(self, name, height, leaves):
        self.name = name
        self.height = height
        self.leaves = leaves
    
    def count_leaves(self):
        return self.leaves
    
oak = Tree("Oak", 15, 20000)
maple = Tree("Maple", 20, 15000)

print(f"The {oak.name} tree has {oak.count_leaves()} leaves.")
print(f"The {maple.name} tree has {maple.count_leaves()} leaves.")
