
# The :< operator puts ten spaces in between.
# THe :^ operator puts centre.

print('{a:<10}|{a:^10}|{a:>10}'.format(a='test'))
print('{a:~<10}|{a:~^10}|{a:~>10}'.format(a='test'))

person = {'first':'John','last':'Weaseley'}

print('{p[first]} {p[last]}'.format(p=person))
data =range(100)
print('{d[0]}..{d[1]}...{d[67]}'.format(d=data))