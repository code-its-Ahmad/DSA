# Find if two rectangles overlap

def rectanglesOverlap(re1,re2):
    if re1[0] > re2[2] or re2[0] > re1[2]:
        return False
    if re1[1] > re2[3] or re2[1] > re1[3]:
        return False
    return True
print(rectanglesOverlap([0,0,2,2],[1,1,3,3]))