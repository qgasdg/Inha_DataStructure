with open('Inha_DataStructure\problem_set_implementation\infix.txt', 'r') as file:
    exp = file.read().strip()
    st = []
    for e in exp:
        if e.isdigit():
            print(e, end='')
        elif e == '(':
            st.append(e)
        elif e == '*' or e == '/':
            st.append(e)
        elif e == '+' or e == '-':
            while len(st) != 0:
                if st[-1] == '(':
                    break
                else:
                    print(st.pop(), end='')
            st.append(e)
        elif e == ')':
            while len(st) != 0:
                if st[-1] == '(':
                    st.pop()
                    break
                else:
                    print(st.pop(), end='')
        # print(*st)
    while len(st) != 0:
        print(st.pop(), end='')
