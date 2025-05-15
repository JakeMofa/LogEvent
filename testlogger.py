# Import unittest for Python unit testing framework
# Import time to simulate time intervals in LogEvent
from logevent2 import LogEvent, Stack
import unittest
import time

# Define a test case class inheriting from unittest.TestCase
class TestLoggerFunctions(unittest.TestCase):
    """
    Unit tests for the LogEvent() and Stack() functions.
    These tests ensure structure, formatting, and correct behavior under typical use cases.
    """

    def test_log_event_structure(self):
        """
        Test that LogEvent returns a properly structured log entry.
        Validates format, length, and content of the returned list.
        """
        event = "Test Event"
        start_time = time.time()
        
        # Call the function and receive the log entry and new start time
        log_entry, new_time = LogEvent(event, start_time)

        # Ensure the returned list has 4 items
        self.assertEqual(len(log_entry), 4, "Log entry should have 4 fields")

        # First item should match the input event message
        self.assertEqual(log_entry[0], event, "First field should be the event string")

        # Second item should be a string-formatted elapsed time
        self.assertTrue(isinstance(log_entry[1], str), "Elapsed time should be a formatted string")

        # Third item should be a valid timestamp in the expected format
        self.assertRegex(log_entry[2], r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', "Timestamp should be in correct format")

        # Fourth item should contain the name of this test method as part of the call stack
        self.assertTrue("test_log_event_structure" in log_entry[3], "Stack should include the calling function")

    def test_stack_function(self):
        """
        Test that Stack() returns a valid call trace string.
        Ensures it's not empty and includes a known callable layer.
        """
        trace = Stack()

        # Ensure it's a non-empty string
        self.assertIsInstance(trace, str, "Stack trace should be a string")
        self.assertGreater(len(trace), 0, "Stack trace should not be empty")

        
        print("Captured Stack Trace:", trace)

        # Confirm at least one recognizable call structure exists
        self.assertTrue(any("call" in f or "run" in f for f in trace.split("/")), "Stack should contain callable frames")


if __name__ == '__main__':
    unittest.main()
