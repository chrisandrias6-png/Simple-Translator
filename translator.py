import numpy as np

# English words
x = np.array([
    "Hi",
    "Hello",
    "What is your name?",
    "cat",
    "dog",
    "translator",
    "AI",
    "Program",
    "USA",
    "New York",
    "home",
    "girl",
    "boy"
])

# Arabic translations
y = np.array([
    "مرحبا",
    "مرحبا",
    "ما اسمك؟",
    "قطة",
    "كلب",
    "مترجم",
    "ذكاء اصطناعي",
    "برنامج",
    "الولايات المتحدة الأمريكية",
    "نيويورك",
    "منزل",
    "فتاة",
    "ولد"
])


def translate(word):
    for i in range(len(x)):
        if x[i].lower() == word.lower():
            return y[i]

    return "Translation not found"


word = input("Enter an English word: ")

result = translate(word)

print("Translation:", result)
