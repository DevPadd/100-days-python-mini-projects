# OLD VERSION

# questions = ("母 ","祖母 ","兄 ","姉 ", "父 ", "祖父 ", "銀行","高校","結構","結論","太陽", "専門学校","改善","音楽","了解")

# answers = ("haha","sobo","ani","ane","chichi", "sofu", "ginkou", "koukou", "kekkou", "ketsuron", "taiyou", "senmongakkou","kaizen", "ongaku", "ryoukai")

# guesses = []
# score = 0 
# print("welcome to kotoba quiz games!")
# for question in questions:
#     question_index = questions.index(question)

#     print(question)
#     answer = input("input your answer: ").lower()

#     if answer == answers[question_index]:
#         print("correct!")
#         score +=1
#     else:
#         print(f"wrong! correct answer is {answers[question_index]}")
#     print("-------------------------")

# print("quiz is done!")
# print(f"score: {score}/{question_index+1}")



# SHUFFLED VERSION
import random

qa_pairs = list(zip(
    ("母 ","祖母 ","兄 ","姉 ", "父 ", "祖父 ", "銀行","高校","結構","結論","太陽", "専門学校","改善","音楽","了解"),
    ("haha","sobo","ani","ane","chichi", "sofu", "ginkou", "koukou", "kekkou", "ketsuron", "taiyou", "senmongakkou","kaizen", "ongaku", "ryoukai")
))
random.shuffle(qa_pairs)
score = 0
print("welcome to kotoba quiz games!")

for question, correct_answer in qa_pairs:
    print(question)
    answer = input("input your answer: ")

    if answer == correct_answer:
        print("correct!")
        score += 1
    else:
        print(f"wrong! correct answer is {correct_answer}")

    print("-------------------------")

print("quiz is done!")
print(f"score: {score}/{len(qa_pairs)}")