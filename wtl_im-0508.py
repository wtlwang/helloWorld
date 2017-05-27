# -*- coding: utf-8-*-
import json
import pdb

dic={
    "data": {
        "displayAgents": [
            {
                "agentUcid":"001",
                "reason":u"我能最及时的响应"
            },
            {
                "agentUcid":"002",
                "reason":u"我对本房源最了解，所有和本房相关的问题，能给您最准确的答复"
            },
            {
                "agentUcid":"003",
                "reason":u"我能很好的理解客户需求，给您相关的决策建议"
            }
        ]
    },
    "errorCode": 0,
    '123':456
     
}
#dic= dict(1:1)
print dic
print dic["data"]["displayAgents"][0]['agentUcid']
print dic["data"]["displayAgents"][0]['reason']
print '\n'
pdb.set_trace()
strDic=json.dumps(dic)
print strDic
print '\n'
dic2=json.loads(strDic)
print dic2
print dic2["data"]["displayAgents"][1]["reason"]


if dic==dic2:
    print "dic==dic2"
else:
    print "dic!=dic2"
