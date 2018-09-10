# 重构二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。 

```python
def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)
```


```python
def middle_digui(self, root):
    """利用递归实现树的中序遍历"""
    if root == None:
        return
    self.middle_digui(root.lchild)
    print root.elem,
    self.middle_digui(root.rchild)
```


```python
def later_digui(self, root):
    """利用递归实现树的后序遍历"""
    if root == None:
        return
    self.later_digui(root.lchild)
    self.later_digui(root.rchild)
    print root.elem
```


```python
def level_queue(self, root):
        """Breadth frist search"""
        if root == None:
            return None
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.elem,
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)
```



