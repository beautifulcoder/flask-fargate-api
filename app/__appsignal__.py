from appsignal import Appsignal

appsignal = Appsignal(
    active=True,
    name="flask-fargate-api",
    # Please do not commit this key to your source control management system.
    # Move this to your app's security credentials or environment variables.
    # https://docs.appsignal.com/python/configuration/options.html#option-push_api_key
    push_api_key="push_api_key"
)
