target = __import__("Hello")
s=target.sum(5,6)
assert s==11,"should be 11"
