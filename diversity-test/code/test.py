from itertools import combinations, permutations from math import comb,
factorial from collections import Counter import numpy as np import pandas as
pd import pickle import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------#
#-----------some functions for translating between rankings in different forms#
#-----------convert standard ranking to position (also count of wins) vector
def ranktopos(rankvec, natord): pos = np.zeros(len(rankvec), dtype=int) for k
in range(len(rankvec)): for l in range(len(natord)): if rankvec[k] ==
natord[l]: pos[l] = k return pos check = ranktopos([7, 5, 3, 1], [1, 3, 5, 7])
print(check) #print(list(pos.keys())[1]) #-----------convert position (also
count of wins) vector to standard ranking def ranktoposinv(posvec, natord):
    rank = np.zeros(len(natord), dtype=int) for k in range(len(posvec)):
        rank[posvec[k]] = natord[k] return rank check = ranktoposinv([3, 2, 1,
                                                                      0], [1,
                                                                           3,
                                                                           5,
                                                                           7])
                                                                      print(check)
                                                                      #-----------convert
                                                                      binary
                                                                      (n-ch-2)
                                                                      ranking
                                                                      to
                                                                      position
                                                                      (count of
                                                                       wins)
                                                                      vector
                                                                      def
                                                                      bintopos(binvec,
                                                                               natord):
                                                                          if
                                                                          (len(binvec)
                                                                           !=
                                                                           comb(len(natord),2))\
                                                                                   or
                                                                                   (type(binvec[0])
                                                                                    !=
                                                                                    type(natord[0])):
                                                                                       print("ERROR:
                                                                                       len"
                                                                                             +
                                                                                             str(1/0))
                                                                                   else:
                                                                                       pos
                                                                                       =
                                                                                       np.zeros(len(natord),
                                                                                                dtype=int)
                                                                                       c
                                                                                       =
                                                                                       list(combinations(range(len(pos)),
                                                                                                         2))
                                                                                       while
                                                                                       sum(pos)
                                                                                       <
                                                                                       len(c):
                                                                                           for
                                                                                           k
                                                                                           in
                                                                                           range(len(binvec)):
                                                                                               for
                                                                                               l
                                                                                               in
                                                                                               range(len(natord)):
                                                                                                   if
                                                                                                   binvec[k]
                                                                                                   ==
                                                                                                   natord[l]:
                                                                                                       pos[l]
                                                                                                       +=
                                                                                                       1
                                                                                                       return
                                                                                                   pos
                                                                                                   check
                                                                                                   =
                                                                                                   bintopos([1,
                                                                                                             1,
                                                                                                             1,
                                                                                                             3,
                                                                                                             3,
                                                                                                             5],
                                                                                                            [1,
                                                                                                             3,
                                                                                                             5,
                                                                                                             7])
                                                                                                            print(check)
                                                                                                            #-----------convert
                                                                                                            position
                                                                                                            (count
                                                                                                             of
                                                                                                             wins)
                                                                                                            vector
                                                                                                            to
                                                                                                            binary
                                                                                                            (n-ch-2)
                                                                                                            ranking
                                                                                                            def
                                                                                                            bintoposinv(posvec,
                                                                                                                        natord):
                                                                                                                c
                                                                                                                =
                                                                                                                list(combinations(range(len(posvec)),
                                                                                                                                  2))
                                                                                                                binvec
                                                                                                                =
                                                                                                                np.zeros(len(c),
                                                                                                                         dtype=int)
                                                                                                                l
                                                                                                                =
                                                                                                                0
                                                                                                                for
                                                                                                                k
                                                                                                                in
                                                                                                                c:
                                                                                                                    if
                                                                                                                    posvec[k[0]]
                                                                                                                    <
                                                                                                                    posvec[k[1]]:
                                                                                                                        binvec[l]
                                                                                                                        =
                                                                                                                        natord[k[1]]
                                                                                                                    else:
                                                                                                                        binvec[l]
                                                                                                                        =
                                                                                                                        natord[k[0]]
                                                                                                                        l
                                                                                                                        +=
                                                                                                                        1
                                                                                                                        return
                                                                                                                    binvec
                                                                                                                    check
                                                                                                                    =
                                                                                                                    bintoposinv([3,
                                                                                                                                 2,
                                                                                                                                 1,
                                                                                                                                 0],
                                                                                                                                [1,
                                                                                                                                 3,
                                                                                                                                 5,
                                                                                                                                 7])
                                                                                                                                print(check)
                                                                                                                                #-----------convert
                                                                                                                                rankings
                                                                                                                                to
                                                                                                                                binary
                                                                                                                                (n-choose-2)
                                                                                                                                form
                                                                                                                                def
                                                                                                                                ranktobin(rankvec,
                                                                                                                                          natord):
                                                                                                                                    posvec
                                                                                                                                    =
                                                                                                                                    ranktopos(rankvec,
                                                                                                                                              natord)
                                                                                                                                    binvec
                                                                                                                                    =
                                                                                                                                    bintoposinv(posvec,
                                                                                                                                                natord)
                                                                                                                                    return
                                                                                                                                binvec
                                                                                                                                #-----------convert
                                                                                                                                rankings
                                                                                                                                in
                                                                                                                                binary
                                                                                                                                (n-choose-2)
                                                                                                                                form
                                                                                                                                to
                                                                                                                                standard
                                                                                                                                rankings
                                                                                                                                def
                                                                                                                                bintorank(binvec,
                                                                                                                                          natord):
                                                                                                                                    posvec
                                                                                                                                    =
                                                                                                                                    bintopos(binvec,
                                                                                                                                             natord)
                                                                                                                                    rankvec
                                                                                                                                    =
                                                                                                                                    ranktoposinv(posvec,
                                                                                                                                                 natord)
                                                                                                                                    return
                                                                                                                                rankvec
                                                                                                                                #-----------the
                                                                                                                                Kendall-tau
                                                                                                                                distance
                                                                                                                                between
                                                                                                                                two
                                                                                                                                rankings
                                                                                                                                in
                                                                                                                                n-choose-2
                                                                                                                                form
                                                                                                                                def
                                                                                                                                ktdistancebin(p,
                                                                                                                                              q):
                                                                                                                                    p
                                                                                                                                    =
                                                                                                                                    np.array(p)
                                                                                                                                    q
                                                                                                                                    =
                                                                                                                                    np.array(q)
                                                                                                                                    if
                                                                                                                                    len(p)
                                                                                                                                    ==
                                                                                                                                    len(q)
                                                                                                                                    and
                                                                                                                                    len(p)
                                                                                                                                    >
                                                                                                                                    0
                                                                                                                                else
                                                                                                                                print("ERROR:
                                                                                                                                len")
                                                                                                                                d
                                                                                                                                =
                                                                                                                                sum(p
                                                                                                                                    !=
                                                                                                                                    q)
                                                                                                                                return
                                                                                                                            d
                                                                                                                            check
                                                                                                                            =
                                                                                                                            ktdistancebin([1,
                                                                                                                                           1,
                                                                                                                                           2],
                                                                                                                                          [2,
                                                                                                                                           3,
                                                                                                                                           3])
                                                                                                                                          print(check)
                                                                                                                                          #-----------the
                                                                                                                                          Kendall-tau
                                                                                                                                          distance
                                                                                                                                          between
                                                                                                                                          two
                                                                                                                                          rankings
                                                                                                                                          in
                                                                                                                                          standard
                                                                                                                                          form
                                                                                                                                          #def
                                                                                                                                          ktdistance(p,
                                                                                                                                                     q):
                                                                                                                                              #    if
                                                                                                                                              #    len(p)
                                                                                                                                              #    !=
                                                                                                                                              #    len(q)
                                                                                                                                              #    or
                                                                                                                                              #    len(p)
                                                                                                                                              #    ==
                                                                                                                                              #    0:
                                                                                                                                              #    print("ERROR:
                                                                                                                                              #    len"
                                                                                                                                              #    +
                                                                                                                                              #    str(1/0))
                                                                                                                                              #    else:
                                                                                                                                              #    p
                                                                                                                                              #    =
                                                                                                                                              #    np.array(p)
                                                                                                                                              #    q
                                                                                                                                              #    =
                                                                                                                                              #    np.array(q)
                                                                                                                                              #    pp
                                                                                                                                              #    =
                                                                                                                                              #    list(p)
                                                                                                                                              #    natord
                                                                                                                                              #    =
                                                                                                                                              #    []
                                                                                                                                              #    while
                                                                                                                                              #    len(pp)
                                                                                                                                              #    >
                                                                                                                                              #    0:
                                                                                                                                              #    natord.append(min(pp))
                                                                                                                                              #    pp.remove(min(pp))
                                                                                                                                              #    p
                                                                                                                                              #    =
                                                                                                                                              #    ranktobin(p,
                                                                                                                                              #    natord)
                                                                                                                                              #    q
                                                                                                                                              #    =
                                                                                                                                              #    ranktobin(q,
                                                                                                                                              #    natord)
                                                                                                                                              #    d
                                                                                                                                              #    =
                                                                                                                                              #    sum(p
                                                                                                                                              #    !=
                                                                                                                                              #    q)
#        return d
#check = ktdistance([3, 1, 2], [2, 3, 1]) #print("The ktdistance of [3, 1, 2]
and [2, 3, 1] is:") #print(check) #-----------convert string representation of
numpy array (no commas) into array def strtovec(s): s = s.replace("[", "") s =
s.replace("]", "") v = [int(n) for n in s.split()] return np.array(v) check =
strtovec(str(np.zeros(3, dtype=int))) print(check) #-----------the ktdistances
between all n-factorial rankings of a set of size n #def alldistances(natord):
#    perm = np.array(list(permutations(natord))) n = len(perm) d = {} for i in
#    range(n): for j in range(i + 1, n): k = np.array((i, j)) d[str(k)] =
#    ktdistancebin(ranktobin(perm[i], natord), ranktobin(perm[j], natord))
#    return d
#check = alldistances([1, 2, 3])
#print(check)
#check2 = tuple(check.keys())
#print(check2)
#check3 = check2[1]
#print(check3)
#check4 = check[check3]
#print(check4)
#check2 = np.array(list(permutations([1, 2, 3])))
#check = check2[strtovec(check3)]
#print(check)
##check = ktdistance(*check)
#print(check)
#-----------function computing distances given a set of rankings (bin form)
def ranklstodistls(listofran):
    ls = []
    z = listofran
    c = combinations(listofran, 2)
    for el in c:
        print(el[0]); print(el[1])
        k = ktdistancebin(el[0], el[1])
        if k > 0:
            ls.append(k)
    return ls
test1 = [np.array([1, 2, 3]), np.array([2, 1, 3]), np.array([2, 3, 1]),
         np.array([3, 2, 1])]
test = ranklstodistls(test1)
print(test)
#-----------function for distances from ranking to set of rankings (bin form)
def newrankdistances(new, listofran):
    l = len(listofran)
    k = np.zeros(l, dtype=int)
    for i in range(l):
        k[i] = ktdistancebin(new, listofran[i])
    return k
test1 = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [3, 2, 1]]
test2 = ranklstodistls(test1)
test3 = np.array([3, 1, 2])
test = newrankdistances(test3, test1)
print(test)
#-----------function computing the allcount increment given a list of distances
def distvectocount(dist):
    totcount = 0
    if Counter(dist)[3] >= 2 or Counter(dist)[2] >= 3:
        totcount = 6
    elif Counter(dist)[3] == 1:
        totcount = 4
    elif Counter(dist)[2] == 1:
        totcount = 3
    elif Counter(dist)[1] == 1:
        totcount = 2
    return totcount
test = distvectocount(test)
print(test)
test1 = [0, 2, 1, 1]
test = distvectocount(test1)
print(test)
test1 = [0, 1, 2, 3]
test = distvectocount(test1)
print(test)
test1 = [0, 1, 2, 3]
test = distvectocount(test1)
print(test)
#-----------the algorithm uses the next function to update the dict of results
def updatelists(obr, d, ak, dd, nrj, step):
    lobr = len(obr)
    #---initial step (may not be j = 0)
    if lobr == 0:
        obr.append(nrj)
        d.append(0)
        ak.append(0)
        dd.append(step)#list(dp.index)[j]
    #---the inductive step
    else:
        newd = newrankdistances(nrj, obr)
        #---only do something if nrj is indeed new
        if np.count_nonzero(newd) == lobr:
            obr.append(nrj)
            d.extend(newd)
            ak.append(distvectocount(d))
            dd.append(step)
    return
#-----------fcn of algorithm that counts rankings under null hypothesis: linear
def genresults(dictofdiv_pts, arraycombstr, numofdays, testthreshold,
               resultspath):
    #-------abbreviations for div_pts objects
    acs = arraycombstr
    resdict = {}
    dictlsls = {i : [[], [], [], []]  for i in acs}
    ak = np.zeros(len(acs), dtype=int)
    freq = np.zeros(numofdays, dtype=int)
    cumfreq = np.zeros(numofdays, dtype=float)
    dd = np.zeros(len(acs), dtype=int)
    xceptn = []
    k = np.zeros(len(acs), dtype=int)
    for h in range(len(acs)):
        i = acs[h]
        dp = dictofdiv_pts[i]
        ldp = len(dp)
        dpk = tuple(dp.keys())
        #-------start the main loop for i
        print("hello")
        while ak[h] < testthreshold and k[h] in range(ldp):
            j = dpk[k]
            print(j)
            #---abbreviations for the lists
            rj = strtovec(dp[j])
            print(i,rj)
            #---the key step:
            updatelists(*dictlsls[i], rj, j)
            print(dictlsls[i])
            ak[h] = dictlsls[i][2][-1]
            k[h] += 1
            print("Current allcount is", ak[h])
            if ak[h] == testthreshold:
                freq[j] += 1
                cumfreq[j:] += 1
        print("the dates for", i, "are", dictlsls[i][3])
        dd[h] = dictlsls[i][3][-1]
        if ak[h] < testthreshold:
            xceptn.append(strtovec(i))
        print(dd[h])
    #-----------save test results to file
    with open(resultspath[testthreshold], "wb") as f:
        pickle.dump(resdict, f)
    testthreshold += 2
    for h in range(len(acs)):
        i = acs[h]
        dp = dictofdiv_pts[i]
        ldp = len(dp)
        dpk = tuple(dp.keys())
        #-------start the main loop for i
        print("hello")
        while ak[h] < testthreshold and k[h] in range(ldp):
            j = dpk[k]
            print(j)
            #---abbreviations for the lists
            rj = strtovec(dp[j])
            print(i,rj)
            #---the key step:
            updatelists(*dictlsls[i], rj, j)
            print(dictlsls[i])
            ak[h] = dictlsls[i][2][-1]
            k[h] += 1
            print("Current allcount is", ak[h])
            if ak[h] == testthreshold:
                freq[j] += 1
                cumfreq[j:] += 1
    resdict = {"testdctlsls" : dictlsls, "divpersubset" : ak, "datefin" : dd,
               "freqperday" : freq, "cumfreqperday" : cumfreq,
               "xceptn": xceptn,}
    #-----------save test results to file
    with open(resultspath[testthreshold], "wb") as f:
        pickle.dump(resdict, f)
    return
#-----------create dict of locations and rankings where diversity may increase
def get_diversity_pts(subsets, rankdf, fin, astring, start=0):
    fin = len(rankdf)
    dd = {}
    for h in range(len(subsets)):
        i = subsets[h]
        dd[i] = {}
        dd[i][start] = rankdf[i][start]
        for j in range(start + 1, fin):
            if rankdf[i][j] != rankdf[i][j - 1]:
                dd[i][j] = rankdf[i][j]
    with open(astring, "wb") as f:
        pickle.dump(dd, f)
    return dd
#-----------pull in rankings and countofrankings files
def genascendingdfs(datapath, svenypath):
    rankings_dec = pd.read_csv(datapath + "rankings.csv")
    #countof = pd.read_csv(datapath + "countof.csv")
    sveny_dec = pd.read_csv(svenypath + ".csv")
    sveny_dec = sveny_dec.iloc[0:len(rankings_dec),:]
    print(len(sveny_dec))
    rankings_dec.rename(sveny_dec['Date'], axis='index', inplace=True)
    #countof.rename(sveny_dec['Date'], axis='index', inplace=True)
    rankings_asc = rankings_dec[::-1]
    with open(datapath + "rankings-asc.pkl", "wb") as f:
        pickle.dump(rankings_asc, f)
    sveny_asc = sveny_dec[::-1]
    with open(datapath + "sveny-asc.pkl", "wb") as f:
        pickle.dump(sveny_asc, f)
#=============================================================================#
#-----------processing begins here (above functions to go in a separate module)
#=============================================================================#
#-----------number of maturity dates
mat = 30
#-----------subset size (eg 3 if testing partial-3-diversity or 3-diversity)
sub = 3
subch2 = comb(sub, 2)
#-----------threshold for the test: 4 for p3div and 6 for 3div
threshold = 6
#-----------order of the dates in rankings and sveny (ascending or descending)
order = "asc"
#-----------generate indices for subsets of four maturity dates
a = np.array(list(combinations(range(1, mat + 1), sub)))
a = list(range(1, 15))
a.extend([25, 26, 27, 29, 30])
a = np.array(list(combinations(a, sub)))
scomb = [str(a[i]).strip('[]') for i in range(len(a))]
scomb = [scomb[i].split() for i in range(len(a))]
scomb = [' '.join(scomb[i]) for i in range(len(a))]
scomb = ['[' + scomb[i] + ']' for i in range(len(a))]
print(scomb[8])
#-----------string for file names
s = "data/" + str(mat) + "choose" + str(sub)
#=============================================================================#
#-----------path to SVENY data
pathtosveny = "data/FED-SVENY-20230224"
#-----------uncomment to generate rankings and sveny df with ascending dates
#genascendingdfs(s, pathtosveny)
#-----------load the div_pts dict for testing
if order == "asc":
    with open (s + "rankings-asc.pkl", "rb") as f:
        rankings = pickle.load(f)
    with open (s + "sveny-asc.pkl", "rb") as f:
        sveny = pickle.load(f)
elif order == "dec":
    rankings = pd.read_csv(s + "rankings.csv");
    sveny = pd.read_csv(pathtosveny + ".csv")
#-----------number of days for which the test will be conducted
num_days = len(rankings)
#print(list(rankings.columns))
#=============================================================================#
#-----------path diversity points file
pathtodivpts = s + "diversity_pts_" + order + ".pkl"
#-----------uncomment to generate div_pts (may take a while) saves to path
#get_diversity_pts(scomb, rankings, num_days, pathtodivpts)
#-----------load the div_pts dict for testing
with open (pathtodivpts, "rb") as f:
    div_pts = pickle.load(f)
#=============================================================================#
#-----------a simple example with an order count of 6 since dist = [0, 2, 2, 2]
#a = [[1, 2, 3]]
#div_pts[scomb[0]] = {0: str(ranktobin([1, 2, 3], a[0])),
#                      8: str(ranktobin([1, 2, 3], a[0])),
#                      11: str(ranktobin([2, 3, 1], a[0])),
#                      15: str(ranktobin([2, 3, 1], a[0])),
#                      30: str(ranktobin([3, 1, 2], a[0])),
#                      40: str(ranktobin([3, 1, 2], a[0])),
#                      }
keydict = {"obr": 0, "d": 1, "ak": 2, "dd": 3}
#=============================================================================#
#-----------RESULTS
#=============================================================================#
#-----------path to test results file
pathtoresults = {4:s + order + "p3div__threshold" + 4 + "__test_results.pkl",
                 6:s + order + "3div__threshold" + 6 + "__test_results.pkl",}
#-----------------------------------------------------------------------------#
#-----------KEY STEP: uncomment on first run to generate the test results
genresults(div_pts, scomb, num_days, threshold, pathtoresults)
#-----------------------------------------------------------------------------#
#-----------load the results dict
resdict = {}
for threshold in [4, 6]:
    with open (pathtoresults[threshold], "rb") as f:
        resdict[threshold] = pickle.load(f)
#=============================================================================#
#-----------print results
stop
ak = resdict[4]["divpersubset"]
dd = resdict["datefin"]
xceptn = np.asarray(resdict["xceptn"])

print(xceptn)
xceptnls = [xceptn[i][j] for i in range(len(xceptn)) for j in range(sub)]
xceptncount = {i : Counter(xceptnls)[i] for i in range(1, mat + 1)}
print(xceptncount)
xceptnmat = list(set(xceptnls))
print(dd)
maxdd = np.max(dd)
print("dd[0] is", dd[0])
freq = resdict["freqperday"]
cumfreq = resdict["cumfreqperday"]

print(resdict["testdctlsls"][scomb[0]])
print("current minimum over allcounts is ", np.min(ak), "at", np.argmin(ak), "\n")
print("the minimum occurs for the subset ", a[np.argmin(ak)])
print("Number of subsets that satisfy p3div but not 3div is", Counter(ak)[4])
print("The maturity dates that generate exceptions:", xceptnmat, "the number of\
      them:", len(xceptnmat))
print("Number of subsets that satisfy 3div is", Counter(ak)[6])
print("The maturity dates that do not generate exceptions:",
      list(set(range(1, 31)) - set(xceptnmat)),
           "the number of them:", 30 - len(xceptnmat))
print("Number of subsets is", len(a))
print(resdict.keys())
print(np.max(freq), np.argmax(freq))
print("current max over all times is", maxdd, "\n")
print("Proportion of dates that condition", threshold, "holds is ",
      1 - maxdd/len(rankings))
print("rankings row 0 is ", rankings.iloc[0, :])
print("sveny row 0 is ", sveny.iloc[0,:])
print("rankings row where diversity is", threshold, "is ", rankings.iloc[maxdd,:])
print("sveny row where diversity is ", threshold, " is ", sveny.iloc[maxdd,:])
convar = {"maturity" : mat, "threshold" : threshold, "order" : order}
print(convar)

plt.xlim = (0, num_days); plt.ylim = (0, 1.2)
plt.yticks(np.arange(0, 1, 0.2))
plt.plot(np.arange(num_days), cumfreq / len(a))
plt.show()

#-----------EOF
#=============================================================================#
