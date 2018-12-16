
from flask import Flask, render_template
from foo import get_records, get_record_by_id
from foo import make_google_map_url, make_google_streetview_url

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html', records=get_records())
    return html


@app.route('/<id>')
def detail(id):
    record = get_record_by_id(id)
    s_url = make_google_streetview_url(record['x'], record['y'])
    m_url = make_google_map_url(record['x'], record['y'])
    html = render_template('detail.html', record=record,
                            streetview_url=s_url,
                            map_url=m_url)
    return html


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
