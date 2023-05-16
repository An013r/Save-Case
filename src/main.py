import os, sys, zip
index = 0
confloc = os.getenv("HOME") + "/.config/savecase.yaml"
mainarg = ""
extarg = []
for arg in sys.argv:
    if index == 0:
        index += 1
        continue
    if arg == "-h" or arg == "--help": #TODO: Write help page
        exit(0)
    if arg[0] != '-' and index == 1:
        index += 1
        mainarg = arg
        continue
    if arg[0] != '-' and index > 1:
        extarg.append(arg)
print(mainarg, extarg)

if mainarg == "addsync":
    if len(extarg) >= 3:
        print("Too many arguments")
    if len(extarg) < 2:
        print("Too little arguments")
    if extarg[0] == "archive":
        #zip.create(extarg[1])
        #TODO: Write a yaml library and implement
        """
        if not os.path.exists(confloc):
            os.popen("mkdir -p " + "/".join(confloc.split("/")[:-1]))
            #print("/".join(confloc.split("/")[:-1]))
            #exit(0)
            tmp = open(confloc, "w")
            tmp.close()
        conf = open(confloc, "a")
        conf.write("savelocation: \n    - " + extarg[1])
        print("Created archive and saved location in savelocation in config!")
        """