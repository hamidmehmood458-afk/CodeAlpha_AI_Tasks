from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=== FAQ Chatbot ===")

questions = [
    "What is AI?",
    "What is machine learning?",
    "What is Python?"
]

answers = [
    "AI is artificial intelligence.",
    "Machine learning is a subset of AI.",
    "Python is a programming language."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

while True:
    query = input("You: ")
    
    if query.lower() == "exit":
        print("Chatbot ended.")
        break

    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X)
    index = similarity.argmax()

    print("Bot:", answers[index])
