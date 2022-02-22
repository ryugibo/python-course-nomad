# from indeed import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
# from save import save_to_file

# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)

def plus(*args):
  result = 0
  for number in args:
    result += number
  return result

def key_plus(**kargs):
  result = 0
  for key in kargs:
    print(key, kargs[key])
    result += kargs[key]
  return result

print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(key_plus(a = 15, b = 55))
