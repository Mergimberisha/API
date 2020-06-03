import requests

# path = 'http://api.postcodes.io/postcodes/'
# arguments = 'SW1X 7LX'


# url_target = path + arguments
# print(url_target)


# response = requests.get(url_target)

# print(response)
# print(type(response))

# print(response.json())
# response_dictionary = response.json()

# print(type(response_dictionary))

# for key in response_dictionary.keys():
#     print(key)

# result_dictionary = response_dictionary['result']

# print(result_dictionary)

# for key in result_dictionary.keys():
#     print(key, 'the value inside is', result_dictionary[key])



                                                                # Task 1
# Make a function that take in a postcode
# Handle your errors for all the status codes
# responds back with
#         your longitude is <>, yourlatitude is <> and your parliamentary_constituenc <>

import requests
while True:
    path = 'http://api.postcodes.io/postcodes/'
    arguments = input("Please enter your post code ")
    arguments.replace(" ", "")
    if arguments == "Thank you, I am done for today" or "exit" in arguments:
        print("Program finished")
        break
    url_target = path + arguments
    response = requests.get(url_target)
    json_response = response.json()
    print(json_response["result"].keys()) # To show all of the keys in the result dictionary
    print(f"Your longitude value is {json_response['result']['longitude']}")
    print(f"Your latitude value is {json_response['result']['latitude']}")
    print(f"Your parliamentary constituency value is {json_response['result']['parliamentary_constituency']}")
    print(f"Your NUTS value is {json_response['result']['nuts']}")