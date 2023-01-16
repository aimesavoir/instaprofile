
import instaloader
import streamlit as st
import glob


def telecharger(dp):
    ig = instaloader.Instaloader()
    resulta=st.text('جاري البحث...')
    
   
    try:
        ig.download_profile(dp ,profile_pic_only=True)
        resulta.text('    ')
    except instaloader.ProfileNotExistsException:
        st.warning('إسم مستخدم أنستغرام غير موجود')
        #resulta.text('إسم مستخدم أنستغرام غير موجود')

#prof= st.text_input('taper le compte instagram')
#telecharger(prof)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


form=st.form('profile')

prof=form.text_input('أدخل إسم بروفايل المستخدم')
ok=form.form_submit_button('بحث')
if ok==True:
    telecharger(prof)
    #st.image(pic)


for filename in glob.glob(prof+'/*.jpg'): #assuming gif
    form.image(filename,width=600)
    #st.image(filename,ImageFormatOrAuto='auto')
    





