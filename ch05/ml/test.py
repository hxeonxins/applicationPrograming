import joblib

from ch05.ml.train_classifier import pipeline

from transformers import pipeline

# vectorizer = joblib.load("vectorizer.joblib")
# model = joblib.load("todo_classifier.joblib")

classifier = pipeline("zero-short-classification",
                      model= "typeform/distilbert-base-uncased-mnli")
CATEGORY = ['공부', '운동', '업무', '개인', '쇼핑']

if __name__ == '__main__':
    result = classifier('시험 공부하기', CATEGORY)
    top_label = result['labels'][0]

    # x = vectorizer.transform(['자바 공부하기'])
    # category = model.predict(x)[0]
    # print(category)

# -> 서비스 계층에서 사용 가능!