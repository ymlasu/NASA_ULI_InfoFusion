# .\_fb.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:31d5e4a51f02c54532375186eedb73a7d2d3e6ed
# Generated 2018-08-28 13:54:41.715858 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace http://www.fixm.aero/base/3.0 [xmlns:fb]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d2045a4a-aaf3-11e8-ae54-ecb1d75f2e16')

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
import _ff as _ImportedBinding__ff

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.fixm.aero/base/3.0', create_if_missing=True)
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


# Atomic simple type: {http://www.fixm.aero/base/3.0}StandardInstrumentRouteDesignatorType
class StandardInstrumentRouteDesignatorType (pyxb.binding.datatypes.string):

    """
            Describes a standard instrument route procedure. May be used for arrival or departure 
            depending on context. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandardInstrumentRouteDesignatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 140, 3)
    _Documentation = '\n            Describes a standard instrument route procedure. May be used for arrival or departure \n            depending on context. \n         '
StandardInstrumentRouteDesignatorType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'StandardInstrumentRouteDesignatorType', StandardInstrumentRouteDesignatorType)
_module_typeBindings.StandardInstrumentRouteDesignatorType = StandardInstrumentRouteDesignatorType

# Atomic simple type: {http://www.fixm.aero/base/3.0}ConstrainedAirspaceType
class ConstrainedAirspaceType (pyxb.binding.datatypes.string):

    """
            Constrained Airspace such as Flow Constrained Area (FCA) 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConstrainedAirspaceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 104, 3)
    _Documentation = '\n            Constrained Airspace such as Flow Constrained Area (FCA) \n         '
ConstrainedAirspaceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ConstrainedAirspaceType', ConstrainedAirspaceType)
_module_typeBindings.ConstrainedAirspaceType = ConstrainedAirspaceType

# Atomic simple type: {http://www.fixm.aero/base/3.0}DelegatedUnitIndicatorType
class DelegatedUnitIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Delegated Unit Indicator: Indicates whether or not the controlling unit has been 
            delegated authority for the flight based on agreement with the unit in whose Area 
            of Responsibility (AOR) the flight is currently located 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DelegatedUnitIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 113, 3)
    _Documentation = '\n            .Delegated Unit Indicator: Indicates whether or not the controlling unit has been \n            delegated authority for the flight based on agreement with the unit in whose Area \n            of Responsibility (AOR) the flight is currently located \n         '
DelegatedUnitIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DelegatedUnitIndicatorType, enum_prefix=None)
DelegatedUnitIndicatorType.AUTHORITY_DELEGATED = DelegatedUnitIndicatorType._CF_enumeration.addEnumeration(unicode_value='AUTHORITY_DELEGATED', tag='AUTHORITY_DELEGATED')
DelegatedUnitIndicatorType._InitializeFacetMap(DelegatedUnitIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DelegatedUnitIndicatorType', DelegatedUnitIndicatorType)
_module_typeBindings.DelegatedUnitIndicatorType = DelegatedUnitIndicatorType

# Atomic simple type: {http://www.fixm.aero/base/3.0}SlotAssignmentType
class SlotAssignmentType (pyxb.binding.datatypes.string):

    """
            Arrival or departure slot assignment. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SlotAssignmentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 153, 3)
    _Documentation = '\n            Arrival or departure slot assignment. \n         '
SlotAssignmentType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SlotAssignmentType', SlotAssignmentType)
_module_typeBindings.SlotAssignmentType = SlotAssignmentType

# Atomic simple type: {http://www.fixm.aero/base/3.0}ProvenanceCentreType
class ProvenanceCentreType (pyxb.binding.datatypes.string):

    """
            Name of the ATC (FIR) center that produced the data 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProvenanceCentreType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 151, 3)
    _Documentation = '\n            Name of the ATC (FIR) center that produced the data \n         '
ProvenanceCentreType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ProvenanceCentreType', ProvenanceCentreType)
_module_typeBindings.ProvenanceCentreType = ProvenanceCentreType

# Atomic simple type: {http://www.fixm.aero/base/3.0}ProvenanceSourceType
class ProvenanceSourceType (pyxb.binding.datatypes.string):

    """
            Indication of the source of the data in the Provenance, for archival analysis. 
            While this field has no formal definition, it might take values like: 
            * ACID of the flight that produced it. 
            * Name or ID of a controller 
            * Name or ID of a pilot 
            * Name of airline 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProvenanceSourceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 160, 3)
    _Documentation = '\n            Indication of the source of the data in the Provenance, for archival analysis. \n            While this field has no formal definition, it might take values like: \n            * ACID of the flight that produced it. \n            * Name or ID of a controller \n            * Name or ID of a pilot \n            * Name of airline \n         '
ProvenanceSourceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ProvenanceSourceType', ProvenanceSourceType)
_module_typeBindings.ProvenanceSourceType = ProvenanceSourceType

# Atomic simple type: {http://www.fixm.aero/base/3.0}ProvenanceSystemType
class ProvenanceSystemType (pyxb.binding.datatypes.string):

    """
            Name of the flight data system that produced the data. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProvenanceSystemType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 174, 3)
    _Documentation = '\n            Name of the flight data system that produced the data. \n         '
ProvenanceSystemType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ProvenanceSystemType', ProvenanceSystemType)
_module_typeBindings.ProvenanceSystemType = ProvenanceSystemType

# Atomic simple type: {http://www.fixm.aero/base/3.0}DirectionReferenceType
class DirectionReferenceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Indicates direction relative to True North or Magnetic North 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DirectionReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 97, 3)
    _Documentation = '\n            Indicates direction relative to True North or Magnetic North \n         '
DirectionReferenceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DirectionReferenceType, enum_prefix=None)
DirectionReferenceType.TRUE = DirectionReferenceType._CF_enumeration.addEnumeration(unicode_value='TRUE', tag='TRUE')
DirectionReferenceType.MAGNETIC = DirectionReferenceType._CF_enumeration.addEnumeration(unicode_value='MAGNETIC', tag='MAGNETIC')
DirectionReferenceType._InitializeFacetMap(DirectionReferenceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DirectionReferenceType', DirectionReferenceType)
_module_typeBindings.DirectionReferenceType = DirectionReferenceType

# Atomic simple type: {http://www.fixm.aero/base/3.0}AftnAddressType
class AftnAddressType (pyxb.binding.datatypes.string):

    """
            Standard AFTN address. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AftnAddressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 79, 3)
    _Documentation = '\n            Standard AFTN address. \n         '
AftnAddressType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AftnAddressType', AftnAddressType)
_module_typeBindings.AftnAddressType = AftnAddressType

# Atomic simple type: {http://www.fixm.aero/base/3.0}AirTrafficTypeType
class AirTrafficTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            The type of flight value associated with the point. It is associated with the first 
            point on the route and any subsequent point where the type of flight value changes. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirTrafficTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 139, 3)
    _Documentation = '\n            The type of flight value associated with the point. It is associated with the first \n            point on the route and any subsequent point where the type of flight value changes. \n            \n         '
AirTrafficTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AirTrafficTypeType, enum_prefix=None)
AirTrafficTypeType.OAT = AirTrafficTypeType._CF_enumeration.addEnumeration(unicode_value='OAT', tag='OAT')
AirTrafficTypeType.GAT = AirTrafficTypeType._CF_enumeration.addEnumeration(unicode_value='GAT', tag='GAT')
AirTrafficTypeType._InitializeFacetMap(AirTrafficTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AirTrafficTypeType', AirTrafficTypeType)
_module_typeBindings.AirTrafficTypeType = AirTrafficTypeType

# Atomic simple type: {http://www.fixm.aero/base/3.0}RestrictedBeaconCodeType
class RestrictedBeaconCodeType (pyxb.binding.datatypes.string):

    """
            Helper type for restrictions on BeaconCodeType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedBeaconCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 213, 3)
    _Documentation = '\n            Helper type for restrictions on BeaconCodeType \n         '
RestrictedBeaconCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
RestrictedBeaconCodeType._CF_pattern.addPattern(pattern='[0-7]{4}')
RestrictedBeaconCodeType._InitializeFacetMap(RestrictedBeaconCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RestrictedBeaconCodeType', RestrictedBeaconCodeType)
_module_typeBindings.RestrictedBeaconCodeType = RestrictedBeaconCodeType

# Atomic simple type: {http://www.fixm.aero/base/3.0}CarrierIdentifierType
class CarrierIdentifierType (pyxb.binding.datatypes.string):

    """
            A 3 letter Identifier for carrier. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CarrierIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 224, 3)
    _Documentation = '\n            A 3 letter Identifier for carrier. \n         '
CarrierIdentifierType._CF_pattern = pyxb.binding.facets.CF_pattern()
CarrierIdentifierType._CF_pattern.addPattern(pattern='[A-Z]{3}')
CarrierIdentifierType._InitializeFacetMap(CarrierIdentifierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CarrierIdentifierType', CarrierIdentifierType)
_module_typeBindings.CarrierIdentifierType = CarrierIdentifierType

# Atomic simple type: {http://www.fixm.aero/base/3.0}CountType
class CountType (pyxb.binding.datatypes.int):

    """
            Represents positive integer counts of objects. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 235, 3)
    _Documentation = '\n            Represents positive integer counts of objects. \n         '
CountType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=CountType, value=pyxb.binding.datatypes.int(0))
CountType._InitializeFacetMap(CountType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'CountType', CountType)
_module_typeBindings.CountType = CountType

# Atomic simple type: {http://www.fixm.aero/base/3.0}DecimalIndexType
class DecimalIndexType (pyxb.binding.datatypes.decimal):

    """
            Generic decimal fraction expressed to tenths, used as scaling or comparison factor. 
            Instances should add high and low bounds as appropriate. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DecimalIndexType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 246, 3)
    _Documentation = '\n            Generic decimal fraction expressed to tenths, used as scaling or comparison factor. \n            Instances should add high and low bounds as appropriate. \n         '
DecimalIndexType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(4))
DecimalIndexType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(1))
DecimalIndexType._InitializeFacetMap(DecimalIndexType._CF_totalDigits,
   DecimalIndexType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'DecimalIndexType', DecimalIndexType)
_module_typeBindings.DecimalIndexType = DecimalIndexType

# Atomic simple type: {http://www.fixm.aero/base/3.0}FleetPriorityType
class FleetPriorityType (pyxb.binding.datatypes.int):

    """
            Used to assign relative priorities to things and events.  A lower number means a 
            higher priority. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FleetPriorityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 259, 3)
    _Documentation = '\n            Used to assign relative priorities to things and events.  A lower number means a \n            higher priority. \n         '
FleetPriorityType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=FleetPriorityType, value=pyxb.binding.datatypes.int(1))
FleetPriorityType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=FleetPriorityType, value=pyxb.binding.datatypes.int(10))
FleetPriorityType._InitializeFacetMap(FleetPriorityType._CF_minInclusive,
   FleetPriorityType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'FleetPriorityType', FleetPriorityType)
_module_typeBindings.FleetPriorityType = FleetPriorityType

# Atomic simple type: {http://www.fixm.aero/base/3.0}FlightIdentifierType
class FlightIdentifierType (pyxb.binding.datatypes.string):

    """
            The flight name - sometimes called ACID 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 272, 3)
    _Documentation = '\n            The flight name - sometimes called ACID \n         '
FlightIdentifierType._CF_pattern = pyxb.binding.facets.CF_pattern()
FlightIdentifierType._CF_pattern.addPattern(pattern='[A-Z0-9]{1,7}')
FlightIdentifierType._InitializeFacetMap(FlightIdentifierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'FlightIdentifierType', FlightIdentifierType)
_module_typeBindings.FlightIdentifierType = FlightIdentifierType

# Atomic simple type: {http://www.fixm.aero/base/3.0}FlightRulesType
class FlightRulesType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            The regulation, or combination of regulations, that governs all aspects of operations 
            under which the pilot plans to fly. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightRulesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 283, 3)
    _Documentation = '\n            The regulation, or combination of regulations, that governs all aspects of operations \n            under which the pilot plans to fly. \n         '
FlightRulesType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FlightRulesType, enum_prefix=None)
FlightRulesType.IFR = FlightRulesType._CF_enumeration.addEnumeration(unicode_value='IFR', tag='IFR')
FlightRulesType.VFR = FlightRulesType._CF_enumeration.addEnumeration(unicode_value='VFR', tag='VFR')
FlightRulesType._InitializeFacetMap(FlightRulesType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FlightRulesType', FlightRulesType)
_module_typeBindings.FlightRulesType = FlightRulesType

# Atomic simple type: {http://www.fixm.aero/base/3.0}FreeTextType
class FreeTextType (pyxb.binding.datatypes.string):

    """
            Provides a standard representation for elements that may contain any text, 
            such as comments and notes. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FreeTextType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 308, 3)
    _Documentation = '\n            Provides a standard representation for elements that may contain any text, \n            such as comments and notes. \n         '
FreeTextType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
FreeTextType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4096))
FreeTextType._InitializeFacetMap(FreeTextType._CF_minLength,
   FreeTextType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'FreeTextType', FreeTextType)
_module_typeBindings.FreeTextType = FreeTextType

# Atomic simple type: {http://www.fixm.aero/base/3.0}FrequencyMeasureType
class FrequencyMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Radio frequency unit of measure. Either kHz OR MHz. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FrequencyMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 321, 3)
    _Documentation = '\n            Radio frequency unit of measure. Either kHz OR MHz. \n         '
FrequencyMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FrequencyMeasureType, enum_prefix=None)
FrequencyMeasureType.MEGAHERTZ = FrequencyMeasureType._CF_enumeration.addEnumeration(unicode_value='MEGAHERTZ', tag='MEGAHERTZ')
FrequencyMeasureType.KILOHERTZ = FrequencyMeasureType._CF_enumeration.addEnumeration(unicode_value='KILOHERTZ', tag='KILOHERTZ')
FrequencyMeasureType._InitializeFacetMap(FrequencyMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FrequencyMeasureType', FrequencyMeasureType)
_module_typeBindings.FrequencyMeasureType = FrequencyMeasureType

# Atomic simple type: {http://www.fixm.aero/base/3.0}RestrictedGloballyUniqueFlightIdentifierType
class RestrictedGloballyUniqueFlightIdentifierType (pyxb.binding.datatypes.string):

    """
            Helper type for restrictions on GloballyUniqueFlightIdentifierType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedGloballyUniqueFlightIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 365, 3)
    _Documentation = '\n            Helper type for restrictions on GloballyUniqueFlightIdentifierType \n         '
RestrictedGloballyUniqueFlightIdentifierType._CF_pattern = pyxb.binding.facets.CF_pattern()
RestrictedGloballyUniqueFlightIdentifierType._CF_pattern.addPattern(pattern='[0-9|aA-fF]{8}-[0-9|aA-fF]{4}-4[0-9|aA-fF]{3}-[89aAbB]{1}[0-9|aA-fF]{3}-[0-9|aA-fF]{12}')
RestrictedGloballyUniqueFlightIdentifierType._InitializeFacetMap(RestrictedGloballyUniqueFlightIdentifierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RestrictedGloballyUniqueFlightIdentifierType', RestrictedGloballyUniqueFlightIdentifierType)
_module_typeBindings.RestrictedGloballyUniqueFlightIdentifierType = RestrictedGloballyUniqueFlightIdentifierType

# Atomic simple type: {http://www.fixm.aero/base/3.0}IcaoAircraftIdentifierType
class IcaoAircraftIdentifierType (pyxb.binding.datatypes.string):

    """
            ICAO standard nomenclature of aircraft manufacturer and type. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IcaoAircraftIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 429, 3)
    _Documentation = '\n            ICAO standard nomenclature of aircraft manufacturer and type. \n         '
IcaoAircraftIdentifierType._CF_pattern = pyxb.binding.facets.CF_pattern()
IcaoAircraftIdentifierType._CF_pattern.addPattern(pattern='[A-Z0-9]{2,4}')
IcaoAircraftIdentifierType._InitializeFacetMap(IcaoAircraftIdentifierType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'IcaoAircraftIdentifierType', IcaoAircraftIdentifierType)
_module_typeBindings.IcaoAircraftIdentifierType = IcaoAircraftIdentifierType

# Atomic simple type: {http://www.fixm.aero/base/3.0}OfftrackDirectionType
class OfftrackDirectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Specifies the direction of the lateral offset offset. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OfftrackDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 529, 3)
    _Documentation = '\n            Specifies the direction of the lateral offset offset. \n         '
OfftrackDirectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OfftrackDirectionType, enum_prefix=None)
OfftrackDirectionType.LEFT = OfftrackDirectionType._CF_enumeration.addEnumeration(unicode_value='LEFT', tag='LEFT')
OfftrackDirectionType.RIGHT = OfftrackDirectionType._CF_enumeration.addEnumeration(unicode_value='RIGHT', tag='RIGHT')
OfftrackDirectionType._InitializeFacetMap(OfftrackDirectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OfftrackDirectionType', OfftrackDirectionType)
_module_typeBindings.OfftrackDirectionType = OfftrackDirectionType

# Atomic simple type: {http://www.fixm.aero/base/3.0}OfftrackReasonType
class OfftrackReasonType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            The reason for boundary crossing offset deviation. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OfftrackReasonType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 567, 3)
    _Documentation = '\n            The reason for boundary crossing offset deviation. \n         '
OfftrackReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OfftrackReasonType, enum_prefix=None)
OfftrackReasonType.OFFSET = OfftrackReasonType._CF_enumeration.addEnumeration(unicode_value='OFFSET', tag='OFFSET')
OfftrackReasonType.DEVIATION = OfftrackReasonType._CF_enumeration.addEnumeration(unicode_value='DEVIATION', tag='DEVIATION')
OfftrackReasonType._InitializeFacetMap(OfftrackReasonType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OfftrackReasonType', OfftrackReasonType)
_module_typeBindings.OfftrackReasonType = OfftrackReasonType

# Atomic simple type: {http://www.fixm.aero/base/3.0}ParametersType
class ParametersType (pyxb.binding.datatypes.string):

    """
            The purpose of this class is to serve as a base class for parameter information for 
            the flight such as the ATN Logon parameters, and FANS/1A parameters 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParametersType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 592, 3)
    _Documentation = '\n            The purpose of this class is to serve as a base class for parameter information for \n            the flight such as the ATN Logon parameters, and FANS/1A parameters \n         '
ParametersType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(49))
ParametersType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(200))
ParametersType._InitializeFacetMap(ParametersType._CF_minLength,
   ParametersType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ParametersType', ParametersType)
_module_typeBindings.ParametersType = ParametersType

# Atomic simple type: {http://www.fixm.aero/base/3.0}SpeedConditionType
class SpeedConditionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            The speed condition indicates whether the aircraft will be maintaining, exceeding, 
            or flying more slowly than the assigned speed. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpeedConditionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 656, 3)
    _Documentation = '\n            The speed condition indicates whether the aircraft will be maintaining, exceeding, \n            or flying more slowly than the assigned speed. \n         '
SpeedConditionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpeedConditionType, enum_prefix=None)
SpeedConditionType.AT_OR_LESS = SpeedConditionType._CF_enumeration.addEnumeration(unicode_value='AT_OR_LESS', tag='AT_OR_LESS')
SpeedConditionType.AT_OR_GREATER = SpeedConditionType._CF_enumeration.addEnumeration(unicode_value='AT_OR_GREATER', tag='AT_OR_GREATER')
SpeedConditionType.AT = SpeedConditionType._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
SpeedConditionType._InitializeFacetMap(SpeedConditionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpeedConditionType', SpeedConditionType)
_module_typeBindings.SpeedConditionType = SpeedConditionType

# Atomic simple type: {http://www.fixm.aero/base/3.0}SsrModeType
class SsrModeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Represents the enumeration of Secondary Surveillance Radar (SSR) Modes: 
            * A - Transponder-Mode A (4 digits-4,096 codes) 
            * C - Transponder-Mode A (4 digits-4,096 codes) and Mode C 
            * S - Transponder-Mode S, including both pressure-altitude and aircraft identification 
            transmission 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SsrModeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 691, 3)
    _Documentation = '\n            Represents the enumeration of Secondary Surveillance Radar (SSR) Modes: \n            * A - Transponder-Mode A (4 digits-4,096 codes) \n            * C - Transponder-Mode A (4 digits-4,096 codes) and Mode C \n            * S - Transponder-Mode S, including both pressure-altitude and aircraft identification \n            transmission \n         '
SsrModeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SsrModeType, enum_prefix=None)
SsrModeType.A = SsrModeType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
SsrModeType.C = SsrModeType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
SsrModeType.S = SsrModeType._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
SsrModeType._InitializeFacetMap(SsrModeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SsrModeType', SsrModeType)
_module_typeBindings.SsrModeType = SsrModeType

# Atomic simple type: [anonymous]
class STD_ANON (FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 505, 9)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='[A-Z0-9_]{1,20}')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 519, 9)
    _Documentation = None
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minLength,
   STD_ANON_._CF_maxLength)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://www.fixm.aero/base/3.0}RestrictedRadioFrequencyType
class RestrictedRadioFrequencyType (_ImportedBinding__ff.UnitOfMeasureType):

    """
            Helper type for restrictions on RadioFrequencyType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedRadioFrequencyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 625, 3)
    _Documentation = '\n            Helper type for restrictions on RadioFrequencyType \n         '
RestrictedRadioFrequencyType._CF_pattern = pyxb.binding.facets.CF_pattern()
RestrictedRadioFrequencyType._CF_pattern.addPattern(pattern='[0-9]{3}\\.[0-9]{2}')
RestrictedRadioFrequencyType._InitializeFacetMap(RestrictedRadioFrequencyType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RestrictedRadioFrequencyType', RestrictedRadioFrequencyType)
_module_typeBindings.RestrictedRadioFrequencyType = RestrictedRadioFrequencyType

# Complex type {http://www.fixm.aero/base/3.0}AerodromeReferenceType with content type EMPTY
class AerodromeReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """
            Aerodromes may be identified by: 
            * their ICAO codes ("KDFW"), OR 
            * (for unlisted aerodromes) their names ("Dallas Fort Worth") PLUS significant point 
            
            * The aerodrome name can also include a 3 character IATA Alternate Identifier such 
            as "DFW" 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AerodromeReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 81, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AerodromeReferenceType = AerodromeReferenceType
Namespace.addCategoryObject('typeBinding', 'AerodromeReferenceType', AerodromeReferenceType)


# Complex type {http://www.fixm.aero/base/3.0}SignificantPointType with content type EMPTY
class SignificantPointType (pyxb.binding.basis.complexTypeDefinition):
    """
            A location type restricted to lat/long location, fix (waypoint) location, or FRD 
            (radial distance offset). 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SignificantPointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 194, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SignificantPointType = SignificantPointType
Namespace.addCategoryObject('typeBinding', 'SignificantPointType', SignificantPointType)


# Complex type {http://www.fixm.aero/base/3.0}MultiTimeType with content type ELEMENT_ONLY
class MultiTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            MultiTime is a general-purpose structure that records a common pattern of flight 
            time: 
             
            * estimated 
            * actual 
            * controlled 
            * earliest 
            * etc. 
             
            This base implementation of MultiTime contains only "actual" and "estimated" time 
            values. It is assumed 
            that users of MultiTime will extend it by adding attributes for the other time types 
            that they need. It is recommended that these extensions also use cardinality 0..1 
            for new time elements. 
             
            Each of these times is an instance of a ReportedTime, and each recorded time is decorated 
            with a Provenance block that describes the system that contributed it, so that data 
            fusion systems can sort out which of the competing times to believe. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 111, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element actual uses Python identifier actual
    __actual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'actual'), 'actual', '__httpwww_fixm_aerobase3_0_MultiTimeType_actual', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9), )

    
    actual = property(__actual.value, __actual.set, None, '\n                  Time at which the event is observed to occur \n               ')

    
    # Element estimated uses Python identifier estimated
    __estimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'estimated'), 'estimated', '__httpwww_fixm_aerobase3_0_MultiTimeType_estimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9), )

    
    estimated = property(__estimated.value, __estimated.set, None, '\n                  Time at which the event is estimated to occur \n               ')

    _ElementMap.update({
        __actual.name() : __actual,
        __estimated.name() : __estimated
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MultiTimeType = MultiTimeType
Namespace.addCategoryObject('typeBinding', 'MultiTimeType', MultiTimeType)


# Complex type {http://www.fixm.aero/base/3.0}TimeSequenceType with content type ELEMENT_ONLY
class TimeSequenceType (pyxb.binding.basis.complexTypeDefinition):
    """
            TimeSequence represents important times in a process that spans some time and has 
            multiple steps. Each element of TimeSequence represents a record of the actual time 
            associated with each step of the process. TimeSequence does not require that all 
            steps of the process be present or complete, and it does not permit multiple occurrences 
            of the same step. 
             
            This base implementation of TimeSequence contains only "approval", "begin", "end", 
            "ready", and "request" times. It is assumed that users of this type will extend it 
            by adding intermediate steps. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeSequenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 201, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element approval uses Python identifier approval
    __approval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'approval'), 'approval', '__httpwww_fixm_aerobase3_0_TimeSequenceType_approval', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 216, 9), )

    
    approval = property(__approval.value, __approval.set, None, '\n                  Step 2 of the TimeSequence. \n               ')

    
    # Element begin uses Python identifier begin
    __begin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_fixm_aerobase3_0_TimeSequenceType_begin', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 223, 9), )

    
    begin = property(__begin.value, __begin.set, None, '\n                  Step 4 of the TimeSequence. \n               ')

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_fixm_aerobase3_0_TimeSequenceType_end', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 230, 9), )

    
    end = property(__end.value, __end.set, None, '\n                  Step 5 of the TimeSequence. \n               ')

    
    # Element ready uses Python identifier ready
    __ready = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ready'), 'ready', '__httpwww_fixm_aerobase3_0_TimeSequenceType_ready', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 237, 9), )

    
    ready = property(__ready.value, __ready.set, None, '\n                  Step 3 of the TimeSequence. \n               ')

    
    # Element request uses Python identifier request
    __request = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'request'), 'request', '__httpwww_fixm_aerobase3_0_TimeSequenceType_request', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 244, 9), )

    
    request = property(__request.value, __request.set, None, '\n                  Step 1 of the TimeSequence. \n               ')

    _ElementMap.update({
        __approval.name() : __approval,
        __begin.name() : __begin,
        __end.name() : __end,
        __ready.name() : __ready,
        __request.name() : __request
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TimeSequenceType = TimeSequenceType
Namespace.addCategoryObject('typeBinding', 'TimeSequenceType', TimeSequenceType)


# Complex type {http://www.fixm.aero/base/3.0}AirspeedChoiceType with content type ELEMENT_ONLY
class AirspeedChoiceType (pyxb.binding.basis.complexTypeDefinition):
    """
            The airspeed choice indicates that airspeed can either be expressed as specific with 
            a speed condition or a speed range between lower and upper bounds. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspeedChoiceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 88, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element airspeed uses Python identifier airspeed
    __airspeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airspeed'), 'airspeed', '__httpwww_fixm_aerobase3_0_AirspeedChoiceType_airspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 96, 9), )

    
    airspeed = property(__airspeed.value, __airspeed.set, None, '\n                  The airspeed can be expressed as a specific speed with a condition. \n               ')

    
    # Element airspeedRange uses Python identifier airspeedRange
    __airspeedRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airspeedRange'), 'airspeedRange', '__httpwww_fixm_aerobase3_0_AirspeedChoiceType_airspeedRange', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 103, 9), )

    
    airspeedRange = property(__airspeedRange.value, __airspeedRange.set, None, '\n                  The airspeed that can be expressed as a range between a lower and upper bound. \n               ')

    _ElementMap.update({
        __airspeed.name() : __airspeed,
        __airspeedRange.name() : __airspeedRange
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AirspeedChoiceType = AirspeedChoiceType
Namespace.addCategoryObject('typeBinding', 'AirspeedChoiceType', AirspeedChoiceType)


# Complex type {http://www.fixm.aero/base/3.0}AirspeedRangeType with content type ELEMENT_ONLY
class AirspeedRangeType (pyxb.binding.basis.complexTypeDefinition):
    """
            The airspeed that can be expressed as a range between a lower and upper bound. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspeedRangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 114, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lowerSpeed uses Python identifier lowerSpeed
    __lowerSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lowerSpeed'), 'lowerSpeed', '__httpwww_fixm_aerobase3_0_AirspeedRangeType_lowerSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 121, 9), )

    
    lowerSpeed = property(__lowerSpeed.value, __lowerSpeed.set, None, '\n                  Lower bound of the speed range. \n               ')

    
    # Element upperSpeed uses Python identifier upperSpeed
    __upperSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upperSpeed'), 'upperSpeed', '__httpwww_fixm_aerobase3_0_AirspeedRangeType_upperSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 128, 9), )

    
    upperSpeed = property(__upperSpeed.value, __upperSpeed.set, None, '\n                  Upper bound of the speed range \n               ')

    _ElementMap.update({
        __lowerSpeed.name() : __lowerSpeed,
        __upperSpeed.name() : __upperSpeed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AirspeedRangeType = AirspeedRangeType
Namespace.addCategoryObject('typeBinding', 'AirspeedRangeType', AirspeedRangeType)


# Complex type {http://www.fixm.aero/base/3.0}AltitudeChoiceType with content type ELEMENT_ONLY
class AltitudeChoiceType (pyxb.binding.basis.complexTypeDefinition):
    """
            The altitude choice allows to either represent a specific altitude or an altitude 
            range with a lower and upper bound 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltitudeChoiceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 166, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altitude'), 'altitude', '__httpwww_fixm_aerobase3_0_AltitudeChoiceType_altitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 174, 9), )

    
    altitude = property(__altitude.value, __altitude.set, None, '\n                  Altitude expressed as a specific altitude. \n               ')

    
    # Element altitudeRange uses Python identifier altitudeRange
    __altitudeRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altitudeRange'), 'altitudeRange', '__httpwww_fixm_aerobase3_0_AltitudeChoiceType_altitudeRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 181, 9), )

    
    altitudeRange = property(__altitudeRange.value, __altitudeRange.set, None, '\n                  Altitude that can be expressed as a range between a lower and upper bound. \n               ')

    _ElementMap.update({
        __altitude.name() : __altitude,
        __altitudeRange.name() : __altitudeRange
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AltitudeChoiceType = AltitudeChoiceType
Namespace.addCategoryObject('typeBinding', 'AltitudeChoiceType', AltitudeChoiceType)


# Complex type {http://www.fixm.aero/base/3.0}GroundspeedChoiceType with content type ELEMENT_ONLY
class GroundspeedChoiceType (pyxb.binding.basis.complexTypeDefinition):
    """
            The groundspeed choice indicates that groundspeed can either be expressed as specific 
            with a speed condition or a speed range between lower and upper bounds. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundspeedChoiceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 376, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element groundspeed uses Python identifier groundspeed
    __groundspeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'groundspeed'), 'groundspeed', '__httpwww_fixm_aerobase3_0_GroundspeedChoiceType_groundspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 384, 9), )

    
    groundspeed = property(__groundspeed.value, __groundspeed.set, None, '\n                  Groundspeed can be expressed as a specific speed. \n               ')

    
    # Element groundspeedRange uses Python identifier groundspeedRange
    __groundspeedRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'groundspeedRange'), 'groundspeedRange', '__httpwww_fixm_aerobase3_0_GroundspeedChoiceType_groundspeedRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 391, 9), )

    
    groundspeedRange = property(__groundspeedRange.value, __groundspeedRange.set, None, '\n                  The groundspeed that can be expressed as a range between a lower and upper bound. \n                  \n               ')

    _ElementMap.update({
        __groundspeed.name() : __groundspeed,
        __groundspeedRange.name() : __groundspeedRange
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GroundspeedChoiceType = GroundspeedChoiceType
Namespace.addCategoryObject('typeBinding', 'GroundspeedChoiceType', GroundspeedChoiceType)


# Complex type {http://www.fixm.aero/base/3.0}GroundspeedRangeType with content type ELEMENT_ONLY
class GroundspeedRangeType (pyxb.binding.basis.complexTypeDefinition):
    """
            The groundspeed that can be expressed as a range between a lower and upper bound. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundspeedRangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 403, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lowerSpeed uses Python identifier lowerSpeed
    __lowerSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lowerSpeed'), 'lowerSpeed', '__httpwww_fixm_aerobase3_0_GroundspeedRangeType_lowerSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 411, 9), )

    
    lowerSpeed = property(__lowerSpeed.value, __lowerSpeed.set, None, '\n                  Lower bound of the groundspeed range. \n               ')

    
    # Element upperSpeed uses Python identifier upperSpeed
    __upperSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upperSpeed'), 'upperSpeed', '__httpwww_fixm_aerobase3_0_GroundspeedRangeType_upperSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 418, 9), )

    
    upperSpeed = property(__upperSpeed.value, __upperSpeed.set, None, '\n                  Upper bound of the sroundspeed range. \n               ')

    _ElementMap.update({
        __lowerSpeed.name() : __lowerSpeed,
        __upperSpeed.name() : __upperSpeed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GroundspeedRangeType = GroundspeedRangeType
Namespace.addCategoryObject('typeBinding', 'GroundspeedRangeType', GroundspeedRangeType)


# Complex type {http://www.fixm.aero/base/3.0}NameValueListType with content type ELEMENT_ONLY
class NameValueListType (pyxb.binding.basis.complexTypeDefinition):
    """
            A basic list of name/value pairs. 
             
            The name/value list structure is intended for use in the RARE situations where otherwise 
            unstructured data can be rendered into a semi-structure of tags and data. It is not 
            appropriate for adding arbitrary data to arbitrary places in the schema. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameValueListType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 467, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element nameValue uses Python identifier nameValue
    __nameValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nameValue'), 'nameValue', '__httpwww_fixm_aerobase3_0_NameValueListType_nameValue', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 478, 9), )

    
    nameValue = property(__nameValue.value, __nameValue.set, None, '\n                  A set of up to 10 name-value pairs. \n               ')

    _ElementMap.update({
        __nameValue.name() : __nameValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NameValueListType = NameValueListType
Namespace.addCategoryObject('typeBinding', 'NameValueListType', NameValueListType)


# Complex type {http://www.fixm.aero/base/3.0}VerticalRangeType with content type ELEMENT_ONLY
class VerticalRangeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Represents a vertical range from a lower bound altitude to an upper bound altitude. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VerticalRangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 727, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lowerBound uses Python identifier lowerBound
    __lowerBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lowerBound'), 'lowerBound', '__httpwww_fixm_aerobase3_0_VerticalRangeType_lowerBound', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 735, 9), )

    
    lowerBound = property(__lowerBound.value, __lowerBound.set, None, '\n                  Lower bound altitude of the vertical range. \n               ')

    
    # Element upperBound uses Python identifier upperBound
    __upperBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upperBound'), 'upperBound', '__httpwww_fixm_aerobase3_0_VerticalRangeType_upperBound', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 742, 9), )

    
    upperBound = property(__upperBound.value, __upperBound.set, None, '\n                  Upper bound altitude of the vertical range. \n               ')

    _ElementMap.update({
        __lowerBound.name() : __lowerBound,
        __upperBound.name() : __upperBound
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VerticalRangeType = VerticalRangeType
Namespace.addCategoryObject('typeBinding', 'VerticalRangeType', VerticalRangeType)


# Complex type {http://www.fixm.aero/base/3.0}IcaoAerodromeReferenceType with content type EMPTY
class IcaoAerodromeReferenceType (AerodromeReferenceType):
    """
            Aerodrome identified by standard ICAO identifier code 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IcaoAerodromeReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 95, 3)
    _ElementMap = AerodromeReferenceType._ElementMap.copy()
    _AttributeMap = AerodromeReferenceType._AttributeMap.copy()
    # Base type is AerodromeReferenceType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpwww_fixm_aerobase3_0_IcaoAerodromeReferenceType_code', _ImportedBinding__ff.AerodromeIcaoCodeType)
    __code._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 103, 12)
    __code._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 103, 12)
    
    code = property(__code.value, __code.set, None, '\n                     Aerodrome\'s ICAO code. e.g. "KDFW" \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })
_module_typeBindings.IcaoAerodromeReferenceType = IcaoAerodromeReferenceType
Namespace.addCategoryObject('typeBinding', 'IcaoAerodromeReferenceType', IcaoAerodromeReferenceType)


# Complex type {http://www.fixm.aero/base/3.0}RunwayPositionAndTimeType with content type ELEMENT_ONLY
class RunwayPositionAndTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Reference to an airport runway for arrival, departure, or surface movement. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunwayPositionAndTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 115, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element runwayTime uses Python identifier runwayTime
    __runwayTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'runwayTime'), 'runwayTime', '__httpwww_fixm_aerobase3_0_RunwayPositionAndTimeType_runwayTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 122, 9), )

    
    runwayTime = property(__runwayTime.value, __runwayTime.set, None, '\n                  Time associated with the specified runway \n               ')

    
    # Attribute runwayName uses Python identifier runwayName
    __runwayName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'runwayName'), 'runwayName', '__httpwww_fixm_aerobase3_0_RunwayPositionAndTimeType_runwayName', _ImportedBinding__ff.RunwayNameType)
    __runwayName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 130, 6)
    __runwayName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 130, 6)
    
    runwayName = property(__runwayName.value, __runwayName.set, None, '\n               Name associated with the runway \n            ')

    _ElementMap.update({
        __runwayTime.name() : __runwayTime
    })
    _AttributeMap.update({
        __runwayName.name() : __runwayName
    })
_module_typeBindings.RunwayPositionAndTimeType = RunwayPositionAndTimeType
Namespace.addCategoryObject('typeBinding', 'RunwayPositionAndTimeType', RunwayPositionAndTimeType)


# Complex type {http://www.fixm.aero/base/3.0}StandPositionAndTimeType with content type ELEMENT_ONLY
class StandPositionAndTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Reference to an airport stand that an aircraft can arrive at, depart from, or traverse 
            during arrival, departure, or surface movement. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandPositionAndTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 150, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element standTime uses Python identifier standTime
    __standTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'standTime'), 'standTime', '__httpwww_fixm_aerobase3_0_StandPositionAndTimeType_standTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 158, 9), )

    
    standTime = property(__standTime.value, __standTime.set, None, '\n                  Represents a time at the stand. Either departure time from the stand or arrival time \n                  to the stand depending on the context in which it is used. \n               ')

    
    # Attribute standName uses Python identifier standName
    __standName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standName'), 'standName', '__httpwww_fixm_aerobase3_0_StandPositionAndTimeType_standName', _ImportedBinding__ff.StandNameType)
    __standName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 167, 6)
    __standName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 167, 6)
    
    standName = property(__standName.value, __standName.set, None, '\n               Name of the traversed stand. \n            ')

    
    # Attribute terminalName uses Python identifier terminalName
    __terminalName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'terminalName'), 'terminalName', '__httpwww_fixm_aerobase3_0_StandPositionAndTimeType_terminalName', _ImportedBinding__ff.TerminalNameType)
    __terminalName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 174, 6)
    __terminalName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 174, 6)
    
    terminalName = property(__terminalName.value, __terminalName.set, None, '\n               Name of the traversed terminal. \n            ')

    _ElementMap.update({
        __standTime.name() : __standTime
    })
    _AttributeMap.update({
        __standName.name() : __standName,
        __terminalName.name() : __terminalName
    })
_module_typeBindings.StandPositionAndTimeType = StandPositionAndTimeType
Namespace.addCategoryObject('typeBinding', 'StandPositionAndTimeType', StandPositionAndTimeType)


# Complex type {http://www.fixm.aero/base/3.0}UnlistedAerodromeReferenceType with content type ELEMENT_ONLY
class UnlistedAerodromeReferenceType (AerodromeReferenceType):
    """
            Identifies an aerodrome (that does not possess a listed ICAO code) by specifying 
            both 
            * its aerodrome name ("Dallas Fort Worth") AND 
            * a significant point consisting of 
    * its geographic location (latitude and longitude) OR
    * the first significant point of a flight route OR
    * fix/radial/offset from a known waypoint.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnlistedAerodromeReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 184, 3)
    _ElementMap = AerodromeReferenceType._ElementMap.copy()
    _AttributeMap = AerodromeReferenceType._AttributeMap.copy()
    # Base type is AerodromeReferenceType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__httpwww_fixm_aerobase3_0_UnlistedAerodromeReferenceType_point', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 199, 15), )

    
    point = property(__point.value, __point.set, None, "\n                        A significant point consisting of the aerodrome's \n                        * geographic location (latitude and longitude) OR \n                        * the first significant point of a flight route OR \n                        * fix/radial/offset from a known waypoint. \n                     ")

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_fixm_aerobase3_0_UnlistedAerodromeReferenceType_name', _ImportedBinding__ff.AerodromeNameType)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 210, 12)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 210, 12)
    
    name = property(__name.value, __name.set, None, '\n                     Aerodrome\'s name. e.g. "Dallas Fort Worth". * The e name can also include a 3 character \n                     IATA Alternate Identifier such as "DFW" \n                  ')

    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.UnlistedAerodromeReferenceType = UnlistedAerodromeReferenceType
Namespace.addCategoryObject('typeBinding', 'UnlistedAerodromeReferenceType', UnlistedAerodromeReferenceType)


# Complex type {http://www.fixm.aero/base/3.0}AtcUnitReferenceType with content type EMPTY
class AtcUnitReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """
            Reference to an Air Traffic Control organization of any type: unit, sector, etc. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtcUnitReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 80, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute delegated uses Python identifier delegated
    __delegated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delegated'), 'delegated', '__httpwww_fixm_aerobase3_0_AtcUnitReferenceType_delegated', _module_typeBindings.DelegatedUnitIndicatorType)
    __delegated._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 87, 6)
    __delegated._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 87, 6)
    
    delegated = property(__delegated.value, __delegated.set, None, '\n               if present, reference represents a delegated authority. \n            ')

    
    # Attribute sectorIdentifier uses Python identifier sectorIdentifier
    __sectorIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sectorIdentifier'), 'sectorIdentifier', '__httpwww_fixm_aerobase3_0_AtcUnitReferenceType_sectorIdentifier', _module_typeBindings.FreeTextType)
    __sectorIdentifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 94, 6)
    __sectorIdentifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 94, 6)
    
    sectorIdentifier = property(__sectorIdentifier.value, __sectorIdentifier.set, None, '\n               Identifies the sector associated with this AtcUnit \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __delegated.name() : __delegated,
        __sectorIdentifier.name() : __sectorIdentifier
    })
_module_typeBindings.AtcUnitReferenceType = AtcUnitReferenceType
Namespace.addCategoryObject('typeBinding', 'AtcUnitReferenceType', AtcUnitReferenceType)


# Complex type {http://www.fixm.aero/base/3.0}FeatureType with content type EMPTY
class FeatureType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Feature type is the parent of all FIXM complex types that describe physical 
            objects or events. 
             
            It is used as a marker to messaging and other tools that the contained information 
            is 
            to be treated as an unit and not further decomposed. 
             
            Feature carries information about the ultimate source of its contained data 
            in the "Provenance" attribute group. Implicitly, this information qualifies all the 
            
            contained elements, unless one of them overrides it locally. 
             
            It is expected that applications will use this to record their own meta-data about 
            the information contained in the feature. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeatureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 78, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute centre uses Python identifier centre
    __centre = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'centre'), 'centre', '__httpwww_fixm_aerobase3_0_FeatureType_centre', _module_typeBindings.ProvenanceCentreType)
    __centre._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 121, 6)
    __centre._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 121, 6)
    
    centre = property(__centre.value, __centre.set, None, '\n               The ATC center (or FIR) that produced the data contained in the Provenance. \n            ')

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__httpwww_fixm_aerobase3_0_FeatureType_source', _module_typeBindings.ProvenanceSourceType)
    __source._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 128, 6)
    __source._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 128, 6)
    
    source = property(__source.value, __source.set, None, '\n               The source of the data in the message (unstructured, for archival analysis). \n            ')

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__httpwww_fixm_aerobase3_0_FeatureType_system', _module_typeBindings.ProvenanceSystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 135, 6)
    __system._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 135, 6)
    
    system = property(__system.value, __system.set, None, '\n               The name of the system that generated the data contained in the Provenance. \n            ')

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__httpwww_fixm_aerobase3_0_FeatureType_timestamp', _ImportedBinding__ff.TimeType)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 142, 6)
    __timestamp._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 142, 6)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, '\n               The time at which the provenance information was recorded. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __centre.name() : __centre,
        __source.name() : __source,
        __system.name() : __system,
        __timestamp.name() : __timestamp
    })
_module_typeBindings.FeatureType = FeatureType
Namespace.addCategoryObject('typeBinding', 'FeatureType', FeatureType)


# Complex type {http://www.fixm.aero/base/3.0}FixPointType with content type EMPTY
class FixPointType (SignificantPointType):
    """
            Significant point described by a fix. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FixPointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 121, 3)
    _ElementMap = SignificantPointType._ElementMap.copy()
    _AttributeMap = SignificantPointType._AttributeMap.copy()
    # Base type is SignificantPointType
    
    # Attribute fix uses Python identifier fix
    __fix = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fix'), 'fix', '__httpwww_fixm_aerobase3_0_FixPointType_fix', _ImportedBinding__ff.FixType)
    __fix._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 129, 12)
    __fix._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 129, 12)
    
    fix = property(__fix.value, __fix.set, None, '\n                     One of three possibilities, "fix" provides the lat/lon of this Significant Point. \n                     \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fix.name() : __fix
    })
_module_typeBindings.FixPointType = FixPointType
Namespace.addCategoryObject('typeBinding', 'FixPointType', FixPointType)


# Complex type {http://www.fixm.aero/base/3.0}LocationPointType with content type ELEMENT_ONLY
class LocationPointType (SignificantPointType):
    """
            Significant point described by a geographic location. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocationPointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 142, 3)
    _ElementMap = SignificantPointType._ElementMap.copy()
    _AttributeMap = SignificantPointType._AttributeMap.copy()
    # Base type is SignificantPointType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__httpwww_fixm_aerobase3_0_LocationPointType_location', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 151, 15), )

    
    location = property(__location.value, __location.set, None, '\n                        One of three possibilities, "location" provides the fix/waypoint of this Significant \n                        Point. \n                     ')

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LocationPointType = LocationPointType
Namespace.addCategoryObject('typeBinding', 'LocationPointType', LocationPointType)


# Complex type {http://www.fixm.aero/base/3.0}ReportedTimeType with content type EMPTY
class ReportedTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            ReportedTime is a record of a time instant, together with a Provenance block that 
            describes the system that 
            contributed it. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportedTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 153, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute centre uses Python identifier centre
    __centre = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'centre'), 'centre', '__httpwww_fixm_aerobase3_0_ReportedTimeType_centre', _module_typeBindings.ProvenanceCentreType)
    __centre._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 121, 6)
    __centre._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 121, 6)
    
    centre = property(__centre.value, __centre.set, None, '\n               The ATC center (or FIR) that produced the data contained in the Provenance. \n            ')

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__httpwww_fixm_aerobase3_0_ReportedTimeType_source', _module_typeBindings.ProvenanceSourceType)
    __source._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 128, 6)
    __source._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 128, 6)
    
    source = property(__source.value, __source.set, None, '\n               The source of the data in the message (unstructured, for archival analysis). \n            ')

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__httpwww_fixm_aerobase3_0_ReportedTimeType_system', _module_typeBindings.ProvenanceSystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 135, 6)
    __system._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 135, 6)
    
    system = property(__system.value, __system.set, None, '\n               The name of the system that generated the data contained in the Provenance. \n            ')

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__httpwww_fixm_aerobase3_0_ReportedTimeType_timestamp', _ImportedBinding__ff.TimeType)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 142, 6)
    __timestamp._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 142, 6)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, '\n               The time at which the provenance information was recorded. \n            ')

    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__httpwww_fixm_aerobase3_0_ReportedTimeType_time', _ImportedBinding__ff.TimeType)
    __time._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 161, 6)
    __time._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 161, 6)
    
    time = property(__time.value, __time.set, None, '\n               Time at which the event occurred \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __centre.name() : __centre,
        __source.name() : __source,
        __system.name() : __system,
        __timestamp.name() : __timestamp,
        __time.name() : __time
    })
_module_typeBindings.ReportedTimeType = ReportedTimeType
Namespace.addCategoryObject('typeBinding', 'ReportedTimeType', ReportedTimeType)


# Complex type {http://www.fixm.aero/base/3.0}TargetMultiTimeType with content type ELEMENT_ONLY
class TargetMultiTimeType (MultiTimeType):
    """
            TargetMultiTime is an extension of MultiTime that includes target time for use in 
            data that requires target time in addition to estimated and actual time. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TargetMultiTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 178, 3)
    _ElementMap = MultiTimeType._ElementMap.copy()
    _AttributeMap = MultiTimeType._AttributeMap.copy()
    # Base type is MultiTimeType
    
    # Element actual (actual) inherited from {http://www.fixm.aero/base/3.0}MultiTimeType
    
    # Element estimated (estimated) inherited from {http://www.fixm.aero/base/3.0}MultiTimeType
    
    # Element target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__httpwww_fixm_aerobase3_0_TargetMultiTimeType_target', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 188, 15), )

    
    target = property(__target.value, __target.set, None, '\n                        Time estimate by qualified personnel \n                     ')

    _ElementMap.update({
        __target.name() : __target
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TargetMultiTimeType = TargetMultiTimeType
Namespace.addCategoryObject('typeBinding', 'TargetMultiTimeType', TargetMultiTimeType)


# Complex type {http://www.fixm.aero/base/3.0}BeaconCodeType with content type SIMPLE
class BeaconCodeType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Beacon Code: The assigned four-character numeric code transmitted by the aircraft 
            transponder in response to a secondary surveillance radar interrogation signal which 
            is used to assist air traffic controllers to identify aircraft. 
         """
    _TypeDefinition = RestrictedBeaconCodeType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BeaconCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 192, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RestrictedBeaconCodeType
    
    # Attribute ssrMode uses Python identifier ssrMode
    __ssrMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ssrMode'), 'ssrMode', '__httpwww_fixm_aerobase3_0_BeaconCodeType_ssrMode', _module_typeBindings.SsrModeType)
    __ssrMode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 202, 12)
    __ssrMode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 202, 12)
    
    ssrMode = property(__ssrMode.value, __ssrMode.set, None, '\n                     Optional Secondary Surveillance Radar (SSR) Mode. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ssrMode.name() : __ssrMode
    })
_module_typeBindings.BeaconCodeType = BeaconCodeType
Namespace.addCategoryObject('typeBinding', 'BeaconCodeType', BeaconCodeType)


# Complex type {http://www.fixm.aero/base/3.0}GloballyUniqueFlightIdentifierType with content type SIMPLE
class GloballyUniqueFlightIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """
            A reference that uniquely identifies a specific flight and that is independent of 
            any particular system. 
         """
    _TypeDefinition = RestrictedGloballyUniqueFlightIdentifierType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GloballyUniqueFlightIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 345, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RestrictedGloballyUniqueFlightIdentifierType
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codeSpace'), 'codeSpace', '__httpwww_fixm_aerobase3_0_GloballyUniqueFlightIdentifierType_codeSpace', pyxb.binding.datatypes.string, fixed=True, unicode_default='urn:uuid', required=True)
    __codeSpace._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 354, 12)
    __codeSpace._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 354, 12)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, '\n                     Code Space of the GUFI \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __codeSpace.name() : __codeSpace
    })
_module_typeBindings.GloballyUniqueFlightIdentifierType = GloballyUniqueFlightIdentifierType
Namespace.addCategoryObject('typeBinding', 'GloballyUniqueFlightIdentifierType', GloballyUniqueFlightIdentifierType)


# Complex type {http://www.fixm.aero/base/3.0}LateralOfftrackType with content type ELEMENT_ONLY
class LateralOfftrackType (pyxb.binding.basis.complexTypeDefinition):
    """
            Represents a lateral offtrack which can either be an offset or weather deviation. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LateralOfftrackType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 440, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element offtrackDistance uses Python identifier offtrackDistance
    __offtrackDistance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offtrackDistance'), 'offtrackDistance', '__httpwww_fixm_aerobase3_0_LateralOfftrackType_offtrackDistance', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 448, 9), )

    
    offtrackDistance = property(__offtrackDistance.value, __offtrackDistance.set, None, '\n                  Represents offtrack distances that are lateral relative to a location expressed by \n                  a distance measurement and offset direction. \n               ')

    
    # Attribute offtrackReason uses Python identifier offtrackReason
    __offtrackReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offtrackReason'), 'offtrackReason', '__httpwww_fixm_aerobase3_0_LateralOfftrackType_offtrackReason', _module_typeBindings.OfftrackReasonType)
    __offtrackReason._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 457, 6)
    __offtrackReason._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 457, 6)
    
    offtrackReason = property(__offtrackReason.value, __offtrackReason.set, None, '\n               Specifies the reason for Lateral Offtrack \n            ')

    _ElementMap.update({
        __offtrackDistance.name() : __offtrackDistance
    })
    _AttributeMap.update({
        __offtrackReason.name() : __offtrackReason
    })
_module_typeBindings.LateralOfftrackType = LateralOfftrackType
Namespace.addCategoryObject('typeBinding', 'LateralOfftrackType', LateralOfftrackType)


# Complex type {http://www.fixm.aero/base/3.0}OfftrackDistanceType with content type ELEMENT_ONLY
class OfftrackDistanceType (pyxb.binding.basis.complexTypeDefinition):
    """
            Represents an offtrack distance that is lateral relative to a location expressed 
            by a distance measurement and offset direction. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OfftrackDistanceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 541, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element distance uses Python identifier distance
    __distance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distance'), 'distance', '__httpwww_fixm_aerobase3_0_OfftrackDistanceType_distance', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 549, 9), )

    
    distance = property(__distance.value, __distance.set, None, '\n                  Specifies the distance of the offtrack. \n               ')

    
    # Attribute direction uses Python identifier direction
    __direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'direction'), 'direction', '__httpwww_fixm_aerobase3_0_OfftrackDistanceType_direction', _module_typeBindings.OfftrackDirectionType)
    __direction._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 557, 6)
    __direction._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 557, 6)
    
    direction = property(__direction.value, __direction.set, None, '\n               Specifies the direction of the offset \n            ')

    _ElementMap.update({
        __distance.name() : __distance
    })
    _AttributeMap.update({
        __direction.name() : __direction
    })
_module_typeBindings.OfftrackDistanceType = OfftrackDistanceType
Namespace.addCategoryObject('typeBinding', 'OfftrackDistanceType', OfftrackDistanceType)


# Complex type {http://www.fixm.aero/base/3.0}IdentifiedUnitReferenceType with content type EMPTY
class IdentifiedUnitReferenceType (AtcUnitReferenceType):
    """
            Represents the Aeronautical Fixed Telecommunication Network station address 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifiedUnitReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 133, 3)
    _ElementMap = AtcUnitReferenceType._ElementMap.copy()
    _AttributeMap = AtcUnitReferenceType._AttributeMap.copy()
    # Base type is AtcUnitReferenceType
    
    # Attribute delegated inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute sectorIdentifier inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute unitIdentifier uses Python identifier unitIdentifier
    __unitIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitIdentifier'), 'unitIdentifier', '__httpwww_fixm_aerobase3_0_IdentifiedUnitReferenceType_unitIdentifier', _ImportedBinding__ff.AtcUnitNameType)
    __unitIdentifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 141, 12)
    __unitIdentifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 141, 12)
    
    unitIdentifier = property(__unitIdentifier.value, __unitIdentifier.set, None, '\n                     Identifier for the unit \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unitIdentifier.name() : __unitIdentifier
    })
_module_typeBindings.IdentifiedUnitReferenceType = IdentifiedUnitReferenceType
Namespace.addCategoryObject('typeBinding', 'IdentifiedUnitReferenceType', IdentifiedUnitReferenceType)


# Complex type {http://www.fixm.aero/base/3.0}UnknownUnitReferenceType with content type ELEMENT_ONLY
class UnknownUnitReferenceType (AtcUnitReferenceType):
    """
            The name and optional location of this ATC unit. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnknownUnitReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 162, 3)
    _ElementMap = AtcUnitReferenceType._ElementMap.copy()
    _AttributeMap = AtcUnitReferenceType._AttributeMap.copy()
    # Base type is AtcUnitReferenceType
    
    # Element unitLocation uses Python identifier unitLocation
    __unitLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'unitLocation'), 'unitLocation', '__httpwww_fixm_aerobase3_0_UnknownUnitReferenceType_unitLocation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 171, 15), )

    
    unitLocation = property(__unitLocation.value, __unitLocation.set, None, '\n                        Location by latitude and longitude. \n                     ')

    
    # Attribute delegated inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute sectorIdentifier inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute unitNameOrAltId uses Python identifier unitNameOrAltId
    __unitNameOrAltId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitNameOrAltId'), 'unitNameOrAltId', '__httpwww_fixm_aerobase3_0_UnknownUnitReferenceType_unitNameOrAltId', _module_typeBindings.FreeTextType)
    __unitNameOrAltId._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 179, 12)
    __unitNameOrAltId._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 179, 12)
    
    unitNameOrAltId = property(__unitNameOrAltId.value, __unitNameOrAltId.set, None, '\n                     Text name of this ATC unit or an alternate identifier for the unit. \n                  ')

    _ElementMap.update({
        __unitLocation.name() : __unitLocation
    })
    _AttributeMap.update({
        __unitNameOrAltId.name() : __unitNameOrAltId
    })
_module_typeBindings.UnknownUnitReferenceType = UnknownUnitReferenceType
Namespace.addCategoryObject('typeBinding', 'UnknownUnitReferenceType', UnknownUnitReferenceType)


# Complex type {http://www.fixm.aero/base/3.0}ExtensionType with content type EMPTY
class ExtensionType (FeatureType):
    """
            The Extension type is the base type from which extension (non-core) objects inherit. 
            
            Extension objects can be attached to a Flight through the "extensions" element. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtensionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Extension.xsd', 77, 3)
    _ElementMap = FeatureType._ElementMap.copy()
    _AttributeMap = FeatureType._AttributeMap.copy()
    # Base type is FeatureType
    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtensionType = ExtensionType
Namespace.addCategoryObject('typeBinding', 'ExtensionType', ExtensionType)


# Complex type {http://www.fixm.aero/base/3.0}RelativePointType with content type ELEMENT_ONLY
class RelativePointType (FixPointType):
    """
            Significant point described by a relative (fix radial distance) location. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelativePointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 165, 3)
    _ElementMap = FixPointType._ElementMap.copy()
    _AttributeMap = FixPointType._AttributeMap.copy()
    # Base type is FixPointType
    
    # Element distance uses Python identifier distance
    __distance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distance'), 'distance', '__httpwww_fixm_aerobase3_0_RelativePointType_distance', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 174, 15), )

    
    distance = property(__distance.value, __distance.set, None, '\n                        The distance from a known waypoint/fix. \n                     ')

    
    # Element radial uses Python identifier radial
    __radial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radial'), 'radial', '__httpwww_fixm_aerobase3_0_RelativePointType_radial', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 181, 15), )

    
    radial = property(__radial.value, __radial.set, None, '\n                        The radius from a known fix/waypoint. \n                     ')

    
    # Attribute fix inherited from {http://www.fixm.aero/base/3.0}FixPointType
    _ElementMap.update({
        __distance.name() : __distance,
        __radial.name() : __radial
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelativePointType = RelativePointType
Namespace.addCategoryObject('typeBinding', 'RelativePointType', RelativePointType)


# Complex type {http://www.fixm.aero/base/3.0}ExtendedMultiTimeType with content type ELEMENT_ONLY
class ExtendedMultiTimeType (TargetMultiTimeType):
    """
            ExpandedMultiTime is an extension of TargetMultiTime and hence MultiTime that includes 
            additional attributes of initial and controlled time for data that requires those 
            additional time fields. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExtendedMultiTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 80, 3)
    _ElementMap = TargetMultiTimeType._ElementMap.copy()
    _AttributeMap = TargetMultiTimeType._AttributeMap.copy()
    # Base type is TargetMultiTimeType
    
    # Element controlled uses Python identifier controlled
    __controlled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'controlled'), 'controlled', '__httpwww_fixm_aerobase3_0_ExtendedMultiTimeType_controlled', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 91, 15), )

    
    controlled = property(__controlled.value, __controlled.set, None, '\n                        Time specified by the controller of control program \n                     ')

    
    # Element initial uses Python identifier initial
    __initial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'initial'), 'initial', '__httpwww_fixm_aerobase3_0_ExtendedMultiTimeType_initial', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 98, 15), )

    
    initial = property(__initial.value, __initial.set, None, '\n                        Time as first specified in the flight plan \n                     ')

    
    # Element actual (actual) inherited from {http://www.fixm.aero/base/3.0}MultiTimeType
    
    # Element estimated (estimated) inherited from {http://www.fixm.aero/base/3.0}MultiTimeType
    
    # Element target (target) inherited from {http://www.fixm.aero/base/3.0}TargetMultiTimeType
    _ElementMap.update({
        __controlled.name() : __controlled,
        __initial.name() : __initial
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExtendedMultiTimeType = ExtendedMultiTimeType
Namespace.addCategoryObject('typeBinding', 'ExtendedMultiTimeType', ExtendedMultiTimeType)


# Complex type {http://www.fixm.aero/base/3.0}NameValuePairType with content type EMPTY
class NameValuePairType (pyxb.binding.basis.complexTypeDefinition):
    """
            This is a general purpose data structure used when it is desired to map an identifying 
            string (the "name") into a data string (the "value"). These name/value pairs are 
            often part of a repeating element so that the whole element expresses a set of names 
            mapped onto a set of values. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameValuePairType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 489, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_fixm_aerobase3_0_NameValuePairType_name', _module_typeBindings.STD_ANON)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 498, 6)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 498, 6)
    
    name = property(__name.value, __name.set, None, '\n               The identifying portion of the pair, formatted as if for an enumeration. Consider \n               using an actual enumeration for legal values. \n            ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__httpwww_fixm_aerobase3_0_NameValuePairType_value', _module_typeBindings.STD_ANON_)
    __value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 511, 6)
    __value._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 511, 6)
    
    value_ = property(__value.value, __value.set, None, '\n               The data content portion of the pair. This is intended for a *short* unstructured \n               string like a natural language comment, and should not be used as storage for codes, \n               values, or other structured data. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
_module_typeBindings.NameValuePairType = NameValuePairType
Namespace.addCategoryObject('typeBinding', 'NameValuePairType', NameValuePairType)


# Complex type {http://www.fixm.aero/base/3.0}RadioFrequencyType with content type SIMPLE
class RadioFrequencyType (pyxb.binding.basis.complexTypeDefinition):
    """
            RadioFrequency is the designation of a communication frequency in the HF, UHF, VHF, 
            EHF bands 
         """
    _TypeDefinition = RestrictedRadioFrequencyType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadioFrequencyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 605, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RestrictedRadioFrequencyType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aerobase3_0_RadioFrequencyType_uom', _module_typeBindings.FrequencyMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 614, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 614, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Required unit of measure for RadioFrequency in KHz OR MHz. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.RadioFrequencyType = RadioFrequencyType
Namespace.addCategoryObject('typeBinding', 'RadioFrequencyType', RadioFrequencyType)


# Complex type {http://www.fixm.aero/base/3.0}SpeedType with content type SIMPLE
class SpeedType (_ImportedBinding__ff.AirspeedInIasOrMachType):
    """
            The airspeed can be expressed as a specific speed with a condition. 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpeedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 636, 3)
    _ElementMap = _ImportedBinding__ff.AirspeedInIasOrMachType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AirspeedInIasOrMachType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AirspeedInIasOrMachType
    
    # Attribute speedCondition uses Python identifier speedCondition
    __speedCondition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speedCondition'), 'speedCondition', '__httpwww_fixm_aerobase3_0_SpeedType_speedCondition', _module_typeBindings.SpeedConditionType)
    __speedCondition._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 644, 12)
    __speedCondition._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 644, 12)
    
    speedCondition = property(__speedCondition.value, __speedCondition.set, None, '\n                     The speed condition indicates whether the aircraft will be maintaining, exceeding, \n                     or flying more slowly than the assigned boundary crossing speed. \n                  ')

    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AirspeedInIasOrMachType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __speedCondition.name() : __speedCondition
    })
_module_typeBindings.SpeedType = SpeedType
Namespace.addCategoryObject('typeBinding', 'SpeedType', SpeedType)


# Complex type {http://www.fixm.aero/base/3.0}DirectionType with content type SIMPLE
class DirectionType (_ImportedBinding__ff.AngleType):
    """
            Represents a compass bearing as an angle in the range [0,360]. 
         """
    _TypeDefinition = _ImportedBinding__ff.RestrictedAngleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DirectionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 78, 3)
    _ElementMap = _ImportedBinding__ff.AngleType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AngleType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AngleType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_fixm_aerobase3_0_DirectionType_ref', _module_typeBindings.DirectionReferenceType)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 86, 12)
    __ref._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 86, 12)
    
    ref = property(__ref.value, __ref.set, None, '\n                     Optional reference to DirectionReference. \n                  ')

    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AngleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
_module_typeBindings.DirectionType = DirectionType
Namespace.addCategoryObject('typeBinding', 'DirectionType', DirectionType)


AerodromeReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AerodromeReference'), AerodromeReferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 93, 3))
Namespace.addCategoryObject('elementBinding', AerodromeReference.name().localName(), AerodromeReference)

SignificantPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SignificantPoint'), SignificantPointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 202, 3))
Namespace.addCategoryObject('elementBinding', SignificantPoint.name().localName(), SignificantPoint)

MultiTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiTime'), MultiTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 151, 3))
Namespace.addCategoryObject('elementBinding', MultiTime.name().localName(), MultiTime)

TimeSequence = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeSequence'), TimeSequenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 253, 3))
Namespace.addCategoryObject('elementBinding', TimeSequence.name().localName(), TimeSequence)

AirspeedChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AirspeedChoice'), AirspeedChoiceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 112, 3))
Namespace.addCategoryObject('elementBinding', AirspeedChoice.name().localName(), AirspeedChoice)

AirspeedRange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AirspeedRange'), AirspeedRangeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 137, 3))
Namespace.addCategoryObject('elementBinding', AirspeedRange.name().localName(), AirspeedRange)

AltitudeChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltitudeChoice'), AltitudeChoiceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 190, 3))
Namespace.addCategoryObject('elementBinding', AltitudeChoice.name().localName(), AltitudeChoice)

GroundspeedChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroundspeedChoice'), GroundspeedChoiceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 401, 3))
Namespace.addCategoryObject('elementBinding', GroundspeedChoice.name().localName(), GroundspeedChoice)

GroundspeedRange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroundspeedRange'), GroundspeedRangeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 427, 3))
Namespace.addCategoryObject('elementBinding', GroundspeedRange.name().localName(), GroundspeedRange)

NameValueList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NameValueList'), NameValueListType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 487, 3))
Namespace.addCategoryObject('elementBinding', NameValueList.name().localName(), NameValueList)

VerticalRange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VerticalRange'), VerticalRangeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 751, 3))
Namespace.addCategoryObject('elementBinding', VerticalRange.name().localName(), VerticalRange)

IcaoAerodromeReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IcaoAerodromeReference'), IcaoAerodromeReferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 113, 3))
Namespace.addCategoryObject('elementBinding', IcaoAerodromeReference.name().localName(), IcaoAerodromeReference)

RunwayPositionAndTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunwayPositionAndTime'), RunwayPositionAndTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 138, 3))
Namespace.addCategoryObject('elementBinding', RunwayPositionAndTime.name().localName(), RunwayPositionAndTime)

StandPositionAndTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StandPositionAndTime'), StandPositionAndTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 182, 3))
Namespace.addCategoryObject('elementBinding', StandPositionAndTime.name().localName(), StandPositionAndTime)

UnlistedAerodromeReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnlistedAerodromeReference'), UnlistedAerodromeReferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 221, 3))
Namespace.addCategoryObject('elementBinding', UnlistedAerodromeReference.name().localName(), UnlistedAerodromeReference)

AtcUnitReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AtcUnitReference'), AtcUnitReferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 102, 3))
Namespace.addCategoryObject('elementBinding', AtcUnitReference.name().localName(), AtcUnitReference)

Feature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Feature'), FeatureType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Feature.xsd', 105, 3))
Namespace.addCategoryObject('elementBinding', Feature.name().localName(), Feature)

FixPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FixPoint'), FixPointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 140, 3))
Namespace.addCategoryObject('elementBinding', FixPoint.name().localName(), FixPoint)

LocationPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocationPoint'), LocationPointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 163, 3))
Namespace.addCategoryObject('elementBinding', LocationPoint.name().localName(), LocationPoint)

ReportedTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReportedTime'), ReportedTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 176, 3))
Namespace.addCategoryObject('elementBinding', ReportedTime.name().localName(), ReportedTime)

TargetMultiTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TargetMultiTime'), TargetMultiTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 199, 3))
Namespace.addCategoryObject('elementBinding', TargetMultiTime.name().localName(), TargetMultiTime)

LateralOfftrack = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LateralOfftrack'), LateralOfftrackType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 465, 3))
Namespace.addCategoryObject('elementBinding', LateralOfftrack.name().localName(), LateralOfftrack)

OfftrackDistance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OfftrackDistance'), OfftrackDistanceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 565, 3))
Namespace.addCategoryObject('elementBinding', OfftrackDistance.name().localName(), OfftrackDistance)

IdentifiedUnitReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentifiedUnitReference'), IdentifiedUnitReferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 151, 3))
Namespace.addCategoryObject('elementBinding', IdentifiedUnitReference.name().localName(), IdentifiedUnitReference)

UnknownUnitReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnknownUnitReference'), UnknownUnitReferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 189, 3))
Namespace.addCategoryObject('elementBinding', UnknownUnitReference.name().localName(), UnknownUnitReference)

Extension = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extension'), ExtensionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Extension.xsd', 89, 3))
Namespace.addCategoryObject('elementBinding', Extension.name().localName(), Extension)

RelativePoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelativePoint'), RelativePointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 192, 3))
Namespace.addCategoryObject('elementBinding', RelativePoint.name().localName(), RelativePoint)

ExtendedMultiTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtendedMultiTime'), ExtendedMultiTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 109, 3))
Namespace.addCategoryObject('elementBinding', ExtendedMultiTime.name().localName(), ExtendedMultiTime)

NameValuePair = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NameValuePair'), NameValuePairType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 527, 3))
Namespace.addCategoryObject('elementBinding', NameValuePair.name().localName(), NameValuePair)



MultiTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'actual'), ReportedTimeType, scope=MultiTimeType, documentation='\n                  Time at which the event is observed to occur \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9)))

MultiTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'estimated'), ReportedTimeType, scope=MultiTimeType, documentation='\n                  Time at which the event is estimated to occur \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'actual')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'estimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MultiTimeType._Automaton = _BuildAutomaton()




TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'approval'), TargetMultiTimeType, scope=TimeSequenceType, documentation='\n                  Step 2 of the TimeSequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 216, 9)))

TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'begin'), MultiTimeType, scope=TimeSequenceType, documentation='\n                  Step 4 of the TimeSequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 223, 9)))

TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'end'), MultiTimeType, scope=TimeSequenceType, documentation='\n                  Step 5 of the TimeSequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 230, 9)))

TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ready'), MultiTimeType, scope=TimeSequenceType, documentation='\n                  Step 3 of the TimeSequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 237, 9)))

TimeSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'request'), MultiTimeType, scope=TimeSequenceType, documentation='\n                  Step 1 of the TimeSequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 244, 9)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 216, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 223, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 230, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 237, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 244, 9))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'approval')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 216, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'begin')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 223, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'end')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 230, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'ready')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 237, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TimeSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'request')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 244, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TimeSequenceType._Automaton = _BuildAutomaton_()




AirspeedChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airspeed'), SpeedType, scope=AirspeedChoiceType, documentation='\n                  The airspeed can be expressed as a specific speed with a condition. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 96, 9)))

AirspeedChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airspeedRange'), AirspeedRangeType, scope=AirspeedChoiceType, documentation='\n                  The airspeed that can be expressed as a range between a lower and upper bound. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 103, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 96, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 103, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AirspeedChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'airspeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 96, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AirspeedChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'airspeedRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 103, 9))
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
AirspeedChoiceType._Automaton = _BuildAutomaton_2()




AirspeedRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lowerSpeed'), _ImportedBinding__ff.AirspeedInIasOrMachType, scope=AirspeedRangeType, documentation='\n                  Lower bound of the speed range. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 121, 9)))

AirspeedRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upperSpeed'), _ImportedBinding__ff.AirspeedInIasOrMachType, scope=AirspeedRangeType, documentation='\n                  Upper bound of the speed range \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 128, 9)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 121, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 128, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AirspeedRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'lowerSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 121, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AirspeedRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'upperSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 128, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AirspeedRangeType._Automaton = _BuildAutomaton_3()




AltitudeChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altitude'), _ImportedBinding__ff.AltitudeType, scope=AltitudeChoiceType, documentation='\n                  Altitude expressed as a specific altitude. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 174, 9)))

AltitudeChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altitudeRange'), VerticalRangeType, scope=AltitudeChoiceType, documentation='\n                  Altitude that can be expressed as a range between a lower and upper bound. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 181, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 174, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 181, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AltitudeChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 174, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AltitudeChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitudeRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 181, 9))
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
AltitudeChoiceType._Automaton = _BuildAutomaton_4()




GroundspeedChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'groundspeed'), _ImportedBinding__ff.GroundspeedType, scope=GroundspeedChoiceType, documentation='\n                  Groundspeed can be expressed as a specific speed. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 384, 9)))

GroundspeedChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'groundspeedRange'), GroundspeedRangeType, scope=GroundspeedChoiceType, documentation='\n                  The groundspeed that can be expressed as a range between a lower and upper bound. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 391, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 384, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 391, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroundspeedChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'groundspeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 384, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GroundspeedChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'groundspeedRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 391, 9))
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
GroundspeedChoiceType._Automaton = _BuildAutomaton_5()




GroundspeedRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lowerSpeed'), _ImportedBinding__ff.GroundspeedType, scope=GroundspeedRangeType, documentation='\n                  Lower bound of the groundspeed range. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 411, 9)))

GroundspeedRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upperSpeed'), _ImportedBinding__ff.GroundspeedType, scope=GroundspeedRangeType, documentation='\n                  Upper bound of the sroundspeed range. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 418, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 411, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 418, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroundspeedRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'lowerSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 411, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GroundspeedRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'upperSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 418, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GroundspeedRangeType._Automaton = _BuildAutomaton_6()




NameValueListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nameValue'), NameValuePairType, scope=NameValueListType, documentation='\n                  A set of up to 10 name-value pairs. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 478, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=10, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 478, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NameValueListType._UseForTag(pyxb.namespace.ExpandedName(None, 'nameValue')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 478, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NameValueListType._Automaton = _BuildAutomaton_7()




VerticalRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lowerBound'), _ImportedBinding__ff.AltitudeType, scope=VerticalRangeType, documentation='\n                  Lower bound altitude of the vertical range. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 735, 9)))

VerticalRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upperBound'), _ImportedBinding__ff.AltitudeType, scope=VerticalRangeType, documentation='\n                  Upper bound altitude of the vertical range. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 742, 9)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 735, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 742, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VerticalRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'lowerBound')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 735, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(VerticalRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'upperBound')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 742, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VerticalRangeType._Automaton = _BuildAutomaton_8()




RunwayPositionAndTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'runwayTime'), ExtendedMultiTimeType, scope=RunwayPositionAndTimeType, documentation='\n                  Time associated with the specified runway \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 122, 9)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 122, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RunwayPositionAndTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 122, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RunwayPositionAndTimeType._Automaton = _BuildAutomaton_9()




StandPositionAndTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'standTime'), ExtendedMultiTimeType, scope=StandPositionAndTimeType, documentation='\n                  Represents a time at the stand. Either departure time from the stand or arrival time \n                  to the stand depending on the context in which it is used. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 158, 9)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 158, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StandPositionAndTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'standTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 158, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StandPositionAndTimeType._Automaton = _BuildAutomaton_10()




UnlistedAerodromeReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), SignificantPointType, scope=UnlistedAerodromeReferenceType, documentation="\n                        A significant point consisting of the aerodrome's \n                        * geographic location (latitude and longitude) OR \n                        * the first significant point of a flight route OR \n                        * fix/radial/offset from a known waypoint. \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 199, 15)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 199, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnlistedAerodromeReferenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Aerodrome.xsd', 199, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UnlistedAerodromeReferenceType._Automaton = _BuildAutomaton_11()




LocationPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), _ImportedBinding__ff.GeographicLocationType, scope=LocationPointType, documentation='\n                        One of three possibilities, "location" provides the fix/waypoint of this Significant \n                        Point. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 151, 15)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 151, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LocationPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 151, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LocationPointType._Automaton = _BuildAutomaton_12()




TargetMultiTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'target'), ReportedTimeType, scope=TargetMultiTimeType, documentation='\n                        Time estimate by qualified personnel \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 188, 15)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 188, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TargetMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'actual')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TargetMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'estimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TargetMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'target')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 188, 15))
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
TargetMultiTimeType._Automaton = _BuildAutomaton_13()




LateralOfftrackType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offtrackDistance'), OfftrackDistanceType, scope=LateralOfftrackType, documentation='\n                  Represents offtrack distances that are lateral relative to a location expressed by \n                  a distance measurement and offset direction. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 448, 9)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 448, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LateralOfftrackType._UseForTag(pyxb.namespace.ExpandedName(None, 'offtrackDistance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 448, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LateralOfftrackType._Automaton = _BuildAutomaton_14()




OfftrackDistanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distance'), _ImportedBinding__ff.DistanceType, scope=OfftrackDistanceType, documentation='\n                  Specifies the distance of the offtrack. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 549, 9)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 549, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OfftrackDistanceType._UseForTag(pyxb.namespace.ExpandedName(None, 'distance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Types.xsd', 549, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OfftrackDistanceType._Automaton = _BuildAutomaton_15()




UnknownUnitReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'unitLocation'), _ImportedBinding__ff.GeographicLocationType, scope=UnknownUnitReferenceType, documentation='\n                        Location by latitude and longitude. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 171, 15)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 171, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnknownUnitReferenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'unitLocation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Airspace.xsd', 171, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UnknownUnitReferenceType._Automaton = _BuildAutomaton_16()




RelativePointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distance'), _ImportedBinding__ff.DistanceType, scope=RelativePointType, documentation='\n                        The distance from a known waypoint/fix. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 174, 15)))

RelativePointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radial'), DirectionType, scope=RelativePointType, documentation='\n                        The radius from a known fix/waypoint. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 181, 15)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 174, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 181, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelativePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'distance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 174, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RelativePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'radial')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Location.xsd', 181, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelativePointType._Automaton = _BuildAutomaton_17()




ExtendedMultiTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'controlled'), ReportedTimeType, nillable=pyxb.binding.datatypes.boolean(1), scope=ExtendedMultiTimeType, documentation='\n                        Time specified by the controller of control program \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 91, 15)))

ExtendedMultiTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'initial'), ReportedTimeType, scope=ExtendedMultiTimeType, documentation='\n                        Time as first specified in the flight plan \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 98, 15)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 188, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 91, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 98, 15))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExtendedMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'actual')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 135, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExtendedMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'estimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 142, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExtendedMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'target')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 188, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ExtendedMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'controlled')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 91, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ExtendedMultiTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'initial')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\base\\Time.xsd', 98, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExtendedMultiTimeType._Automaton = _BuildAutomaton_18()


IcaoAerodromeReference._setSubstitutionGroup(AerodromeReference)

UnlistedAerodromeReference._setSubstitutionGroup(AerodromeReference)

FixPoint._setSubstitutionGroup(SignificantPoint)

LocationPoint._setSubstitutionGroup(SignificantPoint)

TargetMultiTime._setSubstitutionGroup(MultiTime)

IdentifiedUnitReference._setSubstitutionGroup(AtcUnitReference)

UnknownUnitReference._setSubstitutionGroup(AtcUnitReference)

Extension._setSubstitutionGroup(Feature)

RelativePoint._setSubstitutionGroup(SignificantPoint)

ExtendedMultiTime._setSubstitutionGroup(MultiTime)
