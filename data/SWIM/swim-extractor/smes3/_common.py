# .\smes3\_common.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e83a0f219e6b6272a2a76cbce5707bef44db4480
# Generated 2018-10-25 13:10:06.841389 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes [xmlns:common]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes', create_if_missing=True)
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


# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}AircraftIdentifier
class AircraftIdentifier (pyxb.binding.datatypes.string):

    """
				An aircraft identifier is 1 to 8 alphanumeric characters.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AircraftIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 10, 1)
    _Documentation = '\n\t\t\t\tAn aircraft identifier is 1 to 8 alphanumeric characters.\n\t\t\t'
AircraftIdentifier._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
AircraftIdentifier._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
AircraftIdentifier._InitializeFacetMap(AircraftIdentifier._CF_minLength,
   AircraftIdentifier._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'AircraftIdentifier', AircraftIdentifier)
_module_typeBindings.AircraftIdentifier = AircraftIdentifier

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}AirportIdentifier
class AirportIdentifier (pyxb.binding.datatypes.string):

    """
				An airport identifier is 2 to 5 alphanumeric
				characters.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AirportIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 22, 1)
    _Documentation = '\n\t\t\t\tAn airport identifier is 2 to 5 alphanumeric\n\t\t\t\tcharacters.\n\t\t\t'
AirportIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
AirportIdentifier._CF_pattern.addPattern(pattern='[A-Z0-9]{2,5}')
AirportIdentifier._InitializeFacetMap(AirportIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AirportIdentifier', AirportIdentifier)
_module_typeBindings.AirportIdentifier = AirportIdentifier

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}BeaconCode
class BeaconCode (pyxb.binding.datatypes.string):

    """
				A beacon code is a string of 4 characters, each in
				the range "0" to
				"7".
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BeaconCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 34, 1)
    _Documentation = '\n\t\t\t\tA beacon code is a string of 4 characters, each in\n\t\t\t\tthe range "0" to\n\t\t\t\t"7".\n\t\t\t'
BeaconCode._CF_pattern = pyxb.binding.facets.CF_pattern()
BeaconCode._CF_pattern.addPattern(pattern='[0-7]{4}')
BeaconCode._InitializeFacetMap(BeaconCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BeaconCode', BeaconCode)
_module_typeBindings.BeaconCode = BeaconCode

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}latitudeType
class latitudeType (pyxb.binding.datatypes.double):

    """In Degrees"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'latitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 47, 1)
    _Documentation = 'In Degrees'
latitudeType._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes._fp(-90.0))
latitudeType._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes._fp(90.0))
latitudeType._InitializeFacetMap(latitudeType._CF_minExclusive,
   latitudeType._CF_maxExclusive)
Namespace.addCategoryObject('typeBinding', 'latitudeType', latitudeType)
_module_typeBindings.latitudeType = latitudeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}longitudeType
class longitudeType (pyxb.binding.datatypes.double):

    """In degrees"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 57, 1)
    _Documentation = 'In degrees'
longitudeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=longitudeType, value=pyxb.binding.datatypes.double(-180.0))
longitudeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=longitudeType, value=pyxb.binding.datatypes.double(180.0))
longitudeType._InitializeFacetMap(longitudeType._CF_minInclusive,
   longitudeType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'longitudeType', longitudeType)
_module_typeBindings.longitudeType = longitudeType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 80, 4)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='[0-3][0-9]')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 87, 4)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.C = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
STD_ANON_.L = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
STD_ANON_.R = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
STD_ANON_.emptyString = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=' ', tag='emptyString')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}TraconIdentifier
class TraconIdentifier (pyxb.binding.datatypes.string):

    """
				A TRACON identifier is a letter followed by 2 to 6
				alphanumeric
				characters.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TraconIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 123, 1)
    _Documentation = '\n\t\t\t\tA TRACON identifier is a letter followed by 2 to 6\n\t\t\t\talphanumeric\n\t\t\t\tcharacters.\n\t\t\t'
TraconIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
TraconIdentifier._CF_pattern.addPattern(pattern='[A-Z][A-Z0-9]{2,6}')
TraconIdentifier._InitializeFacetMap(TraconIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TraconIdentifier', TraconIdentifier)
_module_typeBindings.TraconIdentifier = TraconIdentifier

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}HoldbarsStatus
class HoldbarsStatus (pyxb.binding.datatypes.string):

    """
				Hex string conveying the bit map status of each hold bar (1…256)
				indicating visibility (0: Not Visible, 1: Visible). The bits are
				assigned sequentially, starting at bit 0 in word 8 and working
				backwards (i.e. Hold Bar 256 is represented by bit 31 in word 1).
				This field will not be published if the hold bars are disabled.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HoldbarsStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 153, 1)
    _Documentation = '\n\t\t\t\tHex string conveying the bit map status of each hold bar (1…256)\n\t\t\t\tindicating visibility (0: Not Visible, 1: Visible). The bits are\n\t\t\t\tassigned sequentially, starting at bit 0 in word 8 and working\n\t\t\t\tbackwards (i.e. Hold Bar 256 is represented by bit 31 in word 1).\n\t\t\t\tThis field will not be published if the hold bars are disabled.\n\t\t\t'
HoldbarsStatus._CF_pattern = pyxb.binding.facets.CF_pattern()
HoldbarsStatus._CF_pattern.addPattern(pattern='[0-9A-Fa-f]{64}')
HoldbarsStatus._InitializeFacetMap(HoldbarsStatus._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'HoldbarsStatus', HoldbarsStatus)
_module_typeBindings.HoldbarsStatus = HoldbarsStatus

# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}RunwayIdentifier with content type ELEMENT_ONLY
class RunwayIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """
				A runway identifier is a numeric identifier (01 to
				36 inclusive)
				followed by a sub identifier (C, L, R, or
				space). Taken
				from NAS-IR-33110001.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunwayIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 67, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element numericRunwayID uses Python identifier numericRunwayID
    __numericRunwayID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numericRunwayID'), 'numericRunwayID', '__urnusgovdotfaaatmterminalentitiesv3_0commontypes_RunwayIdentifier_numericRunwayID', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 78, 3), )

    
    numericRunwayID = property(__numericRunwayID.value, __numericRunwayID.set, None, None)

    
    # Element runwaySubID uses Python identifier runwaySubID
    __runwaySubID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'runwaySubID'), 'runwaySubID', '__urnusgovdotfaaatmterminalentitiesv3_0commontypes_RunwayIdentifier_runwaySubID', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 86, 3), )

    
    runwaySubID = property(__runwaySubID.value, __runwaySubID.set, None, None)

    _ElementMap.update({
        __numericRunwayID.name() : __numericRunwayID,
        __runwaySubID.name() : __runwaySubID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RunwayIdentifier = RunwayIdentifier
Namespace.addCategoryObject('typeBinding', 'RunwayIdentifier', RunwayIdentifier)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v3-0:commontypes}PropertyType with content type ELEMENT_ONLY
class PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """A property value"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 136, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p'), 'p', '__urnusgovdotfaaatmterminalentitiesv3_0commontypes_PropertyType_p', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 141, 4), )

    
    p = property(__p.value, __p.set, None, '\n\t\t\t\t\t\t\tA property value\n\t\t\t\t\t\t')

    
    # Attribute k uses Python identifier k
    __k = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k'), 'k', '__urnusgovdotfaaatmterminalentitiesv3_0commontypes_PropertyType_k', pyxb.binding.datatypes.string, required=True)
    __k._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 149, 2)
    __k._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 149, 2)
    
    k = property(__k.value, __k.set, None, None)

    
    # Attribute v uses Python identifier v
    __v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'v'), 'v', '__urnusgovdotfaaatmterminalentitiesv3_0commontypes_PropertyType_v', pyxb.binding.datatypes.string)
    __v._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 150, 2)
    __v._UseLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 150, 2)
    
    v = property(__v.value, __v.set, None, None)

    _ElementMap.update({
        __p.name() : __p
    })
    _AttributeMap.update({
        __k.name() : __k,
        __v.name() : __v
    })
_module_typeBindings.PropertyType = PropertyType
Namespace.addCategoryObject('typeBinding', 'PropertyType', PropertyType)




RunwayIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numericRunwayID'), STD_ANON, scope=RunwayIdentifier, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 78, 3)))

RunwayIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'runwaySubID'), STD_ANON_, scope=RunwayIdentifier, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 86, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 78, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 86, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RunwayIdentifier._UseForTag(pyxb.namespace.ExpandedName(None, 'numericRunwayID')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 78, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RunwayIdentifier._UseForTag(pyxb.namespace.ExpandedName(None, 'runwaySubID')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 86, 3))
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
RunwayIdentifier._Automaton = _BuildAutomaton()




PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p'), PropertyType, scope=PropertyType, documentation='\n\t\t\t\t\t\t\tA property value\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 141, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 141, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PropertyType._UseForTag(pyxb.namespace.ExpandedName(None, 'p')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R3.3 Schema\\externalInterfaces\\commontypes\\CommonTypes.xsd', 141, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PropertyType._Automaton = _BuildAutomaton_()

