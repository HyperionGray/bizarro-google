from sys import argv, exit
import json
from tabulate import tabulate

#{'form': {'search': 0.9967199965383483}, 'fields': {'q': {'search query': 0.9987888899121808}, 'btnI': {'submit button': 0.9738968692339827}, 'btnG': {'submit button': 0.9801990433706371}}}

def print_form_keys(forms):
    for form in forms:
        #print(form)
        formval = form[0]["form"]
        for k,v in formval.items():
            print(k, v)

    
def search_form_type(forms, search_term):
    for form in forms:
        formval = form[0]["form"]
        #print(formval)
        for key in formval.keys():
            if search_term in key:
                return True

    return False


if __name__ == "__main__":

    usage = "usage: python search.py searchurl|searchbody|searchformtype|searchformfield your_search_term\n\nResults are printed to the terminal."
    if len(argv) < 3:
        print(usage)
        exit(1)
    
    f = open("final_results_forms.jl")
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

    elif argv[1] == "searchformtype":
        search_term = argv[2]
        for line in f:
            #print(line)
            _url = list(json.loads(line.strip()).keys())[0]
            if _url.strip() == "forms":
                _url = list(json.loads(line.strip()).keys())[1]
                #print(list((json.loads(line.strip()).keys())))

            line_json = json.loads(line.strip())
            if search_form_type(line_json["forms"], search_term):
                print("===============================================================")
                print(_url)
                print("===============================================================")
                print_form_keys(line_json["forms"])
            
    elif argv[1] == "searchformfield":
        pass
        
    else:
        print(usage)
        exit(1)
