from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class NonEmptyConsList(Generic[T]):
    value: T
    rest: Optional['NonEmptyConsList[T]']

    def __init__(self, value: T, rest=None) -> None:
        self.value = value
        self.rest = rest

    def length(self) -> int:
        if self.rest is not None:
            return 1 + self.rest.length()
        else:
            return 1


class TreeNode(Generic[T]):
    value: T
    left: Optional['TreeNode[T]']
    right: Optional['TreeNode[T]']

    def __init__(self, value: T, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def get_height(self) -> int:
        options = [0]
        if self.left is not None:
            options.append(self.left.get_height())
        if self.right is not None:
            options.append(self.right.get_height())
        return 1 + max(options)
