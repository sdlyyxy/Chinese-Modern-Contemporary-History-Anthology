import os
_root = os.getcwd()
dep=0
for root, dirs, files in os.walk('.'):
    tab=''
    for c in root:
        if c=='/':tab+='\t'
    if root[:6]=='./.git':continue
    if root=='./.vscode':continue
    if root!='.':
        print('%s* %s'%(tab[1:],root[2:]))
    for name in files:
        if name=='.DS_Store':continue
        if name=='.gitignore':continue
        if name=='mk_toc.py':continue
        if name=='README.md':continue
        if name=='tmp':continue
        print ('%s* [%s](%s)' % (tab,name[:-3], root+name) )
