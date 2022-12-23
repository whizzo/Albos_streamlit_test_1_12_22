import streamlit as st


string1 = st.text_input("Enter your string here", key = "string1")
list1 = []
list2 = []
list3 = []
numri = 0
numri2 = len(list1)
def convert_list():
    words = string1.split(" ")
    for word in words:
        list1.append(word)
     
       
    

return_list = st.button("Return List", on_click=convert_list())
if return_list:
    st.write(list1)
     

def convert_lower():
    for x in list1:
        list2.append(x.lower())
    
      

lower_button = st.button("lower", on_click=convert_lower())
if lower_button:
    st.write(list2)


def count():
    count.numri = 0
    for item in list1:
        count.numri = count.numri + 1

    

print_count = st.button("Print Count", on_click=count())
if print_count:
    st.write(count.numri)





