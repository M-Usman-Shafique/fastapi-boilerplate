from langgraph.checkpoint.mongodb import MongoDBSaver

from app.configs.settings import get_settings

settings = get_settings()

uri = settings.MONGODB_URI

if "?" in uri:
    uri += "&tlsAllowInvalidCertificates=true"
else:
    uri += "?tlsAllowInvalidCertificates=true"

saver_cm = MongoDBSaver.from_conn_string(uri, settings.DB_NAME)
