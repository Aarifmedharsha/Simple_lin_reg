import numpy as np
import pickle
import pandas as pd
import streamlit as st


model = pickle.load(open(r'C:\Users\Aarif\OneDrive\Desktop\projects\model1.pkl', 'rb'))

def welcome():
    return "Welcome All"

def salary(experience):
     
    prediction = model.predict(experience)

    print(prediction)
    return prediction

def main():
    html_temp = """
    <h2 style="color:rgb(241, 153, 20);text-align:center;
	position: absolute;
	top: 40%;
	left: 50%;
	margin: -150px 0 0 -150px;
	width:400px;
	height:400px;">WebApp for Salary Prediction</h2>
    </div>
    """
    a,b,c,d,e= st.columns(5)
    st.markdown(html_temp,unsafe_allow_html=True)
    col6, col7, col8 , col9, col0 = st.columns(5)
    with col6:
        pass
    with col7:
        pass
    with col9:
        pass
    with col0:
        pass
    with col8 :
        EXPERINCE= c.text_input('Enter Experience:',2)
        EXPERINCE=float(EXPERINCE)


    result=0
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        if st.button("Predict"):
            d=(np.array(EXPERINCE))
            f=d.reshape(1,-1)
            result=salary(f)
            st.text('The predicted salary is ${:.2f}'.format(float(result)))
    
        if st.button("About"):
            st.text("This is a diabetes classification model made using StreamLit")
            st.text("This model is built by Aadrif")


if __name__=='__main__' :
    main()