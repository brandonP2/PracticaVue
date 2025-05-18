from flask import Flask, request, Response
from flask_cors import CORS
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)

CORS(app, resources={
    r"/graphql": {
        "origins": ["http://localhost:8080"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/graphql', methods=['OPTIONS'])
def handle_options():
    response = Response('')
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    ),
    methods=['GET', 'POST'] 
)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')