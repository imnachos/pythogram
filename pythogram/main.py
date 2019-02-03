from InstagramAPI import InstagramAPI
from pythogram import settings as cfg, utilities as util

api = InstagramAPI(cfg.USER, cfg.PASSWORD)

saved_cookies = util.get_last_session_cookies()
if saved_cookies is not None:
    api.s.cookies = saved_cookies

if api.login():

    util.save_last_session_cookies(api.s)
    print("Login succes!")

    followers_json = util.get_total_followers(api, api.username_id)
    following_json = util.get_total_followings(api, api.username_id)

    followers_list = []
    followings_list = []

    for follower_user in followers_json:
        username = follower_user.get('username')
        followers_list.append(username)

    for following_user in following_json:
        username = following_user.get('username')
        followings_list.append(username)

    not_following_back = list(set(followings_list) - set(followers_list))
    not_following_them = list(set(followers_list) - set(followings_list))

    last_followers_list = util.get_follower_list()
    stopped_following_since_last = list(set(last_followers_list) - set(followers_list))
    print('Users that stopped following since last time: ', stopped_following_since_last)
    util.save_follower_list(followers_list)

    new_followers_since_last = list(set(followers_list) - set(last_followers_list))
    print('Users that started following since last time: ', new_followers_since_last)

    print('Users that are not following back: ', not_following_back)
    print('Users that you are not following: ', not_following_them)

else:
    print("Can't login!")
    util.clean_cookies()



