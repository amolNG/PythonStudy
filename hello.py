from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
	return "\nHello World!\n"

@app.route("/ABC")
def ABC():
	return "\nABC ABC\n"

@app.route("/addpost" , methods = ['POST'])
def addpost():
   language = request.args.get('language')
   my_body = request.get_json() 

   new_ret = language + " Received"
   print("\nmy_body::")
   print(my_body)
   print(request)
   print("\n")
   return my_body





if __name__ == '__main__':
	app.run(debug=True)


