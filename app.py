import streamlit as st
from streamlit.components.v1 import html

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://lh3.googleusercontent.com/pw/ADCreHfLtvcLHcKU6ShV53bO7dAWxRG-tonlYCRKzKQJu_TAA7rXnq2riuKDc876AdrybmiXBiT6b-k2D2-CFHxDBotb_dvyUeYCylpkrRTH7I3YIt2QcZTmUnkqp6g7GlYU6I9E1j2f9z827eN9SBA_N7X7w63Ps_ET_XpMwYPu2ZJ4WwHXaJgkFX1FNj52W0qUPfujSc09NN-hbnrZ8L61OB5uQ_e41SJwq1K616ODG6_ZsxyOLTOEMrULEU0ywlHTljyXNtKRT7jd8K04SPSgC2KUJA7nFZrTavk_TvvXyAhHexXnpWK_zIBK1OTxdR1kLG4bcUwQXBrO6HhTe2VWnCgIZTXK864oH_dw_OLYnE7wjUd_ASZitkPYqtrJygAcUaTvqJUbu5EQysBvggRMMPS7XLA72_RNTBuBgtZIhDuSM1hq3Awiw4b7N_IDc-u0PHPSYSYGmYnn6MEnj2Y1MBGbvZOHoRg88cEn-LN0U779fBPoJKdoDrjLk3ADSyKrYWesxXeWgAw_owWcfZcdlEwSJkZfRE_dX_hMg84LXZV7cS8I0MVQvahQT56hdkGNRBjDp01EqlkorxRyNN43dK6o4IS2DY1SQetl0xKZ-jY6l6CBSLZtt9xr0OEdYZE3vbjh9iKEQNZArVCCvP8LqfeWOd0awQ-vW3sKxoWDVGRq621-z5_AoKdK-DcdtcnIc4LQYFC6-O4ZH8kQ9HLYqA8XLdjAdFhr7jQB_2LabarRgCkq9uUY9rFdWVz6h25RiDd5vfe1WV_c_SHVp7ztLB5wc_K-jgPQsbXmWChfRUMXbJlL9g7OCUVN0iQ7KmN3kTKPipIA2oUR9NBpMX-fN_Z4LI8ITXXAnx7GOAPJn7D3R093qIikFok9CEWr1Xc8Dzc6dhFNdg1SSTPadS2OGCnjlX-XZujS-WVtbn9pHibE27WefFd_dgncR4JvNAc=w976-h549-s-no-gm?authuser=0");
             background-attachment: fixed;
             background-size: contain;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Chamada da função para alterar o plano de fundo
set_bg_hack_url()

# Criar duas colunas
col1, col2 = st.columns([4, 1])  # Ajuste as proporções conforme necessário

# Coluna para o iframe do chat
with col1:
    iframe_html = """
    <iframe src="https://web.powerva.microsoft.com/environments/Default-cdf2577b-a9c0-4934-9165-b00e7dafdff6/bots/cr1df_legalLabs/webchat?__version__=2" width="100%" height=650'></iframe>
    """
    html(iframe_html, width=400, height=700, scrolling=False)

# Coluna para a logo
# with col2:
#     for i in range(30):
#         st.text('\n\n\n\n\n\n\n\n\n\n\n\n')
#     st.markdown('### Legal Labs')
#     logo = "logo_carrefour_clear.png"
#     st.image(logo, width=130)
