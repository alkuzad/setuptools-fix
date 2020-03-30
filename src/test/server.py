from flask import Flask, redirect, request, after_this_request
from flask_basicauth import BasicAuth

app = Flask('302test')

app.config['BASIC_AUTH_USERNAME'] = 'test'
app.config['BASIC_AUTH_PASSWORD'] = 'pass'

basic_auth = BasicAuth(app)

@app.route('/simple/pip-tools/')
@basic_auth.required
def index():
    return '''
    <html>
    <body>
        <a href="/packages/pip_tools-4.5.0-py2.py3-none-any.whl" data-requires-python="&gt;=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*">pip_tools-4.5.0-py2.py3-none-any.whl</a><br/>
        </body>
    </html>
    '''

@app.route('/packages/<packagefile>')
@basic_auth.required
def packages(packagefile):
    @after_this_request
    def add_header(response):
        response.headers['X-Artifactory-Id'] = 'someid'
        response.headers['X-Artifactory-Node-Id'] = 'someid'
        response.headers['Cache-Control'] = 'someid'
        response.headers['Connection'] = 'keep-alive'
        response.headers['X-Request-ID'] = 'somerequestid'
        return response
    return redirect('https://test-302-setuptools.s3.amazonaws.com/pip_tools-4.5.0-py2.py3-none-any.whl?AWSAccessKeyId=ASIAVASKNV5WQFRHL6XU&Signature=wJM7ZBjZIfW3kKHywKsxA%2BsYw6Y%3D&x-amz-security-token=FwoGZXIvYXdzEAIaDOaFV5WmPYD1cpzBWiKCAcXWYP7vzCUxuxSiF7QNAOX8u9bDmA14ZkP31WO8UVKV1CvIKnjq%2FG8ODMrckHOZvrKrIl4W%2Bq6G97%2FVBl4Cf%2B7%2BqAguWTuIkeprrVu0kJ%2FlPnss8dIic%2BSkFuG68r8zVBNpQ2t0LH1gxtYT8vq1NSJck03yjyyi0DqlhO1%2BfYSC3GAoreSG9AUyKAcdoEl1qMXNYIsJ%2FEFlS68ywup%2BBR%2FxrPUcwKIxPT%2BTDjfV1Q2sAJo%3D&Expires=1585817379', 302)

if __name__ == "__main__":
   app.run(port=8000)
