status_code = int(input("HTTP Status Code:"))

if status_code <= 100:
    print("informational repsonse - the request was received, continuing process")
elif status_code <= 200:
    print("successful- the request was successfully received, understood, and accepeted")
elif status_code <= 300:
    print("further action needs to be taken in order to complete the request")
elif status_code <= 400:
    print("client error - the request contains bad syntax or cannot be fulfilled")
elif status_code <= 500:
    print("server error - the server failed to fulfil an apparently valid request")
else:
    print("invalid")

print("Program complete")