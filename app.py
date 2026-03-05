
from flask import Flask ,render_template

app = Flask(__name__)
products = [
        {
         "name":"Samsung S-26 Ultra",
         "image":"samsungs26.webp",
         "description":"12gb ram ,256 gb rom |newly privacy feauture added |4+years os updates and security paches ",
         "price":"120000",
         "categories":"elect"
         },
        {
            "name":"Oneplus bullet neck band",
            "image":"ONEplus neck band.jpg",
            "description":"12mm drivers|120hrs play back|ANC support ",
            "price":"5000",
            "categories":"elect"
            },
        {
            "name":"realme buds 5",
         "image":"realme buds5.webp",
         "description":"12mm drivers|120hrs play back|ANC support ",
         "price":"5000",
         "categories":"elect"
         },

        {
         "name":"Oneplus powerbank 12000mah",
         "image":"OnePlus-150W-SuperVOOC.webp",
         "description":"fast charge support|2 device connectivity|military grade built quality ",
         "price":"4000",
         "categories":"elect"
         },
        {
         "name":"addidas boot",
         "image":"boot.jpg",
         "description":"easy to run|2 years warrenty |military grade built quality ",
         "price":"15000",
         "categories":"mens_fashion"
        },
        {
            "name":"Vitamin C Scerum",
         "image":"vitaminC.webp",
         "description":"skin moisture|skin brightner |rich in vitamin c ",
         "price":"400",
         "categories":"beauty"
         },
        {
            "name":"wall clock",
            "image":"wall clock.webp",
            "description":"asthetic hoome|wall deceration + time   |home decors ",
            "price":"650",
            "categories":"decors"
            },
            {
            "name":"wall poster",
            "image":"wallposter.webp",
            "description":"asthetic hoome|wall deceration  |home decors ",
            "price":"390",
            "categories":"decors"
            },
         {
         "name":"sneakers",
         "image":"sneakers.webp",
         "description":"white sneakers|better grip  |best quality ",
         "price":"999",
         "categories":"mens_fashion"
        },
        {
            "name":"saliclic acid",
            "image":"saliclic.webp",
            "description":"cleanse the skin|reduce darkspot  |exfoliate the dead cells ",
            "price":"480",
            "categories":"beauty"
            }
    ]

@app.route("/")
def home():
    return render_template("home.html" , products=products)


#----------------------------categories--------------------------------
@app.route("/categories/mens_fashion")
def mens_faction():
    filter_products=[]

    for product in products:
        if product["categories"] == "mens_fashion":
            filter_products.append(product)
    return render_template("home.html", products=filter_products)


@app.route("/categories/elect")
def elect():
    filter_products=[]

    for product in products:
        if product["categories"] == "elect":
            filter_products.append(product)
    return render_template("home.html", products=filter_products)

@app.route("/categories/decors")
def decors():
    filter_products=[]

    for product in products:
        if product["categories"] == "decors":
            filter_products.append(product)
    return render_template("home.html", products=filter_products)

@app.route("/categories/beauty")
def beauty():
    filter_products=[]

    for product in products:
        if product["categories"] == "beauty":
            filter_products.append(product)
    return render_template("home.html", products=filter_products)

if __name__=="__main__":
    app.run(debug=True)
