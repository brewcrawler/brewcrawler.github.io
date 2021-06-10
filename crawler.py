import json
import os.path

big_malt_list = []
big_hop_list = []
big_yeast_list = []

def dump_to_json(type, list):
    data_path = os.path.dirname(__file__)
    json_object = json.dumps(list, indent = 4)
    with open(data_path+"/"+type+"_datas.json", "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.dirname(__file__)+"/shops")
    from shops import *
    arr = os.listdir(os.path.dirname(__file__)+"/shops")
    for file in arr:
        if file != "__init__.py" and file != "__pycache__" and ".py" in file and "olasz" not in file:
            run = file.replace(".py","")+".crawl_malts()"
            locals = {}
            list = exec("list = "+run, None, locals)
            big_malt_list.extend(locals["list"])

            run = file.replace(".py","")+".crawl_hops()"
            locals = {}
            list = exec("list = "+run, None, locals)
            big_hop_list.extend(locals["list"])

            run = file.replace(".py","")+".crawl_yeasts()"
            locals = {}
            list = exec("list = "+run, None, locals)
            big_yeast_list.extend(locals["list"])

    dump_to_json("malt", big_malt_list)
    dump_to_json("hop", big_hop_list)
    dump_to_json("yeast", big_yeast_list)
    #print(big_hop_list)