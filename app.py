import streamlit as st

# ИНИЦИАЛИЗИРАНЕ НА ПАМЕТТА ЗА КНИГИТЕ
if "books" not in st.session_state.books:
    st.session_state.books = []   # Можеш да заредиш примерни книги тук


st.header("Търсене по заглавие")
search_title = st.text_input("Въведи заглавие")

if st.button("Търси по заглавие"):
    found = False

    for book in st.session_state.books:
        if search_title.lower() in book["title"].lower():
            st.write(book)
            found = True

    if not found:
        st.write("Няма намерени книги с това заглавие.")


st.header("Търсене по автор")
search_author = st.text_input("Въведи име на автор")

if st.button("Търси по автор"):
    found = False

    for book in st.session_state.books:
        if search_author.lower() in book["author"].lower():
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", book["price"])
            st.write("----------------------")
            found = True

    if not found:
        st.write("Няма намерени книги от този автор.")
