from flask import Flask

app = Flask(__name__)
app.secret_key = "jkasfhab"

#方式一：
#app.config["SESSION_COOKIE_NAME"] = "session_lvning"
#方式二：
#app.config.from_pyfile("setting.py")
#方式三：
# import os
# os.environ["FLASK_SETTING"] = "setting.py"
# os.environ.from_envvar("FLASK_SETTING")

#方式四：
app.config.from_object("settings.BaseConfig")
print(app.config["NNN"])

if __name__ == '__main__':
    app.run()