
def split_data(filename):
    f= open(filename,"r")
    m_1=[] #data from one microphone
    m_2=[] #data from the other microphone

    l = 0
    for i in f:
        if (l%2 == 0):
            m_1.append(i)
        else:
            m_2.append(i)
        l += 1
    f.close()
    return [m_1,m_2]
