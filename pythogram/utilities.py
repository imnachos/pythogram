import json, pickle


def save_last_session_cookies(session):
    with open('session', 'wb') as f:
        pickle.dump(session.cookies, f)


def save_follower_list(followers):
    with open('followers.txt', 'wb') as f:
        pickle.dump(followers, f)


def get_follower_list():
    with open('followers.txt', 'rb') as f:
        return pickle.load(f)


def save_following_list(following):
    with open('following.txt', 'wb') as f:
        pickle.dump(following, f)


def get_following_list():
    with open('following.txt', 'rb') as f:
        return pickle.load(f)


def get_last_session_cookies():
    with open('session', 'rb') as f:
        return pickle.load(f)


def clean_cookies():
    with open('session', 'rb') as f:
        pickle.dump('', f)


def get_total_followers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        response = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def get_total_followings(api, user_id):
    """
    Returns the list of followings of the user.
    It should be equivalent of calling api.getTotalFollowings from InstagramAPI
    """

    followings = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        response = api.getUserFollowings(user_id, maxid=next_max_id)
        followings.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followings
