# Eliminate Whitespaces CLI

This CLI formats Python code in such a way that after the function definition header all newlines will be deleted. 

**Example**

```python
def foo(a):
    
   return a + 1
   

class A:
    def bar(self,
    b,
    c):
       

        return b + c
```

will be formatted to:

```python
def foo(a):
   return a + 1
   

class A:
    def bar(self,
    b,
    c):
        return a + b + c
```
