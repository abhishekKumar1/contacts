import data

#Given an email-id will search by it. In case of database since
#email will be the primary key, will query using same.
def get_by_email(email):
    for user in data.contacts:
        if(user["email"]) == email:
            return user
    return False

#Given the first-name will search by it. In case of database I will partition by this
#so that it can be faster.
def get_by_first_name(name, limit, offset):
    users = []
    for user in data.contacts:
        if(user["first_name"]) == name:
            users.append(user)
    if len(users) == 0 :
        return False
    else:
        users = users[offset:offset+limit]
        if len(users) == 0 :
            return False
        users.append({"next_page_uri": "/get/name/" + name + "?offset=" + str(offset + len(users))})
    return users

#To add a new user
def add_user_in_db(first_name, last_name, email ,phone_number):
    # will do upsert here so that this can be used for both add or edit 
    return True

#To delete a user
def delete_user_in_db(email):
    flag = get_by_email(email)
    if flag == False:
        return False 
    return True