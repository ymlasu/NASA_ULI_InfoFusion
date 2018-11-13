# .\nas.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b4ab58b58de02ace10f0a450a0f48be030d1c341
# Generated 2018-08-28 14:52:08.000776 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace http://www.faa.aero/nas/3.0

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
import _fx as _ImportedBinding__fx

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.faa.aero/nas/3.0', create_if_missing=True)
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


# Atomic simple type: {http://www.faa.aero/nas/3.0}CmsAccuracyTypeType
class CmsAccuracyTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Performance-Based Navigation Category: This is an enumeration indicating whether 
            the accuracy measure in Performance-Based Navigation Accuracy is measuring Area Navigation 
            (RNAV) or Required Navigation Performance (RNP). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CmsAccuracyTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 95, 3)
    _Documentation = '\n            .Performance-Based Navigation Category: This is an enumeration indicating whether \n            the accuracy measure in Performance-Based Navigation Accuracy is measuring Area Navigation \n            (RNAV) or Required Navigation Performance (RNP). \n         '
CmsAccuracyTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CmsAccuracyTypeType, enum_prefix=None)
CmsAccuracyTypeType.RNV = CmsAccuracyTypeType._CF_enumeration.addEnumeration(unicode_value='RNV', tag='RNV')
CmsAccuracyTypeType.RNP = CmsAccuracyTypeType._CF_enumeration.addEnumeration(unicode_value='RNP', tag='RNP')
CmsAccuracyTypeType._InitializeFacetMap(CmsAccuracyTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CmsAccuracyTypeType', CmsAccuracyTypeType)
_module_typeBindings.CmsAccuracyTypeType = CmsAccuracyTypeType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasAirborneEquipmentQualifierType
class NasAirborneEquipmentQualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Airborne Equipment Qualifier: A value assigned to the aircraft, based on its navigational 
            equipment, whether or not it has a transponder, and if it has a transponder, whether 
            the transponder supports Mode C. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAirborneEquipmentQualifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 109, 3)
    _Documentation = '\n            .Airborne Equipment Qualifier: A value assigned to the aircraft, based on its navigational \n            equipment, whether or not it has a transponder, and if it has a transponder, whether \n            the transponder supports Mode C. \n         '
NasAirborneEquipmentQualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasAirborneEquipmentQualifierType, enum_prefix=None)
NasAirborneEquipmentQualifierType.X = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='X', tag='X')
NasAirborneEquipmentQualifierType.T = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
NasAirborneEquipmentQualifierType.U = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='U', tag='U')
NasAirborneEquipmentQualifierType.D = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
NasAirborneEquipmentQualifierType.B = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
NasAirborneEquipmentQualifierType.A = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
NasAirborneEquipmentQualifierType.M = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
NasAirborneEquipmentQualifierType.N = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
NasAirborneEquipmentQualifierType.P = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
NasAirborneEquipmentQualifierType.Y = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='Y', tag='Y')
NasAirborneEquipmentQualifierType.C = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
NasAirborneEquipmentQualifierType.I = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='I', tag='I')
NasAirborneEquipmentQualifierType.H = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
NasAirborneEquipmentQualifierType.S = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
NasAirborneEquipmentQualifierType.G = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
NasAirborneEquipmentQualifierType.V = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
NasAirborneEquipmentQualifierType.Z = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='Z', tag='Z')
NasAirborneEquipmentQualifierType.L = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
NasAirborneEquipmentQualifierType.W = NasAirborneEquipmentQualifierType._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
NasAirborneEquipmentQualifierType._InitializeFacetMap(NasAirborneEquipmentQualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasAirborneEquipmentQualifierType', NasAirborneEquipmentQualifierType)
_module_typeBindings.NasAirborneEquipmentQualifierType = NasAirborneEquipmentQualifierType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasPerformanceBasedNavigationPhaseType
class NasPerformanceBasedNavigationPhaseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Performance-Based Navigation Phase: The phase of flight for which navigation performance 
            is being recorded. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasPerformanceBasedNavigationPhaseType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 340, 3)
    _Documentation = '\n            .Performance-Based Navigation Phase: The phase of flight for which navigation performance \n            is being recorded. \n         '
NasPerformanceBasedNavigationPhaseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasPerformanceBasedNavigationPhaseType, enum_prefix=None)
NasPerformanceBasedNavigationPhaseType.DEPARTURE = NasPerformanceBasedNavigationPhaseType._CF_enumeration.addEnumeration(unicode_value='DEPARTURE', tag='DEPARTURE')
NasPerformanceBasedNavigationPhaseType.ARRIVAL = NasPerformanceBasedNavigationPhaseType._CF_enumeration.addEnumeration(unicode_value='ARRIVAL', tag='ARRIVAL')
NasPerformanceBasedNavigationPhaseType.ENROUTE = NasPerformanceBasedNavigationPhaseType._CF_enumeration.addEnumeration(unicode_value='ENROUTE', tag='ENROUTE')
NasPerformanceBasedNavigationPhaseType.OCEANIC = NasPerformanceBasedNavigationPhaseType._CF_enumeration.addEnumeration(unicode_value='OCEANIC', tag='OCEANIC')
NasPerformanceBasedNavigationPhaseType.SPARE_1 = NasPerformanceBasedNavigationPhaseType._CF_enumeration.addEnumeration(unicode_value='SPARE_1', tag='SPARE_1')
NasPerformanceBasedNavigationPhaseType.SPARE_2 = NasPerformanceBasedNavigationPhaseType._CF_enumeration.addEnumeration(unicode_value='SPARE_2', tag='SPARE_2')
NasPerformanceBasedNavigationPhaseType._InitializeFacetMap(NasPerformanceBasedNavigationPhaseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasPerformanceBasedNavigationPhaseType', NasPerformanceBasedNavigationPhaseType)
_module_typeBindings.NasPerformanceBasedNavigationPhaseType = NasPerformanceBasedNavigationPhaseType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasSpecialAircraftQualifierType
class NasSpecialAircraftQualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Special Aircraft Qualifier: Indicates the flight is a heavy jet, B757 or, if not 
            present, a large jet and if the flight is either equipped or not with TCAS. This 
            indicator is used for output purposes such as strip printing and message transfers 
            to other facilities such as Automated Radar Terminal System (ARTS). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasSpecialAircraftQualifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 357, 3)
    _Documentation = '\n            .Special Aircraft Qualifier: Indicates the flight is a heavy jet, B757 or, if not \n            present, a large jet and if the flight is either equipped or not with TCAS. This \n            indicator is used for output purposes such as strip printing and message transfers \n            to other facilities such as Automated Radar Terminal System (ARTS). \n         '
NasSpecialAircraftQualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasSpecialAircraftQualifierType, enum_prefix=None)
NasSpecialAircraftQualifierType.HEAVY_JET = NasSpecialAircraftQualifierType._CF_enumeration.addEnumeration(unicode_value='HEAVY_JET', tag='HEAVY_JET')
NasSpecialAircraftQualifierType.TCAS = NasSpecialAircraftQualifierType._CF_enumeration.addEnumeration(unicode_value='TCAS', tag='TCAS')
NasSpecialAircraftQualifierType.B757 = NasSpecialAircraftQualifierType._CF_enumeration.addEnumeration(unicode_value='B757', tag='B757')
NasSpecialAircraftQualifierType.B757_TCAS = NasSpecialAircraftQualifierType._CF_enumeration.addEnumeration(unicode_value='B757_TCAS', tag='B757_TCAS')
NasSpecialAircraftQualifierType.HEAVY_JET_AND_TCAS = NasSpecialAircraftQualifierType._CF_enumeration.addEnumeration(unicode_value='HEAVY_JET_AND_TCAS', tag='HEAVY_JET_AND_TCAS')
NasSpecialAircraftQualifierType._InitializeFacetMap(NasSpecialAircraftQualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasSpecialAircraftQualifierType', NasSpecialAircraftQualifierType)
_module_typeBindings.NasSpecialAircraftQualifierType = NasSpecialAircraftQualifierType

# Atomic simple type: {http://www.faa.aero/nas/3.0}WakeTurbulenceCategoryExtendedType
class WakeTurbulenceCategoryExtendedType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Wake Turbulence Category - NAS: NAS classification of the aircraft wake turbulence, 
            based on wingspan and Maximum Takeoff Weight (MTOW). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WakeTurbulenceCategoryExtendedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 408, 3)
    _Documentation = '\n            .Wake Turbulence Category - NAS: NAS classification of the aircraft wake turbulence, \n            based on wingspan and Maximum Takeoff Weight (MTOW). \n         '
WakeTurbulenceCategoryExtendedType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WakeTurbulenceCategoryExtendedType, enum_prefix=None)
WakeTurbulenceCategoryExtendedType.A = WakeTurbulenceCategoryExtendedType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
WakeTurbulenceCategoryExtendedType.B = WakeTurbulenceCategoryExtendedType._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
WakeTurbulenceCategoryExtendedType.C = WakeTurbulenceCategoryExtendedType._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
WakeTurbulenceCategoryExtendedType.D = WakeTurbulenceCategoryExtendedType._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
WakeTurbulenceCategoryExtendedType.E = WakeTurbulenceCategoryExtendedType._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
WakeTurbulenceCategoryExtendedType.F = WakeTurbulenceCategoryExtendedType._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
WakeTurbulenceCategoryExtendedType._InitializeFacetMap(WakeTurbulenceCategoryExtendedType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WakeTurbulenceCategoryExtendedType', WakeTurbulenceCategoryExtendedType)
_module_typeBindings.WakeTurbulenceCategoryExtendedType = WakeTurbulenceCategoryExtendedType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasHandoffEventType
class NasHandoffEventType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Handoff Event Category: Characterizes a handoff in terms of its status. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasHandoffEventType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 94, 3)
    _Documentation = '\n            .Handoff Event Category: Characterizes a handoff in terms of its status. \n         '
NasHandoffEventType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasHandoffEventType, enum_prefix=None)
NasHandoffEventType.INITIATION = NasHandoffEventType._CF_enumeration.addEnumeration(unicode_value='INITIATION', tag='INITIATION')
NasHandoffEventType.ACCEPTANCE = NasHandoffEventType._CF_enumeration.addEnumeration(unicode_value='ACCEPTANCE', tag='ACCEPTANCE')
NasHandoffEventType.RETRACTION = NasHandoffEventType._CF_enumeration.addEnumeration(unicode_value='RETRACTION', tag='RETRACTION')
NasHandoffEventType.TAKE_CONTROL = NasHandoffEventType._CF_enumeration.addEnumeration(unicode_value='TAKE_CONTROL', tag='TAKE_CONTROL')
NasHandoffEventType.UPDATE = NasHandoffEventType._CF_enumeration.addEnumeration(unicode_value='UPDATE', tag='UPDATE')
NasHandoffEventType.FAILURE = NasHandoffEventType._CF_enumeration.addEnumeration(unicode_value='FAILURE', tag='FAILURE')
NasHandoffEventType._InitializeFacetMap(NasHandoffEventType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasHandoffEventType', NasHandoffEventType)
_module_typeBindings.NasHandoffEventType = NasHandoffEventType

# Atomic simple type: {http://www.faa.aero/nas/3.0}ClassifiedSpeedIndicatorType
class ClassifiedSpeedIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Classified Speed Indicator: The indication that the speed for this flight is classified 
            and is not to be recorded. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClassifiedSpeedIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 67, 3)
    _Documentation = '\n            .Classified Speed Indicator: The indication that the speed for this flight is classified \n            and is not to be recorded. \n         '
ClassifiedSpeedIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ClassifiedSpeedIndicatorType, enum_prefix=None)
ClassifiedSpeedIndicatorType.CLASSIFIED = ClassifiedSpeedIndicatorType._CF_enumeration.addEnumeration(unicode_value='CLASSIFIED', tag='CLASSIFIED')
ClassifiedSpeedIndicatorType._InitializeFacetMap(ClassifiedSpeedIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ClassifiedSpeedIndicatorType', ClassifiedSpeedIndicatorType)
_module_typeBindings.ClassifiedSpeedIndicatorType = ClassifiedSpeedIndicatorType

# Atomic simple type: {http://www.faa.aero/nas/3.0}CoordinationTimeTypeType
class CoordinationTimeTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Coordination Time Type: The indicator for the type of   Coordination Time  . 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoordinationTimeTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 79, 3)
    _Documentation = '\n            .Coordination Time Type: The indicator for the type of   Coordination Time  . \n         '
CoordinationTimeTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CoordinationTimeTypeType, enum_prefix=None)
CoordinationTimeTypeType.P = CoordinationTimeTypeType._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
CoordinationTimeTypeType.D = CoordinationTimeTypeType._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
CoordinationTimeTypeType.E = CoordinationTimeTypeType._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
CoordinationTimeTypeType._InitializeFacetMap(CoordinationTimeTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CoordinationTimeTypeType', CoordinationTimeTypeType)
_module_typeBindings.CoordinationTimeTypeType = CoordinationTimeTypeType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasFlightClassType
class NasFlightClassType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Flight Class: Denotes the flight class of the aircraft which is determined by the 
            aircraft call sign that is in the Aircraft Situation Display to Industry (ASDI) feed. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasFlightClassType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 302, 3)
    _Documentation = '\n            .Flight Class: Denotes the flight class of the aircraft which is determined by the \n            aircraft call sign that is in the Aircraft Situation Display to Industry (ASDI) feed. \n            \n         '
NasFlightClassType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasFlightClassType, enum_prefix=None)
NasFlightClassType.GA = NasFlightClassType._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
NasFlightClassType.LIFEGUARD = NasFlightClassType._CF_enumeration.addEnumeration(unicode_value='LIFEGUARD', tag='LIFEGUARD')
NasFlightClassType.TAXI = NasFlightClassType._CF_enumeration.addEnumeration(unicode_value='TAXI', tag='TAXI')
NasFlightClassType.CANADIAN_GA = NasFlightClassType._CF_enumeration.addEnumeration(unicode_value='CANADIAN_GA', tag='CANADIAN_GA')
NasFlightClassType.MILITARY = NasFlightClassType._CF_enumeration.addEnumeration(unicode_value='MILITARY', tag='MILITARY')
NasFlightClassType._InitializeFacetMap(NasFlightClassType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasFlightClassType', NasFlightClassType)
_module_typeBindings.NasFlightClassType = NasFlightClassType

# Atomic simple type: {http://www.faa.aero/nas/3.0}RVSMFlightIndicatorType
class RVSMFlightIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Current and Future RVSM Flight Compliance 
            .Future RVSM Flight Compliance: Indicates if the flight will beReduced Vertical Separation 
            Minimum (RVSM) compliant when it reaches the RVSM airspace as determined by the Traffic 
            Flow Management System (TFMS). 
            .Current RVSM Flight Compliance: Indicates if the flight is currently Reduced Vertical 
            Separation Minimum (RVSM) compliant in RVSM airspace, as determined by the Traffic 
            Flow Management System. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RVSMFlightIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 406, 3)
    _Documentation = '\n            Current and Future RVSM Flight Compliance \n            .Future RVSM Flight Compliance: Indicates if the flight will beReduced Vertical Separation \n            Minimum (RVSM) compliant when it reaches the RVSM airspace as determined by the Traffic \n            Flow Management System (TFMS). \n            .Current RVSM Flight Compliance: Indicates if the flight is currently Reduced Vertical \n            Separation Minimum (RVSM) compliant in RVSM airspace, as determined by the Traffic \n            Flow Management System. \n         '
RVSMFlightIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RVSMFlightIndicatorType, enum_prefix=None)
RVSMFlightIndicatorType.COMPLIANT = RVSMFlightIndicatorType._CF_enumeration.addEnumeration(unicode_value='COMPLIANT', tag='COMPLIANT')
RVSMFlightIndicatorType._InitializeFacetMap(RVSMFlightIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RVSMFlightIndicatorType', RVSMFlightIndicatorType)
_module_typeBindings.RVSMFlightIndicatorType = RVSMFlightIndicatorType

# Atomic simple type: {http://www.faa.aero/nas/3.0}DeicingIntentType
class DeicingIntentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Deicing Intent: Indicates the intent for the flight to be deiced. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeicingIntentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 124, 3)
    _Documentation = '\n            .Deicing Intent: Indicates the intent for the flight to be deiced. \n         '
DeicingIntentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeicingIntentType, enum_prefix=None)
DeicingIntentType.DEICE = DeicingIntentType._CF_enumeration.addEnumeration(unicode_value='DEICE', tag='DEICE')
DeicingIntentType.NO_DEICE = DeicingIntentType._CF_enumeration.addEnumeration(unicode_value='NO_DEICE', tag='NO_DEICE')
DeicingIntentType._InitializeFacetMap(DeicingIntentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeicingIntentType', DeicingIntentType)
_module_typeBindings.DeicingIntentType = DeicingIntentType

# Atomic simple type: {http://www.faa.aero/nas/3.0}HoldIntentType
class HoldIntentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Airport Movement Area Holding Intent - Departure: Indicates the intent for a departing 
            flight to hold in the airport movement area when surface departure metering or other 
            Traffic Management Initiatives are in effect. 
            .Airport Movement Area Holding Intent - Arrival: Indicates the intent for an arriving 
            flight to hold in the airport movement area due to unavailability of a parking stand 
            or ramp access. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoldIntentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 259, 3)
    _Documentation = '\n            .Airport Movement Area Holding Intent - Departure: Indicates the intent for a departing \n            flight to hold in the airport movement area when surface departure metering or other \n            Traffic Management Initiatives are in effect. \n            .Airport Movement Area Holding Intent - Arrival: Indicates the intent for an arriving \n            flight to hold in the airport movement area due to unavailability of a parking stand \n            or ramp access. \n         '
HoldIntentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HoldIntentType, enum_prefix=None)
HoldIntentType.HOLD = HoldIntentType._CF_enumeration.addEnumeration(unicode_value='HOLD', tag='HOLD')
HoldIntentType.NO_HOLD = HoldIntentType._CF_enumeration.addEnumeration(unicode_value='NO_HOLD', tag='NO_HOLD')
HoldIntentType._InitializeFacetMap(HoldIntentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HoldIntentType', HoldIntentType)
_module_typeBindings.HoldIntentType = HoldIntentType

# Atomic simple type: {http://www.faa.aero/nas/3.0}StandReturnIntentType
class StandReturnIntentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Stand Return Intent: Indicates the intent for the flight to return to the stand. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandReturnIntentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 300, 3)
    _Documentation = '\n            .Stand Return Intent: Indicates the intent for the flight to return to the stand. \n            \n         '
StandReturnIntentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StandReturnIntentType, enum_prefix=None)
StandReturnIntentType.RETURN = StandReturnIntentType._CF_enumeration.addEnumeration(unicode_value='RETURN', tag='RETURN')
StandReturnIntentType.NO_RETURN = StandReturnIntentType._CF_enumeration.addEnumeration(unicode_value='NO_RETURN', tag='NO_RETURN')
StandReturnIntentType._InitializeFacetMap(StandReturnIntentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StandReturnIntentType', StandReturnIntentType)
_module_typeBindings.StandReturnIntentType = StandReturnIntentType

# Atomic simple type: {http://www.faa.aero/nas/3.0}InvalidIndicatorType
class InvalidIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Indicates whether target altitude is invalid. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvalidIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 64, 3)
    _Documentation = '\n            Indicates whether target altitude is invalid. \n         '
InvalidIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvalidIndicatorType, enum_prefix=None)
InvalidIndicatorType.INVALID = InvalidIndicatorType._CF_enumeration.addEnumeration(unicode_value='INVALID', tag='INVALID')
InvalidIndicatorType._InitializeFacetMap(InvalidIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvalidIndicatorType', InvalidIndicatorType)
_module_typeBindings.InvalidIndicatorType = InvalidIndicatorType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasCoastIndicatorType
class NasCoastIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Coast Indicator: An indicator the aircraft was unexpectedly not detected by radar 
            (after a period of tracking). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasCoastIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 131, 3)
    _Documentation = '\n            .Coast Indicator: An indicator the aircraft was unexpectedly not detected by radar \n            (after a period of tracking). \n         '
NasCoastIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasCoastIndicatorType, enum_prefix=None)
NasCoastIndicatorType.COASTING = NasCoastIndicatorType._CF_enumeration.addEnumeration(unicode_value='COASTING', tag='COASTING')
NasCoastIndicatorType._InitializeFacetMap(NasCoastIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasCoastIndicatorType', NasCoastIndicatorType)
_module_typeBindings.NasCoastIndicatorType = NasCoastIndicatorType

# Atomic simple type: {http://www.faa.aero/nas/3.0}NasFlightRulesType
class NasFlightRulesType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Flight Rules - NAS: The regulation, or combination of regulations, that governs 
            all aspects of operations under which the pilot plans to fly in the NAS. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasFlightRulesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 168, 3)
    _Documentation = '\n            .Flight Rules - NAS: The regulation, or combination of regulations, that governs \n            all aspects of operations under which the pilot plans to fly in the NAS. \n         '
NasFlightRulesType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NasFlightRulesType, enum_prefix=None)
NasFlightRulesType.IFR = NasFlightRulesType._CF_enumeration.addEnumeration(unicode_value='IFR', tag='IFR')
NasFlightRulesType.VFR = NasFlightRulesType._CF_enumeration.addEnumeration(unicode_value='VFR', tag='VFR')
NasFlightRulesType.DVFR = NasFlightRulesType._CF_enumeration.addEnumeration(unicode_value='DVFR', tag='DVFR')
NasFlightRulesType._InitializeFacetMap(NasFlightRulesType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NasFlightRulesType', NasFlightRulesType)
_module_typeBindings.NasFlightRulesType = NasFlightRulesType

# Atomic simple type: {http://www.faa.aero/nas/3.0}SfdpsFlightStatusType
class SfdpsFlightStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Represents the current status of the flight as specified by the SWIM SFDPS. 
            .SFDPS Flight Status: Identification of the current aspect of the flight life cycle 
            as determined by the SWIM Flight Data Publication Service (SFDPS). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SfdpsFlightStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 92, 3)
    _Documentation = '\n            Represents the current status of the flight as specified by the SWIM SFDPS. \n            .SFDPS Flight Status: Identification of the current aspect of the flight life cycle \n            as determined by the SWIM Flight Data Publication Service (SFDPS). \n         '
SfdpsFlightStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SfdpsFlightStatusType, enum_prefix=None)
SfdpsFlightStatusType.PROPOSED = SfdpsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='PROPOSED', tag='PROPOSED')
SfdpsFlightStatusType.ACTIVE = SfdpsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='ACTIVE', tag='ACTIVE')
SfdpsFlightStatusType.COMPLETED = SfdpsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='COMPLETED', tag='COMPLETED')
SfdpsFlightStatusType.CANCELLED = SfdpsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='CANCELLED', tag='CANCELLED')
SfdpsFlightStatusType.DROPPED = SfdpsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='DROPPED', tag='DROPPED')
SfdpsFlightStatusType._InitializeFacetMap(SfdpsFlightStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SfdpsFlightStatusType', SfdpsFlightStatusType)
_module_typeBindings.SfdpsFlightStatusType = SfdpsFlightStatusType

# Atomic simple type: {http://www.faa.aero/nas/3.0}TfmsFlightStatusType
class TfmsFlightStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Traffic Flow Management System Flight Status: Indicates the current status of the 
            flight, as determined by Traffic Flow Management System (TFMS). 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TfmsFlightStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 142, 3)
    _Documentation = '\n            .Traffic Flow Management System Flight Status: Indicates the current status of the \n            flight, as determined by Traffic Flow Management System (TFMS). \n         '
TfmsFlightStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TfmsFlightStatusType, enum_prefix=None)
TfmsFlightStatusType.SCHEDULED = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='SCHEDULED', tag='SCHEDULED')
TfmsFlightStatusType.CONTROLLED = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='CONTROLLED', tag='CONTROLLED')
TfmsFlightStatusType.FILED = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='FILED', tag='FILED')
TfmsFlightStatusType.ACTIVE = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='ACTIVE', tag='ACTIVE')
TfmsFlightStatusType.ASCENDING = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='ASCENDING', tag='ASCENDING')
TfmsFlightStatusType.CRUISING = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='CRUISING', tag='CRUISING')
TfmsFlightStatusType.DESCENDING = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='DESCENDING', tag='DESCENDING')
TfmsFlightStatusType.COMPLETED = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='COMPLETED', tag='COMPLETED')
TfmsFlightStatusType.CANCELLED = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='CANCELLED', tag='CANCELLED')
TfmsFlightStatusType.DECONTROLLED = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='DECONTROLLED', tag='DECONTROLLED')
TfmsFlightStatusType.UNKNOWN = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
TfmsFlightStatusType.NONE = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
TfmsFlightStatusType.ERROR = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
TfmsFlightStatusType.OTHER = TfmsFlightStatusType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
TfmsFlightStatusType._InitializeFacetMap(TfmsFlightStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TfmsFlightStatusType', TfmsFlightStatusType)
_module_typeBindings.TfmsFlightStatusType = TfmsFlightStatusType

# Atomic simple type: {http://www.faa.aero/nas/3.0}AdvisoryTypeType
class AdvisoryTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Traffic Flow Management Advisory Number: Advisory number issued by traffic flow 
            management. 
            .Traffic Flow Management Advisory Type: The type for the advisory issued by traffic 
            flow management. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdvisoryTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 61, 3)
    _Documentation = '\n            .Traffic Flow Management Advisory Number: Advisory number issued by traffic flow \n            management. \n            .Traffic Flow Management Advisory Type: The type for the advisory issued by traffic \n            flow management. \n         '
AdvisoryTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AdvisoryTypeType, enum_prefix=None)
AdvisoryTypeType.GDP = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='GDP', tag='GDP')
AdvisoryTypeType.AFP = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='AFP', tag='AFP')
AdvisoryTypeType.GDP_CANCEL = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='GDP_CANCEL', tag='GDP_CANCEL')
AdvisoryTypeType.AFP_CANCEL = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='AFP_CANCEL', tag='AFP_CANCEL')
AdvisoryTypeType.GS = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
AdvisoryTypeType.GS_CANCEL = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='GS_CANCEL', tag='GS_CANCEL')
AdvisoryTypeType.REROUTE = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='REROUTE', tag='REROUTE')
AdvisoryTypeType.CTOP = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='CTOP', tag='CTOP')
AdvisoryTypeType.CTOP_CANCEL = AdvisoryTypeType._CF_enumeration.addEnumeration(unicode_value='CTOP_CANCEL', tag='CTOP_CANCEL')
AdvisoryTypeType._InitializeFacetMap(AdvisoryTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AdvisoryTypeType', AdvisoryTypeType)
_module_typeBindings.AdvisoryTypeType = AdvisoryTypeType

# Atomic simple type: {http://www.faa.aero/nas/3.0}RerouteInclusionIndicatorType
class RerouteInclusionIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Traffic Flow Management System Reroute Inclusion Indicator: Indicates whether the 
            flight is included or proposed to be included in the traffic management reroute initiative. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RerouteInclusionIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 287, 3)
    _Documentation = '\n            .Traffic Flow Management System Reroute Inclusion Indicator: Indicates whether the \n            flight is included or proposed to be included in the traffic management reroute initiative. \n            \n         '
RerouteInclusionIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RerouteInclusionIndicatorType, enum_prefix=None)
RerouteInclusionIndicatorType.INCLUDED = RerouteInclusionIndicatorType._CF_enumeration.addEnumeration(unicode_value='INCLUDED', tag='INCLUDED')
RerouteInclusionIndicatorType._InitializeFacetMap(RerouteInclusionIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RerouteInclusionIndicatorType', RerouteInclusionIndicatorType)
_module_typeBindings.RerouteInclusionIndicatorType = RerouteInclusionIndicatorType

# Atomic simple type: {http://www.faa.aero/nas/3.0}RerouteTypeType
class RerouteTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Traffic Flow Management System Reroute Identifier: Traffic Flow Management System 
            generated unique identifier for the reroute. 
            .Traffic Flow Management System Reroute Name: Traffic Flow Management System assigned 
            name for the reroute. 
            .Traffic Flow Management System Reroute Type: Route type of the assigned reroute. 
            
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RerouteTypeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 307, 3)
    _Documentation = '\n            .Traffic Flow Management System Reroute Identifier: Traffic Flow Management System \n            generated unique identifier for the reroute. \n            .Traffic Flow Management System Reroute Name: Traffic Flow Management System assigned \n            name for the reroute. \n            .Traffic Flow Management System Reroute Type: Route type of the assigned reroute. \n            \n         '
RerouteTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RerouteTypeType, enum_prefix=None)
RerouteTypeType.BLANK = RerouteTypeType._CF_enumeration.addEnumeration(unicode_value='BLANK', tag='BLANK')
RerouteTypeType.CDR_RTE = RerouteTypeType._CF_enumeration.addEnumeration(unicode_value='CDR_RTE', tag='CDR_RTE')
RerouteTypeType.REROUTE = RerouteTypeType._CF_enumeration.addEnumeration(unicode_value='REROUTE', tag='REROUTE')
RerouteTypeType.UPT_RTE = RerouteTypeType._CF_enumeration.addEnumeration(unicode_value='UPT_RTE', tag='UPT_RTE')
RerouteTypeType.UNKNOWN = RerouteTypeType._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
RerouteTypeType._InitializeFacetMap(RerouteTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RerouteTypeType', RerouteTypeType)
_module_typeBindings.RerouteTypeType = RerouteTypeType

# Atomic simple type: {http://www.faa.aero/nas/3.0}SlotHoldStatusType
class SlotHoldStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Slot Hold Status: If a flight is controlled and cancelled [e.g., has a Controlled 
            Time of Departure (CTD), Controlled Time of Arrival (CTA), and Arrival Slot (ASLOT)], 
            the slot hold status indicates whether the slot associated with this flight is being 
            held, or would be held, by the Airspace User for the next full compression. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SlotHoldStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 357, 3)
    _Documentation = '\n            .Slot Hold Status: If a flight is controlled and cancelled [e.g., has a Controlled \n            Time of Departure (CTD), Controlled Time of Arrival (CTA), and Arrival Slot (ASLOT)], \n            the slot hold status indicates whether the slot associated with this flight is being \n            held, or would be held, by the Airspace User for the next full compression. \n         '
SlotHoldStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SlotHoldStatusType, enum_prefix=None)
SlotHoldStatusType.HOLD = SlotHoldStatusType._CF_enumeration.addEnumeration(unicode_value='HOLD', tag='HOLD')
SlotHoldStatusType.RELEASE = SlotHoldStatusType._CF_enumeration.addEnumeration(unicode_value='RELEASE', tag='RELEASE')
SlotHoldStatusType._InitializeFacetMap(SlotHoldStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SlotHoldStatusType', SlotHoldStatusType)
_module_typeBindings.SlotHoldStatusType = SlotHoldStatusType

# Atomic simple type: {http://www.faa.aero/nas/3.0}SlotYieldedIndicatorType
class SlotYieldedIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Yielded Slot Indicator: Indicates the slot currently specified in   Runway Arrival 
            Time - Controlled   is to be given up by the Airspace User in return for a later 
            slot. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SlotYieldedIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 372, 3)
    _Documentation = '\n            .Yielded Slot Indicator: Indicates the slot currently specified in   Runway Arrival \n            Time - Controlled   is to be given up by the Airspace User in return for a later \n            slot. \n         '
SlotYieldedIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SlotYieldedIndicatorType, enum_prefix=None)
SlotYieldedIndicatorType.SLOT_YIELDED = SlotYieldedIndicatorType._CF_enumeration.addEnumeration(unicode_value='SLOT_YIELDED', tag='SLOT_YIELDED')
SlotYieldedIndicatorType._InitializeFacetMap(SlotYieldedIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SlotYieldedIndicatorType', SlotYieldedIndicatorType)
_module_typeBindings.SlotYieldedIndicatorType = SlotYieldedIndicatorType

# Atomic simple type: {http://www.faa.aero/nas/3.0}ManualOverrideIndicatorType
class ManualOverrideIndicatorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            .Trajectory Manual Override Status: An indication whether a trajectory was either 
            selected manually by a traffic manager from the available trajectory options or was 
            entered manually by a traffic manager. 
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManualOverrideIndicatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 92, 3)
    _Documentation = '\n            .Trajectory Manual Override Status: An indication whether a trajectory was either \n            selected manually by a traffic manager from the available trajectory options or was \n            entered manually by a traffic manager. \n         '
ManualOverrideIndicatorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ManualOverrideIndicatorType, enum_prefix=None)
ManualOverrideIndicatorType.MANUAL_OVERRRIDE = ManualOverrideIndicatorType._CF_enumeration.addEnumeration(unicode_value='MANUAL_OVERRRIDE', tag='MANUAL_OVERRRIDE')
ManualOverrideIndicatorType._InitializeFacetMap(ManualOverrideIndicatorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ManualOverrideIndicatorType', ManualOverrideIndicatorType)
_module_typeBindings.ManualOverrideIndicatorType = ManualOverrideIndicatorType

# Atomic simple type: [anonymous]
class STD_ANON (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 96, 15)
    _Documentation = None
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength,
   STD_ANON._CF_maxLength)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 95, 15)
    _Documentation = None
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minLength,
   STD_ANON_._CF_maxLength)
_module_typeBindings.STD_ANON_ = STD_ANON_

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_2 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of _ImportedBinding__fb.FreeTextType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 84, 18)
    _Documentation = None

    _ItemType = _ImportedBinding__fb.FreeTextType
STD_ANON_2._InitializeFacetMap()
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 131, 9)
    _Documentation = None
STD_ANON_3._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_3._CF_pattern.addPattern(pattern='[A-Z0-9/\\-\\?\\(\\)\\.,=\\+ ]{5}')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_pattern)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 271, 15)
    _Documentation = None
STD_ANON_4._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_4._CF_pattern.addPattern(pattern='[A-Z0-9/\\.\\+\\*&lt;&gt;]+')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_pattern)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_5 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of _ImportedBinding__ff.AtsRouteType."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 353, 12)
    _Documentation = None

    _ItemType = _ImportedBinding__ff.AtsRouteType
STD_ANON_5._InitializeFacetMap()
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 193, 9)
    _Documentation = None
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_minLength,
   STD_ANON_6._CF_maxLength)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 220, 9)
    _Documentation = None
STD_ANON_7._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON_7._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_minLength,
   STD_ANON_7._CF_maxLength)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 234, 9)
    _Documentation = None
STD_ANON_8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1000))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_minLength,
   STD_ANON_8._CF_maxLength)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 136, 15)
    _Documentation = None
STD_ANON_9._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_9._CF_pattern.addPattern(pattern='CTP\\d{3}')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_pattern)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (_ImportedBinding__fb.FreeTextType):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 152, 15)
    _Documentation = None
STD_ANON_10._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_minLength,
   STD_ANON_10._CF_maxLength)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Complex type {http://www.faa.aero/nas/3.0}NasPerformanceBasedAccuracyType with content type ELEMENT_ONLY
class NasPerformanceBasedAccuracyType (pyxb.binding.basis.complexTypeDefinition):
    """
            NAS extension for Performance-Based Navigation Accuracy. 
            
            .Performance-Based Navigation Accuracy: This is the flight's navigation accuracy 
            value for the phase of flight, specified in the Performance-Based Navigation Phase. 
            
            .Performance-Based Navigation Category: This is an enumeration indicating whether 
            the accuracy measure in Performance-Based Navigation Accuracy is measuring Area Navigation 
            (RNAV) or Required Navigation Performance (RNP). 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasPerformanceBasedAccuracyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 313, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cmsFieldType uses Python identifier cmsFieldType
    __cmsFieldType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cmsFieldType'), 'cmsFieldType', '__httpwww_faa_aeronas3_0_NasPerformanceBasedAccuracyType_cmsFieldType', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 327, 9), )

    
    cmsFieldType = property(__cmsFieldType.value, __cmsFieldType.set, None, "\n                  .Performance-Based Navigation Accuracy: This is the flight's navigation accuracy \n                  value for the phase of flight, specified in the Performance-Based Navigation Phase. \n                  \n               ")

    _ElementMap.update({
        __cmsFieldType.name() : __cmsFieldType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasPerformanceBasedAccuracyType = NasPerformanceBasedAccuracyType
Namespace.addCategoryObject('typeBinding', 'NasPerformanceBasedAccuracyType', NasPerformanceBasedAccuracyType)


# Complex type {http://www.faa.aero/nas/3.0}AltFixAltAltitudeType with content type ELEMENT_ONLY
class AltFixAltAltitudeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Alt-fix-alt altitude is defined as an altitude prior to a specified fix, the specified 
            fix itself, and altitude post specified fix. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AltFixAltAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 73, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__httpwww_faa_aeronas3_0_AltFixAltAltitudeType_point', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 81, 9), )

    
    point = property(__point.value, __point.set, None, '\n                  Fix associated with the altitude \n               ')

    
    # Element post uses Python identifier post
    __post = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'post'), 'post', '__httpwww_faa_aeronas3_0_AltFixAltAltitudeType_post', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 88, 9), )

    
    post = property(__post.value, __post.set, None, '\n                  Altitude post the specified fix. \n               ')

    
    # Element pre uses Python identifier pre
    __pre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pre'), 'pre', '__httpwww_faa_aeronas3_0_AltFixAltAltitudeType_pre', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 95, 9), )

    
    pre = property(__pre.value, __pre.set, None, '\n                  Altitude pre specified fix. \n               ')

    _ElementMap.update({
        __point.name() : __point,
        __post.name() : __post,
        __pre.name() : __pre
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AltFixAltAltitudeType = AltFixAltAltitudeType
Namespace.addCategoryObject('typeBinding', 'AltFixAltAltitudeType', AltFixAltAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}BlockAltitudeType with content type ELEMENT_ONLY
class BlockAltitudeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Altitude indicates that aircraft is operating  above and below the specified altitudes. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BlockAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 106, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element above uses Python identifier above
    __above = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'above'), 'above', '__httpwww_faa_aeronas3_0_BlockAltitudeType_above', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 114, 9), )

    
    above = property(__above.value, __above.set, None, '\n                  Lower range of the block altitude. \n               ')

    
    # Element below uses Python identifier below
    __below = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'below'), 'below', '__httpwww_faa_aeronas3_0_BlockAltitudeType_below', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 121, 9), )

    
    below = property(__below.value, __below.set, None, '\n                  Upper range of the block altitude. \n               ')

    _ElementMap.update({
        __above.name() : __above,
        __below.name() : __below
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BlockAltitudeType = BlockAltitudeType
Namespace.addCategoryObject('typeBinding', 'BlockAltitudeType', BlockAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}NasAltitudeType with content type ELEMENT_ONLY
class NasAltitudeType (pyxb.binding.basis.complexTypeDefinition):
    """
            A single NAS altitude, which can take on any of the several forms listed in the 
                "choice" below.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 132, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element above uses Python identifier above
    __above = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'above'), 'above', '__httpwww_faa_aeronas3_0_NasAltitudeType_above', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 140, 9), )

    
    above = property(__above.value, __above.set, None, '\n                  aircraft operating above a specified altitude \n               ')

    
    # Element altFixAlt uses Python identifier altFixAlt
    __altFixAlt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'altFixAlt'), 'altFixAlt', '__httpwww_faa_aeronas3_0_NasAltitudeType_altFixAlt', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 147, 9), )

    
    altFixAlt = property(__altFixAlt.value, __altFixAlt.set, None, '\n                  Alt-fix-alt altitude \n               ')

    
    # Element block uses Python identifier block
    __block = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'block'), 'block', '__httpwww_faa_aeronas3_0_NasAltitudeType_block', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 154, 9), )

    
    block = property(__block.value, __block.set, None, '\n                  Altitude indicates that aircraft is operating  above and below the specified altitudes. \n                  \n               ')

    
    # Element simple uses Python identifier simple
    __simple = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'simple'), 'simple', '__httpwww_faa_aeronas3_0_NasAltitudeType_simple', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 162, 9), )

    
    simple = property(__simple.value, __simple.set, None, '\n                  The only NAS altitude that maps directly to the core ICAO altitude types. \n               ')

    
    # Element vfr uses Python identifier vfr
    __vfr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vfr'), 'vfr', '__httpwww_faa_aeronas3_0_NasAltitudeType_vfr', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 169, 9), )

    
    vfr = property(__vfr.value, __vfr.set, None, '\n                  vfr altitude \n               ')

    
    # Element vfrOnTop uses Python identifier vfrOnTop
    __vfrOnTop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vfrOnTop'), 'vfrOnTop', '__httpwww_faa_aeronas3_0_NasAltitudeType_vfrOnTop', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 176, 9), )

    
    vfrOnTop = property(__vfrOnTop.value, __vfrOnTop.set, None, '\n                  vfr-on-top altitude \n               ')

    
    # Element vfrOnTopPlus uses Python identifier vfrOnTopPlus
    __vfrOnTopPlus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vfrOnTopPlus'), 'vfrOnTopPlus', '__httpwww_faa_aeronas3_0_NasAltitudeType_vfrOnTopPlus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 183, 9), )

    
    vfrOnTopPlus = property(__vfrOnTopPlus.value, __vfrOnTopPlus.set, None, '\n                  vfr-on-top with altitude \n               ')

    
    # Element vfrPlus uses Python identifier vfrPlus
    __vfrPlus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vfrPlus'), 'vfrPlus', '__httpwww_faa_aeronas3_0_NasAltitudeType_vfrPlus', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 190, 9), )

    
    vfrPlus = property(__vfrPlus.value, __vfrPlus.set, None, '\n                  vfr plus altitude \n               ')

    _ElementMap.update({
        __above.name() : __above,
        __altFixAlt.name() : __altFixAlt,
        __block.name() : __block,
        __simple.name() : __simple,
        __vfr.name() : __vfr,
        __vfrOnTop.name() : __vfrOnTop,
        __vfrOnTopPlus.name() : __vfrOnTopPlus,
        __vfrPlus.name() : __vfrPlus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasAltitudeType = NasAltitudeType
Namespace.addCategoryObject('typeBinding', 'NasAltitudeType', NasAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}VfrAltitudeType with content type EMPTY
class VfrAltitudeType (pyxb.binding.basis.complexTypeDefinition):
    """
            vfr altitude 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VfrAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 212, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VfrAltitudeType = VfrAltitudeType
Namespace.addCategoryObject('typeBinding', 'VfrAltitudeType', VfrAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}VfrOnTopAltitudeType with content type EMPTY
class VfrOnTopAltitudeType (pyxb.binding.basis.complexTypeDefinition):
    """
            vfr-on-top altitude 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VfrOnTopAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 221, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VfrOnTopAltitudeType = VfrOnTopAltitudeType
Namespace.addCategoryObject('typeBinding', 'VfrOnTopAltitudeType', VfrOnTopAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}RunwayAcceptableSlotSubstitutionType with content type ELEMENT_ONLY
class RunwayAcceptableSlotSubstitutionType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest 
            time at which the Airspace user will accept a slot in a Traffic Management Initiative 
            (TMI) Ground Delay Program (GDP) in return for a yielded slot. 
            .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time 
            at which the Airspace user will accept a slot in a Traffic Management Initiative 
            (TMI) Ground Delay Program (GDP), in return for a yielded slot. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunwayAcceptableSlotSubstitutionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 144, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element earliest uses Python identifier earliest
    __earliest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'earliest'), 'earliest', '__httpwww_faa_aeronas3_0_RunwayAcceptableSlotSubstitutionType_earliest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 156, 9), )

    
    earliest = property(__earliest.value, __earliest.set, None, '\n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n               ')

    
    # Element latest uses Python identifier latest
    __latest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'latest'), 'latest', '__httpwww_faa_aeronas3_0_RunwayAcceptableSlotSubstitutionType_latest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 168, 9), )

    
    latest = property(__latest.value, __latest.set, None, '\n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n               ')

    _ElementMap.update({
        __earliest.name() : __earliest,
        __latest.name() : __latest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RunwayAcceptableSlotSubstitutionType = RunwayAcceptableSlotSubstitutionType
Namespace.addCategoryObject('typeBinding', 'RunwayAcceptableSlotSubstitutionType', RunwayAcceptableSlotSubstitutionType)


# Complex type {http://www.faa.aero/nas/3.0}RunwayArrivalTimeType with content type ELEMENT_ONLY
class RunwayArrivalTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Container for NAS Specific Runway Arrival Times. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunwayArrivalTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 184, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element airlineEstimated uses Python identifier airlineEstimated
    __airlineEstimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airlineEstimated'), 'airlineEstimated', '__httpwww_faa_aeronas3_0_RunwayArrivalTimeType_airlineEstimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 191, 9), )

    
    airlineEstimated = property(__airlineEstimated.value, __airlineEstimated.set, None, '\n                  .Runway Arrival Time - Airspace User Estimated: The estimated time of runway arrival, \n                  as provided by the Airspace User. \n                  .Runway Departure Time - Airspace User Estimated: The estimated time of runway departure, \n                  as provided by the Airspace User. \n               ')

    
    # Element earliest uses Python identifier earliest
    __earliest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'earliest'), 'earliest', '__httpwww_faa_aeronas3_0_RunwayArrivalTimeType_earliest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 201, 9), )

    
    earliest = property(__earliest.value, __earliest.set, None, '\n                  .Runway Arrival Time - Earliest: The earliest acceptable arrival time provided by \n                  the Airspace user for a flight. \n               ')

    
    # Element original uses Python identifier original
    __original = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'original'), 'original', '__httpwww_faa_aeronas3_0_RunwayArrivalTimeType_original', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 209, 9), )

    
    original = property(__original.value, __original.set, None, '\n                  .Runway Arrival Time - Original: The last Runway Arrival Time - Traffic Flow Management \n                  System Estimated modeled by TFMS before either a Traffic Management Initiative (TMI) \n                  is issued, or the flight departs, or the flight is  time-out  delayed by TFMS. \n               ')

    
    # Element preferred uses Python identifier preferred
    __preferred = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'preferred'), 'preferred', '__httpwww_faa_aeronas3_0_RunwayArrivalTimeType_preferred', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 218, 9), )

    
    preferred = property(__preferred.value, __preferred.set, None, '\n                  .Runway Arrival Time - Preferred: A runway arrival time which, when considered in \n                  aggregate with other flights for that Airspace User, indicates the preferred arrival \n                  sequence. \n               ')

    
    # Element slotSubstitution uses Python identifier slotSubstitution
    __slotSubstitution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'slotSubstitution'), 'slotSubstitution', '__httpwww_faa_aeronas3_0_RunwayArrivalTimeType_slotSubstitution', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 227, 9), )

    
    slotSubstitution = property(__slotSubstitution.value, __slotSubstitution.set, None, '\n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n               ')

    
    # Element tfmsEstimated uses Python identifier tfmsEstimated
    __tfmsEstimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tfmsEstimated'), 'tfmsEstimated', '__httpwww_faa_aeronas3_0_RunwayArrivalTimeType_tfmsEstimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 239, 9), )

    
    tfmsEstimated = property(__tfmsEstimated.value, __tfmsEstimated.set, None, '\n                  .Runway Departure Time - Traffic Flow Management System Estimated: The estimated \n                  runway departure time considering all data sources, as determined by Traffic Flow \n                  Management System (TFMS). \n                  .Runway Arrival Time - Traffic Flow Management System Estimated: The estimated runway \n                  arrival time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ')

    _ElementMap.update({
        __airlineEstimated.name() : __airlineEstimated,
        __earliest.name() : __earliest,
        __original.name() : __original,
        __preferred.name() : __preferred,
        __slotSubstitution.name() : __slotSubstitution,
        __tfmsEstimated.name() : __tfmsEstimated
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RunwayArrivalTimeType = RunwayArrivalTimeType
Namespace.addCategoryObject('typeBinding', 'RunwayArrivalTimeType', RunwayArrivalTimeType)


# Complex type {http://www.faa.aero/nas/3.0}RunwayDepartureTimeType with content type ELEMENT_ONLY
class RunwayDepartureTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Container for NAS Specific Runway Departure Times. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunwayDepartureTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 124, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element airlineEstimated uses Python identifier airlineEstimated
    __airlineEstimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'airlineEstimated'), 'airlineEstimated', '__httpwww_faa_aeronas3_0_RunwayDepartureTimeType_airlineEstimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 131, 9), )

    
    airlineEstimated = property(__airlineEstimated.value, __airlineEstimated.set, None, '\n                  .Runway Arrival Time - Airspace User Estimated: The estimated time of runway arrival, \n                  as provided by the Airspace User. \n                  .Runway Departure Time - Airspace User Estimated: The estimated time of runway departure, \n                  as provided by the Airspace User. \n               ')

    
    # Element earliest uses Python identifier earliest
    __earliest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'earliest'), 'earliest', '__httpwww_faa_aeronas3_0_RunwayDepartureTimeType_earliest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 141, 9), )

    
    earliest = property(__earliest.value, __earliest.set, None, '\n                  .Runway Departure Time - Earliest: Earliest acceptable runway departure time (wheels-off \n                  time) an Airspace user provides for a flight. \n               ')

    
    # Element original uses Python identifier original
    __original = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'original'), 'original', '__httpwww_faa_aeronas3_0_RunwayDepartureTimeType_original', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 149, 9), )

    
    original = property(__original.value, __original.set, None, '\n                  .Runway Departure Time - Original: The last Runway Departure Time - Traffic Flow \n                  Management System Estimated modeled by TFMS before either a Traffic Management Initiative \n                  (TMI) is issued, or the flight departs, or the flight is  time-out  delayed by TFMS. \n                  \n               ')

    
    # Element preferred uses Python identifier preferred
    __preferred = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'preferred'), 'preferred', '__httpwww_faa_aeronas3_0_RunwayDepartureTimeType_preferred', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 159, 9), )

    
    preferred = property(__preferred.value, __preferred.set, None, '\n                  .Runway Departure Time - Preferred: A runway departure time which, when considered \n                  in aggregate with other flights for that Airspace User, indicates the preferred departure \n                  sequence. \n               ')

    
    # Element tfmEstimated uses Python identifier tfmEstimated
    __tfmEstimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tfmEstimated'), 'tfmEstimated', '__httpwww_faa_aeronas3_0_RunwayDepartureTimeType_tfmEstimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 168, 9), )

    
    tfmEstimated = property(__tfmEstimated.value, __tfmEstimated.set, None, '\n                  .Runway Departure Time - Traffic Flow Management System Estimated: The estimated \n                  runway departure time considering all data sources, as determined by Traffic Flow \n                  Management System (TFMS). \n                  .Runway Arrival Time - Traffic Flow Management System Estimated: The estimated runway \n                  arrival time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ')

    _ElementMap.update({
        __airlineEstimated.name() : __airlineEstimated,
        __earliest.name() : __earliest,
        __original.name() : __original,
        __preferred.name() : __preferred,
        __tfmEstimated.name() : __tfmEstimated
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RunwayDepartureTimeType = RunwayDepartureTimeType
Namespace.addCategoryObject('typeBinding', 'RunwayDepartureTimeType', RunwayDepartureTimeType)


# Complex type {http://www.faa.aero/nas/3.0}AirspaceAcceptableSlotSubstitutionType with content type ELEMENT_ONLY
class AirspaceAcceptableSlotSubstitutionType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest 
            time at which the Airspace user will accept a slot in a Traffic Management Initiative 
            (TMI) Ground Delay Program (GDP) in return for a yielded slot. 
            .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time 
            at which the Airspace user will accept a slot in a Traffic Management Initiative 
            (TMI) Ground Delay Program (GDP), in return for a yielded slot. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspaceAcceptableSlotSubstitutionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 62, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element earliest uses Python identifier earliest
    __earliest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'earliest'), 'earliest', '__httpwww_faa_aeronas3_0_AirspaceAcceptableSlotSubstitutionType_earliest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 74, 9), )

    
    earliest = property(__earliest.value, __earliest.set, None, '\n                  .Airspace Entry Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP), in return for a yielded slot. \n                  .Airspace Entry Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP) in return for a yielded slot. \n               ')

    
    # Element latest uses Python identifier latest
    __latest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'latest'), 'latest', '__httpwww_faa_aeronas3_0_AirspaceAcceptableSlotSubstitutionType_latest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 86, 9), )

    
    latest = property(__latest.value, __latest.set, None, '\n                  .Airspace Entry Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP), in return for a yielded slot. \n                  .Airspace Entry Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP) in return for a yielded slot. \n               ')

    _ElementMap.update({
        __earliest.name() : __earliest,
        __latest.name() : __latest
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AirspaceAcceptableSlotSubstitutionType = AirspaceAcceptableSlotSubstitutionType
Namespace.addCategoryObject('typeBinding', 'AirspaceAcceptableSlotSubstitutionType', AirspaceAcceptableSlotSubstitutionType)


# Complex type {http://www.faa.aero/nas/3.0}AirspaceEntryTimeType with content type ELEMENT_ONLY
class AirspaceEntryTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Container for : 
            Airspace Entry Time - Earliest 
            Airspace Entry Time - Initial 
            Airspace Entry Time - Original 
            Airspace Entry Time - Traffic Flow Management System Estimated 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspaceEntryTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 102, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element earliest uses Python identifier earliest
    __earliest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'earliest'), 'earliest', '__httpwww_faa_aeronas3_0_AirspaceEntryTimeType_earliest', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 113, 9), )

    
    earliest = property(__earliest.value, __earliest.set, None, '\n                  .Airspace Entry Time - Earliest: The earliest time the flight could enter the constrained \n                  airspace. \n               ')

    
    # Element initial uses Python identifier initial
    __initial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'initial'), 'initial', '__httpwww_faa_aeronas3_0_AirspaceEntryTimeType_initial', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 121, 9), )

    
    initial = property(__initial.value, __initial.set, None, '\n                  .Airspace Entry Time - Initial: The date and time at which a flight was originally \n                  planning to enter into the airspace. \n               ')

    
    # Element original uses Python identifier original
    __original = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'original'), 'original', '__httpwww_faa_aeronas3_0_AirspaceEntryTimeType_original', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 129, 9), )

    
    original = property(__original.value, __original.set, None, '\n                  .Airspace Entry Time - Original: The last Airspace Entry Time - Traffic Flow Management \n                  System Estimated modeled by the Traffic Flow Management System (TFMS) before either \n                  a Traffic Management Initiative is issued, or the flight departs, or the flight is \n                   time-out  delayed by TFMS. \n               ')

    
    # Element slotSubstitution uses Python identifier slotSubstitution
    __slotSubstitution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'slotSubstitution'), 'slotSubstitution', '__httpwww_faa_aeronas3_0_AirspaceEntryTimeType_slotSubstitution', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 139, 9), )

    
    slotSubstitution = property(__slotSubstitution.value, __slotSubstitution.set, None, '\n                  .Airspace Entry Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP), in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n                  .Airspace Entry Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP) in return for a yielded slot. \n               ')

    
    # Element tfmsEstimated uses Python identifier tfmsEstimated
    __tfmsEstimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tfmsEstimated'), 'tfmsEstimated', '__httpwww_faa_aeronas3_0_AirspaceEntryTimeType_tfmsEstimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 157, 9), )

    
    tfmsEstimated = property(__tfmsEstimated.value, __tfmsEstimated.set, None, '\n                  .Airspace Exit Time - Traffic Flow Management System Estimated: The estimated airspace \n                  exit time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n                  .Airspace Entry Time - Traffic Flow Management System Estimated: The estimated airspace \n                  entry time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ')

    _ElementMap.update({
        __earliest.name() : __earliest,
        __initial.name() : __initial,
        __original.name() : __original,
        __slotSubstitution.name() : __slotSubstitution,
        __tfmsEstimated.name() : __tfmsEstimated
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AirspaceEntryTimeType = AirspaceEntryTimeType
Namespace.addCategoryObject('typeBinding', 'AirspaceEntryTimeType', AirspaceEntryTimeType)


# Complex type {http://www.faa.aero/nas/3.0}AirspaceExitTimeType with content type ELEMENT_ONLY
class AirspaceExitTimeType (pyxb.binding.basis.complexTypeDefinition):
    """
            Container for 
            Airspace Exit Time - Traffic Flow Management System Estimated 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirspaceExitTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 173, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element tfmsEstimated uses Python identifier tfmsEstimated
    __tfmsEstimated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tfmsEstimated'), 'tfmsEstimated', '__httpwww_faa_aeronas3_0_AirspaceExitTimeType_tfmsEstimated', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 181, 9), )

    
    tfmsEstimated = property(__tfmsEstimated.value, __tfmsEstimated.set, None, '\n                  .Airspace Exit Time - Traffic Flow Management System Estimated: The estimated airspace \n                  exit time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n                  .Airspace Entry Time - Traffic Flow Management System Estimated: The estimated airspace \n                  entry time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ')

    _ElementMap.update({
        __tfmsEstimated.name() : __tfmsEstimated
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AirspaceExitTimeType = AirspaceExitTimeType
Namespace.addCategoryObject('typeBinding', 'AirspaceExitTimeType', AirspaceExitTimeType)


# Complex type {http://www.faa.aero/nas/3.0}NasAirspeedChoiceType with content type ELEMENT_ONLY
class NasAirspeedChoiceType (pyxb.binding.basis.complexTypeDefinition):
    """
            A NAS extension to add an additional optional value to element Airspeed, 
            In the NAS this element is: Aircraft Speed/Speed Classified.
            The value is "SC". Used when the speed is a classifed value.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAirspeedChoiceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 110, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element classified uses Python identifier classified
    __classified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'classified'), 'classified', '__httpwww_faa_aeronas3_0_NasAirspeedChoiceType_classified', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 119, 9), )

    
    classified = property(__classified.value, __classified.set, None, '\n                  Container for the Classified Speed Indicator. \n                  .Classified Speed Indicator: The indication that the speed for this flight is classified \n                  and is not to be recorded. \n               ')

    
    # Element nasAirspeed uses Python identifier nasAirspeed
    __nasAirspeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nasAirspeed'), 'nasAirspeed', '__httpwww_faa_aeronas3_0_NasAirspeedChoiceType_nasAirspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 128, 9), )

    
    nasAirspeed = property(__nasAirspeed.value, __nasAirspeed.set, None, '\n                  Represents the aircraft speed expressed in either true airspeed or mach. \n               ')

    _ElementMap.update({
        __classified.name() : __classified,
        __nasAirspeed.name() : __nasAirspeed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasAirspeedChoiceType = NasAirspeedChoiceType
Namespace.addCategoryObject('typeBinding', 'NasAirspeedChoiceType', NasAirspeedChoiceType)


# Complex type {http://www.faa.aero/nas/3.0}AbstractMessageType with content type ELEMENT_ONLY
class AbstractMessageType (pyxb.binding.basis.complexTypeDefinition):
    """
            The Message type is the smallest unit of data transmission between components. It 
            contains identifying metadata and a payload. It is expected that extensions will 
            extend this to define their own message types, including their own payloads. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractMessageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 66, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_faa_aeronas3_0_AbstractMessageType_metadata', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9), )

    
    metadata = property(__metadata.value, __metadata.set, None, '\n                  The MessageMetadata provides a unique message identifier, the origin of the message \n                  in time and location, \n                the system\n                that produced the message, and the time span over which the message data is valid.\n               ')

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AbstractMessageType = AbstractMessageType
Namespace.addCategoryObject('typeBinding', 'AbstractMessageType', AbstractMessageType)


# Complex type {http://www.faa.aero/nas/3.0}MessageCollectionType with content type ELEMENT_ONLY
class MessageCollectionType (pyxb.binding.basis.complexTypeDefinition):
    """
            The MessageCollection type is a mechanism for aggregating messages to be transmitted 
            as a group. This is useful 
                both to aggregate messages about one flight, and to pack many messages together for transmission efficiency.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageCollectionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 135, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpwww_faa_aeronas3_0_MessageCollectionType_message', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 144, 9), )

    
    message = property(__message.value, __message.set, None, '\n                  The MessageCollection type is a mechanism for aggregating messages to be transmitted \n                  as a group. This is useful \n                both to aggregate messages about one flight, and to pack many messages together for transmission efficiency.\n               ')

    _ElementMap.update({
        __message.name() : __message
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MessageCollectionType = MessageCollectionType
Namespace.addCategoryObject('typeBinding', 'MessageCollectionType', MessageCollectionType)


# Complex type {http://www.faa.aero/nas/3.0}NasVelocityType with content type ELEMENT_ONLY
class NasVelocityType (pyxb.binding.basis.complexTypeDefinition):
    """
            Describes flight's velocity in X and Y axes 
         
            .Track Speed Components: Speed of the radar surveillance track along the X and Y 
            components. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasVelocityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 165, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__httpwww_faa_aeronas3_0_NasVelocityType_x', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 175, 9), )

    
    x = property(__x.value, __x.set, None, '\n                  speed along the X-axis \n               ')

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__httpwww_faa_aeronas3_0_NasVelocityType_y', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 182, 9), )

    
    y = property(__y.value, __y.set, None, '\n                  speed along the Y-axis \n               ')

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasVelocityType = NasVelocityType
Namespace.addCategoryObject('typeBinding', 'NasVelocityType', NasVelocityType)


# Complex type {http://www.faa.aero/nas/3.0}RouteImpactListType with content type ELEMENT_ONLY
class RouteImpactListType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Route Impact List: Current traffic flow management prediction of en route Air Traffic 
            Control units (centres), sectors and airspace elements along the trajectory of a 
            flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RouteImpactListType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 337, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element predictedAirway uses Python identifier predictedAirway
    __predictedAirway = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedAirway'), 'predictedAirway', '__httpwww_faa_aeronas3_0_RouteImpactListType_predictedAirway', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 346, 9), )

    
    predictedAirway = property(__predictedAirway.value, __predictedAirway.set, None, '\n                  .Predicted Airways: Current prediction of the airways along the trajectory of a flight. \n                  \n               ')

    
    # Element predictedFix uses Python identifier predictedFix
    __predictedFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedFix'), 'predictedFix', '__httpwww_faa_aeronas3_0_RouteImpactListType_predictedFix', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 357, 9), )

    
    predictedFix = property(__predictedFix.value, __predictedFix.set, None, '\n                  .Predicted Fixes: Current prediction of fixes along the trajectory of a flight, where \n                  these predictions are based on all the information available to the Traffic Flow \n                  Management System (TFMS). \n               ')

    
    # Element predictedSector uses Python identifier predictedSector
    __predictedSector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedSector'), 'predictedSector', '__httpwww_faa_aeronas3_0_RouteImpactListType_predictedSector', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 366, 9), )

    
    predictedSector = property(__predictedSector.value, __predictedSector.set, None, '\n                  .Predicted Sectors: Current prediction of the sectors along the trajectory of a flight. \n                  \n               ')

    
    # Element predictedUnit uses Python identifier predictedUnit
    __predictedUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedUnit'), 'predictedUnit', '__httpwww_faa_aeronas3_0_RouteImpactListType_predictedUnit', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 374, 9), )

    
    predictedUnit = property(__predictedUnit.value, __predictedUnit.set, None, '\n                  .Predicted Units: Current prediction of the en route Air Traffic Control units (centres) \n                  along the trajectory of a flight. \n               ')

    
    # Element predictedWaypoint uses Python identifier predictedWaypoint
    __predictedWaypoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'predictedWaypoint'), 'predictedWaypoint', '__httpwww_faa_aeronas3_0_RouteImpactListType_predictedWaypoint', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 382, 9), )

    
    predictedWaypoint = property(__predictedWaypoint.value, __predictedWaypoint.set, None, '\n                  .Predicted Waypoints: Current prediction of the waypoints of the trajectory for a \n                  flight, where these predictions are based on all the information available to the \n                  Traffic Flow Management System (TFMS). \n               ')

    _ElementMap.update({
        __predictedAirway.name() : __predictedAirway,
        __predictedFix.name() : __predictedFix,
        __predictedSector.name() : __predictedSector,
        __predictedUnit.name() : __predictedUnit,
        __predictedWaypoint.name() : __predictedWaypoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RouteImpactListType = RouteImpactListType
Namespace.addCategoryObject('typeBinding', 'RouteImpactListType', RouteImpactListType)


# Complex type {http://www.faa.aero/nas/3.0}NasTmiType with content type ELEMENT_ONLY
class NasTmiType (pyxb.binding.basis.complexTypeDefinition):
    """
            Container for NAS Traffic Management Initiatives.  CTOP Information is not included 
            in this container but instead collected in the NasTmiTrajectoryOption Container and 
            connected to the Flight Object. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasTmiType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 256, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element advisories uses Python identifier advisories
    __advisories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'advisories'), 'advisories', '__httpwww_faa_aeronas3_0_NasTmiType_advisories', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 265, 9), )

    
    advisories = property(__advisories.value, __advisories.set, None, '\n                  .NAS Advisory Information: A container for Traffic Flow Management advisories pertinent \n                  to a single flight. \n               ')

    
    # Element reroute uses Python identifier reroute
    __reroute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reroute'), 'reroute', '__httpwww_faa_aeronas3_0_NasTmiType_reroute', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 273, 9), )

    
    reroute = property(__reroute.value, __reroute.set, None, '\n                  A container for information pertinent to a single NAS reroute issued for a flight \n                  by traffic flow management. \n                  .Traffic Flow Management Reroute Information: A container for information pertinent \n                  to a single NAS reroute issued for a flight by traffic flow management. \n               ')

    _ElementMap.update({
        __advisories.name() : __advisories,
        __reroute.name() : __reroute
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasTmiType = NasTmiType
Namespace.addCategoryObject('typeBinding', 'NasTmiType', NasTmiType)


# Complex type {http://www.faa.aero/nas/3.0}NasHandoffType with content type ELEMENT_ONLY
class NasHandoffType (_ImportedBinding__fx.HandoffType):
    """
            Contains information about flight handoff between sectors. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasHandoffType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 62, 3)
    _ElementMap = _ImportedBinding__fx.HandoffType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.HandoffType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.HandoffType
    
    # Element acceptingUnit uses Python identifier acceptingUnit
    __acceptingUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'acceptingUnit'), 'acceptingUnit', '__httpwww_faa_aeronas3_0_NasHandoffType_acceptingUnit', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 71, 15), )

    
    acceptingUnit = property(__acceptingUnit.value, __acceptingUnit.set, None, '\n                        .Handoff Accepting Unit: The Air Traffic Control (ATC) unit accepting control of \n                        the aircraft as a result of a handoff. \n                        .Handoff Accepting Sector: The Air Traffic Control (ATC) sector accepting control \n                        of the aircraft as a result of a handoff. \n                     ')

    
    # Element coordinationStatus (coordinationStatus) inherited from {http://www.fixm.aero/flight/3.0}HandoffType
    
    # Element receivingUnit (receivingUnit) inherited from {http://www.fixm.aero/flight/3.0}HandoffType
    
    # Element transferringUnit (transferringUnit) inherited from {http://www.fixm.aero/flight/3.0}HandoffType
    
    # Attribute event uses Python identifier event
    __event = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event'), 'event', '__httpwww_faa_aeronas3_0_NasHandoffType_event', _module_typeBindings.NasHandoffEventType)
    __event._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 82, 12)
    __event._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 82, 12)
    
    event = property(__event.value, __event.set, None, '\n                     .Handoff Event Category: Characterizes a handoff in terms of its status. \n                  ')

    _ElementMap.update({
        __acceptingUnit.name() : __acceptingUnit
    })
    _AttributeMap.update({
        __event.name() : __event
    })
_module_typeBindings.NasHandoffType = NasHandoffType
Namespace.addCategoryObject('typeBinding', 'NasHandoffType', NasHandoffType)


# Complex type {http://www.faa.aero/nas/3.0}NasClearedFlightInformationType with content type ELEMENT_ONLY
class NasClearedFlightInformationType (_ImportedBinding__fx.ClearedFlightInformationType):
    """
            Extends the core ClearedFlightInformation to hold additional clearance information. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasClearedFlightInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 263, 3)
    _ElementMap = _ImportedBinding__fx.ClearedFlightInformationType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.ClearedFlightInformationType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.ClearedFlightInformationType
    
    # Element clearedFlightLevel (clearedFlightLevel) inherited from {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType
    
    # Element clearedSpeed (clearedSpeed) inherited from {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType
    
    # Element directRouting (directRouting) inherited from {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType
    
    # Element heading (heading) inherited from {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType
    
    # Element offtrackClearance (offtrackClearance) inherited from {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType
    
    # Element rateOfClimbDescend (rateOfClimbDescend) inherited from {http://www.fixm.aero/flight/3.0}ClearedFlightInformationType
    
    # Attribute clearanceHeading uses Python identifier clearanceHeading
    __clearanceHeading = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'clearanceHeading'), 'clearanceHeading', '__httpwww_faa_aeronas3_0_NasClearedFlightInformationType_clearanceHeading', _ImportedBinding__fb.FreeTextType)
    __clearanceHeading._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 272, 12)
    __clearanceHeading._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 272, 12)
    
    clearanceHeading = property(__clearanceHeading.value, __clearanceHeading.set, None, '\n                     .En Route Clearance Heading: Contains the En Route Controller Clearance heading, \n                     as entered by the controller in the fourth line of the Full Data Block. \n                  ')

    
    # Attribute clearanceSpeed uses Python identifier clearanceSpeed
    __clearanceSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'clearanceSpeed'), 'clearanceSpeed', '__httpwww_faa_aeronas3_0_NasClearedFlightInformationType_clearanceSpeed', _ImportedBinding__fb.FreeTextType)
    __clearanceSpeed._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 280, 12)
    __clearanceSpeed._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 280, 12)
    
    clearanceSpeed = property(__clearanceSpeed.value, __clearanceSpeed.set, None, '\n                     .En Route Clearance Speed: This data element contains the En Route Controller Clearance \n                     speed, as entered by the controller in the fourth line of the Full Data Block. \n                  ')

    
    # Attribute clearanceText uses Python identifier clearanceText
    __clearanceText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'clearanceText'), 'clearanceText', '__httpwww_faa_aeronas3_0_NasClearedFlightInformationType_clearanceText', _ImportedBinding__fb.FreeTextType)
    __clearanceText._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 288, 12)
    __clearanceText._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 288, 12)
    
    clearanceText = property(__clearanceText.value, __clearanceText.set, None, '\n                     .En Route Clearance Text: This data element contains free-form text entered by the \n                     En Route Controller, to be associated with the Clearance in the fourth line of the \n                     Full Data Block. \n                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __clearanceHeading.name() : __clearanceHeading,
        __clearanceSpeed.name() : __clearanceSpeed,
        __clearanceText.name() : __clearanceText
    })
_module_typeBindings.NasClearedFlightInformationType = NasClearedFlightInformationType
Namespace.addCategoryObject('typeBinding', 'NasClearedFlightInformationType', NasClearedFlightInformationType)


# Complex type {http://www.faa.aero/nas/3.0}NasCoordinationType with content type ELEMENT_ONLY
class NasCoordinationType (pyxb.binding.basis.complexTypeDefinition):
    """
            NAS extension to boundary crossing information: includes special handling for ccoordination 
            time type. 
            Coordination Time and Coordination Fix are handled by crossingPoint and crossingTime. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasCoordinationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 139, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element coordinationFix uses Python identifier coordinationFix
    __coordinationFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'coordinationFix'), 'coordinationFix', '__httpwww_faa_aeronas3_0_NasCoordinationType_coordinationFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 149, 9), )

    
    coordinationFix = property(__coordinationFix.value, __coordinationFix.set, None, '\n                  .Coordination Fix: The fix to be used in conjunction with the Coordination Time so \n                  processing for this flight (and its trajectory) can be synchronized for the next \n                  sector/facility.  It   coordinates   the flight plan with the aircraft position. \n                  \n               ')

    
    # Attribute coordinationTime uses Python identifier coordinationTime
    __coordinationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coordinationTime'), 'coordinationTime', '__httpwww_faa_aeronas3_0_NasCoordinationType_coordinationTime', _ImportedBinding__ff.TimeType)
    __coordinationTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 160, 6)
    __coordinationTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 160, 6)
    
    coordinationTime = property(__coordinationTime.value, __coordinationTime.set, None, '\n               .Coordination Time: The time to be used in conjunction with the Coordination Fix \n               so processing for this flight (and its trajectory) can be synchronized for the next \n               sector/facility.  It   coordinates   the flight plan with the aircraft position. \n               \n            ')

    
    # Attribute coordinationTimeHandling uses Python identifier coordinationTimeHandling
    __coordinationTimeHandling = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coordinationTimeHandling'), 'coordinationTimeHandling', '__httpwww_faa_aeronas3_0_NasCoordinationType_coordinationTimeHandling', _module_typeBindings.CoordinationTimeTypeType)
    __coordinationTimeHandling._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 170, 6)
    __coordinationTimeHandling._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 170, 6)
    
    coordinationTimeHandling = property(__coordinationTimeHandling.value, __coordinationTimeHandling.set, None, '\n               Container for Coordination Time Type. \n               .Coordination Time Type: The indicator for the type of   Coordination Time  . \n            ')

    
    # Attribute delayTimeToAbsorb uses Python identifier delayTimeToAbsorb
    __delayTimeToAbsorb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delayTimeToAbsorb'), 'delayTimeToAbsorb', '__httpwww_faa_aeronas3_0_NasCoordinationType_delayTimeToAbsorb', _ImportedBinding__ff.DurationType)
    __delayTimeToAbsorb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 178, 6)
    __delayTimeToAbsorb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 178, 6)
    
    delayTimeToAbsorb = property(__delayTimeToAbsorb.value, __delayTimeToAbsorb.set, None, '\n               .Delay Time to Absorb: Indicates the amount of time that needs to be absorbed during \n               the flight. It is corrective action for meeting the goal of Estimated Departure Clearance \n               Time (EDCT), when flight is already active and needs to arrive at the destination \n               later than originally planned. \n            ')

    _ElementMap.update({
        __coordinationFix.name() : __coordinationFix
    })
    _AttributeMap.update({
        __coordinationTime.name() : __coordinationTime,
        __coordinationTimeHandling.name() : __coordinationTimeHandling,
        __delayTimeToAbsorb.name() : __delayTimeToAbsorb
    })
_module_typeBindings.NasCoordinationType = NasCoordinationType
Namespace.addCategoryObject('typeBinding', 'NasCoordinationType', NasCoordinationType)


# Complex type {http://www.faa.aero/nas/3.0}ArrivalMovementAreaHoldInformationType with content type EMPTY
class ArrivalMovementAreaHoldInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Airport Movement Area Holding - Departure Information: Indicates the intent for 
            a departing flight to hold in the airport movement area when surface departure metering 
            or other Traffic Management Initiatives are in effect, and the time when the flight 
            is estimated to request entry in the airport movement area. 
            .Airport Movement Area Holding - Arrival Information: Indicates the intent for an 
            arriving flight to hold in the airport movement area due to unavailability of a parking 
            stand or ramp access, and the time when the flight is estimated to exit the airport 
            movement area. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrivalMovementAreaHoldInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 61, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute estimatedExitTime uses Python identifier estimatedExitTime
    __estimatedExitTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'estimatedExitTime'), 'estimatedExitTime', '__httpwww_faa_aeronas3_0_ArrivalMovementAreaHoldInformationType_estimatedExitTime', _ImportedBinding__ff.TimeType)
    __estimatedExitTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 74, 6)
    __estimatedExitTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 74, 6)
    
    estimatedExitTime = property(__estimatedExitTime.value, __estimatedExitTime.set, None, '\n               .Movement Area Entry Time - Airspace User Requested: Indicates the time when the \n               flight is estimated to request entry in the airport movement area. \n               .Movement Area Exit Time - Airspace User Requested: Indicates the time when the flight \n               is estimated to exit the airport movement area. \n            ')

    
    # Attribute holdIntent uses Python identifier holdIntent
    __holdIntent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'holdIntent'), 'holdIntent', '__httpwww_faa_aeronas3_0_ArrivalMovementAreaHoldInformationType_holdIntent', _module_typeBindings.HoldIntentType)
    __holdIntent._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 84, 6)
    __holdIntent._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 84, 6)
    
    holdIntent = property(__holdIntent.value, __holdIntent.set, None, '\n               .Airport Movement Area Holding Intent - Departure: Indicates the intent for a departing \n               flight to hold in the airport movement area when surface departure metering or other \n               Traffic Management Initiatives are in effect. \n               .Airport Movement Area Holding Intent - Arrival: Indicates the intent for an arriving \n               flight to hold in the airport movement area due to unavailability of a parking stand \n               or ramp access. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __estimatedExitTime.name() : __estimatedExitTime,
        __holdIntent.name() : __holdIntent
    })
_module_typeBindings.ArrivalMovementAreaHoldInformationType = ArrivalMovementAreaHoldInformationType
Namespace.addCategoryObject('typeBinding', 'ArrivalMovementAreaHoldInformationType', ArrivalMovementAreaHoldInformationType)


# Complex type {http://www.faa.aero/nas/3.0}DeicingInformationType with content type EMPTY
class DeicingInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Deicing Information: Indicates the intent for the flight to be deiced and the intended 
            deicing location. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeicingInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 99, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute deicingIntent uses Python identifier deicingIntent
    __deicingIntent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deicingIntent'), 'deicingIntent', '__httpwww_faa_aeronas3_0_DeicingInformationType_deicingIntent', _module_typeBindings.DeicingIntentType)
    __deicingIntent._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 106, 6)
    __deicingIntent._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 106, 6)
    
    deicingIntent = property(__deicingIntent.value, __deicingIntent.set, None, '\n               .Deicing Intent: Indicates the intent for the flight to be deiced. \n            ')

    
    # Attribute deicingLocation uses Python identifier deicingLocation
    __deicingLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deicingLocation'), 'deicingLocation', '__httpwww_faa_aeronas3_0_DeicingInformationType_deicingLocation', _ImportedBinding__fb.FreeTextType)
    __deicingLocation._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 113, 6)
    __deicingLocation._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 113, 6)
    
    deicingLocation = property(__deicingLocation.value, __deicingLocation.set, None, '\n               .Deicing Location: Indicates the location where the flight intends to be deiced. \n               \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __deicingIntent.name() : __deicingIntent,
        __deicingLocation.name() : __deicingLocation
    })
_module_typeBindings.DeicingInformationType = DeicingInformationType
Namespace.addCategoryObject('typeBinding', 'DeicingInformationType', DeicingInformationType)


# Complex type {http://www.faa.aero/nas/3.0}DepartureMovementAreaHoldInformationType with content type EMPTY
class DepartureMovementAreaHoldInformationType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Airport Movement Area Holding - Departure Information: Indicates the intent for 
            a departing flight to hold in the airport movement area when surface departure metering 
            or other Traffic Management Initiatives are in effect, and the time when the flight 
            is estimated to request entry in the airport movement area. 
            .Airport Movement Area Holding - Arrival Information: Indicates the intent for an 
            arriving flight to hold in the airport movement area due to unavailability of a parking 
            stand or ramp access, and the time when the flight is estimated to exit the airport 
            movement area. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DepartureMovementAreaHoldInformationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 148, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute estimatedEntryTime uses Python identifier estimatedEntryTime
    __estimatedEntryTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'estimatedEntryTime'), 'estimatedEntryTime', '__httpwww_faa_aeronas3_0_DepartureMovementAreaHoldInformationType_estimatedEntryTime', _ImportedBinding__ff.TimeType)
    __estimatedEntryTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 161, 6)
    __estimatedEntryTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 161, 6)
    
    estimatedEntryTime = property(__estimatedEntryTime.value, __estimatedEntryTime.set, None, '\n               .Movement Area Entry Time - Airspace User Requested: Indicates the time when the \n               flight is estimated to request entry in the airport movement area. \n               .Movement Area Exit Time - Airspace User Requested: Indicates the time when the flight \n               is estimated to exit the airport movement area. \n            ')

    
    # Attribute holdIntent uses Python identifier holdIntent
    __holdIntent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'holdIntent'), 'holdIntent', '__httpwww_faa_aeronas3_0_DepartureMovementAreaHoldInformationType_holdIntent', _module_typeBindings.HoldIntentType)
    __holdIntent._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 171, 6)
    __holdIntent._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 171, 6)
    
    holdIntent = property(__holdIntent.value, __holdIntent.set, None, '\n               .Airport Movement Area Holding Intent - Departure: Indicates the intent for a departing \n               flight to hold in the airport movement area when surface departure metering or other \n               Traffic Management Initiatives are in effect. \n               .Airport Movement Area Holding Intent - Arrival: Indicates the intent for an arriving \n               flight to hold in the airport movement area due to unavailability of a parking stand \n               or ramp access. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __estimatedEntryTime.name() : __estimatedEntryTime,
        __holdIntent.name() : __holdIntent
    })
_module_typeBindings.DepartureMovementAreaHoldInformationType = DepartureMovementAreaHoldInformationType
Namespace.addCategoryObject('typeBinding', 'DepartureMovementAreaHoldInformationType', DepartureMovementAreaHoldInformationType)


# Complex type {http://www.faa.aero/nas/3.0}FlightIntentType with content type ELEMENT_ONLY
class FlightIntentType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Flight Intent: A container for the list of intent values provided by the flight 
            operator that designate the intentions of a flight prior to departure from an aerodrome 
            or after arrival at an aerodrome. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightIntentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 186, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element arrival uses Python identifier arrival
    __arrival = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'arrival'), 'arrival', '__httpwww_faa_aeronas3_0_FlightIntentType_arrival', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 195, 9), )

    
    arrival = property(__arrival.value, __arrival.set, None, '\n                  .Airport Movement Area Holding - Departure Information: Indicates the intent for \n                  a departing flight to hold in the airport movement area when surface departure metering \n                  or other Traffic Management Initiatives are in effect, and the time when the flight \n                  is estimated to request entry in the airport movement area. \n                  .Airport Movement Area Holding - Arrival Information: Indicates the intent for an \n                  arriving flight to hold in the airport movement area due to unavailability of a parking \n                  stand or ramp access, and the time when the flight is estimated to exit the airport \n                  movement area. \n               ')

    
    # Element deicing uses Python identifier deicing
    __deicing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deicing'), 'deicing', '__httpwww_faa_aeronas3_0_FlightIntentType_deicing', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 209, 9), )

    
    deicing = property(__deicing.value, __deicing.set, None, '\n                  .Deicing Information: Indicates the intent for the flight to be deiced and the intended \n                  deicing location. \n               ')

    
    # Element departure uses Python identifier departure
    __departure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'departure'), 'departure', '__httpwww_faa_aeronas3_0_FlightIntentType_departure', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 217, 9), )

    
    departure = property(__departure.value, __departure.set, None, '\n                  .Airport Movement Area Holding - Departure Information: Indicates the intent for \n                  a departing flight to hold in the airport movement area when surface departure metering \n                  or other Traffic Management Initiatives are in effect, and the time when the flight \n                  is estimated to request entry in the airport movement area. \n                  .Airport Movement Area Holding - Arrival Information: Indicates the intent for an \n                  arriving flight to hold in the airport movement area due to unavailability of a parking \n                  stand or ramp access, and the time when the flight is estimated to exit the airport \n                  movement area. \n               ')

    
    # Attribute intendedArrivalSpot uses Python identifier intendedArrivalSpot
    __intendedArrivalSpot = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'intendedArrivalSpot'), 'intendedArrivalSpot', '__httpwww_faa_aeronas3_0_FlightIntentType_intendedArrivalSpot', _ImportedBinding__fb.FreeTextType)
    __intendedArrivalSpot._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 232, 6)
    __intendedArrivalSpot._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 232, 6)
    
    intendedArrivalSpot = property(__intendedArrivalSpot.value, __intendedArrivalSpot.set, None, '\n               .Intended Arrival Spot: Indicates the location intended for the flight to enter the \n               non-movement area from the airport movement area. \n            ')

    
    # Attribute intendedDepartureSpot uses Python identifier intendedDepartureSpot
    __intendedDepartureSpot = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'intendedDepartureSpot'), 'intendedDepartureSpot', '__httpwww_faa_aeronas3_0_FlightIntentType_intendedDepartureSpot', _ImportedBinding__fb.FreeTextType)
    __intendedDepartureSpot._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 240, 6)
    __intendedDepartureSpot._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 240, 6)
    
    intendedDepartureSpot = property(__intendedDepartureSpot.value, __intendedDepartureSpot.set, None, '\n               .Intended Departure Spot: Indicates the location intended for the flight to enter \n               the airport movement area from the non-movement area. \n            ')

    
    # Attribute standReturnIntent uses Python identifier standReturnIntent
    __standReturnIntent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standReturnIntent'), 'standReturnIntent', '__httpwww_faa_aeronas3_0_FlightIntentType_standReturnIntent', _module_typeBindings.StandReturnIntentType)
    __standReturnIntent._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 248, 6)
    __standReturnIntent._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 248, 6)
    
    standReturnIntent = property(__standReturnIntent.value, __standReturnIntent.set, None, '\n               .Stand Return Intent: Indicates the intent for the flight to return to the stand. \n               \n            ')

    _ElementMap.update({
        __arrival.name() : __arrival,
        __deicing.name() : __deicing,
        __departure.name() : __departure
    })
    _AttributeMap.update({
        __intendedArrivalSpot.name() : __intendedArrivalSpot,
        __intendedDepartureSpot.name() : __intendedDepartureSpot,
        __standReturnIntent.name() : __standReturnIntent
    })
_module_typeBindings.FlightIntentType = FlightIntentType
Namespace.addCategoryObject('typeBinding', 'FlightIntentType', FlightIntentType)


# Complex type {http://www.faa.aero/nas/3.0}FeatureMessageType with content type ELEMENT_ONLY
class FeatureMessageType (AbstractMessageType):
    """
            It is expected that extensions will extend this to define their own message types, 
            including their own payloads. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FeatureMessageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 89, 3)
    _ElementMap = AbstractMessageType._ElementMap.copy()
    _AttributeMap = AbstractMessageType._AttributeMap.copy()
    # Base type is AbstractMessageType
    
    # Element metadata (metadata) inherited from {http://www.faa.aero/nas/3.0}AbstractMessageType
    
    # Element feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature'), 'feature', '__httpwww_faa_aeronas3_0_FeatureMessageType_feature', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 99, 15), )

    
    feature = property(__feature.value, __feature.set, None, '\n                        Feature that is contained within the feature message. Anything that extends a Feature \n                        can be placed in a Feature message. \n                     ')

    _ElementMap.update({
        __feature.name() : __feature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FeatureMessageType = FeatureMessageType
Namespace.addCategoryObject('typeBinding', 'FeatureMessageType', FeatureMessageType)


# Complex type {http://www.faa.aero/nas/3.0}FlightMessageType with content type ELEMENT_ONLY
class FlightMessageType (AbstractMessageType):
    """
            FlightMessage is used to transmit FIXM flight objects. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FlightMessageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 113, 3)
    _ElementMap = AbstractMessageType._ElementMap.copy()
    _AttributeMap = AbstractMessageType._AttributeMap.copy()
    # Base type is AbstractMessageType
    
    # Element metadata (metadata) inherited from {http://www.faa.aero/nas/3.0}AbstractMessageType
    
    # Element flight uses Python identifier flight
    __flight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flight'), 'flight', '__httpwww_faa_aeronas3_0_FlightMessageType_flight', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 122, 15), )

    
    flight = property(__flight.value, __flight.set, None, '\n                        Flight that is contained within the Flight message. \n                     ')

    _ElementMap.update({
        __flight.name() : __flight
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FlightMessageType = FlightMessageType
Namespace.addCategoryObject('typeBinding', 'FlightMessageType', FlightMessageType)


# Complex type {http://www.faa.aero/nas/3.0}MessageMetadataType with content type ELEMENT_ONLY
class MessageMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """
            The MessageMetadata provides a unique message identifier, the origin of the message 
            in time and location, 
                the system
                that produced the message, and the time span over which the message data is valid.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 157, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element generationLocation uses Python identifier generationLocation
    __generationLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'generationLocation'), 'generationLocation', '__httpwww_faa_aeronas3_0_MessageMetadataType_generationLocation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 167, 9), )

    
    generationLocation = property(__generationLocation.value, __generationLocation.set, None, '\n                  the origin of the message \n               ')

    
    # Element validTimeSpan uses Python identifier validTimeSpan
    __validTimeSpan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'validTimeSpan'), 'validTimeSpan', '__httpwww_faa_aeronas3_0_MessageMetadataType_validTimeSpan', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 174, 9), )

    
    validTimeSpan = property(__validTimeSpan.value, __validTimeSpan.set, None, '\n                  the time span over which the message data is valid \n               ')

    
    # Attribute gumi uses Python identifier gumi
    __gumi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gumi'), 'gumi', '__httpwww_faa_aeronas3_0_MessageMetadataType_gumi', _ImportedBinding__fb.FreeTextType)
    __gumi._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 182, 6)
    __gumi._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 182, 6)
    
    gumi = property(__gumi.value, __gumi.set, None, '\n               The GUMI is the Globally Unique Message Identifier. It has the following format: \n               \n                \n               "urn":"fixm.aero":system:subsystem:timestamp:sequence \n                \n                where:system    is the major system involved, eg "nas"\n                      subsystem is the minor system involved, eg "eram"\n                      timestamp is a time stamp to the second with all punctuation and time offset squeezed out\n                      sequence  is an ascending integer to ensure uniqueness within the second\n                \n                example:\n                      urn:fixm.aero:nas:eram:20120606T142534:384\n            ')

    _ElementMap.update({
        __generationLocation.name() : __generationLocation,
        __validTimeSpan.name() : __validTimeSpan
    })
    _AttributeMap.update({
        __gumi.name() : __gumi
    })
_module_typeBindings.MessageMetadataType = MessageMetadataType
Namespace.addCategoryObject('typeBinding', 'MessageMetadataType', MessageMetadataType)


# Complex type {http://www.faa.aero/nas/3.0}NasExpandedRouteType with content type ELEMENT_ONLY
class NasExpandedRouteType (_ImportedBinding__fx.ExpandedRouteType):
    """
            Extends Expanded Route with a Route Impact List 
             
            .Route Impact List: Current traffic flow management prediction of en route Air Traffic 
            Control units (centres), sectors and airspace elements along the trajectory of a 
            flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasExpandedRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 140, 3)
    _ElementMap = _ImportedBinding__fx.ExpandedRouteType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.ExpandedRouteType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.ExpandedRouteType
    
    # Element routeImpactList uses Python identifier routeImpactList
    __routeImpactList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routeImpactList'), 'routeImpactList', '__httpwww_faa_aeronas3_0_NasExpandedRouteType_routeImpactList', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 153, 15), )

    
    routeImpactList = property(__routeImpactList.value, __routeImpactList.set, None, '\n                        .Route Impact List: Current traffic flow management prediction of en route Air Traffic \n                        Control units (centres), sectors and airspace elements along the trajectory of a \n                        flight. \n                     ')

    
    # Element routePoint (routePoint) inherited from {http://www.fixm.aero/flight/3.0}ExpandedRouteType
    _ElementMap.update({
        __routeImpactList.name() : __routeImpactList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasExpandedRouteType = NasExpandedRouteType
Namespace.addCategoryObject('typeBinding', 'NasExpandedRouteType', NasExpandedRouteType)


# Complex type {http://www.faa.aero/nas/3.0}NasAdvisoryType with content type EMPTY
class NasAdvisoryType (pyxb.binding.basis.complexTypeDefinition):
    """
            .NAS Advisory Information: A container for Traffic Flow Management advisories pertinent 
            to a single flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAdvisoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 137, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute advisoryNumber uses Python identifier advisoryNumber
    __advisoryNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'advisoryNumber'), 'advisoryNumber', '__httpwww_faa_aeronas3_0_NasAdvisoryType_advisoryNumber', _ImportedBinding__fb.FreeTextType)
    __advisoryNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 144, 6)
    __advisoryNumber._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 144, 6)
    
    advisoryNumber = property(__advisoryNumber.value, __advisoryNumber.set, None, '\n               .Traffic Flow Management Advisory Number: Advisory number issued by traffic flow \n               management. \n               .Traffic Flow Management Advisory Type: The type for the advisory issued by traffic \n               flow management. \n            ')

    
    # Attribute advisoryType uses Python identifier advisoryType
    __advisoryType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'advisoryType'), 'advisoryType', '__httpwww_faa_aeronas3_0_NasAdvisoryType_advisoryType', _module_typeBindings.AdvisoryTypeType)
    __advisoryType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 154, 6)
    __advisoryType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 154, 6)
    
    advisoryType = property(__advisoryType.value, __advisoryType.set, None, '\n               .Traffic Flow Management Advisory Number: Advisory number issued by traffic flow \n               management. \n               .Traffic Flow Management Advisory Type: The type for the advisory issued by traffic \n               flow management. \n            ')

    
    # Attribute advisoryUpdateTime uses Python identifier advisoryUpdateTime
    __advisoryUpdateTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'advisoryUpdateTime'), 'advisoryUpdateTime', '__httpwww_faa_aeronas3_0_NasAdvisoryType_advisoryUpdateTime', _ImportedBinding__ff.TimeType)
    __advisoryUpdateTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 164, 6)
    __advisoryUpdateTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 164, 6)
    
    advisoryUpdateTime = property(__advisoryUpdateTime.value, __advisoryUpdateTime.set, None, '\n               .Traffic Flow Management Advisory Update Time: The date and time when the advisory \n               was last updated. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __advisoryNumber.name() : __advisoryNumber,
        __advisoryType.name() : __advisoryType,
        __advisoryUpdateTime.name() : __advisoryUpdateTime
    })
_module_typeBindings.NasAdvisoryType = NasAdvisoryType
Namespace.addCategoryObject('typeBinding', 'NasAdvisoryType', NasAdvisoryType)


# Complex type {http://www.faa.aero/nas/3.0}ConstrainedAirspaceEntryType with content type EMPTY
class ConstrainedAirspaceEntryType (pyxb.binding.basis.complexTypeDefinition):
    """
            Container for NAS Trajectory Option Constraints. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConstrainedAirspaceEntryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 64, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute earliestAirspaceEntryTime uses Python identifier earliestAirspaceEntryTime
    __earliestAirspaceEntryTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'earliestAirspaceEntryTime'), 'earliestAirspaceEntryTime', '__httpwww_faa_aeronas3_0_ConstrainedAirspaceEntryType_earliestAirspaceEntryTime', _ImportedBinding__ff.TimeType)
    __earliestAirspaceEntryTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 70, 6)
    __earliestAirspaceEntryTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 70, 6)
    
    earliestAirspaceEntryTime = property(__earliestAirspaceEntryTime.value, __earliestAirspaceEntryTime.set, None, '\n               .Airspace Entry Time - Earliest: The earliest time the flight could enter the constrained \n               airspace. \n            ')

    
    # Attribute impactFca uses Python identifier impactFca
    __impactFca = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'impactFca'), 'impactFca', '__httpwww_faa_aeronas3_0_ConstrainedAirspaceEntryType_impactFca', _ImportedBinding__fb.ConstrainedAirspaceType)
    __impactFca._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 78, 6)
    __impactFca._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 78, 6)
    
    impactFca = property(__impactFca.value, __impactFca.set, None, '\n               Contains: \n               .Airspace Identifier: Unique Identifier for the constrained airspace to be traversed \n               by the trajectory option. \n               .Trajectory Airspace Impact: Container for the list of constrained airspace areas \n               to be traversed by the trajectory option. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __earliestAirspaceEntryTime.name() : __earliestAirspaceEntryTime,
        __impactFca.name() : __impactFca
    })
_module_typeBindings.ConstrainedAirspaceEntryType = ConstrainedAirspaceEntryType
Namespace.addCategoryObject('typeBinding', 'ConstrainedAirspaceEntryType', ConstrainedAirspaceEntryType)


# Complex type {http://www.faa.aero/nas/3.0}CmsAccuracyType with content type SIMPLE
class CmsAccuracyType (_ImportedBinding__ff.DistanceType):
    """
            .Performance-Based Navigation Accuracy: This is the flight's navigation accuracy 
            value for the phase of flight, specified in the Performance-Based Navigation Phase. 
            
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CmsAccuracyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 64, 3)
    _ElementMap = _ImportedBinding__ff.DistanceType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.DistanceType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.DistanceType
    
    # Attribute phase uses Python identifier phase
    __phase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phase'), 'phase', '__httpwww_faa_aeronas3_0_CmsAccuracyType_phase', _module_typeBindings.NasPerformanceBasedNavigationPhaseType)
    __phase._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 74, 12)
    __phase._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 74, 12)
    
    phase = property(__phase.value, __phase.set, None, '\n                     .Performance-Based Navigation Phase: The phase of flight for which navigation performance \n                     is being recorded. \n                  ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_faa_aeronas3_0_CmsAccuracyType_type', _module_typeBindings.CmsAccuracyTypeType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 82, 12)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 82, 12)
    
    type = property(__type.value, __type.set, None, '\n                     .Performance-Based Navigation Category: This is an enumeration indicating whether \n                     the accuracy measure in Performance-Based Navigation Accuracy is measuring Area Navigation \n                     (RNAV) or Required Navigation Performance (RNP). \n                  ')

    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}DistanceType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __phase.name() : __phase,
        __type.name() : __type
    })
_module_typeBindings.CmsAccuracyType = CmsAccuracyType
Namespace.addCategoryObject('typeBinding', 'CmsAccuracyType', CmsAccuracyType)


# Complex type {http://www.faa.aero/nas/3.0}AboveAltitudeType with content type SIMPLE
class AboveAltitudeType (_ImportedBinding__ff.AltitudeType):
    """
            aircraft operating above a specified altitude 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AboveAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 62, 3)
    _ElementMap = _ImportedBinding__ff.AltitudeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AltitudeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AltitudeType
    
    # Attribute ref inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AboveAltitudeType = AboveAltitudeType
Namespace.addCategoryObject('typeBinding', 'AboveAltitudeType', AboveAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}SimpleAltitudeType with content type SIMPLE
class SimpleAltitudeType (_ImportedBinding__ff.AltitudeType):
    """
            The only NAS altitude that maps directly to the core ICAO altitude types. 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 201, 3)
    _ElementMap = _ImportedBinding__ff.AltitudeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AltitudeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AltitudeType
    
    # Attribute ref inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimpleAltitudeType = SimpleAltitudeType
Namespace.addCategoryObject('typeBinding', 'SimpleAltitudeType', SimpleAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}VfrOnTopPlusAltitudeType with content type SIMPLE
class VfrOnTopPlusAltitudeType (_ImportedBinding__ff.AltitudeType):
    """
            vfr-on-top with altitude 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VfrOnTopPlusAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 230, 3)
    _ElementMap = _ImportedBinding__ff.AltitudeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AltitudeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AltitudeType
    
    # Attribute ref inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VfrOnTopPlusAltitudeType = VfrOnTopPlusAltitudeType
Namespace.addCategoryObject('typeBinding', 'VfrOnTopPlusAltitudeType', VfrOnTopPlusAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}VfrPlusAltitudeType with content type SIMPLE
class VfrPlusAltitudeType (_ImportedBinding__ff.AltitudeType):
    """
            vfr plus altitude 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VfrPlusAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 241, 3)
    _ElementMap = _ImportedBinding__ff.AltitudeType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__ff.AltitudeType._AttributeMap.copy()
    # Base type is _ImportedBinding__ff.AltitudeType
    
    # Attribute ref inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.VfrPlusAltitudeType = VfrPlusAltitudeType
Namespace.addCategoryObject('typeBinding', 'VfrPlusAltitudeType', VfrPlusAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}NasAirspaceConstraintType with content type ELEMENT_ONLY
class NasAirspaceConstraintType (_ImportedBinding__fx.AirspaceConstraintType):
    """
            Container for Airspace Slot Handling. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAirspaceConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 197, 3)
    _ElementMap = _ImportedBinding__fx.AirspaceConstraintType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.AirspaceConstraintType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.AirspaceConstraintType
    
    # Element entryTime uses Python identifier entryTime
    __entryTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'entryTime'), 'entryTime', '__httpwww_faa_aeronas3_0_NasAirspaceConstraintType_entryTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 206, 15), )

    
    entryTime = property(__entryTime.value, __entryTime.set, None, '\n                        Container for : \n                        Airspace Entry Time - Earliest \n                        Airspace Entry Time - Initial \n                        Airspace Entry Time - Original \n                        Airspace Entry Time - Traffic Flow Management System Estimated \n                     ')

    
    # Element exitTime uses Python identifier exitTime
    __exitTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'exitTime'), 'exitTime', '__httpwww_faa_aeronas3_0_NasAirspaceConstraintType_exitTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 217, 15), )

    
    exitTime = property(__exitTime.value, __exitTime.set, None, '\n                        .Airspace Exit Time - Traffic Flow Management System Estimated: The estimated airspace \n                        exit time considering all data sources, as determined by Traffic Flow Management \n                        System (TFMS). \n                        .Airspace Entry Time - Traffic Flow Management System Estimated: The estimated airspace \n                        entry time considering all data sources, as determined by Traffic Flow Management \n                        System (TFMS). \n                     ')

    
    # Element airspaceControlledEntryTime (airspaceControlledEntryTime) inherited from {http://www.fixm.aero/flight/3.0}AirspaceConstraintType
    
    # Attribute arrivalSlot uses Python identifier arrivalSlot
    __arrivalSlot = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalSlot'), 'arrivalSlot', '__httpwww_faa_aeronas3_0_NasAirspaceConstraintType_arrivalSlot', _ImportedBinding__fb.FreeTextType)
    __arrivalSlot._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 230, 12)
    __arrivalSlot._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 230, 12)
    
    arrivalSlot = property(__arrivalSlot.value, __arrivalSlot.set, None, '\n                     .Arrival Slot - NAS: A time slot at an airport or airspace entry point that identifies \n                     a point in time when an aircraft is constrained to arrive at the airport or airspace \n                     entry point. \n                  ')

    
    # Attribute holdStatus uses Python identifier holdStatus
    __holdStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'holdStatus'), 'holdStatus', '__httpwww_faa_aeronas3_0_NasAirspaceConstraintType_holdStatus', _module_typeBindings.SlotHoldStatusType)
    __holdStatus._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 239, 12)
    __holdStatus._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 239, 12)
    
    holdStatus = property(__holdStatus.value, __holdStatus.set, None, '\n                     .Slot Hold Status: If a flight is controlled and cancelled [e.g., has a Controlled \n                     Time of Departure (CTD), Controlled Time of Arrival (CTA), and Arrival Slot (ASLOT)], \n                     the slot hold status indicates whether the slot associated with this flight is being \n                     held, or would be held, by the Airspace User for the next full compression. \n                  ')

    
    # Attribute yieldedSlot uses Python identifier yieldedSlot
    __yieldedSlot = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'yieldedSlot'), 'yieldedSlot', '__httpwww_faa_aeronas3_0_NasAirspaceConstraintType_yieldedSlot', _module_typeBindings.SlotYieldedIndicatorType)
    __yieldedSlot._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 249, 12)
    __yieldedSlot._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 249, 12)
    
    yieldedSlot = property(__yieldedSlot.value, __yieldedSlot.set, None, '\n                     .Yielded Slot Indicator: Indicates the slot currently specified in   Runway Arrival \n                     Time - Controlled   is to be given up by the Airspace User in return for a later \n                     slot. \n                  ')

    
    # Attribute constrainedAirspace inherited from {http://www.fixm.aero/flight/3.0}AirspaceConstraintType
    _ElementMap.update({
        __entryTime.name() : __entryTime,
        __exitTime.name() : __exitTime
    })
    _AttributeMap.update({
        __arrivalSlot.name() : __arrivalSlot,
        __holdStatus.name() : __holdStatus,
        __yieldedSlot.name() : __yieldedSlot
    })
_module_typeBindings.NasAirspaceConstraintType = NasAirspaceConstraintType
Namespace.addCategoryObject('typeBinding', 'NasAirspaceConstraintType', NasAirspaceConstraintType)


# Complex type {http://www.faa.aero/nas/3.0}NasFlightIdentificationType with content type ELEMENT_ONLY
class NasFlightIdentificationType (_ImportedBinding__fx.FlightIdentificationType):
    """
            Extends aircraft identity to include computer id and SSPID. 
            .Site Specific Plan Identifier: Site Specific Plan Identifier is a unique ID for 
            each system plan in each ERAM facility. 
            .Computer ID: A unique identification assigned by ERAM to each flight plan. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasFlightIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 349, 3)
    _ElementMap = _ImportedBinding__fx.FlightIdentificationType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.FlightIdentificationType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.FlightIdentificationType
    
    # Element marketingCarrierFlightIdentifier (marketingCarrierFlightIdentifier) inherited from {http://www.fixm.aero/flight/3.0}FlightIdentificationType
    
    # Attribute computerId uses Python identifier computerId
    __computerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'computerId'), 'computerId', '__httpwww_faa_aeronas3_0_NasFlightIdentificationType_computerId', _ImportedBinding__fb.FreeTextType)
    __computerId._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 360, 12)
    __computerId._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 360, 12)
    
    computerId = property(__computerId.value, __computerId.set, None, '\n                     .Computer ID: A unique identification assigned by ERAM to each flight plan. \n                  ')

    
    # Attribute siteSpecificPlanId uses Python identifier siteSpecificPlanId
    __siteSpecificPlanId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'siteSpecificPlanId'), 'siteSpecificPlanId', '__httpwww_faa_aeronas3_0_NasFlightIdentificationType_siteSpecificPlanId', _ImportedBinding__fb.CountType)
    __siteSpecificPlanId._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 367, 12)
    __siteSpecificPlanId._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 367, 12)
    
    siteSpecificPlanId = property(__siteSpecificPlanId.value, __siteSpecificPlanId.set, None, '\n                     .Site Specific Plan Identifier: Site Specific Plan Identifier is a unique ID for \n                     each system plan in each ERAM facility. \n                  ')

    
    # Attribute aircraftIdentification inherited from {http://www.fixm.aero/flight/3.0}FlightIdentificationType
    
    # Attribute majorCarrierIdentifier inherited from {http://www.fixm.aero/flight/3.0}FlightIdentificationType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __computerId.name() : __computerId,
        __siteSpecificPlanId.name() : __siteSpecificPlanId
    })
_module_typeBindings.NasFlightIdentificationType = NasFlightIdentificationType
Namespace.addCategoryObject('typeBinding', 'NasFlightIdentificationType', NasFlightIdentificationType)


# Complex type {http://www.faa.aero/nas/3.0}NasSupplementalDataType with content type ELEMENT_ONLY
class NasSupplementalDataType (_ImportedBinding__fx.SupplementalDataType):
    """
            Container for additional data specific to nas such as additional flight information. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasSupplementalDataType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 380, 3)
    _ElementMap = _ImportedBinding__fx.SupplementalDataType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.SupplementalDataType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.SupplementalDataType
    
    # Element additionalFlightInformation uses Python identifier additionalFlightInformation
    __additionalFlightInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'additionalFlightInformation'), 'additionalFlightInformation', '__httpwww_faa_aeronas3_0_NasSupplementalDataType_additionalFlightInformation', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 390, 15), )

    
    additionalFlightInformation = property(__additionalFlightInformation.value, __additionalFlightInformation.set, None, '\n                        Additional information about a flight expressed in key-value pairs. \n                        .Other Flight Information: This element consists of an identification tag/indicator \n                        and the relevant value. This information is   extra   information about the flight \n                        that does not fall into some other predefined category. \n                     ')

    
    # Element pilotInCommand (pilotInCommand) inherited from {http://www.fixm.aero/flight/3.0}SupplementalDataType
    
    # Attribute fuelEndurance inherited from {http://www.fixm.aero/flight/3.0}SupplementalDataType
    
    # Attribute personsOnBoard inherited from {http://www.fixm.aero/flight/3.0}SupplementalDataType
    _ElementMap.update({
        __additionalFlightInformation.name() : __additionalFlightInformation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasSupplementalDataType = NasSupplementalDataType
Namespace.addCategoryObject('typeBinding', 'NasSupplementalDataType', NasSupplementalDataType)


# Complex type {http://www.faa.aero/nas/3.0}NasFlightPlanType with content type EMPTY
class NasFlightPlanType (_ImportedBinding__fb.FeatureType):
    """
            Describes the flight plan structure used by NAS. Based on core ICAO flight plan. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasFlightPlanType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightPlan.xsd', 60, 3)
    _ElementMap = _ImportedBinding__fb.FeatureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fb.FeatureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fb.FeatureType
    
    # Attribute flightPlanRemarks uses Python identifier flightPlanRemarks
    __flightPlanRemarks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'flightPlanRemarks'), 'flightPlanRemarks', '__httpwww_faa_aeronas3_0_NasFlightPlanType_flightPlanRemarks', _ImportedBinding__fb.FreeTextType)
    __flightPlanRemarks._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightPlan.xsd', 69, 12)
    __flightPlanRemarks._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightPlan.xsd', 69, 12)
    
    flightPlanRemarks = property(__flightPlanRemarks.value, __flightPlanRemarks.set, None, '\n                     .Traffic Flow Management System Flight Plan Remarks: NAS Flight Plan Field 11 remarks \n                     processed by the Traffic Flow Management System (TFMS) and used for TFM purposes. \n                     \n                  ')

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpwww_faa_aeronas3_0_NasFlightPlanType_identifier', _ImportedBinding__fb.FreeTextType)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightPlan.xsd', 78, 12)
    __identifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightPlan.xsd', 78, 12)
    
    identifier = property(__identifier.value, __identifier.set, None, '\n                     .Flight Plan Identifier: The flight plan identifier is used to uniquely name a flight \n                     plan within the scope of its flight. \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __flightPlanRemarks.name() : __flightPlanRemarks,
        __identifier.name() : __identifier
    })
_module_typeBindings.NasFlightPlanType = NasFlightPlanType
Namespace.addCategoryObject('typeBinding', 'NasFlightPlanType', NasFlightPlanType)


# Complex type {http://www.faa.aero/nas/3.0}NasAdaptedRouteType with content type EMPTY
class NasAdaptedRouteType (pyxb.binding.basis.complexTypeDefinition):
    """
            Representation of converted route 
         
            .Adapted Departure Route Identifier: The identifier used to internally identify the 
            Adapted Departure Route (ADR). 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAdaptedRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 94, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute nasRouteAlphanumeric uses Python identifier nasRouteAlphanumeric
    __nasRouteAlphanumeric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nasRouteAlphanumeric'), 'nasRouteAlphanumeric', '__httpwww_faa_aeronas3_0_NasAdaptedRouteType_nasRouteAlphanumeric', _ImportedBinding__fb.FreeTextType)
    __nasRouteAlphanumeric._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 103, 6)
    __nasRouteAlphanumeric._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 103, 6)
    
    nasRouteAlphanumeric = property(__nasRouteAlphanumeric.value, __nasRouteAlphanumeric.set, None, '\n               Route (AAR) to be provided to the controller at the time the auto-route is applied. \n               \n               .Adapted Departure Arrival Route Clearance Support Alphanumerics: This field contains \n               the route string with an Adapted Departure Arrival Route (ADAR) to be provided to \n               the controller at the time the auto-route is applied. \n               .Adapted Arrival Route Clearance Support Alphanumerics: This field contains the route \n               string with an Adapted Arrival Route (AAR) to be provided to the controller at the \n               time the auto-route is applied. \n               .Adapted Departure Route Clearance Support Alphanumerics: This field contains the \n               route string with an Adapted Departure Route (ADR) to be provided to the controller \n               at the time the auto-route is applied. \n            ')

    
    # Attribute nasRouteIdentifier uses Python identifier nasRouteIdentifier
    __nasRouteIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nasRouteIdentifier'), 'nasRouteIdentifier', '__httpwww_faa_aeronas3_0_NasAdaptedRouteType_nasRouteIdentifier', _module_typeBindings.STD_ANON_3)
    __nasRouteIdentifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 120, 6)
    __nasRouteIdentifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 120, 6)
    
    nasRouteIdentifier = property(__nasRouteIdentifier.value, __nasRouteIdentifier.set, None, '\n               .Adapted Departure Arrival Route Identifier: The five character identifier is used \n               to internally identify an Adapted Departure Arrival Route (ADAR). \n               .Adapted Departure Route Identifier: The identifier used to internally identify the \n               Adapted Departure Route (ADR). \n               .Adapted Arrival Route Identifier: The five character identifier used to internally \n               identify an adapted arrival route. \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nasRouteAlphanumeric.name() : __nasRouteAlphanumeric,
        __nasRouteIdentifier.name() : __nasRouteIdentifier
    })
_module_typeBindings.NasAdaptedRouteType = NasAdaptedRouteType
Namespace.addCategoryObject('typeBinding', 'NasAdaptedRouteType', NasAdaptedRouteType)


# Complex type {http://www.faa.aero/nas/3.0}NasRoutePointType with content type ELEMENT_ONLY
class NasRoutePointType (_ImportedBinding__fx.AbstractRoutePointType):
    """
            Contains NAS Route Point with additional NAS Flight Rules. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasRoutePointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 282, 3)
    _ElementMap = _ImportedBinding__fx.AbstractRoutePointType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.AbstractRoutePointType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.AbstractRoutePointType
    
    # Element point (point) inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute nasFlightRules uses Python identifier nasFlightRules
    __nasFlightRules = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nasFlightRules'), 'nasFlightRules', '__httpwww_faa_aeronas3_0_NasRoutePointType_nasFlightRules', _module_typeBindings.NasFlightRulesType)
    __nasFlightRules._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 290, 12)
    __nasFlightRules._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 290, 12)
    
    nasFlightRules = property(__nasFlightRules.value, __nasFlightRules.set, None, '\n                     .Flight Rules - NAS: The regulation, or combination of regulations, that governs \n                     all aspects of operations under which the pilot plans to fly in the NAS. \n                  ')

    
    # Attribute airTrafficType inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute clearanceLimit inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute delayAtPoint inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    
    # Attribute flightRules inherited from {http://www.fixm.aero/flight/3.0}AbstractRoutePointType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nasFlightRules.name() : __nasFlightRules
    })
_module_typeBindings.NasRoutePointType = NasRoutePointType
Namespace.addCategoryObject('typeBinding', 'NasRoutePointType', NasRoutePointType)


# Complex type {http://www.faa.aero/nas/3.0}NasRouteSegmentType with content type ELEMENT_ONLY
class NasRouteSegmentType (_ImportedBinding__fx.RouteSegmentType):
    """
            Extends the core ICAO flight segment information to add NAS extensions: 
                   1. planned delay at fix,
                   2. number of planned re-entries into the segment, 
                   3. number of special re-entries into the segment.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasRouteSegmentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 303, 3)
    _ElementMap = _ImportedBinding__fx.RouteSegmentType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.RouteSegmentType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.RouteSegmentType
    
    # Element routePoint (routePoint) inherited from {http://www.fixm.aero/flight/3.0}RouteSegmentType
    
    # Attribute reEntryCount uses Python identifier reEntryCount
    __reEntryCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reEntryCount'), 'reEntryCount', '__httpwww_faa_aeronas3_0_NasRouteSegmentType_reEntryCount', _ImportedBinding__fb.CountType)
    __reEntryCount._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 314, 12)
    __reEntryCount._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 314, 12)
    
    reEntryCount = property(__reEntryCount.value, __reEntryCount.set, None, '\n                     .NAS Route - Reentry for Military Route: An indication that a portion of a Military \n                     Route is to be flown more than once.  The element includes an indication of which \n                     adapted portion of the route as well as the number of times the fixes are to be flown. \n                     It is filed in a NAS Route string and associated with a Military Route. There can \n                     be up to two of these per Military Route in the NAS route string. \n                  ')

    
    # Attribute reEntrySpecial uses Python identifier reEntrySpecial
    __reEntrySpecial = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reEntrySpecial'), 'reEntrySpecial', '__httpwww_faa_aeronas3_0_NasRouteSegmentType_reEntrySpecial', _ImportedBinding__fb.CountType)
    __reEntrySpecial._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 325, 12)
    __reEntrySpecial._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 325, 12)
    
    reEntrySpecial = property(__reEntrySpecial.value, __reEntrySpecial.set, None, '\n                     Count of the reentry Special route. \n                  ')

    
    # Attribute airway inherited from {http://www.fixm.aero/flight/3.0}RouteSegmentType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reEntryCount.name() : __reEntryCount,
        __reEntrySpecial.name() : __reEntrySpecial
    })
_module_typeBindings.NasRouteSegmentType = NasRouteSegmentType
Namespace.addCategoryObject('typeBinding', 'NasRouteSegmentType', NasRouteSegmentType)


# Complex type {http://www.faa.aero/nas/3.0}NasRerouteType with content type EMPTY
class NasRerouteType (pyxb.binding.basis.complexTypeDefinition):
    """
            .Traffic Flow Management Reroute Information: A container for information pertinent 
            to a single NAS reroute issued for a flight by traffic flow management. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasRerouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 175, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rerouteIdentifier uses Python identifier rerouteIdentifier
    __rerouteIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rerouteIdentifier'), 'rerouteIdentifier', '__httpwww_faa_aeronas3_0_NasRerouteType_rerouteIdentifier', _module_typeBindings.STD_ANON_6)
    __rerouteIdentifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 182, 6)
    __rerouteIdentifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 182, 6)
    
    rerouteIdentifier = property(__rerouteIdentifier.value, __rerouteIdentifier.set, None, '\n               .Traffic Flow Management System Reroute Identifier: Traffic Flow Management System \n               generated unique identifier for the reroute. \n               .Traffic Flow Management System Reroute Name: Traffic Flow Management System assigned \n               name for the reroute. \n               .Traffic Flow Management System Reroute Type: Route type of the assigned reroute. \n               \n            ')

    
    # Attribute rerouteInclusionIndicator uses Python identifier rerouteInclusionIndicator
    __rerouteInclusionIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rerouteInclusionIndicator'), 'rerouteInclusionIndicator', '__httpwww_faa_aeronas3_0_NasRerouteType_rerouteInclusionIndicator', _module_typeBindings.RerouteInclusionIndicatorType)
    __rerouteInclusionIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 200, 6)
    __rerouteInclusionIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 200, 6)
    
    rerouteInclusionIndicator = property(__rerouteInclusionIndicator.value, __rerouteInclusionIndicator.set, None, '\n               .Traffic Flow Management System Reroute Inclusion Indicator: Indicates whether the \n               flight is included or proposed to be included in the traffic management reroute initiative. \n               \n            ')

    
    # Attribute rerouteName uses Python identifier rerouteName
    __rerouteName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rerouteName'), 'rerouteName', '__httpwww_faa_aeronas3_0_NasRerouteType_rerouteName', _module_typeBindings.STD_ANON_7)
    __rerouteName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 209, 6)
    __rerouteName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 209, 6)
    
    rerouteName = property(__rerouteName.value, __rerouteName.set, None, '\n               .Traffic Flow Management System Reroute Identifier: Traffic Flow Management System \n               generated unique identifier for the reroute. \n               .Traffic Flow Management System Reroute Name: Traffic Flow Management System assigned \n               name for the reroute. \n               .Traffic Flow Management System Reroute Type: Route type of the assigned reroute. \n               \n            ')

    
    # Attribute rerouteProtectedSegment uses Python identifier rerouteProtectedSegment
    __rerouteProtectedSegment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rerouteProtectedSegment'), 'rerouteProtectedSegment', '__httpwww_faa_aeronas3_0_NasRerouteType_rerouteProtectedSegment', _module_typeBindings.STD_ANON_8)
    __rerouteProtectedSegment._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 227, 6)
    __rerouteProtectedSegment._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 227, 6)
    
    rerouteProtectedSegment = property(__rerouteProtectedSegment.value, __rerouteProtectedSegment.set, None, '\n               .Traffic Flow Management System Reroute Protected Segment: All or a portion of the \n               route string that is designated as the protected portion. \n            ')

    
    # Attribute rerouteType uses Python identifier rerouteType
    __rerouteType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rerouteType'), 'rerouteType', '__httpwww_faa_aeronas3_0_NasRerouteType_rerouteType', _module_typeBindings.RerouteTypeType)
    __rerouteType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 241, 6)
    __rerouteType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 241, 6)
    
    rerouteType = property(__rerouteType.value, __rerouteType.set, None, '\n               .Traffic Flow Management System Reroute Identifier: Traffic Flow Management System \n               generated unique identifier for the reroute. \n               .Traffic Flow Management System Reroute Name: Traffic Flow Management System assigned \n               name for the reroute. \n               .Traffic Flow Management System Reroute Type: Route type of the assigned reroute. \n               \n            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rerouteIdentifier.name() : __rerouteIdentifier,
        __rerouteInclusionIndicator.name() : __rerouteInclusionIndicator,
        __rerouteName.name() : __rerouteName,
        __rerouteProtectedSegment.name() : __rerouteProtectedSegment,
        __rerouteType.name() : __rerouteType
    })
_module_typeBindings.NasRerouteType = NasRerouteType
Namespace.addCategoryObject('typeBinding', 'NasRerouteType', NasRerouteType)


# Complex type {http://www.faa.aero/nas/3.0}NasAircraftType with content type ELEMENT_ONLY
class NasAircraftType (_ImportedBinding__fx.AircraftType_):
    """
            NAS specific extensions to aircraft information 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAircraftType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 258, 3)
    _ElementMap = _ImportedBinding__fx.AircraftType_._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.AircraftType_._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.AircraftType_
    
    # Element accuracy uses Python identifier accuracy
    __accuracy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'accuracy'), 'accuracy', '__httpwww_faa_aeronas3_0_NasAircraftType_accuracy', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 267, 15), )

    
    accuracy = property(__accuracy.value, __accuracy.set, None, "\n                        NAS extension for Performance-Based Navigation Accuracy. \n                        .Performance-Based Navigation Accuracy: This is the flight's navigation accuracy \n                        value for the phase of flight, specified in the Performance-Based Navigation Phase. \n                        \n                        .Performance-Based Navigation Category: This is an enumeration indicating whether \n                        the accuracy measure in Performance-Based Navigation Accuracy is measuring Area Navigation \n                        (RNAV) or Required Navigation Performance (RNP). \n                     ")

    
    # Element aircraftType (aircraftType) inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Element capabilities (capabilities) inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute equipmentQualifier uses Python identifier equipmentQualifier
    __equipmentQualifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'equipmentQualifier'), 'equipmentQualifier', '__httpwww_faa_aeronas3_0_NasAircraftType_equipmentQualifier', _module_typeBindings.NasAirborneEquipmentQualifierType)
    __equipmentQualifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 281, 12)
    __equipmentQualifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 281, 12)
    
    equipmentQualifier = property(__equipmentQualifier.value, __equipmentQualifier.set, None, '\n                     .Airborne Equipment Qualifier: A value assigned to the aircraft, based on its navigational \n                     equipment, whether or not it has a transponder, and if it has a transponder, whether \n                     the transponder supports Mode C. \n                  ')

    
    # Attribute nasWakeTurbulence uses Python identifier nasWakeTurbulence
    __nasWakeTurbulence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nasWakeTurbulence'), 'nasWakeTurbulence', '__httpwww_faa_aeronas3_0_NasAircraftType_nasWakeTurbulence', _module_typeBindings.WakeTurbulenceCategoryExtendedType)
    __nasWakeTurbulence._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 290, 12)
    __nasWakeTurbulence._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 290, 12)
    
    nasWakeTurbulence = property(__nasWakeTurbulence.value, __nasWakeTurbulence.set, None, '\n                     .Wake Turbulence Category - NAS: NAS classification of the aircraft wake turbulence, \n                     based on wingspan and Maximum Takeoff Weight (MTOW). \n                  ')

    
    # Attribute tfmsSpecialAircraftQualifier uses Python identifier tfmsSpecialAircraftQualifier
    __tfmsSpecialAircraftQualifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tfmsSpecialAircraftQualifier'), 'tfmsSpecialAircraftQualifier', '__httpwww_faa_aeronas3_0_NasAircraftType_tfmsSpecialAircraftQualifier', _module_typeBindings.NasSpecialAircraftQualifierType)
    __tfmsSpecialAircraftQualifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 298, 12)
    __tfmsSpecialAircraftQualifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 298, 12)
    
    tfmsSpecialAircraftQualifier = property(__tfmsSpecialAircraftQualifier.value, __tfmsSpecialAircraftQualifier.set, None, '\n                     .Special Aircraft Qualifier: Indicates the flight is a heavy jet, B757 or, if not \n                     present, a large jet and if the flight is either equipped or not with TCAS. This \n                     indicator is used for output purposes such as strip printing and message transfers \n                     to other facilities such as Automated Radar Terminal System (ARTS). \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute aircraftAddress inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute aircraftColours inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute aircraftPerformance inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute aircraftQuantity inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute engineType inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute registration inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    
    # Attribute wakeTurbulence inherited from {http://www.fixm.aero/flight/3.0}AircraftType
    _ElementMap.update({
        __accuracy.name() : __accuracy
    })
    _AttributeMap.update({
        __equipmentQualifier.name() : __equipmentQualifier,
        __nasWakeTurbulence.name() : __nasWakeTurbulence,
        __tfmsSpecialAircraftQualifier.name() : __tfmsSpecialAircraftQualifier
    })
_module_typeBindings.NasAircraftType = NasAircraftType
Namespace.addCategoryObject('typeBinding', 'NasAircraftType', NasAircraftType)


# Complex type {http://www.faa.aero/nas/3.0}NasArrivalType with content type ELEMENT_ONLY
class NasArrivalType (_ImportedBinding__fx.FlightArrivalType):
    """
            Extends core Flight Arrival with NAS specific Extensions. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasArrivalType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 64, 3)
    _ElementMap = _ImportedBinding__fx.FlightArrivalType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.FlightArrivalType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.FlightArrivalType
    
    # Element runwayArrivalTime uses Python identifier runwayArrivalTime
    __runwayArrivalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'runwayArrivalTime'), 'runwayArrivalTime', '__httpwww_faa_aeronas3_0_NasArrivalType_runwayArrivalTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 73, 15), )

    
    runwayArrivalTime = property(__runwayArrivalTime.value, __runwayArrivalTime.set, None, '\n                        Contains the NAS Specific arrival times. \n                     ')

    
    # Element approachFix (approachFix) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element approachTime (approachTime) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element arrivalAerodrome (arrivalAerodrome) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element arrivalAerodromeAlternate (arrivalAerodromeAlternate) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element arrivalAerodromeOriginal (arrivalAerodromeOriginal) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element arrivalFix (arrivalFix) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element arrivalFixTime (arrivalFixTime) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element filedRevisedDestinationAerodrome (filedRevisedDestinationAerodrome) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element runwayPositionAndTime (runwayPositionAndTime) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Element standPositionAndTime (standPositionAndTime) inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Attribute arrivalCenter uses Python identifier arrivalCenter
    __arrivalCenter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalCenter'), 'arrivalCenter', '__httpwww_faa_aeronas3_0_NasArrivalType_arrivalCenter', _ImportedBinding__fb.FreeTextType)
    __arrivalCenter._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 81, 12)
    __arrivalCenter._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 81, 12)
    
    arrivalCenter = property(__arrivalCenter.value, __arrivalCenter.set, None, '\n                     .Arrival Center: Indicates the Air Route Traffic Control Center (ARTCC) for the arrival \n                     point for a flight. \n                  ')

    
    # Attribute arrivalPoint uses Python identifier arrivalPoint
    __arrivalPoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPoint'), 'arrivalPoint', '__httpwww_faa_aeronas3_0_NasArrivalType_arrivalPoint', _module_typeBindings.STD_ANON)
    __arrivalPoint._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 89, 12)
    __arrivalPoint._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 89, 12)
    
    arrivalPoint = property(__arrivalPoint.value, __arrivalPoint.set, None, '\n                     .Arrival Point: The final point or other final entity where the air traffic control/management \n                     system route terminates. \n                  ')

    
    # Attribute arrivalSlot uses Python identifier arrivalSlot
    __arrivalSlot = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalSlot'), 'arrivalSlot', '__httpwww_faa_aeronas3_0_NasArrivalType_arrivalSlot', _ImportedBinding__fb.FreeTextType)
    __arrivalSlot._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 103, 12)
    __arrivalSlot._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 103, 12)
    
    arrivalSlot = property(__arrivalSlot.value, __arrivalSlot.set, None, '\n                     .Arrival Slot - NAS: A time slot at an airport or airspace entry point that identifies \n                     a point in time when an aircraft is constrained to arrive at the airport or airspace \n                     entry point. \n                  ')

    
    # Attribute holdStatus uses Python identifier holdStatus
    __holdStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'holdStatus'), 'holdStatus', '__httpwww_faa_aeronas3_0_NasArrivalType_holdStatus', _module_typeBindings.SlotHoldStatusType)
    __holdStatus._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 112, 12)
    __holdStatus._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 112, 12)
    
    holdStatus = property(__holdStatus.value, __holdStatus.set, None, '\n                     .Slot Hold Status: If a flight is controlled and cancelled [e.g., has a Controlled \n                     Time of Departure (CTD), Controlled Time of Arrival (CTA), and Arrival Slot (ASLOT)], \n                     the slot hold status indicates whether the slot associated with this flight is being \n                     held, or would be held, by the Airspace User for the next full compression. \n                  ')

    
    # Attribute scheduledInBlockTime uses Python identifier scheduledInBlockTime
    __scheduledInBlockTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scheduledInBlockTime'), 'scheduledInBlockTime', '__httpwww_faa_aeronas3_0_NasArrivalType_scheduledInBlockTime', _ImportedBinding__ff.TimeType)
    __scheduledInBlockTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 122, 12)
    __scheduledInBlockTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 122, 12)
    
    scheduledInBlockTime = property(__scheduledInBlockTime.value, __scheduledInBlockTime.set, None, '\n                     .In-Block Time - Scheduled: Scheduled gate time of arrival for a flight, as provided \n                     by the OAG (Official Airline Guide). \n                  ')

    
    # Attribute slotYielded uses Python identifier slotYielded
    __slotYielded = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'slotYielded'), 'slotYielded', '__httpwww_faa_aeronas3_0_NasArrivalType_slotYielded', _module_typeBindings.SlotYieldedIndicatorType)
    __slotYielded._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 130, 12)
    __slotYielded._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 130, 12)
    
    slotYielded = property(__slotYielded.value, __slotYielded.set, None, '\n                     .Yielded Slot Indicator: Indicates the slot currently specified in   Runway Arrival \n                     Time - Controlled   is to be given up by the Airspace User in return for a later \n                     slot. \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute arrivalFleetPrioritization inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Attribute arrivalSequenceNumber inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Attribute earliestInBlockTime inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Attribute filedRevisedDestinationStar inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Attribute landingLimits inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    
    # Attribute standardInstrumentArrival inherited from {http://www.fixm.aero/flight/3.0}FlightArrivalType
    _ElementMap.update({
        __runwayArrivalTime.name() : __runwayArrivalTime
    })
    _AttributeMap.update({
        __arrivalCenter.name() : __arrivalCenter,
        __arrivalPoint.name() : __arrivalPoint,
        __arrivalSlot.name() : __arrivalSlot,
        __holdStatus.name() : __holdStatus,
        __scheduledInBlockTime.name() : __scheduledInBlockTime,
        __slotYielded.name() : __slotYielded
    })
_module_typeBindings.NasArrivalType = NasArrivalType
Namespace.addCategoryObject('typeBinding', 'NasArrivalType', NasArrivalType)


# Complex type {http://www.faa.aero/nas/3.0}NasUnitBoundaryType with content type ELEMENT_ONLY
class NasUnitBoundaryType (_ImportedBinding__fx.UnitBoundaryType):
    """
            NAS Specific extension of BoundaryCrossing to include "actual" BoundaryCrossing attributes. 
            
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasUnitBoundaryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 110, 3)
    _ElementMap = _ImportedBinding__fx.UnitBoundaryType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.UnitBoundaryType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.UnitBoundaryType
    
    # Element boundaryCrossingActual uses Python identifier boundaryCrossingActual
    __boundaryCrossingActual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boundaryCrossingActual'), 'boundaryCrossingActual', '__httpwww_faa_aeronas3_0_NasUnitBoundaryType_boundaryCrossingActual', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 120, 15), )

    
    boundaryCrossingActual = property(__boundaryCrossingActual.value, __boundaryCrossingActual.set, None, '\n                        Container for the Actual Boundary Crossing Attributes \n                        .Boundary Crossing Time - Actual: The actual time at which a flight crosses the associated \n                        boundary crossing point. \n                        .Boundary Crossing Position - Actual: The actual boundary crossing point inbound \n                        to the Air Route Traffic Control Center (ARTCC) for the flight. \n                     ')

    
    # Element boundaryCrossingCoordinated (boundaryCrossingCoordinated) inherited from {http://www.fixm.aero/flight/3.0}UnitBoundaryType
    
    # Element boundaryCrossingProposed (boundaryCrossingProposed) inherited from {http://www.fixm.aero/flight/3.0}UnitBoundaryType
    
    # Element downstreamUnit (downstreamUnit) inherited from {http://www.fixm.aero/flight/3.0}UnitBoundaryType
    
    # Element handoff (handoff) inherited from {http://www.fixm.aero/flight/3.0}UnitBoundaryType
    
    # Element upstreamUnit (upstreamUnit) inherited from {http://www.fixm.aero/flight/3.0}UnitBoundaryType
    
    # Attribute delegated inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute sectorIdentifier inherited from {http://www.fixm.aero/base/3.0}AtcUnitReferenceType
    
    # Attribute unitBoundaryIndicator inherited from {http://www.fixm.aero/flight/3.0}UnitBoundaryType
    _ElementMap.update({
        __boundaryCrossingActual.name() : __boundaryCrossingActual
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasUnitBoundaryType = NasUnitBoundaryType
Namespace.addCategoryObject('typeBinding', 'NasUnitBoundaryType', NasUnitBoundaryType)


# Complex type {http://www.faa.aero/nas/3.0}NasDepartureType with content type ELEMENT_ONLY
class NasDepartureType (_ImportedBinding__fx.FlightDepartureType):
    """
            Extends core Flight Departue with NAS specific Extensions. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasDepartureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 63, 3)
    _ElementMap = _ImportedBinding__fx.FlightDepartureType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.FlightDepartureType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.FlightDepartureType
    
    # Element runwayDepartureTime uses Python identifier runwayDepartureTime
    __runwayDepartureTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'runwayDepartureTime'), 'runwayDepartureTime', '__httpwww_faa_aeronas3_0_NasDepartureType_runwayDepartureTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 72, 15), )

    
    runwayDepartureTime = property(__runwayDepartureTime.value, __runwayDepartureTime.set, None, '\n                        Container for NAS Specific Runway Departure Times. \n                     ')

    
    # Element departureAerodrome (departureAerodrome) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element departureFix (departureFix) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element departureFixTime (departureFixTime) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element departureTimes (departureTimes) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element offBlockReadyTime (offBlockReadyTime) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element runwayPositionAndTime (runwayPositionAndTime) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element standPositionAndTime (standPositionAndTime) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element takeoffAlternateAerodrome (takeoffAlternateAerodrome) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Element takeoffWeight (takeoffWeight) inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Attribute departureCenter uses Python identifier departureCenter
    __departureCenter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departureCenter'), 'departureCenter', '__httpwww_faa_aeronas3_0_NasDepartureType_departureCenter', _ImportedBinding__fb.FreeTextType)
    __departureCenter._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 80, 12)
    __departureCenter._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 80, 12)
    
    departureCenter = property(__departureCenter.value, __departureCenter.set, None, '\n                     .Departure Center: Indicates the Air Route Traffic Control Center (ARTCC) for the \n                     departure point for a flight. \n                  ')

    
    # Attribute departurePoint uses Python identifier departurePoint
    __departurePoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departurePoint'), 'departurePoint', '__httpwww_faa_aeronas3_0_NasDepartureType_departurePoint', _module_typeBindings.STD_ANON_)
    __departurePoint._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 88, 12)
    __departurePoint._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 88, 12)
    
    departurePoint = property(__departurePoint.value, __departurePoint.set, None, '\n                     .Departure Point: The first point or other initial entity where the air traffic control/management \n                     system route starts. \n                  ')

    
    # Attribute scheduledOffBlockTime uses Python identifier scheduledOffBlockTime
    __scheduledOffBlockTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scheduledOffBlockTime'), 'scheduledOffBlockTime', '__httpwww_faa_aeronas3_0_NasDepartureType_scheduledOffBlockTime', _ImportedBinding__ff.TimeType)
    __scheduledOffBlockTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 102, 12)
    __scheduledOffBlockTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 102, 12)
    
    scheduledOffBlockTime = property(__scheduledOffBlockTime.value, __scheduledOffBlockTime.set, None, '\n                     .Off-Block Time - Scheduled: Scheduled gate time of departure for a flight, as provided \n                     by the OAG (Official Airline Guide). \n                  ')

    
    # Attribute targetMAEntryTime uses Python identifier targetMAEntryTime
    __targetMAEntryTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetMAEntryTime'), 'targetMAEntryTime', '__httpwww_faa_aeronas3_0_NasDepartureType_targetMAEntryTime', _ImportedBinding__ff.TimeType)
    __targetMAEntryTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 110, 12)
    __targetMAEntryTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 110, 12)
    
    targetMAEntryTime = property(__targetMAEntryTime.value, __targetMAEntryTime.set, None, '\n                     .Movement Area Entry Time - Target: The time at which a flight is assigned to enter \n                     the Airport Movement Area (AMA) when airport surface departure metering procedures \n                     are in effect. \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute departureFleetPrioritization inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Attribute departureSlot inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Attribute earliestOffBlockTime inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    
    # Attribute standardInstrumentDeparture inherited from {http://www.fixm.aero/flight/3.0}FlightDepartureType
    _ElementMap.update({
        __runwayDepartureTime.name() : __runwayDepartureTime
    })
    _AttributeMap.update({
        __departureCenter.name() : __departureCenter,
        __departurePoint.name() : __departurePoint,
        __scheduledOffBlockTime.name() : __scheduledOffBlockTime,
        __targetMAEntryTime.name() : __targetMAEntryTime
    })
_module_typeBindings.NasDepartureType = NasDepartureType
Namespace.addCategoryObject('typeBinding', 'NasDepartureType', NasDepartureType)


# Complex type {http://www.faa.aero/nas/3.0}NasEnRouteType with content type ELEMENT_ONLY
class NasEnRouteType (_ImportedBinding__fx.EnRouteType):
    """
            Extension of core EnRoute to include additional NAS hold information. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasEnRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 302, 3)
    _ElementMap = _ImportedBinding__fx.EnRouteType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.EnRouteType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.EnRouteType
    
    # Element expectedFurtherClearanceTime uses Python identifier expectedFurtherClearanceTime
    __expectedFurtherClearanceTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'expectedFurtherClearanceTime'), 'expectedFurtherClearanceTime', '__httpwww_faa_aeronas3_0_NasEnRouteType_expectedFurtherClearanceTime', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 311, 15), )

    
    expectedFurtherClearanceTime = property(__expectedFurtherClearanceTime.value, __expectedFurtherClearanceTime.set, None, '\n                        .Hold Data Expect Further Clearance Time: The time the flight can expect further \n                        clearance at the specified hold fix. \n                     ')

    
    # Element alternateAerodrome (alternateAerodrome) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element beaconCodeAssignment (beaconCodeAssignment) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element boundaryCrossings (boundaryCrossings) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element cleared (cleared) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element controlElement (controlElement) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element cpdlcConnection (cpdlcConnection) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element pointout (pointout) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Element position (position) inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute fleetPrioritization inherited from {http://www.fixm.aero/flight/3.0}EnRouteType
    _ElementMap.update({
        __expectedFurtherClearanceTime.name() : __expectedFurtherClearanceTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasEnRouteType = NasEnRouteType
Namespace.addCategoryObject('typeBinding', 'NasEnRouteType', NasEnRouteType)


# Complex type {http://www.faa.aero/nas/3.0}NasFlightType with content type ELEMENT_ONLY
class NasFlightType (_ImportedBinding__fx.FlightType):
    """
            Extends core Flight object with NAS extra data 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasFlightType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 191, 3)
    _ElementMap = _ImportedBinding__fx.FlightType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.FlightType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.FlightType
    
    # Element assignedAltitude uses Python identifier assignedAltitude
    __assignedAltitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'assignedAltitude'), 'assignedAltitude', '__httpwww_faa_aeronas3_0_NasFlightType_assignedAltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 200, 15), )

    
    assignedAltitude = property(__assignedAltitude.value, __assignedAltitude.set, None, '\n                        .Assigned Altitude: The cruise altitude assigned to the active flight. \n                     ')

    
    # Element coordination uses Python identifier coordination
    __coordination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'coordination'), 'coordination', '__httpwww_faa_aeronas3_0_NasFlightType_coordination', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 207, 15), )

    
    coordination = property(__coordination.value, __coordination.set, None, '\n                        NAS extension to boundary crossing information: includes special handling for ccoordination \n                        time type. \n                     ')

    
    # Element flightIdentificationPrevious uses Python identifier flightIdentificationPrevious
    __flightIdentificationPrevious = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flightIdentificationPrevious'), 'flightIdentificationPrevious', '__httpwww_faa_aeronas3_0_NasFlightType_flightIdentificationPrevious', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 215, 15), )

    
    flightIdentificationPrevious = property(__flightIdentificationPrevious.value, __flightIdentificationPrevious.set, None, '\n                        The aircraft identification prior to a modification. \n                     ')

    
    # Element flightIntent uses Python identifier flightIntent
    __flightIntent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flightIntent'), 'flightIntent', '__httpwww_faa_aeronas3_0_NasFlightType_flightIntent', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 222, 15), )

    
    flightIntent = property(__flightIntent.value, __flightIntent.set, None, '\n                        .Flight Intent: A container for the list of intent values provided by the flight \n                        operator that designate the intentions of a flight prior to departure from an aerodrome \n                        or after arrival at an aerodrome. \n                     ')

    
    # Element flightPlan uses Python identifier flightPlan
    __flightPlan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flightPlan'), 'flightPlan', '__httpwww_faa_aeronas3_0_NasFlightType_flightPlan', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 231, 15), )

    
    flightPlan = property(__flightPlan.value, __flightPlan.set, None, '\n                        NAS Flight Plan Information \n                     ')

    
    # Element interimAltitude uses Python identifier interimAltitude
    __interimAltitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'interimAltitude'), 'interimAltitude', '__httpwww_faa_aeronas3_0_NasFlightType_interimAltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 238, 15), )

    
    interimAltitude = property(__interimAltitude.value, __interimAltitude.set, None, '\n                        .Interim Altitude Information: The altitude an aircraft is cleared to maintain different \n                        from that in the flight plan. \n                     ')

    
    # Element nasTmi uses Python identifier nasTmi
    __nasTmi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nasTmi'), 'nasTmi', '__httpwww_faa_aeronas3_0_NasFlightType_nasTmi', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 246, 15), )

    
    nasTmi = property(__nasTmi.value, __nasTmi.set, None, '\n                        NAS Traffic Management Initiative Information \n                     ')

    
    # Element requestedAirspeed uses Python identifier requestedAirspeed
    __requestedAirspeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'requestedAirspeed'), 'requestedAirspeed', '__httpwww_faa_aeronas3_0_NasFlightType_requestedAirspeed', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 253, 15), )

    
    requestedAirspeed = property(__requestedAirspeed.value, __requestedAirspeed.set, None, '\n                        .Classified Speed Indicator: The indication that the speed for this flight is classified \n                        and is not to be recorded. \n                     ')

    
    # Element requestedAltitude uses Python identifier requestedAltitude
    __requestedAltitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'requestedAltitude'), 'requestedAltitude', '__httpwww_faa_aeronas3_0_NasFlightType_requestedAltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 261, 15), )

    
    requestedAltitude = property(__requestedAltitude.value, __requestedAltitude.set, None, '\n                        .Requested Altitude: The cruise altitude filed or requested for the proposed flight. \n                        \n                     ')

    
    # Element agreed (agreed) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element aircraftDescription (aircraftDescription) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element arrival (arrival) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element controllingUnit (controllingUnit) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element dangerousGoods (dangerousGoods) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element departure (departure) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element emergency (emergency) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element enRoute (enRoute) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element enRouteDiversion (enRouteDiversion) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element extensions (extensions) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element flightIdentification (flightIdentification) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element flightStatus (flightStatus) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element gufi (gufi) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element negotiating (negotiating) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element operator (operator) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element originator (originator) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element radioCommunicationFailure (radioCommunicationFailure) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element rankedTrajectories (rankedTrajectories) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element routeToRevisedDestination (routeToRevisedDestination) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element specialHandling (specialHandling) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Element supplementalData (supplementalData) inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Attribute currentRVSMCompliance uses Python identifier currentRVSMCompliance
    __currentRVSMCompliance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currentRVSMCompliance'), 'currentRVSMCompliance', '__httpwww_faa_aeronas3_0_NasFlightType_currentRVSMCompliance', _module_typeBindings.RVSMFlightIndicatorType)
    __currentRVSMCompliance._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 270, 12)
    __currentRVSMCompliance._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 270, 12)
    
    currentRVSMCompliance = property(__currentRVSMCompliance.value, __currentRVSMCompliance.set, None, '\n                     .Current RVSM Flight Compliance: Indicates if the flight is currently Reduced Vertical \n                     Separation Minimum (RVSM) compliant in RVSM airspace, as determined by the Traffic \n                     Flow Management System. \n                  ')

    
    # Attribute futureRVSMCompliance uses Python identifier futureRVSMCompliance
    __futureRVSMCompliance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'futureRVSMCompliance'), 'futureRVSMCompliance', '__httpwww_faa_aeronas3_0_NasFlightType_futureRVSMCompliance', _module_typeBindings.RVSMFlightIndicatorType)
    __futureRVSMCompliance._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 279, 12)
    __futureRVSMCompliance._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 279, 12)
    
    futureRVSMCompliance = property(__futureRVSMCompliance.value, __futureRVSMCompliance.set, None, '\n                     .Future RVSM Flight Compliance: Indicates if the flight will beReduced Vertical Separation \n                     Minimum (RVSM) compliant when it reaches the RVSM airspace as determined by the Traffic \n                     Flow Management System (TFMS). \n                  ')

    
    # Attribute tfmsFlightClass uses Python identifier tfmsFlightClass
    __tfmsFlightClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tfmsFlightClass'), 'tfmsFlightClass', '__httpwww_faa_aeronas3_0_NasFlightType_tfmsFlightClass', _module_typeBindings.NasFlightClassType)
    __tfmsFlightClass._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 288, 12)
    __tfmsFlightClass._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 288, 12)
    
    tfmsFlightClass = property(__tfmsFlightClass.value, __tfmsFlightClass.set, None, '\n                     .Flight Class: Denotes the flight class of the aircraft which is determined by the \n                     aircraft call sign that is in the Aircraft Situation Display to Industry (ASDI) feed. \n                     \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute flightFiler inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Attribute flightType inherited from {http://www.fixm.aero/flight/3.0}FlightType
    
    # Attribute remarks inherited from {http://www.fixm.aero/flight/3.0}FlightType
    _ElementMap.update({
        __assignedAltitude.name() : __assignedAltitude,
        __coordination.name() : __coordination,
        __flightIdentificationPrevious.name() : __flightIdentificationPrevious,
        __flightIntent.name() : __flightIntent,
        __flightPlan.name() : __flightPlan,
        __interimAltitude.name() : __interimAltitude,
        __nasTmi.name() : __nasTmi,
        __requestedAirspeed.name() : __requestedAirspeed,
        __requestedAltitude.name() : __requestedAltitude
    })
    _AttributeMap.update({
        __currentRVSMCompliance.name() : __currentRVSMCompliance,
        __futureRVSMCompliance.name() : __futureRVSMCompliance,
        __tfmsFlightClass.name() : __tfmsFlightClass
    })
_module_typeBindings.NasFlightType = NasFlightType
Namespace.addCategoryObject('typeBinding', 'NasFlightType', NasFlightType)


# Complex type {http://www.faa.aero/nas/3.0}NasAircraftPositionType with content type ELEMENT_ONLY
class NasAircraftPositionType (_ImportedBinding__fx.AircraftPositionType):
    """
            Container for NAS target and track aircraft positions. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAircraftPositionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 75, 3)
    _ElementMap = _ImportedBinding__fx.AircraftPositionType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.AircraftPositionType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.AircraftPositionType
    
    # Element targetAltitude uses Python identifier targetAltitude
    __targetAltitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'targetAltitude'), 'targetAltitude', '__httpwww_faa_aeronas3_0_NasAircraftPositionType_targetAltitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 84, 15), )

    
    targetAltitude = property(__targetAltitude.value, __targetAltitude.set, None, '\n                        .Target Altitude: The Mode C target altitude, corrected for barometric pressure. \n                         Can be marked as invalid. \n                     ')

    
    # Element targetPosition uses Python identifier targetPosition
    __targetPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'targetPosition'), 'targetPosition', '__httpwww_faa_aeronas3_0_NasAircraftPositionType_targetPosition', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 92, 15), )

    
    targetPosition = property(__targetPosition.value, __targetPosition.set, None, '\n                        .Target Position: Aircraft target position, as reported by one raw radar return. \n                        \n                     ')

    
    # Element trackVelocity uses Python identifier trackVelocity
    __trackVelocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trackVelocity'), 'trackVelocity', '__httpwww_faa_aeronas3_0_NasAircraftPositionType_trackVelocity', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 100, 15), )

    
    trackVelocity = property(__trackVelocity.value, __trackVelocity.set, None, "\n                        Describes flight's velocity in X and Y axes \n         \n                        .Track Speed Components: Speed of the radar surveillance track along the X and Y \n                        components. \n                     ")

    
    # Element actualSpeed (actualSpeed) inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Element altitude (altitude) inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Element followingPosition (followingPosition) inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Element nextPosition (nextPosition) inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Element position (position) inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Element track (track) inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Attribute coastIndicator uses Python identifier coastIndicator
    __coastIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coastIndicator'), 'coastIndicator', '__httpwww_faa_aeronas3_0_NasAircraftPositionType_coastIndicator', _module_typeBindings.NasCoastIndicatorType)
    __coastIndicator._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 111, 12)
    __coastIndicator._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 111, 12)
    
    coastIndicator = property(__coastIndicator.value, __coastIndicator.set, None, '\n                     .Coast Indicator: An indicator the aircraft was unexpectedly not detected by radar \n                     (after a period of tracking). \n                  ')

    
    # Attribute targetPositionTime uses Python identifier targetPositionTime
    __targetPositionTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetPositionTime'), 'targetPositionTime', '__httpwww_faa_aeronas3_0_NasAircraftPositionType_targetPositionTime', _ImportedBinding__ff.TimeType)
    __targetPositionTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 119, 12)
    __targetPositionTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 119, 12)
    
    targetPositionTime = property(__targetPositionTime.value, __targetPositionTime.set, None, '\n                     .Target Position Time: The time associated with the raw radar return. \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute positionTime inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    
    # Attribute reportSource inherited from {http://www.fixm.aero/flight/3.0}AircraftPositionType
    _ElementMap.update({
        __targetAltitude.name() : __targetAltitude,
        __targetPosition.name() : __targetPosition,
        __trackVelocity.name() : __trackVelocity
    })
    _AttributeMap.update({
        __coastIndicator.name() : __coastIndicator,
        __targetPositionTime.name() : __targetPositionTime
    })
_module_typeBindings.NasAircraftPositionType = NasAircraftPositionType
Namespace.addCategoryObject('typeBinding', 'NasAircraftPositionType', NasAircraftPositionType)


# Complex type {http://www.faa.aero/nas/3.0}NasPositionAltitudeType with content type SIMPLE
class NasPositionAltitudeType (SimpleAltitudeType):
    """
            The Mode C target altitude, corrected for barometric pressure. 
            Suspected invalid altitudes marked with the 'invalid' attribute
            .Target Altitude: The Mode C target altitude, corrected for barometric pressure. 
             Can be marked as invalid. 
         """
    _TypeDefinition = _ImportedBinding__ff.UnitOfMeasureType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasPositionAltitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 143, 3)
    _ElementMap = SimpleAltitudeType._ElementMap.copy()
    _AttributeMap = SimpleAltitudeType._AttributeMap.copy()
    # Base type is SimpleAltitudeType
    
    # Attribute invalid uses Python identifier invalid
    __invalid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'invalid'), 'invalid', '__httpwww_faa_aeronas3_0_NasPositionAltitudeType_invalid', _module_typeBindings.InvalidIndicatorType)
    __invalid._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 154, 12)
    __invalid._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 154, 12)
    
    invalid = property(__invalid.value, __invalid.set, None, '\n                     Indicates whether target altitude is invalid. \n                  ')

    
    # Attribute ref inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    
    # Attribute uom inherited from {http://www.fixm.aero/foundation/3.0}AltitudeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __invalid.name() : __invalid
    })
_module_typeBindings.NasPositionAltitudeType = NasPositionAltitudeType
Namespace.addCategoryObject('typeBinding', 'NasPositionAltitudeType', NasPositionAltitudeType)


# Complex type {http://www.faa.aero/nas/3.0}NasAdaptedArrivalRouteType with content type ELEMENT_ONLY
class NasAdaptedArrivalRouteType (NasAdaptedRouteType):
    """
            Adapted Route Extension for Adapted Arrival Route 
            .Fixed Airspace Volume Number Containing First Adapted Arrival Route Fix: Contains 
            the uncombined Fixed Airspace Volume (FAV) number containing the first Adapted Arrival 
            Route (AAR) fix. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasAdaptedArrivalRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 64, 3)
    _ElementMap = NasAdaptedRouteType._ElementMap.copy()
    _AttributeMap = NasAdaptedRouteType._AttributeMap.copy()
    # Base type is NasAdaptedRouteType
    
    # Element nasFavNumber uses Python identifier nasFavNumber
    __nasFavNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nasFavNumber'), 'nasFavNumber', '__httpwww_faa_aeronas3_0_NasAdaptedArrivalRouteType_nasFavNumber', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 76, 15), )

    
    nasFavNumber = property(__nasFavNumber.value, __nasFavNumber.set, None, '\n                        .Fixed Airspace Volume Number Containing First Adapted Arrival Route Fix: Contains \n                        the uncombined Fixed Airspace Volume (FAV) number containing the first Adapted Arrival \n                        Route (AAR) fix. \n                     ')

    
    # Attribute nasRouteAlphanumeric inherited from {http://www.faa.aero/nas/3.0}NasAdaptedRouteType
    
    # Attribute nasRouteIdentifier inherited from {http://www.faa.aero/nas/3.0}NasAdaptedRouteType
    _ElementMap.update({
        __nasFavNumber.name() : __nasFavNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NasAdaptedArrivalRouteType = NasAdaptedArrivalRouteType
Namespace.addCategoryObject('typeBinding', 'NasAdaptedArrivalRouteType', NasAdaptedArrivalRouteType)


# Complex type {http://www.faa.aero/nas/3.0}NasRouteType with content type ELEMENT_ONLY
class NasRouteType (_ImportedBinding__fx.RouteType):
    """
            Extends the core route type to replace ICAO fields with equivalent NAS-specific elements. 
            
         
            .NAS Route: This element is the filed route. It only includes acknowledged auto routes. 
            Once the flight is active, this element shows the currently cleared route the airplane 
            will fly from the departure airport to the arrival airport. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasRouteType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 200, 3)
    _ElementMap = _ImportedBinding__fx.RouteType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.RouteType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.RouteType
    
    # Element adaptedArrivalDepartureRoute uses Python identifier adaptedArrivalDepartureRoute
    __adaptedArrivalDepartureRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adaptedArrivalDepartureRoute'), 'adaptedArrivalDepartureRoute', '__httpwww_faa_aeronas3_0_NasRouteType_adaptedArrivalDepartureRoute', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 214, 15), )

    
    adaptedArrivalDepartureRoute = property(__adaptedArrivalDepartureRoute.value, __adaptedArrivalDepartureRoute.set, None, '\n                        Container for Adapted Arrival Departure Route information. \n                     ')

    
    # Element adaptedDepartureRoute uses Python identifier adaptedDepartureRoute
    __adaptedDepartureRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adaptedDepartureRoute'), 'adaptedDepartureRoute', '__httpwww_faa_aeronas3_0_NasRouteType_adaptedDepartureRoute', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 221, 15), )

    
    adaptedDepartureRoute = property(__adaptedDepartureRoute.value, __adaptedDepartureRoute.set, None, '\n                        Container for Adapted Departure Route information. \n                     ')

    
    # Element holdFix uses Python identifier holdFix
    __holdFix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'holdFix'), 'holdFix', '__httpwww_faa_aeronas3_0_NasRouteType_holdFix', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 228, 15), )

    
    holdFix = property(__holdFix.value, __holdFix.set, None, '\n                        .Hold Data Fix: The location for the flight to Hold along the filed route of flight. \n                        \n                     ')

    
    # Element nasadaptedArrivalRoute uses Python identifier nasadaptedArrivalRoute
    __nasadaptedArrivalRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nasadaptedArrivalRoute'), 'nasadaptedArrivalRoute', '__httpwww_faa_aeronas3_0_NasRouteType_nasadaptedArrivalRoute', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 236, 15), )

    
    nasadaptedArrivalRoute = property(__nasadaptedArrivalRoute.value, __nasadaptedArrivalRoute.set, None, '\n                        Container for Adapted Arrival Route information. \n                     ')

    
    # Element climbSchedule (climbSchedule) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Element descentSchedule (descentSchedule) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Element estimatedElapsedTime (estimatedElapsedTime) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Element expandedRoute (expandedRoute) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Element initialCruisingSpeed (initialCruisingSpeed) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Element requestedAltitude (requestedAltitude) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Element segment (segment) inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Attribute atcIntendedRoute uses Python identifier atcIntendedRoute
    __atcIntendedRoute = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'atcIntendedRoute'), 'atcIntendedRoute', '__httpwww_faa_aeronas3_0_NasRouteType_atcIntendedRoute', _ImportedBinding__fb.FreeTextType)
    __atcIntendedRoute._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 244, 12)
    __atcIntendedRoute._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 244, 12)
    
    atcIntendedRoute = property(__atcIntendedRoute.value, __atcIntendedRoute.set, None, '\n                     .ATC Intended Route: The current cleared flight plan route with any unacknowledged \n                     auto routes (preferential routes, transition fixes and A-line fixes) already applied. \n                     \n                  ')

    
    # Attribute localIntendedRoute uses Python identifier localIntendedRoute
    __localIntendedRoute = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'localIntendedRoute'), 'localIntendedRoute', '__httpwww_faa_aeronas3_0_NasRouteType_localIntendedRoute', _ImportedBinding__fb.FreeTextType)
    __localIntendedRoute._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 253, 12)
    __localIntendedRoute._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 253, 12)
    
    localIntendedRoute = property(__localIntendedRoute.value, __localIntendedRoute.set, None, '\n                     .Local Intended Route: The flight plan route that is coordinated to penetrated facilities. \n                     It consists of the filed route (CMS field 10a) merged with any expected-to-be-applied-by-the-controlling-center \n                     Adapted Departure Routes (ADRs), Adapted Departure Arrival Routes (ADARs) or Adapted \n                     Arrival Routes (AARs) applied. \n                  ')

    
    # Attribute nasRouteText uses Python identifier nasRouteText
    __nasRouteText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nasRouteText'), 'nasRouteText', '__httpwww_faa_aeronas3_0_NasRouteType_nasRouteText', _module_typeBindings.STD_ANON_4)
    __nasRouteText._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 263, 12)
    __nasRouteText._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 263, 12)
    
    nasRouteText = property(__nasRouteText.value, __nasRouteText.set, None, '\n                     .Flight Plan Route: This element is the filed route. It only includes acknowledged \n                     auto routes. Once the flight is active, this element shows the currently cleared \n                     route the airplane will fly from the departure airport to the arrival airport. \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute airfileRouteStartTime inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Attribute flightDuration inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Attribute initialFlightRules inherited from {http://www.fixm.aero/flight/3.0}RouteType
    
    # Attribute routeText inherited from {http://www.fixm.aero/flight/3.0}RouteType
    _ElementMap.update({
        __adaptedArrivalDepartureRoute.name() : __adaptedArrivalDepartureRoute,
        __adaptedDepartureRoute.name() : __adaptedDepartureRoute,
        __holdFix.name() : __holdFix,
        __nasadaptedArrivalRoute.name() : __nasadaptedArrivalRoute
    })
    _AttributeMap.update({
        __atcIntendedRoute.name() : __atcIntendedRoute,
        __localIntendedRoute.name() : __localIntendedRoute,
        __nasRouteText.name() : __nasRouteText
    })
_module_typeBindings.NasRouteType = NasRouteType
Namespace.addCategoryObject('typeBinding', 'NasRouteType', NasRouteType)


# Complex type {http://www.faa.aero/nas/3.0}NasFlightStatusType with content type EMPTY
class NasFlightStatusType (_ImportedBinding__fx.FlightStatusType):
    """
            Extends core: Flight Status: Identifies the aspect of the flight life cycle. this 
            allows for NAS specific handling. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasFlightStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 61, 3)
    _ElementMap = _ImportedBinding__fx.FlightStatusType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.FlightStatusType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.FlightStatusType
    
    # Attribute fdpsFlightStatus uses Python identifier fdpsFlightStatus
    __fdpsFlightStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fdpsFlightStatus'), 'fdpsFlightStatus', '__httpwww_faa_aeronas3_0_NasFlightStatusType_fdpsFlightStatus', _module_typeBindings.SfdpsFlightStatusType)
    __fdpsFlightStatus._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 70, 12)
    __fdpsFlightStatus._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 70, 12)
    
    fdpsFlightStatus = property(__fdpsFlightStatus.value, __fdpsFlightStatus.set, None, '\n                     Represents the current status of the flight as specified by the SWIM SFDPS. \n                     .SFDPS Flight Status: Identification of the current aspect of the flight life cycle \n                     as determined by the SWIM Flight Data Publication Service (SFDPS). \n                  ')

    
    # Attribute tfmsStatus uses Python identifier tfmsStatus
    __tfmsStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tfmsStatus'), 'tfmsStatus', '__httpwww_faa_aeronas3_0_NasFlightStatusType_tfmsStatus', _module_typeBindings.TfmsFlightStatusType)
    __tfmsStatus._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 79, 12)
    __tfmsStatus._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 79, 12)
    
    tfmsStatus = property(__tfmsStatus.value, __tfmsStatus.set, None, '\n                     .Traffic Flow Management System Flight Status: Indicates the current status of the \n                     flight, as determined by Traffic Flow Management System (TFMS). \n                  ')

    
    # Attribute centre inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute source inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute system inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute timestamp inherited from {http://www.fixm.aero/base/3.0}FeatureType
    
    # Attribute accepted inherited from {http://www.fixm.aero/flight/3.0}FlightStatusType
    
    # Attribute airborneHold inherited from {http://www.fixm.aero/flight/3.0}FlightStatusType
    
    # Attribute airfile inherited from {http://www.fixm.aero/flight/3.0}FlightStatusType
    
    # Attribute flightCycle inherited from {http://www.fixm.aero/flight/3.0}FlightStatusType
    
    # Attribute missedApproach inherited from {http://www.fixm.aero/flight/3.0}FlightStatusType
    
    # Attribute suspended inherited from {http://www.fixm.aero/flight/3.0}FlightStatusType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fdpsFlightStatus.name() : __fdpsFlightStatus,
        __tfmsStatus.name() : __tfmsStatus
    })
_module_typeBindings.NasFlightStatusType = NasFlightStatusType
Namespace.addCategoryObject('typeBinding', 'NasFlightStatusType', NasFlightStatusType)


# Complex type {http://www.faa.aero/nas/3.0}NasTrajectoryOptionType with content type ELEMENT_ONLY
class NasTrajectoryOptionType (_ImportedBinding__fx.RankedTrajectoryType):
    """
            .Traffic Flow Management Collaborative Trajectory Options Program Information: A 
            container for a Traffic Flow Management Collaborative Trajectory Options Program 
            pertinent information for a flight. 
            .Trajectory Option Set: A container for information pertinent to a single trajectory 
            option for a flight. 
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NasTrajectoryOptionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 105, 3)
    _ElementMap = _ImportedBinding__fx.RankedTrajectoryType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__fx.RankedTrajectoryType._AttributeMap.copy()
    # Base type is _ImportedBinding__fx.RankedTrajectoryType
    
    # Element constrainedAirspaceEntry uses Python identifier constrainedAirspaceEntry
    __constrainedAirspaceEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constrainedAirspaceEntry'), 'constrainedAirspaceEntry', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_constrainedAirspaceEntry', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 118, 15), )

    
    constrainedAirspaceEntry = property(__constrainedAirspaceEntry.value, __constrainedAirspaceEntry.set, None, '\n                        Container for NAS Trajectory Option Constraints. \n                     ')

    
    # Element routeTrajectoryPair (routeTrajectoryPair) inherited from {http://www.fixm.aero/flight/3.0}RankedTrajectoryType
    
    # Attribute ctopIdentifier uses Python identifier ctopIdentifier
    __ctopIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ctopIdentifier'), 'ctopIdentifier', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_ctopIdentifier', _module_typeBindings.STD_ANON_9)
    __ctopIdentifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 126, 12)
    __ctopIdentifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 126, 12)
    
    ctopIdentifier = property(__ctopIdentifier.value, __ctopIdentifier.set, None, '\n                     .Collaborative Trajectory Options Program Name: The name for the Collaborative Trajectory \n                     Options Program as defined by the traffic manager. \n                     .Collaborative Trajectory Options Program Identifier: The Traffic Flow Management \n                     System generated unique identifier for the Collaborative Trajectory Options Program. \n                     \n                  ')

    
    # Attribute ctopName uses Python identifier ctopName
    __ctopName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ctopName'), 'ctopName', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_ctopName', _module_typeBindings.STD_ANON_10)
    __ctopName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 142, 12)
    __ctopName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 142, 12)
    
    ctopName = property(__ctopName.value, __ctopName.set, None, '\n                     .Collaborative Trajectory Options Program Name: The name for the Collaborative Trajectory \n                     Options Program as defined by the traffic manager. \n                     .Collaborative Trajectory Options Program Identifier: The Traffic Flow Management \n                     System generated unique identifier for the Collaborative Trajectory Options Program. \n                     \n                  ')

    
    # Attribute manualOverride uses Python identifier manualOverride
    __manualOverride = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'manualOverride'), 'manualOverride', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_manualOverride', _module_typeBindings.ManualOverrideIndicatorType)
    __manualOverride._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 159, 12)
    __manualOverride._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 159, 12)
    
    manualOverride = property(__manualOverride.value, __manualOverride.set, None, '\n                     .Trajectory Manual Override Status: An indication whether a trajectory was either \n                     selected manually by a traffic manager from the available trajectory options or was \n                     entered manually by a traffic manager. \n                  ')

    
    # Attribute minimumNotificationMinutes uses Python identifier minimumNotificationMinutes
    __minimumNotificationMinutes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minimumNotificationMinutes'), 'minimumNotificationMinutes', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_minimumNotificationMinutes', _ImportedBinding__fb.CountType)
    __minimumNotificationMinutes._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 168, 12)
    __minimumNotificationMinutes._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 168, 12)
    
    minimumNotificationMinutes = property(__minimumNotificationMinutes.value, __minimumNotificationMinutes.set, None, '\n                     .Trajectory Minimum Notification Time: The minimum notification time, relative to \n                     off block departure time, the airspace user needs for a trajectory option to be assigned. \n                     \n                  ')

    
    # Attribute relativeCost uses Python identifier relativeCost
    __relativeCost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'relativeCost'), 'relativeCost', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_relativeCost', _ImportedBinding__fb.CountType)
    __relativeCost._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 177, 12)
    __relativeCost._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 177, 12)
    
    relativeCost = property(__relativeCost.value, __relativeCost.set, None, '\n                     .Trajectory Relative Cost: The relative cost of the trajectory option as compared \n                     to another trajectory option. \n                  ')

    
    # Attribute totalCost uses Python identifier totalCost
    __totalCost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'totalCost'), 'totalCost', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_totalCost', _ImportedBinding__fb.CountType)
    __totalCost._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 185, 12)
    __totalCost._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 185, 12)
    
    totalCost = property(__totalCost.value, __totalCost.set, None, '\n                     .Trajectory Total Cost: The total cost the flight would incur if this were the assigned \n                     trajectory option. It includes the Trajectory Relative Cost and the Traffic Flow \n                     Management assigned delay for this trajectory option. \n                  ')

    
    # Attribute validEndTime uses Python identifier validEndTime
    __validEndTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'validEndTime'), 'validEndTime', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_validEndTime', _ImportedBinding__ff.TimeType)
    __validEndTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 194, 12)
    __validEndTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 194, 12)
    
    validEndTime = property(__validEndTime.value, __validEndTime.set, None, '\n                     .Trajectory Valid End Time: The latest runway departure time for which this trajectory \n                     can be used by this flight. \n                  ')

    
    # Attribute validStartTime uses Python identifier validStartTime
    __validStartTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'validStartTime'), 'validStartTime', '__httpwww_faa_aeronas3_0_NasTrajectoryOptionType_validStartTime', _ImportedBinding__ff.TimeType)
    __validStartTime._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 202, 12)
    __validStartTime._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 202, 12)
    
    validStartTime = property(__validStartTime.value, __validStartTime.set, None, '\n                     .Trajectory Valid Start Time: The earliest runway departure time for which this trajectory \n                     can be used by this flight. \n                  ')

    
    # Attribute assignedIndicator inherited from {http://www.fixm.aero/flight/3.0}RankedTrajectoryType
    
    # Attribute identifier inherited from {http://www.fixm.aero/flight/3.0}RankedTrajectoryType
    
    # Attribute maximumAcceptableDelay inherited from {http://www.fixm.aero/flight/3.0}RankedTrajectoryType
    _ElementMap.update({
        __constrainedAirspaceEntry.name() : __constrainedAirspaceEntry
    })
    _AttributeMap.update({
        __ctopIdentifier.name() : __ctopIdentifier,
        __ctopName.name() : __ctopName,
        __manualOverride.name() : __manualOverride,
        __minimumNotificationMinutes.name() : __minimumNotificationMinutes,
        __relativeCost.name() : __relativeCost,
        __totalCost.name() : __totalCost,
        __validEndTime.name() : __validEndTime,
        __validStartTime.name() : __validStartTime
    })
_module_typeBindings.NasTrajectoryOptionType = NasTrajectoryOptionType
Namespace.addCategoryObject('typeBinding', 'NasTrajectoryOptionType', NasTrajectoryOptionType)


NasPerformanceBasedAccuracy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasPerformanceBasedAccuracy'), NasPerformanceBasedAccuracyType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 338, 3))
Namespace.addCategoryObject('elementBinding', NasPerformanceBasedAccuracy.name().localName(), NasPerformanceBasedAccuracy)

AltFixAltAltitude = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltFixAltAltitude'), AltFixAltAltitudeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 104, 3))
Namespace.addCategoryObject('elementBinding', AltFixAltAltitude.name().localName(), AltFixAltAltitude)

BlockAltitude = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BlockAltitude'), BlockAltitudeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 130, 3))
Namespace.addCategoryObject('elementBinding', BlockAltitude.name().localName(), BlockAltitude)

NasAltitude = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAltitude'), NasAltitudeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 199, 3))
Namespace.addCategoryObject('elementBinding', NasAltitude.name().localName(), NasAltitude)

VfrAltitude = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VfrAltitude'), VfrAltitudeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 219, 3))
Namespace.addCategoryObject('elementBinding', VfrAltitude.name().localName(), VfrAltitude)

VfrOnTopAltitude = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VfrOnTopAltitude'), VfrOnTopAltitudeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 228, 3))
Namespace.addCategoryObject('elementBinding', VfrOnTopAltitude.name().localName(), VfrOnTopAltitude)

RunwayAcceptableSlotSubstitution = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunwayAcceptableSlotSubstitution'), RunwayAcceptableSlotSubstitutionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 182, 3))
Namespace.addCategoryObject('elementBinding', RunwayAcceptableSlotSubstitution.name().localName(), RunwayAcceptableSlotSubstitution)

RunwayArrivalTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunwayArrivalTime'), RunwayArrivalTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 253, 3))
Namespace.addCategoryObject('elementBinding', RunwayArrivalTime.name().localName(), RunwayArrivalTime)

RunwayDepartureTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunwayDepartureTime'), RunwayDepartureTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 182, 3))
Namespace.addCategoryObject('elementBinding', RunwayDepartureTime.name().localName(), RunwayDepartureTime)

AirspaceAcceptableSlotSubstitution = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AirspaceAcceptableSlotSubstitution'), AirspaceAcceptableSlotSubstitutionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 100, 3))
Namespace.addCategoryObject('elementBinding', AirspaceAcceptableSlotSubstitution.name().localName(), AirspaceAcceptableSlotSubstitution)

AirspaceEntryTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AirspaceEntryTime'), AirspaceEntryTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 171, 3))
Namespace.addCategoryObject('elementBinding', AirspaceEntryTime.name().localName(), AirspaceEntryTime)

AirspaceExitTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AirspaceExitTime'), AirspaceExitTimeType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 195, 3))
Namespace.addCategoryObject('elementBinding', AirspaceExitTime.name().localName(), AirspaceExitTime)

NasAirspeedChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAirspeedChoice'), NasAirspeedChoiceType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 137, 3))
Namespace.addCategoryObject('elementBinding', NasAirspeedChoice.name().localName(), NasAirspeedChoice)

AbstractMessage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractMessage'), AbstractMessageType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 87, 3))
Namespace.addCategoryObject('elementBinding', AbstractMessage.name().localName(), AbstractMessage)

MessageCollection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MessageCollection'), MessageCollectionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 155, 3))
Namespace.addCategoryObject('elementBinding', MessageCollection.name().localName(), MessageCollection)

NasVelocity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasVelocity'), NasVelocityType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 191, 3))
Namespace.addCategoryObject('elementBinding', NasVelocity.name().localName(), NasVelocity)

RouteImpactList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RouteImpactList'), RouteImpactListType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 393, 3))
Namespace.addCategoryObject('elementBinding', RouteImpactList.name().localName(), RouteImpactList)

NasTmi = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasTmi'), NasTmiType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 285, 3))
Namespace.addCategoryObject('elementBinding', NasTmi.name().localName(), NasTmi)

NasHandoff = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasHandoff'), NasHandoffType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 92, 3))
Namespace.addCategoryObject('elementBinding', NasHandoff.name().localName(), NasHandoff)

NasClearedFlightInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasClearedFlightInformation'), NasClearedFlightInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 300, 3))
Namespace.addCategoryObject('elementBinding', NasClearedFlightInformation.name().localName(), NasClearedFlightInformation)

NasCoordination = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasCoordination'), NasCoordinationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 189, 3))
Namespace.addCategoryObject('elementBinding', NasCoordination.name().localName(), NasCoordination)

ArrivalMovementAreaHoldInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArrivalMovementAreaHoldInformation'), ArrivalMovementAreaHoldInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 97, 3))
Namespace.addCategoryObject('elementBinding', ArrivalMovementAreaHoldInformation.name().localName(), ArrivalMovementAreaHoldInformation)

DeicingInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DeicingInformation'), DeicingInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 122, 3))
Namespace.addCategoryObject('elementBinding', DeicingInformation.name().localName(), DeicingInformation)

DepartureMovementAreaHoldInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DepartureMovementAreaHoldInformation'), DepartureMovementAreaHoldInformationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 184, 3))
Namespace.addCategoryObject('elementBinding', DepartureMovementAreaHoldInformation.name().localName(), DepartureMovementAreaHoldInformation)

FlightIntent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightIntent'), FlightIntentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 257, 3))
Namespace.addCategoryObject('elementBinding', FlightIntent.name().localName(), FlightIntent)

FeatureMessage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FeatureMessage'), FeatureMessageType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 111, 3))
Namespace.addCategoryObject('elementBinding', FeatureMessage.name().localName(), FeatureMessage)

FlightMessage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlightMessage'), FlightMessageType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 133, 3))
Namespace.addCategoryObject('elementBinding', FlightMessage.name().localName(), FlightMessage)

MessageMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MessageMetadata'), MessageMetadataType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 201, 3))
Namespace.addCategoryObject('elementBinding', MessageMetadata.name().localName(), MessageMetadata)

NasExpandedRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasExpandedRoute'), NasExpandedRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 166, 3))
Namespace.addCategoryObject('elementBinding', NasExpandedRoute.name().localName(), NasExpandedRoute)

NasAdvisory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAdvisory'), NasAdvisoryType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 173, 3))
Namespace.addCategoryObject('elementBinding', NasAdvisory.name().localName(), NasAdvisory)

ConstrainedAirspaceEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConstrainedAirspaceEntry'), ConstrainedAirspaceEntryType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 90, 3))
Namespace.addCategoryObject('elementBinding', ConstrainedAirspaceEntry.name().localName(), ConstrainedAirspaceEntry)

NasAirspaceConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAirspaceConstraint'), NasAirspaceConstraintType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 261, 3))
Namespace.addCategoryObject('elementBinding', NasAirspaceConstraint.name().localName(), NasAirspaceConstraint)

NasFlightIdentification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasFlightIdentification'), NasFlightIdentificationType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 378, 3))
Namespace.addCategoryObject('elementBinding', NasFlightIdentification.name().localName(), NasFlightIdentification)

NasSupplementalData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasSupplementalData'), NasSupplementalDataType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 404, 3))
Namespace.addCategoryObject('elementBinding', NasSupplementalData.name().localName(), NasSupplementalData)

NasFlightPlan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasFlightPlan'), NasFlightPlanType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightPlan.xsd', 89, 3))
Namespace.addCategoryObject('elementBinding', NasFlightPlan.name().localName(), NasFlightPlan)

NasAdaptedRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAdaptedRoute'), NasAdaptedRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 138, 3))
Namespace.addCategoryObject('elementBinding', NasAdaptedRoute.name().localName(), NasAdaptedRoute)

NasRoutePoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasRoutePoint'), NasRoutePointType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 301, 3))
Namespace.addCategoryObject('elementBinding', NasRoutePoint.name().localName(), NasRoutePoint)

NasRouteSegment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasRouteSegment'), NasRouteSegmentType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 335, 3))
Namespace.addCategoryObject('elementBinding', NasRouteSegment.name().localName(), NasRouteSegment)

NasReroute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasReroute'), NasRerouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 254, 3))
Namespace.addCategoryObject('elementBinding', NasReroute.name().localName(), NasReroute)

NasAircraft = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAircraft'), NasAircraftType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 311, 3))
Namespace.addCategoryObject('elementBinding', NasAircraft.name().localName(), NasAircraft)

NasArrival = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasArrival'), NasArrivalType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 142, 3))
Namespace.addCategoryObject('elementBinding', NasArrival.name().localName(), NasArrival)

NasUnitBoundary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasUnitBoundary'), NasUnitBoundaryType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 135, 3))
Namespace.addCategoryObject('elementBinding', NasUnitBoundary.name().localName(), NasUnitBoundary)

NasDeparture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasDeparture'), NasDepartureType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 122, 3))
Namespace.addCategoryObject('elementBinding', NasDeparture.name().localName(), NasDeparture)

NasEnRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasEnRoute'), NasEnRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 323, 3))
Namespace.addCategoryObject('elementBinding', NasEnRoute.name().localName(), NasEnRoute)

NasFlight = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasFlight'), NasFlightType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 300, 3))
Namespace.addCategoryObject('elementBinding', NasFlight.name().localName(), NasFlight)

NasAircraftPosition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAircraftPosition'), NasAircraftPositionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 129, 3))
Namespace.addCategoryObject('elementBinding', NasAircraftPosition.name().localName(), NasAircraftPosition)

NasAdaptedArrivalRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasAdaptedArrivalRoute'), NasAdaptedArrivalRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 92, 3))
Namespace.addCategoryObject('elementBinding', NasAdaptedArrivalRoute.name().localName(), NasAdaptedArrivalRoute)

NasRoute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasRoute'), NasRouteType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 280, 3))
Namespace.addCategoryObject('elementBinding', NasRoute.name().localName(), NasRoute)

NasFlightStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasFlightStatus'), NasFlightStatusType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasStatus.xsd', 90, 3))
Namespace.addCategoryObject('elementBinding', NasFlightStatus.name().localName(), NasFlightStatus)

NasTrajectoryOption = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NasTrajectoryOption'), NasTrajectoryOptionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 213, 3))
Namespace.addCategoryObject('elementBinding', NasTrajectoryOption.name().localName(), NasTrajectoryOption)



NasPerformanceBasedAccuracyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cmsFieldType'), CmsAccuracyType, scope=NasPerformanceBasedAccuracyType, documentation="\n                  .Performance-Based Navigation Accuracy: This is the flight's navigation accuracy \n                  value for the phase of flight, specified in the Performance-Based Navigation Phase. \n                  \n               ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 327, 9)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 327, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasPerformanceBasedAccuracyType._UseForTag(pyxb.namespace.ExpandedName(None, 'cmsFieldType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 327, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasPerformanceBasedAccuracyType._Automaton = _BuildAutomaton()




AltFixAltAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), _ImportedBinding__fb.SignificantPointType, scope=AltFixAltAltitudeType, documentation='\n                  Fix associated with the altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 81, 9)))

AltFixAltAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'post'), _ImportedBinding__ff.AltitudeType, scope=AltFixAltAltitudeType, documentation='\n                  Altitude post the specified fix. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 88, 9)))

AltFixAltAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pre'), _ImportedBinding__ff.AltitudeType, scope=AltFixAltAltitudeType, documentation='\n                  Altitude pre specified fix. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 95, 9)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 81, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 88, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 95, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AltFixAltAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 81, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AltFixAltAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'post')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 88, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AltFixAltAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'pre')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 95, 9))
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
AltFixAltAltitudeType._Automaton = _BuildAutomaton_()




BlockAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'above'), _ImportedBinding__ff.AltitudeType, scope=BlockAltitudeType, documentation='\n                  Lower range of the block altitude. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 114, 9)))

BlockAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'below'), _ImportedBinding__ff.AltitudeType, scope=BlockAltitudeType, documentation='\n                  Upper range of the block altitude. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 121, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 114, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 121, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BlockAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'above')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 114, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BlockAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'below')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 121, 9))
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
BlockAltitudeType._Automaton = _BuildAutomaton_2()




NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'above'), AboveAltitudeType, scope=NasAltitudeType, documentation='\n                  aircraft operating above a specified altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 140, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'altFixAlt'), AltFixAltAltitudeType, scope=NasAltitudeType, documentation='\n                  Alt-fix-alt altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 147, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'block'), BlockAltitudeType, scope=NasAltitudeType, documentation='\n                  Altitude indicates that aircraft is operating  above and below the specified altitudes. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 154, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'simple'), SimpleAltitudeType, scope=NasAltitudeType, documentation='\n                  The only NAS altitude that maps directly to the core ICAO altitude types. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 162, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vfr'), VfrAltitudeType, scope=NasAltitudeType, documentation='\n                  vfr altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 169, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vfrOnTop'), VfrOnTopAltitudeType, scope=NasAltitudeType, documentation='\n                  vfr-on-top altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 176, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vfrOnTopPlus'), VfrOnTopPlusAltitudeType, scope=NasAltitudeType, documentation='\n                  vfr-on-top with altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 183, 9)))

NasAltitudeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vfrPlus'), VfrPlusAltitudeType, scope=NasAltitudeType, documentation='\n                  vfr plus altitude \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 190, 9)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 140, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 147, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 154, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 162, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 169, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 176, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 183, 9))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 190, 9))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'above')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 140, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'altFixAlt')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 147, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'block')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 154, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'simple')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 162, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'vfr')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 169, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'vfrOnTop')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 176, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'vfrOnTopPlus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 183, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasAltitudeType._UseForTag(pyxb.namespace.ExpandedName(None, 'vfrPlus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAltitude.xsd', 190, 9))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasAltitudeType._Automaton = _BuildAutomaton_3()




RunwayAcceptableSlotSubstitutionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'earliest'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayAcceptableSlotSubstitutionType, documentation='\n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 156, 9)))

RunwayAcceptableSlotSubstitutionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'latest'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayAcceptableSlotSubstitutionType, documentation='\n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 168, 9)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 156, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 168, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RunwayAcceptableSlotSubstitutionType._UseForTag(pyxb.namespace.ExpandedName(None, 'earliest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 156, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RunwayAcceptableSlotSubstitutionType._UseForTag(pyxb.namespace.ExpandedName(None, 'latest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 168, 9))
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
RunwayAcceptableSlotSubstitutionType._Automaton = _BuildAutomaton_4()




RunwayArrivalTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airlineEstimated'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayArrivalTimeType, documentation='\n                  .Runway Arrival Time - Airspace User Estimated: The estimated time of runway arrival, \n                  as provided by the Airspace User. \n                  .Runway Departure Time - Airspace User Estimated: The estimated time of runway departure, \n                  as provided by the Airspace User. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 191, 9)))

RunwayArrivalTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'earliest'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayArrivalTimeType, documentation='\n                  .Runway Arrival Time - Earliest: The earliest acceptable arrival time provided by \n                  the Airspace user for a flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 201, 9)))

RunwayArrivalTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'original'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayArrivalTimeType, documentation='\n                  .Runway Arrival Time - Original: The last Runway Arrival Time - Traffic Flow Management \n                  System Estimated modeled by TFMS before either a Traffic Management Initiative (TMI) \n                  is issued, or the flight departs, or the flight is  time-out  delayed by TFMS. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 209, 9)))

RunwayArrivalTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'preferred'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayArrivalTimeType, documentation='\n                  .Runway Arrival Time - Preferred: A runway arrival time which, when considered in \n                  aggregate with other flights for that Airspace User, indicates the preferred arrival \n                  sequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 218, 9)))

RunwayArrivalTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'slotSubstitution'), RunwayAcceptableSlotSubstitutionType, scope=RunwayArrivalTimeType, documentation='\n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 227, 9)))

RunwayArrivalTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tfmsEstimated'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayArrivalTimeType, documentation='\n                  .Runway Departure Time - Traffic Flow Management System Estimated: The estimated \n                  runway departure time considering all data sources, as determined by Traffic Flow \n                  Management System (TFMS). \n                  .Runway Arrival Time - Traffic Flow Management System Estimated: The estimated runway \n                  arrival time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 239, 9)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 191, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 201, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 209, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 218, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 227, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 239, 9))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RunwayArrivalTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'airlineEstimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 191, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RunwayArrivalTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'earliest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 201, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RunwayArrivalTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'original')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 209, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RunwayArrivalTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'preferred')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 218, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RunwayArrivalTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'slotSubstitution')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 227, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RunwayArrivalTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'tfmsEstimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 239, 9))
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
RunwayArrivalTimeType._Automaton = _BuildAutomaton_5()




RunwayDepartureTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'airlineEstimated'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayDepartureTimeType, documentation='\n                  .Runway Arrival Time - Airspace User Estimated: The estimated time of runway arrival, \n                  as provided by the Airspace User. \n                  .Runway Departure Time - Airspace User Estimated: The estimated time of runway departure, \n                  as provided by the Airspace User. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 131, 9)))

RunwayDepartureTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'earliest'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayDepartureTimeType, documentation='\n                  .Runway Departure Time - Earliest: Earliest acceptable runway departure time (wheels-off \n                  time) an Airspace user provides for a flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 141, 9)))

RunwayDepartureTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'original'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayDepartureTimeType, documentation='\n                  .Runway Departure Time - Original: The last Runway Departure Time - Traffic Flow \n                  Management System Estimated modeled by TFMS before either a Traffic Management Initiative \n                  (TMI) is issued, or the flight departs, or the flight is  time-out  delayed by TFMS. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 149, 9)))

RunwayDepartureTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'preferred'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayDepartureTimeType, documentation='\n                  .Runway Departure Time - Preferred: A runway departure time which, when considered \n                  in aggregate with other flights for that Airspace User, indicates the preferred departure \n                  sequence. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 159, 9)))

RunwayDepartureTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tfmEstimated'), _ImportedBinding__fb.ReportedTimeType, scope=RunwayDepartureTimeType, documentation='\n                  .Runway Departure Time - Traffic Flow Management System Estimated: The estimated \n                  runway departure time considering all data sources, as determined by Traffic Flow \n                  Management System (TFMS). \n                  .Runway Arrival Time - Traffic Flow Management System Estimated: The estimated runway \n                  arrival time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 168, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 131, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 141, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 149, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 159, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 168, 9))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RunwayDepartureTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'airlineEstimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 131, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RunwayDepartureTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'earliest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 141, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RunwayDepartureTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'original')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 149, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RunwayDepartureTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'preferred')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 159, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RunwayDepartureTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'tfmEstimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 168, 9))
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
RunwayDepartureTimeType._Automaton = _BuildAutomaton_6()




AirspaceAcceptableSlotSubstitutionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'earliest'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceAcceptableSlotSubstitutionType, documentation='\n                  .Airspace Entry Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP), in return for a yielded slot. \n                  .Airspace Entry Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP) in return for a yielded slot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 74, 9)))

AirspaceAcceptableSlotSubstitutionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'latest'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceAcceptableSlotSubstitutionType, documentation='\n                  .Airspace Entry Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP), in return for a yielded slot. \n                  .Airspace Entry Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP) in return for a yielded slot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 86, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 74, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 86, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceAcceptableSlotSubstitutionType._UseForTag(pyxb.namespace.ExpandedName(None, 'earliest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 74, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceAcceptableSlotSubstitutionType._UseForTag(pyxb.namespace.ExpandedName(None, 'latest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 86, 9))
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
AirspaceAcceptableSlotSubstitutionType._Automaton = _BuildAutomaton_7()




AirspaceEntryTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'earliest'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceEntryTimeType, documentation='\n                  .Airspace Entry Time - Earliest: The earliest time the flight could enter the constrained \n                  airspace. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 113, 9)))

AirspaceEntryTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'initial'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceEntryTimeType, documentation='\n                  .Airspace Entry Time - Initial: The date and time at which a flight was originally \n                  planning to enter into the airspace. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 121, 9)))

AirspaceEntryTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'original'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceEntryTimeType, documentation='\n                  .Airspace Entry Time - Original: The last Airspace Entry Time - Traffic Flow Management \n                  System Estimated modeled by the Traffic Flow Management System (TFMS) before either \n                  a Traffic Management Initiative is issued, or the flight departs, or the flight is \n                   time-out  delayed by TFMS. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 129, 9)))

AirspaceEntryTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'slotSubstitution'), AirspaceAcceptableSlotSubstitutionType, scope=AirspaceEntryTimeType, documentation='\n                  .Airspace Entry Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP), in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP) in return for a yielded slot. \n                  .Runway Arrival Time - Slot Credit Substitution Latest Acceptable: The latest time \n                  at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Ground Delay Program (GDP), in return for a yielded slot. \n                  .Airspace Entry Time - Slot Credit Substitution Earliest Acceptable: The earliest \n                  time at which the Airspace user will accept a slot in a Traffic Management Initiative \n                  (TMI) Airspace Flow Program (AFP) in return for a yielded slot. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 139, 9)))

AirspaceEntryTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tfmsEstimated'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceEntryTimeType, documentation='\n                  .Airspace Exit Time - Traffic Flow Management System Estimated: The estimated airspace \n                  exit time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n                  .Airspace Entry Time - Traffic Flow Management System Estimated: The estimated airspace \n                  entry time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 157, 9)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 113, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 121, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 129, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 139, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 157, 9))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceEntryTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'earliest')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 113, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceEntryTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'initial')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 121, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceEntryTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'original')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 129, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceEntryTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'slotSubstitution')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 139, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceEntryTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'tfmsEstimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 157, 9))
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
AirspaceEntryTimeType._Automaton = _BuildAutomaton_8()




AirspaceExitTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tfmsEstimated'), _ImportedBinding__fb.ReportedTimeType, scope=AirspaceExitTimeType, documentation='\n                  .Airspace Exit Time - Traffic Flow Management System Estimated: The estimated airspace \n                  exit time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n                  .Airspace Entry Time - Traffic Flow Management System Estimated: The estimated airspace \n                  entry time considering all data sources, as determined by Traffic Flow Management \n                  System (TFMS). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 181, 9)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 181, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AirspaceExitTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'tfmsEstimated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 181, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AirspaceExitTimeType._Automaton = _BuildAutomaton_9()




NasAirspeedChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'classified'), ClassifiedSpeedIndicatorType, scope=NasAirspeedChoiceType, documentation='\n                  Container for the Classified Speed Indicator. \n                  .Classified Speed Indicator: The indication that the speed for this flight is classified \n                  and is not to be recorded. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 119, 9)))

NasAirspeedChoiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nasAirspeed'), _ImportedBinding__ff.TrueAirspeedOrMachType, scope=NasAirspeedChoiceType, documentation='\n                  Represents the aircraft speed expressed in either true airspeed or mach. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 128, 9)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 119, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 128, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasAirspeedChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'classified')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 119, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasAirspeedChoiceType._UseForTag(pyxb.namespace.ExpandedName(None, 'nasAirspeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 128, 9))
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
NasAirspeedChoiceType._Automaton = _BuildAutomaton_10()




AbstractMessageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), MessageMetadataType, scope=AbstractMessageType, documentation='\n                  The MessageMetadata provides a unique message identifier, the origin of the message \n                  in time and location, \n                the system\n                that produced the message, and the time span over which the message data is valid.\n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractMessageType._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractMessageType._Automaton = _BuildAutomaton_11()




MessageCollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'message'), AbstractMessageType, scope=MessageCollectionType, documentation='\n                  The MessageCollection type is a mechanism for aggregating messages to be transmitted \n                  as a group. This is useful \n                both to aggregate messages about one flight, and to pack many messages together for transmission efficiency.\n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 144, 9)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MessageCollectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'message')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 144, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MessageCollectionType._Automaton = _BuildAutomaton_12()




NasVelocityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x'), _ImportedBinding__ff.AirspeedInIasOrMachType, scope=NasVelocityType, documentation='\n                  speed along the X-axis \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 175, 9)))

NasVelocityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y'), _ImportedBinding__ff.AirspeedInIasOrMachType, scope=NasVelocityType, documentation='\n                  speed along the Y-axis \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 182, 9)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 175, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 182, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasVelocityType._UseForTag(pyxb.namespace.ExpandedName(None, 'x')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 175, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasVelocityType._UseForTag(pyxb.namespace.ExpandedName(None, 'y')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 182, 9))
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
NasVelocityType._Automaton = _BuildAutomaton_13()




RouteImpactListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedAirway'), STD_ANON_5, scope=RouteImpactListType, documentation='\n                  .Predicted Airways: Current prediction of the airways along the trajectory of a flight. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 346, 9)))

RouteImpactListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedFix'), _ImportedBinding__fb.SignificantPointType, scope=RouteImpactListType, documentation='\n                  .Predicted Fixes: Current prediction of fixes along the trajectory of a flight, where \n                  these predictions are based on all the information available to the Traffic Flow \n                  Management System (TFMS). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 357, 9)))

RouteImpactListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedSector'), _ImportedBinding__ff.UnitSectorAirspaceType, scope=RouteImpactListType, documentation='\n                  .Predicted Sectors: Current prediction of the sectors along the trajectory of a flight. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 366, 9)))

RouteImpactListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedUnit'), _ImportedBinding__ff.UnitSectorAirspaceType, scope=RouteImpactListType, documentation='\n                  .Predicted Units: Current prediction of the en route Air Traffic Control units (centres) \n                  along the trajectory of a flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 374, 9)))

RouteImpactListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'predictedWaypoint'), _ImportedBinding__fb.SignificantPointType, scope=RouteImpactListType, documentation='\n                  .Predicted Waypoints: Current prediction of the waypoints of the trajectory for a \n                  flight, where these predictions are based on all the information available to the \n                  Traffic Flow Management System (TFMS). \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 382, 9)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 346, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 357, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 366, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 374, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 382, 9))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RouteImpactListType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedAirway')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 346, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RouteImpactListType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 357, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RouteImpactListType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedSector')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 366, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RouteImpactListType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 374, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RouteImpactListType._UseForTag(pyxb.namespace.ExpandedName(None, 'predictedWaypoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 382, 9))
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
RouteImpactListType._Automaton = _BuildAutomaton_14()




NasTmiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'advisories'), NasAdvisoryType, scope=NasTmiType, documentation='\n                  .NAS Advisory Information: A container for Traffic Flow Management advisories pertinent \n                  to a single flight. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 265, 9)))

NasTmiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reroute'), NasRerouteType, scope=NasTmiType, documentation='\n                  A container for information pertinent to a single NAS reroute issued for a flight \n                  by traffic flow management. \n                  .Traffic Flow Management Reroute Information: A container for information pertinent \n                  to a single NAS reroute issued for a flight by traffic flow management. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 273, 9)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 265, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 273, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasTmiType._UseForTag(pyxb.namespace.ExpandedName(None, 'advisories')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 265, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasTmiType._UseForTag(pyxb.namespace.ExpandedName(None, 'reroute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmi.xsd', 273, 9))
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
NasTmiType._Automaton = _BuildAutomaton_15()




NasHandoffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'acceptingUnit'), _ImportedBinding__fb.AtcUnitReferenceType, scope=NasHandoffType, documentation='\n                        .Handoff Accepting Unit: The Air Traffic Control (ATC) unit accepting control of \n                        the aircraft as a result of a handoff. \n                        .Handoff Accepting Sector: The Air Traffic Control (ATC) sector accepting control \n                        of the aircraft as a result of a handoff. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 71, 15)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 240, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 249, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 259, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 71, 15))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasHandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'coordinationStatus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 240, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasHandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'receivingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 249, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasHandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'transferringUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 259, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasHandoffType._UseForTag(pyxb.namespace.ExpandedName(None, 'acceptingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 71, 15))
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
NasHandoffType._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
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
    symbol = pyxb.binding.content.ElementUse(NasClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'clearedFlightLevel')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 174, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'clearedSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 182, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'directRouting')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 192, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'heading')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 201, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'offtrackClearance')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 209, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasClearedFlightInformationType._UseForTag(pyxb.namespace.ExpandedName(None, 'rateOfClimbDescend')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 217, 9))
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
NasClearedFlightInformationType._Automaton = _BuildAutomaton_17()




NasCoordinationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'coordinationFix'), _ImportedBinding__fb.SignificantPointType, scope=NasCoordinationType, documentation='\n                  .Coordination Fix: The fix to be used in conjunction with the Coordination Time so \n                  processing for this flight (and its trajectory) can be synchronized for the next \n                  sector/facility.  It   coordinates   the flight plan with the aircraft position. \n                  \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 149, 9)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 149, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasCoordinationType._UseForTag(pyxb.namespace.ExpandedName(None, 'coordinationFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 149, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasCoordinationType._Automaton = _BuildAutomaton_18()




FlightIntentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'arrival'), ArrivalMovementAreaHoldInformationType, scope=FlightIntentType, documentation='\n                  .Airport Movement Area Holding - Departure Information: Indicates the intent for \n                  a departing flight to hold in the airport movement area when surface departure metering \n                  or other Traffic Management Initiatives are in effect, and the time when the flight \n                  is estimated to request entry in the airport movement area. \n                  .Airport Movement Area Holding - Arrival Information: Indicates the intent for an \n                  arriving flight to hold in the airport movement area due to unavailability of a parking \n                  stand or ramp access, and the time when the flight is estimated to exit the airport \n                  movement area. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 195, 9)))

FlightIntentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deicing'), DeicingInformationType, scope=FlightIntentType, documentation='\n                  .Deicing Information: Indicates the intent for the flight to be deiced and the intended \n                  deicing location. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 209, 9)))

FlightIntentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'departure'), DepartureMovementAreaHoldInformationType, scope=FlightIntentType, documentation='\n                  .Airport Movement Area Holding - Departure Information: Indicates the intent for \n                  a departing flight to hold in the airport movement area when surface departure metering \n                  or other Traffic Management Initiatives are in effect, and the time when the flight \n                  is estimated to request entry in the airport movement area. \n                  .Airport Movement Area Holding - Arrival Information: Indicates the intent for an \n                  arriving flight to hold in the airport movement area due to unavailability of a parking \n                  stand or ramp access, and the time when the flight is estimated to exit the airport \n                  movement area. \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 217, 9)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 195, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 209, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 217, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FlightIntentType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrival')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 195, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FlightIntentType._UseForTag(pyxb.namespace.ExpandedName(None, 'deicing')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 209, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FlightIntentType._UseForTag(pyxb.namespace.ExpandedName(None, 'departure')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightIntent.xsd', 217, 9))
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
FlightIntentType._Automaton = _BuildAutomaton_19()




FeatureMessageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature'), _ImportedBinding__fb.FeatureType, scope=FeatureMessageType, documentation='\n                        Feature that is contained within the feature message. Anything that extends a Feature \n                        can be placed in a Feature message. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 99, 15)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 99, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FeatureMessageType._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FeatureMessageType._UseForTag(pyxb.namespace.ExpandedName(None, 'feature')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 99, 15))
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
FeatureMessageType._Automaton = _BuildAutomaton_20()




FlightMessageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flight'), _ImportedBinding__fx.FlightType, scope=FlightMessageType, documentation='\n                        Flight that is contained within the Flight message. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 122, 15)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FlightMessageType._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 75, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FlightMessageType._UseForTag(pyxb.namespace.ExpandedName(None, 'flight')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 122, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FlightMessageType._Automaton = _BuildAutomaton_21()




MessageMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'generationLocation'), _ImportedBinding__ff.GeographicLocationType, scope=MessageMetadataType, documentation='\n                  the origin of the message \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 167, 9)))

MessageMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'validTimeSpan'), _ImportedBinding__ff.TimeSpanType, scope=MessageMetadataType, documentation='\n                  the time span over which the message data is valid \n               ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 174, 9)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 167, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 174, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MessageMetadataType._UseForTag(pyxb.namespace.ExpandedName(None, 'generationLocation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 167, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MessageMetadataType._UseForTag(pyxb.namespace.ExpandedName(None, 'validTimeSpan')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasMessage.xsd', 174, 9))
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
MessageMetadataType._Automaton = _BuildAutomaton_22()




NasExpandedRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routeImpactList'), RouteImpactListType, scope=NasExpandedRouteType, documentation='\n                        .Route Impact List: Current traffic flow management prediction of en route Air Traffic \n                        Control units (centres), sectors and airspace elements along the trajectory of a \n                        flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 153, 15)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 216, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 153, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasExpandedRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'routePoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 216, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasExpandedRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeImpactList')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 153, 15))
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
NasExpandedRouteType._Automaton = _BuildAutomaton_23()




NasAirspaceConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'entryTime'), AirspaceEntryTimeType, scope=NasAirspaceConstraintType, documentation='\n                        Container for : \n                        Airspace Entry Time - Earliest \n                        Airspace Entry Time - Initial \n                        Airspace Entry Time - Original \n                        Airspace Entry Time - Traffic Flow Management System Estimated \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 206, 15)))

NasAirspaceConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'exitTime'), AirspaceExitTimeType, scope=NasAirspaceConstraintType, documentation='\n                        .Airspace Exit Time - Traffic Flow Management System Estimated: The estimated airspace \n                        exit time considering all data sources, as determined by Traffic Flow Management \n                        System (TFMS). \n                        .Airspace Entry Time - Traffic Flow Management System Estimated: The estimated airspace \n                        entry time considering all data sources, as determined by Traffic Flow Management \n                        System (TFMS). \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 217, 15)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 92, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 206, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 217, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasAirspaceConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'airspaceControlledEntryTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 92, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasAirspaceConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'entryTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 206, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasAirspaceConstraintType._UseForTag(pyxb.namespace.ExpandedName(None, 'exitTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 217, 15))
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
NasAirspaceConstraintType._Automaton = _BuildAutomaton_24()




def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 360, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightIdentificationType._UseForTag(pyxb.namespace.ExpandedName(None, 'marketingCarrierFlightIdentifier')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 360, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasFlightIdentificationType._Automaton = _BuildAutomaton_25()




NasSupplementalDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'additionalFlightInformation'), _ImportedBinding__fb.NameValueListType, scope=NasSupplementalDataType, documentation='\n                        Additional information about a flight expressed in key-value pairs. \n                        .Other Flight Information: This element consists of an identification tag/indicator \n                        and the relevant value. This information is   extra   information about the flight \n                        that does not fall into some other predefined category. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 390, 15)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 472, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 390, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasSupplementalDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'pilotInCommand')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 472, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasSupplementalDataType._UseForTag(pyxb.namespace.ExpandedName(None, 'additionalFlightInformation')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 390, 15))
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
NasSupplementalDataType._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasRoutePointType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 89, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasRoutePointType._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 409, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteSegmentType._UseForTag(pyxb.namespace.ExpandedName(None, 'routePoint')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 409, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasRouteSegmentType._Automaton = _BuildAutomaton_28()




NasAircraftType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'accuracy'), NasPerformanceBasedAccuracyType, scope=NasAircraftType, documentation="\n                        NAS extension for Performance-Based Navigation Accuracy. \n                        .Performance-Based Navigation Accuracy: This is the flight's navigation accuracy \n                        value for the phase of flight, specified in the Performance-Based Navigation Phase. \n                        \n                        .Performance-Based Navigation Category: This is an enumeration indicating whether \n                        the accuracy measure in Performance-Based Navigation Accuracy is measuring Area Navigation \n                        (RNAV) or Required Navigation Performance (RNP). \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 267, 15)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 92, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 100, 15))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 267, 15))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftType._UseForTag(pyxb.namespace.ExpandedName(None, 'aircraftType')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 92, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftType._UseForTag(pyxb.namespace.ExpandedName(None, 'capabilities')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\aircraft\\AircraftDescription.xsd', 100, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftType._UseForTag(pyxb.namespace.ExpandedName(None, 'accuracy')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasAircraft.xsd', 267, 15))
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
NasAircraftType._Automaton = _BuildAutomaton_29()




NasArrivalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'runwayArrivalTime'), RunwayArrivalTimeType, scope=NasArrivalType, documentation='\n                        Contains the NAS Specific arrival times. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 73, 15)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
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
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 73, 15))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'approachFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 94, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'approachTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 103, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 111, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeAlternate')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 119, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalAerodromeOriginal')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 129, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 137, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrivalFixTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 146, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'filedRevisedDestinationAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 154, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 161, 15))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'standPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Arrival.xsd', 178, 15))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(NasArrivalType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayArrivalTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasArrival.xsd', 73, 15))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasArrivalType._Automaton = _BuildAutomaton_30()




NasUnitBoundaryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boundaryCrossingActual'), _ImportedBinding__fx.BoundaryCrossingType, scope=NasUnitBoundaryType, documentation='\n                        Container for the Actual Boundary Crossing Attributes \n                        .Boundary Crossing Time - Actual: The actual time at which a flight crosses the associated \n                        boundary crossing point. \n                        .Boundary Crossing Position - Actual: The actual boundary crossing point inbound \n                        to the Air Route Traffic Control Center (ARTCC) for the flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 120, 15)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
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
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 120, 15))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasUnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossingCoordinated')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 284, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasUnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossingProposed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 292, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasUnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'downstreamUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 300, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasUnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'handoff')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 311, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasUnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'upstreamUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Coordination.xsd', 320, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasUnitBoundaryType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossingActual')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasCoordination.xsd', 120, 15))
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
NasUnitBoundaryType._Automaton = _BuildAutomaton_31()




NasDepartureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'runwayDepartureTime'), RunwayDepartureTimeType, scope=NasDepartureType, documentation='\n                        Container for NAS Specific Runway Departure Times. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 72, 15)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
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
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 72, 15))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 149, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 157, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureFixTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 166, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'departureTimes')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 176, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'offBlockReadyTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 183, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 195, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'standPositionAndTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 218, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'takeoffAlternateAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 236, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'takeoffWeight')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Departure.xsd', 245, 15))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(NasDepartureType._UseForTag(pyxb.namespace.ExpandedName(None, 'runwayDepartureTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasDeparture.xsd', 72, 15))
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
NasDepartureType._Automaton = _BuildAutomaton_32()




NasEnRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'expectedFurtherClearanceTime'), _ImportedBinding__fb.ReportedTimeType, scope=NasEnRouteType, documentation='\n                        .Hold Data Expect Further Clearance Time: The time the flight can expect further \n                        clearance at the specified hold fix. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 311, 15)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
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
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 311, 15))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'alternateAerodrome')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 297, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'beaconCodeAssignment')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 305, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'boundaryCrossings')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 313, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'cleared')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 322, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'controlElement')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 329, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'cpdlcConnection')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 338, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'pointout')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 345, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\EnRouteData.xsd', 355, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NasEnRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'expectedFurtherClearanceTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasEnRouteData.xsd', 311, 15))
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
NasEnRouteType._Automaton = _BuildAutomaton_33()




NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'assignedAltitude'), NasAltitudeType, scope=NasFlightType, documentation='\n                        .Assigned Altitude: The cruise altitude assigned to the active flight. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 200, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'coordination'), NasCoordinationType, scope=NasFlightType, documentation='\n                        NAS extension to boundary crossing information: includes special handling for ccoordination \n                        time type. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 207, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flightIdentificationPrevious'), NasFlightIdentificationType, scope=NasFlightType, documentation='\n                        The aircraft identification prior to a modification. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 215, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flightIntent'), FlightIntentType, scope=NasFlightType, documentation='\n                        .Flight Intent: A container for the list of intent values provided by the flight \n                        operator that designate the intentions of a flight prior to departure from an aerodrome \n                        or after arrival at an aerodrome. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 222, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flightPlan'), NasFlightPlanType, scope=NasFlightType, documentation='\n                        NAS Flight Plan Information \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 231, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'interimAltitude'), SimpleAltitudeType, nillable=pyxb.binding.datatypes.boolean(1), scope=NasFlightType, documentation='\n                        .Interim Altitude Information: The altitude an aircraft is cleared to maintain different \n                        from that in the flight plan. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 238, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nasTmi'), NasTmiType, scope=NasFlightType, documentation='\n                        NAS Traffic Management Initiative Information \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 246, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'requestedAirspeed'), NasAirspeedChoiceType, scope=NasFlightType, documentation='\n                        .Classified Speed Indicator: The indication that the speed for this flight is classified \n                        and is not to be recorded. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 253, 15)))

NasFlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'requestedAltitude'), NasAltitudeType, scope=NasFlightType, documentation='\n                        .Requested Altitude: The cruise altitude filed or requested for the proposed flight. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 261, 15)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
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
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 200, 15))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 207, 15))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 215, 15))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 222, 15))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 231, 15))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 238, 15))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 246, 15))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 253, 15))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 261, 15))
    counters.add(cc_29)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'agreed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 150, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'aircraftDescription')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 161, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'arrival')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 168, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'controllingUnit')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 175, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'dangerousGoods')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 184, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'departure')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 191, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'emergency')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 198, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'enRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 205, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'enRouteDiversion')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 214, 15))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 222, 15))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightIdentification')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 233, 15))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightStatus')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 240, 15))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'gufi')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 249, 15))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'negotiating')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 257, 15))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'operator')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 269, 15))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'originator')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 276, 15))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'radioCommunicationFailure')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 283, 15))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'rankedTrajectories')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 290, 15))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeToRevisedDestination')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 297, 15))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'specialHandling')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 305, 15))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'supplementalData')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\FlightData.xsd', 316, 15))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'assignedAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 200, 15))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'coordination')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 207, 15))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightIdentificationPrevious')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 215, 15))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightIntent')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 222, 15))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'flightPlan')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 231, 15))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'interimAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 238, 15))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'nasTmi')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 246, 15))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'requestedAirspeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 253, 15))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(NasFlightType._UseForTag(pyxb.namespace.ExpandedName(None, 'requestedAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasFlightData.xsd', 261, 15))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
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
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    st_29._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasFlightType._Automaton = _BuildAutomaton_34()




NasAircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'targetAltitude'), NasPositionAltitudeType, scope=NasAircraftPositionType, documentation='\n                        .Target Altitude: The Mode C target altitude, corrected for barometric pressure. \n                         Can be marked as invalid. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 84, 15)))

NasAircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'targetPosition'), _ImportedBinding__ff.GeographicLocationType, scope=NasAircraftPositionType, documentation='\n                        .Target Position: Aircraft target position, as reported by one raw radar return. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 92, 15)))

NasAircraftPositionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trackVelocity'), NasVelocityType, scope=NasAircraftPositionType, documentation="\n                        Describes flight's velocity in X and Y axes \n         \n                        .Track Speed Components: Speed of the radar surveillance track along the X and Y \n                        components. \n                     ", location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 100, 15)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
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
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 84, 15))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 92, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 100, 15))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'actualSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 127, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 134, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'followingPosition')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 142, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'nextPosition')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 153, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'position')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 165, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'track')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\enroute\\Position.xsd', 174, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'targetAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 84, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'targetPosition')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 92, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NasAircraftPositionType._UseForTag(pyxb.namespace.ExpandedName(None, 'trackVelocity')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasPosition.xsd', 100, 15))
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
NasAircraftPositionType._Automaton = _BuildAutomaton_35()




NasAdaptedArrivalRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nasFavNumber'), STD_ANON_2, scope=NasAdaptedArrivalRouteType, documentation='\n                        .Fixed Airspace Volume Number Containing First Adapted Arrival Route Fix: Contains \n                        the uncombined Fixed Airspace Volume (FAV) number containing the first Adapted Arrival \n                        Route (AAR) fix. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 76, 15)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 76, 15))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasAdaptedArrivalRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'nasFavNumber')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 76, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasAdaptedArrivalRouteType._Automaton = _BuildAutomaton_36()




NasRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adaptedArrivalDepartureRoute'), NasAdaptedRouteType, scope=NasRouteType, documentation='\n                        Container for Adapted Arrival Departure Route information. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 214, 15)))

NasRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adaptedDepartureRoute'), NasAdaptedRouteType, scope=NasRouteType, documentation='\n                        Container for Adapted Departure Route information. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 221, 15)))

NasRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'holdFix'), _ImportedBinding__fb.SignificantPointType, scope=NasRouteType, documentation='\n                        .Hold Data Fix: The location for the flight to Hold along the filed route of flight. \n                        \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 228, 15)))

NasRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nasadaptedArrivalRoute'), NasAdaptedArrivalRouteType, scope=NasRouteType, documentation='\n                        Container for Adapted Arrival Route information. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 236, 15)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
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
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 214, 15))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 221, 15))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 228, 15))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 236, 15))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'climbSchedule')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 279, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'descentSchedule')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 288, 15))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'estimatedElapsedTime')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 297, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'expandedRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 305, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'initialCruisingSpeed')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 316, 15))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'requestedAltitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 325, 15))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'segment')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\Route.xsd', 333, 15))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'adaptedArrivalDepartureRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 214, 15))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'adaptedDepartureRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 221, 15))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'holdFix')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 228, 15))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(NasRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'nasadaptedArrivalRoute')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasRoute.xsd', 236, 15))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NasRouteType._Automaton = _BuildAutomaton_37()




NasTrajectoryOptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constrainedAirspaceEntry'), ConstrainedAirspaceEntryType, scope=NasTrajectoryOptionType, documentation='\n                        Container for NAS Trajectory Option Constraints. \n                     ', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 118, 15)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 103, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 118, 15))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NasTrajectoryOptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeTrajectoryPair')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\core\\flight\\flight\\RankedTrajectory.xsd', 103, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NasTrajectoryOptionType._UseForTag(pyxb.namespace.ExpandedName(None, 'constrainedAirspaceEntry')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\schemas\\extensions\\nas\\NasTmiTrajectoryOptions.xsd', 118, 15))
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
NasTrajectoryOptionType._Automaton = _BuildAutomaton_38()


NasHandoff._setSubstitutionGroup(_ImportedBinding__fx.Handoff)

NasClearedFlightInformation._setSubstitutionGroup(_ImportedBinding__fx.ClearedFlightInformation)

FeatureMessage._setSubstitutionGroup(AbstractMessage)

FlightMessage._setSubstitutionGroup(AbstractMessage)

NasExpandedRoute._setSubstitutionGroup(_ImportedBinding__fx.ExpandedRoute)

NasAirspaceConstraint._setSubstitutionGroup(_ImportedBinding__fx.AirspaceConstraint)

NasFlightIdentification._setSubstitutionGroup(_ImportedBinding__fx.FlightIdentification)

NasSupplementalData._setSubstitutionGroup(_ImportedBinding__fx.SupplementalData)

NasFlightPlan._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasRoutePoint._setSubstitutionGroup(_ImportedBinding__fx.AbstractRoutePoint)

NasRouteSegment._setSubstitutionGroup(_ImportedBinding__fx.RouteSegment)

NasAircraft._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasArrival._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasUnitBoundary._setSubstitutionGroup(_ImportedBinding__fb.AtcUnitReference)

NasDeparture._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasEnRoute._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasFlight._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasAircraftPosition._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasAdaptedArrivalRoute._setSubstitutionGroup(NasAdaptedRoute)

NasRoute._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasFlightStatus._setSubstitutionGroup(_ImportedBinding__fb.Feature)

NasTrajectoryOption._setSubstitutionGroup(_ImportedBinding__fx.RankedTrajectory)
