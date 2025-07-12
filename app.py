from flask import Flask, render_template
import some_nonexistent_module

app = Flask(__name__)

@app.route('/')
def home():
    debug_value = app.config['DEBUG']
    return render_template('index.html', title="Home")

@app.route('/divide')
def divide_numbers():
    numerator = 10
    denominator = 0
    result = numerator / denominator
    return f"The result is {result}"

@app.route('/users/<int:user_id>')
def show_user(user_id):
    users = {1: "Alice", 2: "Bob"}
    return f"User: {users[user_id]}"

if __name__ == '__main__':
    app.run()