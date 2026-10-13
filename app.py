from flask import Flask,jsonify
#create our Flask application
app = Flask(__name__)

#home endpoint:provides basic project information
@app.route("/",methods=["GET"])
def home():
    return jsonify({
        "project":"PyCore Server",
        "message":"Our python server is running!",
        "status":"success"
    })

#Health endpoint:checks wther the server is responding
@app.route("/health",methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


#Run the server when this file is executed directly
if __name__=="__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )


