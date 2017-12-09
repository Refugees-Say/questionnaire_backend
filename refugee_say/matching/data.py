'''
Created on Nov 12, 2017

@author: avisn
'''

class Data():
    pass

familydata = Data()
regiondata = Data()

familydata.names = ['avrohom', 'bob', 'col', 'dov', 'ed', 'fred','gavriel','hal','ian', 'jon']
regiondata.names = ['austin','buffalo','chicago','detroit','el paso','fort worth','greensboro']

familydata.sizes = {
 0:  1,
 1:  1,
 2:  1,
 3:  1,
 4:  1,
 5:  1,
 6:  1,
 7:  1,
 8:  1,
 9:  1
 }
 
regiondata.sizes = {
 0:  1,
 1:  1,
 2:  1,
 3:  2,
 4:  2,
 5:  2,
 6:  1
 }

familydata.prefers = {
 0:  [[0, 4, 2, 3, 5, 1, 6],[]],
 1:  [[2, 0, 3, 4, 5, 1, 6],[]],
 2:  [[4, 0, 3, 1, 5, 6, 2],[]],
 3:  [[5, 3, 6, 4, 1, 2, 0],[]],
 4:  [[3, 1, 2, 5, 4, 0, 6],[]],
 5:  [[1, 0, 3, 6, 4, 2, 5],[]],
 6:  [[6, 4, 1, 2, 0, 3, 5],[]],
 7:  [[0, 4, 5, 2, 1, 6, 3],[]],
 8:  [[2, 3, 6, 1, 0, 5, 4],[]],
 9:  [[0, 5, 6, 4, 1, 3, 2],[]],
}
regiondata.prefers = {
 0:  [[1, 5, 9, 6, 8, 0, 3, 4, 2, 7],[]],
 1:  [[1, 0, 2, 5, 6, 3, 8, 4, 9, 7],[]],
 2:  [[5, 1, 4, 6, 7, 2, 8, 0, 3, 9],[]],
 3:  [[5, 9, 2, 0, 8, 7, 6, 3, 1, 4],[]],
 4:  [[9, 7, 5, 3, 0, 6, 2, 4, 8, 1],[]],
 5:  [[1, 0, 4, 8, 9, 3, 5, 6, 2, 7],[]],
 6:  [[9, 6, 7, 5, 1, 0, 2, 4, 3, 8],[]],
}

def __fillPrefers(prefersDict):
    for prefs in prefersDict.values():
        pref = prefs[0]
        invPref = [None] * len(prefs[0])
        for i in range(len(pref)):
            invPref[pref[i]] = i
        prefs[1] = invPref
        

__fillPrefers(familydata.prefers)
__fillPrefers(regiondata.prefers)

