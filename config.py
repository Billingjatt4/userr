from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25742938
    API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
    # the name to display in your alive message
    ALIVE_NAME = "♡_🫧𝆺꯭𝅥˶֟፝͟͝β𝝰꯭‌𝞉 ꯭𝝡꯭𝞄꯭𝞌𝞉꯭𝝺꯭𝆺꯭𝅥🍷┼❤️༆"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://oaykvtmj:bsIGPV7wmId1x1CNH9eqxQVX5t25cHI3@manny.db.elephantsql.com/oaykvtmj"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "1BZWaqwUAUD43K5aIkXqPBYANp7MOkRB81TplGCA85UrUjc-_CIuB7Cu92H8QudHb5ledoQhn66Hf5FEVpuNV4B7foaGjIOyuzA154wLhf79nFH5nDAr63qVu21TUaeRSQ39IGtmg4mqdd1TPwcDZocG6qnY8uJAsLHDYArvTzblNBJxL4dybniOvYhMaWtHc38Pi6AJdXjrkHM2SATQmaP7psmJQ9xdYKLruPmpH7Jl9FDAzpclUY25NV2YXpO5YhLSNJQOv6tPldqrTS-7R7Xp2EzBxJS4Joodc8NRymg_8HRIYs7n39PvZJwRVt1uwnSoCZ0snrdNOvVLnu_guQWDf0e0Uq2k="
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
