import re

def solution(new_id):
    st = new_id
    # 1단계
    st = st.lower()
    # 2단계
    st = re.sub('[^a-z\d\-_.]', '', st)
    # 3단계
    st = re.sub('\.+', '.', st)
    # 4단계
    st = re.sub('^\.|\.$', '', st)
    # 5단계
    st = 'a' if st == '' else st[:15]
    # 6단계
    st = re.sub('\.$', '', st)
    # 7단계
    while len(st) < 3:
        st += st[-1:]
    return st