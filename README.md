# OpenMod4Africa public workflow

Copyright 2026 IIASA

[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


## Overview


> [!TIP]
> For *users not comfortable working with GitHub repositories and yaml files*,
> the definitions for this project are available for download as an xlsx spreadsheet
> at [https://files.ece.iiasa.ac.at/openmod4africa-public/openmod4africa-public-template.xlsx](https://files.ece.iiasa.ac.at/openmod4africa-public/openmod4africa-public-template.xlsx).


### Project nomenclature

The folder `definitions` can contain the project nomenclature, i.e., list of allowed
variables and regions, for use in the validation workflow. See the **nomenclature**
package for more information ([link](https://github.com/iamconsortium/nomenclature)).

The folder `mappings` can contain model mappings that are used to register models and
define how results should be processed upon upload to a Scenario Explorer.

### Model registration

This is the step-by-step guide to registering your model:

1. Fork this repository
2. Follow the instructions from the nomenclature documentation here: <https://nomenclature-iamc.readthedocs.io/en/stable/user_guide/model-registration.html>. 
Please make sure to follow the instructions completely, both the _Model mapping_ and the _Region definitions_ part. You'll have to end up with two files.
3. Open a pull request into this repository. Make sure that the tests run through and correct any potential issues. If the tests are failing you can view the details by clicking on the failed test run.

4. Set [@danielhuppmann](https://github.com/danielhuppmann) and [@phackstock](https://github.com/phackstock) as reviewers.
5. Once everything is in order we will merge your pull request and your model will be registered.

### Plan4RES v2.0 registration

This fork registers IAMC results produced by **Plan4RES v2.0** for the Senegal
case study. The contribution adds the seven model zones (`Dakar`, `Thies`,
`Diourbel`, `LS`, `FKK`, `MTKK` and `ZS`) below the `Senegal` hierarchy and
allows directed electricity connections between every pair of zones.

Plan4RES exports these regions directly in canonical form, for example
`Senegal|Dakar` and `Senegal|Dakar>Thies`. The spelling `Thies` is used
consistently without an accent. The model registration is defined in
`mappings/plan4res_v2.0.yaml`; the corresponding common-region definitions
are in `definitions/region/senegal_subregions.yaml`.

The submitted Plan4RES dataset uses only variable-unit combinations and
subannual labels already defined by openENTRANCE. This registration therefore
does not introduce Plan4RES-specific variable definitions. The local
GENeSYS-MOD extension files are a separate development concern and are not
required for the Plan4RES registration.

Annual and hourly datetime files can omit the `Subannual` column. When the
column is present, its labels are validated against the openENTRANCE definitions
in `definitions/subannual`. These local copies are required by
`nomenclature-iamc` 0.32.0, which does not support importing that dimension via
`definitions.subannual.repository`.

### Workflow

The module `workflow.py` has a function `main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:`.

Per default, this function takes an **IamDataFrame** and returns it without
modifications. [Read the docs](https://pyam-iamc.readthedocs.io) for more information
about the **pyam** package for scenario analysis and data visualization.

**Important**: Do not change the name of the module `workflow.py` or the function `main`
as they are called like this by the Job Execution Service. Details can be found
[here](https://wiki.ece.iiasa.ac.at/wiki/index.php/Scenario_Explorer/Setup#Job_Execution_Service).
