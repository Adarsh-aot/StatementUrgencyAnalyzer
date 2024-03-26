import unittest
import time
from classes import StatementUrgencyAnalyzer

class TestStatementUrgencyAnalyzer(unittest.TestCase):

    def test_determine_statement_urgency(self):
        # Initialize the StatementUrgencyAnalyzer instance
        analyzer = StatementUrgencyAnalyzer()

        # Test input statements
        input_statement_1 = 'Dear Dr Hasan Dynacare has a pending request for information for your patient Philip Moy. Our request was sent to your office on 2023/03/29 and now is urgently required.'
        input_statement_2 = 'Dear Dr Hasan Dynacare has a pending request for information for your patient Philip Moy. Our request was sent to your office on 2023/03/29 and now is not urgently required.'

        # Expected outputs
        expected_output_1 = 'urgent'
        expected_output_2 = 'not urgent'

        # Determine urgency for input statement 1
        urgency_1 = analyzer.determine_statement_urgency(input_statement_1)

        # Check if urgency matches expected output
        self.assertEqual(urgency_1[0], expected_output_1, "Urgency determination failed for statement 1")
        print("\n\nText 1 passed\n\n")

        # Determine urgency for input statement 2
        urgency_2 = analyzer.determine_statement_urgency(input_statement_2)

        # Check if urgency matches expected output
        self.assertEqual(urgency_2[0], expected_output_2, "Urgency determination failed for statement 2")
        print("\n\nText 2 passed\n\n")

if __name__ == '__main__':
    # Run the test case
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStatementUrgencyAnalyzer)
    start_time = time.time()
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")