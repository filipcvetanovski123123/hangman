import random
words=("apple","banana","coconut","pineapple")

hangman_art={
    0:("   ",
       "   ",
       "   "),
    1:(" 0 ",
       "   ",
       "   "),
    2:(" 0  ",
       "I ",
       "   "),
    3:(" O ",
       " I ",
       "   "),
    4:(" 0 ",
       "/I  ",
       "   "),
    5:(" 0 ",
       "/I\\",
       "   "),
    6:(" 0 ",
       "/I\\",
       "/ "),
    7:(" 0 ",
       "/I\\",
       "/\\",)
}
def display_man(wrong_quesses):
    for line in hangman_art[wrong_quesses]:
        print(line)
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_quesses=0
    quessed_letters= set()
    is_running=True
    while is_running:
        display_man(wrong_quesses)
        display_hint(hint)
        quess=input("Enter your guess: ").lower()
        if len(quess) !=1 or not quess.isalpha():
            print("invalid input")
            continue

        if quess in quessed_letters:
            print(" our quess is already quessed")
            continue

        quessed_letters.add(quess)

        if quess in answer:
            for i in range(len(answer)):
                if answer[i] == quess:
                    hint[i]=quess
        else:
            wrong_quesses += 1
        if "_" not in hint:
            display_man(wrong_quesses)
            display_answer(answer)
            print ("YOU WIN")
            is_running=False
        elif wrong_quesses >= len(hangman_art)-1:
            display_man(wrong_quesses)
            display_answer(answer)
            print ("YOU LOSE")
            is_running = False

if __name__=="__main__":
    main()