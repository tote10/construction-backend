
import urllib.request
import json
import urllib.error

def test_login(username, password):
    url = 'http://127.0.0.1:8000/api/token/'
    data = json.dumps({'username': username, 'password': password}).encode('utf8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    print(f"Testing login for user: {username}")
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Status: {response.getcode()}")
            print(f"Response: {response.read().decode()}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        print(f"Error Body: {e.read().decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_login('totie', 'wrongpassword')
    test_login('nonexistent', 'test')
