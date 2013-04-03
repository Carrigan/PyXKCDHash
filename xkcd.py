import skein, datetime

available = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
             'A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', \
             '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '?', \
             '<', '>', '(', ')', '+', '-', '[', ']', ' ')

xkcd = '5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4f' + \
       'df9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87' + \
       'f4757be023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24' + \
       'b567aa3e2390a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6'

xkcd = int(xkcd,16)

def processBytes(bytesIn):
    """
    Return the difference (based on an xor) between the hashed value and the
    target value.
    """
    hashedValue = skein.skein1024(bytesIn)
    n = int(hashedValue.hexdigest(),16)
    diff = bin(n ^ xkcd).count('1')
    return diff

def getBytesBySeed(seed):
    """
    My belief is that the key is a word or phrase. Thus, I am making keys
    out of common usable characters. This function returns a byte array
    object based on the seed going in.
    """
    stringout = ''
    while(seed > 0):
        currentCharacter = seed % 74
        stringout += available[currentCharacter]
        seed = seed // 74
    return stringout.encode('ascii')


# Open the log and get the goodies. This is for a sequential counter
try:
    log = open('xkcd.txt', 'r')
    i = int(log.readline())
    lowest = int(log.readline())
except:
    log = open('xkcd.txt', 'w')
    log.write('0\n500\n\n')
    i = 0
    lowest = 500

# Print to the console
print(datetime.datetime.now())
print("Starting hash finder, i = " + str(i) + ", lowest= " + str(lowest))
print("\n")

# Keep going until a Control-C
try:
    while True:
        # To make this random: change i to some random function.
        currentKey = getBytesBySeed(i)
        currentDifference = processBytes(currentKey)
        if(currentDifference < lowest):
            currentTime = datetime.datetime.now()
            log = open('xkcd.txt', 'a')
            log.write(str(currentTime))
            log.write('\t')
            log.write(str(currentDifference) + '\t')
            log.write(str(i) + '\t')
            log.write(currentKey.decode('ascii'))
            log.write('\n')
            log.close()
            print(str(currentDifference) + ' ' + currentKey.decode('ascii'))
            lowest = currentDifference
        i = i+1
        if not i % 1000000:
            print("Pulse: " + str(datetime.datetime.now()) + ' :: ' + str(i))
except KeyboardInterrupt:
    # Once CTRL-C is hit, save the new lowest and i values, then quit
    print("Exiting at i = " + str(i))
    log = open('xkcd.txt', 'r')
    lines = log.readlines()
    lines = lines[2:]
    log.close()
    log = open('xkcd.txt', 'wt')
    log.write(str(i) + '\n')
    log.write(str(lowest) + '\n')
    for line in lines:
        log.write(line)
    log.close()
