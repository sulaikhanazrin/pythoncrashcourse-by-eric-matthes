def build_profile(first, last, **user_info):
    """Dictionary with user profile"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('alex','ribbon', location='london',field='physics')
user_profile = build_profile('tom', 'ravalon', location='ottawa', field='architect')
print(user_profile)