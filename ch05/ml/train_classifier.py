import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

df = pd.read_csv('todo_data.csv')
texts = df['content']
labels = df['category']

x_train, x_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

pipeline.fit(x_train, y_train)

#결과 평가
y_pred = pipeline.predict(x_test)
print(classification_report(y_test, y_pred))

joblib.dump(pipeline.named_steps['tfidf'], "vectorizer.joblib")
joblib.dump(pipeline.named_steps['clf'], "todo_classifier.joblib")
