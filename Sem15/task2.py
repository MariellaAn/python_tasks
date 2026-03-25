def solve(st: str) -> str:
    st = st.strip()
    if len(st) % 2 == 0:
        st = st.upper()
    else:
        st = st.lower()
    return st

print(solve(input()))