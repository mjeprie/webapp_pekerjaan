import functions
import streamlit as st

list_pekerjaan = functions.get_pekerjaan()
def tambah_pekerjaan():
    pekerjaan_baru = st.session_state['pekerjaan_baru']
    pekerjaan_baru = pekerjaan_baru.capitalize()
    list_pekerjaan.append(pekerjaan_baru + '\n')
    functions.tulis_pekerjaan(list_pekerjaan)

st.title("Daftar Pekerjaan")
st.subheader("Aplikasi pekerjaan")
st.write("Digunakan untuk mengatur daftar pekerjaan")

for index, pekerjaan in enumerate(list_pekerjaan, start=0):
    checkbox = st.checkbox(pekerjaan, key = pekerjaan)
    if checkbox:
        # print(index, 'dicek')
        # print(st.session_state[pekerjaan], 'dihapus')
        del st.session_state[pekerjaan]
        list_pekerjaan.pop(index)
        functions.tulis_pekerjaan(list_pekerjaan)
        st.experimental_rerun()


st.text_input(label="Tambahkan pekerjaan baru", label_visibility='hidden', placeholder="Tambah pekerjaan baru",
              on_change=tambah_pekerjaan, key='pekerjaan_baru')
st.button(label='Tambah', key='tambah', on_click=tambah_pekerjaan)
# st.button(label='Hapus', key='hapus')
#
# st.session_state
# print(st.session_state)