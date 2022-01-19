class User:
  def __init__(self,email, name, pswd, job):
      self.email = email
      self.name = name
      self.password = pswd
      self.job = job
      
  def change_password(self,new_password):
    self.password = new_password
    
  def change_job(self,new_job):
    self.job = new_job
    
  def get_user_info(self):
    print(f"User {self.name} currently works as {self.job}. You can contact them at {self.email}")

      