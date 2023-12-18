import gmpy2
import math
import numpy
e = 70779241429695560933989782825494118718815991555445954499968064337229510297421368443923605854011348942382549267743238971417118767685860046970566854265937181293192475315907173450111269881621214189433274237197702747531354982360851554865022532791973755114619767772175688495190822421017596099911018030490872985501
N = 104813489135708550207017153723895303316067074109753922213705838812458307027901267855819700803461897844892766271738872355783726215491643445452604371596062170654145653799329732214269870850181003309777961501343799089491738322373432358490678023274981456171268662570516741387338289696273288230495871962811646799877
C = 94400339392688171028204769837171704175101828801186751187946567158245741165959211151857884423450372958864416730321979584159903155197069189702395287975902014564549547729356006315033720025268484112410427279882727348364693308058718038390719731531894525853545662580635148117196994373061628100277038073009998996870

test_N = 90581
test_e = 17993


# Calculate terms a1, a2, a3, ..., an up until n_terms
def determine_aterms(N, e, n_terms):
    a_terms = []
    numer = e
    denom = N
    for i in range(n_terms):
        a_terms.append(numer // denom)
        if (numer % denom) == 0:
            break
        temp = numer
        numer = denom
        denom = temp % denom
    return a_terms

def calculate_h_terms(a_terms):
    h_terms = [0, 1] # Base terms
    for i in range(2, len(a_terms) + 2):
        h_terms.append(a_terms[i-2]*h_terms[i-1] + h_terms[i-2])
    return h_terms[2:]


def calculate_k_terms(a_terms):
    k_terms = [1, 0] # base terms
    for i in range(2, len(a_terms) + 2):
        k_terms.append(a_terms[i-2]*k_terms[i-1] + k_terms[i-2])
    return k_terms[2:]

def find_factorization(h_terms, k_terms, N, e):
    # coeffients of quadratic formulae
    a = 1
    b = 0
    c = N
    d = 0

    for i in range(len(h_terms)):
        if (h_terms[i] == 0):
            continue
        phi_N = (e * k_terms[i] - 1) // h_terms[i]
        b = -(N - phi_N + 1)
        d = (b**2) - (4*a*c)

        if (d < 0):
            d *= -1

        root, isTrueRoot = gmpy2.iroot(d, 2)
        if (isTrueRoot):
            # Doesn't work when using floats (!) May be issue with number representation
            sol1 = (-b-root) // (2 * a)
            sol2 = (-b+root) // (2 * a)
            if (sol1 * sol2) == N:
                return (-sol1, -sol2)
    return None



# From https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

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

    







