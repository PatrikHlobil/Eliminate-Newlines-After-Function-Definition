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

## Example usage:

**Reformat file:**

    eliminate_whitespaces testfile.py

**Reformat folder (recursively):**

    eliminate_whitespaces /path/to/testfolder

**Check mode:**

    eliminate_whitespaces testfile.py --check

**Return Codes**

Return code 0 means nothing would change.

Return code 1 means some files would be reformatted. 

Return code 123 means there was an internal error.


## CLI Documentation:

    eliminate_whitespaces --help


```
Usage: eliminate_whitespaces [OPTIONS] PATH

  This CLI formats Python code in such a way that after the function
  definition  header all newlines will be deleted.

  Return code 0 means nothing would change.  Return code 1 means some files
  would be reformatted. Return code 123 means there was an internal error.""
  pass.

  Passed PATH can be either a file or a directory. In the latter case, all
  files in the folder will be formatted recursively.

Options:
  --check  Don't write the files back, just return the status.
  --help   Show this message and exit.
```
