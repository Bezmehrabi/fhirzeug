import typing
import inspect
import decimal
import base64


import pytest
import pydantic


from fhirzeug.generators.python_pydantic.templates.fhir_basic_types import (
    FHIRDate,
    FHIRDateTime,
    FHIRTime,
    FHIRInstant,
    FHIRBase64Binary,
    FHIRId,
    FHIROid,
)


class ExampleModel(pydantic.BaseModel):
    """A Test class to check all basic datatypes."""

    date: typing.Optional[FHIRDate]
    datetime: typing.Optional[FHIRDateTime]
    time: typing.Optional[FHIRTime]
    instant: typing.Optional[FHIRInstant]
    base64: typing.Optional[FHIRBase64Binary]
    oid: typing.Optional[FHIROid]
    fhir_id: typing.Optional[FHIRId]
    decimal: typing.Optional[decimal.Decimal]


def test_fhirdate():
    """Test FHIRDate
    https://www.hl7.org/fhir/datatypes.html#date"""
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(date="foo")
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(date="24:00")
    model = ExampleModel(date="1905-08-23")


def test_fhirdatetime():
    """Test FHIRDateTime
    https://www.hl7.org/fhir/datatypes.html#dateTime"""
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(datetime="foo")
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(datetime="24:00")
    model = ExampleModel(datetime="1905-08-23")


def test_fhirtime():
    """Test FHIRTime
    https://www.hl7.org/fhir/datatypes.html#time"""
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(time="foo")
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(time="24:00")
    model = ExampleModel(time="17:00:00")


def test_fhirinstant():
    """Test FHIRInstant
    https://www.hl7.org/fhir/datatypes.html#instant"""
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(instant="foo")
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(instant="24:00")
    model = ExampleModel(instant="2017-01-01T00:00:00Z")
    model = ExampleModel(instant="2015-02-07T13:28:17.239+02:00")


def test_fhirbase64binary():
    """Test FHIRBase64Binary
    https://www.hl7.org/fhir/datatypes.html#base64binary"""
    message = "Foo Bar"
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")
    model = ExampleModel(base64=base64_message)

    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(base64=message)


def test_fhiroid():
    """Test FHIROid
    https://www.hl7.org/fhir/datatypes.html#oid"""

    model = ExampleModel(oid="urn:oid:1.2.3.4.5")
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(oid="foo")


def test_fhirid():
    """Test FHIRId
    https://www.hl7.org/fhir/datatypes.html#id"""

    model = ExampleModel(fhir_id="foo.bar")
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(fhir_id="?")


def test_decimal():
    """Test FHIRDecimal
    https://www.hl7.org/fhir/datatypes.html#decimal"""
    with pytest.raises(pydantic.ValidationError):
        model = ExampleModel(decimal="FOO")

    model = ExampleModel(decimal=3.14000000000000012434497875801)
