from flask import Blueprint, render_template
import logging

errors = Blueprint('errors', __name__)

logger = logging.getLogger('flaskblog')

@errors.app_errorhandler(404)
def error_404(error):
    logger.error('404: page not found')
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    logger.error('403: Forbidden')
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    logger.error('500: Too long to respond')
    return render_template('errors/500.html'), 500