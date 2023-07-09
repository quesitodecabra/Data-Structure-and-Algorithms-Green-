n,m,a = map(int, input().split())
# flagstones needed to cover the length
n_flagstones = n // a
# flagstones needed to cover the width
m_flagstones = m // a

# Note: In step 4, we consider the possibility of having some leftover area that requires an additional flagstone. That's why we increment n_flagstones or m_flagstones by 1 if the remainder of the division (n % a or m % a) is non-zero.
if n % a != 0:
    n_flagstones += 1
if m % a != 0:
    m_flagstones += 1


total_flagstones = n_flagstones * m_flagstones
print(total_flagstones)