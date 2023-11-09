# [Dachshund Attack](https://play.picoctf.org/practice/challenge/159?page=4)

[Complete theory: Weiner Attack on Small e](https://en.wikipedia.org/wiki/Wiener%27s_attack)

## Theory
Basic approach is use Weiner Attack on small e which postulates that small d can be aproximated by continoud fractions $\frac{e}{pq}$

## Continued Fractions
Continued fractions give an alternative way of representing a fraction using approximations. For rational numbers a continous fraction is finite.

### Convergence of Continued Fractions
Irrational numbers will not have a finite sequence of numbers that represent the entire fraction
However we can take the first n sequence/segments and observer the convergence 
In general the larger the number in the convergence the closer it is to approximating the final irrational number

Each convergent can be represented by a recursive relation see [a terms, h terms and k terms](https://en.wikipedia.org/wiki/Continued_fraction#Convergents)

### Steps
1. Find the simplified continued fraction of F in terms of [a1, a2, a3, a4, .., an] [Use Section Calculating continued fraction representations](https://en.wikipedia.org/wiki/Continued_fraction#Convergents)
2. Produce the corresponding convergents of k/d using  [Use Section Infinite continued fractions and convergents](https://en.wikipedia.org/wiki/Continued_fraction#Convergents)
3. Tabulate the h_n k_n and a_n
4. For each covergent solve the polynomial eqution to get a factorization of N
5. The factorization is p and q next find d which is modulo inverse of e mod pq
6. M = c ** d mod N then decrypt

## Tips
- Use gmpy to find roots `root, isTrueRoot = gmpy2.iroot(d, 2)`
- Use 
`d = pow(e, -1, (p-1)*(q-1))` to find modulo inverse in python 3.8+; Or extended euclidean algorithm
- Use `bytearray.fromhex(format(M, 'x')).decode()` to decode the message
- To exponential large values use the three argument pow (including N) `M = pow(C, d, N)`

### Flag
picoCTF{proving_wiener_3899149}


# [Full Code Here](dachshund_attack.py)

```python
if __name__ == "__main__":

    a_terms = determine_aterms(N, e, 1000)
    # print(a_terms)
    h_terms = calculate_h_terms(a_terms)
    # print(h_terms)
    k_terms = calculate_k_terms(a_terms)
    # print(k_terms)
    factorization = find_factorization(h_terms, k_terms, N, e)

    p = abs(factorization[0])
    q = abs(factorization[1])

    d = pow(e, -1, (p-1)*(q-1))

    # print((d * e) % ((p-1)*(q-1)))

    M = pow(C, d, N)
    print("Message: {}".format(bytearray.fromhex(format(M, 'x')).decode()))


```