import joblib

vectorizer = joblib.load("vectorizer.joblib")
model = joblib.load("todo_classifier.joblib")

if __name__ == '__main__':
    x = vectorizer.transform(['자바 공부하기'])
    category = model.predict(x)[0]
    print(category)