import requests


def get_first_five_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # вызовет исключение при ошибке 4xx/5xx
        
        posts = response.json()
        
        print("Первые 5 постов:\n")
        for i, post in enumerate(posts[:5], 1):
            print(f"Пост #{i}")
            print(f"Заголовок: {post['title']}")
            print(f"Текст:    {post['body']}")
            print("-" * 60)
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")


if __name__ == "__main__":
    get_first_five_posts()