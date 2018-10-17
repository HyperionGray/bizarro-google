import formasaurus
import json

def process_forms():
    f = open("final_results.jl")
    f_write = open("final_results_forms.jl", "w")
    for line in f:
        line_dic = json.loads(line.strip())
        html = list(line_dic.values())[0].strip()
        if html.strip():
            try:
                forms_all = strip_el(formasaurus.extract_forms(html, proba=True, threshold=0.05))
                line_dic["forms"] = forms_all
                f_write.write(json.dumps(line_dic))
                f_write.write("\n")
            except:
                pass

def strip_el(forms):
    forms_all_minus = []
    for form in forms:
        forms_all_minus.append(form[1:])

    return forms_all_minus


if __name__ == "__main__":
    print(process_forms())
