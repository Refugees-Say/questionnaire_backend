'''
Created on Apr 21, 2017

@author: avisn

next steps:
- test on bigger data
- verify that random switching makes it fail
- import csv data file

'''


import copy
from sortedcontainers import SortedDict
from data import *

print('start')

class Region:
    count = 0
    def __init__(self, name, space):
        self.name = name
        self.space = space
        self.initialSpace = space
        self.families = SortedDict()
    
        self.id = Region.count
        Region.count += 1
    
    def __str__(self):
        return str(self.id) + ' ' + self.name

    def __hash__(self):
        return self.id
    
    def contains(self, family):
        key = self.prefersKey[family.id]
        if key in self.families:
            value = self.families[key]
            if isinstance(value, Family):
                if value == family:
                    return True
            elif family in value:
                return True
        return False
    
    def tryAdd(self, family, famsLeft):
        key = self.prefersKey[family.id]
        if self.space >= family.size:
            # enough space
            self.__add(key, family)
            print('%s(%s -> %s) added %s(%s)' % (self.name, self.space + family.size, self.space, family.name, family.size))
            return True
        # try to replace others
        potentialSpace = self.space
        keys2del = set();
        for k in reversed(self.families):
            if key >= k:
                # priority too low :( 
                return False
            keys2del.add(k)
            potentialSpace += getSize(self.families[k])
            if potentialSpace >= family.size:
                # priority high enough :) 
                break
        if potentialSpace >= family.size:
            j = float('inf')
            while j > k:
                j, fam2remove = self.families.popitem(True)
                fam2remove.region = None
                self.space += fam2remove.size
                famsLeft.append(fam2remove)
                print('%s(%s -> %s) displaced  %s(%s)'  % (self.name, self.space - fam2remove.size, self.space, fam2remove.name, fam2remove.size))
            self.__add(key, family)
            print('%s(%s -> %s) added %s(%s)' % (self.name, self.space + family.size, self.space, family.name, family.size))
            return True
        else:
            # bizarre case of family too big for the whole region
            print("%s (%s) is too big for %s (%s)" % (family.name, family.size, self.name, self.initialSpace))
            return False
        
    def __add(self, key, family):
        family.region = self
        if key in self.families:
            value = self.families[key]
            if isinstance(value, Family):
            # value is a family; transform to set                
                self.families[key] = {value, family}
            else:
            # value is a set of families
                value.add(family)
        else:
            self.families[key] = family
        self.space -= family.size

def getSize(familyElement):
    if isinstance(familyElement, Family):
        return familyElement.size
    else:
        size = 0
        for family in familyElement:
            size += family.size
        return size
    
      
class Family:
    count = 0
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.id = Family.count
        self.region = None
        self.idx = 0
        Family.count += 1
        
    def __str__(self):
        return str(self.id) + ' ' + self.name
    
    def __hash__(self):
        return self.id
    
    def nextRegion(self):
        output = self.prefers[self.idx]
        self.idx += 1
        return output
            
    def regionsEmpty(self):
        return self.idx == len(self.prefers);
    
    def compare(self, region0, region1 = None):
        if region1 is None:
            region1 = self.region
            if region1 is None:
                print('%s has no region' % (self.name))
        key0 = self.prefersKey[region0.id]
        key1 = self.prefersKey[region1.id]
        return key1 - key0

# initialize regions and families
regions = [Region(regiondata.names[k], v) for k,v in regiondata.sizes.items()]
families = [Family(familydata.names[k], v) for k,v in familydata.sizes.items()] 

# add comparison functions
for region in regions:
    region.prefersKey = copy.deepcopy(regiondata.prefers[region.id][1])
for family in families:
    family.prefers = copy.deepcopy(familydata.prefers[family.id][0])
    family.prefersKey = copy.deepcopy(familydata.prefers[family.id][1])

famsLeft = copy.copy(families)
i = 0
while famsLeft:
    print('Iteration = %s' % (i))
    i += 1
    for family in famsLeft:
        regId = family.nextRegion()
        if regions[regId].tryAdd(family, famsLeft):
            famsLeft.remove(family)    
        elif family.regionsEmpty():
            print('no room left for %s(%s)' % (family.name,family.size))
            famsLeft.remove(family)

for region in regions:
    print("%s(%s)" % (region.name, region.initialSpace))
    for family in region.families.values():
        print("\t%s(%s)" % (family.name, family.size))


def check(regions):
    for region in regions:
        for family in families:
            if region.contains(family):
                continue
            if family.compare(region) > 0:
                added = region.tryAdd(family, famsLeft)
                if added:
                    return False
    return True

print('Engagement stability check PASSED' if check(regions) else 'Engagement stability check FAILED')
