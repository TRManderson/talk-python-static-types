class NonEmptyConsList(object):
    def __init__(self, value, rest=None):
        self.value = value
        self.rest = rest

    def length(self):
        if self.rest is not None:
            return 1 + self.rest.length()
        else:
            return 1


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_height(self):
        options = [0]
        if self.left is not None:
            options.append(self.left.get_height())
        if self.right is not None:
            options.append(self.right.get_height())
        return 1 + max(options)
