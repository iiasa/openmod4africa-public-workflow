"""Regression tests for workflow handling of optional IAMC dimensions."""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

import workflow


class TestOptionalSubannualDimension(unittest.TestCase):
    def setUp(self):
        self.dsd = SimpleNamespace(dimensions=["region", "variable", "subannual"])
        self.processor = object()
        self.data = SimpleNamespace(dimensions=["region", "variable"])

    def run_workflow_with_dimensions(self, dimensions):
        self.data.dimensions = dimensions
        expected = object()
        with (
            patch("workflow.DataStructureDefinition", return_value=self.dsd),
            patch("workflow.RegionProcessor.from_directory", return_value=self.processor),
            patch("workflow.process", return_value=expected) as process,
        ):
            result = workflow.main(self.data)

        self.assertIs(result, expected)
        return process

    def test_annual_input_without_subannual_skips_only_that_dimension(self):
        process = self.run_workflow_with_dimensions(["region", "variable"])

        self.assertEqual(
            process.call_args.kwargs["dimensions"], ["region", "variable"]
        )

    def test_input_with_subannual_validates_that_dimension(self):
        process = self.run_workflow_with_dimensions(
            ["region", "variable", "subannual"]
        )

        self.assertEqual(
            process.call_args.kwargs["dimensions"],
            ["region", "variable", "subannual"],
        )


if __name__ == "__main__":
    unittest.main()
