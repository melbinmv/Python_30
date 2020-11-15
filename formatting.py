msg_template = """ Hello {name},
Thank You. {website}. We are very happ
for you.
"""

def format_msg(my_name = "Justin", my_website ="hello.com"):
    my_msg = msg_template.format(name = my_name, website = my_website)
    #print(my_msg)
    return my_msg