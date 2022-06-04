#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


from flask import Flask


# In[3]:


from flask import render_template, request

#extract the template 


# In[4]:


app = Flask(__name__)

#double underscore __ 


# #### Running the frontend script in Cloud

# The following codes extract the template (index.html) and check if app works.

# @app.route("/", methods = ["GET", "POST"])
# def index():
#     if request.method == "POST":
#         return(render_template("index.html", result="temp"))
#     else:
#         return(render_template("index.html", result="waiting..."))

# This step check if the file is created by you. If yes, the app will proceed to run. 

# if __name__ == "__main__":
#     app.run()

# This step extract the text, print out and find the sentiment.

# In[5]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text= request.form.get("text")
        print(text)
        r=TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting...."))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




