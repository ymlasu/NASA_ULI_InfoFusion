# .\smes3\smes3.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a1be4bff0efa31d321d6ddc81efa3701a7e10fbf
# Generated 2018-10-25 13:10:06.843371 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:33ce3cbe-d881-11e8-9546-ecb1d75f2e16')

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
import smes3._common as _ImportedBinding_smes3__common
import smes3._smestypes as _ImportedBinding_smes3__smestypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent', create_if_missing=True)
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


# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}timeType
class timeType (pyxb.binding.datatypes.dateTime):

    """The time at which the message was produced """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 33, 1)
    _Documentation = 'The time at which the message was produced '
timeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'timeType', timeType)
_module_typeBindings.timeType = timeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}trackType
class trackType (pyxb.binding.datatypes.short):

    """Track Number"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'trackType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 40, 1)
    _Documentation = 'Track Number'
trackType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=trackType, value=pyxb.binding.datatypes.short(0))
trackType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=trackType, value=pyxb.binding.datatypes.short(4095))
trackType._InitializeFacetMap(trackType._CF_minInclusive,
   trackType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'trackType', trackType)
_module_typeBindings.trackType = trackType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 50, 1)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='[0-7]{4,4}|ANON')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}latitudeType
class latitudeType (pyxb.binding.datatypes.double):

    """Latitude [Decimal Degrees]"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'latitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 96, 1)
    _Documentation = 'Latitude [Decimal Degrees]'
latitudeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=latitudeType, value=pyxb.binding.datatypes.double(-90.0))
latitudeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=latitudeType, value=pyxb.binding.datatypes.double(90.0))
latitudeType._InitializeFacetMap(latitudeType._CF_minInclusive,
   latitudeType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'latitudeType', latitudeType)
_module_typeBindings.latitudeType = latitudeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}longitudeType
class longitudeType (pyxb.binding.datatypes.double):

    """Longitude [Decimal Degrees]"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 106, 1)
    _Documentation = 'Longitude [Decimal Degrees]'
longitudeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=longitudeType, value=pyxb.binding.datatypes.double(-180.0))
longitudeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=longitudeType, value=pyxb.binding.datatypes.double(180.0))
longitudeType._InitializeFacetMap(longitudeType._CF_minInclusive,
   longitudeType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'longitudeType', longitudeType)
_module_typeBindings.longitudeType = longitudeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}rangeType
class rangeType (pyxb.binding.datatypes.unsignedShort):

    """Target Range"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 125, 1)
    _Documentation = 'Target Range'
rangeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=rangeType, value=pyxb.binding.datatypes.unsignedShort(0))
rangeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=rangeType, value=pyxb.binding.datatypes.unsignedShort(65535))
rangeType._InitializeFacetMap(rangeType._CF_minInclusive,
   rangeType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'rangeType', rangeType)
_module_typeBindings.rangeType = rangeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}azimuthType
class azimuthType (pyxb.binding.datatypes.double):

    """Target Azimuth"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'azimuthType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 135, 1)
    _Documentation = 'Target Azimuth'
azimuthType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=azimuthType, value=pyxb.binding.datatypes.double(0.0))
azimuthType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=azimuthType, value=pyxb.binding.datatypes.double(360.0))
azimuthType._InitializeFacetMap(azimuthType._CF_minInclusive,
   azimuthType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'azimuthType', azimuthType)
_module_typeBindings.azimuthType = azimuthType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}bitType
class bitType (pyxb.binding.datatypes.unsignedShort):

    """Bit-Field Entry [0 = False, 1 = True]
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bitType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 145, 1)
    _Documentation = 'Bit-Field Entry [0 = False, 1 = True]\n\t\t\t'
bitType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=bitType, value=pyxb.binding.datatypes.unsignedShort(0))
bitType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=bitType, value=pyxb.binding.datatypes.unsignedShort(1))
bitType._InitializeFacetMap(bitType._CF_minInclusive,
   bitType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'bitType', bitType)
_module_typeBindings.bitType = bitType

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 156, 1)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.new = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='new', tag='new')
STD_ANON_.confirmed = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='confirmed', tag='confirmed')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 168, 1)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.n0 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
STD_ANON_2.n1 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
STD_ANON_2.n2 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
STD_ANON_2.n3 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 182, 1)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.hexBinary):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 204, 1)
    _Documentation = None
STD_ANON_4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_minLength,
   STD_ANON_4._CF_maxLength)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 216, 1)
    _Documentation = None
STD_ANON_5._InitializeFacetMap()
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 226, 1)
    _Documentation = None
STD_ANON_6._InitializeFacetMap()
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 236, 1)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.undetermined = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='undetermined', tag='undetermined')
STD_ANON_7.aircraft = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='aircraft', tag='aircraft')
STD_ANON_7.surface = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='surface', tag='surface')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableAttrType
class removableAttrType (pyxb.binding.datatypes.short):

    """Used to indicate an element is no longer present in an ASDE-X message when sending deltas [1 = removed]
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableAttrType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 311, 1)
    _Documentation = 'Used to indicate an element is no longer present in an ASDE-X message when sending deltas [1 = removed]\n\t\t\t'
removableAttrType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=removableAttrType, value=pyxb.binding.datatypes.short(1))
removableAttrType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=removableAttrType, value=pyxb.binding.datatypes.short(1))
removableAttrType._InitializeFacetMap(removableAttrType._CF_minInclusive,
   removableAttrType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'removableAttrType', removableAttrType)
_module_typeBindings.removableAttrType = removableAttrType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}RDPSourceType
class RDPSourceType (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RDPSourceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 80, 1)
    _Documentation = None
RDPSourceType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=RDPSourceType, value=pyxb.binding.datatypes.unsignedShort(0))
RDPSourceType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RDPSourceType, value=pyxb.binding.datatypes.unsignedShort(1))
RDPSourceType._InitializeFacetMap(RDPSourceType._CF_minInclusive,
   RDPSourceType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'RDPSourceType', RDPSourceType)
_module_typeBindings.RDPSourceType = RDPSourceType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiFlightPlanInterfaceType
class gfiFlightPlanInterfaceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Flight Plan Interface Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiFlightPlanInterfaceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 20, 1)
    _Documentation = 'Flight Plan Interface Type'
gfiFlightPlanInterfaceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=gfiFlightPlanInterfaceType, enum_prefix=None)
gfiFlightPlanInterfaceType.artsiiia = gfiFlightPlanInterfaceType._CF_enumeration.addEnumeration(unicode_value='artsiiia', tag='artsiiia')
gfiFlightPlanInterfaceType.artsiiie = gfiFlightPlanInterfaceType._CF_enumeration.addEnumeration(unicode_value='artsiiie', tag='artsiiie')
gfiFlightPlanInterfaceType.stars = gfiFlightPlanInterfaceType._CF_enumeration.addEnumeration(unicode_value='stars', tag='stars')
gfiFlightPlanInterfaceType.gfp = gfiFlightPlanInterfaceType._CF_enumeration.addEnumeration(unicode_value='gfp', tag='gfp')
gfiFlightPlanInterfaceType.microearts = gfiFlightPlanInterfaceType._CF_enumeration.addEnumeration(unicode_value='microearts', tag='microearts')
gfiFlightPlanInterfaceType._InitializeFacetMap(gfiFlightPlanInterfaceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'gfiFlightPlanInterfaceType', gfiFlightPlanInterfaceType)
_module_typeBindings.gfiFlightPlanInterfaceType = gfiFlightPlanInterfaceType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiFlightType
class gfiFlightType (pyxb.binding.datatypes.string):

    """Identifies flight as arrival [A], departure [P] or
				enroute [E] (STARS) or a numeric indicator (IIIE/GFP)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiFlightType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 32, 1)
    _Documentation = 'Identifies flight as arrival [A], departure [P] or\n\t\t\t\tenroute [E] (STARS) or a numeric indicator (IIIE/GFP)'
gfiFlightType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'gfiFlightType', gfiFlightType)
_module_typeBindings.gfiFlightType = gfiFlightType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiAircraftId
class gfiAircraftId (pyxb.binding.datatypes.string):

    """Call Sign"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiAircraftId')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 50, 1)
    _Documentation = 'Call Sign'
gfiAircraftId._CF_pattern = pyxb.binding.facets.CF_pattern()
gfiAircraftId._CF_pattern.addPattern(pattern='[A-Z][0-9A-Z]{1,6}')
gfiAircraftId._InitializeFacetMap(gfiAircraftId._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'gfiAircraftId', gfiAircraftId)
_module_typeBindings.gfiAircraftId = gfiAircraftId

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiMode3ACodeType
class gfiMode3ACodeType (pyxb.binding.datatypes.string):

    """Mode 3/A Code"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiMode3ACodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 58, 1)
    _Documentation = 'Mode 3/A Code'
gfiMode3ACodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
gfiMode3ACodeType._CF_pattern.addPattern(pattern='[0-7]{4,4}')
gfiMode3ACodeType._InitializeFacetMap(gfiMode3ACodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'gfiMode3ACodeType', gfiMode3ACodeType)
_module_typeBindings.gfiMode3ACodeType = gfiMode3ACodeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiAcTypeType
class gfiAcTypeType (pyxb.binding.datatypes.string):

    """Aircraft Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiAcTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 91, 1)
    _Documentation = 'Aircraft Type'
gfiAcTypeType._CF_pattern = pyxb.binding.facets.CF_pattern()
gfiAcTypeType._CF_pattern.addPattern(pattern='[A-Z][0-9A-Z]{1,3}')
gfiAcTypeType._InitializeFacetMap(gfiAcTypeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'gfiAcTypeType', gfiAcTypeType)
_module_typeBindings.gfiAcTypeType = gfiAcTypeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiCategoryType
class gfiCategoryType (pyxb.binding.datatypes.string):

    """Aircraft Category"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 99, 1)
    _Documentation = 'Aircraft Category'
gfiCategoryType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiCategoryType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiCategoryType._InitializeFacetMap(gfiCategoryType._CF_minLength,
   gfiCategoryType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiCategoryType', gfiCategoryType)
_module_typeBindings.gfiCategoryType = gfiCategoryType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiFlightRulesType
class gfiFlightRulesType (pyxb.binding.datatypes.string):

    """Aircraft Flight Rules"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiFlightRulesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 108, 1)
    _Documentation = 'Aircraft Flight Rules'
gfiFlightRulesType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiFlightRulesType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiFlightRulesType._InitializeFacetMap(gfiFlightRulesType._CF_minLength,
   gfiFlightRulesType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiFlightRulesType', gfiFlightRulesType)
_module_typeBindings.gfiFlightRulesType = gfiFlightRulesType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiFixType
class gfiFixType (pyxb.binding.datatypes.string):

    """Paired Fix"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiFixType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 117, 1)
    _Documentation = 'Paired Fix'
gfiFixType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiFixType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
gfiFixType._InitializeFacetMap(gfiFixType._CF_minLength,
   gfiFixType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiFixType', gfiFixType)
_module_typeBindings.gfiFixType = gfiFixType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiRunwayType
class gfiRunwayType (pyxb.binding.datatypes.string):

    """Assigned Runway"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiRunwayType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 126, 1)
    _Documentation = 'Assigned Runway'
gfiRunwayType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiRunwayType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
gfiRunwayType._InitializeFacetMap(gfiRunwayType._CF_minLength,
   gfiRunwayType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiRunwayType', gfiRunwayType)
_module_typeBindings.gfiRunwayType = gfiRunwayType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiAirportType
class gfiAirportType (pyxb.binding.datatypes.string):

    """Origin or Destination Airport"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiAirportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 135, 1)
    _Documentation = 'Origin or Destination Airport'
gfiAirportType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
gfiAirportType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
gfiAirportType._InitializeFacetMap(gfiAirportType._CF_minLength,
   gfiAirportType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiAirportType', gfiAirportType)
_module_typeBindings.gfiAirportType = gfiAirportType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiScratchPad1Type
class gfiScratchPad1Type (pyxb.binding.datatypes.string):

    """Scratchpad 1 Data"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiScratchPad1Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 144, 1)
    _Documentation = 'Scratchpad 1 Data'
gfiScratchPad1Type._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiScratchPad1Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
gfiScratchPad1Type._InitializeFacetMap(gfiScratchPad1Type._CF_minLength,
   gfiScratchPad1Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiScratchPad1Type', gfiScratchPad1Type)
_module_typeBindings.gfiScratchPad1Type = gfiScratchPad1Type

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiScratchPad2Type
class gfiScratchPad2Type (pyxb.binding.datatypes.string):

    """Scratchpad 2 Data"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiScratchPad2Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 153, 1)
    _Documentation = 'Scratchpad 2 Data'
gfiScratchPad2Type._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
gfiScratchPad2Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
gfiScratchPad2Type._InitializeFacetMap(gfiScratchPad2Type._CF_minLength,
   gfiScratchPad2Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'gfiScratchPad2Type', gfiScratchPad2Type)
_module_typeBindings.gfiScratchPad2Type = gfiScratchPad2Type

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}airportType
class airportType (pyxb.binding.datatypes.string):

    """The airport at which this message was produced
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'airportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 10, 1)
    _Documentation = 'The airport at which this message was produced\n\t\t\t'
airportType._CF_pattern = pyxb.binding.facets.CF_pattern()
airportType._CF_pattern.addPattern(pattern='[A-Z]{4,4}')
airportType._InitializeFacetMap(airportType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'airportType', airportType)
_module_typeBindings.airportType = airportType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}seqNumType
class seqNumType (pyxb.binding.datatypes.int):

    """ASDE-X sequence number
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'seqNumType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 51, 1)
    _Documentation = 'ASDE-X sequence number\n\t\t\t'
seqNumType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'seqNumType', seqNumType)
_module_typeBindings.seqNumType = seqNumType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}stidType
class stidType (pyxb.binding.datatypes.long):

    """STDDS track id"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stidType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 58, 1)
    _Documentation = 'STDDS track id'
stidType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stidType', stidType)
_module_typeBindings.stidType = stidType

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 79, 1)
    _Documentation = None
STD_ANON_8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_minLength,
   STD_ANON_8._CF_maxLength)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 105, 1)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.unknown = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_9.aircraft = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='aircraft', tag='aircraft')
STD_ANON_9.vehicle = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='vehicle', tag='vehicle')
STD_ANON_9.unknown_aircraft = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='unknown_aircraft', tag='unknown_aircraft')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 118, 1)
    _Documentation = None
STD_ANON_10._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_minLength,
   STD_ANON_10._CF_maxLength)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 129, 1)
    _Documentation = None
STD_ANON_11._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_11._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_minLength,
   STD_ANON_11._CF_maxLength)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 140, 1)
    _Documentation = None
STD_ANON_12._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_12._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_minLength,
   STD_ANON_12._CF_maxLength)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 151, 1)
    _Documentation = None
STD_ANON_13._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_13._CF_pattern.addPattern(pattern='(([1-9]|[12][0-9]|3[0-6])[LRC]{0,1})|filtered|unassigned')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_pattern)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 184, 1)
    _Documentation = None
STD_ANON_14._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_14, value=pyxb.binding.datatypes.int(-1159548))
STD_ANON_14._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_14, value=pyxb.binding.datatypes.int(1159548))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_minInclusive,
   STD_ANON_14._CF_maxInclusive)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 196, 2)
    _Documentation = None
STD_ANON_15._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_15, value=pyxb.binding.datatypes.double(-90.0))
STD_ANON_15._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_15, value=pyxb.binding.datatypes.double(90.0))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_minInclusive,
   STD_ANON_15._CF_maxInclusive)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 207, 1)
    _Documentation = None
STD_ANON_16._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_16, value=pyxb.binding.datatypes.double(-180.0))
STD_ANON_16._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_16, value=pyxb.binding.datatypes.double(180.0))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_minInclusive,
   STD_ANON_16._CF_maxInclusive)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 252, 1)
    _Documentation = None
STD_ANON_17._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_17, value=pyxb.binding.datatypes.double(0.0))
STD_ANON_17._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_17, value=pyxb.binding.datatypes.double(360.0))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_minInclusive,
   STD_ANON_17._CF_maxInclusive)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 263, 1)
    _Documentation = None
STD_ANON_18._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_18, value=pyxb.binding.datatypes.double(-8192.0))
STD_ANON_18._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_18, value=pyxb.binding.datatypes.double(8192.0))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_minInclusive,
   STD_ANON_18._CF_maxInclusive)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 275, 1)
    _Documentation = None
STD_ANON_19._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.double(-31.0))
STD_ANON_19._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.double(31.0))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_minInclusive,
   STD_ANON_19._CF_maxInclusive)
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 522, 1)
    _Documentation = None
STD_ANON_20._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_20, value=pyxb.binding.datatypes.short(0))
STD_ANON_20._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_20, value=pyxb.binding.datatypes.short(1))
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_minInclusive,
   STD_ANON_20._CF_maxInclusive)
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 534, 1)
    _Documentation = None
STD_ANON_21._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_21, enum_prefix=None)
STD_ANON_21.barometric = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='barometric', tag='barometric')
STD_ANON_21.geometric = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='geometric', tag='geometric')
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_enumeration)
_module_typeBindings.STD_ANON_21 = STD_ANON_21

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 545, 1)
    _Documentation = None
STD_ANON_22._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_22, enum_prefix=None)
STD_ANON_22.none = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_22.adsb = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='adsb', tag='adsb')
STD_ANON_22.modec = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='modec', tag='modec')
STD_ANON_22.multilat = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='multilat', tag='multilat')
STD_ANON_22.ground = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='ground', tag='ground')
STD_ANON_22.multiple = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value='multiple', tag='multiple')
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_enumeration)
_module_typeBindings.STD_ANON_22 = STD_ANON_22

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 560, 1)
    _Documentation = None
STD_ANON_23._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_23, enum_prefix=None)
STD_ANON_23.unfiltered = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='unfiltered', tag='unfiltered')
STD_ANON_23.filtered = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='filtered', tag='filtered')
STD_ANON_23.highlight = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='highlight', tag='highlight')
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_enumeration)
_module_typeBindings.STD_ANON_23 = STD_ANON_23

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 572, 1)
    _Documentation = None
STD_ANON_24._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_24, enum_prefix=None)
STD_ANON_24.unknown = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_24.onground = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='onground', tag='onground')
STD_ANON_24.arrival = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='arrival', tag='arrival')
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_enumeration)
_module_typeBindings.STD_ANON_24 = STD_ANON_24

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 584, 1)
    _Documentation = None
STD_ANON_25._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_25, value=pyxb.binding.datatypes.short(0))
STD_ANON_25._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_25, value=pyxb.binding.datatypes.short(100))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_minInclusive,
   STD_ANON_25._CF_maxInclusive)
_module_typeBindings.STD_ANON_25 = STD_ANON_25

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 595, 1)
    _Documentation = None
STD_ANON_26._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_26, enum_prefix=None)
STD_ANON_26.adsbicao = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='adsbicao', tag='adsbicao')
STD_ANON_26.adsbsa = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='adsbsa', tag='adsbsa')
STD_ANON_26.tisbicao = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='tisbicao', tag='tisbicao')
STD_ANON_26.tisbtfi = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='tisbtfi', tag='tisbtfi')
STD_ANON_26.vehicle = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='vehicle', tag='vehicle')
STD_ANON_26.beacon = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='beacon', tag='beacon')
STD_ANON_26.emptyString = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='', tag='emptyString')
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_enumeration)
_module_typeBindings.STD_ANON_26 = STD_ANON_26

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 612, 1)
    _Documentation = None
STD_ANON_27._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_27, value=pyxb.binding.datatypes.unsignedShort(0))
STD_ANON_27._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_27, value=pyxb.binding.datatypes.unsignedShort(7))
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_minInclusive,
   STD_ANON_27._CF_maxInclusive)
_module_typeBindings.STD_ANON_27 = STD_ANON_27

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 638, 1)
    _Documentation = None
STD_ANON_28._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_28, enum_prefix=None)
STD_ANON_28.unknown = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
STD_ANON_28.invalid = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='invalid', tag='invalid')
STD_ANON_28.reserved = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='reserved', tag='reserved')
STD_ANON_28.valid = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='valid', tag='valid')
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_enumeration)
_module_typeBindings.STD_ANON_28 = STD_ANON_28

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 652, 1)
    _Documentation = None
STD_ANON_29._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_29, value=pyxb.binding.datatypes.unsignedShort(0))
STD_ANON_29._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_29, value=pyxb.binding.datatypes.unsignedShort(3))
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_minInclusive,
   STD_ANON_29._CF_maxInclusive)
_module_typeBindings.STD_ANON_29 = STD_ANON_29

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 664, 1)
    _Documentation = None
STD_ANON_30._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_30, value=pyxb.binding.datatypes.unsignedShort(0))
STD_ANON_30._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_30, value=pyxb.binding.datatypes.unsignedShort(11))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_minInclusive,
   STD_ANON_30._CF_maxInclusive)
_module_typeBindings.STD_ANON_30 = STD_ANON_30

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 675, 1)
    _Documentation = None
STD_ANON_31._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_31, value=pyxb.binding.datatypes.unsignedShort(0))
STD_ANON_31._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_31, value=pyxb.binding.datatypes.unsignedShort(11))
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_minInclusive,
   STD_ANON_31._CF_maxInclusive)
_module_typeBindings.STD_ANON_31 = STD_ANON_31

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 687, 1)
    _Documentation = None
STD_ANON_32._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_32, enum_prefix=None)
STD_ANON_32.up = STD_ANON_32._CF_enumeration.addEnumeration(unicode_value='up', tag='up')
STD_ANON_32.down = STD_ANON_32._CF_enumeration.addEnumeration(unicode_value='down', tag='down')
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_enumeration)
_module_typeBindings.STD_ANON_32 = STD_ANON_32

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 698, 1)
    _Documentation = None
STD_ANON_33._InitializeFacetMap()
_module_typeBindings.STD_ANON_33 = STD_ANON_33

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 709, 1)
    _Documentation = None
STD_ANON_34._InitializeFacetMap()
_module_typeBindings.STD_ANON_34 = STD_ANON_34

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 720, 1)
    _Documentation = None
STD_ANON_35._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_35, value=pyxb.binding.datatypes.short(0))
STD_ANON_35._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_35, value=pyxb.binding.datatypes.short(26))
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_minInclusive,
   STD_ANON_35._CF_maxInclusive)
_module_typeBindings.STD_ANON_35 = STD_ANON_35

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 731, 1)
    _Documentation = None
STD_ANON_36._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_36, value=pyxb.binding.datatypes.short(101))
STD_ANON_36._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_36, value=pyxb.binding.datatypes.short(276))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_minInclusive,
   STD_ANON_36._CF_maxInclusive)
_module_typeBindings.STD_ANON_36 = STD_ANON_36

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 743, 1)
    _Documentation = None
STD_ANON_37._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_37, value=pyxb.binding.datatypes.short(300))
STD_ANON_37._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_37, value=pyxb.binding.datatypes.short(999))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_minInclusive,
   STD_ANON_37._CF_maxInclusive)
_module_typeBindings.STD_ANON_37 = STD_ANON_37

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 772, 1)
    _Documentation = None
STD_ANON_38._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_38._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_minLength,
   STD_ANON_38._CF_maxLength)
_module_typeBindings.STD_ANON_38 = STD_ANON_38

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 783, 1)
    _Documentation = None
STD_ANON_39._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_39._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_minLength,
   STD_ANON_39._CF_maxLength)
_module_typeBindings.STD_ANON_39 = STD_ANON_39

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 794, 1)
    _Documentation = None
STD_ANON_40._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_minLength,
   STD_ANON_40._CF_maxLength)
_module_typeBindings.STD_ANON_40 = STD_ANON_40

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 824, 1)
    _Documentation = None
STD_ANON_41._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_41, value=pyxb.binding.datatypes.unsignedShort(0))
STD_ANON_41._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_41, value=pyxb.binding.datatypes.unsignedShort(127))
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_minInclusive,
   STD_ANON_41._CF_maxInclusive)
_module_typeBindings.STD_ANON_41 = STD_ANON_41

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 844, 1)
    _Documentation = None
STD_ANON_42._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_42, value=pyxb.binding.datatypes.double(0.0))
STD_ANON_42._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_42, value=pyxb.binding.datatypes.double(360.0))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_minInclusive,
   STD_ANON_42._CF_maxInclusive)
_module_typeBindings.STD_ANON_42 = STD_ANON_42

# Atomic simple type: [anonymous]
class STD_ANON_43 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 855, 1)
    _Documentation = None
STD_ANON_43._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_43, value=pyxb.binding.datatypes.int(0))
STD_ANON_43._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_43, value=pyxb.binding.datatypes.int(14))
STD_ANON_43._InitializeFacetMap(STD_ANON_43._CF_minInclusive,
   STD_ANON_43._CF_maxInclusive)
_module_typeBindings.STD_ANON_43 = STD_ANON_43

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}modeType
class modeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Current System Mode"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'modeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 14, 1)
    _Documentation = 'Current System Mode'
modeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=modeType, enum_prefix=None)
modeType.operational = modeType._CF_enumeration.addEnumeration(unicode_value='operational', tag='operational')
modeType.maintenance = modeType._CF_enumeration.addEnumeration(unicode_value='maintenance', tag='maintenance')
modeType._InitializeFacetMap(modeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'modeType', modeType)
_module_typeBindings.modeType = modeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}stateType
class stateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Current System State"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 23, 1)
    _Documentation = 'Current System State'
stateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stateType, enum_prefix=None)
stateType.online = stateType._CF_enumeration.addEnumeration(unicode_value='online', tag='online')
stateType.degraded = stateType._CF_enumeration.addEnumeration(unicode_value='degraded', tag='degraded')
stateType.offline = stateType._CF_enumeration.addEnumeration(unicode_value='offline', tag='offline')
stateType.startup = stateType._CF_enumeration.addEnumeration(unicode_value='startup', tag='startup')
stateType.shutdown = stateType._CF_enumeration.addEnumeration(unicode_value='shutdown', tag='shutdown')
stateType._InitializeFacetMap(stateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stateType', stateType)
_module_typeBindings.stateType = stateType

# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}basicReportType with content type ELEMENT_ONLY
class basicReportType (pyxb.binding.basis.complexTypeDefinition):
    """ASDEX Track Basic Report """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'basicReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 8, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'time'), 'time', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_basicReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 13, 3), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}track uses Python identifier track
    __track = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'track'), 'track', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_basicReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtrack', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 14, 3), )

    
    track = property(__track.value, __track.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'position'), 'position', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_basicReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventposition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 15, 3), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'velocity'), 'velocity', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_basicReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventvelocity', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 16, 3), )

    
    velocity = property(__velocity.value, __velocity.set, None, None)

    _ElementMap.update({
        __time.name() : __time,
        __track.name() : __track,
        __position.name() : __position,
        __velocity.name() : __velocity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.basicReportType = basicReportType
Namespace.addCategoryObject('typeBinding', 'basicReportType', basicReportType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extendedReportType with content type ELEMENT_ONLY
class extendedReportType (pyxb.binding.basis.complexTypeDefinition):
    """ASDEX Track Extended Report"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}basicReport uses Python identifier basicReport
    __basicReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'basicReport'), 'basicReport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_extendedReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventbasicReport', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 25, 8), )

    
    basicReport = property(__basicReport.value, __basicReport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACode uses Python identifier mode3ACode
    __mode3ACode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), 'mode3ACode', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_extendedReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmode3ACode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 26, 5), )

    
    mode3ACode = property(__mode3ACode.value, __mode3ACode.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acAddress uses Python identifier acAddress
    __acAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acAddress'), 'acAddress', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_extendedReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventacAddress', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 27, 5), )

    
    acAddress = property(__acAddress.value, __acAddress.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}level uses Python identifier level
    __level = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'level'), 'level', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_extendedReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlevel', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 28, 5), )

    
    level = property(__level.value, __level.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'height'), 'height', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_extendedReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventheight', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 29, 5), )

    
    height = property(__height.value, __height.set, None, None)

    _ElementMap.update({
        __basicReport.name() : __basicReport,
        __mode3ACode.name() : __mode3ACode,
        __acAddress.name() : __acAddress,
        __level.name() : __level,
        __height.name() : __height
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.extendedReportType = extendedReportType
Namespace.addCategoryObject('typeBinding', 'extendedReportType', extendedReportType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}callsign uses Python identifier callsign
    __callsign = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'callsign'), 'callsign', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcallsign', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 20, 4), )

    
    callsign = property(__callsign.value, __callsign.set, None, '\n\t\t\t\t\t\t\tFlight Callsign or UNK if not available\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}track uses Python identifier track
    __track = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'track'), 'track', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtrack', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 27, 4), )

    
    track = property(__track.value, __track.set, None, '\n\t\t\t\t\t\t\tFused Track Number\n\t\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}stid uses Python identifier stid
    __stid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stid'), 'stid', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstid', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 34, 4), )

    
    stid = property(__stid.value, __stid.set, None, '\n\t\t\t\t\t\t\tSTDDS Track Id\n\t\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACode uses Python identifier mode3ACode
    __mode3ACode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), 'mode3ACode', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmode3ACode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 41, 4), )

    
    mode3ACode = property(__mode3ACode.value, __mode3ACode.set, None, '\n\t\t\t\t\t\t\tMode 3A code received from ASDE-X\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acAddress uses Python identifier acAddress
    __acAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acAddress'), 'acAddress', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventacAddress', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 48, 4), )

    
    acAddress = property(__acAddress.value, __acAddress.set, None, '\n\t\t\t\t\t\t\tMode S Code received from ASDE-X\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'time'), 'time', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 55, 4), )

    
    time = property(__time.value, __time.set, None, '\n\t\t\t\t\t\t\tTime of the event\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'event'), 'event', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventevent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 62, 4), )

    
    event = property(__event.value, __event.set, None, '\n\t\t\t\t\t\t\tType of event\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'position'), 'position', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventposition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 69, 4), )

    
    position = property(__position.value, __position.set, None, '\n\t\t\t\t\t\t\t2D Position of the target\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altitude'), 'altitude', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 76, 4), )

    
    altitude = property(__altitude.value, __altitude.set, None, '\n\t\t\t\t\t\t\tAltitude in feet\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 83, 4), )

    
    status = property(__status.value, __status.set, None, '\n\t\t\t\t\t\t\tSurface status of the flight\n                        ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}events uses Python identifier events
    __events = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'events'), 'events', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventevents', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 90, 4), )

    
    events = property(__events.value, __events.set, None, '\n\t\t\t\t\t\t\tList of past events\n                        ')

    _ElementMap.update({
        __callsign.name() : __callsign,
        __track.name() : __track,
        __stid.name() : __stid,
        __mode3ACode.name() : __mode3ACode,
        __acAddress.name() : __acAddress,
        __time.name() : __time,
        __event.name() : __event,
        __position.name() : __position,
        __altitude.name() : __altitude,
        __status.name() : __status,
        __events.name() : __events
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}adsbReportType with content type ELEMENT_ONLY
class adsbReportType (pyxb.binding.basis.complexTypeDefinition):
    """ASDEX CAT10 ADSB Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'adsbReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 11, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}report uses Python identifier report
    __report = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'report'), 'report', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventreport', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 16, 8), )

    
    report = property(__report.value, __report.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}descriptor uses Python identifier descriptor
    __descriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptor'), 'descriptor', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdescriptor', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 17, 5), )

    
    descriptor = property(__descriptor.value, __descriptor.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 18, 5), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extent'), 'extent', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventextent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 19, 5), )

    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportType_full', pyxb.binding.datatypes.boolean)
    __full._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 21, 4)
    __full._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 21, 4)
    
    full = property(__full.value, __full.set, None, 'Indicates whether the message is a full update ')

    _ElementMap.update({
        __report.name() : __report,
        __descriptor.name() : __descriptor,
        __status.name() : __status,
        __extent.name() : __extent
    })
    _AttributeMap.update({
        __full.name() : __full
    })
_module_typeBindings.adsbReportType = adsbReportType
Namespace.addCategoryObject('typeBinding', 'adsbReportType', adsbReportType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}adsbTargetDescriptor with content type ELEMENT_ONLY
class adsbTargetDescriptor (pyxb.binding.basis.complexTypeDefinition):
    """ADSB Target Report Descriptor """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'adsbTargetDescriptor')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 28, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}crt uses Python identifier crt
    __crt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crt'), 'crt', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcrt', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 33, 2), )

    
    crt = property(__crt.value, __crt.set, None, 'Default=0; CorruptedReplies=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}dcr uses Python identifier dcr
    __dcr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dcr'), 'dcr', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdcr', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 38, 3), )

    
    dcr = property(__dcr.value, __dcr.set, None, 'Default=0; ADSBDifferentialCorrection=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}rab uses Python identifier rab
    __rab = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rab'), 'rab', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventrab', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 43, 3), )

    
    rab = property(__rab.value, __rab.set, None, 'TargetReport=0; ReferenceTransmitterReport=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}spi uses Python identifier spi
    __spi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spi'), 'spi', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventspi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 48, 3), )

    
    spi = property(__spi.value, __spi.set, None, 'Default=0; SPI present=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gbs uses Python identifier gbs
    __gbs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gbs'), 'gbs', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgbs', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 53, 3), )

    
    gbs = property(__gbs.value, __gbs.set, None, 'Default=0; GroundBitSet=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tot uses Python identifier tot
    __tot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tot'), 'tot', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtot', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 58, 3), )

    
    tot = property(__tot.value, __tot.set, None, '"undetermined", "aircraft", "surface"')

    _ElementMap.update({
        __crt.name() : __crt,
        __dcr.name() : __dcr,
        __rab.name() : __rab,
        __spi.name() : __spi,
        __gbs.name() : __gbs,
        __tot.name() : __tot
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.adsbTargetDescriptor = adsbTargetDescriptor
Namespace.addCategoryObject('typeBinding', 'adsbTargetDescriptor', adsbTargetDescriptor)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mlatReportType with content type ELEMENT_ONLY
class mlatReportType (pyxb.binding.basis.complexTypeDefinition):
    """ASDEX CAT10 MLAT Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mlatReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 11, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}report uses Python identifier report
    __report = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'report'), 'report', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventreport', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 16, 3), )

    
    report = property(__report.value, __report.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}descriptor uses Python identifier descriptor
    __descriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptor'), 'descriptor', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdescriptor', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 17, 3), )

    
    descriptor = property(__descriptor.value, __descriptor.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 18, 3), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extent'), 'extent', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventextent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 19, 3), )

    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportType_full', pyxb.binding.datatypes.boolean)
    __full._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 21, 2)
    __full._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 21, 2)
    
    full = property(__full.value, __full.set, None, 'Indicates whether the message is a full update ')

    _ElementMap.update({
        __report.name() : __report,
        __descriptor.name() : __descriptor,
        __status.name() : __status,
        __extent.name() : __extent
    })
    _AttributeMap.update({
        __full.name() : __full
    })
_module_typeBindings.mlatReportType = mlatReportType
Namespace.addCategoryObject('typeBinding', 'mlatReportType', mlatReportType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mlatTargetDescriptor with content type ELEMENT_ONLY
class mlatTargetDescriptor (pyxb.binding.basis.complexTypeDefinition):
    """SMR Target Report Descriptor """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mlatTargetDescriptor')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 28, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}crt uses Python identifier crt
    __crt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crt'), 'crt', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcrt', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 33, 2), )

    
    crt = property(__crt.value, __crt.set, None, 'Default=0; CorruptedReplies=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}rab uses Python identifier rab
    __rab = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rab'), 'rab', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventrab', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 38, 3), )

    
    rab = property(__rab.value, __rab.set, None, 'TargetReport=0; ReferenceTransmitterReport=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}spi uses Python identifier spi
    __spi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spi'), 'spi', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventspi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 43, 3), )

    
    spi = property(__spi.value, __spi.set, None, 'Default=0; SPI present=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gbs uses Python identifier gbs
    __gbs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gbs'), 'gbs', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgbs', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 48, 3), )

    
    gbs = property(__gbs.value, __gbs.set, None, 'Default=0; GroundBitSet=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tot uses Python identifier tot
    __tot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tot'), 'tot', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtot', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 53, 3), )

    
    tot = property(__tot.value, __tot.set, None, '"undetermined", "aircraft", ""surface"')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatTargetDescriptor_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtype', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 58, 3), )

    
    type = property(__type.value, __type.set, None, 'ATCRBS=0; UAT=1')

    _ElementMap.update({
        __crt.name() : __crt,
        __rab.name() : __rab,
        __spi.name() : __spi,
        __gbs.name() : __gbs,
        __tot.name() : __tot,
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.mlatTargetDescriptor = mlatTargetDescriptor
Namespace.addCategoryObject('typeBinding', 'mlatTargetDescriptor', mlatTargetDescriptor)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrReportType with content type ELEMENT_ONLY
class smrReportType (pyxb.binding.basis.complexTypeDefinition):
    """ASDEX CAT10 SMR Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smrReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 11, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}report uses Python identifier report
    __report = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'report'), 'report', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventreport', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 16, 4), )

    
    report = property(__report.value, __report.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}rdpSource uses Python identifier rdpSource
    __rdpSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rdpSource'), 'rdpSource', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventrdpSource', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 17, 4), )

    
    rdpSource = property(__rdpSource.value, __rdpSource.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extent'), 'extent', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventextent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 18, 4), )

    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 19, 4), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportType_full', pyxb.binding.datatypes.boolean)
    __full._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 21, 3)
    __full._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 21, 3)
    
    full = property(__full.value, __full.set, None, 'Indicates whether the message is a full update ')

    _ElementMap.update({
        __report.name() : __report,
        __rdpSource.name() : __rdpSource,
        __extent.name() : __extent,
        __status.name() : __status
    })
    _AttributeMap.update({
        __full.name() : __full
    })
_module_typeBindings.smrReportType = smrReportType
Namespace.addCategoryObject('typeBinding', 'smrReportType', smrReportType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """An ASDE-X Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}airport uses Python identifier airport
    __airport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'airport'), 'airport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventairport', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 17, 4), )

    
    airport = property(__airport.value, __airport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}positionReport uses Python identifier positionReport
    __positionReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'positionReport'), 'positionReport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventpositionReport', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 19, 5), )

    
    positionReport = property(__positionReport.value, __positionReport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}adsbReport uses Python identifier adsbReport
    __adsbReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adsbReport'), 'adsbReport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventadsbReport', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 21, 5), )

    
    adsbReport = property(__adsbReport.value, __adsbReport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mlatReport uses Python identifier mlatReport
    __mlatReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mlatReport'), 'mlatReport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmlatReport', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 22, 5), )

    
    mlatReport = property(__mlatReport.value, __mlatReport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrReport uses Python identifier smrReport
    __smrReport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'smrReport'), 'smrReport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsmrReport', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 23, 5), )

    
    smrReport = property(__smrReport.value, __smrReport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}genericFlightInfo uses Python identifier genericFlightInfo
    __genericFlightInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genericFlightInfo'), 'genericFlightInfo', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgenericFlightInfo', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 24, 5), )

    
    genericFlightInfo = property(__genericFlightInfo.value, __genericFlightInfo.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}systemStatus uses Python identifier systemStatus
    __systemStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'systemStatus'), 'systemStatus', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsystemStatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 25, 5), )

    
    systemStatus = property(__systemStatus.value, __systemStatus.set, None, None)

    
    # Attribute v uses Python identifier v
    __v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'v'), 'v', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_CTD_ANON__v', pyxb.binding.datatypes.string, fixed=True, unicode_default='1.1')
    __v._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 28, 3)
    __v._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 28, 3)
    
    v = property(__v.value, __v.set, None, None)

    _ElementMap.update({
        __airport.name() : __airport,
        __positionReport.name() : __positionReport,
        __adsbReport.name() : __adsbReport,
        __mlatReport.name() : __mlatReport,
        __smrReport.name() : __smrReport,
        __genericFlightInfo.name() : __genericFlightInfo,
        __systemStatus.name() : __systemStatus
    })
    _AttributeMap.update({
        __v.name() : __v
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}genericFlightInfoType with content type ELEMENT_ONLY
class genericFlightInfoType (pyxb.binding.basis.complexTypeDefinition):
    """ASDE-X Generic Flight Plan Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genericFlightInfoType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}interface uses Python identifier interface
    __interface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interface'), 'interface', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_genericFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventinterface', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 10, 3), )

    
    interface = property(__interface.value, __interface.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_genericFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtype', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 12, 3), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightId uses Python identifier flightId
    __flightId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flightId'), 'flightId', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_genericFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventflightId', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 14, 3), )

    
    flightId = property(__flightId.value, __flightId.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightInfo uses Python identifier flightInfo
    __flightInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flightInfo'), 'flightInfo', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_genericFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventflightInfo', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 16, 3), )

    
    flightInfo = property(__flightInfo.value, __flightInfo.set, None, None)

    _ElementMap.update({
        __interface.name() : __interface,
        __type.name() : __type,
        __flightId.name() : __flightId,
        __flightInfo.name() : __flightInfo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.genericFlightInfoType = genericFlightInfoType
Namespace.addCategoryObject('typeBinding', 'genericFlightInfoType', genericFlightInfoType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiFlightIdType with content type ELEMENT_ONLY
class gfiFlightIdType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Flight Identification Information"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiFlightIdType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aircraftId uses Python identifier aircraftId
    __aircraftId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aircraftId'), 'aircraftId', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightIdType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaircraftId', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 44, 3), )

    
    aircraftId = property(__aircraftId.value, __aircraftId.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACode uses Python identifier mode3ACode
    __mode3ACode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), 'mode3ACode', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightIdType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmode3ACode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 46, 3), )

    
    mode3ACode = property(__mode3ACode.value, __mode3ACode.set, None, None)

    _ElementMap.update({
        __aircraftId.name() : __aircraftId,
        __mode3ACode.name() : __mode3ACode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.gfiFlightIdType = gfiFlightIdType
Namespace.addCategoryObject('typeBinding', 'gfiFlightIdType', gfiFlightIdType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gfiFlightInfoType with content type ELEMENT_ONLY
class gfiFlightInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Flight Information"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gfiFlightInfoType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 66, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acType uses Python identifier acType
    __acType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acType'), 'acType', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventacType', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 71, 3), )

    
    acType = property(__acType.value, __acType.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'category'), 'category', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcategory', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 73, 3), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightRules uses Python identifier flightRules
    __flightRules = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flightRules'), 'flightRules', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventflightRules', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 75, 3), )

    
    flightRules = property(__flightRules.value, __flightRules.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}entryFix uses Python identifier entryFix
    __entryFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entryFix'), 'entryFix', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevententryFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 77, 3), )

    
    entryFix = property(__entryFix.value, __entryFix.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}exitFix uses Python identifier exitFix
    __exitFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exitFix'), 'exitFix', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventexitFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 79, 3), )

    
    exitFix = property(__exitFix.value, __exitFix.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}runway uses Python identifier runway
    __runway = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runway'), 'runway', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventrunway', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 81, 3), )

    
    runway = property(__runway.value, __runway.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}airport uses Python identifier airport
    __airport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'airport'), 'airport', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventairport', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 83, 3), )

    
    airport = property(__airport.value, __airport.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}scratchpad1 uses Python identifier scratchpad1
    __scratchpad1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scratchpad1'), 'scratchpad1', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventscratchpad1', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 85, 3), )

    
    scratchpad1 = property(__scratchpad1.value, __scratchpad1.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}scratchpad2 uses Python identifier scratchpad2
    __scratchpad2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scratchpad2'), 'scratchpad2', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_gfiFlightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventscratchpad2', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 87, 3), )

    
    scratchpad2 = property(__scratchpad2.value, __scratchpad2.set, None, None)

    _ElementMap.update({
        __acType.name() : __acType,
        __category.name() : __category,
        __flightRules.name() : __flightRules,
        __entryFix.name() : __entryFix,
        __exitFix.name() : __exitFix,
        __runway.name() : __runway,
        __airport.name() : __airport,
        __scratchpad1.name() : __scratchpad1,
        __scratchpad2.name() : __scratchpad2
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.gfiFlightInfoType = gfiFlightInfoType
Namespace.addCategoryObject('typeBinding', 'gfiFlightInfoType', gfiFlightInfoType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}positionReportType with content type ELEMENT_ONLY
class positionReportType (pyxb.binding.basis.complexTypeDefinition):
    """ASDE-X System Track Report"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positionReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 19, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}seqNum uses Python identifier seqNum
    __seqNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'seqNum'), 'seqNum', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventseqNum', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 24, 3), )

    
    seqNum = property(__seqNum.value, __seqNum.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'time'), 'time', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 25, 3), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}track uses Python identifier track
    __track = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'track'), 'track', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtrack', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 26, 3), )

    
    track = property(__track.value, __track.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}stid uses Python identifier stid
    __stid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stid'), 'stid', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstid', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 27, 3), )

    
    stid = property(__stid.value, __stid.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightId uses Python identifier flightId
    __flightId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flightId'), 'flightId', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventflightId', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 28, 3), )

    
    flightId = property(__flightId.value, __flightId.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightInfo uses Python identifier flightInfo
    __flightInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flightInfo'), 'flightInfo', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventflightInfo', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 30, 3), )

    
    flightInfo = property(__flightInfo.value, __flightInfo.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'position'), 'position', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventposition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 32, 3), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}movement uses Python identifier movement
    __movement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'movement'), 'movement', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmovement', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 34, 3), )

    
    movement = property(__movement.value, __movement.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'status'), 'status', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 36, 3), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}slc uses Python identifier slc
    __slc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'slc'), 'slc', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventslc', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 37, 3), )

    
    slc = property(__slc.value, __slc.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}manual uses Python identifier manual
    __manual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'manual'), 'manual', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmanual', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 38, 3), )

    
    manual = property(__manual.value, __manual.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}targetExtent uses Python identifier targetExtent
    __targetExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'targetExtent'), 'targetExtent', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtargetExtent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 39, 3), )

    
    targetExtent = property(__targetExtent.value, __targetExtent.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}plotCount uses Python identifier plotCount
    __plotCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plotCount'), 'plotCount', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventplotCount', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 41, 3), )

    
    plotCount = property(__plotCount.value, __plotCount.set, None, None)

    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionReportType_full', pyxb.binding.datatypes.boolean)
    __full._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 44, 2)
    __full._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 44, 2)
    
    full = property(__full.value, __full.set, None, 'Indicates whether the message is a full update (as\n\t\t\t\t\topposed to a delta)')

    _ElementMap.update({
        __seqNum.name() : __seqNum,
        __time.name() : __time,
        __track.name() : __track,
        __stid.name() : __stid,
        __flightId.name() : __flightId,
        __flightInfo.name() : __flightInfo,
        __position.name() : __position,
        __movement.name() : __movement,
        __status.name() : __status,
        __slc.name() : __slc,
        __manual.name() : __manual,
        __targetExtent.name() : __targetExtent,
        __plotCount.name() : __plotCount
    })
    _AttributeMap.update({
        __full.name() : __full
    })
_module_typeBindings.positionReportType = positionReportType
Namespace.addCategoryObject('typeBinding', 'positionReportType', positionReportType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}systemStatusType with content type ELEMENT_ONLY
class systemStatusType (pyxb.binding.basis.complexTypeDefinition):
    """ASDE-X System Status Message"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'systemStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode uses Python identifier mode
    __mode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mode'), 'mode', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_systemStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 10, 3), )

    
    mode = property(__mode.value, __mode.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_systemStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstate', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 11, 3), )

    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        __mode.name() : __mode,
        __state.name() : __state
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.systemStatusType = systemStatusType
Namespace.addCategoryObject('typeBinding', 'systemStatusType', systemStatusType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACodeDataType with content type ELEMENT_ONLY
class mode3ACodeDataType (pyxb.binding.basis.complexTypeDefinition):
    """Mode 3/A Code"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mode3ACodeDataType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 61, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mode3ACodeDataType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 66, 3), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}g uses Python identifier g
    __g = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'g'), 'g', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mode3ACodeDataType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventg', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 67, 3), )

    
    g = property(__g.value, __g.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mode3ACodeDataType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 69, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 69, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __g.name() : __g
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.mode3ACodeDataType = mode3ACodeDataType
Namespace.addCategoryObject('typeBinding', 'mode3ACodeDataType', mode3ACodeDataType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}positionGroupType with content type ELEMENT_ONLY
class positionGroupType (pyxb.binding.basis.complexTypeDefinition):
    """Basic Position Information """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positionGroupType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 72, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionGroupType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventx', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 77, 3), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'y'), 'y', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionGroupType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventy', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 78, 3), )

    
    y = property(__y.value, __y.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}lat uses Python identifier lat
    __lat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lat'), 'lat', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionGroupType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlat', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 79, 3), )

    
    lat = property(__lat.value, __lat.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}lon uses Python identifier lon
    __lon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lon'), 'lon', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionGroupType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlon', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 80, 3), )

    
    lon = property(__lon.value, __lon.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionGroupType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 82, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 82, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __lat.name() : __lat,
        __lon.name() : __lon
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.positionGroupType = positionGroupType
Namespace.addCategoryObject('typeBinding', 'positionGroupType', positionGroupType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}velocityGroupType with content type ELEMENT_ONLY
class velocityGroupType (pyxb.binding.basis.complexTypeDefinition):
    """Calculated Velocity in Cartesian Coordinates """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'velocityGroupType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 85, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_velocityGroupType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventx', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 90, 3), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'y'), 'y', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_velocityGroupType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventy', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 91, 3), )

    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_velocityGroupType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 93, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 93, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.velocityGroupType = velocityGroupType
Namespace.addCategoryObject('typeBinding', 'velocityGroupType', velocityGroupType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableHexBinaryType with content type SIMPLE
class removableHexBinaryType (pyxb.binding.basis.complexTypeDefinition):
    """Removable type extending type: xs:hexBinary
			"""
    _TypeDefinition = pyxb.binding.datatypes.hexBinary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableHexBinaryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 191, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.hexBinary
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_removableHexBinaryType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 198, 4)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 198, 4)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.removableHexBinaryType = removableHexBinaryType
Namespace.addCategoryObject('typeBinding', 'removableHexBinaryType', removableHexBinaryType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableIntType with content type SIMPLE
class removableIntType (pyxb.binding.basis.complexTypeDefinition):
    """Removable type extending type: xs:int
			"""
    _TypeDefinition = pyxb.binding.datatypes.int
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableIntType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 249, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.int
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_removableIntType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 256, 4)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 256, 4)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.removableIntType = removableIntType
Namespace.addCategoryObject('typeBinding', 'removableIntType', removableIntType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType with content type SIMPLE
class removableShortType (pyxb.binding.basis.complexTypeDefinition):
    """Removable type extending type: xs:short
			"""
    _TypeDefinition = pyxb.binding.datatypes.short
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableShortType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 261, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.short
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_removableShortType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 268, 4)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 268, 4)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.removableShortType = removableShortType
Namespace.addCategoryObject('typeBinding', 'removableShortType', removableShortType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType with content type SIMPLE
class removableUnsignedShortType (pyxb.binding.basis.complexTypeDefinition):
    """Removable type extending type: xs:unsignedShort
			"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedShort
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableUnsignedShortType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 274, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedShort
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_removableUnsignedShortType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 281, 4)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 281, 4)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.removableUnsignedShortType = removableUnsignedShortType
Namespace.addCategoryObject('typeBinding', 'removableUnsignedShortType', removableUnsignedShortType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType with content type SIMPLE
class removableDoubleType (pyxb.binding.basis.complexTypeDefinition):
    """Removable type extending type: xs:double """
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableDoubleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 287, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_removableDoubleType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 293, 4)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 293, 4)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.removableDoubleType = removableDoubleType
Namespace.addCategoryObject('typeBinding', 'removableDoubleType', removableDoubleType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType with content type SIMPLE
class removableStringType (pyxb.binding.basis.complexTypeDefinition):
    """Removable type extending type: xs:string
			"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'removableStringType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 298, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_removableStringType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 305, 4)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 305, 4)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.removableStringType = removableStringType
Namespace.addCategoryObject('typeBinding', 'removableStringType', removableStringType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}adsbStatusType with content type ELEMENT_ONLY
class adsbStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Track Status Information """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'adsbStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 66, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}cnf uses Python identifier cnf
    __cnf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cnf'), 'cnf', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcnf', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 71, 3), )

    
    cnf = property(__cnf.value, __cnf.set, None, '"new" or "confirmed"')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}dou uses Python identifier dou
    __dou = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dou'), 'dou', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdou', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 76, 3), )

    
    dou = property(__dou.value, __dou.set, None, 'HighConfidence=0; LowConfidence=1')

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbStatusType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 82, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 82, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __cnf.name() : __cnf,
        __dou.name() : __dou
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.adsbStatusType = adsbStatusType
Namespace.addCategoryObject('typeBinding', 'adsbStatusType', adsbStatusType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}adsbReportExpansionType with content type ELEMENT_ONLY
class adsbReportExpansionType (pyxb.binding.basis.complexTypeDefinition):
    """ Report Expansion Data """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'adsbReportExpansionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 85, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gm uses Python identifier gm
    __gm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gm'), 'gm', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgm', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 90, 6), )

    
    gm = property(__gm.value, __gm.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}s1 uses Python identifier s1
    __s1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 's1'), 's1', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevents1', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 91, 3), )

    
    s1 = property(__s1.value, __s1.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}su uses Python identifier su
    __su = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'su'), 'su', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsu', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 92, 3), )

    
    su = property(__su.value, __su.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_adsbReportExpansionType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 94, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 94, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __gm.name() : __gm,
        __s1.name() : __s1,
        __su.name() : __su
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.adsbReportExpansionType = adsbReportExpansionType
Namespace.addCategoryObject('typeBinding', 'adsbReportExpansionType', adsbReportExpansionType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mlatStatusType with content type ELEMENT_ONLY
class mlatStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Track Status Information """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mlatStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 66, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}cnf uses Python identifier cnf
    __cnf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cnf'), 'cnf', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcnf', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 71, 3), )

    
    cnf = property(__cnf.value, __cnf.set, None, '"new" or "confirmed"')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}dou uses Python identifier dou
    __dou = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dou'), 'dou', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdou', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 76, 3), )

    
    dou = property(__dou.value, __dou.set, None, 'HighConfidence=0; LowConfidence=1')

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatStatusType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 82, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 82, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __cnf.name() : __cnf,
        __dou.name() : __dou
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.mlatStatusType = mlatStatusType
Namespace.addCategoryObject('typeBinding', 'mlatStatusType', mlatStatusType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mlatReportExpansionType with content type ELEMENT_ONLY
class mlatReportExpansionType (pyxb.binding.basis.complexTypeDefinition):
    """ Report Expansion Data """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mlatReportExpansionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 85, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}u uses Python identifier u
    __u = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'u'), 'u', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventu', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 90, 6), )

    
    u = property(__u.value, __u.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventx', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 91, 6), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gm uses Python identifier gm
    __gm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gm'), 'gm', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgm', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 92, 6), )

    
    gm = property(__gm.value, __gm.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_mlatReportExpansionType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 94, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 94, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __u.name() : __u,
        __x.name() : __x,
        __gm.name() : __gm
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.mlatReportExpansionType = mlatReportExpansionType
Namespace.addCategoryObject('typeBinding', 'mlatReportExpansionType', mlatReportExpansionType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrStatusType with content type ELEMENT_ONLY
class smrStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Track Status Information """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smrStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 28, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}cnf uses Python identifier cnf
    __cnf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cnf'), 'cnf', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcnf', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 33, 3), )

    
    cnf = property(__cnf.value, __cnf.set, None, '"new" or "confirmed"')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tre uses Python identifier tre
    __tre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tre'), 'tre', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtre', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 38, 3), )

    
    tre = property(__tre.value, __tre.set, None, 'Default=0; Drop=1 ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mah uses Python identifier mah
    __mah = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mah'), 'mah', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmah', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 43, 3), )

    
    mah = property(__mah.value, __mah.set, None, 'Default=0; Maneuver=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tom uses Python identifier tom
    __tom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tom'), 'tom', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtom', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 48, 3), )

    
    tom = property(__tom.value, __tom.set, None, '"0", "1", "2" or "3" ')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}dou uses Python identifier dou
    __dou = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dou'), 'dou', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdou', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 53, 3), )

    
    dou = property(__dou.value, __dou.set, None, 'HighConfidence=0; LowConfidence=1')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gho uses Python identifier gho
    __gho = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gho'), 'gho', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgho', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 58, 3), )

    
    gho = property(__gho.value, __gho.set, None, 'Default=0; MultiPath=1')

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrStatusType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 64, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 64, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __cnf.name() : __cnf,
        __tre.name() : __tre,
        __mah.name() : __mah,
        __tom.name() : __tom,
        __dou.name() : __dou,
        __gho.name() : __gho
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.smrStatusType = smrStatusType
Namespace.addCategoryObject('typeBinding', 'smrStatusType', smrStatusType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrReportExpansionType with content type ELEMENT_ONLY
class smrReportExpansionType (pyxb.binding.basis.complexTypeDefinition):
    """ Report Expansion Data """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smrReportExpansionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 67, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}startRange uses Python identifier startRange
    __startRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startRange'), 'startRange', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstartRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 72, 3), )

    
    startRange = property(__startRange.value, __startRange.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}endRange uses Python identifier endRange
    __endRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endRange'), 'endRange', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventendRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 73, 3), )

    
    endRange = property(__endRange.value, __endRange.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}startAzimuth uses Python identifier startAzimuth
    __startAzimuth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startAzimuth'), 'startAzimuth', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstartAzimuth', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 74, 3), )

    
    startAzimuth = property(__startAzimuth.value, __startAzimuth.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}endAzimuth uses Python identifier endAzimuth
    __endAzimuth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endAzimuth'), 'endAzimuth', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportExpansionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventendAzimuth', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 75, 3), )

    
    endAzimuth = property(__endAzimuth.value, __endAzimuth.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_smrReportExpansionType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 77, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 77, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __startRange.name() : __startRange,
        __endRange.name() : __endRange,
        __startAzimuth.name() : __startAzimuth,
        __endAzimuth.name() : __endAzimuth
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.smrReportExpansionType = smrReportExpansionType
Namespace.addCategoryObject('typeBinding', 'smrReportExpansionType', smrReportExpansionType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightIdType with content type ELEMENT_ONLY
class flightIdType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Flight Indentification Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flightIdType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 64, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aircraftId uses Python identifier aircraftId
    __aircraftId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aircraftId'), 'aircraftId', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightIdType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaircraftId', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 70, 3), )

    
    aircraftId = property(__aircraftId.value, __aircraftId.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACode uses Python identifier mode3ACode
    __mode3ACode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), 'mode3ACode', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightIdType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmode3ACode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 72, 3), )

    
    mode3ACode = property(__mode3ACode.value, __mode3ACode.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acAddress uses Python identifier acAddress
    __acAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acAddress'), 'acAddress', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightIdType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventacAddress', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 74, 3), )

    
    acAddress = property(__acAddress.value, __acAddress.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightIdType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 77, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 77, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __aircraftId.name() : __aircraftId,
        __mode3ACode.name() : __mode3ACode,
        __acAddress.name() : __acAddress
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.flightIdType = flightIdType
Namespace.addCategoryObject('typeBinding', 'flightIdType', flightIdType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightInfoType with content type ELEMENT_ONLY
class flightInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Flight Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flightInfoType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 90, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tgtType uses Python identifier tgtType
    __tgtType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tgtType'), 'tgtType', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtgtType', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 96, 3), )

    
    tgtType = property(__tgtType.value, __tgtType.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acType uses Python identifier acType
    __acType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acType'), 'acType', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventacType', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 98, 3), )

    
    acType = property(__acType.value, __acType.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}wake uses Python identifier wake
    __wake = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wake'), 'wake', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventwake', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 99, 3), )

    
    wake = property(__wake.value, __wake.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}fix uses Python identifier fix
    __fix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fix'), 'fix', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventfix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 100, 3), )

    
    fix = property(__fix.value, __fix.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}runway uses Python identifier runway
    __runway = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runway'), 'runway', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightInfoType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventrunway', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 101, 3), )

    
    runway = property(__runway.value, __runway.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_flightInfoType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 103, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 103, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __tgtType.name() : __tgtType,
        __acType.name() : __acType,
        __wake.name() : __wake,
        __fix.name() : __fix,
        __runway.name() : __runway
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.flightInfoType = flightInfoType
Namespace.addCategoryObject('typeBinding', 'flightInfoType', flightInfoType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}positionType with content type ELEMENT_ONLY
class positionType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Position Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 161, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventx', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 167, 3), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'y'), 'y', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventy', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 168, 3), )

    
    y = property(__y.value, __y.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extendedX uses Python identifier extendedX
    __extendedX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extendedX'), 'extendedX', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventextendedX', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 169, 3), )

    
    extendedX = property(__extendedX.value, __extendedX.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extendedY uses Python identifier extendedY
    __extendedY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extendedY'), 'extendedY', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventextendedY', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 171, 3), )

    
    extendedY = property(__extendedY.value, __extendedY.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'latitude'), 'latitude', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlatitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 173, 3), )

    
    latitude = property(__latitude.value, __latitude.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'longitude'), 'longitude', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlongitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 175, 3), )

    
    longitude = property(__longitude.value, __longitude.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altitude'), 'altitude', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 177, 3), )

    
    altitude = property(__altitude.value, __altitude.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightLevel uses Python identifier flightLevel
    __flightLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'flightLevel'), 'flightLevel', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventflightLevel', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 179, 3), )

    
    flightLevel = property(__flightLevel.value, __flightLevel.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_positionType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 182, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 182, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __extendedX.name() : __extendedX,
        __extendedY.name() : __extendedY,
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __altitude.name() : __altitude,
        __flightLevel.name() : __flightLevel
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.positionType = positionType
Namespace.addCategoryObject('typeBinding', 'positionType', positionType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}movementType with content type ELEMENT_ONLY
class movementType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Movement Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'movementType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 226, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}speed uses Python identifier speed
    __speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'speed'), 'speed', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 232, 3), )

    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}heading uses Python identifier heading
    __heading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heading'), 'heading', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventheading', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 233, 3), )

    
    heading = property(__heading.value, __heading.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}vx uses Python identifier vx
    __vx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vx'), 'vx', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventvx', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 235, 3), )

    
    vx = property(__vx.value, __vx.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}vy uses Python identifier vy
    __vy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vy'), 'vy', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventvy', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 236, 3), )

    
    vy = property(__vy.value, __vy.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ax uses Python identifier ax
    __ax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ax'), 'ax', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventax', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 237, 3), )

    
    ax = property(__ax.value, __ax.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ay uses Python identifier ay
    __ay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ay'), 'ay', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventay', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 239, 3), )

    
    ay = property(__ay.value, __ay.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_movementType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 242, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 242, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __speed.name() : __speed,
        __heading.name() : __heading,
        __vx.name() : __vx,
        __vy.name() : __vy,
        __ax.name() : __ax,
        __ay.name() : __ay
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.movementType = movementType
Namespace.addCategoryObject('typeBinding', 'movementType', movementType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}statusType with content type ELEMENT_ONLY
class statusType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Status Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'statusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 287, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mon uses Python identifier mon
    __mon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mon'), 'mon', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmon', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 293, 3), )

    
    mon = property(__mon.value, __mon.set, None, 'Monosensor Indicator (False Indicates Multisensor\n\t\t\t\t\t\tor Coasted Track)')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gbs uses Python identifier gbs
    __gbs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gbs'), 'gbs', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgbs', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 299, 3), )

    
    gbs = property(__gbs.value, __gbs.set, None, 'Ground Bit Set (False Indicates Ground Bit Not\n\t\t\t\t\t\tSet or Unknown)')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mrh uses Python identifier mrh
    __mrh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mrh'), 'mrh', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmrh', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 305, 3), )

    
    mrh = property(__mrh.value, __mrh.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}src uses Python identifier src
    __src = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'src'), 'src', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsrc', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 306, 3), )

    
    src = property(__src.value, __src.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}sim uses Python identifier sim
    __sim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sim'), 'sim', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsim', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 307, 3), )

    
    sim = property(__sim.value, __sim.set, None, 'Simulated Track')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tse uses Python identifier tse
    __tse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tse'), 'tse', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtse', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 312, 3), )

    
    tse = property(__tse.value, __tse.set, None, 'Track Service Ends')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}spi uses Python identifier spi
    __spi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'spi'), 'spi', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventspi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 317, 3), )

    
    spi = property(__spi.value, __spi.set, None, 'SPI Present')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventx', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 322, 3), )

    
    x = property(__x.value, __x.set, None, 'ATCRBS X-bit Present')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gm uses Python identifier gm
    __gm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gm'), 'gm', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgm', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 327, 3), )

    
    gm = property(__gm.value, __gm.set, None, 'GPS Position > 100 Feet from Multilat Position\n\t\t\t\t\t\tIndicator')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}nc uses Python identifier nc
    __nc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nc'), 'nc', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventnc', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 333, 3), )

    
    nc = property(__nc.value, __nc.set, None, 'Non-cooperative Target Indicator (Multipath)\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ls uses Python identifier ls
    __ls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ls'), 'ls', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventls', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 339, 3), )

    
    ls = property(__ls.value, __ls.set, None, 'Coast Lost Sensor Support Indicator\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aq uses Python identifier aq
    __aq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aq'), 'aq', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaq', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 345, 3), )

    
    aq = property(__aq.value, __aq.set, None, 'Coast Association Question Indicator\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ap uses Python identifier ap
    __ap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ap'), 'ap', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventap', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 351, 3), )

    
    ap = property(__ap.value, __ap.set, None, 'Coast in Apron Indicator')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}op uses Python identifier op
    __op = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'op'), 'op', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventop', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 356, 3), )

    
    op = property(__op.value, __op.set, None, 'Coast in Oscillation Period Indicator\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tc uses Python identifier tc
    __tc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tc'), 'tc', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventtc', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 362, 3), )

    
    tc = property(__tc.value, __tc.set, None, 'Manual/Automatic Tag Conflict Indicator\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}da uses Python identifier da
    __da = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'da'), 'da', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventda', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 368, 3), )

    
    da = property(__da.value, __da.set, None, 'Duplicate Discrete Mode A Indicator\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}lv uses Python identifier lv
    __lv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lv'), 'lv', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlv', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 374, 3), )

    
    lv = property(__lv.value, __lv.set, None, 'Local Vehicle Association')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}st uses Python identifier st
    __st = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'st'), 'st', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventst', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 379, 3), )

    
    st = property(__st.value, __st.set, None, 'Suspended Track Indicator')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}rt uses Python identifier rt
    __rt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rt'), 'rt', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventrt', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 384, 3), )

    
    rt = property(__rt.value, __rt.set, None, 'Reference Transmitter Track (maintenace only)\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ss uses Python identifier ss
    __ss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ss'), 'ss', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventss', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 390, 3), )

    
    ss = property(__ss.value, __ss.set, None, 'SMR Source Fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ms uses Python identifier ms
    __ms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ms'), 'ms', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventms', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 395, 3), )

    
    ms = property(__ms.value, __ms.set, None, 'Mode S Source Fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}as uses Python identifier as_
    __as = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'as'), 'as_', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventas', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 400, 3), )

    
    as_ = property(__as.value, __as.set, None, 'ADSB Source Fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}a9s uses Python identifier a9s
    __a9s = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'a9s'), 'a9s', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventa9s', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 405, 3), )

    
    a9s = property(__a9s.value, __a9s.set, None, 'ASR9 Source Fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}at uses Python identifier at
    __at = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'at'), 'at', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventat', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 410, 3), )

    
    at = property(__at.value, __at.set, None, 'ATCRBS Source Fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}si uses Python identifier si
    __si = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'si'), 'si', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 415, 3), )

    
    si = property(__si.value, __si.set, None, 'Safety Logic Processing Inhibited on Track\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}m3c uses Python identifier m3c
    __m3c = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'm3c'), 'm3c', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventm3c', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 421, 3), )

    
    m3c = property(__m3c.value, __m3c.set, None, 'Mode 3/A Code Has Changed')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}di uses Python identifier di
    __di = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'di'), 'di', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 426, 3), )

    
    di = property(__di.value, __di.set, None, 'Display Indicator')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}s1 uses Python identifier s1
    __s1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 's1'), 's1', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevents1', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 431, 3), )

    
    s1 = property(__s1.value, __s1.set, None, 'SBS 1090ES ADSB source fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}su uses Python identifier su
    __su = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'su'), 'su', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsu', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 436, 3), )

    
    su = property(__su.value, __su.set, None, 'SBS UAT ADSB source fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}af uses Python identifier af
    __af = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'af'), 'af', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaf', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 441, 3), )

    
    af = property(__af.value, __af.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gnd uses Python identifier gnd
    __gnd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gnd'), 'gnd', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventgnd', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 442, 3), )

    
    gnd = property(__gnd.value, __gnd.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ua uses Python identifier ua
    __ua = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ua'), 'ua', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventua', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 443, 3), )

    
    ua = property(__ua.value, __ua.set, None, 'UAT source fused')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}df uses Python identifier df
    __df = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'df'), 'df', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventdf', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 448, 3), )

    
    df = property(__df.value, __df.set, None, 'Duplicate Flight Indicator')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}quality uses Python identifier quality
    __quality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quality'), 'quality', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventquality', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 453, 3), )

    
    quality = property(__quality.value, __quality.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aqUat uses Python identifier aqUat
    __aqUat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aqUat'), 'aqUat', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaqUat', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 455, 3), )

    
    aqUat = property(__aqUat.value, __aqUat.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}lvUat uses Python identifier lvUat
    __lvUat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lvUat'), 'lvUat', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlvUat', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 457, 3), )

    
    lvUat = property(__lvUat.value, __lvUat.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aq1090 uses Python identifier aq1090
    __aq1090 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aq1090'), 'aq1090', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaq1090', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 459, 3), )

    
    aq1090 = property(__aq1090.value, __aq1090.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}lv1090 uses Python identifier lv1090
    __lv1090 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lv1090'), 'lv1090', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlv1090', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 461, 3), )

    
    lv1090 = property(__lv1090.value, __lv1090.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aa uses Python identifier aa
    __aa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aa'), 'aa', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventaa', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 463, 3), )

    
    aa = property(__aa.value, __aa.set, None, 'ADSB Associated')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}av uses Python identifier av
    __av = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'av'), 'av', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventav', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 468, 3), )

    
    av = property(__av.value, __av.set, None, 'SBS ADSB Lat/Long Validation status\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}sil uses Python identifier sil
    __sil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sil'), 'sil', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsil', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 474, 3), )

    
    sil = property(__sil.value, __sil.set, None, 'Source Integrity Level')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}nic uses Python identifier nic
    __nic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nic'), 'nic', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventnic', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 479, 3), )

    
    nic = property(__nic.value, __nic.set, None, 'Navigation Integrity Category')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}NACp uses Python identifier NACp
    __NACp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NACp'), 'NACp', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventNACp', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 484, 3), )

    
    NACp = property(__NACp.value, __NACp.set, None, 'Navigation Accuracy Category for Position\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}vs uses Python identifier vs
    __vs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vs'), 'vs', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventvs', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 490, 3), )

    
    vs = property(__vs.value, __vs.set, None, 'Source of the data used to compute the vertical\n\t\t\t\t\t\trate\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}ud uses Python identifier ud
    __ud = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ud'), 'ud', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventud', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 497, 3), )

    
    ud = property(__ud.value, __ud.set, None, 'Vertical rate direction (up/down)\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}vertRate uses Python identifier vertRate
    __vertRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vertRate'), 'vertRate', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventvertRate', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 503, 3), )

    
    vertRate = property(__vertRate.value, __vertRate.set, None, 'Vertical rate of the current track that depicts\n\t\t\t\t\t\twhether the aircraft is climbing or descending\n\t\t\t\t\t')

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}uncorrBaroAlt uses Python identifier uncorrBaroAlt
    __uncorrBaroAlt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uncorrBaroAlt'), 'uncorrBaroAlt', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventuncorrBaroAlt', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 511, 3), )

    
    uncorrBaroAlt = property(__uncorrBaroAlt.value, __uncorrBaroAlt.set, None, 'Most recent barometric pressure altitude reported\n\t\t\t\t\t\tby the aircraft; coasted for a maximum time of 5 seconds.\n\t\t\t\t\t')

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_statusType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 520, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 520, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __mon.name() : __mon,
        __gbs.name() : __gbs,
        __mrh.name() : __mrh,
        __src.name() : __src,
        __sim.name() : __sim,
        __tse.name() : __tse,
        __spi.name() : __spi,
        __x.name() : __x,
        __gm.name() : __gm,
        __nc.name() : __nc,
        __ls.name() : __ls,
        __aq.name() : __aq,
        __ap.name() : __ap,
        __op.name() : __op,
        __tc.name() : __tc,
        __da.name() : __da,
        __lv.name() : __lv,
        __st.name() : __st,
        __rt.name() : __rt,
        __ss.name() : __ss,
        __ms.name() : __ms,
        __as.name() : __as,
        __a9s.name() : __a9s,
        __at.name() : __at,
        __si.name() : __si,
        __m3c.name() : __m3c,
        __di.name() : __di,
        __s1.name() : __s1,
        __su.name() : __su,
        __af.name() : __af,
        __gnd.name() : __gnd,
        __ua.name() : __ua,
        __df.name() : __df,
        __quality.name() : __quality,
        __aqUat.name() : __aqUat,
        __lvUat.name() : __lvUat,
        __aq1090.name() : __aq1090,
        __lv1090.name() : __lv1090,
        __aa.name() : __aa,
        __av.name() : __av,
        __sil.name() : __sil,
        __nic.name() : __nic,
        __NACp.name() : __NACp,
        __vs.name() : __vs,
        __ud.name() : __ud,
        __vertRate.name() : __vertRate,
        __uncorrBaroAlt.name() : __uncorrBaroAlt
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.statusType = statusType
Namespace.addCategoryObject('typeBinding', 'statusType', statusType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}slcType with content type ELEMENT_ONLY
class slcType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Suspended, Local Aircraft Vehicle,
				and Coasted Track Numbers"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'slcType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 623, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}suspNum uses Python identifier suspNum
    __suspNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'suspNum'), 'suspNum', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_slcType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventsuspNum', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 629, 3), )

    
    suspNum = property(__suspNum.value, __suspNum.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}localAvNum uses Python identifier localAvNum
    __localAvNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'localAvNum'), 'localAvNum', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_slcType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventlocalAvNum', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 631, 3), )

    
    localAvNum = property(__localAvNum.value, __localAvNum.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}coastNum uses Python identifier coastNum
    __coastNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coastNum'), 'coastNum', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_slcType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcoastNum', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 633, 3), )

    
    coastNum = property(__coastNum.value, __coastNum.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_slcType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 636, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 636, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __suspNum.name() : __suspNum,
        __localAvNum.name() : __localAvNum,
        __coastNum.name() : __coastNum
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.slcType = slcType
Namespace.addCategoryObject('typeBinding', 'slcType', slcType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}manualType with content type ELEMENT_ONLY
class manualType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Manually Entered Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'manualType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 754, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}callNum uses Python identifier callNum
    __callNum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'callNum'), 'callNum', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcallNum', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 760, 3), )

    
    callNum = property(__callNum.value, __callNum.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACode uses Python identifier mode3ACode
    __mode3ACode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), 'mode3ACode', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventmode3ACode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 762, 3), )

    
    mode3ACode = property(__mode3ACode.value, __mode3ACode.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acType uses Python identifier acType
    __acType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acType'), 'acType', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventacType', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 764, 3), )

    
    acType = property(__acType.value, __acType.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'category'), 'category', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventcategory', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 765, 3), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}fix uses Python identifier fix
    __fix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fix'), 'fix', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventfix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 766, 3), )

    
    fix = property(__fix.value, __fix.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}scratchpad1 uses Python identifier scratchpad1
    __scratchpad1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scratchpad1'), 'scratchpad1', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventscratchpad1', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 767, 3), )

    
    scratchpad1 = property(__scratchpad1.value, __scratchpad1.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}scratchpad2 uses Python identifier scratchpad2
    __scratchpad2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scratchpad2'), 'scratchpad2', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventscratchpad2', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 768, 3), )

    
    scratchpad2 = property(__scratchpad2.value, __scratchpad2.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_manualType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 770, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 770, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __callNum.name() : __callNum,
        __mode3ACode.name() : __mode3ACode,
        __acType.name() : __acType,
        __category.name() : __category,
        __fix.name() : __fix,
        __scratchpad1.name() : __scratchpad1,
        __scratchpad2.name() : __scratchpad2
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.manualType = manualType
Namespace.addCategoryObject('typeBinding', 'manualType', manualType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}targetExtentType with content type ELEMENT_ONLY
class targetExtentType (pyxb.binding.basis.complexTypeDefinition):
    """Aggregation of Target Extent Information
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'targetExtentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 805, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}estimate uses Python identifier estimate
    __estimate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'estimate'), 'estimate', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_targetExtentType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventestimate', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 811, 3), )

    
    estimate = property(__estimate.value, __estimate.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}startRange uses Python identifier startRange
    __startRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startRange'), 'startRange', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_targetExtentType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstartRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 813, 3), )

    
    startRange = property(__startRange.value, __startRange.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}endRange uses Python identifier endRange
    __endRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endRange'), 'endRange', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_targetExtentType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventendRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 815, 3), )

    
    endRange = property(__endRange.value, __endRange.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}startAzimuth uses Python identifier startAzimuth
    __startAzimuth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startAzimuth'), 'startAzimuth', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_targetExtentType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventstartAzimuth', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 817, 3), )

    
    startAzimuth = property(__startAzimuth.value, __startAzimuth.set, None, None)

    
    # Element {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}endAzimuth uses Python identifier endAzimuth
    __endAzimuth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endAzimuth'), 'endAzimuth', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_targetExtentType_urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementeventendAzimuth', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 819, 3), )

    
    endAzimuth = property(__endAzimuth.value, __endAzimuth.set, None, None)

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'r'), 'r', '__urnusgovdotfaaatmterminalentitiesv3_0smessurfacemovementevent_targetExtentType_r', _module_typeBindings.removableAttrType)
    __r._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 822, 2)
    __r._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 822, 2)
    
    r = property(__r.value, __r.set, None, None)

    _ElementMap.update({
        __estimate.name() : __estimate,
        __startRange.name() : __startRange,
        __endRange.name() : __endRange,
        __startAzimuth.name() : __startAzimuth,
        __endAzimuth.name() : __endAzimuth
    })
    _AttributeMap.update({
        __r.name() : __r
    })
_module_typeBindings.targetExtentType = targetExtentType
Namespace.addCategoryObject('typeBinding', 'targetExtentType', targetExtentType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mode3ACodeType with content type SIMPLE
class mode3ACodeType (removableStringType):
    """Mode 3/A Code"""
    _TypeDefinition = STD_ANON
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mode3ACodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 50, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.mode3ACodeType = mode3ACodeType
Namespace.addCategoryObject('typeBinding', 'mode3ACodeType', mode3ACodeType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}cartCoordType with content type SIMPLE
class cartCoordType (removableShortType):
    """Fused Track Position [Meters]"""
    _TypeDefinition = pyxb.binding.datatypes.short
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cartCoordType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 116, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cartCoordType = cartCoordType
Namespace.addCategoryObject('typeBinding', 'cartCoordType', cartCoordType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}cnfType with content type SIMPLE
class cnfType (removableStringType):
    """Confirmed Track Status Type"""
    _TypeDefinition = STD_ANON_
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cnfType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 156, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.cnfType = cnfType
Namespace.addCategoryObject('typeBinding', 'cnfType', cnfType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tomType with content type SIMPLE
class tomType (removableStringType):
    """TOM Status Type"""
    _TypeDefinition = STD_ANON_2
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tomType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 168, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tomType = tomType
Namespace.addCategoryObject('typeBinding', 'tomType', tomType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}radarType with content type SIMPLE
class radarType (removableShortType):
    """Radar Type"""
    _TypeDefinition = STD_ANON_3
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'radarType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 182, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.radarType = radarType
Namespace.addCategoryObject('typeBinding', 'radarType', radarType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acAddressType with content type SIMPLE
class acAddressType (removableHexBinaryType):
    """Mode S Code"""
    _TypeDefinition = STD_ANON_4
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'acAddressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 204, 1)
    _ElementMap = removableHexBinaryType._ElementMap.copy()
    _AttributeMap = removableHexBinaryType._AttributeMap.copy()
    # Base type is removableHexBinaryType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableHexBinaryType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.acAddressType = acAddressType
Namespace.addCategoryObject('typeBinding', 'acAddressType', acAddressType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}flightLevelType with content type SIMPLE
class flightLevelType (removableDoubleType):
    """Flight Level """
    _TypeDefinition = STD_ANON_5
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flightLevelType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 216, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.flightLevelType = flightLevelType
Namespace.addCategoryObject('typeBinding', 'flightLevelType', flightLevelType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}measuredHeightType with content type SIMPLE
class measuredHeightType (removableDoubleType):
    """Measured Height in Feet"""
    _TypeDefinition = STD_ANON_6
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measuredHeightType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 226, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.measuredHeightType = measuredHeightType
Namespace.addCategoryObject('typeBinding', 'measuredHeightType', measuredHeightType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}vehicleType with content type SIMPLE
class vehicleType (removableStringType):
    """Vehicle Type"""
    _TypeDefinition = STD_ANON_7
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vehicleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 236, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.vehicleType = vehicleType
Namespace.addCategoryObject('typeBinding', 'vehicleType', vehicleType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}aircraftIdType with content type SIMPLE
class aircraftIdType (removableStringType):
    """Call Sign"""
    _TypeDefinition = STD_ANON_8
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'aircraftIdType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 79, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.aircraftIdType = aircraftIdType
Namespace.addCategoryObject('typeBinding', 'aircraftIdType', aircraftIdType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}tgtTypeType with content type SIMPLE
class tgtTypeType (removableStringType):
    """Target Type"""
    _TypeDefinition = STD_ANON_9
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tgtTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 105, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tgtTypeType = tgtTypeType
Namespace.addCategoryObject('typeBinding', 'tgtTypeType', tgtTypeType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}acTypeType with content type SIMPLE
class acTypeType (removableStringType):
    """Aircraft Type"""
    _TypeDefinition = STD_ANON_10
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'acTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 118, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.acTypeType = acTypeType
Namespace.addCategoryObject('typeBinding', 'acTypeType', acTypeType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}wakeType with content type SIMPLE
class wakeType (removableStringType):
    """Wake Turbulence Category"""
    _TypeDefinition = STD_ANON_11
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wakeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 129, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.wakeType = wakeType
Namespace.addCategoryObject('typeBinding', 'wakeType', wakeType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}fixType with content type SIMPLE
class fixType (removableStringType):
    """Flight Plan Paired Fix"""
    _TypeDefinition = STD_ANON_12
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fixType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 140, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.fixType = fixType
Namespace.addCategoryObject('typeBinding', 'fixType', fixType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}runwayType with content type SIMPLE
class runwayType (removableStringType):
    """Predicted Runway"""
    _TypeDefinition = STD_ANON_13
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'runwayType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 151, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.runwayType = runwayType
Namespace.addCategoryObject('typeBinding', 'runwayType', runwayType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}extCartCoordType with content type SIMPLE
class extCartCoordType (removableIntType):
    """Extended Fused Track Position [Meters]
			"""
    _TypeDefinition = STD_ANON_14
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extCartCoordType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 184, 1)
    _ElementMap = removableIntType._ElementMap.copy()
    _AttributeMap = removableIntType._AttributeMap.copy()
    # Base type is removableIntType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableIntType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.extCartCoordType = extCartCoordType
Namespace.addCategoryObject('typeBinding', 'extCartCoordType', extCartCoordType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}latitudeRemovableType with content type SIMPLE
class latitudeRemovableType (removableDoubleType):
    """Latitude [Decimal Degrees]"""
    _TypeDefinition = STD_ANON_15
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'latitudeRemovableType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 196, 2)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.latitudeRemovableType = latitudeRemovableType
Namespace.addCategoryObject('typeBinding', 'latitudeRemovableType', latitudeRemovableType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}longitudeRemovableType with content type SIMPLE
class longitudeRemovableType (removableDoubleType):
    """Longitude [Decimal Degrees]"""
    _TypeDefinition = STD_ANON_16
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longitudeRemovableType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 207, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.longitudeRemovableType = longitudeRemovableType
Namespace.addCategoryObject('typeBinding', 'longitudeRemovableType', longitudeRemovableType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}altitudeType with content type SIMPLE
class altitudeType (removableDoubleType):
    """Fused Track Height [Feet]"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'altitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 218, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.altitudeType = altitudeType
Namespace.addCategoryObject('typeBinding', 'altitudeType', altitudeType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}speedType with content type SIMPLE
class speedType (removableUnsignedShortType):
    """Speed [Knots]"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedShort
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'speedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 244, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.speedType = speedType
Namespace.addCategoryObject('typeBinding', 'speedType', speedType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}headingType with content type SIMPLE
class headingType (removableDoubleType):
    """Heading [Degrees]"""
    _TypeDefinition = STD_ANON_17
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'headingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 252, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.headingType = headingType
Namespace.addCategoryObject('typeBinding', 'headingType', headingType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}velocityType with content type SIMPLE
class velocityType (removableDoubleType):
    """Fused Track Velocity [Meters Per Second]
			"""
    _TypeDefinition = STD_ANON_18
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'velocityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 263, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.velocityType = velocityType
Namespace.addCategoryObject('typeBinding', 'velocityType', velocityType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}accelerationType with content type SIMPLE
class accelerationType (removableDoubleType):
    """Fused Track Acceleration [Meters Per Second Per
				Second]"""
    _TypeDefinition = STD_ANON_19
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accelerationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 275, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.accelerationType = accelerationType
Namespace.addCategoryObject('typeBinding', 'accelerationType', accelerationType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}statusBitType with content type SIMPLE
class statusBitType (removableShortType):
    """Bit-Field Entry [0 = False, 1 = True]
			"""
    _TypeDefinition = STD_ANON_20
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'statusBitType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 522, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.statusBitType = statusBitType
Namespace.addCategoryObject('typeBinding', 'statusBitType', statusBitType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}mrhType with content type SIMPLE
class mrhType (removableStringType):
    """Most Reliable Height"""
    _TypeDefinition = STD_ANON_21
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mrhType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 534, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.mrhType = mrhType
Namespace.addCategoryObject('typeBinding', 'mrhType', mrhType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}srcType with content type SIMPLE
class srcType (removableStringType):
    """Fused Height Source"""
    _TypeDefinition = STD_ANON_22
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'srcType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 545, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.srcType = srcType
Namespace.addCategoryObject('typeBinding', 'srcType', srcType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}afType with content type SIMPLE
class afType (removableStringType):
    """Alert Filter Indicator"""
    _TypeDefinition = STD_ANON_23
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'afType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 560, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.afType = afType
Namespace.addCategoryObject('typeBinding', 'afType', afType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}gndType with content type SIMPLE
class gndType (removableStringType):
    """Ground Indicator"""
    _TypeDefinition = STD_ANON_24
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gndType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 572, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.gndType = gndType
Namespace.addCategoryObject('typeBinding', 'gndType', gndType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}qualityType with content type SIMPLE
class qualityType (removableShortType):
    """Track Quality"""
    _TypeDefinition = STD_ANON_25
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 584, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.qualityType = qualityType
Namespace.addCategoryObject('typeBinding', 'qualityType', qualityType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}addressQualifierType with content type SIMPLE
class addressQualifierType (removableStringType):
    """Address Qualifier from CAT033 Report
			"""
    _TypeDefinition = STD_ANON_26
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressQualifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 595, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.addressQualifierType = addressQualifierType
Namespace.addCategoryObject('typeBinding', 'addressQualifierType', addressQualifierType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}linkVersionType with content type SIMPLE
class linkVersionType (removableUnsignedShortType):
    """Link Version"""
    _TypeDefinition = STD_ANON_27
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'linkVersionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 612, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.linkVersionType = linkVersionType
Namespace.addCategoryObject('typeBinding', 'linkVersionType', linkVersionType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}avType with content type SIMPLE
class avType (removableStringType):
    """SBS ADSB Lat/Long Validation status based on
				comparison with other sensor data"""
    _TypeDefinition = STD_ANON_28
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'avType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 638, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.avType = avType
Namespace.addCategoryObject('typeBinding', 'avType', avType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}silType with content type SIMPLE
class silType (removableUnsignedShortType):
    """Source Integrity Level : probability of exceeding
				NIC Containment Radius"""
    _TypeDefinition = STD_ANON_29
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'silType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 652, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.silType = silType
Namespace.addCategoryObject('typeBinding', 'silType', silType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}nicType with content type SIMPLE
class nicType (removableUnsignedShortType):
    """Navigation Integrity Category"""
    _TypeDefinition = STD_ANON_30
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nicType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 664, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.nicType = nicType
Namespace.addCategoryObject('typeBinding', 'nicType', nicType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}NACpType with content type SIMPLE
class NACpType (removableUnsignedShortType):
    """Navigation Accuracy Category for Position
			"""
    _TypeDefinition = STD_ANON_31
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NACpType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 675, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NACpType = NACpType
Namespace.addCategoryObject('typeBinding', 'NACpType', NACpType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}udType with content type SIMPLE
class udType (removableStringType):
    """Vertical rate direction (up/down)"""
    _TypeDefinition = STD_ANON_32
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'udType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 687, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.udType = udType
Namespace.addCategoryObject('typeBinding', 'udType', udType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}vertRateType with content type SIMPLE
class vertRateType (removableStringType):
    """Vertical rate of the current track that depicts
				whether the aircraft is climbing or descending
			"""
    _TypeDefinition = STD_ANON_33
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vertRateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 698, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.vertRateType = vertRateType
Namespace.addCategoryObject('typeBinding', 'vertRateType', vertRateType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}uncorrBaroAltType with content type SIMPLE
class uncorrBaroAltType (removableStringType):
    """: Most recent barometric pressure altitude reported
				by the aircraft; coasted for a maximum time of 5 seconds.
			"""
    _TypeDefinition = STD_ANON_34
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uncorrBaroAltType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 709, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.uncorrBaroAltType = uncorrBaroAltType
Namespace.addCategoryObject('typeBinding', 'uncorrBaroAltType', uncorrBaroAltType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}suspNumType with content type SIMPLE
class suspNumType (removableShortType):
    """Suspended Track Number"""
    _TypeDefinition = STD_ANON_35
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'suspNumType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 720, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.suspNumType = suspNumType
Namespace.addCategoryObject('typeBinding', 'suspNumType', suspNumType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}localAvNumType with content type SIMPLE
class localAvNumType (removableShortType):
    """Local Aircraft Vehicle List Number
			"""
    _TypeDefinition = STD_ANON_36
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'localAvNumType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 731, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.localAvNumType = localAvNumType
Namespace.addCategoryObject('typeBinding', 'localAvNumType', localAvNumType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}coastNumType with content type SIMPLE
class coastNumType (removableShortType):
    """Coasted Track Number"""
    _TypeDefinition = STD_ANON_37
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'coastNumType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 743, 1)
    _ElementMap = removableShortType._ElementMap.copy()
    _AttributeMap = removableShortType._AttributeMap.copy()
    # Base type is removableShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.coastNumType = coastNumType
Namespace.addCategoryObject('typeBinding', 'coastNumType', coastNumType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}callNumType with content type SIMPLE
class callNumType (removableStringType):
    """Aircraft Call Number"""
    _TypeDefinition = STD_ANON_38
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'callNumType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 772, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.callNumType = callNumType
Namespace.addCategoryObject('typeBinding', 'callNumType', callNumType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}categoryType with content type SIMPLE
class categoryType (removableStringType):
    """Aircraft Category Indicator"""
    _TypeDefinition = STD_ANON_39
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'categoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 783, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.categoryType = categoryType
Namespace.addCategoryObject('typeBinding', 'categoryType', categoryType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}scratchPadType with content type SIMPLE
class scratchPadType (removableStringType):
    """Scratchpad Data"""
    _TypeDefinition = STD_ANON_40
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scratchPadType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 794, 1)
    _ElementMap = removableStringType._ElementMap.copy()
    _AttributeMap = removableStringType._AttributeMap.copy()
    # Base type is removableStringType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.scratchPadType = scratchPadType
Namespace.addCategoryObject('typeBinding', 'scratchPadType', scratchPadType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrEstimateType with content type SIMPLE
class smrEstimateType (removableUnsignedShortType):
    """Target Extent Estimate [Meters]
			"""
    _TypeDefinition = STD_ANON_41
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smrEstimateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 824, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.smrEstimateType = smrEstimateType
Namespace.addCategoryObject('typeBinding', 'smrEstimateType', smrEstimateType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrRangeType with content type SIMPLE
class smrRangeType (removableUnsignedShortType):
    """SMR Target Extent Range"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedShort
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smrRangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 836, 1)
    _ElementMap = removableUnsignedShortType._ElementMap.copy()
    _AttributeMap = removableUnsignedShortType._AttributeMap.copy()
    # Base type is removableUnsignedShortType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableUnsignedShortType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.smrRangeType = smrRangeType
Namespace.addCategoryObject('typeBinding', 'smrRangeType', smrRangeType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}smrAzimuthType with content type SIMPLE
class smrAzimuthType (removableDoubleType):
    """SMR Target Extent Azimuth"""
    _TypeDefinition = STD_ANON_42
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'smrAzimuthType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 844, 1)
    _ElementMap = removableDoubleType._ElementMap.copy()
    _AttributeMap = removableDoubleType._AttributeMap.copy()
    # Base type is removableDoubleType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableDoubleType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.smrAzimuthType = smrAzimuthType
Namespace.addCategoryObject('typeBinding', 'smrAzimuthType', smrAzimuthType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}plotCountType with content type SIMPLE
class plotCountType (removableIntType):
    """Plot count
			"""
    _TypeDefinition = STD_ANON_43
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'plotCountType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 855, 1)
    _ElementMap = removableIntType._ElementMap.copy()
    _AttributeMap = removableIntType._AttributeMap.copy()
    # Base type is removableIntType
    
    # Attribute r inherited from {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:smes:surfacemovementevent}removableIntType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.plotCountType = plotCountType
Namespace.addCategoryObject('typeBinding', 'plotCountType', plotCountType)


SurfaceMovementEventMessage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SurfaceMovementEventMessage'), CTD_ANON, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', SurfaceMovementEventMessage.name().localName(), SurfaceMovementEventMessage)

asdexMsg = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'asdexMsg'), CTD_ANON_, documentation='An ASDE-X Message', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 11, 1))
Namespace.addCategoryObject('elementBinding', asdexMsg.name().localName(), asdexMsg)



basicReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'time'), timeType, scope=basicReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 13, 3)))

basicReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'track'), trackType, scope=basicReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 14, 3)))

basicReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'position'), positionGroupType, scope=basicReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 15, 3)))

basicReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'velocity'), velocityGroupType, scope=basicReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 16, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 15, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 16, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(basicReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 13, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(basicReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'track')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 14, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(basicReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 15, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(basicReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'velocity')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 16, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
basicReportType._Automaton = _BuildAutomaton()




extendedReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'basicReport'), basicReportType, scope=extendedReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 25, 8)))

extendedReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), mode3ACodeDataType, scope=extendedReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 26, 5)))

extendedReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acAddress'), acAddressType, scope=extendedReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 27, 5)))

extendedReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'level'), flightLevelType, scope=extendedReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 28, 5)))

extendedReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height'), measuredHeightType, scope=extendedReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 29, 5)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 26, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 27, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 28, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 29, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(extendedReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'basicReport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 25, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 26, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(extendedReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acAddress')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 27, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(extendedReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'level')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(extendedReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'height')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
extendedReportType._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'callsign'), _ImportedBinding_smes3__common.AircraftIdentifier, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tFlight Callsign or UNK if not available\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 20, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'track'), pyxb.binding.datatypes.short, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tFused Track Number\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 27, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stid'), pyxb.binding.datatypes.long, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tSTDDS Track Id\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 34, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), _ImportedBinding_smes3__common.BeaconCode, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tMode 3A code received from ASDE-X\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 41, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acAddress'), pyxb.binding.datatypes.hexBinary, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tMode S Code received from ASDE-X\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 48, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'time'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tTime of the event\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 55, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'event'), _ImportedBinding_smes3__smestypes.surfaceEventType, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tType of event\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 62, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'position'), _ImportedBinding_smes3__smestypes.positionType, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\t2D Position of the target\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 69, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altitude'), _ImportedBinding_smes3__smestypes.altitudeType, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tAltitude in feet\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 76, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), _ImportedBinding_smes3__smestypes.flightStatusType, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tSurface status of the flight\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 83, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'events'), _ImportedBinding_smes3__smestypes.surfaceEventListType, scope=CTD_ANON, documentation='\n\t\t\t\t\t\t\tList of past events\n                        ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 90, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 20, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 41, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 48, 4))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'callsign')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 20, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'track')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 27, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stid')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 34, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 41, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acAddress')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 48, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 55, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'event')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 62, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 69, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 76, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 83, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'events')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\SMESSurfaceMovementEventMessage.xsd', 90, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_2()




adsbReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'report'), extendedReportType, scope=adsbReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 16, 8)))

adsbReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptor'), adsbTargetDescriptor, scope=adsbReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 17, 5)))

adsbReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), adsbStatusType, scope=adsbReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 18, 5)))

adsbReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extent'), adsbReportExpansionType, scope=adsbReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 19, 5)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 17, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 18, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 19, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(adsbReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'report')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 16, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(adsbReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptor')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 17, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(adsbReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 18, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(adsbReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 19, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
adsbReportType._Automaton = _BuildAutomaton_3()




adsbTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crt'), bitType, scope=adsbTargetDescriptor, documentation='Default=0; CorruptedReplies=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 33, 2)))

adsbTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dcr'), bitType, scope=adsbTargetDescriptor, documentation='Default=0; ADSBDifferentialCorrection=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 38, 3)))

adsbTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rab'), bitType, scope=adsbTargetDescriptor, documentation='TargetReport=0; ReferenceTransmitterReport=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 43, 3)))

adsbTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spi'), bitType, scope=adsbTargetDescriptor, documentation='Default=0; SPI present=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 48, 3)))

adsbTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gbs'), bitType, scope=adsbTargetDescriptor, documentation='Default=0; GroundBitSet=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 53, 3)))

adsbTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tot'), vehicleType, scope=adsbTargetDescriptor, documentation='"undetermined", "aircraft", "surface"', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 58, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 33, 2))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 48, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 53, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 58, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(adsbTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crt')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 33, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(adsbTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dcr')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(adsbTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rab')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(adsbTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spi')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(adsbTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gbs')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(adsbTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tot')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
adsbTargetDescriptor._Automaton = _BuildAutomaton_4()




mlatReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'report'), extendedReportType, scope=mlatReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 16, 3)))

mlatReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptor'), mlatTargetDescriptor, scope=mlatReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 17, 3)))

mlatReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), mlatStatusType, scope=mlatReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 18, 3)))

mlatReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extent'), mlatReportExpansionType, scope=mlatReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 19, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 17, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 18, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 19, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mlatReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'report')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 16, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mlatReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptor')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 17, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mlatReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 18, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mlatReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 19, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mlatReportType._Automaton = _BuildAutomaton_5()




mlatTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crt'), bitType, scope=mlatTargetDescriptor, documentation='Default=0; CorruptedReplies=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 33, 2)))

mlatTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rab'), bitType, scope=mlatTargetDescriptor, documentation='TargetReport=0; ReferenceTransmitterReport=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 38, 3)))

mlatTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spi'), bitType, scope=mlatTargetDescriptor, documentation='Default=0; SPI present=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 43, 3)))

mlatTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gbs'), bitType, scope=mlatTargetDescriptor, documentation='Default=0; GroundBitSet=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 48, 3)))

mlatTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tot'), vehicleType, scope=mlatTargetDescriptor, documentation='"undetermined", "aircraft", ""surface"', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 53, 3)))

mlatTargetDescriptor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), radarType, scope=mlatTargetDescriptor, documentation='ATCRBS=0; UAT=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 58, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 33, 2))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 48, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 53, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 58, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mlatTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crt')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 33, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mlatTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rab')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mlatTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spi')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mlatTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gbs')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mlatTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tot')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mlatTargetDescriptor._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mlatTargetDescriptor._Automaton = _BuildAutomaton_6()




smrReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'report'), basicReportType, scope=smrReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 16, 4)))

smrReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rdpSource'), RDPSourceType, scope=smrReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 17, 4)))

smrReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extent'), smrReportExpansionType, scope=smrReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 18, 4)))

smrReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), smrStatusType, scope=smrReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 19, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 17, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 18, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 19, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(smrReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'report')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 16, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(smrReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rdpSource')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 17, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(smrReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 18, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(smrReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 19, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
smrReportType._Automaton = _BuildAutomaton_7()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'airport'), airportType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 17, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'positionReport'), positionReportType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 19, 5)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adsbReport'), adsbReportType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 21, 5)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mlatReport'), mlatReportType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 22, 5)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'smrReport'), smrReportType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 23, 5)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genericFlightInfo'), genericFlightInfoType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 24, 5)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'systemStatus'), systemStatusType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 25, 5)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'airport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'positionReport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 19, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adsbReport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 21, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mlatReport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 22, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smrReport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 23, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genericFlightInfo')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 24, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'systemStatus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\asdexmessage.xsd', 25, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_8()




genericFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interface'), gfiFlightPlanInterfaceType, scope=genericFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 10, 3)))

genericFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), gfiFlightType, scope=genericFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 12, 3)))

genericFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flightId'), gfiFlightIdType, scope=genericFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 14, 3)))

genericFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flightInfo'), gfiFlightInfoType, scope=genericFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 16, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 10, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 12, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 14, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 16, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(genericFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interface')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 10, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(genericFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 12, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(genericFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flightId')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 14, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(genericFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flightInfo')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 16, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
genericFlightInfoType._Automaton = _BuildAutomaton_9()




gfiFlightIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aircraftId'), gfiAircraftId, scope=gfiFlightIdType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 44, 3)))

gfiFlightIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), gfiMode3ACodeType, scope=gfiFlightIdType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 46, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 44, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 46, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aircraftId')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 44, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 46, 3))
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
gfiFlightIdType._Automaton = _BuildAutomaton_10()




gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acType'), gfiAcTypeType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 71, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'category'), gfiCategoryType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 73, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flightRules'), gfiFlightRulesType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 75, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entryFix'), gfiFixType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 77, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exitFix'), gfiFixType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 79, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runway'), gfiRunwayType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 81, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'airport'), gfiAirportType, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 83, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scratchpad1'), gfiScratchPad1Type, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 85, 3)))

gfiFlightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scratchpad2'), gfiScratchPad2Type, scope=gfiFlightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 87, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 71, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 73, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 75, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 77, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 79, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 81, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 83, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 85, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 87, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'category')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 73, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flightRules')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 75, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entryFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 77, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exitFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 79, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runway')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 81, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'airport')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 83, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scratchpad1')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 85, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(gfiFlightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scratchpad2')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\genericflightplan.xsd', 87, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
gfiFlightInfoType._Automaton = _BuildAutomaton_11()




positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'seqNum'), seqNumType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 24, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'time'), timeType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 25, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'track'), trackType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 26, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stid'), stidType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 27, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flightId'), flightIdType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 28, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flightInfo'), flightInfoType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 30, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'position'), positionType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 32, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'movement'), movementType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 34, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'status'), statusType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 36, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'slc'), slcType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 37, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'manual'), manualType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 38, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'targetExtent'), targetExtentType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 39, 3)))

positionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plotCount'), plotCountType, scope=positionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 41, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 28, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 30, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 32, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 34, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 36, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 37, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 38, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 39, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 41, 3))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'seqNum')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'time')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 25, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'track')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 26, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stid')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 27, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flightId')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 28, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flightInfo')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 30, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 32, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'movement')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 34, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'status')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 36, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'slc')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 37, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'manual')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 38, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'targetExtent')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 39, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(positionReportType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plotCount')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 41, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
positionReportType._Automaton = _BuildAutomaton_12()




systemStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mode'), modeType, scope=systemStatusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 10, 3)))

systemStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), stateType, scope=systemStatusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 11, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(systemStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 10, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(systemStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\systemstatus.xsd', 11, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
systemStatusType._Automaton = _BuildAutomaton_13()




mode3ACodeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), mode3ACodeType, scope=mode3ACodeDataType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 66, 3)))

mode3ACodeDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'g'), bitType, scope=mode3ACodeDataType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 67, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mode3ACodeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 66, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mode3ACodeDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'g')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 67, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mode3ACodeDataType._Automaton = _BuildAutomaton_14()




positionGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), cartCoordType, scope=positionGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 77, 3)))

positionGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'y'), cartCoordType, scope=positionGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 78, 3)))

positionGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lat'), latitudeType, scope=positionGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 79, 3)))

positionGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lon'), longitudeType, scope=positionGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 80, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 79, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 80, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 77, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(positionGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'y')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 78, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(positionGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lat')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 79, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(positionGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lon')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 80, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
positionGroupType._Automaton = _BuildAutomaton_15()




velocityGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), pyxb.binding.datatypes.double, scope=velocityGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 90, 3)))

velocityGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'y'), pyxb.binding.datatypes.double, scope=velocityGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 91, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(velocityGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 90, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(velocityGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'y')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\ASDEXTypes.xsd', 91, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
velocityGroupType._Automaton = _BuildAutomaton_16()




adsbStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cnf'), cnfType, scope=adsbStatusType, documentation='"new" or "confirmed"', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 71, 3)))

adsbStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dou'), bitType, scope=adsbStatusType, documentation='HighConfidence=0; LowConfidence=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 76, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 71, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 76, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(adsbStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cnf')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(adsbStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dou')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 76, 3))
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
adsbStatusType._Automaton = _BuildAutomaton_17()




adsbReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gm'), bitType, scope=adsbReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 90, 6)))

adsbReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 's1'), bitType, scope=adsbReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 91, 3)))

adsbReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'su'), bitType, scope=adsbReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 92, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 90, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 91, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 92, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(adsbReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gm')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 90, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(adsbReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 's1')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 91, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(adsbReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'su')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\ADSBMessage.xsd', 92, 3))
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
adsbReportExpansionType._Automaton = _BuildAutomaton_18()




mlatStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cnf'), cnfType, scope=mlatStatusType, documentation='"new" or "confirmed"', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 71, 3)))

mlatStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dou'), bitType, scope=mlatStatusType, documentation='HighConfidence=0; LowConfidence=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 76, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 71, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 76, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mlatStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cnf')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mlatStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dou')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 76, 3))
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
mlatStatusType._Automaton = _BuildAutomaton_19()




mlatReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'u'), bitType, scope=mlatReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 90, 6)))

mlatReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), bitType, scope=mlatReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 91, 6)))

mlatReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gm'), bitType, scope=mlatReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 92, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 90, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 91, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 92, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mlatReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'u')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 90, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mlatReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 91, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mlatReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gm')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\MLATMessage.xsd', 92, 6))
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
mlatReportExpansionType._Automaton = _BuildAutomaton_20()




smrStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cnf'), cnfType, scope=smrStatusType, documentation='"new" or "confirmed"', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 33, 3)))

smrStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tre'), bitType, scope=smrStatusType, documentation='Default=0; Drop=1 ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 38, 3)))

smrStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mah'), bitType, scope=smrStatusType, documentation='Default=0; Maneuver=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 43, 3)))

smrStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tom'), tomType, scope=smrStatusType, documentation='"0", "1", "2" or "3" ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 48, 3)))

smrStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dou'), bitType, scope=smrStatusType, documentation='HighConfidence=0; LowConfidence=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 53, 3)))

smrStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gho'), bitType, scope=smrStatusType, documentation='Default=0; MultiPath=1', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 58, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 33, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 48, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 53, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 58, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(smrStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cnf')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 33, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(smrStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tre')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(smrStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mah')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(smrStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tom')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 48, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(smrStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dou')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(smrStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gho')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 58, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
smrStatusType._Automaton = _BuildAutomaton_21()




smrReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startRange'), rangeType, scope=smrReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 72, 3)))

smrReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endRange'), rangeType, scope=smrReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 73, 3)))

smrReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startAzimuth'), azimuthType, scope=smrReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 74, 3)))

smrReportExpansionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endAzimuth'), azimuthType, scope=smrReportExpansionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 75, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 72, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 73, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 74, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 75, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(smrReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 72, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(smrReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 73, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(smrReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startAzimuth')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 74, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(smrReportExpansionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endAzimuth')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\cat10\\SMRMessage.xsd', 75, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
smrReportExpansionType._Automaton = _BuildAutomaton_22()




flightIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aircraftId'), aircraftIdType, scope=flightIdType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 70, 3)))

flightIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), mode3ACodeType, scope=flightIdType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 72, 3)))

flightIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acAddress'), acAddressType, scope=flightIdType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 74, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 70, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 72, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 74, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flightIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aircraftId')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 70, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(flightIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 72, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(flightIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acAddress')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 74, 3))
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
flightIdType._Automaton = _BuildAutomaton_23()




flightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tgtType'), tgtTypeType, scope=flightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 96, 3)))

flightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acType'), acTypeType, scope=flightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 98, 3)))

flightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wake'), wakeType, scope=flightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 99, 3)))

flightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fix'), fixType, scope=flightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 100, 3)))

flightInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runway'), runwayType, scope=flightInfoType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 101, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 96, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 98, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 99, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 100, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 101, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tgtType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 96, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(flightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 98, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(flightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wake')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 99, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(flightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 100, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(flightInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runway')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 101, 3))
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
flightInfoType._Automaton = _BuildAutomaton_24()




positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), cartCoordType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 167, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'y'), cartCoordType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 168, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extendedX'), extCartCoordType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 169, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extendedY'), extCartCoordType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 171, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'latitude'), latitudeRemovableType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 173, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'longitude'), longitudeRemovableType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 175, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altitude'), altitudeType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 177, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'flightLevel'), flightLevelType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 179, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 167, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 168, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 169, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 171, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 173, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 175, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 177, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 179, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 167, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'y')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 168, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extendedX')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 169, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extendedY')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 171, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'latitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 173, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'longitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 175, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 177, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'flightLevel')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 179, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
positionType._Automaton = _BuildAutomaton_25()




movementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'speed'), speedType, scope=movementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 232, 3)))

movementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heading'), headingType, scope=movementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 233, 3)))

movementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vx'), velocityType, scope=movementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 235, 3)))

movementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vy'), velocityType, scope=movementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 236, 3)))

movementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ax'), accelerationType, scope=movementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 237, 3)))

movementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ay'), accelerationType, scope=movementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 239, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 232, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 233, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 235, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 236, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 237, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 239, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(movementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'speed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 232, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(movementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heading')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 233, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(movementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vx')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 235, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(movementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vy')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 236, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(movementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ax')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 237, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(movementType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ay')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 239, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
movementType._Automaton = _BuildAutomaton_26()




statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mon'), statusBitType, scope=statusType, documentation='Monosensor Indicator (False Indicates Multisensor\n\t\t\t\t\t\tor Coasted Track)', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 293, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gbs'), statusBitType, scope=statusType, documentation='Ground Bit Set (False Indicates Ground Bit Not\n\t\t\t\t\t\tSet or Unknown)', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 299, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mrh'), mrhType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 305, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'src'), srcType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 306, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sim'), statusBitType, scope=statusType, documentation='Simulated Track', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 307, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tse'), statusBitType, scope=statusType, documentation='Track Service Ends', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 312, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'spi'), statusBitType, scope=statusType, documentation='SPI Present', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 317, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), statusBitType, scope=statusType, documentation='ATCRBS X-bit Present', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 322, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gm'), statusBitType, scope=statusType, documentation='GPS Position > 100 Feet from Multilat Position\n\t\t\t\t\t\tIndicator', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 327, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nc'), statusBitType, scope=statusType, documentation='Non-cooperative Target Indicator (Multipath)\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 333, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ls'), statusBitType, scope=statusType, documentation='Coast Lost Sensor Support Indicator\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 339, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aq'), statusBitType, scope=statusType, documentation='Coast Association Question Indicator\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 345, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ap'), statusBitType, scope=statusType, documentation='Coast in Apron Indicator', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 351, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'op'), statusBitType, scope=statusType, documentation='Coast in Oscillation Period Indicator\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 356, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tc'), statusBitType, scope=statusType, documentation='Manual/Automatic Tag Conflict Indicator\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 362, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'da'), statusBitType, scope=statusType, documentation='Duplicate Discrete Mode A Indicator\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 368, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lv'), statusBitType, scope=statusType, documentation='Local Vehicle Association', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 374, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'st'), statusBitType, scope=statusType, documentation='Suspended Track Indicator', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 379, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rt'), statusBitType, scope=statusType, documentation='Reference Transmitter Track (maintenace only)\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 384, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ss'), statusBitType, scope=statusType, documentation='SMR Source Fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 390, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ms'), statusBitType, scope=statusType, documentation='Mode S Source Fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 395, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'as'), statusBitType, scope=statusType, documentation='ADSB Source Fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 400, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a9s'), statusBitType, scope=statusType, documentation='ASR9 Source Fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 405, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'at'), statusBitType, scope=statusType, documentation='ATCRBS Source Fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 410, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'si'), statusBitType, scope=statusType, documentation='Safety Logic Processing Inhibited on Track\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 415, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'm3c'), statusBitType, scope=statusType, documentation='Mode 3/A Code Has Changed', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 421, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'di'), statusBitType, scope=statusType, documentation='Display Indicator', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 426, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 's1'), statusBitType, scope=statusType, documentation='SBS 1090ES ADSB source fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 431, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'su'), statusBitType, scope=statusType, documentation='SBS UAT ADSB source fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 436, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'af'), afType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 441, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gnd'), gndType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 442, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ua'), statusBitType, scope=statusType, documentation='UAT source fused', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 443, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'df'), statusBitType, scope=statusType, documentation='Duplicate Flight Indicator', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 448, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quality'), qualityType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 453, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aqUat'), addressQualifierType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 455, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lvUat'), linkVersionType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 457, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aq1090'), addressQualifierType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 459, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lv1090'), linkVersionType, scope=statusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 461, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aa'), statusBitType, scope=statusType, documentation='ADSB Associated', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 463, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'av'), avType, scope=statusType, documentation='SBS ADSB Lat/Long Validation status\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 468, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sil'), silType, scope=statusType, documentation='Source Integrity Level', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 474, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nic'), nicType, scope=statusType, documentation='Navigation Integrity Category', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 479, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NACp'), NACpType, scope=statusType, documentation='Navigation Accuracy Category for Position\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 484, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vs'), mrhType, scope=statusType, documentation='Source of the data used to compute the vertical\n\t\t\t\t\t\trate\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 490, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ud'), udType, scope=statusType, documentation='Vertical rate direction (up/down)\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 497, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vertRate'), vertRateType, scope=statusType, documentation='Vertical rate of the current track that depicts\n\t\t\t\t\t\twhether the aircraft is climbing or descending\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 503, 3)))

statusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uncorrBaroAlt'), uncorrBaroAltType, scope=statusType, documentation='Most recent barometric pressure altitude reported\n\t\t\t\t\t\tby the aircraft; coasted for a maximum time of 5 seconds.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 511, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 293, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 299, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 305, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 306, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 307, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 312, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 317, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 322, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 327, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 333, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 339, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 345, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 351, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 356, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 362, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 368, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 374, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 379, 3))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 384, 3))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 390, 3))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 395, 3))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 400, 3))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 405, 3))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 410, 3))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 415, 3))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 421, 3))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 426, 3))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 431, 3))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 436, 3))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 441, 3))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 442, 3))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 443, 3))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 448, 3))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 453, 3))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 455, 3))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 457, 3))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 459, 3))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 461, 3))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 463, 3))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 468, 3))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 474, 3))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 479, 3))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 484, 3))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 490, 3))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 497, 3))
    counters.add(cc_44)
    cc_45 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 503, 3))
    counters.add(cc_45)
    cc_46 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 511, 3))
    counters.add(cc_46)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mon')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 293, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gbs')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 299, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mrh')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 305, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'src')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 306, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sim')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 307, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tse')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 312, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'spi')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 317, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 322, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gm')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 327, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nc')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 333, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ls')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 339, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aq')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 345, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ap')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 351, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'op')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 356, 3))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tc')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 362, 3))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'da')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 368, 3))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lv')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 374, 3))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'st')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 379, 3))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rt')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 384, 3))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ss')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 390, 3))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ms')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 395, 3))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'as')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 400, 3))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'a9s')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 405, 3))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'at')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 410, 3))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'si')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 415, 3))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'm3c')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 421, 3))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'di')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 426, 3))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 's1')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 431, 3))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'su')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 436, 3))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'af')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 441, 3))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gnd')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 442, 3))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ua')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 443, 3))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'df')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 448, 3))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quality')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 453, 3))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aqUat')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 455, 3))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lvUat')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 457, 3))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aq1090')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 459, 3))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lv1090')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 461, 3))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aa')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 463, 3))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'av')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 468, 3))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sil')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 474, 3))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nic')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 479, 3))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NACp')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 484, 3))
    st_42 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vs')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 490, 3))
    st_43 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ud')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 497, 3))
    st_44 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_45, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vertRate')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 503, 3))
    st_45 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_46, False))
    symbol = pyxb.binding.content.ElementUse(statusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uncorrBaroAlt')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 511, 3))
    st_46 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_46, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_43, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_44, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_44, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_44, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_45, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_45, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_46, True) ]))
    st_46._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
statusType._Automaton = _BuildAutomaton_27()




slcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'suspNum'), suspNumType, scope=slcType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 629, 3)))

slcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'localAvNum'), localAvNumType, scope=slcType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 631, 3)))

slcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coastNum'), coastNumType, scope=slcType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 633, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 629, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 631, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 633, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(slcType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'suspNum')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 629, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(slcType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'localAvNum')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 631, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(slcType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coastNum')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 633, 3))
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
slcType._Automaton = _BuildAutomaton_28()




manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'callNum'), callNumType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 760, 3)))

manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode'), mode3ACodeType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 762, 3)))

manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acType'), acTypeType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 764, 3)))

manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'category'), categoryType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 765, 3)))

manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fix'), fixType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 766, 3)))

manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scratchpad1'), scratchPadType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 767, 3)))

manualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scratchpad2'), scratchPadType, scope=manualType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 768, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 760, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 762, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 764, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 765, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 766, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 767, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 768, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'callNum')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 760, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mode3ACode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 762, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 764, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'category')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 765, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 766, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scratchpad1')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 767, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(manualType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scratchpad2')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 768, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
manualType._Automaton = _BuildAutomaton_29()




targetExtentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'estimate'), smrEstimateType, scope=targetExtentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 811, 3)))

targetExtentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startRange'), smrRangeType, scope=targetExtentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 813, 3)))

targetExtentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endRange'), smrRangeType, scope=targetExtentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 815, 3)))

targetExtentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startAzimuth'), smrAzimuthType, scope=targetExtentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 817, 3)))

targetExtentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endAzimuth'), smrAzimuthType, scope=targetExtentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 819, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 811, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 813, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 815, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 817, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 819, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(targetExtentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'estimate')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 811, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(targetExtentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 813, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(targetExtentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 815, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(targetExtentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startAzimuth')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 817, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(targetExtentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endAzimuth')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\smes\\sd\\positionreport.xsd', 819, 3))
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
targetExtentType._Automaton = _BuildAutomaton_30()

