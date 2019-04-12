from pymongo import MongoClient
import json

client=MongoClient()
db=client["test"]
collection=db["question bank"]

def getquestions(skill):
    qbank = []
    l = collection.find()
    for i in l:
        for ques in i[skill]:
            qbank1 = {}
            qbank1['question'] = ques["Question"]
            qbank1['choice1'] = ques["Option"][0]["A"]
            qbank1['choice2'] = ques["Option"][0]["B"]
            qbank1['choice3'] = ques["Option"][0]["C"]
            qbank1['choice4'] = ques["Option"][0]["D"]
            qbank1['answer'] = ques["ans"]
            qbank.append(qbank1)
    print (qbank)
    return qbank
