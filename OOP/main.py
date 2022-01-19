from user import User

from post import Post

app_user_one=User("dihfahsih@gmail.com", "Mugoya Dihfahsih","MugoYA23?","Software Developer")

app_user_one.get_user_info()

app_user_one.change_job(new_job="Software Engineer")

app_user_one.get_user_info()

new_post = Post("On a secret mission today", app_user_one.name)

new_post.get_post_info()