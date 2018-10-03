import grequests
import json

def exception_handler(request, exception):
    print("Request failed")

links_filename = "top-10000.csv"
links = open(links_filename)

robots_filename = "robots_results.txt"
clear = open(robots_filename,"w")
clear.close()

hosts_num_lines = sum(1 for line in links)
links.close()

links = open(links_filename)

reqs = grequests.imap((grequests.get("http://" + link.split(",")[1].strip() + "/robots.txt", timeout=0.2, allow_redirects=True, stream = False) for link in links), size=20)

f = open(robots_filename, "a")
c = 0
for req in reqs:
    #f.write((json.dumps({req.url : req.text})))
    try:
        print(req.url)    
        for line in req.text.split("\n"):
            line = line.strip()
            #print(line)
            if line.lower().startswith("disallow"):
                #print(line)
                f.write(re.sub('/robots.txt', '', req.url.strip()) + "/" + line.lower().split(":")[1].strip())
                f.write("\n")
        c += 1
        req.close()
        if c % 10 == 0:
            print("=============Finished %s of robots requests out of %s============" % (str(c), str(hosts_num_lines)))

    except:
        print("Failed on %s" % req.text)
            
f.close()
print("Finished robots requests...")

robots_results_filename = "final_results.jl"
clear = open(robots_results_filename, "w")
clear.close()

links = open(robots_filename)
linkreqs = grequests.imap((grequests.get(link, timeout=0.2, allow_redirects=True, stream = False) for link in links), size=20)
f = open(robots_results_filename, "a")

robots_num_lines = sum(1 for line in open(robots_filename))

c = 0
for req in linkreqs:
    print(req.url)
    #print(req.text)
    f.write(json.dumps({req.url : req.text}))
    f.write("\n")
    c += 1
    if c % 10 == 0:
        print("===========Finished %s of disallows out of %s=================" % (str(c), str(robots_num_lines)))
    req.close()
        
#if __name__ == '__main__':
#    session.run(_main)

