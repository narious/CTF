[MiniRSA](https://play.picoctf.org/practice/challenge/188?page=4)

The premise of this problem is RSA but with a small exponent e. We are also given the information that the cipher text is "barely" larger than N.

This may mislead us to know how much is barely, one stumbling point is to assume that barely means 1. But that is not that case.

The main point is that we find a i such than EncMessage = i * N + C and the cube root of EncMessage is a perfect root. 

Before that we must develop an algorithm to find cube roots


```python
def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = x
    low = 1
    while low < high:
        mid = (low + high) // 2 # This means we take the lower bound
        if (mid ** 3) > x:
            high = mid
        elif (mid ** 3) < x:
            low = mid + 1# Thus this should be plus one
        else:
            return mid
    return -1
```
This is a simple binary search algorithm to find the lower bounds. However it is really slow. (takes 5 minutes)

Preferably we can use
```python
import gmpy2
m, isTrueRoot = gmpy2.iroot(i*N + C, e)
```
to find find the cube root in 1 second

Thus the algorithm look like this


```python
for i in range(0, 10000):
    m, isTrueRoot = gmpy2.iroot(i*N + C, e)
    if is_true_root:
        print(f"Found i = {i}")
        print("Message: {}".format(bytearray.fromhex(format(m, 'x')).decode()))
        break
```

The flag is succesfully found as `picoCTF{e_sh0u1d_b3_lArg3r_85d643d5}`
