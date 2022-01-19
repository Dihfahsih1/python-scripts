import requests

responses=requests.get("https://gitlab.com/api/v4/users/dihfahsih1/projects")
my_projects = responses.json()

for project in my_projects:
  print(f'Project Name: {project["name"]} \nProject Url: {project["web_url"]}\n')