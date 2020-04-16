from sympy.parsing.mathematica import mathematica
from clipboard import copy,paste

additional_translations={
'Pochhammer[x,y]': 'rf(x,y)',
    'ArcTan[x,y]': 'atan2(y,x)'}
copy(str(mathematica(paste(), additional_translations=additional_translations)))
atan2(y, x)
"""
Sin[x]
ArcTan[x,y]
"""
