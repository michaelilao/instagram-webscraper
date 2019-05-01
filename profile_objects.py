class Profile:
    def __init__(self, name,followers,following,num_posts,profilePic,posts):
        self.name = name
        self.followers = followers
        self.following = following
        self.num_posts = num_posts
        self.profilePic = profilePic
        self.posts = posts

    #Setters
    def set_name(self,name):
        self.name = name

    def set_followers(self,followers):
        self.followers = followers

    def set_following(self,following):
        self.following = following

    def set_num_posts(self,num_posts):
        self.num_posts = num_posts

    def set_profilePic(self,profilePic):
        self.profilePic = profilePic

    def set_posts(self,posts):
        self.posts = posts

    #Getters
    def get_name(self):
        return self.name
    def get_followers(self):
        return self.followers
    def get_following(self):
        return self.following
    def get_num_posts(self):
        return self.num_posts
    def get_profilePic(self):
        return self.profilePic
    def get_posts(self):
        return self.posts

    #View
    def view_name(self):
        print("Name: ",self.get_name())
    def view_followers(self):
        print("Number of Followers: ",self.get_followers())
    def view_following(self):
        print("Number of Following: ",self.get_following())
    def view_num_posts(self):
        print("Number of posts: ",self.get_num_posts())
    def view_profilePic(self):
        print("Link to Profile Picture", self.get_profilePic())

    def view_all(self):
        self.view_name()
        self.view_followers()
        self.view_following()
        self.view_num_posts()


class Picture:
    def __init__(self,likes,comments,caption,link):
        self.likes = likes
        self.comments = comments
        self.caption = caption
        self.link = link
