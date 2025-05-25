import requests

# URL of the CSV file
url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2024/12/3888260f107e3701e3cd81af49ef997cf70b6395.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20250521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250521T081235Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=09413e5f74a6a5061e1a733281de9173a52152077fa9aea2841fa6c4389b39b2'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a local file in write-binary mode
    with open('downloaded_file.csv', 'wb') as f:
        f.write(response.content)
    print("File downloaded successfully!")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
