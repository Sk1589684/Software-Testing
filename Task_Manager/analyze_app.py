import urllib.request
import re

url = "https://taskmanagement.ai.studio/assets/index-C6VqzLCx.js"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Search for axios baseURL
pos = content.find('baseURL')
while pos != -1:
    print("baseURL context:", content[max(0, pos-50):min(len(content), pos+150)])
    pos = content.find('baseURL', pos+1)

# Search for task creation schema
task_schema = re.findall(r'(\w+=\$h\(\{[^\}]+title:[^\}]+\}\))', content)
print("Task schema:", task_schema)

# Search for task creation form
pos = content.find('/tasks')
while pos != -1 and pos < 500000:
    print("Around /tasks:", content[max(0, pos-100):min(len(content), pos+200)])
    pos = content.find('/tasks', pos+1)
