import requests
import bs4
from profile_objects import Picture
from profile_objects import Profile

from lxml import html
def unblockeduser(url):

    response = requests.get(url)
    session_requests = requests.session()
    if(response.status_code>=200):
        profile = scrapeData(response.text)
    else:
        print("Page Not Reached")
        return 0


def findCaption(data):
    caption_pattern = "edge_media_to_caption\":{\"edges\":[{\"node\":{\"text\":\""
    start_caption_index = data.find(caption_pattern) + len(caption_pattern)
    caption_pattern_end = "\"}}]},"
    end_caption_index = data.find(caption_pattern_end)

    caption = data[start_caption_index:end_caption_index]
    return caption

def findComments(data):
    comment_pattern = "\"edge_media_to_comment\":{\"count\":"
    start_comment_index = data.find(comment_pattern) + len(comment_pattern)
    comment_pattern_end = "},\"comments_disabled\""
    end_comment_index = data.find(comment_pattern_end)

    comments = data[start_comment_index:end_comment_index]
    return int(comments.strip())

def findLikes(data):
    likes_pattern = "\"edge_liked_by\":{\"count\":"
    start_likes_index = data.find(likes_pattern) + len(likes_pattern)
    likes_pattern_end = "},\"edge_media_preview_like\":"
    end_likes_index = data.find(likes_pattern_end)

    likes = data[start_likes_index:end_likes_index]
    return int(likes.strip())

def findFollowerCount(data):
    follower_pattern = "\"edge_followed_by\":{\"count\":"
    start_follower_index = data.find(follower_pattern) + len(follower_pattern)
    follower_pattern_end = "},\"followed_by_viewer\""
    end_follower_index = data.find(follower_pattern_end)

    followers = data[start_follower_index:end_follower_index]
    return int(followers.strip())

def findFollowingCount(data):
    following_pattern = "\"edge_follow\":{\"count\":"
    start_following_index = data.find(following_pattern) + len(following_pattern)
    following_pattern_end = "},\"follows_viewer\":"
    end_following_index = data.find(following_pattern_end)

    followings = data[start_following_index:end_following_index]
    return int(followings.strip())

def findLink(data):
    link_pattern = ",\"thumbnail_src\":\""
    start_link_index = data.find(link_pattern) + len(link_pattern)
    link_pattern_end = "\",\"thumbnail_resources\":"
    end_link_index = data.find(link_pattern_end)

    link = data[start_link_index:end_link_index]
    return link

def findPosts(data):
    post_pattern = "edge_owner_to_timeline_media\":{\"count\":"
    start_post_index = data.find(post_pattern) + len(post_pattern)
    post_pattern_end = "\"page_info\":{\"has_next_page\""
    end_post_index = data[start_post_index:].find(post_pattern_end) + start_post_index - 1

    posts = data[start_post_index:end_post_index]
    return int(posts.strip())

def findProfilePic(data):
    profile_pattern = "profile_pic_url_hd\":\""
    start_profile_index = data.find(profile_pattern) + len(profile_pattern)
    profile_pattern_end = "\",\"requested_by_viewer\""
    end_profile_index = data.find(profile_pattern_end)

    profilePic = data[start_profile_index:end_profile_index]
    return profilePic

def scrapeData(pagedata):

    soup_obj = bs4.BeautifulSoup(pagedata,'lxml')
    profile_name = soup_obj.select('title')[0].getText()
    profile_name = (profile_name[0:profile_name.find("Instagram photos and videos")-2]).strip()
    results = pagedata.split("{\"node\":{\"__typename\":")

    posts = findPosts(results[0])
    followers = findFollowerCount(results[0])
    following = findFollowingCount(results[0])
    profilePic = findProfilePic(results[0])


    del results[0]
    posts = []
    for pic in results:
        caption = findCaption(pic)
        comments = findComments(pic)
        likes = findLikes(pic)
        link = findLink(pic)
        post = Picture(likes,comments,caption,link)
        posts.append(post)

    profile = Profile(profile_name,followers,following,posts,profilePic,posts)

    return profile
