def adding(a, b):
    if type(a) == int:
        return a + b
    else:
        i = 0
        carry = 0
        while i < max(len(a), len(b)) or carry:
            if i >= len(a):
               a.append(0)
            summand = 0
            if i < len(b):
                summand = int(b[i])
            current = int(a[i]) + summand + carry
            carry = current // 10
            a[i] = str(current % 10)
            i += 1
        a.reverse()
        return str(''.join(a))