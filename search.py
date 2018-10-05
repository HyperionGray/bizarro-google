from sys import argv, exit
import json

if __name__ == "__main__":

    usage = "usage: python search.py searchurl|searchbody your_search_term\n\nResults are printed to the terminal."
    if len(argv) < 3:
        print(usage)
        exit(1)
    
    f = open("final_results.jl")
    if argv[1] == "searchurl":
        search_term = argv[2].strip()
        for line in f:
            _url = list(json.loads(line.strip()).keys())[0]
            if search_term in _url:
                split_url = _url.split(search_term)
                print(_url)

    elif argv[1] == "searchbody":
        search_term = argv[2]
        for line in f:
            _body = list(json.loads(line.strip()).values())[0]            
            _url = list(json.loads(line.strip()).keys())[0]
            if search_term in _body:
                print("=============================%s===============================" % _url)
                print(_body)
        
    else:
        print(usage)
        exit(1)
