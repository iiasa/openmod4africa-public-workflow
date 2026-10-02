from pathlib import Path

import pyam
from nomenclature import DataStructureDefinition, RegionProcessor, process

here = Path(__file__).absolute().parent


def _dimensions_to_validate(df: pyam.IamDataFrame, dsd: DataStructureDefinition) -> list[str]:
    """Skip optional subannual validation when the input has no such column."""
    return [
        dimension for dimension in dsd.dimensions
        if dimension != "subannual" or "subannual" in df.dimensions
    ]


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Run the validation and region-processing
    dsd = DataStructureDefinition(here / "definitions")
    processor = RegionProcessor.from_directory(path=here / "mappings", dsd=dsd)
    # Annual and datetime exports need no subannual column. Validate its labels
    # when present, while retaining time-domain validation for every export.
    dimensions = _dimensions_to_validate(df, dsd)
    return process(df, dsd, dimensions=dimensions, processor=processor)
