# 01 번 1991 - 트리 순회

'''
import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
'''

import sys
input = sys.stdin.readline

N = int(input().strip()) # .strip 공/여백 삭제
tr = {} # 딕 셔 너 리

for n in range(N):
    root, left, right = input().strip().split() 
    # input : A B C 이런식으로 한줄씩..! 들어오는데 root left right 식으로 저장 후에 
    tr[root] = [left, right] # 요런싟으로 저장 #딕셔너리 저장법
    
def preorder(root): # 전위
    if root != '.':
        print(root, end='')
        preorder(tr[root][0])
        preorder(tr[root][1])

def inorder(root):
    if root != '.':
        inorder(tr[root][0])
        print(root, end = '')
        inorder(tr[root][1])

def postorder(root):
    if root != '.':
        postorder(tr[root][0])
        postorder(tr[root][1])
        print(root, end='')
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
    
