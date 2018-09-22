# Contains help functions for the task of transforming a multivariate dataset based on EHR data into 
# a numerical dataset using distance functions.

def alphabetical_diff(c1, c2):
    """
    Returns the alphabetical difference of two characters.
    """
    return abs(string.ascii_lowercase.index(c1) - string.ascii_lowercase.index(c2))  

def alphadist(s1, s2):
    """
    A standard Levenshtein distance with the addition of substitution operations modified according to the alphabetical difference or
    effort required to change a character into another.
    """
    
    # Switch s1 and s2 such that s1 is the shortest
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:

                if(distances_[0] > len(s1)):
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
                else:
                    distances_.append(alphabetical_diff(c1,c2))
        distances = distances_
    return distances[-1]
