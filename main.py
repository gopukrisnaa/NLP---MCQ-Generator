import openai
from PyPDF2 import PdfReader

# Set the OpenAI API key
openai.api_key =  "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"

def generate_questions(chapter_content):
    # Define the prompt for question generation
    prompt = "Generate questions with multiple correct answers based on the following chapter:\n{}\n---\nQuestion:".format(chapter_content[:4000])

    # Generate questions using ChatGPT 3.5
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=5,  # Generate 5 questions
        stop=None,
        temperature=0.7
    )

    # Extract the generated questions from the API response
    questions = [choice["text"] for choice in response.choices]

    # Print the generated questions
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question}")
        print("Possible correct answers:")

        # Replace the answer placeholders with multiple correct answers
        question_with_answers = question.replace("___", "option 1, option 2, option 3")
        print(question_with_answers)
        print()

# Extract text from the PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

    return text

# Provide the path to the PDF file
pdf_path = "chapter-4.pdf"

# Extract text from the PDF
chapter_content = extract_text_from_pdf(pdf_path)

# Generate questions based on the extracted text
generate_questions(chapter_content)

