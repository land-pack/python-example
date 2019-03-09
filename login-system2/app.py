import uuid
import hashlib
import logging.config

from flask import Flask, render_template, make_response, request, redirect, url_for
import redis

import log
import color

from db import DB, MySQLCursorDict


app = Flask(__name__)
app.config['LOGGER_HANDLER_POLICY'] = 'always'  # 'always' (default), 'never',  'production', 'debug'
app.config['LOGGER_NAME'] = 'femmapi'  # define which logger to use for Flask
app.logger  # initialise logger

logging.config.dictConfig(log.LoggerConfig.dictConfig)

print(app.logger.name)

r = redis.Redis(host="127.0.0.1", port=6379)

class UserModeul(object):

    def add_one(self, username, email, password):
        sql = """
            INSERT INTO t_user
            (f_email, f_password)
            VALUES(%s, %s)
        """
        with DB() as db:
            cursor = db.cursor()
            cursor.execute(sql, (email, password))
            db.commit()

    def get_one(self, email):
        sql = """
            SELECT f_email, f_password, f_status
            FROM t_user
            WHERE f_email=%s
        """
        with DB() as db:
            cursor = db.cursor(cursor_class=MySQLCursorDict)
            cursor.execute(sql, (email,))
            record = cursor.fetchone()
        return record

class Password(object):
    def encode(self, string):
        md5 = hashlib.md5()
        md5.update(string.encode('utf-8'))
        res = md5.hexdigest()
        return res
    
    def check(self, string, scret):

        c = self.encode(string)
        app.logger.info("c=[%s] || s=[%s]", c, scret)
        return str(c) == scret

@app.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    username = request.form.get('username', 'root')
    password = request.form.get('password', 'root')
    print("username={} || password={}".format(username, password))
    if request.method == "POST":
        record  = UserModeul().get_one(username)
        app.logger.info("record=%s", record)
        if record is None:
            app.logger.warning("Not such user, name as =%s", username)
            return render_template("auth/signup.html")

        if Password().check(password, record[1]):
            res = make_response(redirect('/vips'))
            expires_time = 60 * 60 * 24
            person_info = "skanfanfl aksndkansd aks dksabd aksndas"
            token_key = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
            res.set_cookie("token", token_key)
            r.set(token_key, person_info, expires_time)
            
            return res
        else:
            app.logger.warning("Password error, and try again, name as =%s", username)
            return render_template("auth/login.html")

    else:
        return render_template("auth/login.html")


@app.route("/auth/signup", methods=['GET', 'POST'])
def signup():
    emailsignup = request.form.get('emailsignup', 'root')
    usernamesignup = request.form.get('usernamesignup', 'root')
    passwordsignup = request.form.get('passwordsignup', 'root')
    passwordsignup_confirm = request.form.get('passwordsignup_confirm', 'root')

    app.logger.info("""emailsignup=%s || usernamesignup=%s
                    || passwordsignup=%s || passwordsignup_confirm=%s""",
                    emailsignup, usernamesignup, passwordsignup,
                    passwordsignup_confirm)
    if request.method == "POST":
        passwordsignup = Password().encode(passwordsignup)
        UserModeul().add_one('guest', emailsignup, passwordsignup)
        return redirect(url_for('auth_login'))

    else:
        return render_template("auth/signup.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitl
    return render_template('error/404.html'), 404


if __name__ == '__main__':
    app.run(debug=False)
