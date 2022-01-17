def check_ids(people, confidence, number_of_ids):
    temp_array = []
    for i in range(number_of_ids):
        temp_array.append([])

    if len(people) != len(set(people)):
        counter = 0
        for i in people:
            if people.count(i) > 1:
                temp_array[i].append(counter)
            counter += 1
        for i in range(number_of_ids):
            if len(temp_array[i]) > 1:
                number = min(confidence[n] for n in temp_array[i])
                temp_array[i] = [number]
        for i in range(len(people)):
            if len(temp_array[people[i]]) > 0:
                if confidence[i] != temp_array[people[i]][0]:
                    people[i] = 0

    return people
