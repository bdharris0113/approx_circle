'''
given a circle connected by random lines; attempts to create circle out of lines
'''



import time,random,math,copy,pygame

pygame.init()
myfont = pygame.font.SysFont("COURIER NEW", 20)


W, H = 420, 420
SIZE = (W, H)
surface = pygame.display.set_mode(SIZE)


def dist(a,b):
    '''
    return distnace from point a -> b
    '''
    
    x = abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2
    return math.sqrt(x)
    
def tot_dist(state):
    '''
    return total distance from state
    '''
    
    total = 0
    total += dist(state[0],state[-1])
    temp = copy.deepcopy(state)
    while len(temp)-1 > 0:
        a = temp.pop(0)
        total = total + dist(a,temp[0])
        
   
    return total
    
    
def swap(state):
    '''
    randomly swap points in state 
    '''
    temp = copy.deepcopy(state)
    i = random.randrange(0,len(temp))
    j = random.randrange(0,len(temp))
    temp2 = temp[i]
    temp[i] = temp[j]
    temp[j] = temp2
    return temp



def uphill(total,state,terminate):
    '''
    swaps two points within state & checks if it has imporved total distance
    '''

    terminate -= 1
    new_state = swap(state)
    new_dist = tot_dist(new_state)

    if new_dist < total: #best_dist:
        return new_dist,new_state,1000
    
    return total, state,terminate
    
def main():
    state = []
    t = 0.0
    while t < 2*math.pi:
        state.append((int(9*math.cos(t)) + random.randrange(0,2), int(9*math.sin(t)) + random.randrange(0,2)))
        t += 0.01
        
    random.shuffle(state)    #original swap t
    print tot_dist(state)
        
    total = 10000
    total,state,terminate = uphill(total,state,1000)
    
    draw(state,total,terminate)
   

def draw(state,total,terminate):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        surface.fill((0,0,0))
        
        newl = []
        for x, y in state:
            newl.append((x * 20 + W/2,
                            -y * 20 + H/2))
        
        # axes
        
        pygame.draw.lines(surface, \
                          (0,0,255), \
                          False,        
                          newl,         
                          1)
                          
        if terminate <= 0:
            print total
            sys.exit()
        total,state,terminate = uphill(total,state,terminate)

         # apply it to text on a label
        label = myfont.render(str(total), 1, (0,255,0))
        #label2 = myfont.render(str(terminate), 1, (0,255,0))

        # put the label object on the screen at point x=100, y=100
        surface.blit(label, (10, 10))
        #surface.blit(label2,(10,40))
            
        pygame.display.flip()
        pygame.display.update()                         #updates screen


main()

