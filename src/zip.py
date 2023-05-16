import os

def create(location):
    os.popen("echo '' > /tmp/savecase.txt && zip -u /tmp/savecase.zip /tmp/savecase.txt && zip -d /tmp/savecase.zip tmp/savecase.txt && mv /tmp/savecase.zip " + location).read()
    os.popen("rm /tmp/savecase.txt").read()
def list(archive):
    output = os.popen("zipinfo " + archive).read().split("\n")
    output = output[2:-2]
    #print(output)
    out = []
    for ln in output:
        out.append(ln.split(" ")[-1])
    return out
def add(archive, *fls):
    for fl in fls:
        if not os.path.exists(fl) or not os.path.exists(archive):
            raise FileNotFoundError("No Such File or Directory: " + fl)
    os.system("zip -u " + archive + " " + " ".join(fls))
def rm(archive, *fls):
    afls = list(archive)
    print(afls)
    for fl in fls:
        if not fl in afls:
            raise FileNotFoundError("No Such File or Directory in Archive: " + fl)
        else:
            os.system("zip -d " + archive + " " + fl)