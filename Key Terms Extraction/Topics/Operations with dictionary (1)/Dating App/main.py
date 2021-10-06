def select_dates(potential_dates):
    names = []
    for item in potential_dates:
        if item['age'] > 30 and 'art' in item["hobbies"] and item['city'] == 'Berlin':
            names.append(item['name'])
    output = names[0]
    for i in range(1, len(names)):
        output += ', ' + names[i]
    return output
