    if util.check_lost (grid):
        print ("Game Over!")
        return
    
    elif util.check_won (grid) and not won_message:
        print ("Won!")
        won_message = True
        
    if not util.grid_equal (saved_grid, grid):
        add_block (grid)
        
random.seed (12) #random number generator will initialize to a fixd sequence

play () 