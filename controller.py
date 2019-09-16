from flask import Flask

app = Flask(__name__)
print(app)

@app.route('/api/AC/on', methods=["POST"])
def ac_on():
    return "AC ON!"

#app.run()

if __name__ == '__main__':
    app.run()
