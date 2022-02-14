import threading

import requests

url1 = "https://www.youtube.com/"
url2 = "https://www.youtube.com/watch?v=EqFzY8dBWHs&ab_channel=EduardoMendes"
url3 = (
    "https://www.youtube.com/watch?v=VhhNlWdLPzA&t=1202s&ab_channel=ProgramandoComRoger"
)
url4 = "https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/learn/lecture/29432174#overview"


def do_request(url):
    requests.get(url)
    return print(f"requisição feita pra {url}")


t1 = threading.Thread(target=do_request, args=(url1,))
t2 = threading.Thread(target=do_request, args=(url2,))
t3 = threading.Thread(target=do_request, args=(url3,))
t4 = threading.Thread(target=do_request, args=(url4,))

thread_list = [t1, t2, t3, t4]

for t in thread_list:
    print("64646")
    t.start()
