# username = "chaiaurcode"

# def fun():
#     username = "chai"  # Corrected the typo
#     print(username)

# print(username)
# fun()

x=99
def func(y):
    z=x+y
    return z
result=func(1)
# print(result)
# Let's go through the code step-by-step:

# ```python
# x = 99

# def func(y):
#     z = x + y  # x is a global variable here
#     return z

# result = func(1)
# print(result)
# ```

# ### Explanation:
# - `x = 99`: This is a global variable.
# - `func(y)` is defined. Inside the function, it uses the global variable `x` and adds it to the local parameter `y`.
# - `func(1)` is called, so:
#   - `x + y = 99 + 1 = 100`
# - `result = 100`
# - `print(result)` will output:

# ```
# 100
# ```

# ### ✅ Final Answer: `100`

def fun3():
    global x # Declare x as global to modify the global variable
    x=88
fun3()
print(x)

def f1():
    x=12
    def f2():
        print(x)
    return f2
result=f1()
result()

def chaicode(num):
    def actual(x):
        return x**num
    return actual

f=chaicode(2)
g=chaicode(3)
print(f(3))
print(g(3))