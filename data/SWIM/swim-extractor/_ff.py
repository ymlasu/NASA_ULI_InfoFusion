# .\_ff.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1c9769bf0fbebc0c81a833c583b3ec2a9d9dbf8e
# Generated 2018-08-28 14:52:07.997211 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace http://www.fixm.aero/foundation/3.0 [xmlns:ff]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d7bde26c-aafb-11e8-9198-ecb1d75f2e16')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.fixm.aero/foundation/3.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TextAddressType
class TextAddressType (pyxb.binding.datatypes.string):

    """
            Basis for e-mail and street addresses. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextAddressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 227, 3)
    _Documentation = '\n            Basis for e-mail and street addresses. \n         '
TextAddressType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TextAddressType', TextAddressType)
_module_typeBindings.TextAddressType = TextAddressType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TextCityType
class TextCityType (pyxb.binding.datatypes.string):

    """
            Address city. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextCityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 236, 3)
    _Documentation = '\n            Address city. \n         '
TextCityType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TextCityType', TextCityType)
_module_typeBindings.TextCityType = TextCityType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TextCountryCodeType
class TextCountryCodeType (pyxb.binding.datatypes.string):

    """
            Used in PostalAddress. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextCountryCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 245, 3)
    _Documentation = '\n            Used in PostalAddress. \n         '
TextCountryCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
TextCountryCodeType._CF_pattern.addPattern(pattern='[A-Z]{2}')
TextCountryCodeType._InitializeFacetMap(TextCountryCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TextCountryCodeType', TextCountryCodeType)
_module_typeBindings.TextCountryCodeType = TextCountryCodeType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TextCountryNameType
class TextCountryNameType (pyxb.binding.datatypes.string):

    """
            The country of the physical address for the location or organisation.  Full name, 
            not ISO 3166 abbreviations. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextCountryNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 256, 3)
    _Documentation = '\n            The country of the physical address for the location or organisation.  Full name, \n            not ISO 3166 abbreviations. \n         '
TextCountryNameType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TextCountryNameType', TextCountryNameType)
_module_typeBindings.TextCountryNameType = TextCountryNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TextNameType
class TextNameType (pyxb.binding.datatypes.string):

    """
            Used for contact's title, name, and postal code. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 266, 3)
    _Documentation = "\n            Used for contact's title, name, and postal code. \n         "
TextNameType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TextNameType', TextNameType)
_module_typeBindings.TextNameType = TextNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TextPhoneType
class TextPhoneType (pyxb.binding.datatypes.string):

    """
            Used for phone and facsimile numbers. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextPhoneType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 275, 3)
    _Documentation = '\n            Used for phone and facsimile numbers. \n         '
TextPhoneType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TextPhoneType', TextPhoneType)
_module_typeBindings.TextPhoneType = TextPhoneType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AerodromeIcaoCodeType
class AerodromeIcaoCodeType (pyxb.binding.datatypes.string):

    """
            ICAO Airport Code 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AerodromeIcaoCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aerodrome.xsd', 76, 3)
    _Documentation = '\n            ICAO Airport Code \n         '
AerodromeIcaoCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
AerodromeIcaoCodeType._CF_pattern.addPattern(pattern='[A-Z]{4}')
AerodromeIcaoCodeType._InitializeFacetMap(AerodromeIcaoCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AerodromeIcaoCodeType', AerodromeIcaoCodeType)
_module_typeBindings.AerodromeIcaoCodeType = AerodromeIcaoCodeType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AerodromeNameType
class AerodromeNameType (pyxb.binding.datatypes.string):

    """
            Common airport name. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AerodromeNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aerodrome.xsd', 87, 3)
    _Documentation = '\n            Common airport name. \n         '
AerodromeNameType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AerodromeNameType', AerodromeNameType)
_module_typeBindings.AerodromeNameType = AerodromeNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}RunwayNameType
class RunwayNameType (pyxb.binding.datatypes.string):

    """
            * A number between 01 and 36 AND 
            * Optionally  Left (L), Center (C), or Right (R) 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunwayNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aerodrome.xsd', 96, 3)
    _Documentation = '\n            * A number between 01 and 36 AND \n            * Optionally  Left (L), Center (C), or Right (R) \n         '
RunwayNameType._CF_pattern = pyxb.binding.facets.CF_pattern()
RunwayNameType._CF_pattern.addPattern(pattern='(0[1-9]|[12][0-9]|3[0-6])[LRC]{0,1}')
RunwayNameType._InitializeFacetMap(RunwayNameType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RunwayNameType', RunwayNameType)
_module_typeBindings.RunwayNameType = RunwayNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}StandNameType
class StandNameType (pyxb.binding.datatypes.string):

    """
            Stand/gate name. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aerodrome.xsd', 108, 3)
    _Documentation = '\n            Stand/gate name. \n         '
StandNameType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'StandNameType', StandNameType)
_module_typeBindings.StandNameType = StandNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TerminalNameType
class TerminalNameType (pyxb.binding.datatypes.string):

    """
            Common terminal name. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerminalNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aerodrome.xsd', 117, 3)
    _Documentation = '\n            Common terminal name. \n         '
TerminalNameType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TerminalNameType', TerminalNameType)
_module_typeBindings.TerminalNameType = TerminalNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AirspaceTypeType
class AirspaceTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Indicates the type of airspsace. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspaceTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 76, 3)
    _Documentation = '\n            Indicates the type of airspsace. \n         '
AirspaceTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AirspaceTypeType, enum_prefix=None)
AirspaceTypeType.SECTOR = AirspaceTypeType._CF_enumeration.addEnumeration(unicode_value='SECTOR', tag='SECTOR')
AirspaceTypeType.FIR = AirspaceTypeType._CF_enumeration.addEnumeration(unicode_value='FIR', tag='FIR')
AirspaceTypeType._InitializeFacetMap(AirspaceTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AirspaceTypeType', AirspaceTypeType)
_module_typeBindings.AirspaceTypeType = AirspaceTypeType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AtcUnitNameType
class AtcUnitNameType (pyxb.binding.datatypes.string):

    """
            The name of the ATC center with authority over the corresponding Flight Information 
            Region (FIR). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtcUnitNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 88, 3)
    _Documentation = '\n            The name of the ATC center with authority over the corresponding Flight Information \n            Region (FIR). \n         '
AtcUnitNameType._CF_pattern = pyxb.binding.facets.CF_pattern()
AtcUnitNameType._CF_pattern.addPattern(pattern='([A-Z]{4})|([A-Za-z0-9]{1,})')
AtcUnitNameType._InitializeFacetMap(AtcUnitNameType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AtcUnitNameType', AtcUnitNameType)
_module_typeBindings.AtcUnitNameType = AtcUnitNameType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AtsRouteType
class AtsRouteType (pyxb.binding.datatypes.string):

    """
            The coded designator for a published ATS route or route segment. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtsRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 100, 3)
    _Documentation = '\n            The coded designator for a published ATS route or route segment. \n         '
AtsRouteType._CF_pattern = pyxb.binding.facets.CF_pattern()
AtsRouteType._CF_pattern.addPattern(pattern='[A-Z][A-Z0-9]{1,7}')
AtsRouteType._InitializeFacetMap(AtsRouteType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AtsRouteType', AtsRouteType)
_module_typeBindings.AtsRouteType = AtsRouteType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}FixType
class FixType (pyxb.binding.datatypes.string):

    """
            Represents a fix either by name. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FixType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 111, 3)
    _Documentation = '\n            Represents a fix either by name. \n         '
FixType._CF_pattern = pyxb.binding.facets.CF_pattern()
FixType._CF_pattern.addPattern(pattern='[A-Z0-9]{2,5}')
FixType._InitializeFacetMap(FixType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'FixType', FixType)
_module_typeBindings.FixType = FixType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AltitudeMeasureType
class AltitudeMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Unit of measurement for altitudes 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltitudeMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 109, 3)
    _Documentation = '\n            Unit of measurement for altitudes \n         '
AltitudeMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AltitudeMeasureType, enum_prefix=None)
AltitudeMeasureType.FEET = AltitudeMeasureType._CF_enumeration.addEnumeration(unicode_value='FEET', tag='FEET')
AltitudeMeasureType.METRES = AltitudeMeasureType._CF_enumeration.addEnumeration(unicode_value='METRES', tag='METRES')
AltitudeMeasureType._InitializeFacetMap(AltitudeMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AltitudeMeasureType', AltitudeMeasureType)
_module_typeBindings.AltitudeMeasureType = AltitudeMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AltitudeReferenceType
class AltitudeReferenceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Reference point for altitude measurement. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltitudeReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 133, 3)
    _Documentation = '\n            Reference point for altitude measurement. \n         '
AltitudeReferenceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AltitudeReferenceType, enum_prefix=None)
AltitudeReferenceType.MEAN_SEA_LEVEL = AltitudeReferenceType._CF_enumeration.addEnumeration(unicode_value='MEAN_SEA_LEVEL', tag='MEAN_SEA_LEVEL')
AltitudeReferenceType.FLIGHT_LEVEL = AltitudeReferenceType._CF_enumeration.addEnumeration(unicode_value='FLIGHT_LEVEL', tag='FLIGHT_LEVEL')
AltitudeReferenceType._InitializeFacetMap(AltitudeReferenceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AltitudeReferenceType', AltitudeReferenceType)
_module_typeBindings.AltitudeReferenceType = AltitudeReferenceType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}VerticalRateMeasureType
class VerticalRateMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Qualifies VerticalRate as ft/min (if [(-3000)-3000] ) or m/s (if [(-15)-15] ). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VerticalRateMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 190, 3)
    _Documentation = '\n            Qualifies VerticalRate as ft/min (if [(-3000)-3000] ) or m/s (if [(-15)-15] ). \n         '
VerticalRateMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VerticalRateMeasureType, enum_prefix=None)
VerticalRateMeasureType.FEET_PER_MINUTE = VerticalRateMeasureType._CF_enumeration.addEnumeration(unicode_value='FEET_PER_MINUTE', tag='FEET_PER_MINUTE')
VerticalRateMeasureType.METRES_PER_SECOND = VerticalRateMeasureType._CF_enumeration.addEnumeration(unicode_value='METRES_PER_SECOND', tag='METRES_PER_SECOND')
VerticalRateMeasureType._InitializeFacetMap(VerticalRateMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VerticalRateMeasureType', VerticalRateMeasureType)
_module_typeBindings.VerticalRateMeasureType = VerticalRateMeasureType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.double."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 100, 12)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.double
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AirspeedMeasureType
class AirspeedMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Provides units of measure for airspeeds. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspeedMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 102, 3)
    _Documentation = '\n            Provides units of measure for airspeeds. \n         '
AirspeedMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AirspeedMeasureType, enum_prefix=None)
AirspeedMeasureType.KILOMETRES_PER_HOUR = AirspeedMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOMETRES_PER_HOUR', tag='KILOMETRES_PER_HOUR')
AirspeedMeasureType.KNOTS = AirspeedMeasureType._CF_enumeration.addEnumeration(unicode_value='KNOTS', tag='KNOTS')
AirspeedMeasureType.MACH = AirspeedMeasureType._CF_enumeration.addEnumeration(unicode_value='MACH', tag='MACH')
AirspeedMeasureType._InitializeFacetMap(AirspeedMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AirspeedMeasureType', AirspeedMeasureType)
_module_typeBindings.AirspeedMeasureType = AirspeedMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}AngleMeasureType
class AngleMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Units of measure for the Angle type. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AngleMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 164, 3)
    _Documentation = '\n            Units of measure for the Angle type. \n         '
AngleMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AngleMeasureType, enum_prefix=None)
AngleMeasureType.DEGREES = AngleMeasureType._CF_enumeration.addEnumeration(unicode_value='DEGREES', tag='DEGREES')
AngleMeasureType._InitializeFacetMap(AngleMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AngleMeasureType', AngleMeasureType)
_module_typeBindings.AngleMeasureType = AngleMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}DistanceMeasureType
class DistanceMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Indicates the units of measures for a Distance. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistanceMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 227, 3)
    _Documentation = '\n            Indicates the units of measures for a Distance. \n         '
DistanceMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DistanceMeasureType, enum_prefix=None)
DistanceMeasureType.NAUTICAL_MILES = DistanceMeasureType._CF_enumeration.addEnumeration(unicode_value='NAUTICAL_MILES', tag='NAUTICAL_MILES')
DistanceMeasureType.MILES = DistanceMeasureType._CF_enumeration.addEnumeration(unicode_value='MILES', tag='MILES')
DistanceMeasureType.KILOMETERS = DistanceMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOMETERS', tag='KILOMETERS')
DistanceMeasureType._InitializeFacetMap(DistanceMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DistanceMeasureType', DistanceMeasureType)
_module_typeBindings.DistanceMeasureType = DistanceMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}GroundspeedMeasureType
class GroundspeedMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Qualifies the Groundspeed type with metric or imperial units of measure. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundspeedMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 279, 3)
    _Documentation = '\n            Qualifies the Groundspeed type with metric or imperial units of measure. \n         '
GroundspeedMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GroundspeedMeasureType, enum_prefix=None)
GroundspeedMeasureType.KILOMETRES_PER_HOUR = GroundspeedMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOMETRES_PER_HOUR', tag='KILOMETRES_PER_HOUR')
GroundspeedMeasureType.KNOTS = GroundspeedMeasureType._CF_enumeration.addEnumeration(unicode_value='KNOTS', tag='KNOTS')
GroundspeedMeasureType._InitializeFacetMap(GroundspeedMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'GroundspeedMeasureType', GroundspeedMeasureType)
_module_typeBindings.GroundspeedMeasureType = GroundspeedMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}LengthMeasureType
class LengthMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Provides units of measure for length (and height, width). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 323, 3)
    _Documentation = '\n            Provides units of measure for length (and height, width). \n         '
LengthMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthMeasureType, enum_prefix=None)
LengthMeasureType.FEET = LengthMeasureType._CF_enumeration.addEnumeration(unicode_value='FEET', tag='FEET')
LengthMeasureType.INCHES = LengthMeasureType._CF_enumeration.addEnumeration(unicode_value='INCHES', tag='INCHES')
LengthMeasureType.METRES = LengthMeasureType._CF_enumeration.addEnumeration(unicode_value='METRES', tag='METRES')
LengthMeasureType.CENTIMETRES = LengthMeasureType._CF_enumeration.addEnumeration(unicode_value='CENTIMETRES', tag='CENTIMETRES')
LengthMeasureType.MILLIMETRES = LengthMeasureType._CF_enumeration.addEnumeration(unicode_value='MILLIMETRES', tag='MILLIMETRES')
LengthMeasureType._InitializeFacetMap(LengthMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthMeasureType', LengthMeasureType)
_module_typeBindings.LengthMeasureType = LengthMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}PressureMeasureType
class PressureMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Units of measurement for the pressure value. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PressureMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 387, 3)
    _Documentation = '\n            Units of measurement for the pressure value. \n         '
PressureMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PressureMeasureType, enum_prefix=None)
PressureMeasureType.ATMOSPHERES = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='ATMOSPHERES', tag='ATMOSPHERES')
PressureMeasureType.BAR = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='BAR', tag='BAR')
PressureMeasureType.HECTOPASCAL = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='HECTOPASCAL', tag='HECTOPASCAL')
PressureMeasureType.PASCAL = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='PASCAL', tag='PASCAL')
PressureMeasureType.POUNDS_PER_SQUARE_INCH = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='POUNDS_PER_SQUARE_INCH', tag='POUNDS_PER_SQUARE_INCH')
PressureMeasureType.TORR = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='TORR', tag='TORR')
PressureMeasureType.MILLIBAR = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='MILLIBAR', tag='MILLIBAR')
PressureMeasureType.INCHES_OF_MERCURY = PressureMeasureType._CF_enumeration.addEnumeration(unicode_value='INCHES_OF_MERCURY', tag='INCHES_OF_MERCURY')
PressureMeasureType._InitializeFacetMap(PressureMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PressureMeasureType', PressureMeasureType)
_module_typeBindings.PressureMeasureType = PressureMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TemperatureMeasureType
class TemperatureMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Provides units of measure for Temperature. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemperatureMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 472, 3)
    _Documentation = '\n            Provides units of measure for Temperature. \n         '
TemperatureMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TemperatureMeasureType, enum_prefix=None)
TemperatureMeasureType.FARENHEIT = TemperatureMeasureType._CF_enumeration.addEnumeration(unicode_value='FARENHEIT', tag='FARENHEIT')
TemperatureMeasureType.CELSIUS = TemperatureMeasureType._CF_enumeration.addEnumeration(unicode_value='CELSIUS', tag='CELSIUS')
TemperatureMeasureType.KELVIN = TemperatureMeasureType._CF_enumeration.addEnumeration(unicode_value='KELVIN', tag='KELVIN')
TemperatureMeasureType._InitializeFacetMap(TemperatureMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TemperatureMeasureType', TemperatureMeasureType)
_module_typeBindings.TemperatureMeasureType = TemperatureMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}UnitOfMeasureType
class UnitOfMeasureType (pyxb.binding.datatypes.double):

    """
            Abstract Supertype for all units of measure. Takes the place of gml:UnitOfMeasureType. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 525, 3)
    _Documentation = '\n            Abstract Supertype for all units of measure. Takes the place of gml:UnitOfMeasureType. \n            \n         '
UnitOfMeasureType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'UnitOfMeasureType', UnitOfMeasureType)
_module_typeBindings.UnitOfMeasureType = UnitOfMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}VolumeMeasureType
class VolumeMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Provides units of measure for Volume. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumeMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 555, 3)
    _Documentation = '\n            Provides units of measure for Volume. \n         '
VolumeMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeMeasureType, enum_prefix=None)
VolumeMeasureType.LITRES = VolumeMeasureType._CF_enumeration.addEnumeration(unicode_value='LITRES', tag='LITRES')
VolumeMeasureType.GALLONS = VolumeMeasureType._CF_enumeration.addEnumeration(unicode_value='GALLONS', tag='GALLONS')
VolumeMeasureType._InitializeFacetMap(VolumeMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VolumeMeasureType', VolumeMeasureType)
_module_typeBindings.VolumeMeasureType = VolumeMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}WeightMeasureType
class WeightMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Provides units of measure for Weight. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeightMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 599, 3)
    _Documentation = '\n            Provides units of measure for Weight. \n         '
WeightMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WeightMeasureType, enum_prefix=None)
WeightMeasureType.KILOGRAMS = WeightMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOGRAMS', tag='KILOGRAMS')
WeightMeasureType.POUNDS = WeightMeasureType._CF_enumeration.addEnumeration(unicode_value='POUNDS', tag='POUNDS')
WeightMeasureType._InitializeFacetMap(WeightMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WeightMeasureType', WeightMeasureType)
_module_typeBindings.WeightMeasureType = WeightMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}WindSpeedMeasureType
class WindSpeedMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Indicates the units of measure for Wind Speed. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindSpeedMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 653, 3)
    _Documentation = '\n            Indicates the units of measure for Wind Speed. \n         '
WindSpeedMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WindSpeedMeasureType, enum_prefix=None)
WindSpeedMeasureType.MILES_PER_HOUR = WindSpeedMeasureType._CF_enumeration.addEnumeration(unicode_value='MILES_PER_HOUR', tag='MILES_PER_HOUR')
WindSpeedMeasureType.KILOMETRES_PER_HOUR = WindSpeedMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOMETRES_PER_HOUR', tag='KILOMETRES_PER_HOUR')
WindSpeedMeasureType.KNOTS = WindSpeedMeasureType._CF_enumeration.addEnumeration(unicode_value='KNOTS', tag='KNOTS')
WindSpeedMeasureType.METERS_PER_SECOND = WindSpeedMeasureType._CF_enumeration.addEnumeration(unicode_value='METERS_PER_SECOND', tag='METERS_PER_SECOND')
WindSpeedMeasureType._InitializeFacetMap(WindSpeedMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WindSpeedMeasureType', WindSpeedMeasureType)
_module_typeBindings.WindSpeedMeasureType = WindSpeedMeasureType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}DurationType
class DurationType (pyxb.binding.datatypes.duration):

    """
            Extent of time without reference to start or stop times. This is a placeholder for 
            gml:DurationType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DurationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 78, 3)
    _Documentation = '\n            Extent of time without reference to start or stop times. This is a placeholder for \n            gml:DurationType \n         '
DurationType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DurationType', DurationType)
_module_typeBindings.DurationType = DurationType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}TimeType
class TimeType (pyxb.binding.datatypes.dateTime):

    """
            A Time instant placeholder for gml:TimePositionType, in its XML dataTime variation. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 88, 3)
    _Documentation = '\n            A Time instant placeholder for gml:TimePositionType, in its XML dataTime variation. \n            \n         '
TimeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TimeType', TimeType)
_module_typeBindings.TimeType = TimeType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}RestrictedVerticalRateType
class RestrictedVerticalRateType (UnitOfMeasureType):

    """
            Helper type for restrictions on VerticalRateType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedVerticalRateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 178, 3)
    _Documentation = '\n            Helper type for restrictions on VerticalRateType \n         '
RestrictedVerticalRateType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=RestrictedVerticalRateType, value=pyxb.binding.datatypes.double(-3000.0))
RestrictedVerticalRateType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RestrictedVerticalRateType, value=pyxb.binding.datatypes.double(3000.0))
RestrictedVerticalRateType._InitializeFacetMap(RestrictedVerticalRateType._CF_minInclusive,
   RestrictedVerticalRateType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'RestrictedVerticalRateType', RestrictedVerticalRateType)
_module_typeBindings.RestrictedVerticalRateType = RestrictedVerticalRateType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}LatitudeType
class LatitudeType (UnitOfMeasureType):

    """
            Either dd[NS]or ddmm[NS] format. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LatitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 117, 3)
    _Documentation = '\n            Either dd[NS]or ddmm[NS] format. \n         '
LatitudeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LatitudeType', LatitudeType)
_module_typeBindings.LatitudeType = LatitudeType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}LongitudeType
class LongitudeType (UnitOfMeasureType):

    """
            Either ddd[EW] or dddmm[EW] format. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LongitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 126, 3)
    _Documentation = '\n            Either ddd[EW] or dddmm[EW] format. \n         '
LongitudeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LongitudeType', LongitudeType)
_module_typeBindings.LongitudeType = LongitudeType

# Atomic simple type: {http://www.fixm.aero/foundation/3.0}RestrictedAngleType
class RestrictedAngleType (UnitOfMeasureType):

    """
            Helper type for restrictions on AngleType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedAngleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 152, 3)
    _Documentation = '\n            Helper type for restrictions on AngleType \n         '
RestrictedAngleType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=RestrictedAngleType, value=pyxb.binding.datatypes.double(0.0))
RestrictedAngleType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RestrictedAngleType, value=pyxb.binding.datatypes.double(360.0))
RestrictedAngleType._InitializeFacetMap(RestrictedAngleType._CF_minInclusive,
   RestrictedAngleType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'RestrictedAngleType', RestrictedAngleType)
_module_typeBindings.RestrictedAngleType = RestrictedAngleType

# Complex type {http://www.fixm.aero/foundation/3.0}GeographicLocationType with content type ELEMENT_ONLY
class GeographicLocationType (pyxb.binding.basis.complexTypeDefinition):
    """
            Represents a location by latitude and longitude reference. The "srsName" attribute 
            
            names the coordinate reference system (CRS) that defines the semantics of the 
            lat/long pair according to the ISO6709 standard. FIXM uses only "urn:ogc:def:crs:EPSG::4326". 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeographicLocationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 82, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pos'), 'pos', '__httpwww_fixm_aerofoundation3_0_GeographicLocationType_pos', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 93, 9), )

    
    pos = property(__pos.value, __pos.set, None, '\n                  This list of doubles contains the latitude and longitude of the location \n                  in order of LATITUDE FIRST, THEN LONGITUDE. \n               ')

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_fixm_aerofoundation3_0_GeographicLocationType_srsName', pyxb.binding.datatypes.string, fixed=True, unicode_default='urn:ogc:def:crs:EPSG::4326', required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 105, 6)
    __srsName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 105, 6)
    
    srsName = property(__srsName.value, __srsName.set, None, '\n               Names the coordinate reference system (CRS) that defines the semantics of the \n               lat/long pair according to the ISO6709 standard. FIXM uses only "urn:ogc:def:crs:EPSG::4326". \n               \n            ')

    _ElementMap.update({
        __pos.name() : __pos
    })
    _AttributeMap.update({
        __srsName.name() : __srsName
    })
_module_typeBindings.GeographicLocationType = GeographicLocationType
Namespace.addCategoryObject('typeBinding', 'GeographicLocationType', GeographicLocationType)


# Complex type {http://www.fixm.aero/foundation/3.0}DimensionsType with content type ELEMENT_ONLY
class DimensionsType (pyxb.binding.basis.complexTypeDefinition):
    """
            Describes dimensions: weight, height, length. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DimensionsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 175, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__httpwww_fixm_aerofoundation3_0_DimensionsType_height', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 182, 9), )

    
    height = property(__height.value, __height.set, None, "\n                  Used, for example, to indicate a package's dimensions. \n               ")

    
    # Element length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__httpwww_fixm_aerofoundation3_0_DimensionsType_length', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 189, 9), )

    
    length = property(__length.value, __length.set, None, "\n                  Used, for example, to indicate a package's dimensions. \n               ")

    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__httpwww_fixm_aerofoundation3_0_DimensionsType_width', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 196, 9), )

    
    width = property(__width.value, __width.set, None, "\n                  Used, for example, to indicate a package's dimensions. \n               ")

    _ElementMap.update({
        __height.name() : __height,
        __length.name() : __length,
        __width.name() : __width
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DimensionsType = DimensionsType
Namespace.addCategoryObject('typeBinding', 'DimensionsType', DimensionsType)


# Complex type {http://www.fixm.aero/foundation/3.0}PersonOrOrganizationType with content type ELEMENT_ONLY
class PersonOrOrganizationType (pyxb.binding.basis.complexTypeDefinition):
    """
            An identifiable, responsible entity that can be either a natural person or an organization. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonOrOrganizationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 137, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element organization uses Python identifier organization
    __organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'organization'), 'organization', '__httpwww_fixm_aerofoundation3_0_PersonOrOrganizationType_organization', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 145, 9), )

    
    organization = property(__organization.value, __organization.set, None, '\n                  Attribute of PersonOrOrganzation indicating PersonOrOrganzation refers to an Organization. \n                  \n               ')

    
    # Element person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'person'), 'person', '__httpwww_fixm_aerofoundation3_0_PersonOrOrganizationType_person', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 153, 9), )

    
    person = property(__person.value, __person.set, None, '\n                  Attribute of PersonOrOrganzation indicating PersonOrOrganzation refers to a Person. \n                  \n               ')

    _ElementMap.update({
        __organization.name() : __organization,
        __person.name() : __person
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonOrOrganizationType = PersonOrOrganizationType
Namespace.addCategoryObject('typeBinding', 'PersonOrOrganizationType', PersonOrOrganizationType)


# Complex type {http://www.fixm.aero/foundation/3.0}ContactInformationType with content type ELEMENT_ONLY
class ContactInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            Information required to enable contact with the responsible person and/or organisation. 
             This model is derived from ISO19115-2003:Geographic Information- Metadata. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 77, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'address'), 'address', '__httpwww_fixm_aerofoundation3_0_ContactInformationType_address', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 85, 9), )

    
    address = property(__address.value, __address.set, None, '\n                  Optional postal address of the contact. \n               ')

    
    # Element onlineContact uses Python identifier onlineContact
    __onlineContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'onlineContact'), 'onlineContact', '__httpwww_fixm_aerofoundation3_0_ContactInformationType_onlineContact', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 92, 9), )

    
    onlineContact = property(__onlineContact.value, __onlineContact.set, None, '\n                  Optional e-mail address of the contact. \n               ')

    
    # Element phoneFax uses Python identifier phoneFax
    __phoneFax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phoneFax'), 'phoneFax', '__httpwww_fixm_aerofoundation3_0_ContactInformationType_phoneFax', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 99, 9), )

    
    phoneFax = property(__phoneFax.value, __phoneFax.set, None, '\n                  Optional phone or facsimile number of the contact. \n               ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_fixm_aerofoundation3_0_ContactInformationType_name', _module_typeBindings.TextNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 107, 6)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 107, 6)
    
    name = property(__name.value, __name.set, None, "\n               The official name of the contact. In case of the organization use, it is the name \n               of the person within the organization who is the contact point. \n                \n               If the usage of  ContactInformation is associated with a person, this field should \n               not be used, insead, the Person class' name should be used instead. \n            ")

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpwww_fixm_aerofoundation3_0_ContactInformationType_title', _module_typeBindings.TextNameType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 118, 6)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 118, 6)
    
    title = property(__title.value, __title.set, None, '\n               The official title of the contact. \n            ')

    _ElementMap.update({
        __address.name() : __address,
        __onlineContact.name() : __onlineContact,
        __phoneFax.name() : __phoneFax
    })
    _AttributeMap.update({
        __name.name() : __name,
        __title.name() : __title
    })
_module_typeBindings.ContactInformationType = ContactInformationType
Namespace.addCategoryObject('typeBinding', 'ContactInformationType', ContactInformationType)


# Complex type {http://www.fixm.aero/foundation/3.0}OnlineContactType with content type EMPTY
class OnlineContactType (pyxb.binding.basis.complexTypeDefinition):
    """
            On-line or Network information that can be used to contact the individual or organisation, 
            including eMail address and web site page. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OnlineContactType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 128, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute email uses Python identifier email
    __email = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'email'), 'email', '__httpwww_fixm_aerofoundation3_0_OnlineContactType_email', _module_typeBindings.TextAddressType)
    __email._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 135, 6)
    __email._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 135, 6)
    
    email = property(__email.value, __email.set, None, '\n               The address of the electronic mailbox of the responsible organisation or individual. \n               \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __email.name() : __email
    })
_module_typeBindings.OnlineContactType = OnlineContactType
Namespace.addCategoryObject('typeBinding', 'OnlineContactType', OnlineContactType)


# Complex type {http://www.fixm.aero/foundation/3.0}PostalAddressType with content type EMPTY
class PostalAddressType (pyxb.binding.basis.complexTypeDefinition):
    """
            Physical address at which the organization or individual may be contacted. Derived 
            from ISO19115-2003 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PostalAddressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 146, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute administrativeArea uses Python identifier administrativeArea
    __administrativeArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'administrativeArea'), 'administrativeArea', '__httpwww_fixm_aerofoundation3_0_PostalAddressType_administrativeArea', _module_typeBindings.TextNameType)
    __administrativeArea._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 153, 6)
    __administrativeArea._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 153, 6)
    
    administrativeArea = property(__administrativeArea.value, __administrativeArea.set, None, '\n               The state or province of the location or organisation. \n            ')

    
    # Attribute city uses Python identifier city
    __city = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__httpwww_fixm_aerofoundation3_0_PostalAddressType_city', _module_typeBindings.TextCityType)
    __city._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 160, 6)
    __city._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 160, 6)
    
    city = property(__city.value, __city.set, None, '\n               The city of the location or organisation. \n            ')

    
    # Attribute countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'countryCode'), 'countryCode', '__httpwww_fixm_aerofoundation3_0_PostalAddressType_countryCode', _module_typeBindings.TextCountryCodeType)
    __countryCode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 167, 6)
    __countryCode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 167, 6)
    
    countryCode = property(__countryCode.value, __countryCode.set, None, '\n               The country of the physical address for the location or organisation.  ISO 3166 abbreviations. \n               \n            ')

    
    # Attribute countryName uses Python identifier countryName
    __countryName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'countryName'), 'countryName', '__httpwww_fixm_aerofoundation3_0_PostalAddressType_countryName', _module_typeBindings.TextCountryNameType)
    __countryName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 175, 6)
    __countryName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 175, 6)
    
    countryName = property(__countryName.value, __countryName.set, None, '\n               The country of the physical address for the location or organisation.  Full name, \n               not ISO 3166 abbreviations. \n            ')

    
    # Attribute deliveryPoint uses Python identifier deliveryPoint
    __deliveryPoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deliveryPoint'), 'deliveryPoint', '__httpwww_fixm_aerofoundation3_0_PostalAddressType_deliveryPoint', _module_typeBindings.TextAddressType)
    __deliveryPoint._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 183, 6)
    __deliveryPoint._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 183, 6)
    
    deliveryPoint = property(__deliveryPoint.value, __deliveryPoint.set, None, '\n               The street address line for the location.  More than one address line may be used. \n               \n            ')

    
    # Attribute postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'postalCode'), 'postalCode', '__httpwww_fixm_aerofoundation3_0_PostalAddressType_postalCode', _module_typeBindings.TextNameType)
    __postalCode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 191, 6)
    __postalCode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 191, 6)
    
    postalCode = property(__postalCode.value, __postalCode.set, None, '\n               The ZIP or other postal code for the location or organisation. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __administrativeArea.name() : __administrativeArea,
        __city.name() : __city,
        __countryCode.name() : __countryCode,
        __countryName.name() : __countryName,
        __deliveryPoint.name() : __deliveryPoint,
        __postalCode.name() : __postalCode
    })
_module_typeBindings.PostalAddressType = PostalAddressType
Namespace.addCategoryObject('typeBinding', 'PostalAddressType', PostalAddressType)


# Complex type {http://www.fixm.aero/foundation/3.0}TelephoneContactType with content type EMPTY
class TelephoneContactType (pyxb.binding.basis.complexTypeDefinition):
    """
            Telephone numbers at which the organisation or individual may be contacted.  From 
            ISO19115-2003 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TelephoneContactType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 201, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute facimile uses Python identifier facimile
    __facimile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'facimile'), 'facimile', '__httpwww_fixm_aerofoundation3_0_TelephoneContactType_facimile', _module_typeBindings.TextPhoneType)
    __facimile._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 208, 6)
    __facimile._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 208, 6)
    
    facimile = property(__facimile.value, __facimile.set, None, '\n               The telephone number of a facsimile machine for the responsible organisation or individual. \n               \n            ')

    
    # Attribute voice uses Python identifier voice
    __voice = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'voice'), 'voice', '__httpwww_fixm_aerofoundation3_0_TelephoneContactType_voice', _module_typeBindings.TextPhoneType)
    __voice._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 216, 6)
    __voice._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 216, 6)
    
    voice = property(__voice.value, __voice.set, None, '\n               The telephone number by which individuals can speak to the responsible organisation \n               or individual. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __facimile.name() : __facimile,
        __voice.name() : __voice
    })
_module_typeBindings.TelephoneContactType = TelephoneContactType
Namespace.addCategoryObject('typeBinding', 'TelephoneContactType', TelephoneContactType)


# Complex type {http://www.fixm.aero/foundation/3.0}UnitSectorAirspaceType with content type SIMPLE
class UnitSectorAirspaceType (pyxb.binding.basis.complexTypeDefinition):
    """
            A subdivision of the airspace. 
         """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitSectorAirspaceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 122, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute airspaceType uses Python identifier airspaceType
    __airspaceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airspaceType'), 'airspaceType', '__httpwww_fixm_aerofoundation3_0_UnitSectorAirspaceType_airspaceType', _module_typeBindings.AirspaceTypeType)
    __airspaceType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 130, 12)
    __airspaceType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Aeronautical.xsd', 130, 12)
    
    airspaceType = property(__airspaceType.value, __airspaceType.set, None, '\n                     Indicates the type of airspace. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __airspaceType.name() : __airspaceType
    })
_module_typeBindings.UnitSectorAirspaceType = UnitSectorAirspaceType
Namespace.addCategoryObject('typeBinding', 'UnitSectorAirspaceType', UnitSectorAirspaceType)


# Complex type {http://www.fixm.aero/foundation/3.0}AltitudeType with content type SIMPLE
class AltitudeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Simple altitude type: single measurement above specified reference point. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 83, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_fixm_aerofoundation3_0_AltitudeType_ref', _module_typeBindings.AltitudeReferenceType)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 91, 12)
    __ref._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 91, 12)
    
    ref = property(__ref.value, __ref.set, None, '\n                     A required AltitudeReference. \n                  ')

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_AltitudeType_uom', _module_typeBindings.AltitudeMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 98, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 98, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     A required AltitudeMeasure. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref,
        __uom.name() : __uom
    })
_module_typeBindings.AltitudeType = AltitudeType
Namespace.addCategoryObject('typeBinding', 'AltitudeType', AltitudeType)


# Complex type {http://www.fixm.aero/foundation/3.0}AirspeedInIasOrMachType with content type SIMPLE
class AirspeedInIasOrMachType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Airspeed type represents any airspeed measurement, in metric. imperial, or Mach 
            units, as 
            specified by the "uom" attribute. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspeedInIasOrMachType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 80, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_AirspeedInIasOrMachType_uom', _module_typeBindings.AirspeedMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 90, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 90, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of IndicatedAirspeed indicating measurement, in metric. imperial, or Mach \n                     units. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.AirspeedInIasOrMachType = AirspeedInIasOrMachType
Namespace.addCategoryObject('typeBinding', 'AirspeedInIasOrMachType', AirspeedInIasOrMachType)


# Complex type {http://www.fixm.aero/foundation/3.0}DistanceType with content type SIMPLE
class DistanceType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Distance type represents any distance between two points in space, in metric 
            or imperial measurements. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistanceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 207, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_DistanceType_uom', _module_typeBindings.DistanceMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 216, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 216, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Required DistanceMeasure. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.DistanceType = DistanceType
Namespace.addCategoryObject('typeBinding', 'DistanceType', DistanceType)


# Complex type {http://www.fixm.aero/foundation/3.0}GroundspeedType with content type SIMPLE
class GroundspeedType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Groundspeed type represents any ground speed measurement, in metric. or imperial, 
            as 
            specified by the "uom" attribute. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundspeedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 258, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_GroundspeedType_uom', _module_typeBindings.GroundspeedMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 268, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 268, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of Groundspeed indicating units of ground speed measurement. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.GroundspeedType = GroundspeedType
Namespace.addCategoryObject('typeBinding', 'GroundspeedType', GroundspeedType)


# Complex type {http://www.fixm.aero/foundation/3.0}LengthType with content type SIMPLE
class LengthType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Length type represents any length measurement, in metric or imperial measurements. 
            
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 303, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_LengthType_uom', _module_typeBindings.LengthMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 312, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 312, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of Length indicating units of measurement. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.LengthType = LengthType
Namespace.addCategoryObject('typeBinding', 'LengthType', LengthType)


# Complex type {http://www.fixm.aero/foundation/3.0}PressureType with content type SIMPLE
class PressureType (pyxb.binding.basis.complexTypeDefinition):
    """
            Describes the atmospheric pressure. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PressureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 368, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_PressureType_uom', _module_typeBindings.PressureMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 376, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 376, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Indicates the pressure units of measure. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.PressureType = PressureType
Namespace.addCategoryObject('typeBinding', 'PressureType', PressureType)


# Complex type {http://www.fixm.aero/foundation/3.0}TemperatureType with content type SIMPLE
class TemperatureType (pyxb.binding.basis.complexTypeDefinition):
    """
            Represents temperature on a specific scale 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemperatureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 453, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_TemperatureType_uom', _module_typeBindings.TemperatureMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 461, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 461, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of Temperature indicating measurement units. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.TemperatureType = TemperatureType
Namespace.addCategoryObject('typeBinding', 'TemperatureType', TemperatureType)


# Complex type {http://www.fixm.aero/foundation/3.0}TrueAirspeedOrMachType with content type SIMPLE
class TrueAirspeedOrMachType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Airspeed type represents any airspeed measurement, in metric. imperial, or Mach 
            units, as 
            specified by the "uom" attribute. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrueAirspeedOrMachType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 503, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_TrueAirspeedOrMachType_uom', _module_typeBindings.AirspeedMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 513, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 513, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of TrueAirspeed indicating measurement, in metric. imperial, or Mach units. \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.TrueAirspeedOrMachType = TrueAirspeedOrMachType
Namespace.addCategoryObject('typeBinding', 'TrueAirspeedOrMachType', TrueAirspeedOrMachType)


# Complex type {http://www.fixm.aero/foundation/3.0}VolumeType with content type SIMPLE
class VolumeType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Volume type represents any volume measurement, in metric or imperial measurements. 
            
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VolumeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 535, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_VolumeType_uom', _module_typeBindings.VolumeMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 544, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 544, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of Volume indicating measurement units. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.VolumeType = VolumeType
Namespace.addCategoryObject('typeBinding', 'VolumeType', VolumeType)


# Complex type {http://www.fixm.aero/foundation/3.0}WeightType with content type SIMPLE
class WeightType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Weight type represents any weight measurement, in metric or imperial measurements. 
            
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeightType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 579, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_WeightType_uom', _module_typeBindings.WeightMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 588, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 588, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Attribute of Weight indicating measurement units. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.WeightType = WeightType
Namespace.addCategoryObject('typeBinding', 'WeightType', WeightType)


# Complex type {http://www.fixm.aero/foundation/3.0}WindspeedType with content type SIMPLE
class WindspeedType (pyxb.binding.basis.complexTypeDefinition):
    """
            Indicates the Speed of wind. 
         """
    _TypeDefinition = UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindspeedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 634, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_WindspeedType_uom', _module_typeBindings.WindSpeedMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 642, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 642, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Indicates the windspeed units of measure. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.WindspeedType = WindspeedType
Namespace.addCategoryObject('typeBinding', 'WindspeedType', WindspeedType)


# Complex type {http://www.fixm.aero/foundation/3.0}OrganizationType with content type ELEMENT_ONLY
class OrganizationType (pyxb.binding.basis.complexTypeDefinition):
    """
            A feature used to model various Organisations and Authorities. For example: ATS Organisations, 
            Aircraft Operating Agencies, States, Groups of States, etc. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganizationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 78, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__httpwww_fixm_aerofoundation3_0_OrganizationType_contact', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 86, 9), )

    
    contact = property(__contact.value, __contact.set, None, '\n                  Optional ContactInformation reference. \n               ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_fixm_aerofoundation3_0_OrganizationType_name', _module_typeBindings.TextNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 94, 6)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 94, 6)
    
    name = property(__name.value, __name.set, None, '\n               The full official name of the State, Organisation, Authority, aircraft operating \n               agency, handling agency etc. \n            ')

    
    # Attribute otherOrganization uses Python identifier otherOrganization
    __otherOrganization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherOrganization'), 'otherOrganization', '__httpwww_fixm_aerofoundation3_0_OrganizationType_otherOrganization', _module_typeBindings.TextNameType)
    __otherOrganization._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 102, 6)
    __otherOrganization._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 102, 6)
    
    otherOrganization = property(__otherOrganization.value, __otherOrganization.set, None, '\n               Used when OrganizationCatergoryCode enumeration is insufficient. \n            ')

    _ElementMap.update({
        __contact.name() : __contact
    })
    _AttributeMap.update({
        __name.name() : __name,
        __otherOrganization.name() : __otherOrganization
    })
_module_typeBindings.OrganizationType = OrganizationType
Namespace.addCategoryObject('typeBinding', 'OrganizationType', OrganizationType)


# Complex type {http://www.fixm.aero/foundation/3.0}PersonType with content type ELEMENT_ONLY
class PersonType (pyxb.binding.basis.complexTypeDefinition):
    """
            A natural person, rather than an organization or agency. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 112, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__httpwww_fixm_aerofoundation3_0_PersonType_contact', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 119, 9), )

    
    contact = property(__contact.value, __contact.set, None, '\n                  Optional ContactInformation reference. \n               ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_fixm_aerofoundation3_0_PersonType_name', _module_typeBindings.TextNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 127, 6)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 127, 6)
    
    name = property(__name.value, __name.set, None, "\n               Person's name. \n            ")

    _ElementMap.update({
        __contact.name() : __contact
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.PersonType = PersonType
Namespace.addCategoryObject('typeBinding', 'PersonType', PersonType)


# Complex type {http://www.fixm.aero/foundation/3.0}TimeSpanType with content type EMPTY
class TimeSpanType (pyxb.binding.basis.complexTypeDefinition):
    """
            TimeSpans represent passage of time between two events. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeSpanType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 98, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute beginPosition uses Python identifier beginPosition
    __beginPosition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'beginPosition'), 'beginPosition', '__httpwww_fixm_aerofoundation3_0_TimeSpanType_beginPosition', _module_typeBindings.TimeType)
    __beginPosition._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 104, 6)
    __beginPosition._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 104, 6)
    
    beginPosition = property(__beginPosition.value, __beginPosition.set, None, '\n               The start of the current TimeSpan. \n            ')

    
    # Attribute endPosition uses Python identifier endPosition
    __endPosition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endPosition'), 'endPosition', '__httpwww_fixm_aerofoundation3_0_TimeSpanType_endPosition', _module_typeBindings.TimeType)
    __endPosition._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 111, 6)
    __endPosition._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 111, 6)
    
    endPosition = property(__endPosition.value, __endPosition.set, None, '\n               The end of the current TimeSpan. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __beginPosition.name() : __beginPosition,
        __endPosition.name() : __endPosition
    })
_module_typeBindings.TimeSpanType = TimeSpanType
Namespace.addCategoryObject('typeBinding', 'TimeSpanType', TimeSpanType)


# Complex type {http://www.fixm.aero/foundation/3.0}VerticalRateType with content type SIMPLE
class VerticalRateType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Vertical Rate: An expression of an aircraft's vertical rate of change (climb if 
            positive, descent if negative) expressed as a float [(-3000)-3000] if expressed in 
            ft/min, [(-15)-15] if expressed in m/s. 
         """
    _TypeDefinition = RestrictedVerticalRateType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VerticalRateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 157, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RestrictedVerticalRateType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_VerticalRateType_uom', _module_typeBindings.VerticalRateMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 167, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Altitude.xsd', 167, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Required VerticalRateMeasure. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.VerticalRateType = VerticalRateType
Namespace.addCategoryObject('typeBinding', 'VerticalRateType', VerticalRateType)


# Complex type {http://www.fixm.aero/foundation/3.0}AngleType with content type SIMPLE
class AngleType (pyxb.binding.basis.complexTypeDefinition):
    """
            This is a placeholder for gml:AngleType. 
         """
    _TypeDefinition = RestrictedAngleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AngleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 133, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RestrictedAngleType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerofoundation3_0_AngleType_uom', _module_typeBindings.AngleMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 141, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 141, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Indicates angle units of measure. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.AngleType = AngleType
Namespace.addCategoryObject('typeBinding', 'AngleType', AngleType)


# Complex type {http://www.fixm.aero/foundation/3.0}WindDirectionType with content type SIMPLE
class WindDirectionType (AngleType):
    """
            Indicates the direction of the wind which is a specialization of the angle. 
         """
    _TypeDefinition = RestrictedAngleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 623, 3)
    _ElementMap = AngleType._ElementMap.copy()
    _AttributeMap = AngleType._AttributeMap.copy()
    # Base type is AngleType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AngleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WindDirectionType = WindDirectionType
Namespace.addCategoryObject('typeBinding', 'WindDirectionType', WindDirectionType)


GeographicLocation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeographicLocation'), GeographicLocationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 115, 3))
Namespace.addCategoryObject('elementBinding', GeographicLocation.name().localName(), GeographicLocation)

Dimensions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dimensions'), DimensionsType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 205, 3))
Namespace.addCategoryObject('elementBinding', Dimensions.name().localName(), Dimensions)

PersonOrOrganization = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PersonOrOrganization'), PersonOrOrganizationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 163, 3))
Namespace.addCategoryObject('elementBinding', PersonOrOrganization.name().localName(), PersonOrOrganization)

ContactInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContactInformation'), ContactInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 126, 3))
Namespace.addCategoryObject('elementBinding', ContactInformation.name().localName(), ContactInformation)

OnlineContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OnlineContact'), OnlineContactType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 144, 3))
Namespace.addCategoryObject('elementBinding', OnlineContact.name().localName(), OnlineContact)

PostalAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalAddress'), PostalAddressType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 199, 3))
Namespace.addCategoryObject('elementBinding', PostalAddress.name().localName(), PostalAddress)

TelephoneContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TelephoneContact'), TelephoneContactType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 225, 3))
Namespace.addCategoryObject('elementBinding', TelephoneContact.name().localName(), TelephoneContact)

Organization = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organization'), OrganizationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 110, 3))
Namespace.addCategoryObject('elementBinding', Organization.name().localName(), Organization)

Person = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), PersonType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 135, 3))
Namespace.addCategoryObject('elementBinding', Person.name().localName(), Person)

TimeSpan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeSpan'), TimeSpanType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Time.xsd', 119, 3))
Namespace.addCategoryObject('elementBinding', TimeSpan.name().localName(), TimeSpan)



GeographicLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pos'), STD_ANON, scope=GeographicLocationType, documentation='\n                  This list of doubles contains the latitude and longitude of the location \n                  in order of LATITUDE FIRST, THEN LONGITUDE. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 93, 9)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 93, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeographicLocationType._UseForTag(pyxb.namespace.ExpandedName(None, 'pos')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 93, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeographicLocationType._Automaton = _BuildAutomaton()




DimensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), LengthType, scope=DimensionsType, documentation="\n                  Used, for example, to indicate a package's dimensions. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 182, 9)))

DimensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'length'), LengthType, scope=DimensionsType, documentation="\n                  Used, for example, to indicate a package's dimensions. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 189, 9)))

DimensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), LengthType, scope=DimensionsType, documentation="\n                  Used, for example, to indicate a package's dimensions. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 196, 9)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 182, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 189, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 196, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DimensionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 182, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DimensionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'length')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 189, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DimensionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Measures.xsd', 196, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DimensionsType._Automaton = _BuildAutomaton_()




PersonOrOrganizationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'organization'), OrganizationType, scope=PersonOrOrganizationType, documentation='\n                  Attribute of PersonOrOrganzation indicating PersonOrOrganzation refers to an Organization. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 145, 9)))

PersonOrOrganizationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'person'), PersonType, scope=PersonOrOrganizationType, documentation='\n                  Attribute of PersonOrOrganzation indicating PersonOrOrganzation refers to a Person. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 153, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 145, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 153, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonOrOrganizationType._UseForTag(pyxb.namespace.ExpandedName(None, 'organization')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 145, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonOrOrganizationType._UseForTag(pyxb.namespace.ExpandedName(None, 'person')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 153, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonOrOrganizationType._Automaton = _BuildAutomaton_2()




ContactInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'address'), PostalAddressType, scope=ContactInformationType, documentation='\n                  Optional postal address of the contact. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 85, 9)))

ContactInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'onlineContact'), OnlineContactType, scope=ContactInformationType, documentation='\n                  Optional e-mail address of the contact. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 92, 9)))

ContactInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phoneFax'), TelephoneContactType, scope=ContactInformationType, documentation='\n                  Optional phone or facsimile number of the contact. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 99, 9)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 85, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 92, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 99, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContactInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'address')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 85, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContactInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'onlineContact')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 92, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContactInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'phoneFax')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 99, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ContactInformationType._Automaton = _BuildAutomaton_3()




OrganizationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), ContactInformationType, scope=OrganizationType, documentation='\n                  Optional ContactInformation reference. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 86, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 86, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganizationType._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 86, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrganizationType._Automaton = _BuildAutomaton_4()




PersonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), ContactInformationType, scope=PersonType, documentation='\n                  Optional ContactInformation reference. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 119, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 119, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonType._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Organization.xsd', 119, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonType._Automaton = _BuildAutomaton_5()

