import streamlit as st

def main():
    # Configuração da barra de navegação
    st.markdown("""
    <style>
    .stApp header {
            z-index: 1;
            background: transparent;
    }
            </style>
            """,
            unsafe_allow_html=True
            )

    st.markdown(
        """
        <style>
        .navbar {
            background-color: #333;
            overflow: hidden;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 100;
        }

        .navbar img {
            margin-left: 20px;
            margin-right: 20px;
            height: 50px;
            width: auto;
            float: left;
        }

        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        </style>
        """
    , unsafe_allow_html=True)

    # Obtém os parâmetros da URL
    params = st.query_params
    params_dict = params.to_dict()
    page = params_dict["page"] if "page" in params_dict else "pagina1"

    # Barra de navegação
    st.markdown(
        """
        <div class="navbar">
            <img src="https://via.placeholder.com/100" alt="Logo">
            <a href="?page=pagina1">Página 1</a>
            <a href="?page=pagina2">Página 2</a>
            <a href="?page=pagina3">Página 3</a>
            <!-- Adicione mais páginas conforme necessário -->
        </div>
        """
    , unsafe_allow_html=True)

    # Conteúdo da página
    if page == "pagina1":
        st.title("Página 1")
        st.write("Este é o conteúdo da Página 1.")
    elif page == "pagina2":
        st.title("Página 2")
        st.write("Este é o conteúdo da Página 2.")
    elif page == "pagina3":
        st.title("Página 3")
        st.write("Este é o conteúdo da Página 3.")

if __name__ == "__main__":
    main()
