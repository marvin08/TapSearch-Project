from flask import Flask, render_template, request
from TapSearchAPI import TapSearch
app = Flask(__name__)


@app.route("/")

def home():
    return render_template('home.html')


@app.route("/search",methods=['POST'] )
def search():
    lists = ["ss ", "bwebfweobwef ", "beowbeobbwebwegbgbwe "]

    text = request.form['document']
    word = request.form['a_word']
    word=word.lower()
    # print(text)
    api = TapSearch(text)
    # print(api.index())
    
    # print(api.search(word))
    lists = api.search(word)
    paragraph_dict = api.index()


    return render_template('search.html', lists = lists, length = len(lists), 
            paragraph_dict = paragraph_dict, search_word = word)
    # return ( request.form['document'])




if __name__ == "__main__":
    app.run(debug=True)
