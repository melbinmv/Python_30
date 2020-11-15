import sys
from datetime import datetime
from formatting import format_msg
import requests
#Positional arguments are not optional
# def send(name,website):
    
#     msg = format_msg(my_name =name, my_website = website) 
#     return msg

def send(name,website = None, verbose = False):
    # if website != None:
    #     msg = format_msg(my_name=name, my_website=website)
    # else:
    #     msg = format_msg(my_website=name)
    if verbose:
        print(name,website)
    #msg = format_msg(my_name =name, my_website = website) 
    r = requests.get("http://httpbin.org/json")
    if r.status_code ==200:
        return r.json()
    else:
        return "There was an Error"
# response = send("Justin", verbose = True) .........used when import
# print(response)

# if __name__ == "__main__":
#     response = send("Justin", verbose = True) .........used when import
#     print(response)


if __name__ == "__main__": #_name_ has the current module name, when executed directly
    print(sys.argv) #can identify the arguments passed through cmd
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, verbose = True)
    print(response)



    
