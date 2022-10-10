def sand(s, a, b=None): return f"{a}{s}{a if b is None else b}" 
def sq(s): return sand(s, "'")
def dq(s): return sand(s, "\"")
def paren(s): return sand(s, "(", ")")
def braces(s): return sand(s, "{", "}")
def bracket(s): return sand(s, "[", "]")
def comma(*ss): return ",".join(ss)
def and_(*ss): return " and ".join([paren(s) for s in ss])
def  or_(*ss): return  " or ".join([paren(s) for s in ss])

"""
s = "s"
a = "a" 
b = "b" 
ss = ["a=aa", "b=bb", "c=cc"]
print(f"sand(s, a, b) -> {sand(s, a, b)}")
print(f"sq(s) -> {sq(s)}")
print(f"dq(s) -> {dq(s)}")
print(f"paren(s) -> {paren(s)}")
print(f"braces(s) -> {braces(s)}")
print(f"bracket(s) -> {bracket(s)}")
print(f"comma(*ss) -> {comma(*ss)}")
print(f"and_(*ss) -> {and_(*ss)}")
print(f" or_(*ss) -> { or_(*ss)}")
"""