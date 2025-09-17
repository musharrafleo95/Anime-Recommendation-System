from utils.helpers import *
from config.path_config import *

from pipeline.prediction_pipeline import hybrid_recommendation



print(getAnimeFrame(40028, ANIME_DF))
user_id = 11880

similar_users = find_similar_users(user_id, USER_WEIGHTS_PATH, USER2USER_ENCODED, USER2USER_DECODED)
print(similar_users)
user_pref = get_user_preferences(user_id, RATING_DF, ANIME_DF)
print(user_pref)

print(hybrid_recommendation(user_id=user_id))