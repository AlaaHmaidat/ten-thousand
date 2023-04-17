import random
from collections import Counter


class GameLogic:

    def __init__(self):
        pass

    # def calculate_score(tuple_of_dice_roll):
        
    #     tuple_of_dice_roll_counter = Counter(tuple_of_dice_roll)
    #     print(tuple_of_dice_roll_counter)

    #     # checks if the tuple_of_dice_roll_counter dictionary is empty or not. If the dictionary is empty
    #     if len(tuple_of_dice_roll)==0:
    #         return 0
        
    #     num, repetition = list(tuple_of_dice_roll_counter.items())[0]
    #     print("num ", num, 'repetition ', repetition)


    #     # for i in range(6):
    #     #     count = 0

    #     #     print(i)

    #     #     if num == 1 and repetition == 1:
    #     #         return 100
    #     #     elif num == 1 and repetition == 2:
    #     #         return 200
    #     #     elif num == 1 and repetition == 3:
    #     #         print(i)
    #     #         return 1000
    #     #     elif num == 1 and repetition == 4:
    #     #         print(i)
    #     #         return 2000
    #     #     elif num == 1 and repetition == 5:
    #     #         print(i)
    #     #         return 3000
    #     #     elif num == 1 and repetition == 6:
    #     #         return 4000


    #     score = 0
    #     if num == 1:
    #         if repetition == 1:
    #             return 100
    #         elif repetition == 2:
    #             return 200
    #         if repetition >= 3:
    #             score += 1000 * (repetition - 3 + 1)
    #             return score
    #         if repetition == 6:
    #             score += 2000
    #             return score
            
    #     if num == 2:
    #         if repetition == 1:
    #             return 0
    #         elif repetition == 2:
    #             return 0
    #         if repetition >= 3:
    #             score += 200 * (repetition - 3 + 1)
    #             return score
    #         if repetition == 6:
    #             score += 200
    #             return score
    #     if num == 3:
    #         if repetition == 1:
    #             return 0
    #         elif repetition == 2:
    #             return 0
    #         if repetition >= 3:
    #             score += 300 * (repetition - 3 + 1)
    #             return score
    #         if repetition == 6:
    #             score += 300
    #             return score


    def calculate_score(tup):
        """
        this function recives a tuple and calculate the unbanked points for a roll of dice depands on the game rule  
        """

        unbancked_points = 0 
        num_counter = Counter(tup)
        if 1 == num_counter[5] or num_counter[5] == 2 :
                unbancked_points += 50 * num_counter[5]
        if 1 == num_counter[1] or num_counter[1] == 2:
                unbancked_points += 100 * num_counter[1]
        # 3 of a kind        
        if num_counter[1]== 3:
             unbancked_points+= 1000
        if num_counter[2] == 3:
             unbancked_points+= 200     
        if num_counter[3] == 3:
             unbancked_points+= 300     
        if num_counter[4] == 3:
             unbancked_points+= 400     
        if num_counter[5] == 3:
             unbancked_points+= 500       
        if num_counter[6] == 3:
             unbancked_points+= 600
        # 4 of a kind         
        if num_counter[1]== 4:
             unbancked_points+= 2000
        if num_counter[2] == 4:
             unbancked_points+= 400     
        if num_counter[3] == 4:
             unbancked_points+= 600     
        if num_counter[4] == 4:
             unbancked_points+= 800     
        if num_counter[5] == 4:
             unbancked_points+= 1000       
        if num_counter[6] == 4:
             unbancked_points+= 1200
        # 5 of a kind 
        if num_counter[1]== 5:
             unbancked_points+= 4000
        if num_counter[2] == 5:
             unbancked_points+= 800     
        if num_counter[3] == 5:
             unbancked_points+= 1200     
        if num_counter[4] == 5:
             unbancked_points+= 1600     
        if num_counter[5] == 5:
             unbancked_points+= 2000       
        if num_counter[6] == 5:
             unbancked_points+= 2400
        # 6 of a kind
        if num_counter[1]== 6:
             unbancked_points+= 8000
        if num_counter[2] == 6:
             unbancked_points+= 1600     
        if num_counter[3] == 6:
             unbancked_points+= 2400     
        if num_counter[4] == 6:
             unbancked_points+= 3200     
        if num_counter[5] == 6:
             unbancked_points+= 4000       
        if num_counter[6] == 6:
             unbancked_points+= 4800
        # 3 pairs      
        if len(num_counter) == 3 and len(set(num_counter.values())) == 1 and list(set(num_counter.values()))[0] == 2:
             unbancked_points += 1500

        if len(num_counter) == 2 and list(set(num_counter.values()))[0] == 3:
             unbancked_points = unbancked_points*2
                
        
        # stright 1-6    
        if len(num_counter) == 6:
             unbancked_points = 2000             
        return unbancked_points   

    def roll_dice(number_of_dice):
        list_of_num = []
        for i in range(number_of_dice):
            num = random.randint(1, 6)
            list_of_num.append(num)
        return list_of_num


if __name__ == '__main__':

    print(GameLogic.calculate_score((1,5)))
