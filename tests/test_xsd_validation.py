import os
import glob
import pytest
from lxml import etree

# Define base directory and paths
BASE_DIR = os.path.dirname(__file__)
SCHEMA_PATH = os.path.join(BASE_DIR, "..", "schemas", "payslipxml-2-0.xsd")
VALID_DIR = os.path.join(BASE_DIR, "data", "valid")
INVALID_DIR = os.path.join(BASE_DIR, "data", "invalid")


@pytest.fixture(scope="session")
def payslip_schema():
    """Load and parse the Payslip XML 2.0 schema once per session."""
    with open(SCHEMA_PATH, "rb") as f:
        schema_doc = etree.parse(f)
    return etree.XMLSchema(schema_doc)


def validate_xml(xml_path, schema):
    """Validate an XML file against the schema and return result and errors."""
    try:
        xml_doc = etree.parse(xml_path)
        schema.assertValid(xml_doc)
        return True, []
    except etree.DocumentInvalid as e:
        # Retrieve the error log for detailed errors
        return False, list(schema.error_log)
    except Exception as e:
        return False, [str(e)]


def test_valid_payslip_passes(payslip_schema):
    """Test that a valid payslip XML passes validation."""
    valid_file = os.path.join(VALID_DIR, "valid_payslip.xml")
    is_valid, errors = validate_xml(valid_file, payslip_schema)
    assert is_valid, f"Expected valid XML to pass but got errors: {errors}"


@pytest.mark.parametrize("xml_file", glob.glob(os.path.join(INVALID_DIR, "*.xml")))
def test_invalid_payslips_fail(payslip_schema, xml_file):
    """Test that invalid XML files fail validation."""
    is_valid, errors = validate_xml(xml_file, payslip_schema)
    assert not is_valid, f"{os.path.basename(xml_file)} unexpectedly passed validation!"
    assert len(errors) > 0, f"{os.path.basename(xml_file)} failed but no errors were captured."
    # Optional: Print errors for debugging
    # print(f"Errors in {os.path.basename(xml_file)}:", errors)
    for err in errors:
        # Ensure errors are identifiable
        assert hasattr(err, "line") or hasattr(err, "message"), "Expected identifiable error path/message"