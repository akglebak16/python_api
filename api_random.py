import requests

class Test_new_joke():


    def __init__(self):
        pass


    def test_create_new_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Status code: " + str(result.status_code))
        assert 200 == result.status_code
        print("Success, we have a new joke!")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("True categorie")
        check_info_value = check.get("value")
        print(check_info_value)
        assert "Chuck" in check_info_value
        print("Value is succesed")
random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()