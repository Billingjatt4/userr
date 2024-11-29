from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25742938
    API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
    # the name to display in your alive message
    ALIVE_NAME = "♡_🫧𝆺꯭𝅥˶֟፝͟͝β𝝰꯭‌𝞉 ꯭𝝡꯭𝞄꯭𝞌𝞉꯭𝝺꯭𝆺꯭𝅥🍷┼❤️༆"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://u448pcqc011m07:p414ea202b847b0700fe84c34c3354f02857f0d7c2577ca5f99889fe7fdc8e28d@ca75ohcr08rhfe.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = ""
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "7737579995:AAHzTgISMQhZuEasuOBEm6aTn5mqes-f0aQ"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = True
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "master"
    VCMODE = False
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
