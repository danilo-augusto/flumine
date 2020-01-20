import unittest
from unittest import mock

from flumine.event import event


class BaseEventTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_event = mock.Mock()
        self.base_event = event.BaseEvent(self.mock_event)

    def test_init(self):
        mock_event = mock.Mock()
        base_event = event.BaseEvent(mock_event)
        self.assertIsNone(base_event.EVENT)
        self.assertIsNone(base_event.QUEUE)
        self.assertEqual(base_event.event, mock_event)

    def test_str(self):
        self.base_event.EVENT = event.Event.MARKET_BOOK
        self.base_event.QUEUE = event.Queue.HANDLER
        self.assertEqual(str(self.base_event), "<MARKET_BOOK [HANDLER]>")
