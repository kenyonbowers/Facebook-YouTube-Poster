import facebook

# Set your Facebook access token and page ID
ACCESS_TOKEN = '<Your_Facebook_Access_Token>'
PAGE_ID = '<Your_Facebook_Page_ID>'

# Prompt the user to enter the YouTube video ID and additional information
youtube_video_id = input('Enter the YouTube video ID: ')
description = input('Enter the description: ')

# Compose the Facebook Graph API request payload
post_data = {
    'message': f'{description}\nhttps://www.youtube.com/watch?v={youtube_video_id}'
}

# Create a Facebook Graph API instance with the access token
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='3.0')

# Post the live stream link to Facebook
try:
    graph.put_object(parent_object=PAGE_ID, connection_name='feed', **post_data)
    print('Live stream link posted to Facebook!')
except facebook.GraphAPIError as e:
    print('Failed to post live stream link to Facebook:\n', e)
