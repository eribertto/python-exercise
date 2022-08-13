# IPython log file

get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('run', 'func_def_args.py')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('reset', '-f')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('ll', '')
git status
get_ipython().run_line_magic('edit', 'func_def_args.py')
get_ipython().run_line_magic('run', 'func_def_args.py')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('reset', '')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('whos', '')
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
type(fruits)
# example of list manipulation
fruits.count('apple') # how many apples
fruits.count('pineapple') # is it in the list?
for fr in fruits:
    print(f'the fruit is {fr}')
    
fruits.count('banana')
fruits.reverse()
fruits
fruits.append('grapes')
fruits
fruits.sort()
fruits
get_ipython().run_line_magic('whos', '')
fruits.pop()
fruits
numbers = []
get_ipython().run_line_magic('whos', '')
for num in range(10):
    numbers.append(num)
    
numbers
get_ipython().run_line_magic('whos', '')
squares = []
for x in range(10):
    squares.append(x**2)
    
squares
get_ipython().run_line_magic('whos', '')
numbers == squares
squares
numbers
# combine list
combs = []
get_ipython().run_line_magic('whos', '')
for x in numbers:
    for y in squares:
        if x != y:
            combs.append((x, y))
            
combs
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('who', '')
get_ipython().run_line_magic('whos', '')
vec = [-4, -2, 0, 2, 4]
vec
[x*2 for x in vec]
new-vec = [x*2 for x in vec]
new_vec = [x*2 for x in vec]
get_ipython().run_line_magic('whos', '')
new_vec
vec == new_vec
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
[abs(x) for x in vec]
[abs(x) for x in new_vec]
dir(abs)
get_ipython().run_line_magic('whos', '')
fruits
get_ipython().run_line_magic('whos', '')
len(combs)
len(fruits)
len(new_vec)
fruits
del fruits[::-1]
fruits
get_ipython().run_line_magic('whos', '')
numbers
del numbers[2::]
numbers
# note del is a statement not a function
get_ipython().run_line_magic('whos', '')
del combs
get_ipython().run_line_magic('whos', '')
empty = ()
type(empty)
singleton = 'hello', # note the trailing comman denoting a tuple
type(singleton)
len(empty)
len(singleton)
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('history', '')
empty
singleton
# next is looping techniques in dictionaries
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
get_ipython().run_line_magic('whos', '')
type(questions)
type(answers)
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
    
dir(zip)
help(zip)
get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('ll', '')
file ipython_log.py
get_ipython().run_line_magic('edit', 'ipython_log.py')
exit()
