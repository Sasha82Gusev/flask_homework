from flask import Flask, jsonify
from views import AdvertisementView
from errors import ApiException

app = Flask('app')


@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({
        'status': 'error',
        'message': error.message
    })
    response.status_code = error.status_code
    return response


def hello_world():

    return jsonify({'hello': 'world'})


app.add_url_rule('/hw', view_func=hello_world, methods=['GET'])
app.add_url_rule('/advertisements/<int:adv_id>', view_func=AdvertisementView.as_view('users'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/advertisements/', view_func=AdvertisementView.as_view('users_create'), methods=['POST'])


app.run()
