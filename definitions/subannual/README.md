# Subannual definitions

These YAML files are copied from the openENTRANCE nomenclature:
https://github.com/openENTRANCE/openentrance/tree/fa5f53aa7d6acc14d6ca2059b5c775d5fb47ec93/definitions/subannual

Local definitions are required because nomenclature-iamc 0.32.0 does not
support `definitions.subannual.repository`. Removing these files and using
that configuration causes `ValueError: Empty codelist: subannual`.

These are standard openENTRANCE labels, not Plan4RES-specific definitions.
Replace the local copies with an external import once a released version of
nomenclature supports it, and validate the project and Plan4RES datasets again.
