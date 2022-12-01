import os
import io
_root = os.getcwd()
dep = 0
f=open('README.md',"r+")
f.readline()
f.readline()
f.seek(0,io.SEEK_CUR)
for root, dirs, files in os.walk('.'):
    dirs.sort()
    files.sort()
    tab = ''
    for c in root:
        if c == '/':
            tab += '\t'
    if root[:6] == './.git':
        continue
    if root == './.vscode':
        continue
    if root == './assets':
        continue
    pos = 0
    for index, c in enumerate(root):
        if c == '/':
            pos = index + 1
    if root != '.':
        print('%s* [%s](%s)' % (tab[1:], root[pos:], root),file=f)
    for name in files:
        if name == '.DS_Store':
            continue
        if name == '.gitignore':
            continue
        if name == 'mk_toc.py':
            continue
        if name == 'README.md':
            continue
        if name == 'tmp':
            continue
        print ('%s* [%s](%s)' % (tab, name[:-3], root + '/' + name),file=f)

f.truncate(f.tell())