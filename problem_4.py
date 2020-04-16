class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
      return True
    else:
      for gr in group.get_groups():
        if is_user_in_group(user,gr):
          return True
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user",parent))


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_sub_child = Group("subsubchild")
sub2_child = Group("sub2child")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_sub_child_user = "sub_sub_child_user"
sub_sub_child.add_user(sub_sub_child_user)

child.add_group(sub_child)
sub_child.add_group(sub_sub_child)
child.add_group(sub2_child)
parent.add_group(child)

print(is_user_in_group("sub_sub_child_user",parent))
print(is_user_in_group("sub_child_user",sub2_child))