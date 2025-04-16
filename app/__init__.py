import os
import logging
from flask import Flask, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_toastr import Toastr

from config import Config
from logging.handlers import TimedRotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import cloudinary

cloudinary.config(
    cloud_name="dqogaxemt",
    api_key="185533732234982",
    api_secret="boacO5AeE5GSaClvKVmg1YTIjJY",
    secure=True,
)


# Khởi tạo ứng dụng Flask
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config.from_object(Config)

# Khởi tạo SQLAlchemy và Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app.models import * # Import models để chúng có thể được phát hiện bởi Flask-Migrate
print("[DEBUG] Loaded models:", db.metadata.tables.keys())

# mail = Mail(app)
# toastr = Toastr(app)

# Configuration for uploads files
app.config['MEDIA_FOLDER'] = os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), '..', 'uploads' )
app.config['MEDIA_URL'] = '/uploads/'

# Đảm bảo thư mục tồn tại
if not os.path.exists(app.config['MEDIA_FOLDER'] ):
    os.makedirs(app.config['MEDIA_FOLDER'] )

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'zip'}

# Configures the logging
def configure_logging(app):
    # Create a file handler which logs even debug messages
    handler = TimedRotatingFileHandler('flask-template.log', when='midnight', interval=1, backupCount=10)
    handler.setLevel(logging.INFO)  # Set the log level you want here
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

configure_logging(app)

from app.routes.main import main
app.register_blueprint(main)

from .routes.admin import admin_bp
app.register_blueprint(admin_bp)

# Serve uploads files
@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)

# @app.route('/static/admin/plugins/ckfinder/ckfinder.html', methods=['GET', 'POST'])
# def ckfinder_connector():
#     # Thực hiện các xử lý cần thiết với file
#     # Ví dụ, bạn có thể sử dụng Flask để upload, xóa file dựa trên các yêu cầu từ CKFinder
#     pass

app.debug = True
toolbar = DebugToolbarExtension(app)