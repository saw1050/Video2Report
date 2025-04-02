from flask import Blueprint, request, send_file
from algorithm import create_report, add_subtitles
from config import config
from flask_login import login_required
import time

bp = Blueprint('main', __name__)
data_dump_path = config['default'].DATA_DUMP_PATH

@bp.route('/video-to-report', methods=['POST'])
@login_required
def video_to_report():
    print(request.method)
    print(request.url)
    print(request.args)
    print(request.headers)
    print(request.data.decode())
    username = request.form['username']
    doc_title = request.form['title']
    files = request.files
    video = files['video']
    suffix = video.filename.split('.')[-1]
    media_id = f'{username}-{time.time()}'
    media_name = f'{media_id}.{suffix}'
    video.save(f'{data_dump_path}/{media_name}')
    # doc_save_path = thread_pool.submit(create_report, f'{data_dump_path}/{media_name}', doc_title, media_id, f'{data_dump_path}/{media_id}')
    doc_save_path = create_report(f'{data_dump_path}/{media_name}', doc_title, media_id, f'{data_dump_path}/{media_id}', username)
    print(doc_save_path)
    return send_file(doc_save_path)


@bp.route('/video-add-subtitles', methods=['POST'])
@login_required
def video_add_subtitles():
    username = request.form['username']
    # doc_title = request.form['doc_title']
    files = request.files
    print(files)
    video = files['video']
    suffix = video.filename.split('.')[-1]
    media_id = f'{username}-{time.time()}'
    media_name = f'{media_id}.{suffix}'
    video.save(f'{data_dump_path}/{media_name}')
    video_with_subtitles_save_path = add_subtitles(f'{data_dump_path}/{media_name}', 40)
    return send_file(video_with_subtitles_save_path)