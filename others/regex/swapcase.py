import re

pattern = '.*'
string = 'HeLlo thEre'
repl = lambda x : x.swapcase()

re.sub (pattern, repl, string)