#!/usr/bin/env python


from mercurial import (
    commands,
    localrepo,
    ui as uimod,
)

u = uimod.ui.load()

print('% creating repo')
repo = localrepo.localrepository(u, '.', create=True)

f = open('test.py', 'w')
try:
    f.write('foo\n')
finally:
    f.close

print('% add and commit')
commands.add(u, repo, 'test.py')
commands.commit(u, repo, message='*')
commands.status(u, repo, clean=True)


print('% change')
f = open('test.py', 'w')
try:
    f.write('bar\n')
finally:
    f.close()

# this would return clean instead of changed before the fix
commands.status(u, repo, clean=True, modified=True)
