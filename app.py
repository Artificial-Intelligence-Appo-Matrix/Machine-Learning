import streamlit as st


st.set_page_config(page_title='Title Here', page_icon=':shark:', layout='wide')    # Set page title, icon and layout
st.title('This is Title Text in WebPage')    # Title of the page




# st.header("_Streamlit_ is :blue[cool] :sunglasses:")
# st.header("This is a header with a divider", divider="gray")
# st.header("These headers have rotating dividers", divider=True)
# st.header("One", divider=True)
# st.header("Two", divider=True)
# st.header("Three", divider=True)
# st.header("Four", divider=True)
# st.header("Foui", divider=True)



# # Header
# st.header("This is a header", help='Helper here', anchor='anchor_id1') 

# # Subheader
# st.subheader("This is a subheader",anchor='a2', help='Help for Sub Heading')


# # Text
# st.text(help='https://www.google.com',body="Hello World Text!!!")



# # Markdown
# st.markdown("- This is a markdown <h1>Hello Html</h1>", help='Markdown Help', unsafe_allow_html=True)


# # Warnings and Errors
a= 30
b= 15
if a<b:
    st.success("a is less than b", icon='👍'
               )
else:
    st.error("a is greater than b", icon='👎')
# success
st.success("Success")

# success
st.info("Information", icon='🔔')

# success
st.warning("Warning", icon='⚠️')

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)




# Write text
st.write("Text with write<p>ASsfsg</p>", unsafe_allow_html=True)

# Writing python inbuilt function range()
st.write( "if" ,range(5),":")




# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=100, caption="This is Caption", channels='BGR',output_format='PNG',clamp=False) 




# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
st.checkbox( key="key1",disabled= False , label= "Try Label", label_visibility= 'visible'
             )


if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")
else:
    st.text("Hiding")





# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.error("Female")
                



# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)





# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')
for hobby in hobbies:
    st.write(hobby)



# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To Lecure of Streamlit!!!")




# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    name = "Hii, "+name
    result = name.title()
    st.success(result)




# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 100)

# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))




