import streamlit as st

from stringsrc import ENTERNITY, ASSHOLES


def check_str(inp: str):
    rawstr = inp
    if len(inp) < 6:
        retstr = rawstr + (6 - len(rawstr)) * 'X'
    else: 
        retstr = inp[0:6]
    return retstr

def letter2num(letter: str, distance: int):
    if ord(letter) + distance > 0:
        return ord(letter) + distance
    else:
        return 0

def return_cords(inp: str, targetword = 'Kaufha'):
    coords = [74, 59, 31, 7, 50, 20]
    exacts = [l for l in targetword]
    distances = [coords[i] - ord(e) for i, e in enumerate(exacts)]
    word = check_str(inp)
    nums = [letter2num(s, distances[i]) for i, s in enumerate(word)]
    return nums

def session_counter() -> int:
    return st.session_state['counter']

def update_counter():
    st.session_state['counter'] = 0
    if st.session_state['answers'][0] == 'kaufhaus':
        st.session_state['counter'] += 1
    if st.session_state['answers'][1] == 'zinnen':
        st.session_state['counter'] += 1

if __name__ == '__main__':
    st.session_state['counter'] = 0
    st.session_state['answers'] = ['', '', '']
    # this is extra dangerous
    
    st.write("""# THIS IS ROUTE 2""")
    
    st.write(ASSHOLES)
    
    st.write('Turn around and input what there is (or was?)')
    
    kaufh_res = st.text_input('Anagram', label_visibility='hidden')
    st.session_state['answers'][0] = kaufh_res.lower()
    coords = return_cords(kaufh_res, 'Kaufha')
    coordstring = ''
    for c in coords:
        coordstring += f'{c:02d}'
    st.write(f'Look to my standing by daylight at {coordstring}. Look to the west!')
    update_counter()
    
    print('Strange: ', session_counter()) 
    if session_counter() >= 1:
    
        st.write('See me standing here all in red [GER]:')
        bridge_res = st.text_input('bridge', label_visibility='hidden')
        st.session_state['answers'][1] = bridge_res.lower()
        update_counter()
    
    print(st.session_state['answers'])
    
    if session_counter() >= 2:
        update_counter()
    
        st.write(ENTERNITY)

