import os

def split_data(filename):
    f= open(filename,"r")
    m_0=[] #data from one microphone
    m_1=[] #data from the other microphone

    l = 0
    for i in f:
        if (l%2 == 0):
            m_0.append(i)
        else:
            m_1.append(i)
        l += 1
    f.close()
    return [m_0,m_1]

def writeArrayToFile(folderpath, filename, m_0, m_1):
    filename_0 = "0-" + filename
    filename_1 = "1-" + filename

    newfolderpath = folderpath + "/separated"
    #os.mkdir(newfolderpath)
    if not os.path.exists(newfolderpath+"/mic0"):
        os.makedirs(newfolderpath+"/mic0")

    if not os.path.exists(newfolderpath+"/mic1"):
        os.makedirs(newfolderpath+"/mic1")

    f = open(newfolderpath+"/mic0/"+filename_0, "w+")
    for i in m_0:
        f.write(str(i))
    f.close()

    f = open(newfolderpath+"/mic1/"+filename_1, "w+")
    for i in m_1:
        f.write(str(i))
    f.close()

    return 0


def separatefile(filePath):

    filePath = "./" + filePath
    fileList = os.listdir(filePath)
    for filename in fileList:
        if filename != "*.txt" :
            fileList.remove(filename)

    for filename in fileList:
        print(filename)
        incoming_file_path = filePath + "/" + filename
        if (filename != "separated"):
            a = split_data(incoming_file_path)
        writeArrayToFile(filePath, filename, a[0], a[1])



    return 0



#separatefile("echo4")
#separatefile("echo5_1")
#separatefile("echo5_2")
separatefile("echo1")
separatefile("echo2")
separatefile("echo3")



