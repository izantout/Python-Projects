import os
from InstagramAPI import InstagramAPI

##### ----- Functions ----- #####

def loginToAccount(username, password):
    api = InstagramAPI(username, password)  # Initialize the Instagram API
    api.login()  # Log in to your account
    return api


def uploadPicture(username, password, image_path, caption):
    api = loginToAccount(username, password)
    if os.path.exists(image_path):
        print('File exists:', image_path)
        # Upload the picture
        with open(image_path, 'rb') as image:
            # path = image.read()[1:]
            api.uploadPhoto(image.read(), caption=caption)

        # Check if the upload was successful
        if api.LastResponse.status_code == 200:
            print("Picture uploaded successfully!")
        else:
            print("Error uploading picture")
        api.logout()
        print('logged out')
    else:
        print('File does not exist:', image_path)
        api.logout()
        print('logged out')

def uploadVideo(username, password, video_path, caption):
    api = loginToAccount(username, password)

    # Upload the video
    with open(video_path, 'rb') as f:
        api.uploadVideo(f, caption=caption)

    # Check if the upload was successful
    if api.LastResponse.status_code == 200:
        print("Video uploaded successfully!")
    else:
        print("Error uploading video")


def check_likes(username, password, media_id):
    api = loginToAccount(username, password)

    # Get the list of users who liked the media
    api.getMediaLikers(media_id)
    likes = api.LastJson

    # Create a list of the users who liked the media
    users_who_liked = [user['username'] for user in likes['users']]

    # Print the number of likes and the list of users who liked the media
    print(f'The media has {len(likes["users"])} likes.')
    print(f'Users who liked the media: {users_who_liked}')


def getFollowingAndFollowers(username, password):
    api = loginToAccount(username, password)
    following = []
    followers = []
    youFollowThemButTheyDontFollowYouBack = []
    theyFollowYouButYouDontFollowThemBack = []
    # Get the list of accounts that you follow
    api.getSelfUsersFollowing()
    for user in api.LastJson['users']:
        following.append(user['username'])
    # Get the list of accounts that follow you
    api.getSelfUserFollowers()
    for user in api.LastJson['users']:
        followers.append(user['username'])
    
    for username in following:
        if username not in followers:
            youFollowThemButTheyDontFollowYouBack.append(username)
    for username in followers:
        if username not in following:
            theyFollowYouButYouDontFollowThemBack.append(username)
            
    # Print the list of unfollowers and non-followers
    print("The people you follow but they dont follow you back are:", youFollowThemButTheyDontFollowYouBack)
    print("The people that follow you but you dont follow them back are:", theyFollowYouButYouDontFollowThemBack)


# Set your Instagram username and password
username = 'Your Username'
password = 'Your password'
image_path = os.path.join('Your 'Path', 'Here', 'photoName.jpg')
caption = 'Your caption'
                          
