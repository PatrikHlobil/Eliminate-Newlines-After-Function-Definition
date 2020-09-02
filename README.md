# Eliminate Newlines CLI

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

    eliminate_newlines testfile.py

**Reformat folder (recursively):**

    eliminate_newlines /path/to/testfolder

**Check mode:**

    eliminate_newlines testfile.py --check

**Return Codes**

Return code 0 means nothing would change.

Return code 1 means some files would be reformatted. 

Return code 123 means there was an internal error.


## CLI Documentation:

    eliminate_newlines --help


```
Usage: eliminate_newlines [OPTIONS] PATH

  This CLI formats Python code in such a way that after the function
  definition header all newlines will be deleted.

  Return code 0 means nothing would change.  Return code 1 means some files
  would be reformatted. Return code 123 means there was an internal error.""
  pass.

  Passed PATHS can be either filea or directories. In the latter case, all
  files in the folders will be formatted recursively.

Options:
  --check  Don't write the files back, just return the status.
  --help   Show this message and exit.
```
