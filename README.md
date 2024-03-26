# Statement Urgency Analyzer

Statement Urgency Analyzer is a Python package for analyzing the urgency of statements. It provides functionality to determine whether a given statement is urgent or not based on a pre-trained model.

## Installation

To install Statement Urgency Analyzer and its dependencies, you can use pip. Run the following command:



transformers: A library for state-of-the-art natural language processing.
torch: PyTorch is an open source deep learning platform that provides a seamless path from research prototyping to production deployment.
numpy: NumPy is the fundamental package for scientific computing with Python.


```bash
pip install transformers torch numpy
```
Usage
Here's how you can use Statement Urgency Analyzer in your Python code:

```python
from classes import StatementUrgencyAnalyzer

result = StatementUrgencyAnalyzer()
print(result.determine_statement_urgency('Dear  Dr Hasan  Dynacare has a pending request for information for your patinet Philip Moy Our request was sent to your office on 2023/03/29 and now is urgently required.'))
```
