from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import numpy as np

class StatementUrgencyAnalyzer:
    """
    A class used to analyze the urgency of statements.

    Attributes:
        qa_model (AutoModelForQuestionAnswering): Pre-trained question answering model.
        qa_tokenizer (AutoTokenizer): Tokenizer for the question answering model.
        nlp (pipeline): Pipeline for question answering using the QA model.
        classify_tokenizer (AutoTokenizer): Tokenizer for the urgency classification model.
        classify_model (AutoModelForSequenceClassification): Pre-trained model for urgency classification.
    """

    def __init__(self):
        """
        Initializes the StatementUrgencyAnalyzer class with pre-trained models and tokenizers.
        """
        self.qa_model = AutoModelForQuestionAnswering.from_pretrained('deepset/roberta-base-squad2')
        self.qa_tokenizer = AutoTokenizer.from_pretrained('deepset/roberta-base-squad2')
        self.nlp = pipeline('question-answering', model=self.qa_model, tokenizer=self.qa_tokenizer)
        self.classify_tokenizer = AutoTokenizer.from_pretrained("quipohealth/bert_fine_tunned_10")
        self.classify_model = AutoModelForSequenceClassification.from_pretrained("quipohealth/bert_fine_tunned_10")

    def determine_urgency(self, text):
        """
        Determines the urgency of a given text.

        Parameters:
            text (str): The input text to determine urgency.

        Returns:
            str: 'urgent' if the text is classified as urgent, 'not urgent' otherwise.
        """
        np.set_printoptions(suppress=True)
        inputs = self.classify_tokenizer(text, padding=True, truncation=True, return_tensors='pt')
        outputs = self.classify_model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predictions = predictions.cpu().detach().numpy()
        if predictions[0][1] > predictions[0][0]:
            return 'not urgent'
        else:
            return 'urgent'

    def determine_statement_urgency(self, qa):
        """
        Determines the urgency of a statement based on a question answering result.

        Parameters:
            qa (str): The statement to analyze using question answering.

        Returns:
            str: 'urgent' if the statement is classified as urgent, 'not urgent' otherwise.
        """
        QA_input = {
            'question': 'is it urgent',
            'context': qa
        }
        res = self.nlp(QA_input)
        text = res['answer']
        result = self.determine_urgency(text)
        return result

# result = StatementUrgencyAnalyzer()
# print(result.determine_statement_urgency('Dear  Dr Hasan Dynacare has a pending request for information for your patinet Philip Moy Our request was sent to your office on 2023/03/29 and now is urgently required.'))