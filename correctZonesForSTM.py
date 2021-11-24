import json

# Opening JSON file
with open('zones.json') as f:
    data = json.load(f)

valuesToReplace = {
    "<+00>": "GMT",
    "<-01>": "CVT",
    "<-10>": "NUT",
    "<-11>": "HST",
    "<-12>": "AOE",
    "<-02>": "WGST",
    "<-0230>": "NDT",
    "<-03>": "ART",
    "<-04>": "AST",
    "<-05>": "EST",
    "<-06>": "CST",
    "<-07>": "MST",
    "<-08>": "PDT",
    "<-09>": "AKST",
    "<-0930>": "MART",
    "<+01>": "BST",
    "<+10>": "AEST",
    "<+1030>": "LHST",
    "<+11>": "SBT",
    "<+12>": "ANAT",
    "<+1245>": "CHAST",
    "<+13>": "TOT",
    "<+1345>": "CHADT",
    "<+14>": "LINT",
    "<+02>": "CEST",
    "<+03>": "MSK",
    "<+0330>": "IRST",
    "<+04>": "GST",
    "<+0430>": "IRDT",
    "<+05>": "UZT",
    "<+0530>": "IST",
    "<+0545>": "NPT",
    "<+06>": "BST",
    "<+0630>": "MMT",
    "<+07>": "WIB",
    "<+08>": "CST",
    "<+0845>": "ACWST",
    "<+09>": "JST",
    "<+0930>": "ACST"
}
def reprocessJson (data):
    for i in data:
        for j in valuesToReplace:
            data[i] = data[i].replace(j, valuesToReplace[j])

reprocessJson(data)
with open('correctedZones.json', 'w') as outfile:
    json.dump(data, outfile, indent=0, sort_keys=True, separators=(",", ":"))
