# .\_fx.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9db7084a19f0f156744c63e4d8ed4c064a08f05f
# Generated 2018-08-28 14:52:08.000262 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace http://www.fixm.aero/flight/3.0 [xmlns:fx]

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
import _fb as _ImportedBinding__fb
import _ff as _ImportedBinding__ff

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.fixm.aero/flight/3.0', create_if_missing=True)
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


# Atomic simple type: {http://www.fixm.aero/flight/3.0}AircraftPerformanceCategoryType
class AircraftPerformanceCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Aircraft Performance Category: A coded category assigned to the aircraft based on 
            a speed directly proportional to its stall speed, which functions as a standardized 
            basis for relating aircraft manoeuvrability to specific instrument approach procedures. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftPerformanceCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 238, 3)
    _Documentation = '\n            .Aircraft Performance Category: A coded category assigned to the aircraft based on \n            a speed directly proportional to its stall speed, which functions as a standardized \n            basis for relating aircraft manoeuvrability to specific instrument approach procedures. \n            \n         '
AircraftPerformanceCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AircraftPerformanceCategoryType, enum_prefix=None)
AircraftPerformanceCategoryType.A = AircraftPerformanceCategoryType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
AircraftPerformanceCategoryType.B = AircraftPerformanceCategoryType._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
AircraftPerformanceCategoryType.C = AircraftPerformanceCategoryType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
AircraftPerformanceCategoryType.D = AircraftPerformanceCategoryType._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
AircraftPerformanceCategoryType.E = AircraftPerformanceCategoryType._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
AircraftPerformanceCategoryType.H = AircraftPerformanceCategoryType._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
AircraftPerformanceCategoryType._InitializeFacetMap(AircraftPerformanceCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AircraftPerformanceCategoryType', AircraftPerformanceCategoryType)
_module_typeBindings.AircraftPerformanceCategoryType = AircraftPerformanceCategoryType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}EngineTypeType
class EngineTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Engine Type: The category of the aircraft  engine. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EngineTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 297, 3)
    _Documentation = '\n            .Engine Type: The category of the aircraft  engine. \n         '
EngineTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EngineTypeType, enum_prefix=None)
EngineTypeType.PISTON = EngineTypeType._CF_enumeration.addEnumeration(unicode_value='PISTON', tag='PISTON')
EngineTypeType.TURBO_PROP = EngineTypeType._CF_enumeration.addEnumeration(unicode_value='TURBO_PROP', tag='TURBO_PROP')
EngineTypeType.TURBO_SHAFT = EngineTypeType._CF_enumeration.addEnumeration(unicode_value='TURBO_SHAFT', tag='TURBO_SHAFT')
EngineTypeType.TURBO_JET = EngineTypeType._CF_enumeration.addEnumeration(unicode_value='TURBO_JET', tag='TURBO_JET')
EngineTypeType.TURBO_FAN = EngineTypeType._CF_enumeration.addEnumeration(unicode_value='TURBO_FAN', tag='TURBO_FAN')
EngineTypeType.PROP_FAN = EngineTypeType._CF_enumeration.addEnumeration(unicode_value='PROP_FAN', tag='PROP_FAN')
EngineTypeType._InitializeFacetMap(EngineTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EngineTypeType', EngineTypeType)
_module_typeBindings.EngineTypeType = EngineTypeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}StandardCapabilitiesIndicatorType
class StandardCapabilitiesIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Standard Capabilities Indicator: This element indicates the aircraft carries the 
            set of capabilities considered   standard   by the appropriate authority. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandardCapabilitiesIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 313, 3)
    _Documentation = '\n            .Standard Capabilities Indicator: This element indicates the aircraft carries the \n            set of capabilities considered   standard   by the appropriate authority. \n         '
StandardCapabilitiesIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StandardCapabilitiesIndicatorType, enum_prefix=None)
StandardCapabilitiesIndicatorType.STANDARD = StandardCapabilitiesIndicatorType._CF_enumeration.addEnumeration(unicode_value='STANDARD', tag='STANDARD')
StandardCapabilitiesIndicatorType._InitializeFacetMap(StandardCapabilitiesIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StandardCapabilitiesIndicatorType', StandardCapabilitiesIndicatorType)
_module_typeBindings.StandardCapabilitiesIndicatorType = StandardCapabilitiesIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}WakeTurbulenceCategoryType
class WakeTurbulenceCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Wake Turbulence Category: ICAO classification of the aircraft wake turbulence, based 
            on the maximum certified take off mass. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WakeTurbulenceCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 325, 3)
    _Documentation = '\n            .Wake Turbulence Category: ICAO classification of the aircraft wake turbulence, based \n            on the maximum certified take off mass. \n         '
WakeTurbulenceCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WakeTurbulenceCategoryType, enum_prefix=None)
WakeTurbulenceCategoryType.L = WakeTurbulenceCategoryType._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
WakeTurbulenceCategoryType.M = WakeTurbulenceCategoryType._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
WakeTurbulenceCategoryType.H = WakeTurbulenceCategoryType._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
WakeTurbulenceCategoryType.J = WakeTurbulenceCategoryType._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
WakeTurbulenceCategoryType._InitializeFacetMap(WakeTurbulenceCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WakeTurbulenceCategoryType', WakeTurbulenceCategoryType)
_module_typeBindings.WakeTurbulenceCategoryType = WakeTurbulenceCategoryType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}CommunicationCodeType
class CommunicationCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Describes the aircraft communication code. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommunicationCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 137, 3)
    _Documentation = '\n            Describes the aircraft communication code. \n         '
CommunicationCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CommunicationCodeType, enum_prefix=None)
CommunicationCodeType.E1 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='E1', tag='E1')
CommunicationCodeType.E2 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='E2', tag='E2')
CommunicationCodeType.E3 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='E3', tag='E3')
CommunicationCodeType.H = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
CommunicationCodeType.M1 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='M1', tag='M1')
CommunicationCodeType.M2 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='M2', tag='M2')
CommunicationCodeType.M3 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='M3', tag='M3')
CommunicationCodeType.P1 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P1', tag='P1')
CommunicationCodeType.P2 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P2', tag='P2')
CommunicationCodeType.P3 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P3', tag='P3')
CommunicationCodeType.P4 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P4', tag='P4')
CommunicationCodeType.P5 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P5', tag='P5')
CommunicationCodeType.P6 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P6', tag='P6')
CommunicationCodeType.P7 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P7', tag='P7')
CommunicationCodeType.P8 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P8', tag='P8')
CommunicationCodeType.P9 = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='P9', tag='P9')
CommunicationCodeType.U = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='U', tag='U')
CommunicationCodeType.V = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
CommunicationCodeType.Y = CommunicationCodeType._CF_enumeration.addEnumeration(unicode_value='Y', tag='Y')
CommunicationCodeType._InitializeFacetMap(CommunicationCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CommunicationCodeType', CommunicationCodeType)
_module_typeBindings.CommunicationCodeType = CommunicationCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}DataLinkCodeType
class DataLinkCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Data Link Communication Capabilities: The serviceable equipment and capabilities 
            available on the aircraft at the time of flight that may be used to communicate data 
            to and from the aircraft. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataLinkCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 166, 3)
    _Documentation = '\n            .Data Link Communication Capabilities: The serviceable equipment and capabilities \n            available on the aircraft at the time of flight that may be used to communicate data \n            to and from the aircraft. \n         '
DataLinkCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataLinkCodeType, enum_prefix=None)
DataLinkCodeType.J1 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J1', tag='J1')
DataLinkCodeType.J2 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J2', tag='J2')
DataLinkCodeType.J3 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J3', tag='J3')
DataLinkCodeType.J4 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J4', tag='J4')
DataLinkCodeType.J5 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J5', tag='J5')
DataLinkCodeType.J6 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J6', tag='J6')
DataLinkCodeType.J7 = DataLinkCodeType._CF_enumeration.addEnumeration(unicode_value='J7', tag='J7')
DataLinkCodeType._InitializeFacetMap(DataLinkCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataLinkCodeType', DataLinkCodeType)
_module_typeBindings.DataLinkCodeType = DataLinkCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}NavigationCodeType
class NavigationCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Describes the aircraft navigation code. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NavigationCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 120, 3)
    _Documentation = '\n            Describes the aircraft navigation code. \n         '
NavigationCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NavigationCodeType, enum_prefix=None)
NavigationCodeType.A = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
NavigationCodeType.B = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
NavigationCodeType.C = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
NavigationCodeType.D = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
NavigationCodeType.F = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
NavigationCodeType.G = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
NavigationCodeType.I = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
NavigationCodeType.K = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
NavigationCodeType.L = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
NavigationCodeType.O = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='O', tag='O')
NavigationCodeType.T = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
NavigationCodeType.W = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
NavigationCodeType.X = NavigationCodeType._CF_enumeration.addEnumeration(unicode_value='X', tag='X')
NavigationCodeType._InitializeFacetMap(NavigationCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NavigationCodeType', NavigationCodeType)
_module_typeBindings.NavigationCodeType = NavigationCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}PerformanceBasedCodeType
class PerformanceBasedCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Performance-Based Navigation Capabilities: A coded category denoting which Required 
            Navigation Performance (RNP) and Area Navigation (RNAV) requirements can be met by 
            the aircraft while operating in the context of a particular airspace when supported 
            by the appropriate navigation infrastructure. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PerformanceBasedCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 143, 3)
    _Documentation = '\n            .Performance-Based Navigation Capabilities: A coded category denoting which Required \n            Navigation Performance (RNP) and Area Navigation (RNAV) requirements can be met by \n            the aircraft while operating in the context of a particular airspace when supported \n            by the appropriate navigation infrastructure. \n         '
PerformanceBasedCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PerformanceBasedCodeType, enum_prefix=None)
PerformanceBasedCodeType.A1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='A1', tag='A1')
PerformanceBasedCodeType.B1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='B1', tag='B1')
PerformanceBasedCodeType.B2 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='B2', tag='B2')
PerformanceBasedCodeType.B3 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='B3', tag='B3')
PerformanceBasedCodeType.B4 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='B4', tag='B4')
PerformanceBasedCodeType.B5 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='B5', tag='B5')
PerformanceBasedCodeType.B6 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='B6', tag='B6')
PerformanceBasedCodeType.C1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='C1', tag='C1')
PerformanceBasedCodeType.C2 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='C2', tag='C2')
PerformanceBasedCodeType.C3 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='C3', tag='C3')
PerformanceBasedCodeType.C4 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='C4', tag='C4')
PerformanceBasedCodeType.D1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='D1', tag='D1')
PerformanceBasedCodeType.D2 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='D2', tag='D2')
PerformanceBasedCodeType.D3 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='D3', tag='D3')
PerformanceBasedCodeType.D4 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='D4', tag='D4')
PerformanceBasedCodeType.L1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='L1', tag='L1')
PerformanceBasedCodeType.O1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='O1', tag='O1')
PerformanceBasedCodeType.O2 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='O2', tag='O2')
PerformanceBasedCodeType.O3 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='O3', tag='O3')
PerformanceBasedCodeType.O4 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='O4', tag='O4')
PerformanceBasedCodeType.S1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='S1', tag='S1')
PerformanceBasedCodeType.S2 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='S2', tag='S2')
PerformanceBasedCodeType.T1 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='T1', tag='T1')
PerformanceBasedCodeType.T2 = PerformanceBasedCodeType._CF_enumeration.addEnumeration(unicode_value='T2', tag='T2')
PerformanceBasedCodeType._InitializeFacetMap(PerformanceBasedCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PerformanceBasedCodeType', PerformanceBasedCodeType)
_module_typeBindings.PerformanceBasedCodeType = PerformanceBasedCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}SurveillanceCodeType
class SurveillanceCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Describes the aircraft surveillance code. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurveillanceCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 108, 3)
    _Documentation = '\n            Describes the aircraft surveillance code. \n         '
SurveillanceCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurveillanceCodeType, enum_prefix=None)
SurveillanceCodeType.A = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
SurveillanceCodeType.B1 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='B1', tag='B1')
SurveillanceCodeType.B2 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='B2', tag='B2')
SurveillanceCodeType.C = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
SurveillanceCodeType.D1 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='D1', tag='D1')
SurveillanceCodeType.E = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
SurveillanceCodeType.G1 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='G1', tag='G1')
SurveillanceCodeType.H = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
SurveillanceCodeType.I = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
SurveillanceCodeType.L = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
SurveillanceCodeType.P = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
SurveillanceCodeType.S = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
SurveillanceCodeType.U1 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='U1', tag='U1')
SurveillanceCodeType.U2 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='U2', tag='U2')
SurveillanceCodeType.V1 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='V1', tag='V1')
SurveillanceCodeType.V2 = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='V2', tag='V2')
SurveillanceCodeType.X = SurveillanceCodeType._CF_enumeration.addEnumeration(unicode_value='X', tag='X')
SurveillanceCodeType._InitializeFacetMap(SurveillanceCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SurveillanceCodeType', SurveillanceCodeType)
_module_typeBindings.SurveillanceCodeType = SurveillanceCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}DinghyColourCodeType
class DinghyColourCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Dinghy Color: The color of the dinghies carried by the aircraft. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DinghyColourCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 146, 3)
    _Documentation = '\n            .Dinghy Color: The color of the dinghies carried by the aircraft. \n         '
DinghyColourCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DinghyColourCodeType, enum_prefix=None)
DinghyColourCodeType.RED = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='RED', tag='RED')
DinghyColourCodeType.ORANGE = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='ORANGE', tag='ORANGE')
DinghyColourCodeType.YELLOW = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='YELLOW', tag='YELLOW')
DinghyColourCodeType.GREEN = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='GREEN', tag='GREEN')
DinghyColourCodeType.BLUE = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='BLUE', tag='BLUE')
DinghyColourCodeType.VIOLET = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='VIOLET', tag='VIOLET')
DinghyColourCodeType.BLACK = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='BLACK', tag='BLACK')
DinghyColourCodeType.WHITE = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='WHITE', tag='WHITE')
DinghyColourCodeType.GRAY = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='GRAY', tag='GRAY')
DinghyColourCodeType.SILVER = DinghyColourCodeType._CF_enumeration.addEnumeration(unicode_value='SILVER', tag='SILVER')
DinghyColourCodeType._InitializeFacetMap(DinghyColourCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DinghyColourCodeType', DinghyColourCodeType)
_module_typeBindings.DinghyColourCodeType = DinghyColourCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}DinghyCoverType
class DinghyCoverType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Dinghy Cover Status: Indication of the covered/uncovered nature of the dinghies 
            carried by the aircraft. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DinghyCoverType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 166, 3)
    _Documentation = '\n            .Dinghy Cover Status: Indication of the covered/uncovered nature of the dinghies \n            carried by the aircraft. \n         '
DinghyCoverType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DinghyCoverType, enum_prefix=None)
DinghyCoverType.COVERED = DinghyCoverType._CF_enumeration.addEnumeration(unicode_value='COVERED', tag='COVERED')
DinghyCoverType._InitializeFacetMap(DinghyCoverType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DinghyCoverType', DinghyCoverType)
_module_typeBindings.DinghyCoverType = DinghyCoverType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}EmergencyRadioCodeType
class EmergencyRadioCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Emergency Radio Transmitter Type: The type of serviceable communication devices 
            available on the aircraft that are able to transmit an emergency radio signal. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EmergencyRadioCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 178, 3)
    _Documentation = '\n            .Emergency Radio Transmitter Type: The type of serviceable communication devices \n            available on the aircraft that are able to transmit an emergency radio signal. \n         '
EmergencyRadioCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EmergencyRadioCodeType, enum_prefix=None)
EmergencyRadioCodeType.ULTRA_HIGH_FREQUENCY = EmergencyRadioCodeType._CF_enumeration.addEnumeration(unicode_value='ULTRA_HIGH_FREQUENCY', tag='ULTRA_HIGH_FREQUENCY')
EmergencyRadioCodeType.VERY_HIGH_FREQUENCY = EmergencyRadioCodeType._CF_enumeration.addEnumeration(unicode_value='VERY_HIGH_FREQUENCY', tag='VERY_HIGH_FREQUENCY')
EmergencyRadioCodeType.EMERGENCY_LOCATOR_TRANSMITTER = EmergencyRadioCodeType._CF_enumeration.addEnumeration(unicode_value='EMERGENCY_LOCATOR_TRANSMITTER', tag='EMERGENCY_LOCATOR_TRANSMITTER')
EmergencyRadioCodeType._InitializeFacetMap(EmergencyRadioCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EmergencyRadioCodeType', EmergencyRadioCodeType)
_module_typeBindings.EmergencyRadioCodeType = EmergencyRadioCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}LifeJacketCodeType
class LifeJacketCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Life Jacket Type: The type of life jackets available on board the aircraft. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LifeJacketCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 192, 3)
    _Documentation = '\n            .Life Jacket Type: The type of life jackets available on board the aircraft. \n         '
LifeJacketCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LifeJacketCodeType, enum_prefix=None)
LifeJacketCodeType.FLUORESCEIN = LifeJacketCodeType._CF_enumeration.addEnumeration(unicode_value='FLUORESCEIN', tag='FLUORESCEIN')
LifeJacketCodeType.VERY_HIGH_FREQUENCY = LifeJacketCodeType._CF_enumeration.addEnumeration(unicode_value='VERY_HIGH_FREQUENCY', tag='VERY_HIGH_FREQUENCY')
LifeJacketCodeType.LIGHTS = LifeJacketCodeType._CF_enumeration.addEnumeration(unicode_value='LIGHTS', tag='LIGHTS')
LifeJacketCodeType.ULTRA_HIGH_FREQUENCY = LifeJacketCodeType._CF_enumeration.addEnumeration(unicode_value='ULTRA_HIGH_FREQUENCY', tag='ULTRA_HIGH_FREQUENCY')
LifeJacketCodeType._InitializeFacetMap(LifeJacketCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LifeJacketCodeType', LifeJacketCodeType)
_module_typeBindings.LifeJacketCodeType = LifeJacketCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}SurvivalEquipmentCodeType
class SurvivalEquipmentCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Survival Equipment Type: The type of equipment carried on board the aircraft that 
            can be used by the crew and passengers to assist survival in harsh environments in 
            case of emergency. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurvivalEquipmentCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 265, 3)
    _Documentation = '\n            .Survival Equipment Type: The type of equipment carried on board the aircraft that \n            can be used by the crew and passengers to assist survival in harsh environments in \n            case of emergency. \n         '
SurvivalEquipmentCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SurvivalEquipmentCodeType, enum_prefix=None)
SurvivalEquipmentCodeType.POLAR = SurvivalEquipmentCodeType._CF_enumeration.addEnumeration(unicode_value='POLAR', tag='POLAR')
SurvivalEquipmentCodeType.DESERT = SurvivalEquipmentCodeType._CF_enumeration.addEnumeration(unicode_value='DESERT', tag='DESERT')
SurvivalEquipmentCodeType.MARITIME = SurvivalEquipmentCodeType._CF_enumeration.addEnumeration(unicode_value='MARITIME', tag='MARITIME')
SurvivalEquipmentCodeType.JUNGLE = SurvivalEquipmentCodeType._CF_enumeration.addEnumeration(unicode_value='JUNGLE', tag='JUNGLE')
SurvivalEquipmentCodeType._InitializeFacetMap(SurvivalEquipmentCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SurvivalEquipmentCodeType', SurvivalEquipmentCodeType)
_module_typeBindings.SurvivalEquipmentCodeType = SurvivalEquipmentCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AircraftDangerousGoodsLimitationType
class AircraftDangerousGoodsLimitationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Aircraft Dangerous Goods Limitation: Describes whether the shipment is packed to 
            comply with the limitations prescribed for passenger and cargo aircraft or the limitations 
            for cargo aircraft only. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftDangerousGoodsLimitationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 102, 3)
    _Documentation = '\n            .Aircraft Dangerous Goods Limitation: Describes whether the shipment is packed to \n            comply with the limitations prescribed for passenger and cargo aircraft or the limitations \n            for cargo aircraft only. \n         '
AircraftDangerousGoodsLimitationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AircraftDangerousGoodsLimitationType, enum_prefix=None)
AircraftDangerousGoodsLimitationType.PASSENGER_AND_CARGO_AIRCRAFT = AircraftDangerousGoodsLimitationType._CF_enumeration.addEnumeration(unicode_value='PASSENGER_AND_CARGO_AIRCRAFT', tag='PASSENGER_AND_CARGO_AIRCRAFT')
AircraftDangerousGoodsLimitationType.CARGO_AIRCRAFT_ONLY = AircraftDangerousGoodsLimitationType._CF_enumeration.addEnumeration(unicode_value='CARGO_AIRCRAFT_ONLY', tag='CARGO_AIRCRAFT_ONLY')
AircraftDangerousGoodsLimitationType._InitializeFacetMap(AircraftDangerousGoodsLimitationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AircraftDangerousGoodsLimitationType', AircraftDangerousGoodsLimitationType)
_module_typeBindings.AircraftDangerousGoodsLimitationType = AircraftDangerousGoodsLimitationType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}ShipmentTypeType
class ShipmentTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Shipment Type: An indicator used for dangerous cargo of whether the package is radioactive 
            or not. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShipmentTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 278, 3)
    _Documentation = '\n            .Shipment Type: An indicator used for dangerous cargo of whether the package is radioactive \n            or not. \n         '
ShipmentTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShipmentTypeType, enum_prefix=None)
ShipmentTypeType.RADIOACTIVE = ShipmentTypeType._CF_enumeration.addEnumeration(unicode_value='RADIOACTIVE', tag='RADIOACTIVE')
ShipmentTypeType._InitializeFacetMap(ShipmentTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShipmentTypeType', ShipmentTypeType)
_module_typeBindings.ShipmentTypeType = ShipmentTypeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}MarinePollutantIndicatorType
class MarinePollutantIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Marine Pollutant Indicator: An indicator if the transported dangerous goods have 
            marine pollutant content. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MarinePollutantIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 459, 3)
    _Documentation = '\n            .Marine Pollutant Indicator: An indicator if the transported dangerous goods have \n            marine pollutant content. \n         '
MarinePollutantIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MarinePollutantIndicatorType, enum_prefix=None)
MarinePollutantIndicatorType.MARINE_POLLUTANT = MarinePollutantIndicatorType._CF_enumeration.addEnumeration(unicode_value='MARINE_POLLUTANT', tag='MARINE_POLLUTANT')
MarinePollutantIndicatorType._InitializeFacetMap(MarinePollutantIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MarinePollutantIndicatorType', MarinePollutantIndicatorType)
_module_typeBindings.MarinePollutantIndicatorType = MarinePollutantIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}OverpackIndicatorType
class OverpackIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Overpack Indicator: An indicator that individual packages are assembled into a single 
            unit for handling. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OverpackIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 477, 3)
    _Documentation = '\n            .Overpack Indicator: An indicator that individual packages are assembled into a single \n            unit for handling. \n         '
OverpackIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OverpackIndicatorType, enum_prefix=None)
OverpackIndicatorType.OVERPACK_USED = OverpackIndicatorType._CF_enumeration.addEnumeration(unicode_value='OVERPACK_USED', tag='OVERPACK_USED')
OverpackIndicatorType._InitializeFacetMap(OverpackIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OverpackIndicatorType', OverpackIndicatorType)
_module_typeBindings.OverpackIndicatorType = OverpackIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}PackingGroupType
class PackingGroupType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Packing Group: A code that indicates the relative degree of danger presented by 
            various articles and substances within a Class or Division. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PackingGroupType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 496, 3)
    _Documentation = '\n            .Packing Group: A code that indicates the relative degree of danger presented by \n            various articles and substances within a Class or Division. \n         '
PackingGroupType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PackingGroupType, enum_prefix=None)
PackingGroupType.I = PackingGroupType._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
PackingGroupType.II = PackingGroupType._CF_enumeration.addEnumeration(unicode_value='II', tag='II')
PackingGroupType.III = PackingGroupType._CF_enumeration.addEnumeration(unicode_value='III', tag='III')
PackingGroupType._InitializeFacetMap(PackingGroupType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PackingGroupType', PackingGroupType)
_module_typeBindings.PackingGroupType = PackingGroupType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}ShipmentUseType
class ShipmentUseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Exclusive Use Shipment Indicator: An indicator of sole use, by a single shipper, 
            of an aircraft or of a large freight container, of which all initial, intermediate 
            and final loading and unloading is carried out in accordance with the directions 
            of the shipper or consignee. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShipmentUseType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 528, 3)
    _Documentation = '\n            .Exclusive Use Shipment Indicator: An indicator of sole use, by a single shipper, \n            of an aircraft or of a large freight container, of which all initial, intermediate \n            and final loading and unloading is carried out in accordance with the directions \n            of the shipper or consignee. \n         '
ShipmentUseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ShipmentUseType, enum_prefix=None)
ShipmentUseType.EXCLUSIVE = ShipmentUseType._CF_enumeration.addEnumeration(unicode_value='EXCLUSIVE', tag='EXCLUSIVE')
ShipmentUseType._InitializeFacetMap(ShipmentUseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ShipmentUseType', ShipmentUseType)
_module_typeBindings.ShipmentUseType = ShipmentUseType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}FissileExceptedType
class FissileExceptedType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Fissile Excepted Indicator: An indicator of whether the restrictions for fissile 
            material are excepted for a particular package. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FissileExceptedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 81, 3)
    _Documentation = '\n            .Fissile Excepted Indicator: An indicator of whether the restrictions for fissile \n            material are excepted for a particular package. \n         '
FissileExceptedType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FissileExceptedType, enum_prefix=None)
FissileExceptedType.EXCEPTED = FissileExceptedType._CF_enumeration.addEnumeration(unicode_value='EXCEPTED', tag='EXCEPTED')
FissileExceptedType._InitializeFacetMap(FissileExceptedType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FissileExceptedType', FissileExceptedType)
_module_typeBindings.FissileExceptedType = FissileExceptedType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}MaterialDispersabilityType
class MaterialDispersabilityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Low Dispersible Material Indicator: An indicator the dangerous good is a low dispersible 
            radioactive material, a solid radioactive material or a solid radioactive material 
            in a sealed capsule, which has limited dispersibility and is not in powder form. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialDispersabilityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 100, 3)
    _Documentation = '\n            .Low Dispersible Material Indicator: An indicator the dangerous good is a low dispersible \n            radioactive material, a solid radioactive material or a solid radioactive material \n            in a sealed capsule, which has limited dispersibility and is not in powder form. \n            \n         '
MaterialDispersabilityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MaterialDispersabilityType, enum_prefix=None)
MaterialDispersabilityType.LOW_DISPERSIBLE = MaterialDispersabilityType._CF_enumeration.addEnumeration(unicode_value='LOW_DISPERSIBLE', tag='LOW_DISPERSIBLE')
MaterialDispersabilityType._InitializeFacetMap(MaterialDispersabilityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MaterialDispersabilityType', MaterialDispersabilityType)
_module_typeBindings.MaterialDispersabilityType = MaterialDispersabilityType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}RadioactiveMaterialCategoryType
class RadioactiveMaterialCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Radioactive Material Category: A category used for radioactive materials in a package, 
            overpack or freight container, based on their maximum radiation level. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadioactiveMaterialCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 207, 3)
    _Documentation = '\n            .Radioactive Material Category: A category used for radioactive materials in a package, \n            overpack or freight container, based on their maximum radiation level. \n         '
RadioactiveMaterialCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RadioactiveMaterialCategoryType, enum_prefix=None)
RadioactiveMaterialCategoryType.I_WHITE = RadioactiveMaterialCategoryType._CF_enumeration.addEnumeration(unicode_value='I_WHITE', tag='I_WHITE')
RadioactiveMaterialCategoryType.II_YELLOW = RadioactiveMaterialCategoryType._CF_enumeration.addEnumeration(unicode_value='II_YELLOW', tag='II_YELLOW')
RadioactiveMaterialCategoryType.III_YELLOW = RadioactiveMaterialCategoryType._CF_enumeration.addEnumeration(unicode_value='III_YELLOW', tag='III_YELLOW')
RadioactiveMaterialCategoryType._InitializeFacetMap(RadioactiveMaterialCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RadioactiveMaterialCategoryType', RadioactiveMaterialCategoryType)
_module_typeBindings.RadioactiveMaterialCategoryType = RadioactiveMaterialCategoryType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}RadioactivityMeasureType
class RadioactivityMeasureType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Units of measure of for RadioactiveMaterialActivity. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadioactivityMeasureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 241, 3)
    _Documentation = '\n            Units of measure of for RadioactiveMaterialActivity. \n         '
RadioactivityMeasureType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RadioactivityMeasureType, enum_prefix=None)
RadioactivityMeasureType.GRAMS = RadioactivityMeasureType._CF_enumeration.addEnumeration(unicode_value='GRAMS', tag='GRAMS')
RadioactivityMeasureType.BECQUERELS = RadioactivityMeasureType._CF_enumeration.addEnumeration(unicode_value='BECQUERELS', tag='BECQUERELS')
RadioactivityMeasureType._InitializeFacetMap(RadioactivityMeasureType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RadioactivityMeasureType', RadioactivityMeasureType)
_module_typeBindings.RadioactivityMeasureType = RadioactivityMeasureType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}SpecialFormType
class SpecialFormType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Special Form Indicator: A notation that the material is 'special form' and cannot 
            produce radioactive contamination. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpecialFormType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 332, 3)
    _Documentation = "\n            .Special Form Indicator: A notation that the material is 'special form' and cannot \n            produce radioactive contamination. \n         "
SpecialFormType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpecialFormType, enum_prefix=None)
SpecialFormType.SPECIAL_FORM = SpecialFormType._CF_enumeration.addEnumeration(unicode_value='SPECIAL_FORM', tag='SPECIAL_FORM')
SpecialFormType._InitializeFacetMap(SpecialFormType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpecialFormType', SpecialFormType)
_module_typeBindings.SpecialFormType = SpecialFormType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}BoundaryCrossingConditionType
class BoundaryCrossingConditionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Boundary Crossing Condition: Indicator of whether an aircraft will cross an associated 
            boundary crossing point at or above, or at or below the altitude specified by the 
            Boundary Crossing Level - Transition. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundaryCrossingConditionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 205, 3)
    _Documentation = '\n            .Boundary Crossing Condition: Indicator of whether an aircraft will cross an associated \n            boundary crossing point at or above, or at or below the altitude specified by the \n            Boundary Crossing Level - Transition. \n         '
BoundaryCrossingConditionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BoundaryCrossingConditionType, enum_prefix=None)
BoundaryCrossingConditionType.AT_OR_ABOVE = BoundaryCrossingConditionType._CF_enumeration.addEnumeration(unicode_value='AT_OR_ABOVE', tag='AT_OR_ABOVE')
BoundaryCrossingConditionType.AT_OR_BELOW = BoundaryCrossingConditionType._CF_enumeration.addEnumeration(unicode_value='AT_OR_BELOW', tag='AT_OR_BELOW')
BoundaryCrossingConditionType._InitializeFacetMap(BoundaryCrossingConditionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BoundaryCrossingConditionType', BoundaryCrossingConditionType)
_module_typeBindings.BoundaryCrossingConditionType = BoundaryCrossingConditionType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}UnitBoundaryIndicatorType
class UnitBoundaryIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Unit Boundary Indicator: An indicator of the status of the boundary crossing in 
            the Unit Boundary List as a past crossing, the current or next crossing, or a future 
            crossing. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitBoundaryIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 346, 3)
    _Documentation = '\n            .Unit Boundary Indicator: An indicator of the status of the boundary crossing in \n            the Unit Boundary List as a past crossing, the current or next crossing, or a future \n            crossing. \n         '
UnitBoundaryIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitBoundaryIndicatorType, enum_prefix=None)
UnitBoundaryIndicatorType.PAST = UnitBoundaryIndicatorType._CF_enumeration.addEnumeration(unicode_value='PAST', tag='PAST')
UnitBoundaryIndicatorType.CURRENT = UnitBoundaryIndicatorType._CF_enumeration.addEnumeration(unicode_value='CURRENT', tag='CURRENT')
UnitBoundaryIndicatorType.FUTURE = UnitBoundaryIndicatorType._CF_enumeration.addEnumeration(unicode_value='FUTURE', tag='FUTURE')
UnitBoundaryIndicatorType._InitializeFacetMap(UnitBoundaryIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitBoundaryIndicatorType', UnitBoundaryIndicatorType)
_module_typeBindings.UnitBoundaryIndicatorType = UnitBoundaryIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AbrogationReasonCodeType
class AbrogationReasonCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Abrogation Reason: If the Coordination Status is abrogated, indicating coordination 
            is abolished by authoritative action, the reason the coordination was terminated. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbrogationReasonCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 77, 3)
    _Documentation = '\n            .Abrogation Reason: If the Coordination Status is abrogated, indicating coordination \n            is abolished by authoritative action, the reason the coordination was terminated. \n            \n         '
AbrogationReasonCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AbrogationReasonCodeType, enum_prefix=None)
AbrogationReasonCodeType.TFL = AbrogationReasonCodeType._CF_enumeration.addEnumeration(unicode_value='TFL', tag='TFL')
AbrogationReasonCodeType.ROUTE = AbrogationReasonCodeType._CF_enumeration.addEnumeration(unicode_value='ROUTE', tag='ROUTE')
AbrogationReasonCodeType.CANCELLATION = AbrogationReasonCodeType._CF_enumeration.addEnumeration(unicode_value='CANCELLATION', tag='CANCELLATION')
AbrogationReasonCodeType.DELAY = AbrogationReasonCodeType._CF_enumeration.addEnumeration(unicode_value='DELAY', tag='DELAY')
AbrogationReasonCodeType.HOLD = AbrogationReasonCodeType._CF_enumeration.addEnumeration(unicode_value='HOLD', tag='HOLD')
AbrogationReasonCodeType._InitializeFacetMap(AbrogationReasonCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AbrogationReasonCodeType', AbrogationReasonCodeType)
_module_typeBindings.AbrogationReasonCodeType = AbrogationReasonCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}CoordinationStatusCodeType
class CoordinationStatusCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Coordination Status: The status of Coordination and Transfer of Control between 
            the currently Controlling Air Traffic Service Unit (ATSU) to the downstream to be 
            Controlling ATSU. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoordinationStatusCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 140, 3)
    _Documentation = '\n            .Coordination Status: The status of Coordination and Transfer of Control between \n            the currently Controlling Air Traffic Service Unit (ATSU) to the downstream to be \n            Controlling ATSU. \n         '
CoordinationStatusCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CoordinationStatusCodeType, enum_prefix=None)
CoordinationStatusCodeType.NOTIFIED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='NOTIFIED', tag='NOTIFIED')
CoordinationStatusCodeType.OFFERED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='OFFERED', tag='OFFERED')
CoordinationStatusCodeType.RENEGOTIATE_REQUESTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='RENEGOTIATE_REQUESTED', tag='RENEGOTIATE_REQUESTED')
CoordinationStatusCodeType.RENEGOTIATE_REJECTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='RENEGOTIATE_REJECTED', tag='RENEGOTIATE_REJECTED')
CoordinationStatusCodeType.COORDINATED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='COORDINATED', tag='COORDINATED')
CoordinationStatusCodeType.REJECTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='REJECTED', tag='REJECTED')
CoordinationStatusCodeType.REQUESTED_ON_FREQUENCY = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='REQUESTED_ON_FREQUENCY', tag='REQUESTED_ON_FREQUENCY')
CoordinationStatusCodeType.ASSUMED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='ASSUMED', tag='ASSUMED')
CoordinationStatusCodeType.BACKWARD_COORDINATING = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='BACKWARD_COORDINATING', tag='BACKWARD_COORDINATING')
CoordinationStatusCodeType.BACKWARD_COORDINATING_REJECTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='BACKWARD_COORDINATING_REJECTED', tag='BACKWARD_COORDINATING_REJECTED')
CoordinationStatusCodeType.BACKWARD_COORDINATING_ACCEPTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='BACKWARD_COORDINATING_ACCEPTED', tag='BACKWARD_COORDINATING_ACCEPTED')
CoordinationStatusCodeType.ABROGATED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='ABROGATED', tag='ABROGATED')
CoordinationStatusCodeType.ATSU_SKIPPED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='ATSU_SKIPPED', tag='ATSU_SKIPPED')
CoordinationStatusCodeType.FREQUENCY_CHANGED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='FREQUENCY_CHANGED', tag='FREQUENCY_CHANGED')
CoordinationStatusCodeType.RELEASE_REQUESTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='RELEASE_REQUESTED', tag='RELEASE_REQUESTED')
CoordinationStatusCodeType.RELEASE_REJECTED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='RELEASE_REJECTED', tag='RELEASE_REJECTED')
CoordinationStatusCodeType.RELEASED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='RELEASED', tag='RELEASED')
CoordinationStatusCodeType.MANUALLY_REFERRED = CoordinationStatusCodeType._CF_enumeration.addEnumeration(unicode_value='MANUALLY_REFERRED', tag='MANUALLY_REFERRED')
CoordinationStatusCodeType._InitializeFacetMap(CoordinationStatusCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CoordinationStatusCodeType', CoordinationStatusCodeType)
_module_typeBindings.CoordinationStatusCodeType = CoordinationStatusCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}NonStandardCoordinationReasonType
class NonStandardCoordinationReasonType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Reason for Non-Standard Coordination: In case of non-standard coordination, the 
            reason for non-standard coordination is indicated. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NonStandardCoordinationReasonType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 170, 3)
    _Documentation = '\n            .Reason for Non-Standard Coordination: In case of non-standard coordination, the \n            reason for non-standard coordination is indicated. \n         '
NonStandardCoordinationReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NonStandardCoordinationReasonType, enum_prefix=None)
NonStandardCoordinationReasonType.LATE_ACTIVATION = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='LATE_ACTIVATION', tag='LATE_ACTIVATION')
NonStandardCoordinationReasonType.LATERAL_DEVIATION = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='LATERAL_DEVIATION', tag='LATERAL_DEVIATION')
NonStandardCoordinationReasonType.LATE_REVISION = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='LATE_REVISION', tag='LATE_REVISION')
NonStandardCoordinationReasonType.NON_STANDARD_TFL = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='NON_STANDARD_TFL', tag='NON_STANDARD_TFL')
NonStandardCoordinationReasonType.NON_STANDARD_EQUIPMENT = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='NON_STANDARD_EQUIPMENT', tag='NON_STANDARD_EQUIPMENT')
NonStandardCoordinationReasonType.NON_STANDARD_SSR_CODE = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='NON_STANDARD_SSR_CODE', tag='NON_STANDARD_SSR_CODE')
NonStandardCoordinationReasonType.TRANSITION_POINT = NonStandardCoordinationReasonType._CF_enumeration.addEnumeration(unicode_value='TRANSITION_POINT', tag='TRANSITION_POINT')
NonStandardCoordinationReasonType._InitializeFacetMap(NonStandardCoordinationReasonType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NonStandardCoordinationReasonType', NonStandardCoordinationReasonType)
_module_typeBindings.NonStandardCoordinationReasonType = NonStandardCoordinationReasonType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}ReleaseConditionsType
class ReleaseConditionsType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Release Conditions: When the flight is released from the agreed transfer conditions, 
            contains the Release conditions specified by the transferring ATSUs.  The Release 
            conditions indicate the type of manoeuvres the flight is released to perform. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseConditionsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 188, 3)
    _Documentation = '\n            .Release Conditions: When the flight is released from the agreed transfer conditions, \n            contains the Release conditions specified by the transferring ATSUs.  The Release \n            conditions indicate the type of manoeuvres the flight is released to perform. \n         '
ReleaseConditionsType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseConditionsType, enum_prefix=None)
ReleaseConditionsType.CLIMB = ReleaseConditionsType._CF_enumeration.addEnumeration(unicode_value='CLIMB', tag='CLIMB')
ReleaseConditionsType.DESCENT = ReleaseConditionsType._CF_enumeration.addEnumeration(unicode_value='DESCENT', tag='DESCENT')
ReleaseConditionsType.TURNS = ReleaseConditionsType._CF_enumeration.addEnumeration(unicode_value='TURNS', tag='TURNS')
ReleaseConditionsType.FULL = ReleaseConditionsType._CF_enumeration.addEnumeration(unicode_value='FULL', tag='FULL')
ReleaseConditionsType._InitializeFacetMap(ReleaseConditionsType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseConditionsType', ReleaseConditionsType)
_module_typeBindings.ReleaseConditionsType = ReleaseConditionsType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}CpdlcConnectionStatusType
class CpdlcConnectionStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .CPDLC Connection Status: Provides the aircraft s Controller Pilot Data Link Communications 
            (CPDLC) Connection status and optional frequency information. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CpdlcConnectionStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 149, 3)
    _Documentation = '\n            .CPDLC Connection Status: Provides the aircraft s Controller Pilot Data Link Communications \n            (CPDLC) Connection status and optional frequency information. \n         '
CpdlcConnectionStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CpdlcConnectionStatusType, enum_prefix=None)
CpdlcConnectionStatusType.NO_CONNECTION = CpdlcConnectionStatusType._CF_enumeration.addEnumeration(unicode_value='NO_CONNECTION', tag='NO_CONNECTION')
CpdlcConnectionStatusType.CONNECTION_FAILED = CpdlcConnectionStatusType._CF_enumeration.addEnumeration(unicode_value='CONNECTION_FAILED', tag='CONNECTION_FAILED')
CpdlcConnectionStatusType.CONNECTION_ESTABLISHED = CpdlcConnectionStatusType._CF_enumeration.addEnumeration(unicode_value='CONNECTION_ESTABLISHED', tag='CONNECTION_ESTABLISHED')
CpdlcConnectionStatusType._InitializeFacetMap(CpdlcConnectionStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CpdlcConnectionStatusType', CpdlcConnectionStatusType)
_module_typeBindings.CpdlcConnectionStatusType = CpdlcConnectionStatusType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}CpdlcStartRequestIndicatorType
class CpdlcStartRequestIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .CPDLC Start Request Indicator: For a flight crossing the boundary from one facility 
            to the next, notifies the data link equipped unit it can send a CPDLC Start Request 
            to the aircraft, because the aircraft is authorized to accept a CPDLC connection 
            request from the receiving unit. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CpdlcStartRequestIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 163, 3)
    _Documentation = '\n            .CPDLC Start Request Indicator: For a flight crossing the boundary from one facility \n            to the next, notifies the data link equipped unit it can send a CPDLC Start Request \n            to the aircraft, because the aircraft is authorized to accept a CPDLC connection \n            request from the receiving unit. \n         '
CpdlcStartRequestIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CpdlcStartRequestIndicatorType, enum_prefix=None)
CpdlcStartRequestIndicatorType.SEND_CPDLC_START_REQUEST = CpdlcStartRequestIndicatorType._CF_enumeration.addEnumeration(unicode_value='SEND_CPDLC_START_REQUEST', tag='SEND_CPDLC_START_REQUEST')
CpdlcStartRequestIndicatorType._InitializeFacetMap(CpdlcStartRequestIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CpdlcStartRequestIndicatorType', CpdlcStartRequestIndicatorType)
_module_typeBindings.CpdlcStartRequestIndicatorType = CpdlcStartRequestIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}FrequencyUsageType
class FrequencyUsageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Frequency Usage: The usage of the frequency. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FrequencyUsageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 187, 3)
    _Documentation = '\n            .Frequency Usage: The usage of the frequency. \n         '
FrequencyUsageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FrequencyUsageType, enum_prefix=None)
FrequencyUsageType.VOICE = FrequencyUsageType._CF_enumeration.addEnumeration(unicode_value='VOICE', tag='VOICE')
FrequencyUsageType.CPDLC = FrequencyUsageType._CF_enumeration.addEnumeration(unicode_value='CPDLC', tag='CPDLC')
FrequencyUsageType._InitializeFacetMap(FrequencyUsageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FrequencyUsageType', FrequencyUsageType)
_module_typeBindings.FrequencyUsageType = FrequencyUsageType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}PositionReportSourceType
class PositionReportSourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Current Position Report Source: The source of the current position report information. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionReportSourceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 248, 3)
    _Documentation = '\n            .Current Position Report Source: The source of the current position report information. \n            \n         '
PositionReportSourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PositionReportSourceType, enum_prefix=None)
PositionReportSourceType.PROGRESS_REPORT = PositionReportSourceType._CF_enumeration.addEnumeration(unicode_value='PROGRESS_REPORT', tag='PROGRESS_REPORT')
PositionReportSourceType.SURVEILLANCE = PositionReportSourceType._CF_enumeration.addEnumeration(unicode_value='SURVEILLANCE', tag='SURVEILLANCE')
PositionReportSourceType._InitializeFacetMap(PositionReportSourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PositionReportSourceType', PositionReportSourceType)
_module_typeBindings.PositionReportSourceType = PositionReportSourceType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}LandingLimitsType
class LandingLimitsType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Landing Limits: The landing qualification of the flight, considering crew and equipment. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LandingLimitsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 252, 3)
    _Documentation = '\n            .Landing Limits: The landing qualification of the flight, considering crew and equipment. \n            \n         '
LandingLimitsType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LandingLimitsType, enum_prefix=None)
LandingLimitsType.I = LandingLimitsType._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
LandingLimitsType.II = LandingLimitsType._CF_enumeration.addEnumeration(unicode_value='II', tag='II')
LandingLimitsType.III = LandingLimitsType._CF_enumeration.addEnumeration(unicode_value='III', tag='III')
LandingLimitsType.IIIA = LandingLimitsType._CF_enumeration.addEnumeration(unicode_value='IIIA', tag='IIIA')
LandingLimitsType.IIIB = LandingLimitsType._CF_enumeration.addEnumeration(unicode_value='IIIB', tag='IIIB')
LandingLimitsType.IIIC = LandingLimitsType._CF_enumeration.addEnumeration(unicode_value='IIIC', tag='IIIC')
LandingLimitsType._InitializeFacetMap(LandingLimitsType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LandingLimitsType', LandingLimitsType)
_module_typeBindings.LandingLimitsType = LandingLimitsType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AltitudeQualifierType
class AltitudeQualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Specifies that the altitude specified in the ClimbToLevelConstraint is not a maximum 
            altitude, and aircraft may climb to a higher level. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltitudeQualifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 79, 3)
    _Documentation = '\n            Specifies that the altitude specified in the ClimbToLevelConstraint is not a maximum \n            altitude, and aircraft may climb to a higher level. \n         '
AltitudeQualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AltitudeQualifierType, enum_prefix=None)
AltitudeQualifierType.AT_OR_ABOVE_ALTITUDE = AltitudeQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_OR_ABOVE_ALTITUDE', tag='AT_OR_ABOVE_ALTITUDE')
AltitudeQualifierType._InitializeFacetMap(AltitudeQualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AltitudeQualifierType', AltitudeQualifierType)
_module_typeBindings.AltitudeQualifierType = AltitudeQualifierType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}ConstraintOrPreferenceCategoryType
class ConstraintOrPreferenceCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Constraint Category: Specifies the category (implying a relative importance) of 
            the constraint associated with a point in the route or expanded route. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConstraintOrPreferenceCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 138, 3)
    _Documentation = '\n            .Constraint Category: Specifies the category (implying a relative importance) of \n            the constraint associated with a point in the route or expanded route. \n         '
ConstraintOrPreferenceCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConstraintOrPreferenceCategoryType, enum_prefix=None)
ConstraintOrPreferenceCategoryType.EXECUTIVE_CONTROL = ConstraintOrPreferenceCategoryType._CF_enumeration.addEnumeration(unicode_value='EXECUTIVE_CONTROL', tag='EXECUTIVE_CONTROL')
ConstraintOrPreferenceCategoryType.CONTROLLER_TACTICAL_PLANNING = ConstraintOrPreferenceCategoryType._CF_enumeration.addEnumeration(unicode_value='CONTROLLER_TACTICAL_PLANNING', tag='CONTROLLER_TACTICAL_PLANNING')
ConstraintOrPreferenceCategoryType.NETWORK_STRATEGIC = ConstraintOrPreferenceCategoryType._CF_enumeration.addEnumeration(unicode_value='NETWORK_STRATEGIC', tag='NETWORK_STRATEGIC')
ConstraintOrPreferenceCategoryType.OPERATOR_CONSTRAINT = ConstraintOrPreferenceCategoryType._CF_enumeration.addEnumeration(unicode_value='OPERATOR_CONSTRAINT', tag='OPERATOR_CONSTRAINT')
ConstraintOrPreferenceCategoryType.FLIGHT_PLAN_EXPECTATION = ConstraintOrPreferenceCategoryType._CF_enumeration.addEnumeration(unicode_value='FLIGHT_PLAN_EXPECTATION', tag='FLIGHT_PLAN_EXPECTATION')
ConstraintOrPreferenceCategoryType._InitializeFacetMap(ConstraintOrPreferenceCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ConstraintOrPreferenceCategoryType', ConstraintOrPreferenceCategoryType)
_module_typeBindings.ConstraintOrPreferenceCategoryType = ConstraintOrPreferenceCategoryType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}PositionQualifierType
class PositionQualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Qualifies the position associated with the constraint. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PositionQualifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 195, 3)
    _Documentation = '\n            Qualifies the position associated with the constraint. \n         '
PositionQualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PositionQualifierType, enum_prefix=None)
PositionQualifierType.AT_OR_BEFORE_POINT = PositionQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_OR_BEFORE_POINT', tag='AT_OR_BEFORE_POINT')
PositionQualifierType.AT_POINT = PositionQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_POINT', tag='AT_POINT')
PositionQualifierType.AT_OR_AFTER_POINT = PositionQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_OR_AFTER_POINT', tag='AT_OR_AFTER_POINT')
PositionQualifierType._InitializeFacetMap(PositionQualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PositionQualifierType', PositionQualifierType)
_module_typeBindings.PositionQualifierType = PositionQualifierType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}TimeQualifierType
class TimeQualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Qualifies the time associated with the constraint. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeQualifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 299, 3)
    _Documentation = '\n            Qualifies the time associated with the constraint. \n         '
TimeQualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TimeQualifierType, enum_prefix=None)
TimeQualifierType.AT_OR_BEFORE_TIME = TimeQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_OR_BEFORE_TIME', tag='AT_OR_BEFORE_TIME')
TimeQualifierType.AT_TIME = TimeQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_TIME', tag='AT_TIME')
TimeQualifierType.AT_OR_AFTER_TIME = TimeQualifierType._CF_enumeration.addEnumeration(unicode_value='AT_OR_AFTER_TIME', tag='AT_OR_AFTER_TIME')
TimeQualifierType.UNTIL_TIME = TimeQualifierType._CF_enumeration.addEnumeration(unicode_value='UNTIL_TIME', tag='UNTIL_TIME')
TimeQualifierType._InitializeFacetMap(TimeQualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TimeQualifierType', TimeQualifierType)
_module_typeBindings.TimeQualifierType = TimeQualifierType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}EmergencyPhaseType
class EmergencyPhaseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Emergency Phase: Stage of emergency the flight is currently under or an indication 
            the emergency has been cancelled, as designated by an ATS unit. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EmergencyPhaseType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 80, 3)
    _Documentation = '\n            .Emergency Phase: Stage of emergency the flight is currently under or an indication \n            the emergency has been cancelled, as designated by an ATS unit. \n         '
EmergencyPhaseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EmergencyPhaseType, enum_prefix=None)
EmergencyPhaseType.INCERFA = EmergencyPhaseType._CF_enumeration.addEnumeration(unicode_value='INCERFA', tag='INCERFA')
EmergencyPhaseType.ALERFA = EmergencyPhaseType._CF_enumeration.addEnumeration(unicode_value='ALERFA', tag='ALERFA')
EmergencyPhaseType.DETRESFA = EmergencyPhaseType._CF_enumeration.addEnumeration(unicode_value='DETRESFA', tag='DETRESFA')
EmergencyPhaseType.CANCELLED = EmergencyPhaseType._CF_enumeration.addEnumeration(unicode_value='CANCELLED', tag='CANCELLED')
EmergencyPhaseType._InitializeFacetMap(EmergencyPhaseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EmergencyPhaseType', EmergencyPhaseType)
_module_typeBindings.EmergencyPhaseType = EmergencyPhaseType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}OperatorCategoryType
class OperatorCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Flight Operator Category: The category of the flight operator operating the flight. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperatorCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 392, 3)
    _Documentation = '\n            .Flight Operator Category: The category of the flight operator operating the flight. \n            \n         '
OperatorCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OperatorCategoryType, enum_prefix=None)
OperatorCategoryType.AIR_CARRIER = OperatorCategoryType._CF_enumeration.addEnumeration(unicode_value='AIR_CARRIER', tag='AIR_CARRIER')
OperatorCategoryType.FREIGHT_CARGO_CARRIER = OperatorCategoryType._CF_enumeration.addEnumeration(unicode_value='FREIGHT_CARGO_CARRIER', tag='FREIGHT_CARGO_CARRIER')
OperatorCategoryType.GENERAL_AVIATION = OperatorCategoryType._CF_enumeration.addEnumeration(unicode_value='GENERAL_AVIATION', tag='GENERAL_AVIATION')
OperatorCategoryType.MILITARY = OperatorCategoryType._CF_enumeration.addEnumeration(unicode_value='MILITARY', tag='MILITARY')
OperatorCategoryType.AIR_TAXI = OperatorCategoryType._CF_enumeration.addEnumeration(unicode_value='AIR_TAXI', tag='AIR_TAXI')
OperatorCategoryType.OTHER = OperatorCategoryType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
OperatorCategoryType._InitializeFacetMap(OperatorCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OperatorCategoryType', OperatorCategoryType)
_module_typeBindings.OperatorCategoryType = OperatorCategoryType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}SpecialHandlingCodeType
class SpecialHandlingCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Special Handling Reason: A property of the flight that requires ATS units to give 
            it special consideration. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpecialHandlingCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 441, 3)
    _Documentation = '\n            .Special Handling Reason: A property of the flight that requires ATS units to give \n            it special consideration. \n         '
SpecialHandlingCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpecialHandlingCodeType, enum_prefix=None)
SpecialHandlingCodeType.ALTRV = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='ALTRV', tag='ALTRV')
SpecialHandlingCodeType.ATFMX = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='ATFMX', tag='ATFMX')
SpecialHandlingCodeType.FFR = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='FFR', tag='FFR')
SpecialHandlingCodeType.FLTCK = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='FLTCK', tag='FLTCK')
SpecialHandlingCodeType.HAZMAT = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='HAZMAT', tag='HAZMAT')
SpecialHandlingCodeType.HEAD = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='HEAD', tag='HEAD')
SpecialHandlingCodeType.HOSP = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='HOSP', tag='HOSP')
SpecialHandlingCodeType.HUM = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='HUM', tag='HUM')
SpecialHandlingCodeType.MARSA = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='MARSA', tag='MARSA')
SpecialHandlingCodeType.MEDEVAC = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='MEDEVAC', tag='MEDEVAC')
SpecialHandlingCodeType.NONRVSM = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='NONRVSM', tag='NONRVSM')
SpecialHandlingCodeType.SAR = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='SAR', tag='SAR')
SpecialHandlingCodeType.STATE = SpecialHandlingCodeType._CF_enumeration.addEnumeration(unicode_value='STATE', tag='STATE')
SpecialHandlingCodeType._InitializeFacetMap(SpecialHandlingCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SpecialHandlingCodeType', SpecialHandlingCodeType)
_module_typeBindings.SpecialHandlingCodeType = SpecialHandlingCodeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}TypeOfFlightType
class TypeOfFlightType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Flight Type: Indication of the rule under which an air traffic controller provides 
            categorical handling of a flight. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeOfFlightType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 499, 3)
    _Documentation = '\n            .Flight Type: Indication of the rule under which an air traffic controller provides \n            categorical handling of a flight. \n         '
TypeOfFlightType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TypeOfFlightType, enum_prefix=None)
TypeOfFlightType.MILITARY = TypeOfFlightType._CF_enumeration.addEnumeration(unicode_value='MILITARY', tag='MILITARY')
TypeOfFlightType.GENERAL = TypeOfFlightType._CF_enumeration.addEnumeration(unicode_value='GENERAL', tag='GENERAL')
TypeOfFlightType.NON_SCHEDULED = TypeOfFlightType._CF_enumeration.addEnumeration(unicode_value='NON_SCHEDULED', tag='NON_SCHEDULED')
TypeOfFlightType.SCHEDULED = TypeOfFlightType._CF_enumeration.addEnumeration(unicode_value='SCHEDULED', tag='SCHEDULED')
TypeOfFlightType.OTHER = TypeOfFlightType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
TypeOfFlightType._InitializeFacetMap(TypeOfFlightType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TypeOfFlightType', TypeOfFlightType)
_module_typeBindings.TypeOfFlightType = TypeOfFlightType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AssignedIndicatorType
class AssignedIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Ranked 4D Trajectory Assignment Status: An indication whether the Ranked 4D trajectory 
            has been assigned by the Air Navigation Service Provider (ANSP). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssignedIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 79, 3)
    _Documentation = '\n            .Ranked 4D Trajectory Assignment Status: An indication whether the Ranked 4D trajectory \n            has been assigned by the Air Navigation Service Provider (ANSP). \n         '
AssignedIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssignedIndicatorType, enum_prefix=None)
AssignedIndicatorType.ASSIGNED = AssignedIndicatorType._CF_enumeration.addEnumeration(unicode_value='ASSIGNED', tag='ASSIGNED')
AssignedIndicatorType._InitializeFacetMap(AssignedIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AssignedIndicatorType', AssignedIndicatorType)
_module_typeBindings.AssignedIndicatorType = AssignedIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}ClearanceLimitIndicatorType
class ClearanceLimitIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Clearance Limit:  The point to which an aircraft is granted an air traffic control 
            clearance. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClearanceLimitIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 135, 3)
    _Documentation = '\n            .Clearance Limit:  The point to which an aircraft is granted an air traffic control \n            clearance. \n         '
ClearanceLimitIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ClearanceLimitIndicatorType, enum_prefix=None)
ClearanceLimitIndicatorType.CLEARANCE_LIMIT = ClearanceLimitIndicatorType._CF_enumeration.addEnumeration(unicode_value='CLEARANCE_LIMIT', tag='CLEARANCE_LIMIT')
ClearanceLimitIndicatorType._InitializeFacetMap(ClearanceLimitIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ClearanceLimitIndicatorType', ClearanceLimitIndicatorType)
_module_typeBindings.ClearanceLimitIndicatorType = ClearanceLimitIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AirborneHoldIndicatorType
class AirborneHoldIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Hold State - Airborne Indicator: Specifies whether or not the aircraft is in an 
            airborne hold. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirborneHoldIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 78, 3)
    _Documentation = '\n            .Hold State - Airborne Indicator: Specifies whether or not the aircraft is in an \n            airborne hold. \n         '
AirborneHoldIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AirborneHoldIndicatorType, enum_prefix=None)
AirborneHoldIndicatorType.AIRBORNE_HOLD = AirborneHoldIndicatorType._CF_enumeration.addEnumeration(unicode_value='AIRBORNE_HOLD', tag='AIRBORNE_HOLD')
AirborneHoldIndicatorType.NOT_AIRBORNE_HOLD = AirborneHoldIndicatorType._CF_enumeration.addEnumeration(unicode_value='NOT_AIRBORNE_HOLD', tag='NOT_AIRBORNE_HOLD')
AirborneHoldIndicatorType._InitializeFacetMap(AirborneHoldIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AirborneHoldIndicatorType', AirborneHoldIndicatorType)
_module_typeBindings.AirborneHoldIndicatorType = AirborneHoldIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AirfileIndicatorType
class AirfileIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Airfile Indicator: An indication the information about this flight was filed from 
            the air. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirfileIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 91, 3)
    _Documentation = '\n            .Airfile Indicator: An indication the information about this flight was filed from \n            the air. \n         '
AirfileIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AirfileIndicatorType, enum_prefix=None)
AirfileIndicatorType.AIRFILE = AirfileIndicatorType._CF_enumeration.addEnumeration(unicode_value='AIRFILE', tag='AIRFILE')
AirfileIndicatorType._InitializeFacetMap(AirfileIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AirfileIndicatorType', AirfileIndicatorType)
_module_typeBindings.AirfileIndicatorType = AirfileIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}FlightAcceptedIndicatorType
class FlightAcceptedIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Flight Plan Accepted: An indicator of acceptance of the flight plan by the appropriate 
            ATS authority. 
            .Flight Plan Accepted Indicator: An indicator of acceptance of the flight plan by 
            the appropriate ATS authority. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightAcceptedIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 103, 3)
    _Documentation = '\n            .Flight Plan Accepted: An indicator of acceptance of the flight plan by the appropriate \n            ATS authority. \n            .Flight Plan Accepted Indicator: An indicator of acceptance of the flight plan by \n            the appropriate ATS authority. \n         '
FlightAcceptedIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FlightAcceptedIndicatorType, enum_prefix=None)
FlightAcceptedIndicatorType.ACCEPTED = FlightAcceptedIndicatorType._CF_enumeration.addEnumeration(unicode_value='ACCEPTED', tag='ACCEPTED')
FlightAcceptedIndicatorType._InitializeFacetMap(FlightAcceptedIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FlightAcceptedIndicatorType', FlightAcceptedIndicatorType)
_module_typeBindings.FlightAcceptedIndicatorType = FlightAcceptedIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}FlightCycleType
class FlightCycleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Flight Cycle is contains a mutually exclusive set of values representing stages of 
            flight. 
            .Flight Completed Indicator: An indicator that the flight was airborne and is now 
            completed. 
            .Flight Cancelled Indicator: Indication the flight has been cancelled after Flight 
            Object creation. 
            .Flight Filed Indicator: An indicator that flight information was filed to the appropriate 
            Air Traffic Services authority. 
            .Airborne Indicator: An indication of whether the flight is airborne or not. 
            .Flight Scheduled Indicator: An indicator a flight has been created in the Air Traffic 
            Services system and is expected to operate. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightCycleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 117, 3)
    _Documentation = '\n            Flight Cycle is contains a mutually exclusive set of values representing stages of \n            flight. \n            .Flight Completed Indicator: An indicator that the flight was airborne and is now \n            completed. \n            .Flight Cancelled Indicator: Indication the flight has been cancelled after Flight \n            Object creation. \n            .Flight Filed Indicator: An indicator that flight information was filed to the appropriate \n            Air Traffic Services authority. \n            .Airborne Indicator: An indication of whether the flight is airborne or not. \n            .Flight Scheduled Indicator: An indicator a flight has been created in the Air Traffic \n            Services system and is expected to operate. \n         '
FlightCycleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FlightCycleType, enum_prefix=None)
FlightCycleType.FILED = FlightCycleType._CF_enumeration.addEnumeration(unicode_value='FILED', tag='FILED')
FlightCycleType.SCHEDULED = FlightCycleType._CF_enumeration.addEnumeration(unicode_value='SCHEDULED', tag='SCHEDULED')
FlightCycleType.AIRBORNE = FlightCycleType._CF_enumeration.addEnumeration(unicode_value='AIRBORNE', tag='AIRBORNE')
FlightCycleType.COMPLETED = FlightCycleType._CF_enumeration.addEnumeration(unicode_value='COMPLETED', tag='COMPLETED')
FlightCycleType.CANCELLED = FlightCycleType._CF_enumeration.addEnumeration(unicode_value='CANCELLED', tag='CANCELLED')
FlightCycleType._InitializeFacetMap(FlightCycleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FlightCycleType', FlightCycleType)
_module_typeBindings.FlightCycleType = FlightCycleType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}FlightSuspendedIndicatorType
class FlightSuspendedIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Flight Suspended Indicator: An indicator a flight has been suspended in the Air 
            Traffic Services system. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightSuspendedIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 212, 3)
    _Documentation = '\n            .Flight Suspended Indicator: An indicator a flight has been suspended in the Air \n            Traffic Services system. \n         '
FlightSuspendedIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FlightSuspendedIndicatorType, enum_prefix=None)
FlightSuspendedIndicatorType.SUSPENDED = FlightSuspendedIndicatorType._CF_enumeration.addEnumeration(unicode_value='SUSPENDED', tag='SUSPENDED')
FlightSuspendedIndicatorType.NOT_SUSPENDED = FlightSuspendedIndicatorType._CF_enumeration.addEnumeration(unicode_value='NOT_SUSPENDED', tag='NOT_SUSPENDED')
FlightSuspendedIndicatorType._InitializeFacetMap(FlightSuspendedIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FlightSuspendedIndicatorType', FlightSuspendedIndicatorType)
_module_typeBindings.FlightSuspendedIndicatorType = FlightSuspendedIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}MissedApproachIndicatorType
class MissedApproachIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Missed Approach Indicator: An indicator that a flight executed a missed approach. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MissedApproachIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 225, 3)
    _Documentation = '\n            .Missed Approach Indicator: An indicator that a flight executed a missed approach. \n            \n         '
MissedApproachIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MissedApproachIndicatorType, enum_prefix=None)
MissedApproachIndicatorType.MISSED_APPROACH = MissedApproachIndicatorType._CF_enumeration.addEnumeration(unicode_value='MISSED_APPROACH', tag='MISSED_APPROACH')
MissedApproachIndicatorType._InitializeFacetMap(MissedApproachIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MissedApproachIndicatorType', MissedApproachIndicatorType)
_module_typeBindings.MissedApproachIndicatorType = MissedApproachIndicatorType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}TrajectoryChangePointTypeType
class TrajectoryChangePointTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Trajectory Change Point - Type: Identifies the type(s) of trajectory change point 
            being described by the associated 4D Point. 
            .Trajectory Change Point - Type: Identifies the type(s) of trajectory change point 
            being described by the associated 4D Point. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajectoryChangePointTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 265, 3)
    _Documentation = '\n            Trajectory Change Point - Type: Identifies the type(s) of trajectory change point \n            being described by the associated 4D Point. \n            .Trajectory Change Point - Type: Identifies the type(s) of trajectory change point \n            being described by the associated 4D Point. \n         '
TrajectoryChangePointTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TrajectoryChangePointTypeType, enum_prefix=None)
TrajectoryChangePointTypeType.START_OF_CLIMB = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='START_OF_CLIMB', tag='START_OF_CLIMB')
TrajectoryChangePointTypeType.TOP_OF_CLIMB = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='TOP_OF_CLIMB', tag='TOP_OF_CLIMB')
TrajectoryChangePointTypeType.START_OF_DESCENT = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='START_OF_DESCENT', tag='START_OF_DESCENT')
TrajectoryChangePointTypeType.END_OF_DESCENT = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='END_OF_DESCENT', tag='END_OF_DESCENT')
TrajectoryChangePointTypeType.LEVEL_OFF = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='LEVEL_OFF', tag='LEVEL_OFF')
TrajectoryChangePointTypeType.CROSSOVER_ALTITUDE = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='CROSSOVER_ALTITUDE', tag='CROSSOVER_ALTITUDE')
TrajectoryChangePointTypeType.TRANSITION_ALTITUDE = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='TRANSITION_ALTITUDE', tag='TRANSITION_ALTITUDE')
TrajectoryChangePointTypeType.SPEED_CHANGE = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='SPEED_CHANGE', tag='SPEED_CHANGE')
TrajectoryChangePointTypeType.UNNAMED_FIX = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='UNNAMED_FIX', tag='UNNAMED_FIX')
TrajectoryChangePointTypeType.RUNWAY = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='RUNWAY', tag='RUNWAY')
TrajectoryChangePointTypeType.ENTRY_SPECIAL_ACTIVITY_AIRSPACE = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='ENTRY_SPECIAL_ACTIVITY_AIRSPACE', tag='ENTRY_SPECIAL_ACTIVITY_AIRSPACE')
TrajectoryChangePointTypeType.EXIT_SPECIAL_ACTIVITY_AIRSPACE = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='EXIT_SPECIAL_ACTIVITY_AIRSPACE', tag='EXIT_SPECIAL_ACTIVITY_AIRSPACE')
TrajectoryChangePointTypeType.CROSSING_CONSTRAINED_AIRSPACE = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='CROSSING_CONSTRAINED_AIRSPACE', tag='CROSSING_CONSTRAINED_AIRSPACE')
TrajectoryChangePointTypeType.ENTER_HOLD = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='ENTER_HOLD', tag='ENTER_HOLD')
TrajectoryChangePointTypeType.INITIAL_PREDICTION = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='INITIAL_PREDICTION', tag='INITIAL_PREDICTION')
TrajectoryChangePointTypeType.EXIT_HOLD = TrajectoryChangePointTypeType._CF_enumeration.addEnumeration(unicode_value='EXIT_HOLD', tag='EXIT_HOLD')
TrajectoryChangePointTypeType._InitializeFacetMap(TrajectoryChangePointTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TrajectoryChangePointTypeType', TrajectoryChangePointTypeType)
_module_typeBindings.TrajectoryChangePointTypeType = TrajectoryChangePointTypeType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AircraftAddressType
class AircraftAddressType (_ImportedBinding__fb.FreeTextType):

    """
            .Aircraft Address: A code that enables the exchange of text-based messages between 
            suitably equipped Air Traffic Service (ATS) ground systems and aircraft cockpit displays. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftAddressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 173, 3)
    _Documentation = '\n            .Aircraft Address: A code that enables the exchange of text-based messages between \n            suitably equipped Air Traffic Service (ATS) ground systems and aircraft cockpit displays. \n            \n         '
AircraftAddressType._CF_pattern = pyxb.binding.facets.CF_pattern()
AircraftAddressType._CF_pattern.addPattern(pattern='[0-9A-F]{6}')
AircraftAddressType._InitializeFacetMap(AircraftAddressType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AircraftAddressType', AircraftAddressType)
_module_typeBindings.AircraftAddressType = AircraftAddressType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AircraftRegistrationType
class AircraftRegistrationType (_ImportedBinding__fb.FreeTextType):

    """
            .Aircraft Registration Mark: A unique, alphanumeric string that identifies a civil 
            aircraft and consists of the Aircraft Nationality or Common Mark and an additional 
            alphanumeric string assigned by the state of registry or common mark registering 
            authority. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftRegistrationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 257, 3)
    _Documentation = '\n            .Aircraft Registration Mark: A unique, alphanumeric string that identifies a civil \n            aircraft and consists of the Aircraft Nationality or Common Mark and an additional \n            alphanumeric string assigned by the state of registry or common mark registering \n            authority. \n         '
AircraftRegistrationType._CF_pattern = pyxb.binding.facets.CF_pattern()
AircraftRegistrationType._CF_pattern.addPattern(pattern='[A-Z0-9]{1,7}')
AircraftRegistrationType._InitializeFacetMap(AircraftRegistrationType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AircraftRegistrationType', AircraftRegistrationType)
_module_typeBindings.AircraftRegistrationType = AircraftRegistrationType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON (pyxb.binding.basis.STD_list):

    """Simple type that is a list of CommunicationCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 94, 12)
    _Documentation = None

    _ItemType = CommunicationCodeType
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_ (pyxb.binding.basis.STD_list):

    """Simple type that is a list of DataLinkCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 106, 12)
    _Documentation = None

    _ItemType = DataLinkCodeType
STD_ANON_._InitializeFacetMap()
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://www.fixm.aero/flight/3.0}SelectiveCallingCodeType
class SelectiveCallingCodeType (_ImportedBinding__fb.FreeTextType):

    """
            .Selective Calling Code: A code that consists of two 2-letter pairs and acts as a 
            paging system for an ATS unit to establish voice communications with the pilot of 
            an aircraft. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SelectiveCallingCodeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 185, 3)
    _Documentation = '\n            .Selective Calling Code: A code that consists of two 2-letter pairs and acts as a \n            paging system for an ATS unit to establish voice communications with the pilot of \n            an aircraft. \n         '
SelectiveCallingCodeType._CF_pattern = pyxb.binding.facets.CF_pattern()
SelectiveCallingCodeType._CF_pattern.addPattern(pattern='[A-HJ-MP-S]{4}')
SelectiveCallingCodeType._InitializeFacetMap(SelectiveCallingCodeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SelectiveCallingCodeType', SelectiveCallingCodeType)
_module_typeBindings.SelectiveCallingCodeType = SelectiveCallingCodeType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_2 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of NavigationCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 92, 12)
    _Documentation = None

    _ItemType = NavigationCodeType
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_3 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of PerformanceBasedCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 105, 12)
    _Documentation = None

    _ItemType = PerformanceBasedCodeType
STD_ANON_3._InitializeFacetMap()
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_4 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of SurveillanceCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 93, 12)
    _Documentation = None

    _ItemType = SurveillanceCodeType
STD_ANON_4._InitializeFacetMap()
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_5 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of EmergencyRadioCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 227, 12)
    _Documentation = None

    _ItemType = EmergencyRadioCodeType
STD_ANON_5._InitializeFacetMap()
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_6 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of LifeJacketCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 237, 12)
    _Documentation = None

    _ItemType = LifeJacketCodeType
STD_ANON_6._InitializeFacetMap()
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_7 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of SurvivalEquipmentCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 249, 12)
    _Documentation = None

    _ItemType = SurvivalEquipmentCodeType
STD_ANON_7._InitializeFacetMap()
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 213, 15)
    _Documentation = None
STD_ANON_8._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_8._CF_pattern.addPattern(pattern='[#\\d+|\\d+]')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_pattern)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_9 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of _ImportedBinding__ff.AerodromeIcaoCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 368, 12)
    _Documentation = None

    _ItemType = _ImportedBinding__ff.AerodromeIcaoCodeType
STD_ANON_9._InitializeFacetMap()
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (_ImportedBinding__fb.DecimalIndexType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 103, 9)
    _Documentation = None
STD_ANON_10._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_10, value=pyxb.binding.datatypes.decimal('0.0'))
STD_ANON_10._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_10, value=pyxb.binding.datatypes.decimal('1.0'))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_minInclusive,
   STD_ANON_10._CF_maxInclusive)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: {http://www.fixm.aero/flight/3.0}CompatibilityGroupType
class CompatibilityGroupType (_ImportedBinding__fb.FreeTextType):

    """
            .Compatibility Group: When shipping dangerous goods, the reference to the group which 
            identifies the kind of substances and articles deemed to be compatible. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompatibilityGroupType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 113, 3)
    _Documentation = '\n            .Compatibility Group: When shipping dangerous goods, the reference to the group which \n            identifies the kind of substances and articles deemed to be compatible. \n         '
CompatibilityGroupType._CF_pattern = pyxb.binding.facets.CF_pattern()
CompatibilityGroupType._CF_pattern.addPattern(pattern='[A-H|K-L|N|S]')
CompatibilityGroupType._InitializeFacetMap(CompatibilityGroupType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CompatibilityGroupType', CompatibilityGroupType)
_module_typeBindings.CompatibilityGroupType = CompatibilityGroupType

# Atomic simple type: [anonymous]
class STD_ANON_11 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 297, 9)
    _Documentation = None
STD_ANON_11._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_11._CF_pattern.addPattern(pattern='Y?[0-9]{3}')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_pattern)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 369, 9)
    _Documentation = None
STD_ANON_12._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_12._CF_pattern.addPattern(pattern='(UN|ID|NA)?\\d{4}')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_pattern)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (_ImportedBinding__fb.CountType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 436, 15)
    _Documentation = None
STD_ANON_13._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_13, value=pyxb.binding.datatypes.int(0))
STD_ANON_13._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_13, value=pyxb.binding.datatypes.int(99))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_minInclusive,
   STD_ANON_13._CF_maxInclusive)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: {http://www.fixm.aero/flight/3.0}RestrictedHazardClassType
class RestrictedHazardClassType (_ImportedBinding__fb.CountType):

    """
            Helper type for restrictions on HazardClassType 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RestrictedHazardClassType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 447, 3)
    _Documentation = '\n            Helper type for restrictions on HazardClassType \n         '
RestrictedHazardClassType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=RestrictedHazardClassType, value=pyxb.binding.datatypes.int(1))
RestrictedHazardClassType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=RestrictedHazardClassType, value=pyxb.binding.datatypes.int(9))
RestrictedHazardClassType._InitializeFacetMap(RestrictedHazardClassType._CF_minInclusive,
   RestrictedHazardClassType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'RestrictedHazardClassType', RestrictedHazardClassType)
_module_typeBindings.RestrictedHazardClassType = RestrictedHazardClassType

# Atomic simple type: [anonymous]
class STD_ANON_14 (_ImportedBinding__fb.DecimalIndexType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 155, 9)
    _Documentation = None
STD_ANON_14._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_14, value=pyxb.binding.datatypes.decimal('0.0'))
STD_ANON_14._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_14, value=pyxb.binding.datatypes.decimal('100.0'))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_minInclusive,
   STD_ANON_14._CF_maxInclusive)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (_ImportedBinding__fb.DecimalIndexType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 177, 9)
    _Documentation = None
STD_ANON_15._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_15, value=pyxb.binding.datatypes.decimal('0.0'))
STD_ANON_15._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_15, value=pyxb.binding.datatypes.decimal('50.0'))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_minInclusive,
   STD_ANON_15._CF_maxInclusive)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 307, 9)
    _Documentation = None
STD_ANON_16._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_16._CF_pattern.addPattern(pattern='(UN)|(ID)|(NA)?\\d{4}')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_pattern)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: {http://www.fixm.aero/flight/3.0}AtnLogonParametersType
class AtnLogonParametersType (_ImportedBinding__fb.ParametersType):

    """
            .ATN Logon Parameters:  The ATN logon parameters allow the ground unit to log on 
            to the data link equipped aircraft to use the data link applications. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtnLogonParametersType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 80, 3)
    _Documentation = '\n            .ATN Logon Parameters:  The ATN logon parameters allow the ground unit to log on \n            to the data link equipped aircraft to use the data link applications. \n         '
AtnLogonParametersType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AtnLogonParametersType', AtnLogonParametersType)
_module_typeBindings.AtnLogonParametersType = AtnLogonParametersType

# Atomic simple type: {http://www.fixm.aero/flight/3.0}Fans1ALogonParametersType
class Fans1ALogonParametersType (_ImportedBinding__fb.ParametersType):

    """
            .FANS/1A Logon Parameters:  The information necessary to establish CPDLC and/or ADS-C 
            connections with a FANS equipped aircraft. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Fans1ALogonParametersType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 177, 3)
    _Documentation = '\n            .FANS/1A Logon Parameters:  The information necessary to establish CPDLC and/or ADS-C \n            connections with a FANS equipped aircraft. \n         '
Fans1ALogonParametersType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Fans1ALogonParametersType', Fans1ALogonParametersType)
_module_typeBindings.Fans1ALogonParametersType = Fans1ALogonParametersType

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_17 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of SpecialHandlingCodeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 312, 18)
    _Documentation = None

    _ItemType = SpecialHandlingCodeType
STD_ANON_17._InitializeFacetMap()
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_18 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of _ImportedBinding__fb.FlightIdentifierType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 368, 12)
    _Documentation = None

    _ItemType = _ImportedBinding__fb.FlightIdentifierType
STD_ANON_18._InitializeFacetMap()
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 127, 9)
    _Documentation = None
STD_ANON_19._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_19._CF_pattern.addPattern(pattern='[0-9]{1,2}')
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_pattern)
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_20 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of TrajectoryChangePointTypeType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 367, 12)
    _Documentation = None

    _ItemType = TrajectoryChangePointTypeType
STD_ANON_20._InitializeFacetMap()
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Complex type {http://www.fixm.aero/flight/3.0}AircraftTypeType with content type ELEMENT_ONLY
class AircraftTypeType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Aircraft Type: The manufacturer and model of the airframe expressed either as an 
            ICAO-approved designator or a text description. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 271, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element icaoModelIdentifier uses Python identifier icaoModelIdentifier
    __icaoModelIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'icaoModelIdentifier'), 'icaoModelIdentifier', '__httpwww_fixm_aeroflight3_0_AircraftTypeType_icaoModelIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 279, 9), )

    
    icaoModelIdentifier = property(__icaoModelIdentifier.value, __icaoModelIdentifier.set, None, '\n                  The ICAO code of the aircraft type \n               ')

    
    # Element otherModelData uses Python identifier otherModelData
    __otherModelData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'otherModelData'), 'otherModelData', '__httpwww_fixm_aeroflight3_0_AircraftTypeType_otherModelData', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 286, 9), )

    
    otherModelData = property(__otherModelData.value, __otherModelData.set, None, '\n                  Other, non-ICAO identification of the aircraft type. \n               ')

    _ElementMap.update({
        __icaoModelIdentifier.name() : __icaoModelIdentifier,
        __otherModelData.name() : __otherModelData
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AircraftTypeType = AircraftTypeType
Namespace.addCategoryObject('typeBinding', 'AircraftTypeType', AircraftTypeType)


# Complex type {http://www.fixm.aero/flight/3.0}DinghyColourType with content type ELEMENT_ONLY
class DinghyColourType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Dinghy Colour: The colour of the dinghies carried by the aircraft. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DinghyColourType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 121, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element colourCode uses Python identifier colourCode
    __colourCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'colourCode'), 'colourCode', '__httpwww_fixm_aeroflight3_0_DinghyColourType_colourCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 128, 9), )

    
    colourCode = property(__colourCode.value, __colourCode.set, None, '\n                  .Dinghy Color: The color of the dinghies carried by the aircraft. \n               ')

    
    # Element otherColour uses Python identifier otherColour
    __otherColour = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'otherColour'), 'otherColour', '__httpwww_fixm_aeroflight3_0_DinghyColourType_otherColour', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 135, 9), )

    
    otherColour = property(__otherColour.value, __otherColour.set, None, '\n                  Any other color of the dinghy that is not among the standards set. \n               ')

    _ElementMap.update({
        __colourCode.name() : __colourCode,
        __otherColour.name() : __otherColour
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DinghyColourType = DinghyColourType
Namespace.addCategoryObject('typeBinding', 'DinghyColourType', DinghyColourType)


# Complex type {http://www.fixm.aero/flight/3.0}AdditionalHandlingInformationType with content type ELEMENT_ONLY
class AdditionalHandlingInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Additional Handling Information: Additional information related to the handling 
            of dangerous goods, as identified on the Shipper's Declaration for Dangerous Goods. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdditionalHandlingInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 82, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element responsibleAgent uses Python identifier responsibleAgent
    __responsibleAgent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'responsibleAgent'), 'responsibleAgent', '__httpwww_fixm_aeroflight3_0_AdditionalHandlingInformationType_responsibleAgent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 91, 9), )

    
    responsibleAgent = property(__responsibleAgent.value, __responsibleAgent.set, None, '\n                  Person or organization responsible for infectious substances. \n               ')

    _ElementMap.update({
        __responsibleAgent.name() : __responsibleAgent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AdditionalHandlingInformationType = AdditionalHandlingInformationType
Namespace.addCategoryObject('typeBinding', 'AdditionalHandlingInformationType', AdditionalHandlingInformationType)


# Complex type {http://www.fixm.aero/flight/3.0}DangerousGoodsDimensionsType with content type ELEMENT_ONLY
class DangerousGoodsDimensionsType (pyxb.binding.basis.complexTypeDefinition):
    """
            Weight and volume (not height, width, and depth): 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsDimensionsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 125, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element grossWeight uses Python identifier grossWeight
    __grossWeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'grossWeight'), 'grossWeight', '__httpwww_fixm_aeroflight3_0_DangerousGoodsDimensionsType_grossWeight', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 132, 9), )

    
    grossWeight = property(__grossWeight.value, __grossWeight.set, None, '\n                  .Dangerous Goods Gross Weight: The total gross weight of dangerous goods transported \n                  for each unique UN number. \n               ')

    
    # Element netWeight uses Python identifier netWeight
    __netWeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'netWeight'), 'netWeight', '__httpwww_fixm_aeroflight3_0_DangerousGoodsDimensionsType_netWeight', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 140, 9), )

    
    netWeight = property(__netWeight.value, __netWeight.set, None, '\n                  .Dangerous Goods Net Weight: The total net weight of dangerous goods transported \n                  for each unique UN number. \n               ')

    
    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'volume'), 'volume', '__httpwww_fixm_aeroflight3_0_DangerousGoodsDimensionsType_volume', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 148, 9), )

    
    volume = property(__volume.value, __volume.set, None, '\n                  .Dangerous Goods Volume: The total displacement of dangerous goods transported for \n                  each unique UN number. \n               ')

    _ElementMap.update({
        __grossWeight.name() : __grossWeight,
        __netWeight.name() : __netWeight,
        __volume.name() : __volume
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DangerousGoodsDimensionsType = DangerousGoodsDimensionsType
Namespace.addCategoryObject('typeBinding', 'DangerousGoodsDimensionsType', DangerousGoodsDimensionsType)


# Complex type {http://www.fixm.aero/flight/3.0}TemperaturesType with content type ELEMENT_ONLY
class TemperaturesType (pyxb.binding.basis.complexTypeDefinition):
    """
            Control Temperature: 
             
            Emergency Temperature: 
             
            Flashpoint Temperature: 
            The lowest temperature at which it can vaporize to form an ignitable mixture in air. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemperaturesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 550, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element controlTemperature uses Python identifier controlTemperature
    __controlTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'controlTemperature'), 'controlTemperature', '__httpwww_fixm_aeroflight3_0_TemperaturesType_controlTemperature', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 563, 9), )

    
    controlTemperature = property(__controlTemperature.value, __controlTemperature.set, None, '\n                  .Control Temperature: The maximum temperature at which the substance can be safely \n                  transported. \n               ')

    
    # Element emergencyTemperature uses Python identifier emergencyTemperature
    __emergencyTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emergencyTemperature'), 'emergencyTemperature', '__httpwww_fixm_aeroflight3_0_TemperaturesType_emergencyTemperature', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 571, 9), )

    
    emergencyTemperature = property(__emergencyTemperature.value, __emergencyTemperature.set, None, '\n                  .Emergency Temperature: The temperature at which emergency procedures shall be implemented \n                  in the event of loss of temperature control. \n               ')

    
    # Element flashpointTemperature uses Python identifier flashpointTemperature
    __flashpointTemperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flashpointTemperature'), 'flashpointTemperature', '__httpwww_fixm_aeroflight3_0_TemperaturesType_flashpointTemperature', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 579, 9), )

    
    flashpointTemperature = property(__flashpointTemperature.value, __flashpointTemperature.set, None, '\n                  The lowest temperature at which it can vaporize to form an ignitable mixture in air. \n                  \n               ')

    _ElementMap.update({
        __controlTemperature.name() : __controlTemperature,
        __emergencyTemperature.name() : __emergencyTemperature,
        __flashpointTemperature.name() : __flashpointTemperature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TemperaturesType = TemperaturesType
Namespace.addCategoryObject('typeBinding', 'TemperaturesType', TemperaturesType)


# Complex type {http://www.fixm.aero/flight/3.0}HandoffType with content type ELEMENT_ONLY
class HandoffType (pyxb.binding.basis.complexTypeDefinition):
    """
            An action taken to transfer the radar identification of an aircraft from one controller 
            to another controller if the aircraft will enter the receiving controller's airspace 
            and radio communications with the aircraft will be transferred. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HandoffType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 231, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element coordinationStatus uses Python identifier coordinationStatus
    __coordinationStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'coordinationStatus'), 'coordinationStatus', '__httpwww_fixm_aeroflight3_0_HandoffType_coordinationStatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 240, 9), )

    
    coordinationStatus = property(__coordinationStatus.value, __coordinationStatus.set, None, '\n                  .Coordination Status: The status of Coordination and Transfer of Control between \n                  the currently Controlling Air Traffic Service Unit (ATSU) to the downstream to be \n                  Controlling ATSU. \n               ')

    
    # Element receivingUnit uses Python identifier receivingUnit
    __receivingUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'receivingUnit'), 'receivingUnit', '__httpwww_fixm_aeroflight3_0_HandoffType_receivingUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 249, 9), )

    
    receivingUnit = property(__receivingUnit.value, __receivingUnit.set, None, '\n                  .Handoff Receiving Sector: Identifies the ATC sector receiving control of the aircraft \n                  as a result of a handoff. \n                  .Handoff Receiving Unit: The Air Traffic Control unit receiving control of the aircraft \n                  as a result of a handoff. \n               ')

    
    # Element transferringUnit uses Python identifier transferringUnit
    __transferringUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transferringUnit'), 'transferringUnit', '__httpwww_fixm_aeroflight3_0_HandoffType_transferringUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 259, 9), )

    
    transferringUnit = property(__transferringUnit.value, __transferringUnit.set, None, '\n                  .Handoff Transferring Unit: The Air Traffic Control unit transferring control of \n                  the aircraft as a result of a handoff. \n                  .Handoff Transferring Sector: Identifies the ATC sector transferring control of the \n                  aircraft as a result of a handoff. \n               ')

    _ElementMap.update({
        __coordinationStatus.name() : __coordinationStatus,
        __receivingUnit.name() : __receivingUnit,
        __transferringUnit.name() : __transferringUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.HandoffType = HandoffType
Namespace.addCategoryObject('typeBinding', 'HandoffType', HandoffType)


# Complex type {http://www.fixm.aero/flight/3.0}BeaconCodeAssignmentType with content type ELEMENT_ONLY
class BeaconCodeAssignmentType (pyxb.binding.basis.complexTypeDefinition):
    """
            Contains information about current, previous and next beacon code assignments along 
            with the beacon code assigning facility. 
            .Beacon Code: The assigned four-character numeric code transmitted by the aircraft 
            transponder in response to a secondary surveillance radar interrogation signal which 
            is used to assist air traffic controllers to identify aircraft. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BeaconCodeAssignmentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 112, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element currentBeaconCode uses Python identifier currentBeaconCode
    __currentBeaconCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'currentBeaconCode'), 'currentBeaconCode', '__httpwww_fixm_aeroflight3_0_BeaconCodeAssignmentType_currentBeaconCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 123, 9), )

    
    currentBeaconCode = property(__currentBeaconCode.value, __currentBeaconCode.set, None, '\n                  Current assigned beacon code. \n               ')

    
    # Element previousBeaconCode uses Python identifier previousBeaconCode
    __previousBeaconCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'previousBeaconCode'), 'previousBeaconCode', '__httpwww_fixm_aeroflight3_0_BeaconCodeAssignmentType_previousBeaconCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 130, 9), )

    
    previousBeaconCode = property(__previousBeaconCode.value, __previousBeaconCode.set, None, "\n                  .Previous SSR Mode and Beacon Code: The Secondary surveillance radar (SSR) mode and \n                  code the flight was transponding before the current SSR Mode and Code. \n                  .Reassigned SSR Mode and Beacon Code: The Secondary Surveillance Radar (SSR) mode \n                  and beacon code assigned to the flight in the downstream facility, if the flight's \n                  current beacon code is already in use by another flight in that facility. The next \n                  beacon code differs from the flight's current beacon code. \n               ")

    
    # Element reassignedBeaconCode uses Python identifier reassignedBeaconCode
    __reassignedBeaconCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reassignedBeaconCode'), 'reassignedBeaconCode', '__httpwww_fixm_aeroflight3_0_BeaconCodeAssignmentType_reassignedBeaconCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 142, 9), )

    
    reassignedBeaconCode = property(__reassignedBeaconCode.value, __reassignedBeaconCode.set, None, "\n                  .Previous SSR Mode and Beacon Code: The Secondary surveillance radar (SSR) mode and \n                  code the flight was transponding before the current SSR Mode and Code. \n                  .Reassigned SSR Mode and Beacon Code: The Secondary Surveillance Radar (SSR) mode \n                  and beacon code assigned to the flight in the downstream facility, if the flight's \n                  current beacon code is already in use by another flight in that facility. The next \n                  beacon code differs from the flight's current beacon code. \n               ")

    
    # Element reassigningUnit uses Python identifier reassigningUnit
    __reassigningUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reassigningUnit'), 'reassigningUnit', '__httpwww_fixm_aeroflight3_0_BeaconCodeAssignmentType_reassigningUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 154, 9), )

    
    reassigningUnit = property(__reassigningUnit.value, __reassigningUnit.set, None, '\n                  .Reassigned Beacon Code Unit: Identifies the downstream unit that assigned the next \n                  beacon code, in the case the beacon code was already in use by another flight at \n                  the downstream unit. \n               ')

    _ElementMap.update({
        __currentBeaconCode.name() : __currentBeaconCode,
        __previousBeaconCode.name() : __previousBeaconCode,
        __reassignedBeaconCode.name() : __reassignedBeaconCode,
        __reassigningUnit.name() : __reassigningUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BeaconCodeAssignmentType = BeaconCodeAssignmentType
Namespace.addCategoryObject('typeBinding', 'BeaconCodeAssignmentType', BeaconCodeAssignmentType)


# Complex type {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType with content type ELEMENT_ONLY
class ClearedFlightInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups cleared information about the fight 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClearedFlightInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 167, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element clearedFlightLevel uses Python identifier clearedFlightLevel
    __clearedFlightLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'clearedFlightLevel'), 'clearedFlightLevel', '__httpwww_fixm_aeroflight3_0_ClearedFlightInformationType_clearedFlightLevel', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 174, 9), )

    
    clearedFlightLevel = property(__clearedFlightLevel.value, __clearedFlightLevel.set, None, '\n                  .Cleared Flight Level: The Altitude an aircraft is cleared to maintain as specified \n                  by ATC.  It may differ from the Cruising Altitude, which is more strategic. \n               ')

    
    # Element clearedSpeed uses Python identifier clearedSpeed
    __clearedSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'clearedSpeed'), 'clearedSpeed', '__httpwww_fixm_aeroflight3_0_ClearedFlightInformationType_clearedSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 182, 9), )

    
    clearedSpeed = property(__clearedSpeed.value, __clearedSpeed.set, None, '\n                  .Cleared Speed: The speed (or speed range) cleared from the controller to the pilot. \n                   The element is tactical in nature. The speed condition indicates whether the aircraft \n                  will be maintaining, exceeding, or flying more slowly than the associated speed. \n                  \n               ')

    
    # Element directRouting uses Python identifier directRouting
    __directRouting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'directRouting'), 'directRouting', '__httpwww_fixm_aeroflight3_0_ClearedFlightInformationType_directRouting', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 192, 9), )

    
    directRouting = property(__directRouting.value, __directRouting.set, None, '\n                  .Cleared Direct To: Contains the optional starting location from which the direct \n                  clearance is granted and the position the aircraft has been cleared directly to. \n                  \n               ')

    
    # Element heading uses Python identifier heading
    __heading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'heading'), 'heading', '__httpwww_fixm_aeroflight3_0_ClearedFlightInformationType_heading', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 201, 9), )

    
    heading = property(__heading.value, __heading.set, None, "\n                  .Cleared Heading: The heading assigned to a flight by ATC.  It is the magnetic heading \n                  the aircraft's nose is pointing to. \n               ")

    
    # Element offtrackClearance uses Python identifier offtrackClearance
    __offtrackClearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offtrackClearance'), 'offtrackClearance', '__httpwww_fixm_aeroflight3_0_ClearedFlightInformationType_offtrackClearance', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 209, 9), )

    
    offtrackClearance = property(__offtrackClearance.value, __offtrackClearance.set, None, '\n                  .Off Track Clearance: This field specifies the offtrack information applicable to \n                  the route. \n               ')

    
    # Element rateOfClimbDescend uses Python identifier rateOfClimbDescend
    __rateOfClimbDescend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rateOfClimbDescend'), 'rateOfClimbDescend', '__httpwww_fixm_aeroflight3_0_ClearedFlightInformationType_rateOfClimbDescend', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 217, 9), )

    
    rateOfClimbDescend = property(__rateOfClimbDescend.value, __rateOfClimbDescend.set, None, "\n                  .Cleared Rate of Climb/Descent: The flight's current assigned Rate of climb/descent, \n                  which is part of the current clearance. \n               ")

    _ElementMap.update({
        __clearedFlightLevel.name() : __clearedFlightLevel,
        __clearedSpeed.name() : __clearedSpeed,
        __directRouting.name() : __directRouting,
        __heading.name() : __heading,
        __offtrackClearance.name() : __offtrackClearance,
        __rateOfClimbDescend.name() : __rateOfClimbDescend
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ClearedFlightInformationType = ClearedFlightInformationType
Namespace.addCategoryObject('typeBinding', 'ClearedFlightInformationType', ClearedFlightInformationType)


# Complex type {http://www.fixm.aero/flight/3.0}ControlElementType with content type ELEMENT_ONLY
class ControlElementType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Control Element: The constrained aerodrome or airspace element (subject to a Traffic 
            Management Initiative/Regulation) indicating the reason for a flight being controlled. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControlElementType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 229, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element airspace uses Python identifier airspace
    __airspace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airspace'), 'airspace', '__httpwww_fixm_aeroflight3_0_ControlElementType_airspace', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 238, 9), )

    
    airspace = property(__airspace.value, __airspace.set, None, '\n                  Represents an airspace that has been constrained such as flow constrained area with \n                  associated controlled time. \n               ')

    
    # Element arrivalAerodrome uses Python identifier arrivalAerodrome
    __arrivalAerodrome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome'), 'arrivalAerodrome', '__httpwww_fixm_aeroflight3_0_ControlElementType_arrivalAerodrome', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 246, 9), )

    
    arrivalAerodrome = property(__arrivalAerodrome.value, __arrivalAerodrome.set, None, '\n                  An arrival aerodrome that is subject to air traffic control management. \n                  .Arrival Aerodrome: The ICAO designator or the name of the aerodrome at which the \n                  flight has arrived. \n               ')

    _ElementMap.update({
        __airspace.name() : __airspace,
        __arrivalAerodrome.name() : __arrivalAerodrome
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ControlElementType = ControlElementType
Namespace.addCategoryObject('typeBinding', 'ControlElementType', ControlElementType)


# Complex type {http://www.fixm.aero/flight/3.0}DirectRoutingType with content type ELEMENT_ONLY
class DirectRoutingType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Cleared Direct To: Contains the optional starting location from which the direct 
            clearance is granted and the position the aircraft has been cleared directly to. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DirectRoutingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 259, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element from uses Python identifier from_
    __from = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__httpwww_fixm_aeroflight3_0_DirectRoutingType_from', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 268, 9), )

    
    from_ = property(__from.value, __from.set, None, '\n                  Location from which the direct clearance is granted. \n               ')

    
    # Element to uses Python identifier to
    __to = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__httpwww_fixm_aeroflight3_0_DirectRoutingType_to', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 275, 9), )

    
    to = property(__to.value, __to.set, None, '\n                  Location to which the direct clearance is granted. \n               ')

    _ElementMap.update({
        __from.name() : __from,
        __to.name() : __to
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DirectRoutingType = DirectRoutingType
Namespace.addCategoryObject('typeBinding', 'DirectRoutingType', DirectRoutingType)


# Complex type {http://www.fixm.aero/flight/3.0}PointoutType with content type ELEMENT_ONLY
class PointoutType (pyxb.binding.basis.complexTypeDefinition):
    """
            A physical or automated action taken by a controller to transfer the radar identification 
            of an aircraft to another controller if the aircraft will or may enter the airspace 
            or protected airspace of another controller and radio communications will not be 
            transferred. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointoutType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 376, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element originatingUnit uses Python identifier originatingUnit
    __originatingUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'originatingUnit'), 'originatingUnit', '__httpwww_fixm_aeroflight3_0_PointoutType_originatingUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 386, 9), )

    
    originatingUnit = property(__originatingUnit.value, __originatingUnit.set, None, '\n                  .Point Out - Originating Sector: Identifies the ATC sector originating the point \n                  out. \n                  .Point Out - Originating Unit: Identifies the Air Traffic Control unit originating \n                  the point out. \n               ')

    
    # Element receivingUnit uses Python identifier receivingUnit
    __receivingUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'receivingUnit'), 'receivingUnit', '__httpwww_fixm_aeroflight3_0_PointoutType_receivingUnit', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 396, 9), )

    
    receivingUnit = property(__receivingUnit.value, __receivingUnit.set, None, '\n                  .Point Out - Receiving Sector: Identifies the ATC sector receiving the point out. \n                  \n                  .Point Out - Receiving Unit: Identifies the Air Traffic Control unit receiving the \n                  point out. \n               ')

    _ElementMap.update({
        __originatingUnit.name() : __originatingUnit,
        __receivingUnit.name() : __receivingUnit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PointoutType = PointoutType
Namespace.addCategoryObject('typeBinding', 'PointoutType', PointoutType)


# Complex type {http://www.fixm.aero/flight/3.0}ActualSpeedType with content type ELEMENT_ONLY
class ActualSpeedType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Speed - Actual: The actual speed of the aircraft, collected via various methods. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActualSpeedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 81, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element calculated uses Python identifier calculated
    __calculated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'calculated'), 'calculated', '__httpwww_fixm_aeroflight3_0_ActualSpeedType_calculated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 89, 9), )

    
    calculated = property(__calculated.value, __calculated.set, None, '\n                  .Speed - Calculated: The estimated horizontal speed of the aircraft relative to a \n                  fixed point on the ground. \n               ')

    
    # Element pilotReported uses Python identifier pilotReported
    __pilotReported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pilotReported'), 'pilotReported', '__httpwww_fixm_aeroflight3_0_ActualSpeedType_pilotReported', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 97, 9), )

    
    pilotReported = property(__pilotReported.value, __pilotReported.set, None, '\n                  .Speed - Pilot Reported: The speed of the aircraft relative to the air mass in which \n                  it is flying. This is the speed reported by the pilot. \n               ')

    
    # Element surveillance uses Python identifier surveillance
    __surveillance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surveillance'), 'surveillance', '__httpwww_fixm_aeroflight3_0_ActualSpeedType_surveillance', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 105, 9), )

    
    surveillance = property(__surveillance.value, __surveillance.set, None, '\n                  .Speed - Surveillance: The measured horizontal speed of the aircraft relative to \n                  a fixed point on the ground, for flights being tracked by surveillance or satellite. \n                  \n               ')

    _ElementMap.update({
        __calculated.name() : __calculated,
        __pilotReported.name() : __pilotReported,
        __surveillance.name() : __surveillance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ActualSpeedType = ActualSpeedType
Namespace.addCategoryObject('typeBinding', 'ActualSpeedType', ActualSpeedType)


# Complex type {http://www.fixm.aero/flight/3.0}DepartureActivityTimesType with content type ELEMENT_ONLY
class DepartureActivityTimesType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups various TimeSequences associated with departure activities. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DepartureActivityTimesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 81, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element boardingTime uses Python identifier boardingTime
    __boardingTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boardingTime'), 'boardingTime', '__httpwww_fixm_aeroflight3_0_DepartureActivityTimesType_boardingTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 88, 9), )

    
    boardingTime = property(__boardingTime.value, __boardingTime.set, None, '\n                  .Boarding Start Time - Actual: Time passengers are entering the bridge or bus to \n                  the aircraft. \n               ')

    
    # Element deIcingTime uses Python identifier deIcingTime
    __deIcingTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deIcingTime'), 'deIcingTime', '__httpwww_fixm_aeroflight3_0_DepartureActivityTimesType_deIcingTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 96, 9), )

    
    deIcingTime = property(__deIcingTime.value, __deIcingTime.set, None, '\n                  .De-icing End Time - Estimated: The time when de-icing operations on the aircraft \n                  are expected to end. \n                  .De-icing Start Time - Estimated: The time when de-icing operations on the aircraft \n                  are expected to start. \n                  .De-icing Ready Time - Estimated: The time when the aircraft is expected to be ready \n                  for de-icing operations. \n                  .De-icing Start Time - Actual: The time when de-icing operations on the aircraft \n                  start. \n                  .De-icing Ready Time - Actual:  The time when the aircraft is ready to be de-iced. \n                  \n                  .De-icing End Time - Actual: The time when de-icing operations on the aircraft end. \n                  \n               ')

    
    # Element groundHandlingTime uses Python identifier groundHandlingTime
    __groundHandlingTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'groundHandlingTime'), 'groundHandlingTime', '__httpwww_fixm_aeroflight3_0_DepartureActivityTimesType_groundHandlingTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 114, 9), )

    
    groundHandlingTime = property(__groundHandlingTime.value, __groundHandlingTime.set, None, '\n                  .Ground Handling End Time - Actual: The time when ground handling on the aircraft \n                  ends. \n                  .Ground Handling Start Time - Actual: The time when ground handling on the aircraft \n                  starts. \n               ')

    
    # Element startupTime uses Python identifier startupTime
    __startupTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'startupTime'), 'startupTime', '__httpwww_fixm_aeroflight3_0_DepartureActivityTimesType_startupTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 124, 9), )

    
    startupTime = property(__startupTime.value, __startupTime.set, None, '\n                  .Start Up Approval Time - Target: The time when the aircraft is expected to receive \n                  start up/pushback approval. \n                  .Start Up Approval Time - Actual: The time when the aircraft receives the start up \n                  approval. \n                  .Start Up Request Time - Actual: The time when the aircraft requests start up clearance. \n                  \n               ')

    _ElementMap.update({
        __boardingTime.name() : __boardingTime,
        __deIcingTime.name() : __deIcingTime,
        __groundHandlingTime.name() : __groundHandlingTime,
        __startupTime.name() : __startupTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DepartureActivityTimesType = DepartureActivityTimesType
Namespace.addCategoryObject('typeBinding', 'DepartureActivityTimesType', DepartureActivityTimesType)


# Complex type {http://www.fixm.aero/flight/3.0}EnRouteDiversionType with content type ELEMENT_ONLY
class EnRouteDiversionType (pyxb.binding.basis.complexTypeDefinition):
    """
            Contains information about the En Route Diversion of the flight such as diversion 
            recovery. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnRouteDiversionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 119, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element diversionRecoveryInformation uses Python identifier diversionRecoveryInformation
    __diversionRecoveryInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diversionRecoveryInformation'), 'diversionRecoveryInformation', '__httpwww_fixm_aeroflight3_0_EnRouteDiversionType_diversionRecoveryInformation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 127, 9), )

    
    diversionRecoveryInformation = property(__diversionRecoveryInformation.value, __diversionRecoveryInformation.set, None, '\n                  .Diversion Recovery Information: The Diversion Recovery Information indicates a flight \n                  is the recovery for a flight that changed its original destination. It is represented \n                  by the GUFI of the original flight. \n               ')

    _ElementMap.update({
        __diversionRecoveryInformation.name() : __diversionRecoveryInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EnRouteDiversionType = EnRouteDiversionType
Namespace.addCategoryObject('typeBinding', 'EnRouteDiversionType', EnRouteDiversionType)


# Complex type {http://www.fixm.aero/flight/3.0}OriginatorType with content type ELEMENT_ONLY
class OriginatorType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Flight Plan Originator: The originator's eight-letter AFTN address, or other appropriate 
            contact details, in cases where the originator of the flight plan may not be readily 
            identified. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OriginatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 409, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element aftnAddress uses Python identifier aftnAddress
    __aftnAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aftnAddress'), 'aftnAddress', '__httpwww_fixm_aeroflight3_0_OriginatorType_aftnAddress', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 418, 9), )

    
    aftnAddress = property(__aftnAddress.value, __aftnAddress.set, None, "\n                  Represents the Aeronautical Fixed Telecommunication Network station address \n                  .Originator AFTN Address: The originator's eight-letter AFTN address, or other appropriate \n                  contact details, in cases where the originator of the flight plan may not be readily \n                  identified. \n               ")

    
    # Element flightOriginator uses Python identifier flightOriginator
    __flightOriginator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flightOriginator'), 'flightOriginator', '__httpwww_fixm_aeroflight3_0_OriginatorType_flightOriginator', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 428, 9), )

    
    flightOriginator = property(__flightOriginator.value, __flightOriginator.set, None, "\n                  .Flight Originator: The originator's eight-letter AFTN address, or other appropriate \n                  contact details, in cases where the originator of the flight plan may not be readily \n                  identified. \n               ")

    _ElementMap.update({
        __aftnAddress.name() : __aftnAddress,
        __flightOriginator.name() : __flightOriginator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OriginatorType = OriginatorType
Namespace.addCategoryObject('typeBinding', 'OriginatorType', OriginatorType)


# Complex type {http://www.fixm.aero/flight/3.0}ElapsedTimeLocationType with content type ELEMENT_ONLY
class ElapsedTimeLocationType (pyxb.binding.basis.complexTypeDefinition):
    """
            The location associated with estimated elapsed time. It can be a longitude, significant 
            point of flight information region. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElapsedTimeLocationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 147, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'longitude'), 'longitude', '__httpwww_fixm_aeroflight3_0_ElapsedTimeLocationType_longitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 155, 9), )

    
    longitude = property(__longitude.value, __longitude.set, None, '\n                  Longitude associated with the elapsed time. \n               ')

    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__httpwww_fixm_aeroflight3_0_ElapsedTimeLocationType_point', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 162, 9), )

    
    point = property(__point.value, __point.set, None, '\n                  Point associated with the estimated elapsed time. \n               ')

    
    # Element region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_fixm_aeroflight3_0_ElapsedTimeLocationType_region', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 169, 9), )

    
    region = property(__region.value, __region.set, None, '\n                  Flight information boundary associated with the elapsed time. \n               ')

    _ElementMap.update({
        __longitude.name() : __longitude,
        __point.name() : __point,
        __region.name() : __region
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ElapsedTimeLocationType = ElapsedTimeLocationType
Namespace.addCategoryObject('typeBinding', 'ElapsedTimeLocationType', ElapsedTimeLocationType)


# Complex type {http://www.fixm.aero/flight/3.0}ExpandedRouteType with content type ELEMENT_ONLY
class ExpandedRouteType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Expanded Route: The expansion of the route into a set of points which describe the 
            aircraft's expected 2D path from the departure aerodrome to the destination aerodrome. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpandedRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 207, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element routePoint uses Python identifier routePoint
    __routePoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routePoint'), 'routePoint', '__httpwww_fixm_aeroflight3_0_ExpandedRouteType_routePoint', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 216, 9), )

    
    routePoint = property(__routePoint.value, __routePoint.set, None, "\n                  Expanded Route contains an ordered list of expanded route points. \n                  .Expanded Route Point: A point that is part of the aircraft's expanded route of flight. \n                  \n               ")

    _ElementMap.update({
        __routePoint.name() : __routePoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExpandedRouteType = ExpandedRouteType
Namespace.addCategoryObject('typeBinding', 'ExpandedRouteType', ExpandedRouteType)


# Complex type {http://www.fixm.aero/flight/3.0}SpeedScheduleType with content type ELEMENT_ONLY
class SpeedScheduleType (pyxb.binding.basis.complexTypeDefinition):
    """
            Defines the speed schedule for climb and descent of the aircraft through the crossover 
            altitude. 
            .Speed Schedule - Climb: Initially submitted by the airspace user, this defines the 
            target speed in both Initial Airspeed (IAS) and MACH so the aircraft can climb through 
            the crossover altitude and target the MACH speed when needed. 
            .Speed Schedule - Descent: Initially submitted by the airspace user, this defines 
            the target speed in both IAS and MACH so the aircraft can descend through the crossover 
            altitude and target the Initial Airspeed (IAS) speed when needed. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpeedScheduleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 427, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element initialSpeed uses Python identifier initialSpeed
    __initialSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'initialSpeed'), 'initialSpeed', '__httpwww_fixm_aeroflight3_0_SpeedScheduleType_initialSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 441, 9), )

    
    initialSpeed = property(__initialSpeed.value, __initialSpeed.set, None, '\n                  Initial speed of the aircraft during the climb \n               ')

    
    # Element subsequentSpeed uses Python identifier subsequentSpeed
    __subsequentSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subsequentSpeed'), 'subsequentSpeed', '__httpwww_fixm_aeroflight3_0_SpeedScheduleType_subsequentSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 448, 9), )

    
    subsequentSpeed = property(__subsequentSpeed.value, __subsequentSpeed.set, None, '\n                  Subsequent speed of the aircraft during the climb \n               ')

    _ElementMap.update({
        __initialSpeed.name() : __initialSpeed,
        __subsequentSpeed.name() : __subsequentSpeed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpeedScheduleType = SpeedScheduleType
Namespace.addCategoryObject('typeBinding', 'SpeedScheduleType', SpeedScheduleType)


# Complex type {http://www.fixm.aero/flight/3.0}MeteorologicalDataType with content type ELEMENT_ONLY
class MeteorologicalDataType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Meteorological Data: In a predicted trajectory, the instantaneous temperature and 
            wind vector used at the 4D Point for creating the 4D trajectory. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeteorologicalDataType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 81, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'temperature'), 'temperature', '__httpwww_fixm_aeroflight3_0_MeteorologicalDataType_temperature', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 89, 9), )

    
    temperature = property(__temperature.value, __temperature.set, None, '\n                  Temperature at the trajectory point. \n               ')

    
    # Element windDirection uses Python identifier windDirection
    __windDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'windDirection'), 'windDirection', '__httpwww_fixm_aeroflight3_0_MeteorologicalDataType_windDirection', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 96, 9), )

    
    windDirection = property(__windDirection.value, __windDirection.set, None, '\n                  Wind vector at the trajectory point. \n               ')

    
    # Element windSpeed uses Python identifier windSpeed
    __windSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'windSpeed'), 'windSpeed', '__httpwww_fixm_aeroflight3_0_MeteorologicalDataType_windSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 103, 9), )

    
    windSpeed = property(__windSpeed.value, __windSpeed.set, None, '\n                  Wind speed at the trajectory point. \n               ')

    _ElementMap.update({
        __temperature.name() : __temperature,
        __windDirection.name() : __windDirection,
        __windSpeed.name() : __windSpeed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeteorologicalDataType = MeteorologicalDataType
Namespace.addCategoryObject('typeBinding', 'MeteorologicalDataType', MeteorologicalDataType)


# Complex type {http://www.fixm.aero/flight/3.0}PointRangeType with content type ELEMENT_ONLY
class PointRangeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Provides a vertical, lateral or temporal range to a 4D point when clearances are 
            provided in the form of: 
             
    block altitude clearances
    offsets for deviations due to weather
    assigned speed ranges
            .Point Range: Provides a vertical, lateral or temporal range to a 4D point when clearances 
            are provided in the form of:block altitude clearancesoffsets for deviations due to 
            weatherassigned speed ranges 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointRangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 155, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lateralRange uses Python identifier lateralRange
    __lateralRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lateralRange'), 'lateralRange', '__httpwww_fixm_aeroflight3_0_PointRangeType_lateralRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 170, 9), )

    
    lateralRange = property(__lateralRange.value, __lateralRange.set, None, '\n                  Lateral range representing  offsets for deviations due to weather \n               ')

    
    # Element temporalRange uses Python identifier temporalRange
    __temporalRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'temporalRange'), 'temporalRange', '__httpwww_fixm_aeroflight3_0_PointRangeType_temporalRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 177, 9), )

    
    temporalRange = property(__temporalRange.value, __temporalRange.set, None, '\n                  Temporal range resulting from assigned speed range. \n               ')

    
    # Element verticalRange uses Python identifier verticalRange
    __verticalRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'verticalRange'), 'verticalRange', '__httpwww_fixm_aeroflight3_0_PointRangeType_verticalRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 184, 9), )

    
    verticalRange = property(__verticalRange.value, __verticalRange.set, None, '\n                  Vertical Range representing block altitude clearances \n               ')

    _ElementMap.update({
        __lateralRange.name() : __lateralRange,
        __temporalRange.name() : __temporalRange,
        __verticalRange.name() : __verticalRange
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PointRangeType = PointRangeType
Namespace.addCategoryObject('typeBinding', 'PointRangeType', PointRangeType)


# Complex type {http://www.fixm.aero/flight/3.0}TrajectoryType with content type ELEMENT_ONLY
class TrajectoryType (pyxb.binding.basis.complexTypeDefinition):
    """
            For FIXM v3.0, this data type only covers the airborne segment.  However, future 
            versions of FIXM will cover gate-to-gate operations. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajectoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 218, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element trajectoryPoint uses Python identifier trajectoryPoint
    __trajectoryPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trajectoryPoint'), 'trajectoryPoint', '__httpwww_fixm_aeroflight3_0_TrajectoryType_trajectoryPoint', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 226, 9), )

    
    trajectoryPoint = property(__trajectoryPoint.value, __trajectoryPoint.set, None, '\n                  a 4D Trajectory consists of an ordered list of trajectory points. \n                  .Trajectory Point: A container for information pertinent to a single point in a trajectory. \n                  \n               ')

    _ElementMap.update({
        __trajectoryPoint.name() : __trajectoryPoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TrajectoryType = TrajectoryType
Namespace.addCategoryObject('typeBinding', 'TrajectoryType', TrajectoryType)


# Complex type {http://www.fixm.aero/flight/3.0}TrajectoryPointType with content type ELEMENT_ONLY
class TrajectoryPointType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Trajectory Point: A container for information pertinent to a single point in a trajectory. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajectoryPointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 294, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element altimeterSetting uses Python identifier altimeterSetting
    __altimeterSetting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altimeterSetting'), 'altimeterSetting', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_altimeterSetting', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 302, 9), )

    
    altimeterSetting = property(__altimeterSetting.value, __altimeterSetting.set, None, '\n                  .Assumed Altimeter Setting: The barometric pressure reading used to adjust a pressure \n                  altimeter for variations in existing atmospheric pressure or to the standard altimeter \n                  setting (29.92). \n               ')

    
    # Element metData uses Python identifier metData
    __metData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metData'), 'metData', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_metData', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 311, 9), )

    
    metData = property(__metData.value, __metData.set, None, '\n                  .Meteorological Data: In a predicted trajectory, the instantaneous temperature and \n                  wind vector used at the 4D Point for creating the 4D trajectory. \n               ')

    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_point', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 319, 9), )

    
    point = property(__point.value, __point.set, None, '\n                  .4D Point: Identifies the location, altitude and time of a trajectory point. \n               ')

    
    # Element predictedAirspeed uses Python identifier predictedAirspeed
    __predictedAirspeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedAirspeed'), 'predictedAirspeed', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_predictedAirspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 326, 9), )

    
    predictedAirspeed = property(__predictedAirspeed.value, __predictedAirspeed.set, None, '\n                  .Airspeed - Predicted: The airspeed (or range of speeds) of the flight at the 4D \n                  Point expressed as either Indicated Airspeed or Mach. \n               ')

    
    # Element predictedGroundspeed uses Python identifier predictedGroundspeed
    __predictedGroundspeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedGroundspeed'), 'predictedGroundspeed', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_predictedGroundspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 334, 9), )

    
    predictedGroundspeed = property(__predictedGroundspeed.value, __predictedGroundspeed.set, None, '\n                  .Ground Speed - Predicted: Aircraft predicted ground speed (or range of speeds) at \n                  this point. \n               ')

    
    # Element referencePoint uses Python identifier referencePoint
    __referencePoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'referencePoint'), 'referencePoint', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_referencePoint', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 342, 9), )

    
    referencePoint = property(__referencePoint.value, __referencePoint.set, None, '\n                  .Reference Point: For 4D Points associated with a waypoint on the expanded route, \n                  the reference point provides the expanded route waypoint enabling the 4D Trajectory \n                  to be linked with the route information. \n               ')

    
    # Element trajectoryChange uses Python identifier trajectoryChange
    __trajectoryChange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trajectoryChange'), 'trajectoryChange', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_trajectoryChange', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 351, 9), )

    
    trajectoryChange = property(__trajectoryChange.value, __trajectoryChange.set, None, '\n                  Indicates features that are crossed at the specified trajectory point. \n               ')

    
    # Element trajectoryChangeType uses Python identifier trajectoryChangeType
    __trajectoryChangeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trajectoryChangeType'), 'trajectoryChangeType', '__httpwww_fixm_aeroflight3_0_TrajectoryPointType_trajectoryChangeType', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 358, 9), )

    
    trajectoryChangeType = property(__trajectoryChangeType.value, __trajectoryChangeType.set, None, '\n                  Trajectory Change Point - Type: Identifies the type(s) of trajectory change point \n                  being described by the associated 4D Point. \n                  .Trajectory Change Point - Type: Identifies the type(s) of trajectory change point \n                  being described by the associated 4D Point. \n               ')

    _ElementMap.update({
        __altimeterSetting.name() : __altimeterSetting,
        __metData.name() : __metData,
        __point.name() : __point,
        __predictedAirspeed.name() : __predictedAirspeed,
        __predictedGroundspeed.name() : __predictedGroundspeed,
        __referencePoint.name() : __referencePoint,
        __trajectoryChange.name() : __trajectoryChange,
        __trajectoryChangeType.name() : __trajectoryChangeType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TrajectoryPointType = TrajectoryPointType
Namespace.addCategoryObject('typeBinding', 'TrajectoryPointType', TrajectoryPointType)


# Complex type {http://www.fixm.aero/flight/3.0}TrajectoryRoutePairType with content type ELEMENT_ONLY
class TrajectoryRoutePairType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups and associates a Route and 4D Trajectory. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajectoryRoutePairType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 375, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__httpwww_fixm_aeroflight3_0_TrajectoryRoutePairType_route', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 382, 9), )

    
    route = property(__route.value, __route.set, None, '\n                  Route associated with the Trajectory Route Pair. \n                  .Route: The ICAO route string as depicted from the flight plan. \n               ')

    
    # Element trajectory uses Python identifier trajectory
    __trajectory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trajectory'), 'trajectory', '__httpwww_fixm_aeroflight3_0_TrajectoryRoutePairType_trajectory', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 390, 9), )

    
    trajectory = property(__trajectory.value, __trajectory.set, None, '\n                  4D Trajectory associated with the Trajectory Route Pair. \n               ')

    _ElementMap.update({
        __route.name() : __route,
        __trajectory.name() : __trajectory
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TrajectoryRoutePairType = TrajectoryRoutePairType
Namespace.addCategoryObject('typeBinding', 'TrajectoryRoutePairType', TrajectoryRoutePairType)


# Complex type {http://www.fixm.aero/flight/3.0}AircraftCapabilitiesType with content type ELEMENT_ONLY
class AircraftCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups all the aircraft's capabilities. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 186, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element communication uses Python identifier communication
    __communication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'communication'), 'communication', '__httpwww_fixm_aeroflight3_0_AircraftCapabilitiesType_communication', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 193, 9), )

    
    communication = property(__communication.value, __communication.set, None, '\n                  .Communications Capabilities: The serviceable communications equipment, available \n                  on the aircraft at the time of flight, and associated flight crew qualifications \n                  that may be used to communicate with ATS units. \n               ')

    
    # Element navigation uses Python identifier navigation
    __navigation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navigation'), 'navigation', '__httpwww_fixm_aeroflight3_0_AircraftCapabilitiesType_navigation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 202, 9), )

    
    navigation = property(__navigation.value, __navigation.set, None, '\n                  .Navigation Capabilities: The serviceable navigation equipment available on board \n                  the aircraft at the time of flight and for which the flight crew is qualified. \n               ')

    
    # Element surveillance uses Python identifier surveillance
    __surveillance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surveillance'), 'surveillance', '__httpwww_fixm_aeroflight3_0_AircraftCapabilitiesType_surveillance', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 210, 9), )

    
    surveillance = property(__surveillance.value, __surveillance.set, None, '\n                  .Surveillance Capabilities: The serviceable Secondary Surveillance Radar (SSR) and/or \n                  Automatic Dependent Surveillance (ADS) equipment available on the aircraft at the \n                  time of flight that may be used to identify and/or locate the aircraft. \n               ')

    
    # Element survival uses Python identifier survival
    __survival = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'survival'), 'survival', '__httpwww_fixm_aeroflight3_0_AircraftCapabilitiesType_survival', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 219, 9), )

    
    survival = property(__survival.value, __survival.set, None, '\n                  Aircraft is equipped with survival capabilities. \n               ')

    
    # Attribute standardCapabilities uses Python identifier standardCapabilities
    __standardCapabilities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standardCapabilities'), 'standardCapabilities', '__httpwww_fixm_aeroflight3_0_AircraftCapabilitiesType_standardCapabilities', _module_typeBindings.StandardCapabilitiesIndicatorType)
    __standardCapabilities._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 227, 6)
    __standardCapabilities._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 227, 6)
    
    standardCapabilities = property(__standardCapabilities.value, __standardCapabilities.set, None, '\n               if present, indicates that aircraft has the "standard" capabilities for the flight. \n               \n            ')

    _ElementMap.update({
        __communication.name() : __communication,
        __navigation.name() : __navigation,
        __surveillance.name() : __surveillance,
        __survival.name() : __survival
    })
    _AttributeMap.update({
        __standardCapabilities.name() : __standardCapabilities
    })
_module_typeBindings.AircraftCapabilitiesType = AircraftCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'AircraftCapabilitiesType', AircraftCapabilitiesType)


# Complex type {http://www.fixm.aero/flight/3.0}NavigationCapabilitiesType with content type ELEMENT_ONLY
class NavigationCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Navigation Capabilities: The serviceable navigation equipment available on board 
            the aircraft at the time of flight and for which the flight crew is qualified. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NavigationCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 78, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element navigationCode uses Python identifier navigationCode
    __navigationCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'navigationCode'), 'navigationCode', '__httpwww_fixm_aeroflight3_0_NavigationCapabilitiesType_navigationCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 86, 9), )

    
    navigationCode = property(__navigationCode.value, __navigationCode.set, None, '\n                  Describes the aircraft navigation code. \n               ')

    
    # Element performanceBasedCode uses Python identifier performanceBasedCode
    __performanceBasedCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'performanceBasedCode'), 'performanceBasedCode', '__httpwww_fixm_aeroflight3_0_NavigationCapabilitiesType_performanceBasedCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 96, 9), )

    
    performanceBasedCode = property(__performanceBasedCode.value, __performanceBasedCode.set, None, '\n                  .Performance-Based Navigation Capabilities: A coded category denoting which Required \n                  Navigation Performance (RNP) and Area Navigation (RNAV) requirements can be met by \n                  the aircraft while operating in the context of a particular airspace when supported \n                  by the appropriate navigation infrastructure. \n               ')

    
    # Attribute otherNavigationCapabilities uses Python identifier otherNavigationCapabilities
    __otherNavigationCapabilities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherNavigationCapabilities'), 'otherNavigationCapabilities', '__httpwww_fixm_aeroflight3_0_NavigationCapabilitiesType_otherNavigationCapabilities', _ImportedBinding__fb.FreeTextType)
    __otherNavigationCapabilities._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 110, 6)
    __otherNavigationCapabilities._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 110, 6)
    
    otherNavigationCapabilities = property(__otherNavigationCapabilities.value, __otherNavigationCapabilities.set, None, '\n               Additional navigation capabilities available on board the aircraft. \n            ')

    _ElementMap.update({
        __navigationCode.name() : __navigationCode,
        __performanceBasedCode.name() : __performanceBasedCode
    })
    _AttributeMap.update({
        __otherNavigationCapabilities.name() : __otherNavigationCapabilities
    })
_module_typeBindings.NavigationCapabilitiesType = NavigationCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'NavigationCapabilitiesType', NavigationCapabilitiesType)


# Complex type {http://www.fixm.aero/flight/3.0}SurveillanceCapabilitiesType with content type ELEMENT_ONLY
class SurveillanceCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Surveillance Capabilities: The serviceable Secondary Surveillance Radar (SSR) and/or 
            Automatic Dependent Surveillance (ADS) equipment available on the aircraft at the 
            time of flight that may be used to identify and/or locate the aircraft. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurveillanceCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 78, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element surveillanceCode uses Python identifier surveillanceCode
    __surveillanceCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'surveillanceCode'), 'surveillanceCode', '__httpwww_fixm_aeroflight3_0_SurveillanceCapabilitiesType_surveillanceCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 87, 9), )

    
    surveillanceCode = property(__surveillanceCode.value, __surveillanceCode.set, None, '\n                  Describes the aircraft surveillance code. \n               ')

    
    # Attribute otherSurveillanceCapabilities uses Python identifier otherSurveillanceCapabilities
    __otherSurveillanceCapabilities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherSurveillanceCapabilities'), 'otherSurveillanceCapabilities', '__httpwww_fixm_aeroflight3_0_SurveillanceCapabilitiesType_otherSurveillanceCapabilities', _ImportedBinding__fb.FreeTextType)
    __otherSurveillanceCapabilities._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 98, 6)
    __otherSurveillanceCapabilities._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 98, 6)
    
    otherSurveillanceCapabilities = property(__otherSurveillanceCapabilities.value, __otherSurveillanceCapabilities.set, None, '\n               Additional surveillance capabilities available on board the aircraft. \n            ')

    _ElementMap.update({
        __surveillanceCode.name() : __surveillanceCode
    })
    _AttributeMap.update({
        __otherSurveillanceCapabilities.name() : __otherSurveillanceCapabilities
    })
_module_typeBindings.SurveillanceCapabilitiesType = SurveillanceCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'SurveillanceCapabilitiesType', SurveillanceCapabilitiesType)


# Complex type {http://www.fixm.aero/flight/3.0}DinghyType with content type ELEMENT_ONLY
class DinghyType (pyxb.binding.basis.complexTypeDefinition):
    """
            Describes the aircraft dingy. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DinghyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 78, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element colour uses Python identifier colour
    __colour = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'colour'), 'colour', '__httpwww_fixm_aeroflight3_0_DinghyType_colour', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 85, 9), )

    
    colour = property(__colour.value, __colour.set, None, '\n                  .Dinghy Color: The color of the dinghies carried by the aircraft. \n               ')

    
    # Attribute covered uses Python identifier covered
    __covered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'covered'), 'covered', '__httpwww_fixm_aeroflight3_0_DinghyType_covered', _module_typeBindings.DinghyCoverType)
    __covered._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 93, 6)
    __covered._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 93, 6)
    
    covered = property(__covered.value, __covered.set, None, '\n               .Dinghy Cover Status: Indication of the covered/uncovered nature of the dinghies \n               carried by the aircraft. \n            ')

    
    # Attribute quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'quantity'), 'quantity', '__httpwww_fixm_aeroflight3_0_DinghyType_quantity', _ImportedBinding__fb.CountType)
    __quantity._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 101, 6)
    __quantity._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 101, 6)
    
    quantity = property(__quantity.value, __quantity.set, None, '\n               .Dinghy Quantity: The number of dinghies carried by the aircraft. \n            ')

    
    # Attribute totalCapacity uses Python identifier totalCapacity
    __totalCapacity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'totalCapacity'), 'totalCapacity', '__httpwww_fixm_aeroflight3_0_DinghyType_totalCapacity', _ImportedBinding__fb.CountType)
    __totalCapacity._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 108, 6)
    __totalCapacity._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 108, 6)
    
    totalCapacity = property(__totalCapacity.value, __totalCapacity.set, None, '\n               Dinghy Total Capacity: The total number of persons that can be accommodated by the \n               dinghies carried on board the aircraft. \n               .Dinghy Total Capacity: The total number of persons that can be accommodated by the \n               dinghies carried on board the aircraft. \n            ')

    _ElementMap.update({
        __colour.name() : __colour
    })
    _AttributeMap.update({
        __covered.name() : __covered,
        __quantity.name() : __quantity,
        __totalCapacity.name() : __totalCapacity
    })
_module_typeBindings.DinghyType = DinghyType
Namespace.addCategoryObject('typeBinding', 'DinghyType', DinghyType)


# Complex type {http://www.fixm.aero/flight/3.0}SurvivalCapabilitiesType with content type ELEMENT_ONLY
class SurvivalCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups the aircraft survival capabilities. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SurvivalCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 206, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dinghyInformation uses Python identifier dinghyInformation
    __dinghyInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dinghyInformation'), 'dinghyInformation', '__httpwww_fixm_aeroflight3_0_SurvivalCapabilitiesType_dinghyInformation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 213, 9), )

    
    dinghyInformation = property(__dinghyInformation.value, __dinghyInformation.set, None, '\n                  Describes the aircraft dingy. \n               ')

    
    # Element emergencyRadioCode uses Python identifier emergencyRadioCode
    __emergencyRadioCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emergencyRadioCode'), 'emergencyRadioCode', '__httpwww_fixm_aeroflight3_0_SurvivalCapabilitiesType_emergencyRadioCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 220, 9), )

    
    emergencyRadioCode = property(__emergencyRadioCode.value, __emergencyRadioCode.set, None, '\n                  .Emergency Radio Transmitter Type: The type of serviceable communication devices \n                  available on the aircraft that are able to transmit an emergency radio signal. \n               ')

    
    # Element lifeJacketCode uses Python identifier lifeJacketCode
    __lifeJacketCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lifeJacketCode'), 'lifeJacketCode', '__httpwww_fixm_aeroflight3_0_SurvivalCapabilitiesType_lifeJacketCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 231, 9), )

    
    lifeJacketCode = property(__lifeJacketCode.value, __lifeJacketCode.set, None, '\n                  .Life Jacket Type: The type of life jackets available on board the aircraft. \n               ')

    
    # Element survivalEquipmentCode uses Python identifier survivalEquipmentCode
    __survivalEquipmentCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'survivalEquipmentCode'), 'survivalEquipmentCode', '__httpwww_fixm_aeroflight3_0_SurvivalCapabilitiesType_survivalEquipmentCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 241, 9), )

    
    survivalEquipmentCode = property(__survivalEquipmentCode.value, __survivalEquipmentCode.set, None, '\n                  .Survival Equipment Type: The type of equipment carried on board the aircraft that \n                  can be used by the crew and passengers to assist survival in harsh environments in \n                  case of emergency. \n               ')

    
    # Attribute survivalEquipmentRemarks uses Python identifier survivalEquipmentRemarks
    __survivalEquipmentRemarks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'survivalEquipmentRemarks'), 'survivalEquipmentRemarks', '__httpwww_fixm_aeroflight3_0_SurvivalCapabilitiesType_survivalEquipmentRemarks', _ImportedBinding__fb.FreeTextType)
    __survivalEquipmentRemarks._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 254, 6)
    __survivalEquipmentRemarks._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 254, 6)
    
    survivalEquipmentRemarks = property(__survivalEquipmentRemarks.value, __survivalEquipmentRemarks.set, None, '\n               .Survival Equipment Remarks: A description of survival equipment carried on the aircraft \n               and any other useful remarks regarding survival equipment. \n            ')

    _ElementMap.update({
        __dinghyInformation.name() : __dinghyInformation,
        __emergencyRadioCode.name() : __emergencyRadioCode,
        __lifeJacketCode.name() : __lifeJacketCode,
        __survivalEquipmentCode.name() : __survivalEquipmentCode
    })
    _AttributeMap.update({
        __survivalEquipmentRemarks.name() : __survivalEquipmentRemarks
    })
_module_typeBindings.SurvivalCapabilitiesType = SurvivalCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'SurvivalCapabilitiesType', SurvivalCapabilitiesType)


# Complex type {http://www.fixm.aero/flight/3.0}AirWaybillType with content type SIMPLE
class AirWaybillType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Air Waybill Number: The number referencing the air waybill. 
         """
    _TypeDefinition = _ImportedBinding__fb.FreeTextType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirWaybillType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 130, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__fb.FreeTextType
    
    # Attribute airWaybillNumber uses Python identifier airWaybillNumber
    __airWaybillNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airWaybillNumber'), 'airWaybillNumber', '__httpwww_fixm_aeroflight3_0_AirWaybillType_airWaybillNumber', _ImportedBinding__fb.FreeTextType)
    __airWaybillNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 138, 12)
    __airWaybillNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 138, 12)
    
    airWaybillNumber = property(__airWaybillNumber.value, __airWaybillNumber.set, None, '\n                     .Air Waybill Number: The number referencing the air waybill. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __airWaybillNumber.name() : __airWaybillNumber
    })
_module_typeBindings.AirWaybillType = AirWaybillType
Namespace.addCategoryObject('typeBinding', 'AirWaybillType', AirWaybillType)


# Complex type {http://www.fixm.aero/flight/3.0}DeclarationTextType with content type EMPTY
class DeclarationTextType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Declaration Text: Consignor: The consignor's statement indicating the dangerous 
            goods have been packaged and handled according to regulations. 
            .Declaration Text: Shipper: This shipper's statement indicating the dangerous goods 
            have been packaged and handled according to regulations. 
            .Declaration Text: Compliance: The warning message for not complying with the regulations. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclarationTextType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 240, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute compliance uses Python identifier compliance
    __compliance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'compliance'), 'compliance', '__httpwww_fixm_aeroflight3_0_DeclarationTextType_compliance', _ImportedBinding__fb.FreeTextType)
    __compliance._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 251, 6)
    __compliance._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 251, 6)
    
    compliance = property(__compliance.value, __compliance.set, None, '\n               .Declaration Text: Compliance: The warning message for not complying with the regulations. \n               \n            ')

    
    # Attribute consignor uses Python identifier consignor
    __consignor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'consignor'), 'consignor', '__httpwww_fixm_aeroflight3_0_DeclarationTextType_consignor', _ImportedBinding__fb.FreeTextType)
    __consignor._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 259, 6)
    __consignor._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 259, 6)
    
    consignor = property(__consignor.value, __consignor.set, None, "\n               .Declaration Text: Consignor: The consignor's statement indicating the dangerous \n               goods have been packaged and handled according to regulations. \n            ")

    
    # Attribute shipper uses Python identifier shipper
    __shipper = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shipper'), 'shipper', '__httpwww_fixm_aeroflight3_0_DeclarationTextType_shipper', _ImportedBinding__fb.FreeTextType)
    __shipper._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 267, 6)
    __shipper._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 267, 6)
    
    shipper = property(__shipper.value, __shipper.set, None, "\n               .Declaration Text: Shipper: This shipper's statement indicating the dangerous goods \n               have been packaged and handled according to regulations. \n            ")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __compliance.name() : __compliance,
        __consignor.name() : __consignor,
        __shipper.name() : __shipper
    })
_module_typeBindings.DeclarationTextType = DeclarationTextType
Namespace.addCategoryObject('typeBinding', 'DeclarationTextType', DeclarationTextType)


# Complex type {http://www.fixm.aero/flight/3.0}ShippingInformationType with content type ELEMENT_ONLY
class ShippingInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            IATA Shipper's Declaration for Dangerous Goods. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShippingInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 296, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element aerodromeOfLoading uses Python identifier aerodromeOfLoading
    __aerodromeOfLoading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aerodromeOfLoading'), 'aerodromeOfLoading', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_aerodromeOfLoading', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 303, 9), )

    
    aerodromeOfLoading = property(__aerodromeOfLoading.value, __aerodromeOfLoading.set, None, '\n                  .Aerodrome of Loading: The aerodrome where dangerous goods were loaded onto the flight. \n                  \n               ')

    
    # Element aerodromeOfUnloading uses Python identifier aerodromeOfUnloading
    __aerodromeOfUnloading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aerodromeOfUnloading'), 'aerodromeOfUnloading', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_aerodromeOfUnloading', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 311, 9), )

    
    aerodromeOfUnloading = property(__aerodromeOfUnloading.value, __aerodromeOfUnloading.set, None, '\n                  .Aerodrome of Unloading: The aerodrome where dangerous goods were unloaded from the \n                  flight. \n               ')

    
    # Element consignee uses Python identifier consignee
    __consignee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'consignee'), 'consignee', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_consignee', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 319, 9), )

    
    consignee = property(__consignee.value, __consignee.set, None, "\n                  .Consignee Name and Address: The XML Grouping Element unites the Consignee Name with \n                  the Postal Structure Address (detailed breakout of address components). \n                  .Consignee Phone Number: The phone number of the consignee contact department or \n                  person to call, in the event of an emergency, security event, or when further information \n                  about the shipment is needed. \n                  .Consignee Contact Name: The name of the consignee contact department or person responsible \n                  in the event of an emergency, security event, or when further information about the \n                  shipment is needed. \n                  .Consignee Address: Specifies the consignee's mailing address. \n                  .Consignee Name: Contains the name or legal identity of the organization or person \n                  receiving the package. \n               ")

    
    # Element declarationText uses Python identifier declarationText
    __declarationText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'declarationText'), 'declarationText', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_declarationText', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 336, 9), )

    
    declarationText = property(__declarationText.value, __declarationText.set, None, '\n                  compliance: \n                   \n                  consignor: \n                   \n                  shipper: \n               ')

    
    # Element shipper uses Python identifier shipper
    __shipper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shipper'), 'shipper', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_shipper', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 347, 9), )

    
    shipper = property(__shipper.value, __shipper.set, None, "\n                  .Shipper Address: The shipper's mailing address. \n                  .Shipper Emergency Phone Number: Phone number of the shipper or someone who is not \n                  on board the aircraft and who can be reached in an emergency involving the dangerous \n                  good. \n                  .Shipper Name and Address: The XML Grouping Element unites the Shipper (Consignor) \n                  Name with the Postal Structure Address (detailed breakout of address components). \n                  \n                  .Shipper Name: The Shipper's name, legal identity, and/or organization. \n               ")

    
    # Element transferAerodromes uses Python identifier transferAerodromes
    __transferAerodromes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transferAerodromes'), 'transferAerodromes', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_transferAerodromes', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 361, 9), )

    
    transferAerodromes = property(__transferAerodromes.value, __transferAerodromes.set, None, '\n                  .Transfer Aerodromes: A list of the aerodromes through which the package has travelled \n                  en route to its final destination. \n               ')

    
    # Attribute dangerousGoodsScreeningLocation uses Python identifier dangerousGoodsScreeningLocation
    __dangerousGoodsScreeningLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dangerousGoodsScreeningLocation'), 'dangerousGoodsScreeningLocation', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_dangerousGoodsScreeningLocation', _ImportedBinding__fb.FreeTextType)
    __dangerousGoodsScreeningLocation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 373, 6)
    __dangerousGoodsScreeningLocation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 373, 6)
    
    dangerousGoodsScreeningLocation = property(__dangerousGoodsScreeningLocation.value, __dangerousGoodsScreeningLocation.set, None, '\n               .Dangerous Goods Screening Location: The name of the Certified Cargo Screening Facility, \n               as approved by the Transportation Security Administration (TSA), or the location/name \n               of any screening performed. \n            ')

    
    # Attribute departureCountry uses Python identifier departureCountry
    __departureCountry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departureCountry'), 'departureCountry', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_departureCountry', _ImportedBinding__ff.TextCountryNameType)
    __departureCountry._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 382, 6)
    __departureCountry._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 382, 6)
    
    departureCountry = property(__departureCountry.value, __departureCountry.set, None, '\n               .Departure Country: The Code and Name of the departure country where the package \n               originated. \n            ')

    
    # Attribute destinationCountry uses Python identifier destinationCountry
    __destinationCountry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'destinationCountry'), 'destinationCountry', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_destinationCountry', _ImportedBinding__ff.TextCountryNameType)
    __destinationCountry._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 390, 6)
    __destinationCountry._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 390, 6)
    
    destinationCountry = property(__destinationCountry.value, __destinationCountry.set, None, "\n               .Destination Country: The Name and Code of the dangerous good's country of destination. \n               \n            ")

    
    # Attribute originCountry uses Python identifier originCountry
    __originCountry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'originCountry'), 'originCountry', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_originCountry', _ImportedBinding__ff.TextCountryNameType)
    __originCountry._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 398, 6)
    __originCountry._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 398, 6)
    
    originCountry = property(__originCountry.value, __originCountry.set, None, '\n               .Departure Country: The Code and Name of the departure country where the package \n               originated. \n            ')

    
    # Attribute shipmentAuthorizations uses Python identifier shipmentAuthorizations
    __shipmentAuthorizations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shipmentAuthorizations'), 'shipmentAuthorizations', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_shipmentAuthorizations', _ImportedBinding__fb.FreeTextType)
    __shipmentAuthorizations._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 406, 6)
    __shipmentAuthorizations._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 406, 6)
    
    shipmentAuthorizations = property(__shipmentAuthorizations.value, __shipmentAuthorizations.set, None, '\n               .Shipment Authorizations: Additional information related to an approval, permission, \n               or other specific detail regarding the shipment of dangerous goods. \n            ')

    
    # Attribute subsidiaryHazardClassAndDivision uses Python identifier subsidiaryHazardClassAndDivision
    __subsidiaryHazardClassAndDivision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subsidiaryHazardClassAndDivision'), 'subsidiaryHazardClassAndDivision', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_subsidiaryHazardClassAndDivision', _ImportedBinding__fb.FreeTextType)
    __subsidiaryHazardClassAndDivision._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 414, 6)
    __subsidiaryHazardClassAndDivision._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 414, 6)
    
    subsidiaryHazardClassAndDivision = property(__subsidiaryHazardClassAndDivision.value, __subsidiaryHazardClassAndDivision.set, None, '\n               .Subsidiary Hazard Class and Division: An identifier of any subsidiary hazard class(es)/division(s) \n               in addition to the primary hazard class and division. \n            ')

    
    # Attribute supplementaryInformation uses Python identifier supplementaryInformation
    __supplementaryInformation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supplementaryInformation'), 'supplementaryInformation', '__httpwww_fixm_aeroflight3_0_ShippingInformationType_supplementaryInformation', _ImportedBinding__fb.FreeTextType)
    __supplementaryInformation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 422, 6)
    __supplementaryInformation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 422, 6)
    
    supplementaryInformation = property(__supplementaryInformation.value, __supplementaryInformation.set, None, '\n               .Supplementary Information: Additional information that may be added to the proper \n               shipping name to more fully describe the goods or to identify a particular condition. \n               \n               .Supplementary Shipping Information: Additional information that may be added to \n               the proper shipping name to more fully describe the goods or to identify a particular \n               condition. \n            ')

    _ElementMap.update({
        __aerodromeOfLoading.name() : __aerodromeOfLoading,
        __aerodromeOfUnloading.name() : __aerodromeOfUnloading,
        __consignee.name() : __consignee,
        __declarationText.name() : __declarationText,
        __shipper.name() : __shipper,
        __transferAerodromes.name() : __transferAerodromes
    })
    _AttributeMap.update({
        __dangerousGoodsScreeningLocation.name() : __dangerousGoodsScreeningLocation,
        __departureCountry.name() : __departureCountry,
        __destinationCountry.name() : __destinationCountry,
        __originCountry.name() : __originCountry,
        __shipmentAuthorizations.name() : __shipmentAuthorizations,
        __subsidiaryHazardClassAndDivision.name() : __subsidiaryHazardClassAndDivision,
        __supplementaryInformation.name() : __supplementaryInformation
    })
_module_typeBindings.ShippingInformationType = ShippingInformationType
Namespace.addCategoryObject('typeBinding', 'ShippingInformationType', ShippingInformationType)


# Complex type {http://www.fixm.aero/flight/3.0}DangerousGoodsPackageGroupType with content type ELEMENT_ONLY
class DangerousGoodsPackageGroupType (pyxb.binding.basis.complexTypeDefinition):
    """
            A collection of at least one DangerousGoodsPackage. 
            .Shipper's Declaration For Dangerous Goods Packaging Detail: The part of the IATA 
            Shipper's Declaration For Dangerous Goods that contains the packaging details for 
            this shipment. 
            .Dangerous Goods Package Details: The part of the IATA Shipper's Declaration For 
            Dangerous Goods that contains the Package Details for the shipment. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsPackageGroupType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 378, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dangerousGoodsPackage uses Python identifier dangerousGoodsPackage
    __dangerousGoodsPackage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dangerousGoodsPackage'), 'dangerousGoodsPackage', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageGroupType_dangerousGoodsPackage', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 390, 9), )

    
    dangerousGoodsPackage = property(__dangerousGoodsPackage.value, __dangerousGoodsPackage.set, None, '\n                  A collection of at least one DangerousGoodsPackage. \n               ')

    
    # Element shipmentDimensions uses Python identifier shipmentDimensions
    __shipmentDimensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shipmentDimensions'), 'shipmentDimensions', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageGroupType_shipmentDimensions', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 397, 9), )

    
    shipmentDimensions = property(__shipmentDimensions.value, __shipmentDimensions.set, None, '\n                  Weight and volume (not height, width, and depth): \n               ')

    
    # Attribute shipmentUseIndicator uses Python identifier shipmentUseIndicator
    __shipmentUseIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shipmentUseIndicator'), 'shipmentUseIndicator', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageGroupType_shipmentUseIndicator', _module_typeBindings.ShipmentUseType)
    __shipmentUseIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 405, 6)
    __shipmentUseIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 405, 6)
    
    shipmentUseIndicator = property(__shipmentUseIndicator.value, __shipmentUseIndicator.set, None, '\n               .Exclusive Use Shipment Indicator: An indicator of sole use, by a single shipper, \n               of an aircraft or of a large freight container, of which all initial, intermediate \n               and final loading and unloading is carried out in accordance with the directions \n               of the shipper or consignee. \n            ')

    _ElementMap.update({
        __dangerousGoodsPackage.name() : __dangerousGoodsPackage,
        __shipmentDimensions.name() : __shipmentDimensions
    })
    _AttributeMap.update({
        __shipmentUseIndicator.name() : __shipmentUseIndicator
    })
_module_typeBindings.DangerousGoodsPackageGroupType = DangerousGoodsPackageGroupType
Namespace.addCategoryObject('typeBinding', 'DangerousGoodsPackageGroupType', DangerousGoodsPackageGroupType)


# Complex type {http://www.fixm.aero/flight/3.0}RadioactiveMaterialActivityType with content type SIMPLE
class RadioactiveMaterialActivityType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Activity: The measure of the rate of decay, or activity, of a radioactive material. 
            
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadioactiveMaterialActivityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 187, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__ff.UnitOfMeasureType
    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uom'), 'uom', '__httpwww_fixm_aeroflight3_0_RadioactiveMaterialActivityType_uom', _module_typeBindings.RadioactivityMeasureType, required=True)
    __uom._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 196, 12)
    __uom._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 196, 12)
    
    uom = property(__uom.value, __uom.set, None, '\n                     Units of measure of for RadioactiveMaterialActivity. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uom.name() : __uom
    })
_module_typeBindings.RadioactiveMaterialActivityType = RadioactiveMaterialActivityType
Namespace.addCategoryObject('typeBinding', 'RadioactiveMaterialActivityType', RadioactiveMaterialActivityType)


# Complex type {http://www.fixm.aero/flight/3.0}BoundaryCrossingType with content type ELEMENT_ONLY
class BoundaryCrossingType (pyxb.binding.basis.complexTypeDefinition):
    """
            Abstract Boundary Crossing contains shared data between the BoundaryCrossingProposed 
            and BoundaryCrossingCoordinated classes. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundaryCrossingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 113, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altitude'), 'altitude', '__httpwww_fixm_aeroflight3_0_BoundaryCrossingType_altitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 121, 9), )

    
    altitude = property(__altitude.value, __altitude.set, None, '\n                  .Boundary Crossing Level - Cleared/Coordinated: The cleared altitude (flight level) \n                  at which the aircraft will cross the boundary crossing point if in level cruising \n                  flight or, if the aircraft is climbing or descending at the boundary crossing point, \n                  the cleared flight level to which it is proceeding. \n                  .Boundary Crossing Level - Cleared Block - Proposed: The proposed vertical range \n                  of levels transmitted as the boundary crossing level during negotiation between controllers. \n                  \n                  .Boundary Crossing Level - Transition/Coordinated: An altitude (flight level) at \n                  or above/below which an aircraft will cross the associated boundary point. \n                  .Boundary Crossing Level - Cleared Block/Coordinated: A vertical range of levels \n                  transmitted as the boundary crossing level. \n                  .Boundary Crossing Level - Proposed: If the aircraft is at level cruising, the proposed \n                  altitude (flight level) at which the aircraft will cross the boundary crossing point. \n                   If the aircraft is climbing or descending at the boundary crossing point, then the \n                  proposed cruise flight level to which it is proceeding when it crosses the boundary \n                  crossing point. \n               ')

    
    # Element altitudeInTransition uses Python identifier altitudeInTransition
    __altitudeInTransition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altitudeInTransition'), 'altitudeInTransition', '__httpwww_fixm_aeroflight3_0_BoundaryCrossingType_altitudeInTransition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 143, 9), )

    
    altitudeInTransition = property(__altitudeInTransition.value, __altitudeInTransition.set, None, '\n                  Negotiated boundary crossing transition altitude. \n               ')

    
    # Element crossingPoint uses Python identifier crossingPoint
    __crossingPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'crossingPoint'), 'crossingPoint', '__httpwww_fixm_aeroflight3_0_BoundaryCrossingType_crossingPoint', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 150, 9), )

    
    crossingPoint = property(__crossingPoint.value, __crossingPoint.set, None, '\n                  .Boundary Crossing Point/Coordinated: The point where the flight will cross an ATS \n                  facility boundary. \n                  .Boundary Crossing Point - Proposed: The proposed point where the flight will cross \n                  an ATS facility boundary, as requested by the accepting controller from the transferring \n                  controller. \n               ')

    
    # Element crossingSpeed uses Python identifier crossingSpeed
    __crossingSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'crossingSpeed'), 'crossingSpeed', '__httpwww_fixm_aeroflight3_0_BoundaryCrossingType_crossingSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 161, 9), )

    
    crossingSpeed = property(__crossingSpeed.value, __crossingSpeed.set, None, '\n                  .Boundary Crossing - Assigned Speed - Proposed: During negotiation between controllers, \n                  the proposed clearance information assigning a speed (or range of speeds) and speed \n                  condition to the flight at the boundary point.  The speed condition indicates whether \n                  the aircraft will be maintaining, exceeding, or flying more slowly than the assigned \n                  boundary crossing speed. \n                  .Boundary Crossing - Assigned Speed/Coordinated: Clearance information assigning \n                  a speed (or range of speeds) and speed condition to the flight at the boundary point. \n                   The speed condition indicates whether the aircraft will be maintaining, exceeding, \n                  or flying more slowly than the assigned boundary crossing speed. \n               ')

    
    # Element offtrack uses Python identifier offtrack
    __offtrack = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offtrack'), 'offtrack', '__httpwww_fixm_aeroflight3_0_BoundaryCrossingType_offtrack', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 176, 9), )

    
    offtrack = property(__offtrack.value, __offtrack.set, None, '\n                  .Boundary Crossing - Off Track Information - Proposed: Provides the off track clearance \n                  information, if the flight is proposed to be off track at the boundary crossing point. \n                   For the boundary crossing point, the off track information includes the off track \n                  direction, the distance and the reason the aircraft is off track. \n                  .Boundary Crossing - Off Track Information/Coordinated: Provides the off track clearance \n                  information, if the flight will be off track at the boundary crossing point.  For \n                  the boundary crossing point, the off track information includes the off track direction, \n                  the distance and the reason the aircraft is off track. \n               ')

    
    # Attribute crossingTime uses Python identifier crossingTime
    __crossingTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crossingTime'), 'crossingTime', '__httpwww_fixm_aeroflight3_0_BoundaryCrossingType_crossingTime', _ImportedBinding__ff.TimeType)
    __crossingTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 191, 6)
    __crossingTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 191, 6)
    
    crossingTime = property(__crossingTime.value, __crossingTime.set, None, '\n               .Boundary Crossing Time - Proposed: The estimated time when the flight will cross \n               the Boundary Crossing Point - Proposed, as requested by the accepting controller \n               from the transferring controller. \n               .Boundary Crossing Time/Coordinated: The estimated time at which a flight will cross \n               the associated boundary crossing point. \n            ')

    _ElementMap.update({
        __altitude.name() : __altitude,
        __altitudeInTransition.name() : __altitudeInTransition,
        __crossingPoint.name() : __crossingPoint,
        __crossingSpeed.name() : __crossingSpeed,
        __offtrack.name() : __offtrack
    })
    _AttributeMap.update({
        __crossingTime.name() : __crossingTime
    })
_module_typeBindings.BoundaryCrossingType = BoundaryCrossingType
Namespace.addCategoryObject('typeBinding', 'BoundaryCrossingType', BoundaryCrossingType)


# Complex type {http://www.fixm.aero/flight/3.0}CoordinationStatusType with content type EMPTY
class CoordinationStatusType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Coordination Status: The status of Coordination and Transfer of Control between 
            the currently Controlling Air Traffic Service Unit (ATSU) to the downstream to be 
            Controlling ATSU. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoordinationStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 94, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute abrogationReason uses Python identifier abrogationReason
    __abrogationReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'abrogationReason'), 'abrogationReason', '__httpwww_fixm_aeroflight3_0_CoordinationStatusType_abrogationReason', _module_typeBindings.AbrogationReasonCodeType)
    __abrogationReason._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 102, 6)
    __abrogationReason._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 102, 6)
    
    abrogationReason = property(__abrogationReason.value, __abrogationReason.set, None, '\n               .Abrogation Reason: If the Coordination Status is abrogated, indicating coordination \n               is abolished by authoritative action, the reason the coordination was terminated. \n               \n            ')

    
    # Attribute coordinationStatus uses Python identifier coordinationStatus
    __coordinationStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coordinationStatus'), 'coordinationStatus', '__httpwww_fixm_aeroflight3_0_CoordinationStatusType_coordinationStatus', _module_typeBindings.CoordinationStatusCodeType)
    __coordinationStatus._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 111, 6)
    __coordinationStatus._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 111, 6)
    
    coordinationStatus = property(__coordinationStatus.value, __coordinationStatus.set, None, '\n               .Coordination Status: The status of Coordination and Transfer of Control between \n               the currently Controlling Air Traffic Service Unit (ATSU) to the downstream to be \n               Controlling ATSU. \n            ')

    
    # Attribute nonStandardCommunicationReason uses Python identifier nonStandardCommunicationReason
    __nonStandardCommunicationReason = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nonStandardCommunicationReason'), 'nonStandardCommunicationReason', '__httpwww_fixm_aeroflight3_0_CoordinationStatusType_nonStandardCommunicationReason', _module_typeBindings.NonStandardCoordinationReasonType)
    __nonStandardCommunicationReason._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 120, 6)
    __nonStandardCommunicationReason._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 120, 6)
    
    nonStandardCommunicationReason = property(__nonStandardCommunicationReason.value, __nonStandardCommunicationReason.set, None, '\n               .Reason for Non-Standard Coordination: In case of non-standard coordination, the \n               reason for non-standard coordination is indicated. \n            ')

    
    # Attribute releaseConditions uses Python identifier releaseConditions
    __releaseConditions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'releaseConditions'), 'releaseConditions', '__httpwww_fixm_aeroflight3_0_CoordinationStatusType_releaseConditions', _module_typeBindings.ReleaseConditionsType)
    __releaseConditions._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 128, 6)
    __releaseConditions._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 128, 6)
    
    releaseConditions = property(__releaseConditions.value, __releaseConditions.set, None, '\n               .Release Conditions: When the flight is released from the agreed transfer conditions, \n               contains the Release conditions specified by the transferring ATSUs.  The Release \n               conditions indicate the type of manoeuvres the flight is released to perform. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __abrogationReason.name() : __abrogationReason,
        __coordinationStatus.name() : __coordinationStatus,
        __nonStandardCommunicationReason.name() : __nonStandardCommunicationReason,
        __releaseConditions.name() : __releaseConditions
    })
_module_typeBindings.CoordinationStatusType = CoordinationStatusType
Namespace.addCategoryObject('typeBinding', 'CoordinationStatusType', CoordinationStatusType)


# Complex type {http://www.fixm.aero/flight/3.0}AirspaceConstraintType with content type ELEMENT_ONLY
class AirspaceConstraintType (pyxb.binding.basis.complexTypeDefinition):
    """
            Represents an airspace that has been constrained such as flow constrained area with 
            associated controlled time. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspaceConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 84, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element airspaceControlledEntryTime uses Python identifier airspaceControlledEntryTime
    __airspaceControlledEntryTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airspaceControlledEntryTime'), 'airspaceControlledEntryTime', '__httpwww_fixm_aeroflight3_0_AirspaceConstraintType_airspaceControlledEntryTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 92, 9), )

    
    airspaceControlledEntryTime = property(__airspaceControlledEntryTime.value, __airspaceControlledEntryTime.set, None, '\n                  .Airspace Entry Time - Controlled: The time at which a flight is required to arrive \n                  at a constrained airspace element as a result of a tactical slot allocation or a \n                  Traffic Management Initiative (TMI). \n               ')

    
    # Attribute constrainedAirspace uses Python identifier constrainedAirspace
    __constrainedAirspace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'constrainedAirspace'), 'constrainedAirspace', '__httpwww_fixm_aeroflight3_0_AirspaceConstraintType_constrainedAirspace', _ImportedBinding__fb.ConstrainedAirspaceType)
    __constrainedAirspace._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 102, 6)
    __constrainedAirspace._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 102, 6)
    
    constrainedAirspace = property(__constrainedAirspace.value, __constrainedAirspace.set, None, '\n               Constrained Airspace associated with the airspace controlled entry time. \n            ')

    _ElementMap.update({
        __airspaceControlledEntryTime.name() : __airspaceControlledEntryTime
    })
    _AttributeMap.update({
        __constrainedAirspace.name() : __constrainedAirspace
    })
_module_typeBindings.AirspaceConstraintType = AirspaceConstraintType
Namespace.addCategoryObject('typeBinding', 'AirspaceConstraintType', AirspaceConstraintType)


# Complex type {http://www.fixm.aero/flight/3.0}PlannedReportingPositionType with content type ELEMENT_ONLY
class PlannedReportingPositionType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Aircraft Planned Reporting Position: Estimated future position, altitude and time 
            of the aircraft transmitted in a non-radar airspace position report. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlannedReportingPositionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 204, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpwww_fixm_aeroflight3_0_PlannedReportingPositionType_position', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 212, 9), )

    
    position = property(__position.value, __position.set, None, '\n                  Planned reporting position point. \n               ')

    
    # Element positionAltitude uses Python identifier positionAltitude
    __positionAltitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'positionAltitude'), 'positionAltitude', '__httpwww_fixm_aeroflight3_0_PlannedReportingPositionType_positionAltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 219, 9), )

    
    positionAltitude = property(__positionAltitude.value, __positionAltitude.set, None, '\n                  Altitude associated with the planned reporting position. \n                  .Next Future Reporting Position Altitude: Expected altitude at the estimated next \n                  future position of the aircraft transmitted in a non-radar airspace position report. \n                  \n                  .Following Future Reporting Position Altitude: Expected altitude at the estimated \n                  second future position of the aircraft transmitted in a non-radar airspace position \n                  report. \n               ')

    
    # Attribute positionEstimatedTime uses Python identifier positionEstimatedTime
    __positionEstimatedTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positionEstimatedTime'), 'positionEstimatedTime', '__httpwww_fixm_aeroflight3_0_PlannedReportingPositionType_positionEstimatedTime', _ImportedBinding__ff.TimeType)
    __positionEstimatedTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 233, 6)
    __positionEstimatedTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 233, 6)
    
    positionEstimatedTime = property(__positionEstimatedTime.value, __positionEstimatedTime.set, None, '\n               Estimated time associated with the planned reporting position. \n               .Next Future Reporting Position Time - Estimated: Estimated time at the next future \n               position of the aircraft transmitted in a non-radar airspace position report. \n               .Following Future Reporting Position Time - Estimated: Estimated time at the second \n               future position of the aircraft transmitted in a non-radar airspace position report. \n               \n            ')

    _ElementMap.update({
        __position.name() : __position,
        __positionAltitude.name() : __positionAltitude
    })
    _AttributeMap.update({
        __positionEstimatedTime.name() : __positionEstimatedTime
    })
_module_typeBindings.PlannedReportingPositionType = PlannedReportingPositionType
Namespace.addCategoryObject('typeBinding', 'PlannedReportingPositionType', PlannedReportingPositionType)


# Complex type {http://www.fixm.aero/flight/3.0}RouteConstraintOrPreferenceType with content type EMPTY
class RouteConstraintOrPreferenceType (pyxb.binding.basis.complexTypeDefinition):
    """
            A constraint that is applicable to a route. Can be any of the several defined constraints. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RouteConstraintOrPreferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 208, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute constraintType uses Python identifier constraintType
    __constraintType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'constraintType'), 'constraintType', '__httpwww_fixm_aeroflight3_0_RouteConstraintOrPreferenceType_constraintType', _module_typeBindings.ConstraintOrPreferenceCategoryType)
    __constraintType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 215, 6)
    __constraintType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 215, 6)
    
    constraintType = property(__constraintType.value, __constraintType.set, None, '\n               .Constraint Category: Specifies the category (implying a relative importance) of \n               the constraint associated with a point in the route or expanded route. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __constraintType.name() : __constraintType
    })
_module_typeBindings.RouteConstraintOrPreferenceType = RouteConstraintOrPreferenceType
Namespace.addCategoryObject('typeBinding', 'RouteConstraintOrPreferenceType', RouteConstraintOrPreferenceType)


# Complex type {http://www.fixm.aero/flight/3.0}LastPositionReportType with content type ELEMENT_ONLY
class LastPositionReportType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Last Known Position Report: The position of the aircraft last known to ATS and a 
            corresponding timestamp. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LastPositionReportType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 208, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpwww_fixm_aeroflight3_0_LastPositionReportType_position', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 216, 9), )

    
    position = property(__position.value, __position.set, None, '\n                  The position of the aircraft last known to ATS. \n               ')

    
    # Attribute determinationMethod uses Python identifier determinationMethod
    __determinationMethod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'determinationMethod'), 'determinationMethod', '__httpwww_fixm_aeroflight3_0_LastPositionReportType_determinationMethod', _ImportedBinding__fb.FreeTextType)
    __determinationMethod._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 224, 6)
    __determinationMethod._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 224, 6)
    
    determinationMethod = property(__determinationMethod.value, __determinationMethod.set, None, '\n               .Last Known Position Report - Determination Method: A plain-language description \n               of the method used to determine the last known position of an aircraft. \n            ')

    
    # Attribute timeAtPosition uses Python identifier timeAtPosition
    __timeAtPosition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeAtPosition'), 'timeAtPosition', '__httpwww_fixm_aeroflight3_0_LastPositionReportType_timeAtPosition', _ImportedBinding__ff.TimeType)
    __timeAtPosition._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 232, 6)
    __timeAtPosition._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 232, 6)
    
    timeAtPosition = property(__timeAtPosition.value, __timeAtPosition.set, None, '\n               Timestamp corresponding to the last known position. \n            ')

    _ElementMap.update({
        __position.name() : __position
    })
    _AttributeMap.update({
        __determinationMethod.name() : __determinationMethod,
        __timeAtPosition.name() : __timeAtPosition
    })
_module_typeBindings.LastPositionReportType = LastPositionReportType
Namespace.addCategoryObject('typeBinding', 'LastPositionReportType', LastPositionReportType)


# Complex type {http://www.fixm.aero/flight/3.0}AircraftOperatorType with content type ELEMENT_ONLY
class AircraftOperatorType (pyxb.binding.basis.complexTypeDefinition):
    """
            Contains information about the identify of aircraft operator. 
            .Flight Plan Filer: The name of the unit, agency or person filing the flight plan. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftOperatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 90, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element operatingOrganization uses Python identifier operatingOrganization
    __operatingOrganization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'operatingOrganization'), 'operatingOrganization', '__httpwww_fixm_aeroflight3_0_AircraftOperatorType_operatingOrganization', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 99, 9), )

    
    operatingOrganization = property(__operatingOrganization.value, __operatingOrganization.set, None, '\n                  .Aircraft Operator Identity: Identity of a person, organization or enterprise engaged \n                  in or offering to engage in aircraft operation. \n               ')

    
    # Attribute operatorCategory uses Python identifier operatorCategory
    __operatorCategory = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'operatorCategory'), 'operatorCategory', '__httpwww_fixm_aeroflight3_0_AircraftOperatorType_operatorCategory', _module_typeBindings.OperatorCategoryType)
    __operatorCategory._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 108, 6)
    __operatorCategory._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 108, 6)
    
    operatorCategory = property(__operatorCategory.value, __operatorCategory.set, None, '\n               .Flight Operator Category: The category of the flight operator operating the flight. \n               \n            ')

    _ElementMap.update({
        __operatingOrganization.name() : __operatingOrganization
    })
    _AttributeMap.update({
        __operatorCategory.name() : __operatorCategory
    })
_module_typeBindings.AircraftOperatorType = AircraftOperatorType
Namespace.addCategoryObject('typeBinding', 'AircraftOperatorType', AircraftOperatorType)


# Complex type {http://www.fixm.aero/flight/3.0}FlightIdentificationType with content type ELEMENT_ONLY
class FlightIdentificationType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups flight identifying data such as the aircraft and carrier information. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 353, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element marketingCarrierFlightIdentifier uses Python identifier marketingCarrierFlightIdentifier
    __marketingCarrierFlightIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'marketingCarrierFlightIdentifier'), 'marketingCarrierFlightIdentifier', '__httpwww_fixm_aeroflight3_0_FlightIdentificationType_marketingCarrierFlightIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 360, 9), )

    
    marketingCarrierFlightIdentifier = property(__marketingCarrierFlightIdentifier.value, __marketingCarrierFlightIdentifier.set, None, '\n                  .Aircraft Identification - Marketing Carrier: The aircraft identification used by \n                  a carrier who has sold tickets for the flight but is not involved with the operation \n                  of the flight. \n               ')

    
    # Attribute aircraftIdentification uses Python identifier aircraftIdentification
    __aircraftIdentification = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aircraftIdentification'), 'aircraftIdentification', '__httpwww_fixm_aeroflight3_0_FlightIdentificationType_aircraftIdentification', _ImportedBinding__fb.FlightIdentifierType)
    __aircraftIdentification._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 373, 6)
    __aircraftIdentification._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 373, 6)
    
    aircraftIdentification = property(__aircraftIdentification.value, __aircraftIdentification.set, None, '\n               .Aircraft Identification: Name used by Air Traffic Services units to identify and \n               communicate with an aircraft. \n            ')

    
    # Attribute majorCarrierIdentifier uses Python identifier majorCarrierIdentifier
    __majorCarrierIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'majorCarrierIdentifier'), 'majorCarrierIdentifier', '__httpwww_fixm_aeroflight3_0_FlightIdentificationType_majorCarrierIdentifier', _ImportedBinding__fb.CarrierIdentifierType)
    __majorCarrierIdentifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 381, 6)
    __majorCarrierIdentifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 381, 6)
    
    majorCarrierIdentifier = property(__majorCarrierIdentifier.value, __majorCarrierIdentifier.set, None, '\n               .Major Carrier Identifier: The identification of the carrier who has contracted out \n               the operation of the flight to a sub-carrier. \n            ')

    _ElementMap.update({
        __marketingCarrierFlightIdentifier.name() : __marketingCarrierFlightIdentifier
    })
    _AttributeMap.update({
        __aircraftIdentification.name() : __aircraftIdentification,
        __majorCarrierIdentifier.name() : __majorCarrierIdentifier
    })
_module_typeBindings.FlightIdentificationType = FlightIdentificationType
Namespace.addCategoryObject('typeBinding', 'FlightIdentificationType', FlightIdentificationType)


# Complex type {http://www.fixm.aero/flight/3.0}SupplementalDataType with content type ELEMENT_ONLY
class SupplementalDataType (pyxb.binding.basis.complexTypeDefinition):
    """
            Contains the supplemental data about the flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplementalDataType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 465, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pilotInCommand uses Python identifier pilotInCommand
    __pilotInCommand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pilotInCommand'), 'pilotInCommand', '__httpwww_fixm_aeroflight3_0_SupplementalDataType_pilotInCommand', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 472, 9), )

    
    pilotInCommand = property(__pilotInCommand.value, __pilotInCommand.set, None, '\n                  .Pilot In Command: The name of the pilot in command of the aircraft. \n               ')

    
    # Attribute fuelEndurance uses Python identifier fuelEndurance
    __fuelEndurance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fuelEndurance'), 'fuelEndurance', '__httpwww_fixm_aeroflight3_0_SupplementalDataType_fuelEndurance', _ImportedBinding__ff.DurationType)
    __fuelEndurance._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 480, 6)
    __fuelEndurance._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 480, 6)
    
    fuelEndurance = property(__fuelEndurance.value, __fuelEndurance.set, None, '\n               .Fuel Endurance: The estimated maximum length of time the aircraft can spend in the \n               cruise phase of flight, determined by the amount of fuel at takeoff. \n            ')

    
    # Attribute personsOnBoard uses Python identifier personsOnBoard
    __personsOnBoard = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'personsOnBoard'), 'personsOnBoard', '__httpwww_fixm_aeroflight3_0_SupplementalDataType_personsOnBoard', _ImportedBinding__fb.CountType)
    __personsOnBoard._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 488, 6)
    __personsOnBoard._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 488, 6)
    
    personsOnBoard = property(__personsOnBoard.value, __personsOnBoard.set, None, '\n               .Number of Persons on Board: The total number of persons (passengers and crew) on \n               board the aircraft. \n            ')

    _ElementMap.update({
        __pilotInCommand.name() : __pilotInCommand
    })
    _AttributeMap.update({
        __fuelEndurance.name() : __fuelEndurance,
        __personsOnBoard.name() : __personsOnBoard
    })
_module_typeBindings.SupplementalDataType = SupplementalDataType
Namespace.addCategoryObject('typeBinding', 'SupplementalDataType', SupplementalDataType)


# Complex type {http://www.fixm.aero/flight/3.0}AbstractRoutePointType with content type ELEMENT_ONLY
class AbstractRoutePointType (pyxb.binding.basis.complexTypeDefinition):
    """
            An abstract route point containing basic shared data between RoutePoint and ExpandedRoutePoint. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractRoutePointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 81, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__httpwww_fixm_aeroflight3_0_AbstractRoutePointType_point', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9), )

    
    point = property(__point.value, __point.set, None, '\n                  .Significant Point: A single point along the flight route. \n               ')

    
    # Attribute airTrafficType uses Python identifier airTrafficType
    __airTrafficType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airTrafficType'), 'airTrafficType', '__httpwww_fixm_aeroflight3_0_AbstractRoutePointType_airTrafficType', _ImportedBinding__fb.AirTrafficTypeType)
    __airTrafficType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 97, 6)
    __airTrafficType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 97, 6)
    
    airTrafficType = property(__airTrafficType.value, __airTrafficType.set, None, '\n               .Route-Change Air Traffic Type: The type of flight value associated with the point. \n               It is associated with the first point on the route and any subsequent point where \n               the type of flight value changes. \n            ')

    
    # Attribute clearanceLimit uses Python identifier clearanceLimit
    __clearanceLimit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'clearanceLimit'), 'clearanceLimit', '__httpwww_fixm_aeroflight3_0_AbstractRoutePointType_clearanceLimit', _module_typeBindings.ClearanceLimitIndicatorType)
    __clearanceLimit._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 106, 6)
    __clearanceLimit._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 106, 6)
    
    clearanceLimit = property(__clearanceLimit.value, __clearanceLimit.set, None, '\n               .Clearance Limit:  The point to which an aircraft is granted an air traffic control \n               clearance. \n            ')

    
    # Attribute delayAtPoint uses Python identifier delayAtPoint
    __delayAtPoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delayAtPoint'), 'delayAtPoint', '__httpwww_fixm_aeroflight3_0_AbstractRoutePointType_delayAtPoint', _ImportedBinding__ff.DurationType)
    __delayAtPoint._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 114, 6)
    __delayAtPoint._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 114, 6)
    
    delayAtPoint = property(__delayAtPoint.value, __delayAtPoint.set, None, '\n               .En Route Delay - Filed: The length of time the flight is expected to be delayed \n               at a specific point en route. \n            ')

    
    # Attribute flightRules uses Python identifier flightRules
    __flightRules = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'flightRules'), 'flightRules', '__httpwww_fixm_aeroflight3_0_AbstractRoutePointType_flightRules', _ImportedBinding__fb.FlightRulesType)
    __flightRules._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 122, 6)
    __flightRules._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 122, 6)
    
    flightRules = property(__flightRules.value, __flightRules.set, None, '\n               .Change Flight Rules: The planned flight rules the aircraft will change to upon reaching \n               the associated Significant Point along its Route. \n               .Route-Change Flight Rules: The planned flight rules the aircraft will change to \n               upon reaching the associated Significant Point along its Route. \n            ')

    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        __airTrafficType.name() : __airTrafficType,
        __clearanceLimit.name() : __clearanceLimit,
        __delayAtPoint.name() : __delayAtPoint,
        __flightRules.name() : __flightRules
    })
_module_typeBindings.AbstractRoutePointType = AbstractRoutePointType
Namespace.addCategoryObject('typeBinding', 'AbstractRoutePointType', AbstractRoutePointType)


# Complex type {http://www.fixm.aero/flight/3.0}EstimatedElapsedTimeType with content type ELEMENT_ONLY
class EstimatedElapsedTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Elapsed Time - Estimated: The estimated amount of time from takeoff to reach a significant 
            point or Flight Information Region (FIR) boundary along the route of flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EstimatedElapsedTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 180, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__httpwww_fixm_aeroflight3_0_EstimatedElapsedTimeType_location', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 188, 9), )

    
    location = property(__location.value, __location.set, None, '\n                  The location associated with estimated elapsed time. It can be a longitude, significant \n                  point of flight information region. \n               ')

    
    # Attribute elapsedTime uses Python identifier elapsedTime
    __elapsedTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'elapsedTime'), 'elapsedTime', '__httpwww_fixm_aeroflight3_0_EstimatedElapsedTimeType_elapsedTime', _ImportedBinding__ff.DurationType, required=True)
    __elapsedTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 197, 6)
    __elapsedTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 197, 6)
    
    elapsedTime = property(__elapsedTime.value, __elapsedTime.set, None, '\n               The estimated amount of elapsed time. \n            ')

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        __elapsedTime.name() : __elapsedTime
    })
_module_typeBindings.EstimatedElapsedTimeType = EstimatedElapsedTimeType
Namespace.addCategoryObject('typeBinding', 'EstimatedElapsedTimeType', EstimatedElapsedTimeType)


# Complex type {http://www.fixm.aero/flight/3.0}RouteSegmentType with content type ELEMENT_ONLY
class RouteSegmentType (pyxb.binding.basis.complexTypeDefinition):
    """
            Route Segment contained within the route. Each segment may contain a route point 
            and an airway. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RouteSegmentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 401, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element routePoint uses Python identifier routePoint
    __routePoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routePoint'), 'routePoint', '__httpwww_fixm_aeroflight3_0_RouteSegmentType_routePoint', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 409, 9), )

    
    routePoint = property(__routePoint.value, __routePoint.set, None, '\n                  Route Segment consists of an optional route point. \n               ')

    
    # Attribute airway uses Python identifier airway
    __airway = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airway'), 'airway', '__httpwww_fixm_aeroflight3_0_RouteSegmentType_airway', _ImportedBinding__ff.AtsRouteType)
    __airway._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 417, 6)
    __airway._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 417, 6)
    
    airway = property(__airway.value, __airway.set, None, '\n               .Airway: The coded designator for a published ATS route or route segment. \n            ')

    _ElementMap.update({
        __routePoint.name() : __routePoint
    })
    _AttributeMap.update({
        __airway.name() : __airway
    })
_module_typeBindings.RouteSegmentType = RouteSegmentType
Namespace.addCategoryObject('typeBinding', 'RouteSegmentType', RouteSegmentType)


# Complex type {http://www.fixm.aero/flight/3.0}Point4DType with content type ELEMENT_ONLY
class Point4DType (_ImportedBinding__ff.GeographicLocationType):
    """
            .4D Point: Identifies the location, altitude and time of a trajectory point. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Point4DType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 114, 3)
    _ElementMap = _ImportedBinding__ff.GeographicLocationType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.GeographicLocationType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.GeographicLocationType
    
    # Element altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altitude'), 'altitude', '__httpwww_fixm_aeroflight3_0_Point4DType_altitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 123, 15), )

    
    altitude = property(__altitude.value, __altitude.set, None, '\n                        Altitude of the 4D point. \n                     ')

    
    # Element pointRange uses Python identifier pointRange
    __pointRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pointRange'), 'pointRange', '__httpwww_fixm_aeroflight3_0_Point4DType_pointRange', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 130, 15), )

    
    pointRange = property(__pointRange.value, __pointRange.set, None, '\n                        block altitude clearances \n    offsets for deviations due to weather\n    assigned speed ranges\n                        .Point Range: Provides a vertical, lateral or temporal range to a 4D point when clearances \n                        are provided in the form of:block altitude clearancesoffsets for deviations due to \n                        weatherassigned speed ranges \n                     ')

    
    # Element pos (pos) inherited from {http://www.fixm.aero/foundation/3.0}GeographicLocationType
    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__httpwww_fixm_aeroflight3_0_Point4DType_time', _ImportedBinding__ff.TimeType)
    __time._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 143, 12)
    __time._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 143, 12)
    
    time = property(__time.value, __time.set, None, '\n                     Time of the 4D point. \n                  ')

    
    # Attribute srsName inherited from {http://www.fixm.aero/foundation/3.0}GeographicLocationType
    _ElementMap.update({
        __altitude.name() : __altitude,
        __pointRange.name() : __pointRange
    })
    _AttributeMap.update({
        __time.name() : __time
    })
_module_typeBindings.Point4DType = Point4DType
Namespace.addCategoryObject('typeBinding', 'Point4DType', Point4DType)


# Complex type {http://www.fixm.aero/flight/3.0}TemporalRangeType with content type EMPTY
class TemporalRangeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Temporal range resulting from assigned speed range. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TemporalRangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 195, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute earliest uses Python identifier earliest
    __earliest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'earliest'), 'earliest', '__httpwww_fixm_aeroflight3_0_TemporalRangeType_earliest', _ImportedBinding__ff.TimeType)
    __earliest._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 201, 6)
    __earliest._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 201, 6)
    
    earliest = property(__earliest.value, __earliest.set, None, '\n               lower bound of the temporal range. \n            ')

    
    # Attribute latest uses Python identifier latest
    __latest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'latest'), 'latest', '__httpwww_fixm_aeroflight3_0_TemporalRangeType_latest', _ImportedBinding__ff.TimeType)
    __latest._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 208, 6)
    __latest._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 208, 6)
    
    latest = property(__latest.value, __latest.set, None, '\n               Upper bound of the temporal range. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __earliest.name() : __earliest,
        __latest.name() : __latest
    })
_module_typeBindings.TemporalRangeType = TemporalRangeType
Namespace.addCategoryObject('typeBinding', 'TemporalRangeType', TemporalRangeType)


# Complex type {http://www.fixm.aero/flight/3.0}TrajectoryChangeType with content type EMPTY
class TrajectoryChangeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups information about features crossed associated with the trajectory point. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrajectoryChangeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 239, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute constrainedAirspace uses Python identifier constrainedAirspace
    __constrainedAirspace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'constrainedAirspace'), 'constrainedAirspace', '__httpwww_fixm_aeroflight3_0_TrajectoryChangeType_constrainedAirspace', _ImportedBinding__fb.ConstrainedAirspaceType)
    __constrainedAirspace._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 245, 6)
    __constrainedAirspace._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 245, 6)
    
    constrainedAirspace = property(__constrainedAirspace.value, __constrainedAirspace.set, None, '\n               .Constrained Airspace Entered: For 4D Points of TCP Type   crossing point into constrained \n               airspace  , the name or identifier of the Constrained Airspace being entered. \n            ')

    
    # Attribute specialActivityAirspace uses Python identifier specialActivityAirspace
    __specialActivityAirspace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'specialActivityAirspace'), 'specialActivityAirspace', '__httpwww_fixm_aeroflight3_0_TrajectoryChangeType_specialActivityAirspace', _ImportedBinding__fb.FreeTextType)
    __specialActivityAirspace._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 253, 6)
    __specialActivityAirspace._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 253, 6)
    
    specialActivityAirspace = property(__specialActivityAirspace.value, __specialActivityAirspace.set, None, '\n               .Special Activity Airspace Entered/Exited: For 4D Points of TCP Type   entry point \n               into special activity airspace   or   exit point from special activity airspace  \n               , the name or identifier of the Special Activity Airspace being entered/exited. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __constrainedAirspace.name() : __constrainedAirspace,
        __specialActivityAirspace.name() : __specialActivityAirspace
    })
_module_typeBindings.TrajectoryChangeType = TrajectoryChangeType
Namespace.addCategoryObject('typeBinding', 'TrajectoryChangeType', TrajectoryChangeType)


# Complex type {http://www.fixm.aero/flight/3.0}AircraftType with content type ELEMENT_ONLY
class AircraftType_ (_ImportedBinding__fb.FeatureType):
    """
            This is a main aircraft class that contains all the information about the aircraft. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 82, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element aircraftType uses Python identifier aircraftType
    __aircraftType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aircraftType'), 'aircraftType', '__httpwww_fixm_aeroflight3_0_AircraftType__aircraftType', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 92, 15), )

    
    aircraftType = property(__aircraftType.value, __aircraftType.set, None, '\n                        .Aircraft Type: The manufacturer and model of the airframe expressed either as an \n                        ICAO-approved designator or a text description. \n                     ')

    
    # Element capabilities uses Python identifier capabilities
    __capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'capabilities'), 'capabilities', '__httpwww_fixm_aeroflight3_0_AircraftType__capabilities', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 100, 15), )

    
    capabilities = property(__capabilities.value, __capabilities.set, None, '\n                        Aircraft contains several types of capabilities. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute aircraftAddress uses Python identifier aircraftAddress
    __aircraftAddress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aircraftAddress'), 'aircraftAddress', '__httpwww_fixm_aeroflight3_0_AircraftType__aircraftAddress', _module_typeBindings.AircraftAddressType)
    __aircraftAddress._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 108, 12)
    __aircraftAddress._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 108, 12)
    
    aircraftAddress = property(__aircraftAddress.value, __aircraftAddress.set, None, '\n                     .Aircraft Address: A code that enables the exchange of text-based messages between \n                     suitably equipped Air Traffic Service (ATS) ground systems and aircraft cockpit displays. \n                     \n                  ')

    
    # Attribute aircraftColours uses Python identifier aircraftColours
    __aircraftColours = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aircraftColours'), 'aircraftColours', '__httpwww_fixm_aeroflight3_0_AircraftType__aircraftColours', _ImportedBinding__fb.FreeTextType)
    __aircraftColours._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 117, 12)
    __aircraftColours._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 117, 12)
    
    aircraftColours = property(__aircraftColours.value, __aircraftColours.set, None, "\n                     .Aircraft Colour and Markings: The colours of the aircraft and a description of the \n                     aircraft's significant markings. \n                  ")

    
    # Attribute aircraftPerformance uses Python identifier aircraftPerformance
    __aircraftPerformance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aircraftPerformance'), 'aircraftPerformance', '__httpwww_fixm_aeroflight3_0_AircraftType__aircraftPerformance', _module_typeBindings.AircraftPerformanceCategoryType)
    __aircraftPerformance._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 125, 12)
    __aircraftPerformance._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 125, 12)
    
    aircraftPerformance = property(__aircraftPerformance.value, __aircraftPerformance.set, None, '\n                     .Aircraft Performance Category: A coded category assigned to the aircraft based on \n                     a speed directly proportional to its stall speed, which functions as a standardized \n                     basis for relating aircraft manoeuvrability to specific instrument approach procedures. \n                     \n                  ')

    
    # Attribute aircraftQuantity uses Python identifier aircraftQuantity
    __aircraftQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aircraftQuantity'), 'aircraftQuantity', '__httpwww_fixm_aeroflight3_0_AircraftType__aircraftQuantity', _ImportedBinding__fb.CountType)
    __aircraftQuantity._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 135, 12)
    __aircraftQuantity._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 135, 12)
    
    aircraftQuantity = property(__aircraftQuantity.value, __aircraftQuantity.set, None, '\n                     .Aircraft Quantity: Number of aircraft flying in a formation in which the aircraft \n                     are governed by one flight plan. \n                  ')

    
    # Attribute engineType uses Python identifier engineType
    __engineType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'engineType'), 'engineType', '__httpwww_fixm_aeroflight3_0_AircraftType__engineType', _module_typeBindings.EngineTypeType)
    __engineType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 143, 12)
    __engineType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 143, 12)
    
    engineType = property(__engineType.value, __engineType.set, None, '\n                     .Engine Type: The category of the aircraft  engine. \n                  ')

    
    # Attribute registration uses Python identifier registration
    __registration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registration'), 'registration', '__httpwww_fixm_aeroflight3_0_AircraftType__registration', _module_typeBindings.AircraftRegistrationType)
    __registration._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 150, 12)
    __registration._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 150, 12)
    
    registration = property(__registration.value, __registration.set, None, '\n                     .Aircraft Registration Mark: A unique, alphanumeric string that identifies a civil \n                     aircraft and consists of the Aircraft Nationality or Common Mark and an additional \n                     alphanumeric string assigned by the state of registry or common mark registering \n                     authority. \n                  ')

    
    # Attribute wakeTurbulence uses Python identifier wakeTurbulence
    __wakeTurbulence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wakeTurbulence'), 'wakeTurbulence', '__httpwww_fixm_aeroflight3_0_AircraftType__wakeTurbulence', _module_typeBindings.WakeTurbulenceCategoryType)
    __wakeTurbulence._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 160, 12)
    __wakeTurbulence._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 160, 12)
    
    wakeTurbulence = property(__wakeTurbulence.value, __wakeTurbulence.set, None, '\n                     .Wake Turbulence Category: ICAO classification of the aircraft wake turbulence, based \n                     on the maximum certified take off mass. \n                  ')

    _ElementMap.update({
        __aircraftType.name() : __aircraftType,
        __capabilities.name() : __capabilities
    })
    _AttributeMap.update({
        __aircraftAddress.name() : __aircraftAddress,
        __aircraftColours.name() : __aircraftColours,
        __aircraftPerformance.name() : __aircraftPerformance,
        __aircraftQuantity.name() : __aircraftQuantity,
        __engineType.name() : __engineType,
        __registration.name() : __registration,
        __wakeTurbulence.name() : __wakeTurbulence
    })
_module_typeBindings.AircraftType_ = AircraftType_
Namespace.addCategoryObject('typeBinding', 'AircraftType', AircraftType_)


# Complex type {http://www.fixm.aero/flight/3.0}CommunicationCapabilitiesType with content type ELEMENT_ONLY
class CommunicationCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Communications Capabilities: The serviceable communications equipment, available 
            on the aircraft at the time of flight, and associated flight crew qualifications 
            that may be used to communicate with ATS units. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommunicationCapabilitiesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 79, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element communicationCode uses Python identifier communicationCode
    __communicationCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'communicationCode'), 'communicationCode', '__httpwww_fixm_aeroflight3_0_CommunicationCapabilitiesType_communicationCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 88, 9), )

    
    communicationCode = property(__communicationCode.value, __communicationCode.set, None, '\n                  Describes the aircraft communication code. \n               ')

    
    # Element dataLinkCode uses Python identifier dataLinkCode
    __dataLinkCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataLinkCode'), 'dataLinkCode', '__httpwww_fixm_aeroflight3_0_CommunicationCapabilitiesType_dataLinkCode', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 98, 9), )

    
    dataLinkCode = property(__dataLinkCode.value, __dataLinkCode.set, None, '\n                  .Data Link Communication Capabilities: The serviceable equipment and capabilities \n                  available on the aircraft at the time of flight that may be used to communicate data \n                  to and from the aircraft. \n               ')

    
    # Attribute otherCommunicationCapabilities uses Python identifier otherCommunicationCapabilities
    __otherCommunicationCapabilities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherCommunicationCapabilities'), 'otherCommunicationCapabilities', '__httpwww_fixm_aeroflight3_0_CommunicationCapabilitiesType_otherCommunicationCapabilities', _ImportedBinding__fb.FreeTextType)
    __otherCommunicationCapabilities._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 111, 6)
    __otherCommunicationCapabilities._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 111, 6)
    
    otherCommunicationCapabilities = property(__otherCommunicationCapabilities.value, __otherCommunicationCapabilities.set, None, '\n               Additional Communication capabilities available on the aircraft. \n            ')

    
    # Attribute otherDataLinkCapabilities uses Python identifier otherDataLinkCapabilities
    __otherDataLinkCapabilities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherDataLinkCapabilities'), 'otherDataLinkCapabilities', '__httpwww_fixm_aeroflight3_0_CommunicationCapabilitiesType_otherDataLinkCapabilities', _ImportedBinding__fb.FreeTextType)
    __otherDataLinkCapabilities._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 118, 6)
    __otherDataLinkCapabilities._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 118, 6)
    
    otherDataLinkCapabilities = property(__otherDataLinkCapabilities.value, __otherDataLinkCapabilities.set, None, '\n               Additional data link capabilities available on the aircraft. \n            ')

    
    # Attribute selectiveCallingCode uses Python identifier selectiveCallingCode
    __selectiveCallingCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'selectiveCallingCode'), 'selectiveCallingCode', '__httpwww_fixm_aeroflight3_0_CommunicationCapabilitiesType_selectiveCallingCode', _module_typeBindings.SelectiveCallingCodeType)
    __selectiveCallingCode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 125, 6)
    __selectiveCallingCode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 125, 6)
    
    selectiveCallingCode = property(__selectiveCallingCode.value, __selectiveCallingCode.set, None, '\n               .Selective Calling Code: A code that consists of two 2-letter pairs and acts as a \n               paging system for an ATS unit to establish voice communications with the pilot of \n               an aircraft. \n            ')

    _ElementMap.update({
        __communicationCode.name() : __communicationCode,
        __dataLinkCode.name() : __dataLinkCode
    })
    _AttributeMap.update({
        __otherCommunicationCapabilities.name() : __otherCommunicationCapabilities,
        __otherDataLinkCapabilities.name() : __otherDataLinkCapabilities,
        __selectiveCallingCode.name() : __selectiveCallingCode
    })
_module_typeBindings.CommunicationCapabilitiesType = CommunicationCapabilitiesType
Namespace.addCategoryObject('typeBinding', 'CommunicationCapabilitiesType', CommunicationCapabilitiesType)


# Complex type {http://www.fixm.aero/flight/3.0}DangerousGoodsType with content type ELEMENT_ONLY
class DangerousGoodsType (_ImportedBinding__fb.FeatureType):
    """
            .Shipper's Declaration For Dangerous Goods Summary: The section of the IATA Shipper's 
            Declaration For Dangerous Goods required at the end portion of the SDDG for a shipment. 
            
            .Shipper's Declaration For Dangerous Goods Header: The part of the IATA Shipper's 
            Declaration For Dangerous Goods that contains the basic header information on who 
            is sending and receiving this shipment. 
            .IATA Shipper's Declaration For Dangerous Goods: This is the outermost grouping element 
            for the information required for the shipment of dangerous goods. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 149, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element airWayBill uses Python identifier airWayBill
    __airWayBill = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airWayBill'), 'airWayBill', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_airWayBill', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 165, 15), )

    
    airWayBill = property(__airWayBill.value, __airWayBill.set, None, '\n                        .Air Waybill Number: The number referencing the air waybill. \n                     ')

    
    # Element handlingInformation uses Python identifier handlingInformation
    __handlingInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'handlingInformation'), 'handlingInformation', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_handlingInformation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 172, 15), )

    
    handlingInformation = property(__handlingInformation.value, __handlingInformation.set, None, "\n                        .Additional Handling Information: Additional information related to the handling \n                        of dangerous goods, as identified on the Shipper's Declaration for Dangerous Goods. \n                        \n                     ")

    
    # Element packageGroup uses Python identifier packageGroup
    __packageGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'packageGroup'), 'packageGroup', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_packageGroup', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 181, 15), )

    
    packageGroup = property(__packageGroup.value, __packageGroup.set, None, '\n                        .Packing Group: A code that indicates the relative degree of danger presented by \n                        various articles and substances within a Class or Division. \n                     ')

    
    # Element shippingInformation uses Python identifier shippingInformation
    __shippingInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shippingInformation'), 'shippingInformation', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_shippingInformation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 189, 15), )

    
    shippingInformation = property(__shippingInformation.value, __shippingInformation.set, None, "\n                        IATA Shipper's Declaration for Dangerous Goods. \n                     ")

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute aircraftLimitation uses Python identifier aircraftLimitation
    __aircraftLimitation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aircraftLimitation'), 'aircraftLimitation', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_aircraftLimitation', _module_typeBindings.AircraftDangerousGoodsLimitationType)
    __aircraftLimitation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 197, 12)
    __aircraftLimitation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 197, 12)
    
    aircraftLimitation = property(__aircraftLimitation.value, __aircraftLimitation.set, None, '\n                     .Aircraft Dangerous Goods Limitation: Describes whether the shipment is packed to \n                     comply with the limitations prescribed for passenger and cargo aircraft or the limitations \n                     for cargo aircraft only. \n                  ')

    
    # Attribute guidebookNumber uses Python identifier guidebookNumber
    __guidebookNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'guidebookNumber'), 'guidebookNumber', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_guidebookNumber', _module_typeBindings.STD_ANON_8)
    __guidebookNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 206, 12)
    __guidebookNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 206, 12)
    
    guidebookNumber = property(__guidebookNumber.value, __guidebookNumber.set, None, '\n                     .Emergency Response Guidebook Number: A reference to a set of instructions to handle \n                     a specific dangerous goods situation. \n                  ')

    
    # Attribute onboardLocation uses Python identifier onboardLocation
    __onboardLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'onboardLocation'), 'onboardLocation', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_onboardLocation', _ImportedBinding__fb.FreeTextType)
    __onboardLocation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 219, 12)
    __onboardLocation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 219, 12)
    
    onboardLocation = property(__onboardLocation.value, __onboardLocation.set, None, '\n                     .On Board Dangerous Goods Location: The location of a dangerous goods shipment inside \n                     the airframe. \n                  ')

    
    # Attribute shipment uses Python identifier shipment
    __shipment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shipment'), 'shipment', '__httpwww_fixm_aeroflight3_0_DangerousGoodsType_shipment', _module_typeBindings.ShipmentTypeType)
    __shipment._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 227, 12)
    __shipment._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 227, 12)
    
    shipment = property(__shipment.value, __shipment.set, None, '\n                     .Shipment Type: An indicator used for dangerous cargo of whether the package is radioactive \n                     or not. \n                  ')

    _ElementMap.update({
        __airWayBill.name() : __airWayBill,
        __handlingInformation.name() : __handlingInformation,
        __packageGroup.name() : __packageGroup,
        __shippingInformation.name() : __shippingInformation
    })
    _AttributeMap.update({
        __aircraftLimitation.name() : __aircraftLimitation,
        __guidebookNumber.name() : __guidebookNumber,
        __onboardLocation.name() : __onboardLocation,
        __shipment.name() : __shipment
    })
_module_typeBindings.DangerousGoodsType = DangerousGoodsType
Namespace.addCategoryObject('typeBinding', 'DangerousGoodsType', DangerousGoodsType)


# Complex type {http://www.fixm.aero/flight/3.0}StructuredPostalAddressType with content type ELEMENT_ONLY
class StructuredPostalAddressType (_ImportedBinding__ff.ContactInformationType):
    """
            .Country Name: The name of a country. 
            .Region Name: The name of the region within a country specific to this address. 
            .Postal Structured Address: The XML Grouping Element that contains the parts of a 
            Postal Address broken into its component parts (Structured). 
            .Post Office Box: The Post Office (PO) Box number portion of a structured postal 
            address. 
            .Department: Contains the Department Name portion of the Address. 
            .Country Code: A code that indicates a country. 
            .Street: The building number and Street Name portion of the Address. 
            .City Name: The name of the city the package is being shipped to. 
            .ZIP or Postal Code: The ZIP/Postal Code corresponding to the street address. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StructuredPostalAddressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 437, 3)
    _ElementMap = _ImportedBinding__ff.ContactInformationType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.ContactInformationType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.ContactInformationType
    
    # Element address (address) inherited from {http://www.fixm.aero/foundation/3.0}ContactInformationType
    
    # Element onlineContact (onlineContact) inherited from {http://www.fixm.aero/foundation/3.0}ContactInformationType
    
    # Element phoneFax (phoneFax) inherited from {http://www.fixm.aero/foundation/3.0}ContactInformationType
    
    # Attribute name inherited from {http://www.fixm.aero/foundation/3.0}ContactInformationType
    
    # Attribute title inherited from {http://www.fixm.aero/foundation/3.0}ContactInformationType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StructuredPostalAddressType = StructuredPostalAddressType
Namespace.addCategoryObject('typeBinding', 'StructuredPostalAddressType', StructuredPostalAddressType)


# Complex type {http://www.fixm.aero/flight/3.0}AllPackedInOneType with content type EMPTY
class AllPackedInOneType (pyxb.binding.basis.complexTypeDefinition):
    """
            .All Packed In One: A statement identifying the dangerous goods listed are all contained 
            within the same outer packaging. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllPackedInOneType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 83, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute numberOfPackages uses Python identifier numberOfPackages
    __numberOfPackages = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numberOfPackages'), 'numberOfPackages', '__httpwww_fixm_aeroflight3_0_AllPackedInOneType_numberOfPackages', _ImportedBinding__fb.CountType)
    __numberOfPackages._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 90, 6)
    __numberOfPackages._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 90, 6)
    
    numberOfPackages = property(__numberOfPackages.value, __numberOfPackages.set, None, '\n               The number of packages in the same outer packaging. \n            ')

    
    # Attribute qValue uses Python identifier qValue
    __qValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'qValue'), 'qValue', '__httpwww_fixm_aeroflight3_0_AllPackedInOneType_qValue', _module_typeBindings.STD_ANON_10)
    __qValue._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 97, 6)
    __qValue._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 97, 6)
    
    qValue = property(__qValue.value, __qValue.set, None, '\n               .Q Value: The amount of energy released in a reaction. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __numberOfPackages.name() : __numberOfPackages,
        __qValue.name() : __qValue
    })
_module_typeBindings.AllPackedInOneType = AllPackedInOneType
Namespace.addCategoryObject('typeBinding', 'AllPackedInOneType', AllPackedInOneType)


# Complex type {http://www.fixm.aero/flight/3.0}DangerousGoodsPackageType with content type ELEMENT_ONLY
class DangerousGoodsPackageType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Dangerous Goods List of Package Detail: The part of the IATA Shipper's Declaration 
            For Dangerous Goods that contains the Package Details for the shipment. 
            .Shipper's Declaration For Dangerous Goods Packaging Detail: The part of the IATA 
            Shipper's Declaration For Dangerous Goods that contains the packaging details for 
            this shipment. 
            .Shipper's Declaration For Dangerous Goods Line Item Details: The part of the IATA 
            Shipper's Declaration For Dangerous Goods contains the line items details for this 
            shipment. 
            .Dangerous Goods List of Line Item Detail: The part of the IATA Shipper's Declaration 
            For Dangerous Goods that contains the Line Item information for the shipment. 
            .Dangerous Goods List of Overpack Detail: The part of the IATA Shipper's Declaration 
            For Dangerous Goods that contains the Overpack Detail for the shipment. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsPackageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 160, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element allPackedInOne uses Python identifier allPackedInOne
    __allPackedInOne = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'allPackedInOne'), 'allPackedInOne', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_allPackedInOne', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 178, 9), )

    
    allPackedInOne = property(__allPackedInOne.value, __allPackedInOne.set, None, '\n                  .All Packed In One: A statement identifying the dangerous goods listed are all contained \n                  within the same outer packaging. \n               ')

    
    # Element hazardClass uses Python identifier hazardClass
    __hazardClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazardClass'), 'hazardClass', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_hazardClass', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 186, 9), )

    
    hazardClass = property(__hazardClass.value, __hazardClass.set, None, '\n                  .Hazard Class and Division: A number assigned to a dangerous good that represents \n                  a classification (Class) according to the most dominant hazard it represents, potentially \n                  followed by a number representing a subdivision (Division) within the Class. \n               ')

    
    # Element packageDimensions uses Python identifier packageDimensions
    __packageDimensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'packageDimensions'), 'packageDimensions', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_packageDimensions', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 195, 9), )

    
    packageDimensions = property(__packageDimensions.value, __packageDimensions.set, None, "\n                  .Package Width: The depth component of the package's volumetric dimensions. \n                  .Package Length: The lateral component of the package's volumetric dimensions. \n                  .Package Height: The vertical component of the package's volumetric dimensions. \n               ")

    
    # Element radioactiveMaterials uses Python identifier radioactiveMaterials
    __radioactiveMaterials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radioactiveMaterials'), 'radioactiveMaterials', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_radioactiveMaterials', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 204, 9), )

    
    radioactiveMaterials = property(__radioactiveMaterials.value, __radioactiveMaterials.set, None, '\n                  .Radioactive Materials: The XML grouping element for goods that contain radioactive \n                  materials. \n               ')

    
    # Element shipmentDimensions uses Python identifier shipmentDimensions
    __shipmentDimensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shipmentDimensions'), 'shipmentDimensions', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_shipmentDimensions', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 212, 9), )

    
    shipmentDimensions = property(__shipmentDimensions.value, __shipmentDimensions.set, None, '\n                  Weight and volume (not height, width, and depth): \n               ')

    
    # Element subsidiaryHazardClass uses Python identifier subsidiaryHazardClass
    __subsidiaryHazardClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subsidiaryHazardClass'), 'subsidiaryHazardClass', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_subsidiaryHazardClass', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 219, 9), )

    
    subsidiaryHazardClass = property(__subsidiaryHazardClass.value, __subsidiaryHazardClass.set, None, '\n                  .Subsidiary Hazard Class and Division: An identifier of any subsidiary hazard class(es)/division(s) \n                  in addition to the primary hazard class and division. \n               ')

    
    # Element temperatures uses Python identifier temperatures
    __temperatures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'temperatures'), 'temperatures', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_temperatures', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 227, 9), )

    
    temperatures = property(__temperatures.value, __temperatures.set, None, '\n                  Control Temperature: \n                   \n                  Emergency Temperature: \n                   \n                  Flashpoint Temperature: \n                  The lowest temperature at which it can vaporize to form an ignitable mixture in air. \n                  \n               ')

    
    # Attribute compatibilityGroup uses Python identifier compatibilityGroup
    __compatibilityGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'compatibilityGroup'), 'compatibilityGroup', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_compatibilityGroup', _module_typeBindings.CompatibilityGroupType)
    __compatibilityGroup._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 241, 6)
    __compatibilityGroup._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 241, 6)
    
    compatibilityGroup = property(__compatibilityGroup.value, __compatibilityGroup.set, None, '\n               .Compatibility Group: When shipping dangerous goods, the reference to the group which \n               identifies the kind of substances and articles deemed to be compatible. \n            ')

    
    # Attribute dangerousGoodsLimitation uses Python identifier dangerousGoodsLimitation
    __dangerousGoodsLimitation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dangerousGoodsLimitation'), 'dangerousGoodsLimitation', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_dangerousGoodsLimitation', _module_typeBindings.AircraftDangerousGoodsLimitationType)
    __dangerousGoodsLimitation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 249, 6)
    __dangerousGoodsLimitation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 249, 6)
    
    dangerousGoodsLimitation = property(__dangerousGoodsLimitation.value, __dangerousGoodsLimitation.set, None, '\n               .Aircraft Dangerous Goods Limitation: Describes whether the shipment is packed to \n               comply with the limitations prescribed for passenger and cargo aircraft or the limitations \n               for cargo aircraft only. \n            ')

    
    # Attribute dangerousGoodsQuantity uses Python identifier dangerousGoodsQuantity
    __dangerousGoodsQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dangerousGoodsQuantity'), 'dangerousGoodsQuantity', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_dangerousGoodsQuantity', _ImportedBinding__fb.CountType)
    __dangerousGoodsQuantity._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 258, 6)
    __dangerousGoodsQuantity._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 258, 6)
    
    dangerousGoodsQuantity = property(__dangerousGoodsQuantity.value, __dangerousGoodsQuantity.set, None, '\n               .Dangerous Goods Quantity: The total number of dangerous good packages of the same \n               type and content. \n            ')

    
    # Attribute marinePollutantIndicator uses Python identifier marinePollutantIndicator
    __marinePollutantIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'marinePollutantIndicator'), 'marinePollutantIndicator', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_marinePollutantIndicator', _module_typeBindings.MarinePollutantIndicatorType)
    __marinePollutantIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 266, 6)
    __marinePollutantIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 266, 6)
    
    marinePollutantIndicator = property(__marinePollutantIndicator.value, __marinePollutantIndicator.set, None, '\n               .Marine Pollutant Indicator: An indicator if the transported dangerous goods have \n               marine pollutant content. \n            ')

    
    # Attribute overpackIndicator uses Python identifier overpackIndicator
    __overpackIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'overpackIndicator'), 'overpackIndicator', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_overpackIndicator', _module_typeBindings.OverpackIndicatorType)
    __overpackIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 274, 6)
    __overpackIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 274, 6)
    
    overpackIndicator = property(__overpackIndicator.value, __overpackIndicator.set, None, '\n               .Overpack Indicator: An indicator that individual packages are assembled into a single \n               unit for handling. \n            ')

    
    # Attribute packingGroup uses Python identifier packingGroup
    __packingGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'packingGroup'), 'packingGroup', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_packingGroup', _module_typeBindings.PackingGroupType)
    __packingGroup._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 282, 6)
    __packingGroup._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 282, 6)
    
    packingGroup = property(__packingGroup.value, __packingGroup.set, None, '\n               .Packing Group: A code that indicates the relative degree of danger presented by \n               various articles and substances within a Class or Division. \n            ')

    
    # Attribute packingInstructionNumber uses Python identifier packingInstructionNumber
    __packingInstructionNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'packingInstructionNumber'), 'packingInstructionNumber', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_packingInstructionNumber', _module_typeBindings.STD_ANON_11)
    __packingInstructionNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 290, 6)
    __packingInstructionNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 290, 6)
    
    packingInstructionNumber = property(__packingInstructionNumber.value, __packingInstructionNumber.set, None, '\n               .Packing Instruction Number: A number that corresponds to packing instructions required \n               by U.S. and international regulations. \n            ')

    
    # Attribute productName uses Python identifier productName
    __productName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'productName'), 'productName', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_productName', _ImportedBinding__fb.FreeTextType)
    __productName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 303, 6)
    __productName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 303, 6)
    
    productName = property(__productName.value, __productName.set, None, '\n               .Product Name: The commonly used trade name associated with a dangerous good. \n            ')

    
    # Attribute properShippingName uses Python identifier properShippingName
    __properShippingName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'properShippingName'), 'properShippingName', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_properShippingName', _ImportedBinding__fb.FreeTextType)
    __properShippingName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 310, 6)
    __properShippingName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 310, 6)
    
    properShippingName = property(__properShippingName.value, __properShippingName.set, None, '\n               .Proper Shipping Name: The name used to describe a particular article or substance \n               in all shipping documents and notifications and, where appropriate, on packaging, \n               as shown in the UN Model Regulations Dangerous Goods List. \n            ')

    
    # Attribute reportableQuantity uses Python identifier reportableQuantity
    __reportableQuantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reportableQuantity'), 'reportableQuantity', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_reportableQuantity', _ImportedBinding__fb.CountType)
    __reportableQuantity._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 319, 6)
    __reportableQuantity._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 319, 6)
    
    reportableQuantity = property(__reportableQuantity.value, __reportableQuantity.set, None, '\n               .Reportable Quantity: The minimum amount of hazardous substance released into the \n               environment before the Environmental Protection Agency (EPA) requires notification \n               of the release to the National Response Centre. \n            ')

    
    # Attribute shipmentType uses Python identifier shipmentType
    __shipmentType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shipmentType'), 'shipmentType', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_shipmentType', _module_typeBindings.ShipmentTypeType)
    __shipmentType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 328, 6)
    __shipmentType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 328, 6)
    
    shipmentType = property(__shipmentType.value, __shipmentType.set, None, '\n               .Shipment Type: An indicator used for dangerous cargo of whether the package is radioactive \n               or not. \n            ')

    
    # Attribute supplementaryInformation uses Python identifier supplementaryInformation
    __supplementaryInformation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'supplementaryInformation'), 'supplementaryInformation', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_supplementaryInformation', _ImportedBinding__fb.FreeTextType)
    __supplementaryInformation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 336, 6)
    __supplementaryInformation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 336, 6)
    
    supplementaryInformation = property(__supplementaryInformation.value, __supplementaryInformation.set, None, '\n               .Supplementary Information: Additional information that may be added to the proper \n               shipping name to more fully describe the goods or to identify a particular condition. \n               \n            ')

    
    # Attribute technicalName uses Python identifier technicalName
    __technicalName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'technicalName'), 'technicalName', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_technicalName', _ImportedBinding__fb.FreeTextType)
    __technicalName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 345, 6)
    __technicalName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 345, 6)
    
    technicalName = property(__technicalName.value, __technicalName.set, None, '\n               .Technical Name: The additional chemical name(s) required for some proper shipping \n               names for dangerous goods. \n            ')

    
    # Attribute typeOfPackaging uses Python identifier typeOfPackaging
    __typeOfPackaging = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'typeOfPackaging'), 'typeOfPackaging', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_typeOfPackaging', _ImportedBinding__fb.FreeTextType)
    __typeOfPackaging._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 353, 6)
    __typeOfPackaging._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 353, 6)
    
    typeOfPackaging = property(__typeOfPackaging.value, __typeOfPackaging.set, None, '\n               .Dangerous Goods Type of Packaging: The material or container in which the dangerous \n               good is packaged. \n            ')

    
    # Attribute unNumber uses Python identifier unNumber
    __unNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unNumber'), 'unNumber', '__httpwww_fixm_aeroflight3_0_DangerousGoodsPackageType_unNumber', _module_typeBindings.STD_ANON_12)
    __unNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 361, 6)
    __unNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 361, 6)
    
    unNumber = property(__unNumber.value, __unNumber.set, None, '\n               .United Nations Number: A four-digit identification number assigned by the United \n               Nations Committee of Experts on the Transport of Dangerous Goods to identify a substance \n               or a particular group of substances considered dangerous goods. \n            ')

    _ElementMap.update({
        __allPackedInOne.name() : __allPackedInOne,
        __hazardClass.name() : __hazardClass,
        __packageDimensions.name() : __packageDimensions,
        __radioactiveMaterials.name() : __radioactiveMaterials,
        __shipmentDimensions.name() : __shipmentDimensions,
        __subsidiaryHazardClass.name() : __subsidiaryHazardClass,
        __temperatures.name() : __temperatures
    })
    _AttributeMap.update({
        __compatibilityGroup.name() : __compatibilityGroup,
        __dangerousGoodsLimitation.name() : __dangerousGoodsLimitation,
        __dangerousGoodsQuantity.name() : __dangerousGoodsQuantity,
        __marinePollutantIndicator.name() : __marinePollutantIndicator,
        __overpackIndicator.name() : __overpackIndicator,
        __packingGroup.name() : __packingGroup,
        __packingInstructionNumber.name() : __packingInstructionNumber,
        __productName.name() : __productName,
        __properShippingName.name() : __properShippingName,
        __reportableQuantity.name() : __reportableQuantity,
        __shipmentType.name() : __shipmentType,
        __supplementaryInformation.name() : __supplementaryInformation,
        __technicalName.name() : __technicalName,
        __typeOfPackaging.name() : __typeOfPackaging,
        __unNumber.name() : __unNumber
    })
_module_typeBindings.DangerousGoodsPackageType = DangerousGoodsPackageType
Namespace.addCategoryObject('typeBinding', 'DangerousGoodsPackageType', DangerousGoodsPackageType)


# Complex type {http://www.fixm.aero/flight/3.0}HazardClassType with content type SIMPLE
class HazardClassType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Hazard Class and Division: A number assigned to a dangerous good that represents 
            a classification (Class) according to the most dominant hazard it represents, potentially 
            followed by a number representing a subdivision (Division) within the Class. 
            .Subsidiary Hazard Class and Division: An identifier of any subsidiary hazard class(es)/division(s) 
            in addition to the primary hazard class and division. 
         """
    _TypeDefinition = RestrictedHazardClassType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HazardClassType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 418, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RestrictedHazardClassType
    
    # Attribute hazardDivision uses Python identifier hazardDivision
    __hazardDivision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hazardDivision'), 'hazardDivision', '__httpwww_fixm_aeroflight3_0_HazardClassType_hazardDivision', _module_typeBindings.STD_ANON_13)
    __hazardDivision._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 430, 12)
    __hazardDivision._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 430, 12)
    
    hazardDivision = property(__hazardDivision.value, __hazardDivision.set, None, '\n                     A number representing a subdivision (Division) within the Class. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __hazardDivision.name() : __hazardDivision
    })
_module_typeBindings.HazardClassType = HazardClassType
Namespace.addCategoryObject('typeBinding', 'HazardClassType', HazardClassType)


# Complex type {http://www.fixm.aero/flight/3.0}RadioactiveMaterialType with content type ELEMENT_ONLY
class RadioactiveMaterialType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Radioactive Materials: The XML grouping element for goods that contain radioactive 
            materials. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadioactiveMaterialType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 122, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element radionuclide uses Python identifier radionuclide
    __radionuclide = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radionuclide'), 'radionuclide', '__httpwww_fixm_aeroflight3_0_RadioactiveMaterialType_radionuclide', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 130, 9), )

    
    radionuclide = property(__radionuclide.value, __radionuclide.set, None, '\n                  .Radionuclide: The XML sub-grouping element for Radioactive Materials. \n               ')

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__httpwww_fixm_aeroflight3_0_RadioactiveMaterialType_category', _module_typeBindings.RadioactiveMaterialCategoryType)
    __category._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 138, 6)
    __category._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 138, 6)
    
    category = property(__category.value, __category.set, None, '\n               .Radioactive Material Category: A category used for radioactive materials in a package, \n               overpack or freight container, based on their maximum radiation level. \n            ')

    
    # Attribute criticalitySafetyIndex uses Python identifier criticalitySafetyIndex
    __criticalitySafetyIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'criticalitySafetyIndex'), 'criticalitySafetyIndex', '__httpwww_fixm_aeroflight3_0_RadioactiveMaterialType_criticalitySafetyIndex', _module_typeBindings.STD_ANON_14)
    __criticalitySafetyIndex._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 146, 6)
    __criticalitySafetyIndex._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 146, 6)
    
    criticalitySafetyIndex = property(__criticalitySafetyIndex.value, __criticalitySafetyIndex.set, None, '\n               .Criticality Safety Index: The dimensionless number (rounded up to the next tenth) \n               assigned to and placed on the label of a fissile material package to designate the \n               degree of control of accumulation of packages containing fissile material during \n               transportation. \n            ')

    
    # Attribute fissileExceptedIndicator uses Python identifier fissileExceptedIndicator
    __fissileExceptedIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fissileExceptedIndicator'), 'fissileExceptedIndicator', '__httpwww_fixm_aeroflight3_0_RadioactiveMaterialType_fissileExceptedIndicator', _module_typeBindings.FissileExceptedType)
    __fissileExceptedIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 162, 6)
    __fissileExceptedIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 162, 6)
    
    fissileExceptedIndicator = property(__fissileExceptedIndicator.value, __fissileExceptedIndicator.set, None, '\n               .Fissile Excepted Indicator: An indicator of whether the restrictions for fissile \n               material are excepted for a particular package. \n            ')

    
    # Attribute transportIndex uses Python identifier transportIndex
    __transportIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'transportIndex'), 'transportIndex', '__httpwww_fixm_aeroflight3_0_RadioactiveMaterialType_transportIndex', _module_typeBindings.STD_ANON_15)
    __transportIndex._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 170, 6)
    __transportIndex._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 170, 6)
    
    transportIndex = property(__transportIndex.value, __transportIndex.set, None, '\n               .Transport Index: A figure representing the radiation level measured at one meter \n               from the package. \n            ')

    _ElementMap.update({
        __radionuclide.name() : __radionuclide
    })
    _AttributeMap.update({
        __category.name() : __category,
        __criticalitySafetyIndex.name() : __criticalitySafetyIndex,
        __fissileExceptedIndicator.name() : __fissileExceptedIndicator,
        __transportIndex.name() : __transportIndex
    })
_module_typeBindings.RadioactiveMaterialType = RadioactiveMaterialType
Namespace.addCategoryObject('typeBinding', 'RadioactiveMaterialType', RadioactiveMaterialType)


# Complex type {http://www.fixm.aero/flight/3.0}RadionuclideType with content type ELEMENT_ONLY
class RadionuclideType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Radionuclide: The XML sub-grouping element for Radioactive Materials. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadionuclideType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 266, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element activity uses Python identifier activity
    __activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'activity'), 'activity', '__httpwww_fixm_aeroflight3_0_RadionuclideType_activity', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 273, 9), )

    
    activity = property(__activity.value, __activity.set, None, '\n                  .Activity: The measure of the rate of decay, or activity, of a radioactive material. \n                  \n               ')

    
    # Attribute lowDispersibleMaterialIndicator uses Python identifier lowDispersibleMaterialIndicator
    __lowDispersibleMaterialIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lowDispersibleMaterialIndicator'), 'lowDispersibleMaterialIndicator', '__httpwww_fixm_aeroflight3_0_RadionuclideType_lowDispersibleMaterialIndicator', _module_typeBindings.MaterialDispersabilityType)
    __lowDispersibleMaterialIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 282, 6)
    __lowDispersibleMaterialIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 282, 6)
    
    lowDispersibleMaterialIndicator = property(__lowDispersibleMaterialIndicator.value, __lowDispersibleMaterialIndicator.set, None, '\n               .Low Dispersible Material Indicator: An indicator the dangerous good is a low dispersible \n               radioactive material, a solid radioactive material or a solid radioactive material \n               in a sealed capsule, which has limited dispersibility and is not in powder form. \n               \n            ')

    
    # Attribute physicalChemicalForm uses Python identifier physicalChemicalForm
    __physicalChemicalForm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'physicalChemicalForm'), 'physicalChemicalForm', '__httpwww_fixm_aeroflight3_0_RadionuclideType_physicalChemicalForm', _ImportedBinding__fb.FreeTextType)
    __physicalChemicalForm._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 292, 6)
    __physicalChemicalForm._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 292, 6)
    
    physicalChemicalForm = property(__physicalChemicalForm.value, __physicalChemicalForm.set, None, '\n               .Physical and Chemical Form: A description of the physical and chemical form when \n               the dangerous goods are radioactive. \n            ')

    
    # Attribute radionuclideId uses Python identifier radionuclideId
    __radionuclideId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radionuclideId'), 'radionuclideId', '__httpwww_fixm_aeroflight3_0_RadionuclideType_radionuclideId', _module_typeBindings.STD_ANON_16)
    __radionuclideId._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 300, 6)
    __radionuclideId._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 300, 6)
    
    radionuclideId = property(__radionuclideId.value, __radionuclideId.set, None, '\n               .Radionuclide ID: Identification number of each radionuclide or for mixtures of radionuclides. \n               \n            ')

    
    # Attribute radionuclideName uses Python identifier radionuclideName
    __radionuclideName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radionuclideName'), 'radionuclideName', '__httpwww_fixm_aeroflight3_0_RadionuclideType_radionuclideName', _ImportedBinding__fb.FreeTextType)
    __radionuclideName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 313, 6)
    __radionuclideName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 313, 6)
    
    radionuclideName = property(__radionuclideName.value, __radionuclideName.set, None, '\n               .Radionuclide Name: The name or symbol of each radionuclide or for mixtures of radionuclides, \n               an appropriate general description, or a list of the most restrictive nuclides. \n            ')

    
    # Attribute specialFormIndicator uses Python identifier specialFormIndicator
    __specialFormIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'specialFormIndicator'), 'specialFormIndicator', '__httpwww_fixm_aeroflight3_0_RadionuclideType_specialFormIndicator', _module_typeBindings.SpecialFormType)
    __specialFormIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 321, 6)
    __specialFormIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 321, 6)
    
    specialFormIndicator = property(__specialFormIndicator.value, __specialFormIndicator.set, None, "\n               .Special Form Indicator: A notation that the material is 'special form' and cannot \n               produce radioactive contamination. \n            ")

    _ElementMap.update({
        __activity.name() : __activity
    })
    _AttributeMap.update({
        __lowDispersibleMaterialIndicator.name() : __lowDispersibleMaterialIndicator,
        __physicalChemicalForm.name() : __physicalChemicalForm,
        __radionuclideId.name() : __radionuclideId,
        __radionuclideName.name() : __radionuclideName,
        __specialFormIndicator.name() : __specialFormIndicator
    })
_module_typeBindings.RadionuclideType = RadionuclideType
Namespace.addCategoryObject('typeBinding', 'RadionuclideType', RadionuclideType)


# Complex type {http://www.fixm.aero/flight/3.0}AltitudeInTransitionType with content type SIMPLE
class AltitudeInTransitionType (_ImportedBinding__ff.AltitudeType):
    """
            .Boundary Crossing Level - Transition/Coordinated: An altitude (flight level) at 
            or above/below which an aircraft will cross the associated boundary point. 
            .Boundary Crossing Level - Transition - Proposed: The proposed altitude (flight level) 
            at or above/below which an aircraft will cross the associated boundary point, as 
            requested by the accepting controller from the transferring controller. 
            .Boundary Crossing Level - Transition: An altitude (flight level) at or above/below 
            which (specified in Boundary Crossing Condition) an aircraft will cross the associated 
            boundary point. 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltitudeInTransitionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 83, 3)
    _ElementMap = _ImportedBinding__ff.AltitudeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AltitudeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AltitudeType
    
    # Attribute crossingCondition uses Python identifier crossingCondition
    __crossingCondition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crossingCondition'), 'crossingCondition', '__httpwww_fixm_aeroflight3_0_AltitudeInTransitionType_crossingCondition', _module_typeBindings.BoundaryCrossingConditionType)
    __crossingCondition._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 98, 12)
    __crossingCondition._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 98, 12)
    
    crossingCondition = property(__crossingCondition.value, __crossingCondition.set, None, '\n                     .Boundary Crossing Level - Transition/Coordinated: An altitude (flight level) at \n                     or above/below which an aircraft will cross the associated boundary point. \n                     .Boundary Crossing Level - Transition - Proposed: The proposed altitude (flight level) \n                     at or above/below which an aircraft will cross the associated boundary point, as \n                     requested by the accepting controller from the transferring controller. \n                  ')

    
    # Attribute ref inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __crossingCondition.name() : __crossingCondition
    })
_module_typeBindings.AltitudeInTransitionType = AltitudeInTransitionType
Namespace.addCategoryObject('typeBinding', 'AltitudeInTransitionType', AltitudeInTransitionType)


# Complex type {http://www.fixm.aero/flight/3.0}UnitBoundaryType with content type ELEMENT_ONLY
class UnitBoundaryType (_ImportedBinding__fb.AtcUnitReferenceType):
    """
            Represents an Unit boundary that will be traversed En Route. 
            .Unit Boundary: Identifies the unit whose boundary the flight is expected to traverse, 
            based on the planned route of flight and altitude. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitBoundaryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 273, 3)
    _ElementMap = _ImportedBinding__fb.AtcUnitReferenceType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.AtcUnitReferenceType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.AtcUnitReferenceType
    
    # Element boundaryCrossingCoordinated uses Python identifier boundaryCrossingCoordinated
    __boundaryCrossingCoordinated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundaryCrossingCoordinated'), 'boundaryCrossingCoordinated', '__httpwww_fixm_aeroflight3_0_UnitBoundaryType_boundaryCrossingCoordinated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 284, 15), )

    
    boundaryCrossingCoordinated = property(__boundaryCrossingCoordinated.value, __boundaryCrossingCoordinated.set, None, '\n                        Coordinated boundary crossing information with associated details including altitude, \n                        crossing point and crossing time. \n                     ')

    
    # Element boundaryCrossingProposed uses Python identifier boundaryCrossingProposed
    __boundaryCrossingProposed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundaryCrossingProposed'), 'boundaryCrossingProposed', '__httpwww_fixm_aeroflight3_0_UnitBoundaryType_boundaryCrossingProposed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 292, 15), )

    
    boundaryCrossingProposed = property(__boundaryCrossingProposed.value, __boundaryCrossingProposed.set, None, '\n                        A proposed boundary crossing information with associated details including altitude, \n                        crossing point and crossing time. \n                     ')

    
    # Element downstreamUnit uses Python identifier downstreamUnit
    __downstreamUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'downstreamUnit'), 'downstreamUnit', '__httpwww_fixm_aeroflight3_0_UnitBoundaryType_downstreamUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 300, 15), )

    
    downstreamUnit = property(__downstreamUnit.value, __downstreamUnit.set, None, '\n                        .Delegated Unit Indicator: Indicates whether or not the controlling unit has been \n                        delegated authority for the flight based on agreement with the unit in whose Area \n                        of Responsibility (AOR) the flight is currently located. \n                        .Downstream Unit: The next unit the flight will be controlled by based on the planned \n                        route of flight, altitude, and accepted constraints. \n                     ')

    
    # Element handoff uses Python identifier handoff
    __handoff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'handoff'), 'handoff', '__httpwww_fixm_aeroflight3_0_UnitBoundaryType_handoff', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 311, 15), )

    
    handoff = property(__handoff.value, __handoff.set, None, "\n                        An action taken to transfer the radar identification of an aircraft from one controller \n                        to another controller if the aircraft will enter the receiving controller's airspace \n                        and radio communications with the aircraft will be transferred. \n                     ")

    
    # Element upstreamUnit uses Python identifier upstreamUnit
    __upstreamUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upstreamUnit'), 'upstreamUnit', '__httpwww_fixm_aeroflight3_0_UnitBoundaryType_upstreamUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 320, 15), )

    
    upstreamUnit = property(__upstreamUnit.value, __upstreamUnit.set, None, '\n                        .Upstream Unit: The unit the flight will enter prior to this unit, based on the planned \n                        route of flight, altitude, and accepted constraints. \n                        .Delegated Unit Indicator: Indicates whether or not the controlling unit has been \n                        delegated authority for the flight based on agreement with the unit in whose Area \n                        of Responsibility (AOR) the flight is currently located. \n                     ')

    
    # Attribute delegated inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute sectorIdentifier inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute unitBoundaryIndicator uses Python identifier unitBoundaryIndicator
    __unitBoundaryIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unitBoundaryIndicator'), 'unitBoundaryIndicator', '__httpwww_fixm_aeroflight3_0_UnitBoundaryType_unitBoundaryIndicator', _module_typeBindings.UnitBoundaryIndicatorType)
    __unitBoundaryIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 332, 12)
    __unitBoundaryIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 332, 12)
    
    unitBoundaryIndicator = property(__unitBoundaryIndicator.value, __unitBoundaryIndicator.set, None, '\n                     .Unit Boundary Indicator: An indicator of the status of the boundary crossing in \n                     the Unit Boundary List as a past crossing, the current or next crossing, or a future \n                     crossing. \n                  ')

    _ElementMap.update({
        __boundaryCrossingCoordinated.name() : __boundaryCrossingCoordinated,
        __boundaryCrossingProposed.name() : __boundaryCrossingProposed,
        __downstreamUnit.name() : __downstreamUnit,
        __handoff.name() : __handoff,
        __upstreamUnit.name() : __upstreamUnit
    })
    _AttributeMap.update({
        __unitBoundaryIndicator.name() : __unitBoundaryIndicator
    })
_module_typeBindings.UnitBoundaryType = UnitBoundaryType
Namespace.addCategoryObject('typeBinding', 'UnitBoundaryType', UnitBoundaryType)


# Complex type {http://www.fixm.aero/flight/3.0}CpdlcConnectionType with content type ELEMENT_ONLY
class CpdlcConnectionType (pyxb.binding.basis.complexTypeDefinition):
    """
            Groups information regarding CPDLC connection between air traffic control units 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CpdlcConnectionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 90, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element receivingUnitFrequency uses Python identifier receivingUnitFrequency
    __receivingUnitFrequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'receivingUnitFrequency'), 'receivingUnitFrequency', '__httpwww_fixm_aeroflight3_0_CpdlcConnectionType_receivingUnitFrequency', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 97, 9), )

    
    receivingUnitFrequency = property(__receivingUnitFrequency.value, __receivingUnitFrequency.set, None, '\n                  .Receiving Unit Frequency: The frequency of the receiving unit. \n               ')

    
    # Attribute atnLogonParameters uses Python identifier atnLogonParameters
    __atnLogonParameters = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'atnLogonParameters'), 'atnLogonParameters', '__httpwww_fixm_aeroflight3_0_CpdlcConnectionType_atnLogonParameters', _module_typeBindings.AtnLogonParametersType)
    __atnLogonParameters._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 105, 6)
    __atnLogonParameters._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 105, 6)
    
    atnLogonParameters = property(__atnLogonParameters.value, __atnLogonParameters.set, None, '\n               .ATN Logon Parameters:  The ATN logon parameters allow the ground unit to log on \n               to the data link equipped aircraft to use the data link applications. \n            ')

    
    # Attribute connectionStatus uses Python identifier connectionStatus
    __connectionStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'connectionStatus'), 'connectionStatus', '__httpwww_fixm_aeroflight3_0_CpdlcConnectionType_connectionStatus', _module_typeBindings.CpdlcConnectionStatusType)
    __connectionStatus._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 113, 6)
    __connectionStatus._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 113, 6)
    
    connectionStatus = property(__connectionStatus.value, __connectionStatus.set, None, '\n               .CPDLC Connection Status: Provides the aircraft s Controller Pilot Data Link Communications \n               (CPDLC) Connection status and optional frequency information. \n            ')

    
    # Attribute fans1ALogonParameters uses Python identifier fans1ALogonParameters
    __fans1ALogonParameters = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fans1ALogonParameters'), 'fans1ALogonParameters', '__httpwww_fixm_aeroflight3_0_CpdlcConnectionType_fans1ALogonParameters', _module_typeBindings.Fans1ALogonParametersType)
    __fans1ALogonParameters._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 121, 6)
    __fans1ALogonParameters._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 121, 6)
    
    fans1ALogonParameters = property(__fans1ALogonParameters.value, __fans1ALogonParameters.set, None, '\n               .FANS/1A Logon Parameters:  The information necessary to establish CPDLC and/or ADS-C \n               connections with a FANS equipped aircraft. \n            ')

    
    # Attribute frequencyUsage uses Python identifier frequencyUsage
    __frequencyUsage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'frequencyUsage'), 'frequencyUsage', '__httpwww_fixm_aeroflight3_0_CpdlcConnectionType_frequencyUsage', _module_typeBindings.FrequencyUsageType)
    __frequencyUsage._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 129, 6)
    __frequencyUsage._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 129, 6)
    
    frequencyUsage = property(__frequencyUsage.value, __frequencyUsage.set, None, '\n               .Frequency Usage: The usage of the frequency. \n            ')

    
    # Attribute sendCpldcIndicator uses Python identifier sendCpldcIndicator
    __sendCpldcIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sendCpldcIndicator'), 'sendCpldcIndicator', '__httpwww_fixm_aeroflight3_0_CpdlcConnectionType_sendCpldcIndicator', _module_typeBindings.CpdlcStartRequestIndicatorType)
    __sendCpldcIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 136, 6)
    __sendCpldcIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 136, 6)
    
    sendCpldcIndicator = property(__sendCpldcIndicator.value, __sendCpldcIndicator.set, None, '\n               .CPDLC Start Request Indicator: For a flight crossing the boundary from one facility \n               to the next, notifies the data link equipped unit it can send a CPDLC Start Request \n               to the aircraft, because the aircraft is authorized to accept a CPDLC connection \n               request from the receiving unit. \n            ')

    _ElementMap.update({
        __receivingUnitFrequency.name() : __receivingUnitFrequency
    })
    _AttributeMap.update({
        __atnLogonParameters.name() : __atnLogonParameters,
        __connectionStatus.name() : __connectionStatus,
        __fans1ALogonParameters.name() : __fans1ALogonParameters,
        __frequencyUsage.name() : __frequencyUsage,
        __sendCpldcIndicator.name() : __sendCpldcIndicator
    })
_module_typeBindings.CpdlcConnectionType = CpdlcConnectionType
Namespace.addCategoryObject('typeBinding', 'CpdlcConnectionType', CpdlcConnectionType)


# Complex type {http://www.fixm.aero/flight/3.0}EnRouteType with content type ELEMENT_ONLY
class EnRouteType (_ImportedBinding__fb.FeatureType):
    """
            Groups the en route information about the flight such as the current position, coordination 
            between air traffic units, and boundary crossing throughout the duration of the flight. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 286, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element alternateAerodrome uses Python identifier alternateAerodrome
    __alternateAerodrome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'alternateAerodrome'), 'alternateAerodrome', '__httpwww_fixm_aeroflight3_0_EnRouteType_alternateAerodrome', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 297, 15), )

    
    alternateAerodrome = property(__alternateAerodrome.value, __alternateAerodrome.set, None, '\n                        .En Route Alternate Aerodrome: An ICAO designator of the aerodrome to which a flight \n                        could be diverted while en route, if needed. \n                     ')

    
    # Element beaconCodeAssignment uses Python identifier beaconCodeAssignment
    __beaconCodeAssignment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'beaconCodeAssignment'), 'beaconCodeAssignment', '__httpwww_fixm_aeroflight3_0_EnRouteType_beaconCodeAssignment', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 305, 15), )

    
    beaconCodeAssignment = property(__beaconCodeAssignment.value, __beaconCodeAssignment.set, None, '\n                        Contains information about current, previous and next beacon code assignments along \n                        with the beacon code assigning facility. \n                     ')

    
    # Element boundaryCrossings uses Python identifier boundaryCrossings
    __boundaryCrossings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundaryCrossings'), 'boundaryCrossings', '__httpwww_fixm_aeroflight3_0_EnRouteType_boundaryCrossings', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 313, 15), )

    
    boundaryCrossings = property(__boundaryCrossings.value, __boundaryCrossings.set, None, '\n                        A list of boundary crossings that will be traversed En Route \n                        .Unit Boundary List: The ordered list of units the flight is expected to traverse, \n                        based on the planned route of flight and altitude. \n                     ')

    
    # Element cleared uses Python identifier cleared
    __cleared = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cleared'), 'cleared', '__httpwww_fixm_aeroflight3_0_EnRouteType_cleared', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 322, 15), )

    
    cleared = property(__cleared.value, __cleared.set, None, '\n                        Contains the cleared information about the flight. \n                     ')

    
    # Element controlElement uses Python identifier controlElement
    __controlElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'controlElement'), 'controlElement', '__httpwww_fixm_aeroflight3_0_EnRouteType_controlElement', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 329, 15), )

    
    controlElement = property(__controlElement.value, __controlElement.set, None, '\n                        .Control Element: The constrained aerodrome or airspace element (subject to a Traffic \n                        Management Initiative/Regulation) indicating the reason for a flight being controlled. \n                        \n                     ')

    
    # Element cpdlcConnection uses Python identifier cpdlcConnection
    __cpdlcConnection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cpdlcConnection'), 'cpdlcConnection', '__httpwww_fixm_aeroflight3_0_EnRouteType_cpdlcConnection', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 338, 15), )

    
    cpdlcConnection = property(__cpdlcConnection.value, __cpdlcConnection.set, None, '\n                        Groups information regarding CPDLC connection between air traffic control units \n                     ')

    
    # Element pointout uses Python identifier pointout
    __pointout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pointout'), 'pointout', '__httpwww_fixm_aeroflight3_0_EnRouteType_pointout', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 345, 15), )

    
    pointout = property(__pointout.value, __pointout.set, None, '\n                        A physical or automated action taken by a controller to transfer the radar identification \n                        of an aircraft to another controller if the aircraft will or may enter the airspace \n                        or protected airspace of another controller and radio communications will not be \n                        transferred. \n                     ')

    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpwww_fixm_aeroflight3_0_EnRouteType_position', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 355, 15), )

    
    position = property(__position.value, __position.set, None, '\n                        Contains the current position and associated data of the aircraft. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute fleetPrioritization uses Python identifier fleetPrioritization
    __fleetPrioritization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fleetPrioritization'), 'fleetPrioritization', '__httpwww_fixm_aeroflight3_0_EnRouteType_fleetPrioritization', _ImportedBinding__fb.FleetPriorityType)
    __fleetPrioritization._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 363, 12)
    __fleetPrioritization._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 363, 12)
    
    fleetPrioritization = property(__fleetPrioritization.value, __fleetPrioritization.set, None, '\n                     The relative priority of a flight, within a flight operator’s fleet of aircraft, \n                     defined for a portion or the entire en route phase of flight \n                  ')

    _ElementMap.update({
        __alternateAerodrome.name() : __alternateAerodrome,
        __beaconCodeAssignment.name() : __beaconCodeAssignment,
        __boundaryCrossings.name() : __boundaryCrossings,
        __cleared.name() : __cleared,
        __controlElement.name() : __controlElement,
        __cpdlcConnection.name() : __cpdlcConnection,
        __pointout.name() : __pointout,
        __position.name() : __position
    })
    _AttributeMap.update({
        __fleetPrioritization.name() : __fleetPrioritization
    })
_module_typeBindings.EnRouteType = EnRouteType
Namespace.addCategoryObject('typeBinding', 'EnRouteType', EnRouteType)


# Complex type {http://www.fixm.aero/flight/3.0}AircraftPositionType with content type ELEMENT_ONLY
class AircraftPositionType (_ImportedBinding__fb.FeatureType):
    """
            Contains the current position and associated data of the aircraft. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftPositionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 118, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element actualSpeed uses Python identifier actualSpeed
    __actualSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'actualSpeed'), 'actualSpeed', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_actualSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 127, 15), )

    
    actualSpeed = property(__actualSpeed.value, __actualSpeed.set, None, '\n                        Actual flight  speed supplied by various sources. \n                     ')

    
    # Element altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altitude'), 'altitude', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_altitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 134, 15), )

    
    altitude = property(__altitude.value, __altitude.set, None, '\n                        .Reported Altitude: The latest valid Mode C altitude received from an aircraft, or \n                        the latest reported altitude received from a pilot. \n                     ')

    
    # Element followingPosition uses Python identifier followingPosition
    __followingPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'followingPosition'), 'followingPosition', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_followingPosition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 142, 15), )

    
    followingPosition = property(__followingPosition.value, __followingPosition.set, None, '\n                        .Following Future Reporting Position: Estimated second future position of the aircraft \n                        transmitted in a non-radar airspace position report. \n                        .Following Future Reporting Position Altitude: Expected altitude at the estimated \n                        second future position of the aircraft transmitted in a non-radar airspace position \n                        report. \n                     ')

    
    # Element nextPosition uses Python identifier nextPosition
    __nextPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nextPosition'), 'nextPosition', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_nextPosition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 153, 15), )

    
    nextPosition = property(__nextPosition.value, __nextPosition.set, None, '\n                        For Oceanic flights, the next reporting position is required. \n                        .Next Future Reporting Position Altitude: Expected altitude at the estimated next \n                        future position of the aircraft transmitted in a non-radar airspace position report. \n                        \n                        .Next Future Reporting Position: Estimated next future position of the aircraft transmitted \n                        in a non-radar airspace position report. \n                     ')

    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_position', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 165, 15), )

    
    position = property(__position.value, __position.set, None, '\n                        .Current Position: The actual location of an active flight as reported by surveillance, \n                        for a flight tracked by radar, or from the position part of a pilot progress report, \n                        for an oceanic flight or flight operating in non-radar airspace. \n                     ')

    
    # Element track uses Python identifier track
    __track = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'track'), 'track', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_track', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 174, 15), )

    
    track = property(__track.value, __track.set, None, '\n                        .Current Track: The direction the aircraft is flying, over the ground, relative to \n                        true north.  It is the heading of the aircraft as impacted by the wind. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute positionTime uses Python identifier positionTime
    __positionTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positionTime'), 'positionTime', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_positionTime', _ImportedBinding__ff.TimeType)
    __positionTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 183, 12)
    __positionTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 183, 12)
    
    positionTime = property(__positionTime.value, __positionTime.set, None, '\n                     .Current Position Time: The time associated with the Current Position of an active \n                     flight, from the radar surveillance report or progress report. \n                  ')

    
    # Attribute reportSource uses Python identifier reportSource
    __reportSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reportSource'), 'reportSource', '__httpwww_fixm_aeroflight3_0_AircraftPositionType_reportSource', _module_typeBindings.PositionReportSourceType)
    __reportSource._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 191, 12)
    __reportSource._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 191, 12)
    
    reportSource = property(__reportSource.value, __reportSource.set, None, '\n                     .Current Position Report Source: The source of the current position report information. \n                     \n                  ')

    _ElementMap.update({
        __actualSpeed.name() : __actualSpeed,
        __altitude.name() : __altitude,
        __followingPosition.name() : __followingPosition,
        __nextPosition.name() : __nextPosition,
        __position.name() : __position,
        __track.name() : __track
    })
    _AttributeMap.update({
        __positionTime.name() : __positionTime,
        __reportSource.name() : __reportSource
    })
_module_typeBindings.AircraftPositionType = AircraftPositionType
Namespace.addCategoryObject('typeBinding', 'AircraftPositionType', AircraftPositionType)


# Complex type {http://www.fixm.aero/flight/3.0}FlightArrivalType with content type ELEMENT_ONLY
class FlightArrivalType (_ImportedBinding__fb.FeatureType):
    """
            Arrival information linked to a flight. This information shall include: 
            * assigned runway 
            * assigned STAR procedure 
            * Missed_Approach status (Boolean) 
            * Eligibility for AMAN (Is the flight already in the scope of AMAN sequencing?) 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightArrivalType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 81, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element approachFix uses Python identifier approachFix
    __approachFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'approachFix'), 'approachFix', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_approachFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 94, 15), )

    
    approachFix = property(__approachFix.value, __approachFix.set, None, '\n                        .Initial Approach Fix: The point on the arrival route at which arrival sequencing \n                        activities are focused, such that, when the flight passes this point, a stable runway \n                        arrival sequence can be provided. \n                     ')

    
    # Element approachTime uses Python identifier approachTime
    __approachTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'approachTime'), 'approachTime', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_approachTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 103, 15), )

    
    approachTime = property(__approachTime.value, __approachTime.set, None, "\n                        .Approach Time - Estimated: The shared time estimate at which the flight's final \n                        approach is expected to commence. \n                     ")

    
    # Element arrivalAerodrome uses Python identifier arrivalAerodrome
    __arrivalAerodrome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome'), 'arrivalAerodrome', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalAerodrome', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 111, 15), )

    
    arrivalAerodrome = property(__arrivalAerodrome.value, __arrivalAerodrome.set, None, '\n                        .Destination Aerodrome: The ICAO designator or the name of the aerodrome at which \n                        the flight is scheduled to arrive. \n                     ')

    
    # Element arrivalAerodromeAlternate uses Python identifier arrivalAerodromeAlternate
    __arrivalAerodromeAlternate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeAlternate'), 'arrivalAerodromeAlternate', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalAerodromeAlternate', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 119, 15), )

    
    arrivalAerodromeAlternate = property(__arrivalAerodromeAlternate.value, __arrivalAerodromeAlternate.set, None, '\n                        .Destination Aerodrome - Alternate: ICAO designator or the name of an alternate aerodrome \n                        to which an aircraft may proceed, should it become either impossible or inadvisable \n                        to land at the original destination aerodrome or an alternate destination location. \n                        \n                     ')

    
    # Element arrivalAerodromeOriginal uses Python identifier arrivalAerodromeOriginal
    __arrivalAerodromeOriginal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeOriginal'), 'arrivalAerodromeOriginal', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalAerodromeOriginal', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 129, 15), )

    
    arrivalAerodromeOriginal = property(__arrivalAerodromeOriginal.value, __arrivalAerodromeOriginal.set, None, '\n                        .Original Destination Aerodrome: The Original Destination Airport is the Destination \n                        Airport submitted when a Flight Plan was initially filed. \n                     ')

    
    # Element arrivalFix uses Python identifier arrivalFix
    __arrivalFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrivalFix'), 'arrivalFix', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 137, 15), )

    
    arrivalFix = property(__arrivalFix.value, __arrivalFix.set, None, '\n                        .Aerodrome Arrival Fix: The point at which the responsibility for control of the \n                        flight is transferred from the En Route Air Traffic Control unit (Centre, ARTCC) \n                        to the Terminal Air Traffic Control unit. \n                     ')

    
    # Element arrivalFixTime uses Python identifier arrivalFixTime
    __arrivalFixTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrivalFixTime'), 'arrivalFixTime', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalFixTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 146, 15), )

    
    arrivalFixTime = property(__arrivalFixTime.value, __arrivalFixTime.set, None, '\n                        .Arrival Fix Time - Estimated: Estimated time over the arrival fix. \n                        .Arrival Fix Time - Actual: Actual time the flight passed over the arrival fix. \n                     ')

    
    # Element filedRevisedDestinationAerodrome uses Python identifier filedRevisedDestinationAerodrome
    __filedRevisedDestinationAerodrome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'filedRevisedDestinationAerodrome'), 'filedRevisedDestinationAerodrome', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_filedRevisedDestinationAerodrome', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 154, 15), )

    
    filedRevisedDestinationAerodrome = property(__filedRevisedDestinationAerodrome.value, __filedRevisedDestinationAerodrome.set, None, '\n                        Represents the filed revised destination aerodrome. \n                     ')

    
    # Element runwayPositionAndTime uses Python identifier runwayPositionAndTime
    __runwayPositionAndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime'), 'runwayPositionAndTime', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_runwayPositionAndTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 161, 15), )

    
    runwayPositionAndTime = property(__runwayPositionAndTime.value, __runwayPositionAndTime.set, None, '\n                        .Arrival Runway: The expected, assigned, or actual runway for an arriving flight. \n                        \n                        .Runway Arrival Time - Estimated: The most reliable estimated time when an aircraft \n                        will touch down on the runway. \n                        .Runway Arrival Time - Target: The time when the aircraft is planned to touch down \n                        at the runway. \n                        .Runway Arrival Time - Actual: The actual time at which the aircraft lands on a runway. \n                        \n                        .Runway Arrival Time - Controlled: The time at which a flight is required to touch \n                        down at the runway, as a result of a tactical slot allocation or a Traffic Management \n                        Initiative. \n                     ')

    
    # Element standPositionAndTime uses Python identifier standPositionAndTime
    __standPositionAndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'standPositionAndTime'), 'standPositionAndTime', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_standPositionAndTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 178, 15), )

    
    standPositionAndTime = property(__standPositionAndTime.value, __standPositionAndTime.set, None, '\n                        .In-Block Time - Earliest: The earliest time an aircraft operator is able to arrive \n                        at the gate on completion of the flight, as specified by the aircraft operator when \n                        submitting the flight information. \n                        .Arrival Stand: The stand at which an aircraft arrives at the destination airport \n                        on completion of the flight. \n                        .In-Block Time - Actual: The time at which a flight arrives at the stand. \n                        .In-Block Time - Initial: The original stand arrival time of the flight when the \n                        flight is first created. \n                        .Arrival Terminal: The airport terminal at which the flight arrives. \n                        .In-Block Time - Controlled: The time at which a flight is required to arrive at \n                        the destination stand as determined by a TMI. \n                        .In-Block Time - Estimated: The estimated time at which a flight will arrive at the \n                        stand. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute arrivalFleetPrioritization uses Python identifier arrivalFleetPrioritization
    __arrivalFleetPrioritization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalFleetPrioritization'), 'arrivalFleetPrioritization', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalFleetPrioritization', _ImportedBinding__fb.FleetPriorityType)
    __arrivalFleetPrioritization._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 198, 12)
    __arrivalFleetPrioritization._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 198, 12)
    
    arrivalFleetPrioritization = property(__arrivalFleetPrioritization.value, __arrivalFleetPrioritization.set, None, '\n                     .Fleet Prioritization - Arrival: The relative priority of a flight, within a flight \n                     operator s fleet of aircraft, defined for a portion or the entire arrival phase of \n                     flight. \n                  ')

    
    # Attribute arrivalSequenceNumber uses Python identifier arrivalSequenceNumber
    __arrivalSequenceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalSequenceNumber'), 'arrivalSequenceNumber', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_arrivalSequenceNumber', _ImportedBinding__fb.CountType)
    __arrivalSequenceNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 207, 12)
    __arrivalSequenceNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 207, 12)
    
    arrivalSequenceNumber = property(__arrivalSequenceNumber.value, __arrivalSequenceNumber.set, None, '\n                     .Arrival Sequence Number: The expected sequence of the flight in the scheduling list \n                     of arriving flights. \n                  ')

    
    # Attribute earliestInBlockTime uses Python identifier earliestInBlockTime
    __earliestInBlockTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'earliestInBlockTime'), 'earliestInBlockTime', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_earliestInBlockTime', _ImportedBinding__ff.TimeType)
    __earliestInBlockTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 215, 12)
    __earliestInBlockTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 215, 12)
    
    earliestInBlockTime = property(__earliestInBlockTime.value, __earliestInBlockTime.set, None, '\n                     .In-Block Time - Earliest: The earliest time an aircraft operator is able to arrive \n                     at the gate on completion of the flight, as specified by the aircraft operator when \n                     submitting the flight information. \n                  ')

    
    # Attribute filedRevisedDestinationStar uses Python identifier filedRevisedDestinationStar
    __filedRevisedDestinationStar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filedRevisedDestinationStar'), 'filedRevisedDestinationStar', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_filedRevisedDestinationStar', _ImportedBinding__fb.StandardInstrumentRouteDesignatorType)
    __filedRevisedDestinationStar._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 224, 12)
    __filedRevisedDestinationStar._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 224, 12)
    
    filedRevisedDestinationStar = property(__filedRevisedDestinationStar.value, __filedRevisedDestinationStar.set, None, '\n                     Standard Instrument Arrival Route procedure for the revised destination. \n                  ')

    
    # Attribute landingLimits uses Python identifier landingLimits
    __landingLimits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'landingLimits'), 'landingLimits', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_landingLimits', _module_typeBindings.LandingLimitsType)
    __landingLimits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 231, 12)
    __landingLimits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 231, 12)
    
    landingLimits = property(__landingLimits.value, __landingLimits.set, None, '\n                     .Landing Limits: The landing qualification of the flight, considering crew and equipment. \n                     \n                  ')

    
    # Attribute standardInstrumentArrival uses Python identifier standardInstrumentArrival
    __standardInstrumentArrival = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standardInstrumentArrival'), 'standardInstrumentArrival', '__httpwww_fixm_aeroflight3_0_FlightArrivalType_standardInstrumentArrival', _ImportedBinding__fb.StandardInstrumentRouteDesignatorType)
    __standardInstrumentArrival._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 239, 12)
    __standardInstrumentArrival._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 239, 12)
    
    standardInstrumentArrival = property(__standardInstrumentArrival.value, __standardInstrumentArrival.set, None, '\n                     .Standard Instrument Arrival Designator: The textual designator of the Standard Instrument \n                     Arrival (STAR). \n                  ')

    _ElementMap.update({
        __approachFix.name() : __approachFix,
        __approachTime.name() : __approachTime,
        __arrivalAerodrome.name() : __arrivalAerodrome,
        __arrivalAerodromeAlternate.name() : __arrivalAerodromeAlternate,
        __arrivalAerodromeOriginal.name() : __arrivalAerodromeOriginal,
        __arrivalFix.name() : __arrivalFix,
        __arrivalFixTime.name() : __arrivalFixTime,
        __filedRevisedDestinationAerodrome.name() : __filedRevisedDestinationAerodrome,
        __runwayPositionAndTime.name() : __runwayPositionAndTime,
        __standPositionAndTime.name() : __standPositionAndTime
    })
    _AttributeMap.update({
        __arrivalFleetPrioritization.name() : __arrivalFleetPrioritization,
        __arrivalSequenceNumber.name() : __arrivalSequenceNumber,
        __earliestInBlockTime.name() : __earliestInBlockTime,
        __filedRevisedDestinationStar.name() : __filedRevisedDestinationStar,
        __landingLimits.name() : __landingLimits,
        __standardInstrumentArrival.name() : __standardInstrumentArrival
    })
_module_typeBindings.FlightArrivalType = FlightArrivalType
Namespace.addCategoryObject('typeBinding', 'FlightArrivalType', FlightArrivalType)


# Complex type {http://www.fixm.aero/flight/3.0}ClimbToLevelConstraintType with content type ELEMENT_ONLY
class ClimbToLevelConstraintType (RouteConstraintOrPreferenceType):
    """
            .Change Cruise Climb: The parameters of a cruise climb executed at the associated 
            significant point. It contains the following parameters: 1. the speed to be maintained 
            during cruise climb; 2. either the minimum and maximum levels defining the layer 
            to be occupied during cruise climb, or the level above which cruise climb is planned. 
            
            .Route-Change Cruise Climb: The parameters of a cruise climb executed at the associated 
            significant point. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClimbToLevelConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 98, 3)
    _ElementMap = RouteConstraintOrPreferenceType._ElementMap.copy()
    _AttributeMap = RouteConstraintOrPreferenceType._AttributeMap.copy()
    # Base type is RouteConstraintOrPreferenceType
    
    # Element climbToLevel uses Python identifier climbToLevel
    __climbToLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'climbToLevel'), 'climbToLevel', '__httpwww_fixm_aeroflight3_0_ClimbToLevelConstraintType_climbToLevel', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 113, 15), )

    
    climbToLevel = property(__climbToLevel.value, __climbToLevel.set, None, '\n                        .Change Cruise Climb: The parameters of a cruise climb executed at the associated \n                        significant point. It contains the following parameters: 1. the speed to be maintained \n                        during cruise climb; 2. either the minimum and maximum levels defining the layer \n                        to be occupied during cruise climb, or the level above which cruise climb is planned. \n                        \n                     ')

    
    # Attribute altitudeQualification uses Python identifier altitudeQualification
    __altitudeQualification = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'altitudeQualification'), 'altitudeQualification', '__httpwww_fixm_aeroflight3_0_ClimbToLevelConstraintType_altitudeQualification', _module_typeBindings.AltitudeQualifierType)
    __altitudeQualification._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 125, 12)
    __altitudeQualification._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 125, 12)
    
    altitudeQualification = property(__altitudeQualification.value, __altitudeQualification.set, None, '\n                     Specifies that the altitude specified in the ClimbToLevelConstraint is not a maximum \n                     altitude, and aircraft may climb to a higher level. \n                  ')

    
    # Attribute constraintType inherited from {http://www.fixm.aero/flight/3.0}RouteConstraintOrPreferenceType
    _ElementMap.update({
        __climbToLevel.name() : __climbToLevel
    })
    _AttributeMap.update({
        __altitudeQualification.name() : __altitudeQualification
    })
_module_typeBindings.ClimbToLevelConstraintType = ClimbToLevelConstraintType
Namespace.addCategoryObject('typeBinding', 'ClimbToLevelConstraintType', ClimbToLevelConstraintType)


# Complex type {http://www.fixm.aero/flight/3.0}LevelConstraintType with content type ELEMENT_ONLY
class LevelConstraintType (RouteConstraintOrPreferenceType):
    """
            .Route-Change Speed and Altitude: The planned speed and altitude the aircraft will 
            change to either prior to, or after reaching, the associated Significant Point along 
            its Route. 
            .Change Speed and Altitude: The planned speed and altitude that the aircraft will 
            change to upon reaching the associated Significant Point along its Route. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LevelConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 154, 3)
    _ElementMap = RouteConstraintOrPreferenceType._ElementMap.copy()
    _AttributeMap = RouteConstraintOrPreferenceType._AttributeMap.copy()
    # Base type is RouteConstraintOrPreferenceType
    
    # Element level uses Python identifier level
    __level = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'level'), 'level', '__httpwww_fixm_aeroflight3_0_LevelConstraintType_level', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 167, 15), )

    
    level = property(__level.value, __level.set, None, '\n                        .Change Speed and Altitude: The planned speed and altitude that the aircraft will \n                        change to upon reaching the associated Significant Point along its Route. \n                     ')

    
    # Element timeConstraint uses Python identifier timeConstraint
    __timeConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'timeConstraint'), 'timeConstraint', '__httpwww_fixm_aeroflight3_0_LevelConstraintType_timeConstraint', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 175, 15), )

    
    timeConstraint = property(__timeConstraint.value, __timeConstraint.set, None, '\n                        Level constraint may have an associated time constraint. \n                     ')

    
    # Attribute positionQualification uses Python identifier positionQualification
    __positionQualification = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positionQualification'), 'positionQualification', '__httpwww_fixm_aeroflight3_0_LevelConstraintType_positionQualification', _module_typeBindings.PositionQualifierType)
    __positionQualification._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 183, 12)
    __positionQualification._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 183, 12)
    
    positionQualification = property(__positionQualification.value, __positionQualification.set, None, '\n                     Qualifies the position associated with the level constraint. \n                  ')

    
    # Attribute constraintType inherited from {http://www.fixm.aero/flight/3.0}RouteConstraintOrPreferenceType
    _ElementMap.update({
        __level.name() : __level,
        __timeConstraint.name() : __timeConstraint
    })
    _AttributeMap.update({
        __positionQualification.name() : __positionQualification
    })
_module_typeBindings.LevelConstraintType = LevelConstraintType
Namespace.addCategoryObject('typeBinding', 'LevelConstraintType', LevelConstraintType)


# Complex type {http://www.fixm.aero/flight/3.0}SpeedConstraintType with content type ELEMENT_ONLY
class SpeedConstraintType (RouteConstraintOrPreferenceType):
    """
            .Route-Change Speed and Altitude: The planned speed and altitude the aircraft will 
            change to either prior to, or after reaching, the associated Significant Point along 
            its Route. 
            .Change Speed and Altitude: The planned speed and altitude that the aircraft will 
            change to upon reaching the associated Significant Point along its Route. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpeedConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 226, 3)
    _ElementMap = RouteConstraintOrPreferenceType._ElementMap.copy()
    _AttributeMap = RouteConstraintOrPreferenceType._AttributeMap.copy()
    # Base type is RouteConstraintOrPreferenceType
    
    # Element speed uses Python identifier speed
    __speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__httpwww_fixm_aeroflight3_0_SpeedConstraintType_speed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 239, 15), )

    
    speed = property(__speed.value, __speed.set, None, '\n                        .Change Speed and Altitude: The planned speed and altitude that the aircraft will \n                        change to upon reaching the associated Significant Point along its Route. \n                     ')

    
    # Element timeConstraint uses Python identifier timeConstraint
    __timeConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'timeConstraint'), 'timeConstraint', '__httpwww_fixm_aeroflight3_0_SpeedConstraintType_timeConstraint', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 247, 15), )

    
    timeConstraint = property(__timeConstraint.value, __timeConstraint.set, None, '\n                        A speed constraint may have an associated time constraint. \n                     ')

    
    # Attribute constraintType inherited from {http://www.fixm.aero/flight/3.0}RouteConstraintOrPreferenceType
    
    # Attribute positionQualification uses Python identifier positionQualification
    __positionQualification = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'positionQualification'), 'positionQualification', '__httpwww_fixm_aeroflight3_0_SpeedConstraintType_positionQualification', _module_typeBindings.PositionQualifierType)
    __positionQualification._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 255, 12)
    __positionQualification._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 255, 12)
    
    positionQualification = property(__positionQualification.value, __positionQualification.set, None, '\n                     Qualifies the position associated with the speed constraint. \n                  ')

    _ElementMap.update({
        __speed.name() : __speed,
        __timeConstraint.name() : __timeConstraint
    })
    _AttributeMap.update({
        __positionQualification.name() : __positionQualification
    })
_module_typeBindings.SpeedConstraintType = SpeedConstraintType
Namespace.addCategoryObject('typeBinding', 'SpeedConstraintType', SpeedConstraintType)


# Complex type {http://www.fixm.aero/flight/3.0}TimeConstraintType with content type EMPTY
class TimeConstraintType (RouteConstraintOrPreferenceType):
    """
            Time Constraint associated with a route point or with other constraint. 
            .Route-Change Speed and Altitude at Time: The planned speed and altitude the aircraft 
            will change to relative to the associated time. 
            .Route-Fix Time - Required: Contains the time at fix and the time at fix constraint 
            condition, which together describe when the aircraft should arrive at a particular 
            fix. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TimeConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 267, 3)
    _ElementMap = RouteConstraintOrPreferenceType._ElementMap.copy()
    _AttributeMap = RouteConstraintOrPreferenceType._AttributeMap.copy()
    # Base type is RouteConstraintOrPreferenceType
    
    # Attribute constraintType inherited from {http://www.fixm.aero/flight/3.0}RouteConstraintOrPreferenceType
    
    # Attribute requiredTime uses Python identifier requiredTime
    __requiredTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requiredTime'), 'requiredTime', '__httpwww_fixm_aeroflight3_0_TimeConstraintType_requiredTime', _ImportedBinding__ff.TimeType)
    __requiredTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 280, 12)
    __requiredTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 280, 12)
    
    requiredTime = property(__requiredTime.value, __requiredTime.set, None, '\n                     Time associated with the time constraint. \n                  ')

    
    # Attribute timeQualification uses Python identifier timeQualification
    __timeQualification = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeQualification'), 'timeQualification', '__httpwww_fixm_aeroflight3_0_TimeConstraintType_timeQualification', _module_typeBindings.TimeQualifierType)
    __timeQualification._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 287, 12)
    __timeQualification._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 287, 12)
    
    timeQualification = property(__timeQualification.value, __timeQualification.set, None, '\n                     Qualifies the time associated with the constraint. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __requiredTime.name() : __requiredTime,
        __timeQualification.name() : __timeQualification
    })
_module_typeBindings.TimeConstraintType = TimeConstraintType
Namespace.addCategoryObject('typeBinding', 'TimeConstraintType', TimeConstraintType)


# Complex type {http://www.fixm.aero/flight/3.0}FlightDepartureType with content type ELEMENT_ONLY
class FlightDepartureType (_ImportedBinding__fb.FeatureType):
    """
            Groups information pertaining to the flight's departure. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightDepartureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 140, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element departureAerodrome uses Python identifier departureAerodrome
    __departureAerodrome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'departureAerodrome'), 'departureAerodrome', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_departureAerodrome', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 149, 15), )

    
    departureAerodrome = property(__departureAerodrome.value, __departureAerodrome.set, None, '\n                        .Departure Aerodrome: The ICAO designator of the aerodrome from which the flight \n                        departs. \n                     ')

    
    # Element departureFix uses Python identifier departureFix
    __departureFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'departureFix'), 'departureFix', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_departureFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 157, 15), )

    
    departureFix = property(__departureFix.value, __departureFix.set, None, '\n                        .Aerodrome Departure Fix: The point at which the responsibility for control of the \n                        flight is transferred from the Terminal Air Traffic Control unit to the En Route \n                        Air Traffic Control unit (Centre, ARTCC). \n                     ')

    
    # Element departureFixTime uses Python identifier departureFixTime
    __departureFixTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'departureFixTime'), 'departureFixTime', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_departureFixTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 166, 15), )

    
    departureFixTime = property(__departureFixTime.value, __departureFixTime.set, None, '\n                        .Departure Fix Time - Estimated: The estimated time the flight is over the departure \n                        fix. \n                        .Departure Fix Time - Actual: The actual time the flight passed over the departure \n                        fix. \n                     ')

    
    # Element departureTimes uses Python identifier departureTimes
    __departureTimes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'departureTimes'), 'departureTimes', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_departureTimes', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 176, 15), )

    
    departureTimes = property(__departureTimes.value, __departureTimes.set, None, '\n                        Optional TimeSequences associated with departure activities. \n                     ')

    
    # Element offBlockReadyTime uses Python identifier offBlockReadyTime
    __offBlockReadyTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offBlockReadyTime'), 'offBlockReadyTime', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_offBlockReadyTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 183, 15), )

    
    offBlockReadyTime = property(__offBlockReadyTime.value, __offBlockReadyTime.set, None, '\n                        .Off-Block Ready Time - Actual: The time when the aircraft is ready for start-up/pushback \n                        or taxi immediately after clearance delivery. \n                        .Off-Block Ready Time - Target: The time an Aircraft Operator or Ground Handler estimates \n                        an aircraft will be ready, all doors closed, boarding bridge removed, push back vehicle \n                        available and ready to start up / push back immediately upon reception of clearance \n                        from the tower. \n                     ')

    
    # Element runwayPositionAndTime uses Python identifier runwayPositionAndTime
    __runwayPositionAndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime'), 'runwayPositionAndTime', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_runwayPositionAndTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 195, 15), )

    
    runwayPositionAndTime = property(__runwayPositionAndTime.value, __runwayPositionAndTime.set, None, "\n                        .Runway Departure Time - Estimated: The most reliable estimated take off time. \n                        .Departure Time - Estimated: The estimated off-block time for the flight at the Departure \n                        Aerodrome, or, if the flight plan is filed in the air, the estimated time of departure \n                        from the first point on the route. The time is given in UTC. \n                        .Departure Runway: The expected, assigned, or actual runway for a departing flight. \n                        \n                        .Departure Time - Actual: The actual time of departure from the aerodrome, or the \n                        actual time of departure from the first point on the Route when the flight is an \n                        'air file', i.e., the flight plan is filed once the aircraft is already airborne. \n                        This time is given in UTC. \n                        .Runway Departure Time - Target: The time when the aircraft is planned to take off \n                        from the runway. \n                        .Runway Departure Time - Actual: The actual time at which a flight takes off from \n                        the runway. \n                        .Runway Departure Time - Controlled: The time at which a flight is required to take \n                        off from the runway as a result of a tactical slot allocation or a Traffic Management \n                        Initiative. \n                     ")

    
    # Element standPositionAndTime uses Python identifier standPositionAndTime
    __standPositionAndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'standPositionAndTime'), 'standPositionAndTime', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_standPositionAndTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 218, 15), )

    
    standPositionAndTime = property(__standPositionAndTime.value, __standPositionAndTime.set, None, '\n                        .Off-Block Time - Actual: The time at which a flight departs from the stand. \n                        .Off Block Time - Earliest: The earliest time an aircraft can push back or taxi from \n                        the stand. \n                        .Departure Terminal: The airport terminal from which the flight departs. \n                        .Departure Stand: The stand from which an aircraft departs on commencement of the \n                        flight. \n                        .Off-Block Time - Initial: The date and time at which a flight was originally planning \n                        to depart the stand. \n                        .Off Block Time - Estimated: The estimated time at which a flight will depart from \n                        the stand. \n                        .Off-Block Time - Controlled: The time at which a flight is required to depart from \n                        the stand as determined by a TMI. \n                     ')

    
    # Element takeoffAlternateAerodrome uses Python identifier takeoffAlternateAerodrome
    __takeoffAlternateAerodrome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'takeoffAlternateAerodrome'), 'takeoffAlternateAerodrome', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_takeoffAlternateAerodrome', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 236, 15), )

    
    takeoffAlternateAerodrome = property(__takeoffAlternateAerodrome.value, __takeoffAlternateAerodrome.set, None, '\n                        .Take Off Alternate Aerodrome: An alternate aerodrome at which an aircraft can land, \n                        should it become necessary shortly after take off, and it is not possible to land \n                        at the departure aerodrome. \n                     ')

    
    # Element takeoffWeight uses Python identifier takeoffWeight
    __takeoffWeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'takeoffWeight'), 'takeoffWeight', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_takeoffWeight', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 245, 15), )

    
    takeoffWeight = property(__takeoffWeight.value, __takeoffWeight.set, None, '\n                        .Takeoff Weight: The expected takeoff weight of the aircraft, expressed in thousands \n                        of pounds or kilograms. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute departureFleetPrioritization uses Python identifier departureFleetPrioritization
    __departureFleetPrioritization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departureFleetPrioritization'), 'departureFleetPrioritization', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_departureFleetPrioritization', _ImportedBinding__fb.FleetPriorityType)
    __departureFleetPrioritization._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 254, 12)
    __departureFleetPrioritization._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 254, 12)
    
    departureFleetPrioritization = property(__departureFleetPrioritization.value, __departureFleetPrioritization.set, None, '\n                     .Fleet Prioritization - Departure: The relative priority of a flight, within a flight \n                     operator s fleet of aircraft, defined for a portion or the entire departure phase \n                     of flight. \n                  ')

    
    # Attribute departureSlot uses Python identifier departureSlot
    __departureSlot = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departureSlot'), 'departureSlot', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_departureSlot', _ImportedBinding__fb.SlotAssignmentType)
    __departureSlot._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 263, 12)
    __departureSlot._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 263, 12)
    
    departureSlot = property(__departureSlot.value, __departureSlot.set, None, '\n                     .Departure Slot: A time slot at an airport that identifies a point in time when an \n                     aircraft is constrained to depart from the airport. \n                  ')

    
    # Attribute earliestOffBlockTime uses Python identifier earliestOffBlockTime
    __earliestOffBlockTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'earliestOffBlockTime'), 'earliestOffBlockTime', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_earliestOffBlockTime', _ImportedBinding__ff.TimeType)
    __earliestOffBlockTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 271, 12)
    __earliestOffBlockTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 271, 12)
    
    earliestOffBlockTime = property(__earliestOffBlockTime.value, __earliestOffBlockTime.set, None, '\n                     .Off Block Time - Earliest: The earliest time an aircraft can push back or taxi from \n                     the stand. \n                  ')

    
    # Attribute standardInstrumentDeparture uses Python identifier standardInstrumentDeparture
    __standardInstrumentDeparture = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standardInstrumentDeparture'), 'standardInstrumentDeparture', '__httpwww_fixm_aeroflight3_0_FlightDepartureType_standardInstrumentDeparture', _ImportedBinding__fb.StandardInstrumentRouteDesignatorType)
    __standardInstrumentDeparture._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 279, 12)
    __standardInstrumentDeparture._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 279, 12)
    
    standardInstrumentDeparture = property(__standardInstrumentDeparture.value, __standardInstrumentDeparture.set, None, "\n                     .Standard Instrument Departure Designator: This is the name of a published procedure \n                     extending from the departure runway to the start of the en route part of the aircraft's \n                     route. \n                  ")

    _ElementMap.update({
        __departureAerodrome.name() : __departureAerodrome,
        __departureFix.name() : __departureFix,
        __departureFixTime.name() : __departureFixTime,
        __departureTimes.name() : __departureTimes,
        __offBlockReadyTime.name() : __offBlockReadyTime,
        __runwayPositionAndTime.name() : __runwayPositionAndTime,
        __standPositionAndTime.name() : __standPositionAndTime,
        __takeoffAlternateAerodrome.name() : __takeoffAlternateAerodrome,
        __takeoffWeight.name() : __takeoffWeight
    })
    _AttributeMap.update({
        __departureFleetPrioritization.name() : __departureFleetPrioritization,
        __departureSlot.name() : __departureSlot,
        __earliestOffBlockTime.name() : __earliestOffBlockTime,
        __standardInstrumentDeparture.name() : __standardInstrumentDeparture
    })
_module_typeBindings.FlightDepartureType = FlightDepartureType
Namespace.addCategoryObject('typeBinding', 'FlightDepartureType', FlightDepartureType)


# Complex type {http://www.fixm.aero/flight/3.0}FlightEmergencyType with content type ELEMENT_ONLY
class FlightEmergencyType (_ImportedBinding__fb.FeatureType):
    """
            Groups emergency information (description, phase, position, etc) for the flight. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightEmergencyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 95, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__httpwww_fixm_aeroflight3_0_FlightEmergencyType_contact', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 105, 15), )

    
    contact = property(__contact.value, __contact.set, None, '\n                        .Last Contact Unit: The last ATS unit which had two-way contact with the aircraft. \n                        \n                     ')

    
    # Element originator uses Python identifier originator
    __originator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'originator'), 'originator', '__httpwww_fixm_aeroflight3_0_FlightEmergencyType_originator', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 113, 15), )

    
    originator = property(__originator.value, __originator.set, None, '\n                        .Emergency Message Originator: The ICAO identifier of the ATS unit originating the \n                        emergency message. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute actionTaken uses Python identifier actionTaken
    __actionTaken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'actionTaken'), 'actionTaken', '__httpwww_fixm_aeroflight3_0_FlightEmergencyType_actionTaken', _ImportedBinding__fb.FreeTextType)
    __actionTaken._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 122, 12)
    __actionTaken._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 122, 12)
    
    actionTaken = property(__actionTaken.value, __actionTaken.set, None, '\n                     .Action Taken By Reporting Unit: A description of the actions taken by the reporting \n                     Air Traffic Service (ATS) unit, in the event of search and rescue. \n                  ')

    
    # Attribute emergencyDescription uses Python identifier emergencyDescription
    __emergencyDescription = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'emergencyDescription'), 'emergencyDescription', '__httpwww_fixm_aeroflight3_0_FlightEmergencyType_emergencyDescription', _ImportedBinding__fb.FreeTextType)
    __emergencyDescription._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 130, 12)
    __emergencyDescription._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 130, 12)
    
    emergencyDescription = property(__emergencyDescription.value, __emergencyDescription.set, None, '\n                     .Emergency Description: A short, plain-language description of the nature of the \n                     emergency. \n                  ')

    
    # Attribute otherInformation uses Python identifier otherInformation
    __otherInformation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherInformation'), 'otherInformation', '__httpwww_fixm_aeroflight3_0_FlightEmergencyType_otherInformation', _ImportedBinding__fb.FreeTextType)
    __otherInformation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 138, 12)
    __otherInformation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 138, 12)
    
    otherInformation = property(__otherInformation.value, __otherInformation.set, None, '\n                     .Other Search and Rescue Information: Other pertinent information not captured elsewhere \n                     needed to notify appropriate organizations regarding aircraft in need of search and \n                     rescue. \n                  ')

    
    # Attribute phase uses Python identifier phase
    __phase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phase'), 'phase', '__httpwww_fixm_aeroflight3_0_FlightEmergencyType_phase', _module_typeBindings.EmergencyPhaseType)
    __phase._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 147, 12)
    __phase._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 147, 12)
    
    phase = property(__phase.value, __phase.set, None, '\n                     .Emergency Phase: Stage of emergency the flight is currently under or an indication \n                     the emergency has been cancelled, as designated by an ATS unit. \n                  ')

    _ElementMap.update({
        __contact.name() : __contact,
        __originator.name() : __originator
    })
    _AttributeMap.update({
        __actionTaken.name() : __actionTaken,
        __emergencyDescription.name() : __emergencyDescription,
        __otherInformation.name() : __otherInformation,
        __phase.name() : __phase
    })
_module_typeBindings.FlightEmergencyType = FlightEmergencyType
Namespace.addCategoryObject('typeBinding', 'FlightEmergencyType', FlightEmergencyType)


# Complex type {http://www.fixm.aero/flight/3.0}LastContactType with content type ELEMENT_ONLY
class LastContactType (_ImportedBinding__fb.FeatureType):
    """
            .Last Contact Unit: The last ATS unit which had two-way contact with the aircraft. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LastContactType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 160, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element contactFrequency uses Python identifier contactFrequency
    __contactFrequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contactFrequency'), 'contactFrequency', '__httpwww_fixm_aeroflight3_0_LastContactType_contactFrequency', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 170, 15), )

    
    contactFrequency = property(__contactFrequency.value, __contactFrequency.set, None, '\n                        .Last Contact Radio Frequency: The transmitting/receiving frequency of the last two-way \n                        contact between the aircraft and an ATS unit. \n                     ')

    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpwww_fixm_aeroflight3_0_LastContactType_position', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 178, 15), )

    
    position = property(__position.value, __position.set, None, '\n                        .Last Known Position Report: The position of the aircraft last known to ATS and a \n                        corresponding timestamp. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute lastContactTime uses Python identifier lastContactTime
    __lastContactTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastContactTime'), 'lastContactTime', '__httpwww_fixm_aeroflight3_0_LastContactType_lastContactTime', _ImportedBinding__ff.TimeType)
    __lastContactTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 187, 12)
    __lastContactTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 187, 12)
    
    lastContactTime = property(__lastContactTime.value, __lastContactTime.set, None, '\n                     .Last Contact Time: The time of the last two-way contact between the aircraft and \n                     an ATS unit. The time is given in UTC. \n                  ')

    
    # Attribute lastContactUnit uses Python identifier lastContactUnit
    __lastContactUnit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastContactUnit'), 'lastContactUnit', '__httpwww_fixm_aeroflight3_0_LastContactType_lastContactUnit', _ImportedBinding__ff.AtcUnitNameType)
    __lastContactUnit._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 195, 12)
    __lastContactUnit._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 195, 12)
    
    lastContactUnit = property(__lastContactUnit.value, __lastContactUnit.set, None, '\n                     .Last Contact Unit: The last ATS unit which had two-way contact with the aircraft. \n                     \n                  ')

    _ElementMap.update({
        __contactFrequency.name() : __contactFrequency,
        __position.name() : __position
    })
    _AttributeMap.update({
        __lastContactTime.name() : __lastContactTime,
        __lastContactUnit.name() : __lastContactUnit
    })
_module_typeBindings.LastContactType = LastContactType
Namespace.addCategoryObject('typeBinding', 'LastContactType', LastContactType)


# Complex type {http://www.fixm.aero/flight/3.0}RadioCommunicationFailureType with content type ELEMENT_ONLY
class RadioCommunicationFailureType (_ImportedBinding__fb.FeatureType):
    """
            Groups information regarding loss of radio communication capabilities. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RadioCommunicationFailureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 242, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__httpwww_fixm_aeroflight3_0_RadioCommunicationFailureType_contact', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 251, 15), )

    
    contact = property(__contact.value, __contact.set, None, '\n                        .Last Contact Unit: The last ATS unit which had two-way contact with the aircraft. \n                        \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute radioFailureRemarks uses Python identifier radioFailureRemarks
    __radioFailureRemarks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radioFailureRemarks'), 'radioFailureRemarks', '__httpwww_fixm_aeroflight3_0_RadioCommunicationFailureType_radioFailureRemarks', _ImportedBinding__fb.FreeTextType)
    __radioFailureRemarks._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 260, 12)
    __radioFailureRemarks._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 260, 12)
    
    radioFailureRemarks = property(__radioFailureRemarks.value, __radioFailureRemarks.set, None, '\n                     .Radio Failure Remarks: Pertinent information needed to notify appropriate organizations \n                     regarding loss of radio communication capabilities. \n                  ')

    
    # Attribute remainingComCapability uses Python identifier remainingComCapability
    __remainingComCapability = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'remainingComCapability'), 'remainingComCapability', '__httpwww_fixm_aeroflight3_0_RadioCommunicationFailureType_remainingComCapability', _ImportedBinding__fb.FreeTextType)
    __remainingComCapability._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 268, 12)
    __remainingComCapability._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 268, 12)
    
    remainingComCapability = property(__remainingComCapability.value, __remainingComCapability.set, None, '\n                     .Remaining Communication Capabilities: The remaining communication capability of \n                     the aircraft following radio failure. \n                  ')

    _ElementMap.update({
        __contact.name() : __contact
    })
    _AttributeMap.update({
        __radioFailureRemarks.name() : __radioFailureRemarks,
        __remainingComCapability.name() : __remainingComCapability
    })
_module_typeBindings.RadioCommunicationFailureType = RadioCommunicationFailureType
Namespace.addCategoryObject('typeBinding', 'RadioCommunicationFailureType', RadioCommunicationFailureType)


# Complex type {http://www.fixm.aero/flight/3.0}FlightType with content type ELEMENT_ONLY
class FlightType (_ImportedBinding__fb.FeatureType):
    """
            Central object of the FIXM Logical Model. Groups all information about the flight. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 140, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element agreed uses Python identifier agreed
    __agreed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'agreed'), 'agreed', '__httpwww_fixm_aeroflight3_0_FlightType_agreed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 150, 15), )

    
    agreed = property(__agreed.value, __agreed.set, None, '\n                        .Route - Agreed To: The route of flight agreed to by the Airspace User and the Airspace \n                        Provider.  This route is amended as the flight progresses. \n                        .Agreed 4D Trajectory: This trajectory expresses the 4D trajectory agreed to between \n                        the airspace user and the airspace navigation service providers (ANSP) after collaboration \n                        or imposition of pre-collaborated rules. \n                     ')

    
    # Element aircraftDescription uses Python identifier aircraftDescription
    __aircraftDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aircraftDescription'), 'aircraftDescription', '__httpwww_fixm_aeroflight3_0_FlightType_aircraftDescription', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 161, 15), )

    
    aircraftDescription = property(__aircraftDescription.value, __aircraftDescription.set, None, '\n                        Describes the details of the aircraft used in the flight. \n                     ')

    
    # Element arrival uses Python identifier arrival
    __arrival = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrival'), 'arrival', '__httpwww_fixm_aeroflight3_0_FlightType_arrival', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 168, 15), )

    
    arrival = property(__arrival.value, __arrival.set, None, '\n                        Contains flight arrival information \n                     ')

    
    # Element controllingUnit uses Python identifier controllingUnit
    __controllingUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'controllingUnit'), 'controllingUnit', '__httpwww_fixm_aeroflight3_0_FlightType_controllingUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 175, 15), )

    
    controllingUnit = property(__controllingUnit.value, __controllingUnit.set, None, '\n                        .Controlling Unit: The identifier of the Air Traffic Control unit in control of the \n                        aircraft. \n                        .Controlling Sector: Identifies the ATC sector in control of the aircraft. \n                     ')

    
    # Element dangerousGoods uses Python identifier dangerousGoods
    __dangerousGoods = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dangerousGoods'), 'dangerousGoods', '__httpwww_fixm_aeroflight3_0_FlightType_dangerousGoods', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 184, 15), )

    
    dangerousGoods = property(__dangerousGoods.value, __dangerousGoods.set, None, '\n                        Contains information about any board dangerous goods \n                     ')

    
    # Element departure uses Python identifier departure
    __departure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'departure'), 'departure', '__httpwww_fixm_aeroflight3_0_FlightType_departure', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 191, 15), )

    
    departure = property(__departure.value, __departure.set, None, '\n                        Contains flight departure information \n                     ')

    
    # Element emergency uses Python identifier emergency
    __emergency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emergency'), 'emergency', '__httpwww_fixm_aeroflight3_0_FlightType_emergency', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 198, 15), )

    
    emergency = property(__emergency.value, __emergency.set, None, '\n                        Contains flight emergency linformation \n                     ')

    
    # Element enRoute uses Python identifier enRoute
    __enRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'enRoute'), 'enRoute', '__httpwww_fixm_aeroflight3_0_FlightType_enRoute', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 205, 15), )

    
    enRoute = property(__enRoute.value, __enRoute.set, None, '\n                        Groups the en route information about the flight such as the current position, coordination \n                        between air traffic units, and boundary crossing throughout the duration of the flight. \n                        \n                     ')

    
    # Element enRouteDiversion uses Python identifier enRouteDiversion
    __enRouteDiversion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'enRouteDiversion'), 'enRouteDiversion', '__httpwww_fixm_aeroflight3_0_FlightType_enRouteDiversion', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 214, 15), )

    
    enRouteDiversion = property(__enRouteDiversion.value, __enRouteDiversion.set, None, '\n                        Contains information about the En Route Diversion of the flight such as diversion \n                        recovery. \n                     ')

    
    # Element extensions uses Python identifier extensions
    __extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'extensions'), 'extensions', '__httpwww_fixm_aeroflight3_0_FlightType_extensions', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 222, 15), )

    
    extensions = property(__extensions.value, __extensions.set, None, '\n                        Allow to add or redefine the core FIXM elements and create regional scope extensions \n                        such as NAS extension or Eurocontrol extension. This approach is not recommended, \n                        however as the preferred method is to extend individual classes and replace the core \n                        classes where appropriate as described in the FIXM Modeling Best Practices Guide. \n                        \n                     ')

    
    # Element flightIdentification uses Python identifier flightIdentification
    __flightIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flightIdentification'), 'flightIdentification', '__httpwww_fixm_aeroflight3_0_FlightType_flightIdentification', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 233, 15), )

    
    flightIdentification = property(__flightIdentification.value, __flightIdentification.set, None, '\n                        Groups flight identifying information. \n                     ')

    
    # Element flightStatus uses Python identifier flightStatus
    __flightStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flightStatus'), 'flightStatus', '__httpwww_fixm_aeroflight3_0_FlightType_flightStatus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 240, 15), )

    
    flightStatus = property(__flightStatus.value, __flightStatus.set, None, '\n                        Flight Status of the flight containing a set of indicators of the current flight \n                        status. \n                        .Flight Status: Identification of the aspect of the flight life cycle. \n                     ')

    
    # Element gufi uses Python identifier gufi
    __gufi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gufi'), 'gufi', '__httpwww_fixm_aeroflight3_0_FlightType_gufi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 249, 15), )

    
    gufi = property(__gufi.value, __gufi.set, None, '\n                        .Globally Unique Flight Identifier: A reference that uniquely identifies a specific \n                        flight and is independent of any particular system. \n                     ')

    
    # Element negotiating uses Python identifier negotiating
    __negotiating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'negotiating'), 'negotiating', '__httpwww_fixm_aeroflight3_0_FlightType_negotiating', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 257, 15), )

    
    negotiating = property(__negotiating.value, __negotiating.set, None, '\n                        .Negotiating 4D Trajectory: The 4D Trajectory used during the collaboration between \n                        the airspace user and the airspace provider to agree on a 4D trajectory. This trajectory \n                        is intended to be transitory. \n                        .Negotiating Route: This Route is used during collaboration between the airspace \n                        user and the airspace providers to agree on a route.  This route field is intended \n                        to be transitory. \n                     ')

    
    # Element operator uses Python identifier operator
    __operator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'operator'), 'operator', '__httpwww_fixm_aeroflight3_0_FlightType_operator', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 269, 15), )

    
    operator = property(__operator.value, __operator.set, None, '\n                        Contains information about the identify of aircraft operator. \n                     ')

    
    # Element originator uses Python identifier originator
    __originator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'originator'), 'originator', '__httpwww_fixm_aeroflight3_0_FlightType_originator', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 276, 15), )

    
    originator = property(__originator.value, __originator.set, None, '\n                        Contains information about the flight originator that initiated the flight. \n                     ')

    
    # Element radioCommunicationFailure uses Python identifier radioCommunicationFailure
    __radioCommunicationFailure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radioCommunicationFailure'), 'radioCommunicationFailure', '__httpwww_fixm_aeroflight3_0_FlightType_radioCommunicationFailure', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 283, 15), )

    
    radioCommunicationFailure = property(__radioCommunicationFailure.value, __radioCommunicationFailure.set, None, '\n                        Contains information about radio communication failure \n                     ')

    
    # Element rankedTrajectories uses Python identifier rankedTrajectories
    __rankedTrajectories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rankedTrajectories'), 'rankedTrajectories', '__httpwww_fixm_aeroflight3_0_FlightType_rankedTrajectories', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 290, 15), )

    
    rankedTrajectories = property(__rankedTrajectories.value, __rankedTrajectories.set, None, '\n                        Ranked Trajectories associated with the flight. \n                     ')

    
    # Element routeToRevisedDestination uses Python identifier routeToRevisedDestination
    __routeToRevisedDestination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routeToRevisedDestination'), 'routeToRevisedDestination', '__httpwww_fixm_aeroflight3_0_FlightType_routeToRevisedDestination', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 297, 15), )

    
    routeToRevisedDestination = property(__routeToRevisedDestination.value, __routeToRevisedDestination.set, None, '\n                        .Route - Revised Destination: The route (from some point on the filed route) to the \n                        revised destination aerodrome. \n                     ')

    
    # Element specialHandling uses Python identifier specialHandling
    __specialHandling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specialHandling'), 'specialHandling', '__httpwww_fixm_aeroflight3_0_FlightType_specialHandling', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 305, 15), )

    
    specialHandling = property(__specialHandling.value, __specialHandling.set, None, '\n                        .Special Handling Reason: A property of the flight that requires ATS units to give \n                        it special consideration. \n                     ')

    
    # Element supplementalData uses Python identifier supplementalData
    __supplementalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'supplementalData'), 'supplementalData', '__httpwww_fixm_aeroflight3_0_FlightType_supplementalData', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 316, 15), )

    
    supplementalData = property(__supplementalData.value, __supplementalData.set, None, '\n                        Contains the supplemental data about the flight. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute flightFiler uses Python identifier flightFiler
    __flightFiler = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'flightFiler'), 'flightFiler', '__httpwww_fixm_aeroflight3_0_FlightType_flightFiler', _ImportedBinding__fb.FreeTextType)
    __flightFiler._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 324, 12)
    __flightFiler._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 324, 12)
    
    flightFiler = property(__flightFiler.value, __flightFiler.set, None, '\n                     .Flight Information Filer: The name of the unit, agency or person filing the flight \n                     plan. \n                  ')

    
    # Attribute flightType uses Python identifier flightType
    __flightType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'flightType'), 'flightType', '__httpwww_fixm_aeroflight3_0_FlightType_flightType', _module_typeBindings.TypeOfFlightType)
    __flightType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 332, 12)
    __flightType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 332, 12)
    
    flightType = property(__flightType.value, __flightType.set, None, '\n                     .Flight Type: Indication of the rule under which an air traffic controller provides \n                     categorical handling of a flight. \n                  ')

    
    # Attribute remarks uses Python identifier remarks
    __remarks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'remarks'), 'remarks', '__httpwww_fixm_aeroflight3_0_FlightType_remarks', _ImportedBinding__fb.FreeTextType)
    __remarks._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 340, 12)
    __remarks._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 340, 12)
    
    remarks = property(__remarks.value, __remarks.set, None, '\n                     .Remarks: Plain language remarks providing additional information about the flight \n                     (e.g., requested flight level changes after takeoff). \n                  ')

    _ElementMap.update({
        __agreed.name() : __agreed,
        __aircraftDescription.name() : __aircraftDescription,
        __arrival.name() : __arrival,
        __controllingUnit.name() : __controllingUnit,
        __dangerousGoods.name() : __dangerousGoods,
        __departure.name() : __departure,
        __emergency.name() : __emergency,
        __enRoute.name() : __enRoute,
        __enRouteDiversion.name() : __enRouteDiversion,
        __extensions.name() : __extensions,
        __flightIdentification.name() : __flightIdentification,
        __flightStatus.name() : __flightStatus,
        __gufi.name() : __gufi,
        __negotiating.name() : __negotiating,
        __operator.name() : __operator,
        __originator.name() : __originator,
        __radioCommunicationFailure.name() : __radioCommunicationFailure,
        __rankedTrajectories.name() : __rankedTrajectories,
        __routeToRevisedDestination.name() : __routeToRevisedDestination,
        __specialHandling.name() : __specialHandling,
        __supplementalData.name() : __supplementalData
    })
    _AttributeMap.update({
        __flightFiler.name() : __flightFiler,
        __flightType.name() : __flightType,
        __remarks.name() : __remarks
    })
_module_typeBindings.FlightType = FlightType
Namespace.addCategoryObject('typeBinding', 'FlightType', FlightType)


# Complex type {http://www.fixm.aero/flight/3.0}RankedTrajectoryType with content type ELEMENT_ONLY
class RankedTrajectoryType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Ranked 4D Route: This is the route associated with a single Ranked 4D trajectory 
            for a flight.  It indicates the intent of the flight and includes the path over the 
            surface of the earth, the altitude and the speed for the flight. 
            .Ranked 4D Trajectory: A series of desired 4D trajectories, with tolerances supplied 
            if necessary by the airspace user to define when the next ranked trajectory should 
            be used. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RankedTrajectoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 91, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element routeTrajectoryPair uses Python identifier routeTrajectoryPair
    __routeTrajectoryPair = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routeTrajectoryPair'), 'routeTrajectoryPair', '__httpwww_fixm_aeroflight3_0_RankedTrajectoryType_routeTrajectoryPair', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 103, 9), )

    
    routeTrajectoryPair = property(__routeTrajectoryPair.value, __routeTrajectoryPair.set, None, '\n                  Route Trajectory pair that is the subject of the Trajectory option. \n               ')

    
    # Attribute assignedIndicator uses Python identifier assignedIndicator
    __assignedIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'assignedIndicator'), 'assignedIndicator', '__httpwww_fixm_aeroflight3_0_RankedTrajectoryType_assignedIndicator', _module_typeBindings.AssignedIndicatorType)
    __assignedIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 111, 6)
    __assignedIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 111, 6)
    
    assignedIndicator = property(__assignedIndicator.value, __assignedIndicator.set, None, '\n               .Ranked 4D Trajectory Assignment Status: An indication whether the Ranked 4D trajectory \n               has been assigned by the Air Navigation Service Provider (ANSP). \n            ')

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_fixm_aeroflight3_0_RankedTrajectoryType_identifier', _module_typeBindings.STD_ANON_19)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 119, 6)
    __identifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 119, 6)
    
    identifier = property(__identifier.value, __identifier.set, None, '\n               Unique Identifier used to differentiate the 4D trajectories. \n               .Ranked 4D Trajectory Identifier: Unique Identifier used to differentiate the 4D \n               trajectories. \n            ')

    
    # Attribute maximumAcceptableDelay uses Python identifier maximumAcceptableDelay
    __maximumAcceptableDelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maximumAcceptableDelay'), 'maximumAcceptableDelay', '__httpwww_fixm_aeroflight3_0_RankedTrajectoryType_maximumAcceptableDelay', _ImportedBinding__fb.CountType)
    __maximumAcceptableDelay._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 133, 6)
    __maximumAcceptableDelay._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 133, 6)
    
    maximumAcceptableDelay = property(__maximumAcceptableDelay.value, __maximumAcceptableDelay.set, None, '\n               .Ranked 4D Trajectory Maximum Acceptable Delay: The maximum acceptable delay the \n               flight could incur for the Ranked 4D trajectory, if this were the assigned 4D trajectory. \n               \n            ')

    _ElementMap.update({
        __routeTrajectoryPair.name() : __routeTrajectoryPair
    })
    _AttributeMap.update({
        __assignedIndicator.name() : __assignedIndicator,
        __identifier.name() : __identifier,
        __maximumAcceptableDelay.name() : __maximumAcceptableDelay
    })
_module_typeBindings.RankedTrajectoryType = RankedTrajectoryType
Namespace.addCategoryObject('typeBinding', 'RankedTrajectoryType', RankedTrajectoryType)


# Complex type {http://www.fixm.aero/flight/3.0}ExpandedRoutePointType with content type ELEMENT_ONLY
class ExpandedRoutePointType (AbstractRoutePointType):
    """
            .Expanded Route Point: A point that is part of the aircraft's expanded route of flight. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpandedRoutePointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 229, 3)
    _ElementMap = AbstractRoutePointType._ElementMap.copy()
    _AttributeMap = AbstractRoutePointType._AttributeMap.copy()
    # Base type is AbstractRoutePointType
    
    # Element point (point) inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Element constraint uses Python identifier constraint
    __constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constraint'), 'constraint', '__httpwww_fixm_aeroflight3_0_ExpandedRoutePointType_constraint', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 239, 15), )

    
    constraint = property(__constraint.value, __constraint.set, None, '\n                        An Expanded route point may contain an ordered list of constraints. \n                     ')

    
    # Element estimatedLevel uses Python identifier estimatedLevel
    __estimatedLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'estimatedLevel'), 'estimatedLevel', '__httpwww_fixm_aeroflight3_0_ExpandedRoutePointType_estimatedLevel', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 246, 15), )

    
    estimatedLevel = property(__estimatedLevel.value, __estimatedLevel.set, None, '\n                        .Expanded Route Point Altitude: The estimated altitude over the expanded route point. \n                        \n                     ')

    
    # Attribute airTrafficType inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute clearanceLimit inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute delayAtPoint inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute flightRules inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute estimatedTime uses Python identifier estimatedTime
    __estimatedTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'estimatedTime'), 'estimatedTime', '__httpwww_fixm_aeroflight3_0_ExpandedRoutePointType_estimatedTime', _ImportedBinding__ff.TimeType)
    __estimatedTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 255, 12)
    __estimatedTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 255, 12)
    
    estimatedTime = property(__estimatedTime.value, __estimatedTime.set, None, '\n                     .Expanded Route Point Time: The estimated time over the expanded route point. \n                  ')

    _ElementMap.update({
        __constraint.name() : __constraint,
        __estimatedLevel.name() : __estimatedLevel
    })
    _AttributeMap.update({
        __estimatedTime.name() : __estimatedTime
    })
_module_typeBindings.ExpandedRoutePointType = ExpandedRoutePointType
Namespace.addCategoryObject('typeBinding', 'ExpandedRoutePointType', ExpandedRoutePointType)


# Complex type {http://www.fixm.aero/flight/3.0}RouteType with content type ELEMENT_ONLY
class RouteType (_ImportedBinding__fb.FeatureType):
    """
            Contains information about the Flight Route. The route is comprised of Route Segments, 
            which are comprised of Route Point/Airway pairs. Route also contains an expanded 
            route. 
            .Route: The ICAO route string as depicted from the flight plan. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 267, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Element climbSchedule uses Python identifier climbSchedule
    __climbSchedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'climbSchedule'), 'climbSchedule', '__httpwww_fixm_aeroflight3_0_RouteType_climbSchedule', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 279, 15), )

    
    climbSchedule = property(__climbSchedule.value, __climbSchedule.set, None, '\n                        .Speed Schedule - Climb: Initially submitted by the airspace user, this defines the \n                        target speed in both Initial Airspeed (IAS) and MACH so the aircraft can climb through \n                        the crossover altitude and target the MACH speed when needed. \n                     ')

    
    # Element descentSchedule uses Python identifier descentSchedule
    __descentSchedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'descentSchedule'), 'descentSchedule', '__httpwww_fixm_aeroflight3_0_RouteType_descentSchedule', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 288, 15), )

    
    descentSchedule = property(__descentSchedule.value, __descentSchedule.set, None, '\n                        .Speed Schedule - Descent: Initially submitted by the airspace user, this defines \n                        the target speed in both IAS and MACH so the aircraft can descend through the crossover \n                        altitude and target the Initial Airspeed (IAS) speed when needed. \n                     ')

    
    # Element estimatedElapsedTime uses Python identifier estimatedElapsedTime
    __estimatedElapsedTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'estimatedElapsedTime'), 'estimatedElapsedTime', '__httpwww_fixm_aeroflight3_0_RouteType_estimatedElapsedTime', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 297, 15), )

    
    estimatedElapsedTime = property(__estimatedElapsedTime.value, __estimatedElapsedTime.set, None, '\n                        .Elapsed Time - Estimated: The estimated amount of time from takeoff to reach a significant \n                        point or Flight Information Region (FIR) boundary along the route of flight. \n                     ')

    
    # Element expandedRoute uses Python identifier expandedRoute
    __expandedRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'expandedRoute'), 'expandedRoute', '__httpwww_fixm_aeroflight3_0_RouteType_expandedRoute', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 305, 15), )

    
    expandedRoute = property(__expandedRoute.value, __expandedRoute.set, None, "\n                        A route may contain an optional expanded route where the route consisting of expanded \n                        route points. \n                        .Expanded Route: The expansion of the route into a set of points which describe the \n                        aircraft's expected 2D path from the departure aerodrome to the destination aerodrome. \n                        \n                     ")

    
    # Element initialCruisingSpeed uses Python identifier initialCruisingSpeed
    __initialCruisingSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'initialCruisingSpeed'), 'initialCruisingSpeed', '__httpwww_fixm_aeroflight3_0_RouteType_initialCruisingSpeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 316, 15), )

    
    initialCruisingSpeed = property(__initialCruisingSpeed.value, __initialCruisingSpeed.set, None, '\n                        .Cruising Speed: The true airspeed for the first or the whole cruising portion of \n                        the flight.  This can be for a filed flight or an active flight.  This element is \n                        strategic in nature. \n                     ')

    
    # Element requestedAltitude uses Python identifier requestedAltitude
    __requestedAltitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'requestedAltitude'), 'requestedAltitude', '__httpwww_fixm_aeroflight3_0_RouteType_requestedAltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 325, 15), )

    
    requestedAltitude = property(__requestedAltitude.value, __requestedAltitude.set, None, '\n                        .Cruising Altitude - Requested: The filed altitude (flight level) for the first or \n                        the whole cruising portion of the flight. \n                     ')

    
    # Element segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'segment'), 'segment', '__httpwww_fixm_aeroflight3_0_RouteType_segment', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 333, 15), )

    
    segment = property(__segment.value, __segment.set, None, '\n                        Route consists of an optional ordered list of route segments. \n                     ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute airfileRouteStartTime uses Python identifier airfileRouteStartTime
    __airfileRouteStartTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airfileRouteStartTime'), 'airfileRouteStartTime', '__httpwww_fixm_aeroflight3_0_RouteType_airfileRouteStartTime', _ImportedBinding__ff.TimeType)
    __airfileRouteStartTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 341, 12)
    __airfileRouteStartTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 341, 12)
    
    airfileRouteStartTime = property(__airfileRouteStartTime.value, __airfileRouteStartTime.set, None, '\n                     .Airfile Route Start Time: The actual or estimated time of departure from the first \n                     point on the route for a flight filed in the air. \n                  ')

    
    # Attribute flightDuration uses Python identifier flightDuration
    __flightDuration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'flightDuration'), 'flightDuration', '__httpwww_fixm_aeroflight3_0_RouteType_flightDuration', _ImportedBinding__ff.DurationType)
    __flightDuration._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 349, 12)
    __flightDuration._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 349, 12)
    
    flightDuration = property(__flightDuration.value, __flightDuration.set, None, '\n                     .Time En Route - Estimated: The total estimated time en route, from the departure \n                     time (runway) to the arrival at the destination (runway).  For an airfile flight, \n                     this is the total estimated time en route, from the route start point to the arrival \n                     at the destination (runway). \n                  ')

    
    # Attribute initialFlightRules uses Python identifier initialFlightRules
    __initialFlightRules = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'initialFlightRules'), 'initialFlightRules', '__httpwww_fixm_aeroflight3_0_RouteType_initialFlightRules', _ImportedBinding__fb.FlightRulesType)
    __initialFlightRules._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 359, 12)
    __initialFlightRules._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 359, 12)
    
    initialFlightRules = property(__initialFlightRules.value, __initialFlightRules.set, None, '\n                     .Flight Rules: The regulation, or combination of regulations, that governs all aspects \n                     of operations under which the pilot plans to fly. \n                  ')

    
    # Attribute routeText uses Python identifier routeText
    __routeText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'routeText'), 'routeText', '__httpwww_fixm_aeroflight3_0_RouteType_routeText', _ImportedBinding__fb.FreeTextType)
    __routeText._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 367, 12)
    __routeText._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 367, 12)
    
    routeText = property(__routeText.value, __routeText.set, None, '\n                     .Route String: The ICAO route string as depicted from the flight plan. \n                  ')

    _ElementMap.update({
        __climbSchedule.name() : __climbSchedule,
        __descentSchedule.name() : __descentSchedule,
        __estimatedElapsedTime.name() : __estimatedElapsedTime,
        __expandedRoute.name() : __expandedRoute,
        __initialCruisingSpeed.name() : __initialCruisingSpeed,
        __requestedAltitude.name() : __requestedAltitude,
        __segment.name() : __segment
    })
    _AttributeMap.update({
        __airfileRouteStartTime.name() : __airfileRouteStartTime,
        __flightDuration.name() : __flightDuration,
        __initialFlightRules.name() : __initialFlightRules,
        __routeText.name() : __routeText
    })
_module_typeBindings.RouteType = RouteType
Namespace.addCategoryObject('typeBinding', 'RouteType', RouteType)


# Complex type {http://www.fixm.aero/flight/3.0}RoutePointType with content type ELEMENT_ONLY
class RoutePointType (AbstractRoutePointType):
    """
            Route point along a route of the flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoutePointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 379, 3)
    _ElementMap = AbstractRoutePointType._ElementMap.copy()
    _AttributeMap = AbstractRoutePointType._AttributeMap.copy()
    # Base type is AbstractRoutePointType
    
    # Element point (point) inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Element constraint uses Python identifier constraint
    __constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constraint'), 'constraint', '__httpwww_fixm_aeroflight3_0_RoutePointType_constraint', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 388, 15), )

    
    constraint = property(__constraint.value, __constraint.set, None, '\n                        A Route point may contain an ordered list of constraints. \n                     ')

    
    # Attribute airTrafficType inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute clearanceLimit inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute delayAtPoint inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute flightRules inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    _ElementMap.update({
        __constraint.name() : __constraint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RoutePointType = RoutePointType
Namespace.addCategoryObject('typeBinding', 'RoutePointType', RoutePointType)


# Complex type {http://www.fixm.aero/flight/3.0}FlightStatusType with content type EMPTY
class FlightStatusType (_ImportedBinding__fb.FeatureType):
    """
            .Flight Status: Identification of the aspect of the flight life cycle. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 142, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute accepted uses Python identifier accepted
    __accepted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accepted'), 'accepted', '__httpwww_fixm_aeroflight3_0_FlightStatusType_accepted', _module_typeBindings.FlightAcceptedIndicatorType)
    __accepted._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 150, 12)
    __accepted._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 150, 12)
    
    accepted = property(__accepted.value, __accepted.set, None, '\n                     .Flight Plan Accepted Indicator: An indicator of acceptance of the flight plan by \n                     the appropriate ATS authority. \n                  ')

    
    # Attribute airborneHold uses Python identifier airborneHold
    __airborneHold = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airborneHold'), 'airborneHold', '__httpwww_fixm_aeroflight3_0_FlightStatusType_airborneHold', _module_typeBindings.AirborneHoldIndicatorType)
    __airborneHold._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 158, 12)
    __airborneHold._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 158, 12)
    
    airborneHold = property(__airborneHold.value, __airborneHold.set, None, '\n                     .Hold State - Airborne Indicator: Specifies whether or not the aircraft is in an \n                     airborne hold. \n                  ')

    
    # Attribute airfile uses Python identifier airfile
    __airfile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'airfile'), 'airfile', '__httpwww_fixm_aeroflight3_0_FlightStatusType_airfile', _module_typeBindings.AirfileIndicatorType)
    __airfile._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 166, 12)
    __airfile._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 166, 12)
    
    airfile = property(__airfile.value, __airfile.set, None, '\n                     .Airfile Indicator: An indication the information about this flight was filed from \n                     the air. \n                  ')

    
    # Attribute flightCycle uses Python identifier flightCycle
    __flightCycle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'flightCycle'), 'flightCycle', '__httpwww_fixm_aeroflight3_0_FlightStatusType_flightCycle', _module_typeBindings.FlightCycleType)
    __flightCycle._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 174, 12)
    __flightCycle._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 174, 12)
    
    flightCycle = property(__flightCycle.value, __flightCycle.set, None, '\n                     Flight Cycle is contains a mutually exclusive set of values representing stages of \n                     flight. \n                     .Flight Completed Indicator: An indicator that the flight was airborne and is now \n                     completed. \n                     .Flight Cancelled Indicator: Indication the flight has been cancelled after Flight \n                     Object creation. \n                     .Flight Filed Indicator: An indicator that flight information was filed to the appropriate \n                     Air Traffic Services authority. \n                     .Airborne Indicator: An indication of whether the flight is airborne or not. \n                     .Flight Scheduled Indicator: An indicator a flight has been created in the Air Traffic \n                     Services system and is expected to operate. \n                  ')

    
    # Attribute missedApproach uses Python identifier missedApproach
    __missedApproach = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'missedApproach'), 'missedApproach', '__httpwww_fixm_aeroflight3_0_FlightStatusType_missedApproach', _module_typeBindings.MissedApproachIndicatorType)
    __missedApproach._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 191, 12)
    __missedApproach._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 191, 12)
    
    missedApproach = property(__missedApproach.value, __missedApproach.set, None, '\n                     .Missed Approach Indicator: An indicator that a flight executed a missed approach. \n                     \n                  ')

    
    # Attribute suspended uses Python identifier suspended
    __suspended = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'suspended'), 'suspended', '__httpwww_fixm_aeroflight3_0_FlightStatusType_suspended', _module_typeBindings.FlightSuspendedIndicatorType)
    __suspended._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 199, 12)
    __suspended._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 199, 12)
    
    suspended = property(__suspended.value, __suspended.set, None, '\n                     .Flight Suspended Indicator: An indicator a flight has been suspended in the Air \n                     Traffic Services system. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accepted.name() : __accepted,
        __airborneHold.name() : __airborneHold,
        __airfile.name() : __airfile,
        __flightCycle.name() : __flightCycle,
        __missedApproach.name() : __missedApproach,
        __suspended.name() : __suspended
    })
_module_typeBindings.FlightStatusType = FlightStatusType
Namespace.addCategoryObject('typeBinding', 'FlightStatusType', FlightStatusType)


AircraftType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AircraftType'), AircraftTypeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 295, 3))
Namespace.addCategoryObject('elementBinding', AircraftType.name().localName(), AircraftType)

DinghyColour = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DinghyColour'), DinghyColourType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 144, 3))
Namespace.addCategoryObject('elementBinding', DinghyColour.name().localName(), DinghyColour)

AdditionalHandlingInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdditionalHandlingInformation'), AdditionalHandlingInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 100, 3))
Namespace.addCategoryObject('elementBinding', AdditionalHandlingInformation.name().localName(), AdditionalHandlingInformation)

DangerousGoodsDimensions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsDimensions'), DangerousGoodsDimensionsType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 158, 3))
Namespace.addCategoryObject('elementBinding', DangerousGoodsDimensions.name().localName(), DangerousGoodsDimensions)

Temperatures = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Temperatures'), TemperaturesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 589, 3))
Namespace.addCategoryObject('elementBinding', Temperatures.name().localName(), Temperatures)

Handoff = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Handoff'), HandoffType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 271, 3))
Namespace.addCategoryObject('elementBinding', Handoff.name().localName(), Handoff)

BeaconCodeAssignment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BeaconCodeAssignment'), BeaconCodeAssignmentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 165, 3))
Namespace.addCategoryObject('elementBinding', BeaconCodeAssignment.name().localName(), BeaconCodeAssignment)

ClearedFlightInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClearedFlightInformation'), ClearedFlightInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 227, 3))
Namespace.addCategoryObject('elementBinding', ClearedFlightInformation.name().localName(), ClearedFlightInformation)

ControlElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlElement'), ControlElementType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 257, 3))
Namespace.addCategoryObject('elementBinding', ControlElement.name().localName(), ControlElement)

DirectRouting = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DirectRouting'), DirectRoutingType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 284, 3))
Namespace.addCategoryObject('elementBinding', DirectRouting.name().localName(), DirectRouting)

Pointout = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pointout'), PointoutType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 408, 3))
Namespace.addCategoryObject('elementBinding', Pointout.name().localName(), Pointout)

ActualSpeed = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ActualSpeed'), ActualSpeedType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 116, 3))
Namespace.addCategoryObject('elementBinding', ActualSpeed.name().localName(), ActualSpeed)

DepartureActivityTimes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DepartureActivityTimes'), DepartureActivityTimesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 138, 3))
Namespace.addCategoryObject('elementBinding', DepartureActivityTimes.name().localName(), DepartureActivityTimes)

EnRouteDiversion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnRouteDiversion'), EnRouteDiversionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 138, 3))
Namespace.addCategoryObject('elementBinding', EnRouteDiversion.name().localName(), EnRouteDiversion)

Originator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Originator'), OriginatorType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 439, 3))
Namespace.addCategoryObject('elementBinding', Originator.name().localName(), Originator)

ElapsedTimeLocation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElapsedTimeLocation'), ElapsedTimeLocationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 178, 3))
Namespace.addCategoryObject('elementBinding', ElapsedTimeLocation.name().localName(), ElapsedTimeLocation)

ExpandedRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExpandedRoute'), ExpandedRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 227, 3))
Namespace.addCategoryObject('elementBinding', ExpandedRoute.name().localName(), ExpandedRoute)

SpeedSchedule = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpeedSchedule'), SpeedScheduleType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 457, 3))
Namespace.addCategoryObject('elementBinding', SpeedSchedule.name().localName(), SpeedSchedule)

MeteorologicalData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeteorologicalData'), MeteorologicalDataType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 112, 3))
Namespace.addCategoryObject('elementBinding', MeteorologicalData.name().localName(), MeteorologicalData)

PointRange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PointRange'), PointRangeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 193, 3))
Namespace.addCategoryObject('elementBinding', PointRange.name().localName(), PointRange)

Trajectory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Trajectory'), TrajectoryType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 237, 3))
Namespace.addCategoryObject('elementBinding', Trajectory.name().localName(), Trajectory)

TrajectoryPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrajectoryPoint'), TrajectoryPointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 373, 3))
Namespace.addCategoryObject('elementBinding', TrajectoryPoint.name().localName(), TrajectoryPoint)

TrajectoryRoutePair = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrajectoryRoutePair'), TrajectoryRoutePairType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 399, 3))
Namespace.addCategoryObject('elementBinding', TrajectoryRoutePair.name().localName(), TrajectoryRoutePair)

AircraftCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AircraftCapabilities'), AircraftCapabilitiesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 236, 3))
Namespace.addCategoryObject('elementBinding', AircraftCapabilities.name().localName(), AircraftCapabilities)

NavigationCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavigationCapabilities'), NavigationCapabilitiesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 118, 3))
Namespace.addCategoryObject('elementBinding', NavigationCapabilities.name().localName(), NavigationCapabilities)

SurveillanceCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SurveillanceCapabilities'), SurveillanceCapabilitiesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 106, 3))
Namespace.addCategoryObject('elementBinding', SurveillanceCapabilities.name().localName(), SurveillanceCapabilities)

Dinghy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dinghy'), DinghyType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 119, 3))
Namespace.addCategoryObject('elementBinding', Dinghy.name().localName(), Dinghy)

SurvivalCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SurvivalCapabilities'), SurvivalCapabilitiesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 263, 3))
Namespace.addCategoryObject('elementBinding', SurvivalCapabilities.name().localName(), SurvivalCapabilities)

DeclarationText = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeclarationText'), DeclarationTextType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 276, 3))
Namespace.addCategoryObject('elementBinding', DeclarationText.name().localName(), DeclarationText)

ShippingInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShippingInformation'), ShippingInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 435, 3))
Namespace.addCategoryObject('elementBinding', ShippingInformation.name().localName(), ShippingInformation)

DangerousGoodsPackageGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsPackageGroup'), DangerousGoodsPackageGroupType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 416, 3))
Namespace.addCategoryObject('elementBinding', DangerousGoodsPackageGroup.name().localName(), DangerousGoodsPackageGroup)

BoundaryCrossing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundaryCrossing'), BoundaryCrossingType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 203, 3))
Namespace.addCategoryObject('elementBinding', BoundaryCrossing.name().localName(), BoundaryCrossing)

CoordinationStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoordinationStatus'), CoordinationStatusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\CoordinationStatus.xsd', 138, 3))
Namespace.addCategoryObject('elementBinding', CoordinationStatus.name().localName(), CoordinationStatus)

AirspaceConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AirspaceConstraint'), AirspaceConstraintType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 110, 3))
Namespace.addCategoryObject('elementBinding', AirspaceConstraint.name().localName(), AirspaceConstraint)

PlannedReportingPosition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlannedReportingPosition'), PlannedReportingPositionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 246, 3))
Namespace.addCategoryObject('elementBinding', PlannedReportingPosition.name().localName(), PlannedReportingPosition)

RouteConstraintOrPreference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RouteConstraintOrPreference'), RouteConstraintOrPreferenceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 224, 3))
Namespace.addCategoryObject('elementBinding', RouteConstraintOrPreference.name().localName(), RouteConstraintOrPreference)

LastPositionReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LastPositionReport'), LastPositionReportType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 240, 3))
Namespace.addCategoryObject('elementBinding', LastPositionReport.name().localName(), LastPositionReport)

AircraftOperator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AircraftOperator'), AircraftOperatorType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 117, 3))
Namespace.addCategoryObject('elementBinding', AircraftOperator.name().localName(), AircraftOperator)

FlightIdentification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightIdentification'), FlightIdentificationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 390, 3))
Namespace.addCategoryObject('elementBinding', FlightIdentification.name().localName(), FlightIdentification)

SupplementalData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupplementalData'), SupplementalDataType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 497, 3))
Namespace.addCategoryObject('elementBinding', SupplementalData.name().localName(), SupplementalData)

AbstractRoutePoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractRoutePoint'), AbstractRoutePointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 133, 3))
Namespace.addCategoryObject('elementBinding', AbstractRoutePoint.name().localName(), AbstractRoutePoint)

EstimatedElapsedTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EstimatedElapsedTime'), EstimatedElapsedTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 205, 3))
Namespace.addCategoryObject('elementBinding', EstimatedElapsedTime.name().localName(), EstimatedElapsedTime)

RouteSegment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RouteSegment'), RouteSegmentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 425, 3))
Namespace.addCategoryObject('elementBinding', RouteSegment.name().localName(), RouteSegment)

Point4D = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Point4D'), Point4DType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 153, 3))
Namespace.addCategoryObject('elementBinding', Point4D.name().localName(), Point4D)

TemporalRange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemporalRange'), TemporalRangeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 216, 3))
Namespace.addCategoryObject('elementBinding', TemporalRange.name().localName(), TemporalRange)

TrajectoryChange = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrajectoryChange'), TrajectoryChangeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 263, 3))
Namespace.addCategoryObject('elementBinding', TrajectoryChange.name().localName(), TrajectoryChange)

Aircraft = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Aircraft'), AircraftType_, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 171, 3))
Namespace.addCategoryObject('elementBinding', Aircraft.name().localName(), Aircraft)

CommunicationCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommunicationCapabilities'), CommunicationCapabilitiesType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 135, 3))
Namespace.addCategoryObject('elementBinding', CommunicationCapabilities.name().localName(), CommunicationCapabilities)

DangerousGoods = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DangerousGoods'), DangerousGoodsType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 238, 3))
Namespace.addCategoryObject('elementBinding', DangerousGoods.name().localName(), DangerousGoods)

StructuredPostalAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StructuredPostalAddress'), StructuredPostalAddressType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 457, 3))
Namespace.addCategoryObject('elementBinding', StructuredPostalAddress.name().localName(), StructuredPostalAddress)

AllPackedInOne = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllPackedInOne'), AllPackedInOneType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 111, 3))
Namespace.addCategoryObject('elementBinding', AllPackedInOne.name().localName(), AllPackedInOne)

DangerousGoodsPackage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DangerousGoodsPackage'), DangerousGoodsPackageType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 376, 3))
Namespace.addCategoryObject('elementBinding', DangerousGoodsPackage.name().localName(), DangerousGoodsPackage)

RadioactiveMaterial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RadioactiveMaterial'), RadioactiveMaterialType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 185, 3))
Namespace.addCategoryObject('elementBinding', RadioactiveMaterial.name().localName(), RadioactiveMaterial)

Radionuclide = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Radionuclide'), RadionuclideType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 330, 3))
Namespace.addCategoryObject('elementBinding', Radionuclide.name().localName(), Radionuclide)

UnitBoundary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UnitBoundary'), UnitBoundaryType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 344, 3))
Namespace.addCategoryObject('elementBinding', UnitBoundary.name().localName(), UnitBoundary)

CpdlcConnection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CpdlcConnection'), CpdlcConnectionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 147, 3))
Namespace.addCategoryObject('elementBinding', CpdlcConnection.name().localName(), CpdlcConnection)

EnRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnRoute'), EnRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 374, 3))
Namespace.addCategoryObject('elementBinding', EnRoute.name().localName(), EnRoute)

AircraftPosition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AircraftPosition'), AircraftPositionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 202, 3))
Namespace.addCategoryObject('elementBinding', AircraftPosition.name().localName(), AircraftPosition)

FlightArrival = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightArrival'), FlightArrivalType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 250, 3))
Namespace.addCategoryObject('elementBinding', FlightArrival.name().localName(), FlightArrival)

ClimbToLevelConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClimbToLevelConstraint'), ClimbToLevelConstraintType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 136, 3))
Namespace.addCategoryObject('elementBinding', ClimbToLevelConstraint.name().localName(), ClimbToLevelConstraint)

LevelConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LevelConstraint'), LevelConstraintType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 193, 3))
Namespace.addCategoryObject('elementBinding', LevelConstraint.name().localName(), LevelConstraint)

SpeedConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpeedConstraint'), SpeedConstraintType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 265, 3))
Namespace.addCategoryObject('elementBinding', SpeedConstraint.name().localName(), SpeedConstraint)

TimeConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeConstraint'), TimeConstraintType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 297, 3))
Namespace.addCategoryObject('elementBinding', TimeConstraint.name().localName(), TimeConstraint)

FlightDeparture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightDeparture'), FlightDepartureType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 291, 3))
Namespace.addCategoryObject('elementBinding', FlightDeparture.name().localName(), FlightDeparture)

FlightEmergency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightEmergency'), FlightEmergencyType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 158, 3))
Namespace.addCategoryObject('elementBinding', FlightEmergency.name().localName(), FlightEmergency)

LastContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LastContact'), LastContactType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 206, 3))
Namespace.addCategoryObject('elementBinding', LastContact.name().localName(), LastContact)

RadioCommunicationFailure = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RadioCommunicationFailure'), RadioCommunicationFailureType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 279, 3))
Namespace.addCategoryObject('elementBinding', RadioCommunicationFailure.name().localName(), RadioCommunicationFailure)

Flight = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Flight'), FlightType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 351, 3))
Namespace.addCategoryObject('elementBinding', Flight.name().localName(), Flight)

RankedTrajectory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RankedTrajectory'), RankedTrajectoryType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 143, 3))
Namespace.addCategoryObject('elementBinding', RankedTrajectory.name().localName(), RankedTrajectory)

ExpandedRoutePoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExpandedRoutePoint'), ExpandedRoutePointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 265, 3))
Namespace.addCategoryObject('elementBinding', ExpandedRoutePoint.name().localName(), ExpandedRoutePoint)

Route = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Route'), RouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 377, 3))
Namespace.addCategoryObject('elementBinding', Route.name().localName(), Route)

RoutePoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RoutePoint'), RoutePointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 399, 3))
Namespace.addCategoryObject('elementBinding', RoutePoint.name().localName(), RoutePoint)

FlightStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightStatus'), FlightStatusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Status.xsd', 210, 3))
Namespace.addCategoryObject('elementBinding', FlightStatus.name().localName(), FlightStatus)



AircraftTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'icaoModelIdentifier'), _ImportedBinding__fb.IcaoAircraftIdentifierType, scope=AircraftTypeType, documentation='\n                  The ICAO code of the aircraft type \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 279, 9)))

AircraftTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'otherModelData'), _ImportedBinding__fb.FreeTextType, scope=AircraftTypeType, documentation='\n                  Other, non-ICAO identification of the aircraft type. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 286, 9)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 279, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 286, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AircraftTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'icaoModelIdentifier')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 279, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AircraftTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'otherModelData')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 286, 9))
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
AircraftTypeType._Automaton = _BuildAutomaton()




DinghyColourType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'colourCode'), DinghyColourCodeType, scope=DinghyColourType, documentation='\n                  .Dinghy Color: The color of the dinghies carried by the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 128, 9)))

DinghyColourType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'otherColour'), _ImportedBinding__fb.FreeTextType, scope=DinghyColourType, documentation='\n                  Any other color of the dinghy that is not among the standards set. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 135, 9)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 128, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 135, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DinghyColourType._UseForTag(pyxb.namespace.ExpandedName(None, 'colourCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 128, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DinghyColourType._UseForTag(pyxb.namespace.ExpandedName(None, 'otherColour')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 135, 9))
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
DinghyColourType._Automaton = _BuildAutomaton_()




AdditionalHandlingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'responsibleAgent'), _ImportedBinding__ff.PersonOrOrganizationType, scope=AdditionalHandlingInformationType, documentation='\n                  Person or organization responsible for infectious substances. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 91, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 91, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalHandlingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'responsibleAgent')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 91, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalHandlingInformationType._Automaton = _BuildAutomaton_2()




DangerousGoodsDimensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'grossWeight'), _ImportedBinding__ff.WeightType, scope=DangerousGoodsDimensionsType, documentation='\n                  .Dangerous Goods Gross Weight: The total gross weight of dangerous goods transported \n                  for each unique UN number. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 132, 9)))

DangerousGoodsDimensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'netWeight'), _ImportedBinding__ff.WeightType, scope=DangerousGoodsDimensionsType, documentation='\n                  .Dangerous Goods Net Weight: The total net weight of dangerous goods transported \n                  for each unique UN number. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 140, 9)))

DangerousGoodsDimensionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'volume'), _ImportedBinding__ff.VolumeType, scope=DangerousGoodsDimensionsType, documentation='\n                  .Dangerous Goods Volume: The total displacement of dangerous goods transported for \n                  each unique UN number. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 148, 9)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 132, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 140, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 148, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsDimensionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'grossWeight')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 132, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsDimensionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'netWeight')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 140, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsDimensionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'volume')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 148, 9))
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
DangerousGoodsDimensionsType._Automaton = _BuildAutomaton_3()




TemperaturesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'controlTemperature'), _ImportedBinding__ff.TemperatureType, scope=TemperaturesType, documentation='\n                  .Control Temperature: The maximum temperature at which the substance can be safely \n                  transported. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 563, 9)))

TemperaturesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emergencyTemperature'), _ImportedBinding__ff.TemperatureType, scope=TemperaturesType, documentation='\n                  .Emergency Temperature: The temperature at which emergency procedures shall be implemented \n                  in the event of loss of temperature control. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 571, 9)))

TemperaturesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flashpointTemperature'), _ImportedBinding__ff.TemperatureType, scope=TemperaturesType, documentation='\n                  The lowest temperature at which it can vaporize to form an ignitable mixture in air. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 579, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 563, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 571, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 579, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TemperaturesType._UseForTag(pyxb.namespace.ExpandedName(None, 'controlTemperature')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 563, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TemperaturesType._UseForTag(pyxb.namespace.ExpandedName(None, 'emergencyTemperature')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 571, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TemperaturesType._UseForTag(pyxb.namespace.ExpandedName(None, 'flashpointTemperature')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 579, 9))
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
TemperaturesType._Automaton = _BuildAutomaton_4()




HandoffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'coordinationStatus'), CoordinationStatusType, scope=HandoffType, documentation='\n                  .Coordination Status: The status of Coordination and Transfer of Control between \n                  the currently Controlling Air Traffic Service Unit (ATSU) to the downstream to be \n                  Controlling ATSU. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 240, 9)))

HandoffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'receivingUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=HandoffType, documentation='\n                  .Handoff Receiving Sector: Identifies the ATC sector receiving control of the aircraft \n                  as a result of a handoff. \n                  .Handoff Receiving Unit: The Air Traffic Control unit receiving control of the aircraft \n                  as a result of a handoff. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 249, 9)))

HandoffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transferringUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=HandoffType, documentation='\n                  .Handoff Transferring Unit: The Air Traffic Control unit transferring control of \n                  the aircraft as a result of a handoff. \n                  .Handoff Transferring Sector: Identifies the ATC sector transferring control of the \n                  aircraft as a result of a handoff. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 259, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 240, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 249, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 259, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'coordinationStatus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 240, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(HandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'receivingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 249, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(HandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'transferringUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 259, 9))
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
HandoffType._Automaton = _BuildAutomaton_5()




BeaconCodeAssignmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'currentBeaconCode'), _ImportedBinding__fb.BeaconCodeType, scope=BeaconCodeAssignmentType, documentation='\n                  Current assigned beacon code. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 123, 9)))

BeaconCodeAssignmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'previousBeaconCode'), _ImportedBinding__fb.BeaconCodeType, scope=BeaconCodeAssignmentType, documentation="\n                  .Previous SSR Mode and Beacon Code: The Secondary surveillance radar (SSR) mode and \n                  code the flight was transponding before the current SSR Mode and Code. \n                  .Reassigned SSR Mode and Beacon Code: The Secondary Surveillance Radar (SSR) mode \n                  and beacon code assigned to the flight in the downstream facility, if the flight's \n                  current beacon code is already in use by another flight in that facility. The next \n                  beacon code differs from the flight's current beacon code. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 130, 9)))

BeaconCodeAssignmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reassignedBeaconCode'), _ImportedBinding__fb.BeaconCodeType, nillable=pyxb.binding.datatypes.boolean(1), scope=BeaconCodeAssignmentType, documentation="\n                  .Previous SSR Mode and Beacon Code: The Secondary surveillance radar (SSR) mode and \n                  code the flight was transponding before the current SSR Mode and Code. \n                  .Reassigned SSR Mode and Beacon Code: The Secondary Surveillance Radar (SSR) mode \n                  and beacon code assigned to the flight in the downstream facility, if the flight's \n                  current beacon code is already in use by another flight in that facility. The next \n                  beacon code differs from the flight's current beacon code. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 142, 9)))

BeaconCodeAssignmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reassigningUnit'), _ImportedBinding__fb.AtcUnitReferenceType, nillable=pyxb.binding.datatypes.boolean(1), scope=BeaconCodeAssignmentType, documentation='\n                  .Reassigned Beacon Code Unit: Identifies the downstream unit that assigned the next \n                  beacon code, in the case the beacon code was already in use by another flight at \n                  the downstream unit. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 154, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 123, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 130, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 142, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 154, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BeaconCodeAssignmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'currentBeaconCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 123, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BeaconCodeAssignmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'previousBeaconCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 130, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BeaconCodeAssignmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'reassignedBeaconCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 142, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BeaconCodeAssignmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'reassigningUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 154, 9))
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
BeaconCodeAssignmentType._Automaton = _BuildAutomaton_6()




ClearedFlightInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'clearedFlightLevel'), _ImportedBinding__fb.AltitudeChoiceType, scope=ClearedFlightInformationType, documentation='\n                  .Cleared Flight Level: The Altitude an aircraft is cleared to maintain as specified \n                  by ATC.  It may differ from the Cruising Altitude, which is more strategic. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 174, 9)))

ClearedFlightInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'clearedSpeed'), _ImportedBinding__fb.AirspeedChoiceType, nillable=pyxb.binding.datatypes.boolean(1), scope=ClearedFlightInformationType, documentation='\n                  .Cleared Speed: The speed (or speed range) cleared from the controller to the pilot. \n                   The element is tactical in nature. The speed condition indicates whether the aircraft \n                  will be maintaining, exceeding, or flying more slowly than the associated speed. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 182, 9)))

ClearedFlightInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'directRouting'), DirectRoutingType, scope=ClearedFlightInformationType, documentation='\n                  .Cleared Direct To: Contains the optional starting location from which the direct \n                  clearance is granted and the position the aircraft has been cleared directly to. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 192, 9)))

ClearedFlightInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'heading'), _ImportedBinding__fb.DirectionType, nillable=pyxb.binding.datatypes.boolean(1), scope=ClearedFlightInformationType, documentation="\n                  .Cleared Heading: The heading assigned to a flight by ATC.  It is the magnetic heading \n                  the aircraft's nose is pointing to. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 201, 9)))

ClearedFlightInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offtrackClearance'), _ImportedBinding__fb.LateralOfftrackType, nillable=pyxb.binding.datatypes.boolean(1), scope=ClearedFlightInformationType, documentation='\n                  .Off Track Clearance: This field specifies the offtrack information applicable to \n                  the route. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 209, 9)))

ClearedFlightInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rateOfClimbDescend'), _ImportedBinding__ff.VerticalRateType, nillable=pyxb.binding.datatypes.boolean(1), scope=ClearedFlightInformationType, documentation="\n                  .Cleared Rate of Climb/Descent: The flight's current assigned Rate of climb/descent, \n                  which is part of the current clearance. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 217, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 174, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 182, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 192, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 201, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 209, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 217, 9))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'clearedFlightLevel')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 174, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'clearedSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 182, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'directRouting')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 192, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'heading')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 201, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'offtrackClearance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 209, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'rateOfClimbDescend')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 217, 9))
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
ClearedFlightInformationType._Automaton = _BuildAutomaton_7()




ControlElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airspace'), AirspaceConstraintType, scope=ControlElementType, documentation='\n                  Represents an airspace that has been constrained such as flow constrained area with \n                  associated controlled time. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 238, 9)))

ControlElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome'), _ImportedBinding__ff.AerodromeIcaoCodeType, scope=ControlElementType, documentation='\n                  An arrival aerodrome that is subject to air traffic control management. \n                  .Arrival Aerodrome: The ICAO designator or the name of the aerodrome at which the \n                  flight has arrived. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 246, 9)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 238, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 246, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ControlElementType._UseForTag(pyxb.namespace.ExpandedName(None, 'airspace')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 238, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ControlElementType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 246, 9))
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
ControlElementType._Automaton = _BuildAutomaton_8()




DirectRoutingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'from'), _ImportedBinding__fb.SignificantPointType, scope=DirectRoutingType, documentation='\n                  Location from which the direct clearance is granted. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 268, 9)))

DirectRoutingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'to'), _ImportedBinding__fb.SignificantPointType, scope=DirectRoutingType, documentation='\n                  Location to which the direct clearance is granted. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 275, 9)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 268, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 275, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DirectRoutingType._UseForTag(pyxb.namespace.ExpandedName(None, 'from')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 268, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DirectRoutingType._UseForTag(pyxb.namespace.ExpandedName(None, 'to')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 275, 9))
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
DirectRoutingType._Automaton = _BuildAutomaton_9()




PointoutType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'originatingUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=PointoutType, documentation='\n                  .Point Out - Originating Sector: Identifies the ATC sector originating the point \n                  out. \n                  .Point Out - Originating Unit: Identifies the Air Traffic Control unit originating \n                  the point out. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 386, 9)))

PointoutType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'receivingUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=PointoutType, documentation='\n                  .Point Out - Receiving Sector: Identifies the ATC sector receiving the point out. \n                  \n                  .Point Out - Receiving Unit: Identifies the Air Traffic Control unit receiving the \n                  point out. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 396, 9)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 386, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 396, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointoutType._UseForTag(pyxb.namespace.ExpandedName(None, 'originatingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 386, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PointoutType._UseForTag(pyxb.namespace.ExpandedName(None, 'receivingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 396, 9))
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
PointoutType._Automaton = _BuildAutomaton_10()




ActualSpeedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'calculated'), _ImportedBinding__ff.GroundspeedType, scope=ActualSpeedType, documentation='\n                  .Speed - Calculated: The estimated horizontal speed of the aircraft relative to a \n                  fixed point on the ground. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 89, 9)))

ActualSpeedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pilotReported'), _ImportedBinding__ff.TrueAirspeedOrMachType, scope=ActualSpeedType, documentation='\n                  .Speed - Pilot Reported: The speed of the aircraft relative to the air mass in which \n                  it is flying. This is the speed reported by the pilot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 97, 9)))

ActualSpeedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surveillance'), _ImportedBinding__ff.GroundspeedType, scope=ActualSpeedType, documentation='\n                  .Speed - Surveillance: The measured horizontal speed of the aircraft relative to \n                  a fixed point on the ground, for flights being tracked by surveillance or satellite. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 105, 9)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 89, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 97, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 105, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActualSpeedType._UseForTag(pyxb.namespace.ExpandedName(None, 'calculated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ActualSpeedType._UseForTag(pyxb.namespace.ExpandedName(None, 'pilotReported')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 97, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ActualSpeedType._UseForTag(pyxb.namespace.ExpandedName(None, 'surveillance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 105, 9))
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
ActualSpeedType._Automaton = _BuildAutomaton_11()




DepartureActivityTimesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boardingTime'), _ImportedBinding__fb.TimeSequenceType, scope=DepartureActivityTimesType, documentation='\n                  .Boarding Start Time - Actual: Time passengers are entering the bridge or bus to \n                  the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 88, 9)))

DepartureActivityTimesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deIcingTime'), _ImportedBinding__fb.TimeSequenceType, nillable=pyxb.binding.datatypes.boolean(1), scope=DepartureActivityTimesType, documentation='\n                  .De-icing End Time - Estimated: The time when de-icing operations on the aircraft \n                  are expected to end. \n                  .De-icing Start Time - Estimated: The time when de-icing operations on the aircraft \n                  are expected to start. \n                  .De-icing Ready Time - Estimated: The time when the aircraft is expected to be ready \n                  for de-icing operations. \n                  .De-icing Start Time - Actual: The time when de-icing operations on the aircraft \n                  start. \n                  .De-icing Ready Time - Actual:  The time when the aircraft is ready to be de-iced. \n                  \n                  .De-icing End Time - Actual: The time when de-icing operations on the aircraft end. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 96, 9)))

DepartureActivityTimesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'groundHandlingTime'), _ImportedBinding__fb.TimeSequenceType, scope=DepartureActivityTimesType, documentation='\n                  .Ground Handling End Time - Actual: The time when ground handling on the aircraft \n                  ends. \n                  .Ground Handling Start Time - Actual: The time when ground handling on the aircraft \n                  starts. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 114, 9)))

DepartureActivityTimesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'startupTime'), _ImportedBinding__fb.TimeSequenceType, scope=DepartureActivityTimesType, documentation='\n                  .Start Up Approval Time - Target: The time when the aircraft is expected to receive \n                  start up/pushback approval. \n                  .Start Up Approval Time - Actual: The time when the aircraft receives the start up \n                  approval. \n                  .Start Up Request Time - Actual: The time when the aircraft requests start up clearance. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 124, 9)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 88, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 96, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 114, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 124, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DepartureActivityTimesType._UseForTag(pyxb.namespace.ExpandedName(None, 'boardingTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 88, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DepartureActivityTimesType._UseForTag(pyxb.namespace.ExpandedName(None, 'deIcingTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 96, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DepartureActivityTimesType._UseForTag(pyxb.namespace.ExpandedName(None, 'groundHandlingTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 114, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DepartureActivityTimesType._UseForTag(pyxb.namespace.ExpandedName(None, 'startupTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 124, 9))
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
DepartureActivityTimesType._Automaton = _BuildAutomaton_12()




EnRouteDiversionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diversionRecoveryInformation'), _ImportedBinding__fb.GloballyUniqueFlightIdentifierType, scope=EnRouteDiversionType, documentation='\n                  .Diversion Recovery Information: The Diversion Recovery Information indicates a flight \n                  is the recovery for a flight that changed its original destination. It is represented \n                  by the GUFI of the original flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 127, 9)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 127, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteDiversionType._UseForTag(pyxb.namespace.ExpandedName(None, 'diversionRecoveryInformation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 127, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EnRouteDiversionType._Automaton = _BuildAutomaton_13()




OriginatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aftnAddress'), _ImportedBinding__fb.AftnAddressType, scope=OriginatorType, documentation="\n                  Represents the Aeronautical Fixed Telecommunication Network station address \n                  .Originator AFTN Address: The originator's eight-letter AFTN address, or other appropriate \n                  contact details, in cases where the originator of the flight plan may not be readily \n                  identified. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 418, 9)))

OriginatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flightOriginator'), _ImportedBinding__fb.FreeTextType, scope=OriginatorType, documentation="\n                  .Flight Originator: The originator's eight-letter AFTN address, or other appropriate \n                  contact details, in cases where the originator of the flight plan may not be readily \n                  identified. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 428, 9)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 418, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 428, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OriginatorType._UseForTag(pyxb.namespace.ExpandedName(None, 'aftnAddress')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 418, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OriginatorType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightOriginator')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 428, 9))
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
OriginatorType._Automaton = _BuildAutomaton_14()




ElapsedTimeLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'longitude'), _ImportedBinding__ff.LongitudeType, scope=ElapsedTimeLocationType, documentation='\n                  Longitude associated with the elapsed time. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 155, 9)))

ElapsedTimeLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), _ImportedBinding__fb.SignificantPointType, scope=ElapsedTimeLocationType, documentation='\n                  Point associated with the estimated elapsed time. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 162, 9)))

ElapsedTimeLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'region'), _ImportedBinding__ff.UnitSectorAirspaceType, scope=ElapsedTimeLocationType, documentation='\n                  Flight information boundary associated with the elapsed time. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 169, 9)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 155, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 162, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 169, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ElapsedTimeLocationType._UseForTag(pyxb.namespace.ExpandedName(None, 'longitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 155, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ElapsedTimeLocationType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 162, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ElapsedTimeLocationType._UseForTag(pyxb.namespace.ExpandedName(None, 'region')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 169, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ElapsedTimeLocationType._Automaton = _BuildAutomaton_15()




ExpandedRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routePoint'), ExpandedRoutePointType, scope=ExpandedRouteType, documentation="\n                  Expanded Route contains an ordered list of expanded route points. \n                  .Expanded Route Point: A point that is part of the aircraft's expanded route of flight. \n                  \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 216, 9)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 216, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExpandedRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'routePoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 216, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExpandedRouteType._Automaton = _BuildAutomaton_16()




SpeedScheduleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'initialSpeed'), _ImportedBinding__ff.AirspeedInIasOrMachType, scope=SpeedScheduleType, documentation='\n                  Initial speed of the aircraft during the climb \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 441, 9)))

SpeedScheduleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subsequentSpeed'), _ImportedBinding__ff.AirspeedInIasOrMachType, scope=SpeedScheduleType, documentation='\n                  Subsequent speed of the aircraft during the climb \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 448, 9)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 441, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 448, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpeedScheduleType._UseForTag(pyxb.namespace.ExpandedName(None, 'initialSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 441, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpeedScheduleType._UseForTag(pyxb.namespace.ExpandedName(None, 'subsequentSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 448, 9))
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
SpeedScheduleType._Automaton = _BuildAutomaton_17()




MeteorologicalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'temperature'), _ImportedBinding__ff.TemperatureType, scope=MeteorologicalDataType, documentation='\n                  Temperature at the trajectory point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 89, 9)))

MeteorologicalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'windDirection'), _ImportedBinding__ff.WindDirectionType, scope=MeteorologicalDataType, documentation='\n                  Wind vector at the trajectory point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 96, 9)))

MeteorologicalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'windSpeed'), _ImportedBinding__ff.WindspeedType, scope=MeteorologicalDataType, documentation='\n                  Wind speed at the trajectory point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 103, 9)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 89, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 96, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 103, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeteorologicalDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'temperature')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeteorologicalDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'windDirection')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 96, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeteorologicalDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'windSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 103, 9))
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
MeteorologicalDataType._Automaton = _BuildAutomaton_18()




PointRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lateralRange'), _ImportedBinding__fb.LateralOfftrackType, scope=PointRangeType, documentation='\n                  Lateral range representing  offsets for deviations due to weather \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 170, 9)))

PointRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'temporalRange'), TemporalRangeType, scope=PointRangeType, documentation='\n                  Temporal range resulting from assigned speed range. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 177, 9)))

PointRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'verticalRange'), _ImportedBinding__fb.VerticalRangeType, scope=PointRangeType, documentation='\n                  Vertical Range representing block altitude clearances \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 184, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 170, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 177, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 184, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'lateralRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 170, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PointRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'temporalRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 177, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PointRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'verticalRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 184, 9))
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
PointRangeType._Automaton = _BuildAutomaton_19()




TrajectoryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trajectoryPoint'), TrajectoryPointType, scope=TrajectoryType, documentation='\n                  a 4D Trajectory consists of an ordered list of trajectory points. \n                  .Trajectory Point: A container for information pertinent to a single point in a trajectory. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 226, 9)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 226, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryType._UseForTag(pyxb.namespace.ExpandedName(None, 'trajectoryPoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 226, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TrajectoryType._Automaton = _BuildAutomaton_20()




TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altimeterSetting'), _ImportedBinding__ff.PressureType, scope=TrajectoryPointType, documentation='\n                  .Assumed Altimeter Setting: The barometric pressure reading used to adjust a pressure \n                  altimeter for variations in existing atmospheric pressure or to the standard altimeter \n                  setting (29.92). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 302, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metData'), MeteorologicalDataType, scope=TrajectoryPointType, documentation='\n                  .Meteorological Data: In a predicted trajectory, the instantaneous temperature and \n                  wind vector used at the 4D Point for creating the 4D trajectory. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 311, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), Point4DType, scope=TrajectoryPointType, documentation='\n                  .4D Point: Identifies the location, altitude and time of a trajectory point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 319, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedAirspeed'), _ImportedBinding__fb.AirspeedChoiceType, scope=TrajectoryPointType, documentation='\n                  .Airspeed - Predicted: The airspeed (or range of speeds) of the flight at the 4D \n                  Point expressed as either Indicated Airspeed or Mach. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 326, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedGroundspeed'), _ImportedBinding__fb.GroundspeedChoiceType, scope=TrajectoryPointType, documentation='\n                  .Ground Speed - Predicted: Aircraft predicted ground speed (or range of speeds) at \n                  this point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 334, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'referencePoint'), ExpandedRoutePointType, scope=TrajectoryPointType, documentation='\n                  .Reference Point: For 4D Points associated with a waypoint on the expanded route, \n                  the reference point provides the expanded route waypoint enabling the 4D Trajectory \n                  to be linked with the route information. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 342, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trajectoryChange'), TrajectoryChangeType, scope=TrajectoryPointType, documentation='\n                  Indicates features that are crossed at the specified trajectory point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 351, 9)))

TrajectoryPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trajectoryChangeType'), STD_ANON_20, scope=TrajectoryPointType, documentation='\n                  Trajectory Change Point - Type: Identifies the type(s) of trajectory change point \n                  being described by the associated 4D Point. \n                  .Trajectory Change Point - Type: Identifies the type(s) of trajectory change point \n                  being described by the associated 4D Point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 358, 9)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 302, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 311, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 319, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 326, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 334, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 342, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 351, 9))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 358, 9))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'altimeterSetting')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 302, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'metData')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 311, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 319, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedAirspeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 326, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedGroundspeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 334, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'referencePoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 342, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'trajectoryChange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 351, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryPointType._UseForTag(pyxb.namespace.ExpandedName(None, 'trajectoryChangeType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 358, 9))
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
TrajectoryPointType._Automaton = _BuildAutomaton_21()




TrajectoryRoutePairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route'), RouteType, scope=TrajectoryRoutePairType, documentation='\n                  Route associated with the Trajectory Route Pair. \n                  .Route: The ICAO route string as depicted from the flight plan. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 382, 9)))

TrajectoryRoutePairType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trajectory'), TrajectoryType, scope=TrajectoryRoutePairType, documentation='\n                  4D Trajectory associated with the Trajectory Route Pair. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 390, 9)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 382, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 390, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryRoutePairType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 382, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TrajectoryRoutePairType._UseForTag(pyxb.namespace.ExpandedName(None, 'trajectory')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 390, 9))
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
TrajectoryRoutePairType._Automaton = _BuildAutomaton_22()




AircraftCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'communication'), CommunicationCapabilitiesType, scope=AircraftCapabilitiesType, documentation='\n                  .Communications Capabilities: The serviceable communications equipment, available \n                  on the aircraft at the time of flight, and associated flight crew qualifications \n                  that may be used to communicate with ATS units. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 193, 9)))

AircraftCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navigation'), NavigationCapabilitiesType, scope=AircraftCapabilitiesType, documentation='\n                  .Navigation Capabilities: The serviceable navigation equipment available on board \n                  the aircraft at the time of flight and for which the flight crew is qualified. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 202, 9)))

AircraftCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surveillance'), SurveillanceCapabilitiesType, scope=AircraftCapabilitiesType, documentation='\n                  .Surveillance Capabilities: The serviceable Secondary Surveillance Radar (SSR) and/or \n                  Automatic Dependent Surveillance (ADS) equipment available on the aircraft at the \n                  time of flight that may be used to identify and/or locate the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 210, 9)))

AircraftCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'survival'), SurvivalCapabilitiesType, scope=AircraftCapabilitiesType, documentation='\n                  Aircraft is equipped with survival capabilities. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 219, 9)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 193, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 202, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 210, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 219, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AircraftCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'communication')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 193, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AircraftCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'navigation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 202, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AircraftCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'surveillance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 210, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AircraftCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'survival')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 219, 9))
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
AircraftCapabilitiesType._Automaton = _BuildAutomaton_23()




NavigationCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'navigationCode'), STD_ANON_2, scope=NavigationCapabilitiesType, documentation='\n                  Describes the aircraft navigation code. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 86, 9)))

NavigationCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'performanceBasedCode'), STD_ANON_3, scope=NavigationCapabilitiesType, documentation='\n                  .Performance-Based Navigation Capabilities: A coded category denoting which Required \n                  Navigation Performance (RNP) and Area Navigation (RNAV) requirements can be met by \n                  the aircraft while operating in the context of a particular airspace when supported \n                  by the appropriate navigation infrastructure. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 96, 9)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 86, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 96, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NavigationCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'navigationCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 86, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NavigationCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'performanceBasedCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\NavigationCapability.xsd', 96, 9))
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
NavigationCapabilitiesType._Automaton = _BuildAutomaton_24()




SurveillanceCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'surveillanceCode'), STD_ANON_4, scope=SurveillanceCapabilitiesType, documentation='\n                  Describes the aircraft surveillance code. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 87, 9)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 87, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SurveillanceCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'surveillanceCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurveillanceCapability.xsd', 87, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SurveillanceCapabilitiesType._Automaton = _BuildAutomaton_25()




DinghyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'colour'), DinghyColourType, scope=DinghyType, documentation='\n                  .Dinghy Color: The color of the dinghies carried by the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 85, 9)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 85, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DinghyType._UseForTag(pyxb.namespace.ExpandedName(None, 'colour')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 85, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DinghyType._Automaton = _BuildAutomaton_26()




SurvivalCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dinghyInformation'), DinghyType, scope=SurvivalCapabilitiesType, documentation='\n                  Describes the aircraft dingy. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 213, 9)))

SurvivalCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emergencyRadioCode'), STD_ANON_5, scope=SurvivalCapabilitiesType, documentation='\n                  .Emergency Radio Transmitter Type: The type of serviceable communication devices \n                  available on the aircraft that are able to transmit an emergency radio signal. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 220, 9)))

SurvivalCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lifeJacketCode'), STD_ANON_6, scope=SurvivalCapabilitiesType, documentation='\n                  .Life Jacket Type: The type of life jackets available on board the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 231, 9)))

SurvivalCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'survivalEquipmentCode'), STD_ANON_7, scope=SurvivalCapabilitiesType, documentation='\n                  .Survival Equipment Type: The type of equipment carried on board the aircraft that \n                  can be used by the crew and passengers to assist survival in harsh environments in \n                  case of emergency. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 241, 9)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 213, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 220, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 231, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 241, 9))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SurvivalCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'dinghyInformation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 213, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SurvivalCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'emergencyRadioCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 220, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SurvivalCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'lifeJacketCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 231, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SurvivalCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'survivalEquipmentCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\SurvivalCapability.xsd', 241, 9))
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
SurvivalCapabilitiesType._Automaton = _BuildAutomaton_27()




ShippingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aerodromeOfLoading'), _ImportedBinding__fb.AerodromeReferenceType, scope=ShippingInformationType, documentation='\n                  .Aerodrome of Loading: The aerodrome where dangerous goods were loaded onto the flight. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 303, 9)))

ShippingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aerodromeOfUnloading'), _ImportedBinding__fb.AerodromeReferenceType, scope=ShippingInformationType, documentation='\n                  .Aerodrome of Unloading: The aerodrome where dangerous goods were unloaded from the \n                  flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 311, 9)))

ShippingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'consignee'), StructuredPostalAddressType, scope=ShippingInformationType, documentation="\n                  .Consignee Name and Address: The XML Grouping Element unites the Consignee Name with \n                  the Postal Structure Address (detailed breakout of address components). \n                  .Consignee Phone Number: The phone number of the consignee contact department or \n                  person to call, in the event of an emergency, security event, or when further information \n                  about the shipment is needed. \n                  .Consignee Contact Name: The name of the consignee contact department or person responsible \n                  in the event of an emergency, security event, or when further information about the \n                  shipment is needed. \n                  .Consignee Address: Specifies the consignee's mailing address. \n                  .Consignee Name: Contains the name or legal identity of the organization or person \n                  receiving the package. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 319, 9)))

ShippingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'declarationText'), DeclarationTextType, scope=ShippingInformationType, documentation='\n                  compliance: \n                   \n                  consignor: \n                   \n                  shipper: \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 336, 9)))

ShippingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shipper'), StructuredPostalAddressType, scope=ShippingInformationType, documentation="\n                  .Shipper Address: The shipper's mailing address. \n                  .Shipper Emergency Phone Number: Phone number of the shipper or someone who is not \n                  on board the aircraft and who can be reached in an emergency involving the dangerous \n                  good. \n                  .Shipper Name and Address: The XML Grouping Element unites the Shipper (Consignor) \n                  Name with the Postal Structure Address (detailed breakout of address components). \n                  \n                  .Shipper Name: The Shipper's name, legal identity, and/or organization. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 347, 9)))

ShippingInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transferAerodromes'), STD_ANON_9, scope=ShippingInformationType, documentation='\n                  .Transfer Aerodromes: A list of the aerodromes through which the package has travelled \n                  en route to its final destination. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 361, 9)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 303, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 311, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 319, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 336, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 347, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 361, 9))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ShippingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'aerodromeOfLoading')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 303, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ShippingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'aerodromeOfUnloading')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 311, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ShippingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'consignee')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 319, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ShippingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'declarationText')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 336, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ShippingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'shipper')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 347, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ShippingInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'transferAerodromes')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 361, 9))
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
ShippingInformationType._Automaton = _BuildAutomaton_28()




DangerousGoodsPackageGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dangerousGoodsPackage'), DangerousGoodsPackageType, scope=DangerousGoodsPackageGroupType, documentation='\n                  A collection of at least one DangerousGoodsPackage. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 390, 9)))

DangerousGoodsPackageGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shipmentDimensions'), DangerousGoodsDimensionsType, scope=DangerousGoodsPackageGroupType, documentation='\n                  Weight and volume (not height, width, and depth): \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 397, 9)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 390, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 397, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageGroupType._UseForTag(pyxb.namespace.ExpandedName(None, 'dangerousGoodsPackage')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 390, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageGroupType._UseForTag(pyxb.namespace.ExpandedName(None, 'shipmentDimensions')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 397, 9))
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
DangerousGoodsPackageGroupType._Automaton = _BuildAutomaton_29()




BoundaryCrossingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altitude'), _ImportedBinding__fb.AltitudeChoiceType, scope=BoundaryCrossingType, documentation='\n                  .Boundary Crossing Level - Cleared/Coordinated: The cleared altitude (flight level) \n                  at which the aircraft will cross the boundary crossing point if in level cruising \n                  flight or, if the aircraft is climbing or descending at the boundary crossing point, \n                  the cleared flight level to which it is proceeding. \n                  .Boundary Crossing Level - Cleared Block - Proposed: The proposed vertical range \n                  of levels transmitted as the boundary crossing level during negotiation between controllers. \n                  \n                  .Boundary Crossing Level - Transition/Coordinated: An altitude (flight level) at \n                  or above/below which an aircraft will cross the associated boundary point. \n                  .Boundary Crossing Level - Cleared Block/Coordinated: A vertical range of levels \n                  transmitted as the boundary crossing level. \n                  .Boundary Crossing Level - Proposed: If the aircraft is at level cruising, the proposed \n                  altitude (flight level) at which the aircraft will cross the boundary crossing point. \n                   If the aircraft is climbing or descending at the boundary crossing point, then the \n                  proposed cruise flight level to which it is proceeding when it crosses the boundary \n                  crossing point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 121, 9)))

BoundaryCrossingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altitudeInTransition'), AltitudeInTransitionType, scope=BoundaryCrossingType, documentation='\n                  Negotiated boundary crossing transition altitude. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 143, 9)))

BoundaryCrossingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'crossingPoint'), _ImportedBinding__fb.SignificantPointType, scope=BoundaryCrossingType, documentation='\n                  .Boundary Crossing Point/Coordinated: The point where the flight will cross an ATS \n                  facility boundary. \n                  .Boundary Crossing Point - Proposed: The proposed point where the flight will cross \n                  an ATS facility boundary, as requested by the accepting controller from the transferring \n                  controller. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 150, 9)))

BoundaryCrossingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'crossingSpeed'), _ImportedBinding__fb.AirspeedChoiceType, scope=BoundaryCrossingType, documentation='\n                  .Boundary Crossing - Assigned Speed - Proposed: During negotiation between controllers, \n                  the proposed clearance information assigning a speed (or range of speeds) and speed \n                  condition to the flight at the boundary point.  The speed condition indicates whether \n                  the aircraft will be maintaining, exceeding, or flying more slowly than the assigned \n                  boundary crossing speed. \n                  .Boundary Crossing - Assigned Speed/Coordinated: Clearance information assigning \n                  a speed (or range of speeds) and speed condition to the flight at the boundary point. \n                   The speed condition indicates whether the aircraft will be maintaining, exceeding, \n                  or flying more slowly than the assigned boundary crossing speed. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 161, 9)))

BoundaryCrossingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offtrack'), _ImportedBinding__fb.LateralOfftrackType, scope=BoundaryCrossingType, documentation='\n                  .Boundary Crossing - Off Track Information - Proposed: Provides the off track clearance \n                  information, if the flight is proposed to be off track at the boundary crossing point. \n                   For the boundary crossing point, the off track information includes the off track \n                  direction, the distance and the reason the aircraft is off track. \n                  .Boundary Crossing - Off Track Information/Coordinated: Provides the off track clearance \n                  information, if the flight will be off track at the boundary crossing point.  For \n                  the boundary crossing point, the off track information includes the off track direction, \n                  the distance and the reason the aircraft is off track. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 176, 9)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 121, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 143, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 150, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 161, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 176, 9))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryCrossingType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 121, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryCrossingType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitudeInTransition')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 143, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryCrossingType._UseForTag(pyxb.namespace.ExpandedName(None, 'crossingPoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 150, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryCrossingType._UseForTag(pyxb.namespace.ExpandedName(None, 'crossingSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 161, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryCrossingType._UseForTag(pyxb.namespace.ExpandedName(None, 'offtrack')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 176, 9))
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
BoundaryCrossingType._Automaton = _BuildAutomaton_30()




AirspaceConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airspaceControlledEntryTime'), _ImportedBinding__ff.TimeType, nillable=pyxb.binding.datatypes.boolean(1), scope=AirspaceConstraintType, documentation='\n                  .Airspace Entry Time - Controlled: The time at which a flight is required to arrive \n                  at a constrained airspace element as a result of a tactical slot allocation or a \n                  Traffic Management Initiative (TMI). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 92, 9)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 92, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'airspaceControlledEntryTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 92, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AirspaceConstraintType._Automaton = _BuildAutomaton_31()




PlannedReportingPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), _ImportedBinding__fb.SignificantPointType, scope=PlannedReportingPositionType, documentation='\n                  Planned reporting position point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 212, 9)))

PlannedReportingPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'positionAltitude'), _ImportedBinding__ff.AltitudeType, scope=PlannedReportingPositionType, documentation='\n                  Altitude associated with the planned reporting position. \n                  .Next Future Reporting Position Altitude: Expected altitude at the estimated next \n                  future position of the aircraft transmitted in a non-radar airspace position report. \n                  \n                  .Following Future Reporting Position Altitude: Expected altitude at the estimated \n                  second future position of the aircraft transmitted in a non-radar airspace position \n                  report. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 219, 9)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 212, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 219, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PlannedReportingPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 212, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PlannedReportingPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'positionAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 219, 9))
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
PlannedReportingPositionType._Automaton = _BuildAutomaton_32()




LastPositionReportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), _ImportedBinding__fb.SignificantPointType, scope=LastPositionReportType, documentation='\n                  The position of the aircraft last known to ATS. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 216, 9)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 216, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LastPositionReportType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 216, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LastPositionReportType._Automaton = _BuildAutomaton_33()




AircraftOperatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'operatingOrganization'), _ImportedBinding__ff.PersonOrOrganizationType, scope=AircraftOperatorType, documentation='\n                  .Aircraft Operator Identity: Identity of a person, organization or enterprise engaged \n                  in or offering to engage in aircraft operation. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 99, 9)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 99, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AircraftOperatorType._UseForTag(pyxb.namespace.ExpandedName(None, 'operatingOrganization')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 99, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AircraftOperatorType._Automaton = _BuildAutomaton_34()




FlightIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'marketingCarrierFlightIdentifier'), STD_ANON_18, scope=FlightIdentificationType, documentation='\n                  .Aircraft Identification - Marketing Carrier: The aircraft identification used by \n                  a carrier who has sold tickets for the flight but is not involved with the operation \n                  of the flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 360, 9)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 360, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlightIdentificationType._UseForTag(pyxb.namespace.ExpandedName(None, 'marketingCarrierFlightIdentifier')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 360, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FlightIdentificationType._Automaton = _BuildAutomaton_35()




SupplementalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pilotInCommand'), _ImportedBinding__ff.PersonType, scope=SupplementalDataType, documentation='\n                  .Pilot In Command: The name of the pilot in command of the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 472, 9)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 472, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplementalDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'pilotInCommand')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 472, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplementalDataType._Automaton = _BuildAutomaton_36()




AbstractRoutePointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), _ImportedBinding__fb.SignificantPointType, scope=AbstractRoutePointType, documentation='\n                  .Significant Point: A single point along the flight route. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractRoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractRoutePointType._Automaton = _BuildAutomaton_37()




EstimatedElapsedTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), ElapsedTimeLocationType, scope=EstimatedElapsedTimeType, documentation='\n                  The location associated with estimated elapsed time. It can be a longitude, significant \n                  point of flight information region. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 188, 9)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 188, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EstimatedElapsedTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 188, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EstimatedElapsedTimeType._Automaton = _BuildAutomaton_38()




RouteSegmentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routePoint'), RoutePointType, scope=RouteSegmentType, documentation='\n                  Route Segment consists of an optional route point. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 409, 9)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 409, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RouteSegmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'routePoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 409, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RouteSegmentType._Automaton = _BuildAutomaton_39()




Point4DType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altitude'), _ImportedBinding__ff.AltitudeType, scope=Point4DType, documentation='\n                        Altitude of the 4D point. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 123, 15)))

Point4DType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pointRange'), PointRangeType, scope=Point4DType, documentation='\n                        block altitude clearances \n    offsets for deviations due to weather\n    assigned speed ranges\n                        .Point Range: Provides a vertical, lateral or temporal range to a 4D point when clearances \n                        are provided in the form of:block altitude clearancesoffsets for deviations due to \n                        weatherassigned speed ranges \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 130, 15)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 93, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 123, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 130, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Point4DType._UseForTag(pyxb.namespace.ExpandedName(None, 'pos')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Location.xsd', 93, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Point4DType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 123, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Point4DType._UseForTag(pyxb.namespace.ExpandedName(None, 'pointRange')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Trajectory.xsd', 130, 15))
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
Point4DType._Automaton = _BuildAutomaton_40()




AircraftType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aircraftType'), AircraftTypeType, scope=AircraftType_, documentation='\n                        .Aircraft Type: The manufacturer and model of the airframe expressed either as an \n                        ICAO-approved designator or a text description. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 92, 15)))

AircraftType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'capabilities'), AircraftCapabilitiesType, scope=AircraftType_, documentation='\n                        Aircraft contains several types of capabilities. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 100, 15)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 92, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 100, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AircraftType_._UseForTag(pyxb.namespace.ExpandedName(None, 'aircraftType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 92, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AircraftType_._UseForTag(pyxb.namespace.ExpandedName(None, 'capabilities')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 100, 15))
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
AircraftType_._Automaton = _BuildAutomaton_41()




CommunicationCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'communicationCode'), STD_ANON, scope=CommunicationCapabilitiesType, documentation='\n                  Describes the aircraft communication code. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 88, 9)))

CommunicationCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataLinkCode'), STD_ANON_, scope=CommunicationCapabilitiesType, documentation='\n                  .Data Link Communication Capabilities: The serviceable equipment and capabilities \n                  available on the aircraft at the time of flight that may be used to communicate data \n                  to and from the aircraft. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 98, 9)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 88, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 98, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'communicationCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 88, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(None, 'dataLinkCode')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\CommunicationCapability.xsd', 98, 9))
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
CommunicationCapabilitiesType._Automaton = _BuildAutomaton_42()




DangerousGoodsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airWayBill'), AirWaybillType, scope=DangerousGoodsType, documentation='\n                        .Air Waybill Number: The number referencing the air waybill. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 165, 15)))

DangerousGoodsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'handlingInformation'), AdditionalHandlingInformationType, scope=DangerousGoodsType, documentation="\n                        .Additional Handling Information: Additional information related to the handling \n                        of dangerous goods, as identified on the Shipper's Declaration for Dangerous Goods. \n                        \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 172, 15)))

DangerousGoodsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'packageGroup'), DangerousGoodsPackageGroupType, scope=DangerousGoodsType, documentation='\n                        .Packing Group: A code that indicates the relative degree of danger presented by \n                        various articles and substances within a Class or Division. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 181, 15)))

DangerousGoodsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shippingInformation'), ShippingInformationType, scope=DangerousGoodsType, documentation="\n                        IATA Shipper's Declaration for Dangerous Goods. \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 189, 15)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 165, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 172, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 181, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 189, 15))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsType._UseForTag(pyxb.namespace.ExpandedName(None, 'airWayBill')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 165, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsType._UseForTag(pyxb.namespace.ExpandedName(None, 'handlingInformation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 172, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsType._UseForTag(pyxb.namespace.ExpandedName(None, 'packageGroup')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 181, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsType._UseForTag(pyxb.namespace.ExpandedName(None, 'shippingInformation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\DangerousGoods.xsd', 189, 15))
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
DangerousGoodsType._Automaton = _BuildAutomaton_43()




def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
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
    symbol = pyxb.binding.content.ElementUse(StructuredPostalAddressType._UseForTag(pyxb.namespace.ExpandedName(None, 'address')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 85, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StructuredPostalAddressType._UseForTag(pyxb.namespace.ExpandedName(None, 'onlineContact')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 92, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StructuredPostalAddressType._UseForTag(pyxb.namespace.ExpandedName(None, 'phoneFax')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\foundation\\Address.xsd', 99, 9))
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
StructuredPostalAddressType._Automaton = _BuildAutomaton_44()




DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'allPackedInOne'), AllPackedInOneType, scope=DangerousGoodsPackageType, documentation='\n                  .All Packed In One: A statement identifying the dangerous goods listed are all contained \n                  within the same outer packaging. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 178, 9)))

DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazardClass'), HazardClassType, scope=DangerousGoodsPackageType, documentation='\n                  .Hazard Class and Division: A number assigned to a dangerous good that represents \n                  a classification (Class) according to the most dominant hazard it represents, potentially \n                  followed by a number representing a subdivision (Division) within the Class. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 186, 9)))

DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'packageDimensions'), _ImportedBinding__ff.DimensionsType, scope=DangerousGoodsPackageType, documentation="\n                  .Package Width: The depth component of the package's volumetric dimensions. \n                  .Package Length: The lateral component of the package's volumetric dimensions. \n                  .Package Height: The vertical component of the package's volumetric dimensions. \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 195, 9)))

DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radioactiveMaterials'), RadioactiveMaterialType, scope=DangerousGoodsPackageType, documentation='\n                  .Radioactive Materials: The XML grouping element for goods that contain radioactive \n                  materials. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 204, 9)))

DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shipmentDimensions'), DangerousGoodsDimensionsType, scope=DangerousGoodsPackageType, documentation='\n                  Weight and volume (not height, width, and depth): \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 212, 9)))

DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subsidiaryHazardClass'), HazardClassType, scope=DangerousGoodsPackageType, documentation='\n                  .Subsidiary Hazard Class and Division: An identifier of any subsidiary hazard class(es)/division(s) \n                  in addition to the primary hazard class and division. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 219, 9)))

DangerousGoodsPackageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'temperatures'), TemperaturesType, scope=DangerousGoodsPackageType, documentation='\n                  Control Temperature: \n                   \n                  Emergency Temperature: \n                   \n                  Flashpoint Temperature: \n                  The lowest temperature at which it can vaporize to form an ignitable mixture in air. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 227, 9)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 178, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 186, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 195, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 204, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 212, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 219, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 227, 9))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'allPackedInOne')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 178, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'hazardClass')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 186, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'packageDimensions')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 195, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'radioactiveMaterials')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 204, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'shipmentDimensions')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 212, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'subsidiaryHazardClass')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 219, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DangerousGoodsPackageType._UseForTag(pyxb.namespace.ExpandedName(None, 'temperatures')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\Packaging.xsd', 227, 9))
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
DangerousGoodsPackageType._Automaton = _BuildAutomaton_45()




RadioactiveMaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radionuclide'), RadionuclideType, scope=RadioactiveMaterialType, documentation='\n                  .Radionuclide: The XML sub-grouping element for Radioactive Materials. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 130, 9)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 130, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RadioactiveMaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'radionuclide')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 130, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RadioactiveMaterialType._Automaton = _BuildAutomaton_46()




RadionuclideType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'activity'), RadioactiveMaterialActivityType, scope=RadionuclideType, documentation='\n                  .Activity: The measure of the rate of decay, or activity, of a radioactive material. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 273, 9)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 273, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RadionuclideType._UseForTag(pyxb.namespace.ExpandedName(None, 'activity')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\cargo\\RadioactiveMaterials.xsd', 273, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RadionuclideType._Automaton = _BuildAutomaton_47()




UnitBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundaryCrossingCoordinated'), BoundaryCrossingType, scope=UnitBoundaryType, documentation='\n                        Coordinated boundary crossing information with associated details including altitude, \n                        crossing point and crossing time. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 284, 15)))

UnitBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundaryCrossingProposed'), BoundaryCrossingType, scope=UnitBoundaryType, documentation='\n                        A proposed boundary crossing information with associated details including altitude, \n                        crossing point and crossing time. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 292, 15)))

UnitBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'downstreamUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=UnitBoundaryType, documentation='\n                        .Delegated Unit Indicator: Indicates whether or not the controlling unit has been \n                        delegated authority for the flight based on agreement with the unit in whose Area \n                        of Responsibility (AOR) the flight is currently located. \n                        .Downstream Unit: The next unit the flight will be controlled by based on the planned \n                        route of flight, altitude, and accepted constraints. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 300, 15)))

UnitBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'handoff'), HandoffType, scope=UnitBoundaryType, documentation="\n                        An action taken to transfer the radar identification of an aircraft from one controller \n                        to another controller if the aircraft will enter the receiving controller's airspace \n                        and radio communications with the aircraft will be transferred. \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 311, 15)))

UnitBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upstreamUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=UnitBoundaryType, documentation='\n                        .Upstream Unit: The unit the flight will enter prior to this unit, based on the planned \n                        route of flight, altitude, and accepted constraints. \n                        .Delegated Unit Indicator: Indicates whether or not the controlling unit has been \n                        delegated authority for the flight based on agreement with the unit in whose Area \n                        of Responsibility (AOR) the flight is currently located. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 320, 15)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 284, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 292, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 300, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 311, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 320, 15))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossingCoordinated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 284, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossingProposed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 292, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'downstreamUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 300, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'handoff')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 311, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'upstreamUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 320, 15))
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
UnitBoundaryType._Automaton = _BuildAutomaton_48()




CpdlcConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'receivingUnitFrequency'), _ImportedBinding__fb.RadioFrequencyType, scope=CpdlcConnectionType, documentation='\n                  .Receiving Unit Frequency: The frequency of the receiving unit. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 97, 9)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 97, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CpdlcConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'receivingUnitFrequency')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Datalink.xsd', 97, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CpdlcConnectionType._Automaton = _BuildAutomaton_49()




EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'alternateAerodrome'), _ImportedBinding__fb.AerodromeReferenceType, scope=EnRouteType, documentation='\n                        .En Route Alternate Aerodrome: An ICAO designator of the aerodrome to which a flight \n                        could be diverted while en route, if needed. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 297, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'beaconCodeAssignment'), BeaconCodeAssignmentType, scope=EnRouteType, documentation='\n                        Contains information about current, previous and next beacon code assignments along \n                        with the beacon code assigning facility. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 305, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundaryCrossings'), UnitBoundaryType, scope=EnRouteType, documentation='\n                        A list of boundary crossings that will be traversed En Route \n                        .Unit Boundary List: The ordered list of units the flight is expected to traverse, \n                        based on the planned route of flight and altitude. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 313, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cleared'), ClearedFlightInformationType, scope=EnRouteType, documentation='\n                        Contains the cleared information about the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 322, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'controlElement'), ControlElementType, nillable=pyxb.binding.datatypes.boolean(1), scope=EnRouteType, documentation='\n                        .Control Element: The constrained aerodrome or airspace element (subject to a Traffic \n                        Management Initiative/Regulation) indicating the reason for a flight being controlled. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 329, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cpdlcConnection'), CpdlcConnectionType, scope=EnRouteType, documentation='\n                        Groups information regarding CPDLC connection between air traffic control units \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 338, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pointout'), PointoutType, nillable=pyxb.binding.datatypes.boolean(1), scope=EnRouteType, documentation='\n                        A physical or automated action taken by a controller to transfer the radar identification \n                        of an aircraft to another controller if the aircraft will or may enter the airspace \n                        or protected airspace of another controller and radio communications will not be \n                        transferred. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 345, 15)))

EnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), AircraftPositionType, scope=EnRouteType, documentation='\n                        Contains the current position and associated data of the aircraft. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 355, 15)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 297, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 305, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 313, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 322, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 329, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 338, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 345, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 355, 15))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'alternateAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 297, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'beaconCodeAssignment')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 305, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossings')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 313, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'cleared')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 322, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'controlElement')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 329, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'cpdlcConnection')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 338, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'pointout')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 345, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(EnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 355, 15))
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
EnRouteType._Automaton = _BuildAutomaton_50()




AircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'actualSpeed'), ActualSpeedType, scope=AircraftPositionType, documentation='\n                        Actual flight  speed supplied by various sources. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 127, 15)))

AircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altitude'), _ImportedBinding__ff.AltitudeType, scope=AircraftPositionType, documentation='\n                        .Reported Altitude: The latest valid Mode C altitude received from an aircraft, or \n                        the latest reported altitude received from a pilot. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 134, 15)))

AircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'followingPosition'), PlannedReportingPositionType, nillable=pyxb.binding.datatypes.boolean(1), scope=AircraftPositionType, documentation='\n                        .Following Future Reporting Position: Estimated second future position of the aircraft \n                        transmitted in a non-radar airspace position report. \n                        .Following Future Reporting Position Altitude: Expected altitude at the estimated \n                        second future position of the aircraft transmitted in a non-radar airspace position \n                        report. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 142, 15)))

AircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nextPosition'), PlannedReportingPositionType, nillable=pyxb.binding.datatypes.boolean(1), scope=AircraftPositionType, documentation='\n                        For Oceanic flights, the next reporting position is required. \n                        .Next Future Reporting Position Altitude: Expected altitude at the estimated next \n                        future position of the aircraft transmitted in a non-radar airspace position report. \n                        \n                        .Next Future Reporting Position: Estimated next future position of the aircraft transmitted \n                        in a non-radar airspace position report. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 153, 15)))

AircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), _ImportedBinding__fb.SignificantPointType, scope=AircraftPositionType, documentation='\n                        .Current Position: The actual location of an active flight as reported by surveillance, \n                        for a flight tracked by radar, or from the position part of a pilot progress report, \n                        for an oceanic flight or flight operating in non-radar airspace. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 165, 15)))

AircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'track'), _ImportedBinding__fb.DirectionType, scope=AircraftPositionType, documentation='\n                        .Current Track: The direction the aircraft is flying, over the ground, relative to \n                        true north.  It is the heading of the aircraft as impacted by the wind. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 174, 15)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 127, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 134, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 142, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 153, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 165, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 174, 15))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'actualSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 127, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 134, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'followingPosition')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 142, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'nextPosition')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 153, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 165, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'track')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 174, 15))
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
AircraftPositionType._Automaton = _BuildAutomaton_51()




FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'approachFix'), _ImportedBinding__fb.SignificantPointType, scope=FlightArrivalType, documentation='\n                        .Initial Approach Fix: The point on the arrival route at which arrival sequencing \n                        activities are focused, such that, when the flight passes this point, a stable runway \n                        arrival sequence can be provided. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 94, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'approachTime'), _ImportedBinding__fb.MultiTimeType, scope=FlightArrivalType, documentation="\n                        .Approach Time - Estimated: The shared time estimate at which the flight's final \n                        approach is expected to commence. \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 103, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome'), _ImportedBinding__fb.AerodromeReferenceType, scope=FlightArrivalType, documentation='\n                        .Destination Aerodrome: The ICAO designator or the name of the aerodrome at which \n                        the flight is scheduled to arrive. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 111, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeAlternate'), _ImportedBinding__fb.AerodromeReferenceType, scope=FlightArrivalType, documentation='\n                        .Destination Aerodrome - Alternate: ICAO designator or the name of an alternate aerodrome \n                        to which an aircraft may proceed, should it become either impossible or inadvisable \n                        to land at the original destination aerodrome or an alternate destination location. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 119, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeOriginal'), _ImportedBinding__fb.AerodromeReferenceType, scope=FlightArrivalType, documentation='\n                        .Original Destination Aerodrome: The Original Destination Airport is the Destination \n                        Airport submitted when a Flight Plan was initially filed. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 129, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrivalFix'), _ImportedBinding__fb.SignificantPointType, scope=FlightArrivalType, documentation='\n                        .Aerodrome Arrival Fix: The point at which the responsibility for control of the \n                        flight is transferred from the En Route Air Traffic Control unit (Centre, ARTCC) \n                        to the Terminal Air Traffic Control unit. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 137, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrivalFixTime'), _ImportedBinding__fb.MultiTimeType, scope=FlightArrivalType, documentation='\n                        .Arrival Fix Time - Estimated: Estimated time over the arrival fix. \n                        .Arrival Fix Time - Actual: Actual time the flight passed over the arrival fix. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 146, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'filedRevisedDestinationAerodrome'), _ImportedBinding__fb.AerodromeReferenceType, scope=FlightArrivalType, documentation='\n                        Represents the filed revised destination aerodrome. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 154, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime'), _ImportedBinding__fb.RunwayPositionAndTimeType, scope=FlightArrivalType, documentation='\n                        .Arrival Runway: The expected, assigned, or actual runway for an arriving flight. \n                        \n                        .Runway Arrival Time - Estimated: The most reliable estimated time when an aircraft \n                        will touch down on the runway. \n                        .Runway Arrival Time - Target: The time when the aircraft is planned to touch down \n                        at the runway. \n                        .Runway Arrival Time - Actual: The actual time at which the aircraft lands on a runway. \n                        \n                        .Runway Arrival Time - Controlled: The time at which a flight is required to touch \n                        down at the runway, as a result of a tactical slot allocation or a Traffic Management \n                        Initiative. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 161, 15)))

FlightArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'standPositionAndTime'), _ImportedBinding__fb.StandPositionAndTimeType, scope=FlightArrivalType, documentation='\n                        .In-Block Time - Earliest: The earliest time an aircraft operator is able to arrive \n                        at the gate on completion of the flight, as specified by the aircraft operator when \n                        submitting the flight information. \n                        .Arrival Stand: The stand at which an aircraft arrives at the destination airport \n                        on completion of the flight. \n                        .In-Block Time - Actual: The time at which a flight arrives at the stand. \n                        .In-Block Time - Initial: The original stand arrival time of the flight when the \n                        flight is first created. \n                        .Arrival Terminal: The airport terminal at which the flight arrives. \n                        .In-Block Time - Controlled: The time at which a flight is required to arrive at \n                        the destination stand as determined by a TMI. \n                        .In-Block Time - Estimated: The estimated time at which a flight will arrive at the \n                        stand. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 178, 15)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 94, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 103, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 111, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 119, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 129, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 137, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 146, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 154, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 161, 15))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 178, 15))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'approachFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 94, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'approachTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 103, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 111, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeAlternate')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 119, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeOriginal')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 129, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 137, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalFixTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 146, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'filedRevisedDestinationAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 154, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 161, 15))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(FlightArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'standPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 178, 15))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FlightArrivalType._Automaton = _BuildAutomaton_52()




ClimbToLevelConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'climbToLevel'), _ImportedBinding__ff.AltitudeType, scope=ClimbToLevelConstraintType, documentation='\n                        .Change Cruise Climb: The parameters of a cruise climb executed at the associated \n                        significant point. It contains the following parameters: 1. the speed to be maintained \n                        during cruise climb; 2. either the minimum and maximum levels defining the layer \n                        to be occupied during cruise climb, or the level above which cruise climb is planned. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 113, 15)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 113, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClimbToLevelConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'climbToLevel')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 113, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClimbToLevelConstraintType._Automaton = _BuildAutomaton_53()




LevelConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'level'), _ImportedBinding__ff.AltitudeType, scope=LevelConstraintType, documentation='\n                        .Change Speed and Altitude: The planned speed and altitude that the aircraft will \n                        change to upon reaching the associated Significant Point along its Route. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 167, 15)))

LevelConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'timeConstraint'), TimeConstraintType, scope=LevelConstraintType, documentation='\n                        Level constraint may have an associated time constraint. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 175, 15)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 167, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 175, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LevelConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'level')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 167, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LevelConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'timeConstraint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 175, 15))
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
LevelConstraintType._Automaton = _BuildAutomaton_54()




SpeedConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'speed'), _ImportedBinding__ff.TrueAirspeedOrMachType, scope=SpeedConstraintType, documentation='\n                        .Change Speed and Altitude: The planned speed and altitude that the aircraft will \n                        change to upon reaching the associated Significant Point along its Route. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 239, 15)))

SpeedConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'timeConstraint'), TimeConstraintType, scope=SpeedConstraintType, documentation='\n                        A speed constraint may have an associated time constraint. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 247, 15)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 239, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 247, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpeedConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'speed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 239, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpeedConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'timeConstraint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\ConstraintsAndPreferences.xsd', 247, 15))
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
SpeedConstraintType._Automaton = _BuildAutomaton_55()




FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'departureAerodrome'), _ImportedBinding__fb.AerodromeReferenceType, scope=FlightDepartureType, documentation='\n                        .Departure Aerodrome: The ICAO designator of the aerodrome from which the flight \n                        departs. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 149, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'departureFix'), _ImportedBinding__fb.SignificantPointType, scope=FlightDepartureType, documentation='\n                        .Aerodrome Departure Fix: The point at which the responsibility for control of the \n                        flight is transferred from the Terminal Air Traffic Control unit to the En Route \n                        Air Traffic Control unit (Centre, ARTCC). \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 157, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'departureFixTime'), _ImportedBinding__fb.MultiTimeType, scope=FlightDepartureType, documentation='\n                        .Departure Fix Time - Estimated: The estimated time the flight is over the departure \n                        fix. \n                        .Departure Fix Time - Actual: The actual time the flight passed over the departure \n                        fix. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 166, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'departureTimes'), DepartureActivityTimesType, scope=FlightDepartureType, documentation='\n                        Optional TimeSequences associated with departure activities. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 176, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offBlockReadyTime'), _ImportedBinding__fb.TargetMultiTimeType, scope=FlightDepartureType, documentation='\n                        .Off-Block Ready Time - Actual: The time when the aircraft is ready for start-up/pushback \n                        or taxi immediately after clearance delivery. \n                        .Off-Block Ready Time - Target: The time an Aircraft Operator or Ground Handler estimates \n                        an aircraft will be ready, all doors closed, boarding bridge removed, push back vehicle \n                        available and ready to start up / push back immediately upon reception of clearance \n                        from the tower. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 183, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime'), _ImportedBinding__fb.RunwayPositionAndTimeType, scope=FlightDepartureType, documentation="\n                        .Runway Departure Time - Estimated: The most reliable estimated take off time. \n                        .Departure Time - Estimated: The estimated off-block time for the flight at the Departure \n                        Aerodrome, or, if the flight plan is filed in the air, the estimated time of departure \n                        from the first point on the route. The time is given in UTC. \n                        .Departure Runway: The expected, assigned, or actual runway for a departing flight. \n                        \n                        .Departure Time - Actual: The actual time of departure from the aerodrome, or the \n                        actual time of departure from the first point on the Route when the flight is an \n                        'air file', i.e., the flight plan is filed once the aircraft is already airborne. \n                        This time is given in UTC. \n                        .Runway Departure Time - Target: The time when the aircraft is planned to take off \n                        from the runway. \n                        .Runway Departure Time - Actual: The actual time at which a flight takes off from \n                        the runway. \n                        .Runway Departure Time - Controlled: The time at which a flight is required to take \n                        off from the runway as a result of a tactical slot allocation or a Traffic Management \n                        Initiative. \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 195, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'standPositionAndTime'), _ImportedBinding__fb.StandPositionAndTimeType, scope=FlightDepartureType, documentation='\n                        .Off-Block Time - Actual: The time at which a flight departs from the stand. \n                        .Off Block Time - Earliest: The earliest time an aircraft can push back or taxi from \n                        the stand. \n                        .Departure Terminal: The airport terminal from which the flight departs. \n                        .Departure Stand: The stand from which an aircraft departs on commencement of the \n                        flight. \n                        .Off-Block Time - Initial: The date and time at which a flight was originally planning \n                        to depart the stand. \n                        .Off Block Time - Estimated: The estimated time at which a flight will depart from \n                        the stand. \n                        .Off-Block Time - Controlled: The time at which a flight is required to depart from \n                        the stand as determined by a TMI. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 218, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'takeoffAlternateAerodrome'), _ImportedBinding__fb.AerodromeReferenceType, scope=FlightDepartureType, documentation='\n                        .Take Off Alternate Aerodrome: An alternate aerodrome at which an aircraft can land, \n                        should it become necessary shortly after take off, and it is not possible to land \n                        at the departure aerodrome. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 236, 15)))

FlightDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'takeoffWeight'), _ImportedBinding__ff.WeightType, scope=FlightDepartureType, documentation='\n                        .Takeoff Weight: The expected takeoff weight of the aircraft, expressed in thousands \n                        of pounds or kilograms. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 245, 15)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 149, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 157, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 166, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 176, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 183, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 195, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 218, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 236, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 245, 15))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 149, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 157, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureFixTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 166, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureTimes')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 176, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'offBlockReadyTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 183, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 195, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'standPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 218, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'takeoffAlternateAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 236, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(FlightDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'takeoffWeight')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 245, 15))
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
FlightDepartureType._Automaton = _BuildAutomaton_56()




FlightEmergencyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), LastContactType, scope=FlightEmergencyType, documentation='\n                        .Last Contact Unit: The last ATS unit which had two-way contact with the aircraft. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 105, 15)))

FlightEmergencyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'originator'), _ImportedBinding__fb.IdentifiedUnitReferenceType, scope=FlightEmergencyType, documentation='\n                        .Emergency Message Originator: The ICAO identifier of the ATS unit originating the \n                        emergency message. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 113, 15)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 105, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 113, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlightEmergencyType._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 105, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FlightEmergencyType._UseForTag(pyxb.namespace.ExpandedName(None, 'originator')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 113, 15))
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
FlightEmergencyType._Automaton = _BuildAutomaton_57()




LastContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contactFrequency'), _ImportedBinding__fb.RadioFrequencyType, scope=LastContactType, documentation='\n                        .Last Contact Radio Frequency: The transmitting/receiving frequency of the last two-way \n                        contact between the aircraft and an ATS unit. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 170, 15)))

LastContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position'), LastPositionReportType, scope=LastContactType, documentation='\n                        .Last Known Position Report: The position of the aircraft last known to ATS and a \n                        corresponding timestamp. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 178, 15)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 170, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 178, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LastContactType._UseForTag(pyxb.namespace.ExpandedName(None, 'contactFrequency')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 170, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LastContactType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 178, 15))
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
LastContactType._Automaton = _BuildAutomaton_58()




RadioCommunicationFailureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), LastContactType, scope=RadioCommunicationFailureType, documentation='\n                        .Last Contact Unit: The last ATS unit which had two-way contact with the aircraft. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 251, 15)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 251, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RadioCommunicationFailureType._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Emergency.xsd', 251, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RadioCommunicationFailureType._Automaton = _BuildAutomaton_59()




FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'agreed'), TrajectoryRoutePairType, scope=FlightType, documentation='\n                        .Route - Agreed To: The route of flight agreed to by the Airspace User and the Airspace \n                        Provider.  This route is amended as the flight progresses. \n                        .Agreed 4D Trajectory: This trajectory expresses the 4D trajectory agreed to between \n                        the airspace user and the airspace navigation service providers (ANSP) after collaboration \n                        or imposition of pre-collaborated rules. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 150, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aircraftDescription'), AircraftType_, scope=FlightType, documentation='\n                        Describes the details of the aircraft used in the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 161, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrival'), FlightArrivalType, scope=FlightType, documentation='\n                        Contains flight arrival information \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 168, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'controllingUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=FlightType, documentation='\n                        .Controlling Unit: The identifier of the Air Traffic Control unit in control of the \n                        aircraft. \n                        .Controlling Sector: Identifies the ATC sector in control of the aircraft. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 175, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dangerousGoods'), DangerousGoodsType, scope=FlightType, documentation='\n                        Contains information about any board dangerous goods \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 184, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'departure'), FlightDepartureType, scope=FlightType, documentation='\n                        Contains flight departure information \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 191, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emergency'), FlightEmergencyType, scope=FlightType, documentation='\n                        Contains flight emergency linformation \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 198, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'enRoute'), EnRouteType, scope=FlightType, documentation='\n                        Groups the en route information about the flight such as the current position, coordination \n                        between air traffic units, and boundary crossing throughout the duration of the flight. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 205, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'enRouteDiversion'), EnRouteDiversionType, scope=FlightType, documentation='\n                        Contains information about the En Route Diversion of the flight such as diversion \n                        recovery. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 214, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'extensions'), _ImportedBinding__fb.ExtensionType, scope=FlightType, documentation='\n                        Allow to add or redefine the core FIXM elements and create regional scope extensions \n                        such as NAS extension or Eurocontrol extension. This approach is not recommended, \n                        however as the preferred method is to extend individual classes and replace the core \n                        classes where appropriate as described in the FIXM Modeling Best Practices Guide. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 222, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flightIdentification'), FlightIdentificationType, scope=FlightType, documentation='\n                        Groups flight identifying information. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 233, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flightStatus'), FlightStatusType, scope=FlightType, documentation='\n                        Flight Status of the flight containing a set of indicators of the current flight \n                        status. \n                        .Flight Status: Identification of the aspect of the flight life cycle. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 240, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gufi'), _ImportedBinding__fb.GloballyUniqueFlightIdentifierType, scope=FlightType, documentation='\n                        .Globally Unique Flight Identifier: A reference that uniquely identifies a specific \n                        flight and is independent of any particular system. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 249, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'negotiating'), TrajectoryRoutePairType, scope=FlightType, documentation='\n                        .Negotiating 4D Trajectory: The 4D Trajectory used during the collaboration between \n                        the airspace user and the airspace provider to agree on a 4D trajectory. This trajectory \n                        is intended to be transitory. \n                        .Negotiating Route: This Route is used during collaboration between the airspace \n                        user and the airspace providers to agree on a route.  This route field is intended \n                        to be transitory. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 257, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'operator'), AircraftOperatorType, scope=FlightType, documentation='\n                        Contains information about the identify of aircraft operator. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 269, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'originator'), OriginatorType, scope=FlightType, documentation='\n                        Contains information about the flight originator that initiated the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 276, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radioCommunicationFailure'), RadioCommunicationFailureType, scope=FlightType, documentation='\n                        Contains information about radio communication failure \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 283, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rankedTrajectories'), RankedTrajectoryType, scope=FlightType, documentation='\n                        Ranked Trajectories associated with the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 290, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routeToRevisedDestination'), TrajectoryRoutePairType, scope=FlightType, documentation='\n                        .Route - Revised Destination: The route (from some point on the filed route) to the \n                        revised destination aerodrome. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 297, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specialHandling'), STD_ANON_17, scope=FlightType, documentation='\n                        .Special Handling Reason: A property of the flight that requires ATS units to give \n                        it special consideration. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 305, 15)))

FlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'supplementalData'), SupplementalDataType, scope=FlightType, documentation='\n                        Contains the supplemental data about the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 316, 15)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 150, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 161, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 168, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 175, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 184, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 191, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 198, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 205, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 214, 15))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 222, 15))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 233, 15))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 240, 15))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 249, 15))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 257, 15))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 269, 15))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 276, 15))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 283, 15))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 290, 15))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 297, 15))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 305, 15))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 316, 15))
    counters.add(cc_20)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'agreed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 150, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'aircraftDescription')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 161, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrival')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 168, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'controllingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 175, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'dangerousGoods')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 184, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'departure')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 191, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'emergency')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 198, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'enRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 205, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'enRouteDiversion')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 214, 15))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 222, 15))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightIdentification')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 233, 15))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightStatus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 240, 15))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'gufi')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 249, 15))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'negotiating')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 257, 15))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'operator')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 269, 15))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'originator')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 276, 15))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'radioCommunicationFailure')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 283, 15))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'rankedTrajectories')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 290, 15))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeToRevisedDestination')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 297, 15))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'specialHandling')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 305, 15))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(FlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'supplementalData')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 316, 15))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
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
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FlightType._Automaton = _BuildAutomaton_60()




RankedTrajectoryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routeTrajectoryPair'), TrajectoryRoutePairType, scope=RankedTrajectoryType, documentation='\n                  Route Trajectory pair that is the subject of the Trajectory option. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 103, 9)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 103, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RankedTrajectoryType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeTrajectoryPair')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 103, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RankedTrajectoryType._Automaton = _BuildAutomaton_61()




ExpandedRoutePointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constraint'), RouteConstraintOrPreferenceType, scope=ExpandedRoutePointType, documentation='\n                        An Expanded route point may contain an ordered list of constraints. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 239, 15)))

ExpandedRoutePointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'estimatedLevel'), _ImportedBinding__ff.AltitudeType, scope=ExpandedRoutePointType, documentation='\n                        .Expanded Route Point Altitude: The estimated altitude over the expanded route point. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 246, 15)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 239, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 246, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExpandedRoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExpandedRoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 239, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExpandedRoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'estimatedLevel')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 246, 15))
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
ExpandedRoutePointType._Automaton = _BuildAutomaton_62()




RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'climbSchedule'), SpeedScheduleType, scope=RouteType, documentation='\n                        .Speed Schedule - Climb: Initially submitted by the airspace user, this defines the \n                        target speed in both Initial Airspeed (IAS) and MACH so the aircraft can climb through \n                        the crossover altitude and target the MACH speed when needed. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 279, 15)))

RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'descentSchedule'), SpeedScheduleType, scope=RouteType, documentation='\n                        .Speed Schedule - Descent: Initially submitted by the airspace user, this defines \n                        the target speed in both IAS and MACH so the aircraft can descend through the crossover \n                        altitude and target the Initial Airspeed (IAS) speed when needed. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 288, 15)))

RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'estimatedElapsedTime'), EstimatedElapsedTimeType, scope=RouteType, documentation='\n                        .Elapsed Time - Estimated: The estimated amount of time from takeoff to reach a significant \n                        point or Flight Information Region (FIR) boundary along the route of flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 297, 15)))

RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'expandedRoute'), ExpandedRouteType, scope=RouteType, documentation="\n                        A route may contain an optional expanded route where the route consisting of expanded \n                        route points. \n                        .Expanded Route: The expansion of the route into a set of points which describe the \n                        aircraft's expected 2D path from the departure aerodrome to the destination aerodrome. \n                        \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 305, 15)))

RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'initialCruisingSpeed'), _ImportedBinding__ff.TrueAirspeedOrMachType, scope=RouteType, documentation='\n                        .Cruising Speed: The true airspeed for the first or the whole cruising portion of \n                        the flight.  This can be for a filed flight or an active flight.  This element is \n                        strategic in nature. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 316, 15)))

RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'requestedAltitude'), _ImportedBinding__ff.AltitudeType, scope=RouteType, documentation='\n                        .Cruising Altitude - Requested: The filed altitude (flight level) for the first or \n                        the whole cruising portion of the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 325, 15)))

RouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'segment'), RouteSegmentType, scope=RouteType, documentation='\n                        Route consists of an optional ordered list of route segments. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 333, 15)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 279, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 288, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 297, 15))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 305, 15))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 316, 15))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 325, 15))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 333, 15))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'climbSchedule')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 279, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'descentSchedule')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 288, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'estimatedElapsedTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 297, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'expandedRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 305, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'initialCruisingSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 316, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'requestedAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 325, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'segment')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 333, 15))
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
RouteType._Automaton = _BuildAutomaton_63()




RoutePointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constraint'), RouteConstraintOrPreferenceType, scope=RoutePointType, documentation='\n                        A Route point may contain an ordered list of constraints. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 388, 15)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 388, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 388, 15))
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
RoutePointType._Automaton = _BuildAutomaton_64()


Point4D._setSubstitutionGroup(_ImportedBinding__ff.GeographicLocation)

Aircraft._setSubstitutionGroup(_ImportedBinding__fb.Feature)

DangerousGoods._setSubstitutionGroup(_ImportedBinding__fb.Feature)

StructuredPostalAddress._setSubstitutionGroup(_ImportedBinding__ff.ContactInformation)

UnitBoundary._setSubstitutionGroup(_ImportedBinding__fb.AtcUnitReference)

EnRoute._setSubstitutionGroup(_ImportedBinding__fb.Feature)

AircraftPosition._setSubstitutionGroup(_ImportedBinding__fb.Feature)

FlightArrival._setSubstitutionGroup(_ImportedBinding__fb.Feature)

ClimbToLevelConstraint._setSubstitutionGroup(RouteConstraintOrPreference)

LevelConstraint._setSubstitutionGroup(RouteConstraintOrPreference)

SpeedConstraint._setSubstitutionGroup(RouteConstraintOrPreference)

TimeConstraint._setSubstitutionGroup(RouteConstraintOrPreference)

FlightDeparture._setSubstitutionGroup(_ImportedBinding__fb.Feature)

FlightEmergency._setSubstitutionGroup(_ImportedBinding__fb.Feature)

LastContact._setSubstitutionGroup(_ImportedBinding__fb.Feature)

RadioCommunicationFailure._setSubstitutionGroup(_ImportedBinding__fb.Feature)

Flight._setSubstitutionGroup(_ImportedBinding__fb.Feature)

ExpandedRoutePoint._setSubstitutionGroup(AbstractRoutePoint)

Route._setSubstitutionGroup(_ImportedBinding__fb.Feature)

RoutePoint._setSubstitutionGroup(AbstractRoutePoint)

FlightStatus._setSubstitutionGroup(_ImportedBinding__fb.Feature)
