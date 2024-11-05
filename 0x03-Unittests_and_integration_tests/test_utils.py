#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
import unittest.mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        A method to test that access_nested_map returns
        what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            ) -> None:
        """
        A method test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case class for get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @unittest.mock.patch("requests.get")
    def test_get_json(
            self, mock_get,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """
        A method that tests `get_json`'s output.
        """
        mock_get.return_value = Mock(json=Mock(return_value=test_payload))
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
