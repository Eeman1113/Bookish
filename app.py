#@title Add info on your book
import streamlit as st

st.markdown("<h1 style='text-align: center;'>Bookish_</h1>", unsafe_allow_html=True)
st.markdown("___")
with st.expander("Who Am I?"):
    st.write("""*📖🤔 Are you tired of staring at a blank page, trying to come up with the perfect book chapter?*

`Do you wish you had a magical genie who could grant your every writing wish?`

Well, wish no more because **Bookish_** is here to make all your writing dreams come true! 🧞‍♂️✨

**Bookish_** is like having your own personal writing wizard, who can whip up a 2000-word book chapter in the blink of an eye. 🧙‍♀️💫

Simply give **Bookish_** your book title, description, genre, lead characters, and plot, and voila! You'll have a shiny new chapter ready to go. 📝🎉

Gone are the days of writer's block and endless hours of staring at a blank page. With **Bookish_**, you'll never run out of ideas again. Whether you're a bestselling author or a first-time writer, **Bookish_** has got your back. 💪💡

So why waste time struggling to write when you can let **Bookish_** do the heavy lifting for you? Try **Bookish_** today and unleash your inner writing genius! 🚀📚""")
Title_of_the_book = st.text_input("Title of the book")
What_is_the_book_about = st.text_input("What is the book about? (optional)")
What_is_the_chapter_about = st.text_input("What is the chapter about? (optional)")
Genre = st.text_input("Genre")
Lead_Characters = st.text_input("Lead Characters (optional)")
Plot_of_the_book = st.text_input("Plot of the book (optional)")
How_many_chapters=st.slider("How many chapters do you want to generate?", 1,10,1)

write = st.button("Generate Chapter")


a=0
if write == True:
    while a<=0:
        import openai
        openai.api_key = st.secrets['open_api']
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="generate a 2000-word book chapter of the "+Genre+" genre based on the following book description: \nTitle of the book: "+Title_of_the_book+"\nWhat is the book about: "+What_is_the_book_about+"\nWhat is the chapter about: "+What_is_the_chapter_about+"\nLead Characters: "+Lead_Characters+"\nPlot of the book: "+Plot_of_the_book,
            temperature=0.7,
            max_tokens=1000,     
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )#model
        b=response
        print("\n")
        print(response.choices[0].text)#output
        sus=response.choices[0].text
        j=open("book.txt",'a')
        j.write(response.choices[0].text)
        j.close()
        a=a+1

        st.markdown("___")
        st.write(response.choices[0].text)
        st.markdown("___")
        st.balloons()

        import pandas as pd
        df = pd.DataFrame()
        df['Title_of_the_book']=Title_of_the_book
        df['Description'] = [What_is_the_book_about]
        df['Genre'] = [Genre]
        df['Lead_Characters'] = [Lead_Characters]
        df['Plot_of_the_book'] = [Plot_of_the_book]
        df['Chapter'] = [sus]
        df.to_csv('book.csv', index=False)
        st.dataframe(df)
