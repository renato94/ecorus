from flask import current_app as app
from flaskapp.database import db_session


@app.teardown_request
def session_clear(exception=None):
    app.logger.debug("Removing DB session")
    db_session.remove()
    if exception and db_session.is_active:
        db_session.rollback()


@app.errorhandler(500)
def handle_500(error):
    return 'application error', 500


@app.errorhandler(404)
def page_not_found(error):
    return 'that page does not exist', 404
