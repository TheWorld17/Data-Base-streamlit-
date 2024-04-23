import streamlit as st
import pandas as pd
import time

with st.spinner('Зачекайте...'):
    time.sleep(1.5)
st.success('Зроблено!')


def main():
    st.title("Таблиця спортсменів")

    # Check if data for the table exists
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame({
            'Ім\'я': ['Вася', 'Петро', 'Марія'],
            'Вік': [25, 30, 28],
            'Спорт': ['Футбол', 'Волейбол', 'Теніс']
        })

    st.dataframe(st.session_state.data, width=800)



    # Add an athlete
    st.subheader("Додати спортсмена")
    new_name = st.text_input("Ім\'я:")
    new_age = st.number_input("Вік:", min_value=0, max_value=150, value=0)
    new_sport = st.text_input("Спорт:")

    if st.button("Додати"):
        new_athlete = pd.DataFrame({
            'Ім\'я': [new_name],
            'Вік': [new_age],
            'Спорт': [new_sport]
        })
        st.session_state.data = pd.concat([st.session_state.data, new_athlete], ignore_index=True)

        # Save the table
        st.session_state.data.to_csv("athletes_data.csv", index=False)

    # Delete an athlete
    st.subheader("Видалити спортсмена зі списку")
    delete_index = st.number_input("Напиши індекс спортсмена:", min_value=0, max_value=len(st.session_state.data)-1, value=0, step=1)

    if st.button("Видалити"):
        st.session_state.data = st.session_state.data.drop(delete_index).reset_index(drop=True)

        # Save the table


if __name__ == "__main__":
    main()
