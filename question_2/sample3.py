# pyminifier -O dataset/pyminifier/script_1_obfs.py > dataset/pyminifier/script_1_obfs.py

from collections.abc import Mapping
c=isinstance
p=len
N=repr
I=staticmethod
m=enumerate
g=ValueError
Q=str
d=tuple
import abc
class K(A):
 def __init__(l,C):
  if not c(C,A):
   C={k:v for k,v in l.z(C)}
  l._store={k.lower():(k,v)for k,v in C.items()}
 def __getitem__(l,key):
  return l._store[key.lower()][1]
 def __len__(l):
  return p(l._store)
 def __eq__(l,n):
  U={k.lower():v for k,v in l.items()}
  e={k.lower():v for k,v in n.items()}
  return c(n,A)and U==e
 def __iter__(l):
  o=[original_key for original_key,value in l._store.values()]
  return o
 def __repr__(l):
  return N({key:value for key,value in l._store.values()})
 def P(l):
  return l
 @I
 def z(C):
  for i,elem in m(C):
   if p(elem)!=2:
    raise g('dictionary update sequence element #{} has length {}; 2 is required.'.format(i,p(elem)))
   if not c(elem[0],Q):
    raise g('Element key %s invalid, only strings are allowed'%elem[0])
   yield d(elem)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

