def rand_int(obj):
    num = hash(obj) % 1000
    return num

def get_email_prefix(email):
    split_email = email.split('@')

    if len(split_email) == 2:
        return email.split("@")[0]
    
    return -1