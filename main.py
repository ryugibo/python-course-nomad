def is_number(a):
  if type(a) is int:
    return True
  elif type(a) is str and a.isdigit():
    return True
  else:
    return False

def plus(a, b):
  if is_number(a) and is_number(b):
    return int(a) + int(b)
  else:
    return None
  
def minus(a, b):
  if is_number(a) and is_number(b):
    return int(a) - int(b)
  else:
    return None
  
def times(a, b):
  if is_number(a) and is_number(b):
    return int(a) * int(b)
  else:
    return None
  
def division(a, b):
  if is_number(a) and is_number(b):
    return int(a) / int(b)
  else:
    return None
  
def negation(a):
  if is_number(a):
    return -int(a)
  else:
    return None
  
def power(a, b):
  if is_number(a) and is_number(b):
    return int(a) ** int(b)
  else:
    return None
  
def remainder(a, b):
  if is_number(a) and is_number(b):
    return int(a) % int(b)
  else:
    return None

print(f" 3  +  7 : {plus(3, 7)}")
print(f"\"3\" +  7 : {plus('3', 7)}")
print(f" 3  + \"7\": {plus(3, '7')}")

print(f" 3  -  7 : {minus(3, 7)}")
print(f"\"3\" -  7 : {minus('3', 7)}")
print(f" 3  - \"7\": {minus(3, '7')}")

print(f" 3  *  7 : {times(3, 7)}")
print(f"\"3\" *  7 : {times('3', 7)}")
print(f" 3  * \"7\": {times(3, '7')}")

print(f" 3  /  7 : {division(3, 7)}")
print(f"\"3\" /  7 : {division('3', 7)}")
print(f" 3  / \"7\": {division(3, '7')}")


print(f"  -3 : {negation(3)}")
print(f" -\"3\": {negation('3')}")

print(f" 3  **  7 : {power(3, 7)}")
print(f"\"3\" **  7 : {power('3', 7)}")
print(f" 3  ** \"7\": {power(3, '7')}")

print(f" 3  %  7 : {remainder(3, 7)}")
print(f"\"3\" %  7 : {remainder('3', 7)}")
print(f" 3  % \"7\": {remainder(3, '7')}")
