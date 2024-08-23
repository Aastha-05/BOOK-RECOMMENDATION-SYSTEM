# import requests
# import urllib.parse

# class Request:
#     def __init__(self, method, args):
#         self.args=args
#         self.method=method


# request=Request('GET', {'search':"Galvin"})

# if request.method == 'GET':
#     search=urllib.parse.quote(request.args.get('search', ''))
#     # url=f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=1"
#     url=f"https://www.googleapis.com/books/v1/volumes?q=%7Bsearch%7D&maxResults=1"
#     response=requests.get(url)
#     #print(response.json())

#     if response.status_code==200:  #200 means the request was successful, 404 means not found, 401 means unauthorized
#         data = response.json()
#         for item in data.get('item',[]):
#             volume_info = item.get('volumeInfo', {})
#             title = volume_info.get('title','N/A')
#             publisher = volume_info.get('publisher', 'N/A')
#             published_date=volume_info.get('publishedDate', 'N/A')
#             author=volume_info.get('authors', ['N/A'])
#             rating=volume_info.get('averageRating',['N/A'])
#             image_link=volume_info.get('imageLinks', {})
#             image=image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'
            
#             print(title)
#             print(publisher)
#             print(published_date )
#             print(author)
#             print(rating)
#             print(image)


import requests
import urllib.parse

class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method

request = Request('GET', {'search': "Galvin"})

if request.method == 'GET':
    search = urllib.parse.quote(request.args.get('search', ''))
    url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=1"
    response = requests.get(url)

    if response.status_code == 200:  # 200 means the request was successful
        data = response.json()
        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', 'N/A')
            publisher = volume_info.get('publisher', 'N/A')
            published_date = volume_info.get('publishedDate', 'N/A')
            author = volume_info.get('authors', ['N/A'])
            rating = volume_info.get('averageRating', 'N/A')
            image_link = volume_info.get('imageLinks', {})
            image = image_link.get('thumbnail', 'N/A')
            
            print("Title:", title)
            print("Publisher:", publisher)
            print("Published Date:", published_date)
            print("Author(s):", ", ".join(author))
            print("Rating:", rating)
            print("Image URL:", image)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
