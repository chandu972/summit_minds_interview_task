import json

if __name__ == "__main__":
    id = 0
    json_files = ['G:\DataScienceLearning\customersdata.json']
    fraudent_data = []
    for json_file in json_files:
        with open(json_file, 'r')  as jf:
            for line in jf:
                fraudent_data.append(json.loads(line))
                # print(line)

    print(len(fraudent_data))
    # for id, val in enumerate(fraudent_data):
    #     print("id is {} and person profile is {}".format(id, val))

    # for fraudulent in fraudent_data:
    #     print(fraudulent)

    for i in fraudent_data:
        cmd = i['fraudulent']
        if i['fraudulent'] == True:
            print(i['customer'])
        # print(cmd)