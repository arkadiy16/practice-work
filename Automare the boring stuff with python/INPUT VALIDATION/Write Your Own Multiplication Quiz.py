import time, random
import pyinputplus as pyip


# This is practice work from Automate the boring stuf with python
# Input validation
# Write Your Own Multiplication Quiz
# Main task is to write a quiz program that similar to multiplication table.
# The program should use PyInputPlus functions 



def main():
    score  = 0
    for _ in range(10):
        num_1 = random.randint(0, 9)
        num_2 = random.randint(0, 9)
        try:
            pyip.inputInt(f'{num_1} * {num_2}\n',
                          allowRegexes=[f'{num_1*num_2}'],
                          blockRegexes=[r'.*'],
                          timeout=8, limit=3)                          
        except pyip.TimeoutException:
            print('Time has passed.')
        except pyip.RetryLimitException:
            print('No more tries.')
        else:
            print('Correct')
            score += 1
        time.sleep(1)
    print(f'You have {score} correct answers from 10 possible')
            
                            
main()
