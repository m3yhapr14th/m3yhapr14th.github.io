from flask import Flask, render_template
import rf

app = Flask(__name__)

@app.route("/")
def page_gets():
    page = rf.page_get.find_all("a")
    pval = []
    
    for pages in page[0:-2]:
        pval.append(pages.string)

    return render_template("index.html", pageGetHtml = pval)

def title_gets():
    title = rf.table_get.find_all("a")
    tval = []

    for titles in title:
        tval.append(titles.string)

    return render_template("index.html", titleGetHtml = tval)

