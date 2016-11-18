'''
Problem:  Bad Neighbors      https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
          The old song declares "Go ahead and hate your neighbor", and the 
          residents of Onetinville have taken those words to heart. Every 
          resident hates his next-door neighbors on both sides. Nobody is 
          willing to live farther away from the town's well than his neighbors, 
          so the town has been arranged in a big circle around the well. 
          Unfortunately, the town's well is in disrepair and needs to be 
          restored. You have been hired to collect donations for the Save 
          Our Well fund.

          Each of the town's residents is willing to donate a certain amount, 
          as specified in the int[] donations, which is listed in clockwise order 
          around the well. However, nobody is willing to contribute to a fund to 
          which his neighbor has also contributed. Next-door neighbors are always 
          listed consecutively in donations, except that the first and last entries 
          in donations are also for next-door neighbors. You must calculate and 
          return the maximum amount of donations that can be collected. 
'''

def getMaxDonation(donationList):
    size = len(donationList)
    d = [[0, 0]]*size
    if d:
        d[0] = [donationList[0], 1]
    if size > 1:
        d[1] = [donationList[1], 0]
    if size > 2:
        for i in range(2, size-1):
            sublist = d[:i-1]
            subsize = len(sublist)
            maxDonation = 0
            containFirst = 1
            for j in range(subsize):
                if maxDonation > sublist[j][0]:
                    continue
                if maxDonation == sublist[j][0]:
                    containFirst = sublist[j][1]*containFirst
                else:
                    containFirst = sublist[j][1]
                maxDonation = sublist[j][0]
            d[i] = [donationList[i]+maxDonation, containFirst]
        sublistForLast = d[1:size-2]
        maxDonationForLast = 0
        for element in sublistForLast:
            if element[1] == 1:
                continue
            if maxDonationForLast < element[0]:
                maxDonationForLast = element[0]
        d[size-1] = [donationList[size-1]+maxDonationForLast, 0]
    result = max([x[0] for x in d])
    return result
    
if __name__ == '__main__':
    testSample1 = [10, 3, 2, 5, 7, 8]
    testSample2 = [11, 15]
    testSample3 = [7, 7, 7, 7, 7, 7, 7]
    testSample4 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    testSample5 = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
                   6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
                   52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
                   
    print getMaxDonation(testSample1)
    print getMaxDonation(testSample2)
    print getMaxDonation(testSample3)
    print getMaxDonation(testSample4)
    print getMaxDonation(testSample5)
    
    
    
    