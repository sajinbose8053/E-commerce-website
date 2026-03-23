
from flask import Flask ,render_template , request , redirect , session ,url_for,jsonify
app = Flask(__name__)

app.secret_key = "secret8053"


products = [
        {
            "id":1,
         "name":"Samsung S-26 Ultra",
         "image":"samsungs26.webp",
         "description":"12gb ram ,256 gb rom phone |newly privacy feauture added |4+years os updates and security paches ",
         "price":"120000",
         "categories":"elect"
         },
        {   
            "id":2,
            "name":"Oneplus bullet neck band",
            "image":"ONEplus neck band.jpg",
            "description":"12mm drivers|120hrs play back|ANC support ",
            "price":"5000",
            "categories":"elect"
            },
        {   
            "id":3,
            "name":"realme buds 5",
         "image":"realme buds5.webp",
         "description":"12mm drivers|120hrs play back|ANC support ",
         "price":"5000",
         "categories":"elect"
         },

        {
            "id":4,
         "name":"Oneplus powerbank 12000mah",
         "image":"OnePlus-150W-SuperVOOC.webp",
         "description":"fast charge support|2 device connectivity|military grade built quality ",
         "price":"4000",
         "categories":"elect"
         },

        {
         "id":5,
         "name":"addidas boot",
         "image":"boot.jpg",
         "description":"easy to run|2 years warrenty |military grade built quality ",
         "price":"15000",
         "categories":"mens_fashion"
        },

        {
         "id":6,
         "name":"Vitamin C Scerum",
         "image":"vitaminC.webp",
         "description":"skin moisture|skin brightner |rich in vitamin c ",
         "price":"400",
         "categories":"beauty"
         },
        {   
            "id":7,
            "name":"wall clock",
            "image":"wall clock.webp",
            "description":"asthetic hoome|wall deceration + time   |home decors ",
            "price":"650",
            "categories":"decors"
            },

            {
            "id":8,
            "name":"wall poster",
            "image":"wallposter.webp",
            "description":"asthetic hoome|wall deceration  |home decors ",
            "price":"390",
            "categories":"decors"
            },

         {
         "id":9,
         "name":"sneakers",
         "image":"sneakers.webp",
         "description":"white sneakers|better grip  |best quality ",
         "price":"999",
         "categories":"mens_fashion"
        },

        {   
            "id":10,
            "name":"saliclic acid",
            "image":"saliclic.webp",
            "description":"cleanse the skin|reduce darkspot  |exfoliate the dead cells ",
            "price":"480",
            "categories":"beauty"
            }
    ]
#-------------------------------------------HOME-----------------------------------------------

@app.route("/")
def home():
    return render_template("home.html" , products=products , username = session.get("username"))


#----------------------------------------login_page-----------------------------------------------

@app.route("/login", methods=["GET","POST"])
def login():

    #if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # simple login check
        if username == "sajin" and password == "1234":
            session["username"] = username
            return jsonify({"success":True})
        else:
            return jsonify({
                "success":False ,
                "message":"invalid username or password"})
        
        '''
        else:
            error = "Invalid Username or Password"
            return render_template("home.html",error=error ,products=products,show_login=True,username=session.get("username"))
    
    #return render_template("home.html" , show_login=True, username=session.get("username"))
    '''

    

#--------------------------------logout-------------------------------------------------------
@app.route("/logout")
def logout():
    session.pop("username" , None)
    return redirect("/")
    

#----------------------------categories--------------------------------
@app.route("/categories/mens_fashion")
def mens_faction():
    filter_products=[]

    for product in products:
        if product["categories"] == "mens_fashion":
            filter_products.append(product)
            
    return render_template("home.html", products=filter_products )


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

#----------------------------search products-----------------------------------------------------
'''

@app.route("/search" ,methods=["GET"])
def search():
    search = request.args.get("search")
    result = []

    if search:                                                                                                       # ------this is the search before including the js for search box 
        for product in products:
            if search.lower() in product["name"].lower() or search.lower() in product["description"].lower():
                result.append(product)
        return render_template("home.html", products = result)
        
    '''

# ---------------------------------------for dropdown suggestions---------------------------------------------------------
@app.route("/search-suggestions")
def search_suggestions():
    query = request.args.get("q", "").lower().strip()
    results = []

    if query:
        for product in products:
            if query in product["name"].lower():
                results.append(product["name"])

    return jsonify(results)

#------------------------------------ for full search result page---------------------------------------------------
@app.route("/search")
def search():
    query = request.args.get("q", "").lower().strip()
    matched_products = []

    if query:
        for product in products:
            if query in product["name"].lower():
                matched_products.append(product)
                

    return render_template("home.html", products=matched_products, query=query,username=session.get("username"))
    

#------------------------------------------product__page------------------------------------------

@app.route("/product/<int:id>")
def product_detail(id):
    for product in products:
        if product["id"] == id:
            username=session.get("username")
            return render_template("product.html", product=product, username=username)

if __name__=="__main__":
    app.run(debug=True)
