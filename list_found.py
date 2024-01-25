def agents(list_found, list_records):
    if not list_found:
        return None
    if list_found in list_records:
        return "Match found"
    else:
        return "No matches"
    

def agents(list_found, list_records):
    if list_found:
        return "Match found" if list_found in list_records else "No matches"