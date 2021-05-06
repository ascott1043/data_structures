
class TreeNode:
    def __init__(self, data, title=None):
        self.data = data
        self.children = []
        self.parent = None
        self.title = title

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        node = self
        current_level = 0
        while node.parent:
            current_level += 1
            node = node.parent
        return current_level

    def __str__(self):
        tree = self.data
        tree += '\n'
        for child in self.children:
            tree += '\t' * child.get_level()
            tree += child.__str__()
        return tree

    def print_org(self, option):
        if option.lower() == 'name':
            tree = self.data
        elif option.lower() == 'designation':
            tree = self.title
        else:
            tree = self.data + ' > ' + self.title

        tree += '\n'
        for child in self.children:
            tree += '\t' * child.get_level()
            tree += child.print_org(option)
        return tree  

    def print_geo(self, level, current=0):
        tree = self.data + '\n'
        if current + 1< level:
            for child in self.children:
                tree += '\t' * child.get_level()
                tree += child.print_geo(level, current+1)
        return tree

        



def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Dell"))

    cellphone = TreeNode("Cell Phone")
    iphone = TreeNode("iPhone")
    iphone.add_child(TreeNode("iPhone 8"))
    iphone.add_child(TreeNode("iPhone 11"))
    cellphone.add_child(iphone)
    
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

def build_company_org_tree():

    nilupul = TreeNode('Nilupul','CEO')
    chinmay = TreeNode('Chinmay', 'CTO')
    vishwa = TreeNode('Vishwa', 'Infrastructure Head')
    dhaval = TreeNode('Dhaval','Cloud Manager')
    abhijit = TreeNode('Abhijit','App Manager')
    aamir = TreeNode('Aamir', 'Application Head')
    gels = TreeNode('Gels','HR Head')
    peter = TreeNode('Peter','Recruitment Manager')
    waqas = TreeNode('Waqas', 'Policy Manager')

    nilupul.add_child(chinmay)
    chinmay.add_child(vishwa)
    vishwa.add_child(dhaval)
    vishwa.add_child(abhijit)
    chinmay.add_child(aamir)
    nilupul.add_child(gels)
    gels.add_child(peter)
    gels.add_child(waqas)

    return nilupul

def build_geo_tree():
    world = TreeNode('Global')
    india = TreeNode('India')
    usa = TreeNode('USA')
    gujarat = TreeNode('Gujarat')
    karnataka = TreeNode('Karnataka')
    nj = TreeNode('New Jersey')
    cali = TreeNode('California')

    world.add_child(india)
    world.add_child(usa)
    india.add_child(gujarat)
    india.add_child(karnataka)
    usa.add_child(nj)
    usa.add_child(cali)

    return world


if __name__ == '__main__':
    root = build_product_tree()
    print(root)

    root = build_company_org_tree()
    print(root.print_org('both'))


    root = build_geo_tree()
    print(root.print_geo(3))