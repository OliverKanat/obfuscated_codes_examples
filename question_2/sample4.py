from collections .abc import Mapping #line:1
import abc #line:2
class CaseInsensitiveMapping (Mapping ):#line:5
    ""#line:21
    def __init__ (O0OOOOO000OO0OO00 ,O00OOOOOOOO00O0OO ):#line:23
        if not isinstance (O00OOOOOOOO00O0OO ,Mapping ):#line:24
            O00OOOOOOOO00O0OO ={OOOO0O0OOOO0O0O0O :O00OOOOO000OO0000 for OOOO0O0OOOO0O0O0O ,O00OOOOO000OO0000 in O0OOOOO000OO0OO00 ._destruct_iterable_mapping_values (O00OOOOOOOO00O0OO )}#line:25
        O0OOOOO000OO0OO00 ._store ={OO00O00OO00OO000O .lower ():(OO00O00OO00OO000O ,OO0O0OOO0000OO00O )for OO00O00OO00OO000O ,OO0O0OOO0000OO00O in O00OOOOOOOO00O0OO .items ()}#line:26
    def __getitem__ (O00O000OO0O00OO0O ,OOO0O0O00O0OO0000 ):#line:28
        return O00O000OO0O00OO0O ._store [OOO0O0O00O0OO0000 .lower ()][1 ]#line:29
    def __len__ (O000OOOOO0O000O0O ):#line:31
        return len (O000OOOOO0O000O0O ._store )#line:32
    def __eq__ (O000O0000OOOOO000 ,OO000OO0000OO0O0O ):#line:34
        O0O000000O0O0O0OO ={OO0OO000O00000O0O .lower ():O0O0O0OO0O0OOOO00 for OO0OO000O00000O0O ,O0O0O0OO0O0OOOO00 in O000O0000OOOOO000 .items ()}#line:35
        OOO0O0O00O00OOOOO ={OO00OOOO0O0O0O000 .lower ():OO0OOOOO000OOO000 for OO00OOOO0O0O0O000 ,OO0OOOOO000OOO000 in OO000OO0000OO0O0O .items ()}#line:36
        return isinstance (OO000OO0000OO0O0O ,Mapping )and O0O000000O0O0O0OO ==OOO0O0O00O00OOOOO #line:37
    def __iter__ (OO0OO00O0OOO0000O ):#line:39
        OO00OOO0OOOOOO0OO =[OO000O0OO00OO0OO0 for OO000O0OO00OO0OO0 ,OOOO00OO000OOO00O in OO0OO00O0OOO0000O ._store .values ()]#line:40
        return OO00OOO0OOOOOO0OO #line:41
    def __repr__ (OOOOOOOO0OOO0O00O ):#line:43
        return repr ({OO0O0000OO00OOOO0 :OOO0OO00OOOOOOOOO for OO0O0000OO00OOOO0 ,OOO0OO00OOOOOOOOO in OOOOOOOO0OOO0O00O ._store .values ()})#line:44
    def copy (OOOOO000000O00O00 ):#line:46
        return OOOOO000000O00O00 #line:47
    @staticmethod #line:49
    def _destruct_iterable_mapping_values (OO00000OOO0O00OOO ):#line:50
        for O00O00O00OOO0OOO0 ,O00O00O00O00OOOOO in enumerate (OO00000OOO0O00OOO ):#line:51
            if len (O00O00O00O00OOOOO )!=2 :#line:52
                raise ValueError ('dictionary update sequence element #{} has length {}; 2 is required.'.format (O00O00O00OOO0OOO0 ,len (O00O00O00O00OOOOO )))#line:53
            if not isinstance (O00O00O00O00OOOOO [0 ],str ):#line:54
                raise ValueError ('Element key %s invalid, only strings are allowed'%O00O00O00O00OOOOO [0 ])#line:55
            yield tuple (O00O00O00O00OOOOO )#line:56
