import sys
if len(sys.argv) < 2: 
    print("none") 
else:
    args = sys.argv[1] 
    print(args.lower())