# Breadth First Search

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

 

# N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a `3-ary` tree:

 

![img](https://leetcode.com/static/images/problemset/NaryTreeExample.png)

 

We should return its level order traversal:

 

 

```
[
     [1],
     [3,2,4],
     [5,6]
]
```

 

**Note:**

1. The depth of the tree is at most `1000`.
2. The total number of nodes is at most `5000`.