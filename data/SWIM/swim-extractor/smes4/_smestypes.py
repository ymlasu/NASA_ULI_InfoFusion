# .\smes4\_smestypes.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:cdc00f7678203403b0fb74d823fcea4b22d00b99
# Generated 2018-10-25 13:10:31.876278 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes [xmlns:smestypes]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:42b95870-d881-11e8-abcd-ecb1d75f2e16')

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
import smes4._common as _ImportedBinding_smes4__common

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes', create_if_missing=True)
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


# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}surfaceEventType
class surfaceEventType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'surfaceEventType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 14, 1)
    _Documentation = None
surfaceEventType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=surfaceEventType, enum_prefix=None)
surfaceEventType.on = surfaceEventType._CF_enumeration.addEnumeration(unicode_value='on', tag='on')
surfaceEventType.off = surfaceEventType._CF_enumeration.addEnumeration(unicode_value='off', tag='off')
surfaceEventType.spotout = surfaceEventType._CF_enumeration.addEnumeration(unicode_value='spotout', tag='spotout')
surfaceEventType.spotin = surfaceEventType._CF_enumeration.addEnumeration(unicode_value='spotin', tag='spotin')
surfaceEventType._InitializeFacetMap(surfaceEventType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'surfaceEventType', surfaceEventType)
_module_typeBindings.surfaceEventType = surfaceEventType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}altitudeType
class altitudeType (pyxb.binding.datatypes.double):

    """In feet"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'altitudeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 46, 1)
    _Documentation = 'In feet'
altitudeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'altitudeType', altitudeType)
_module_typeBindings.altitudeType = altitudeType

# Atomic simple type: {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}flightStatusType
class flightStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flightStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 67, 1)
    _Documentation = None
flightStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=flightStatusType, enum_prefix=None)
flightStatusType.undefined = flightStatusType._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
flightStatusType.airborne = flightStatusType._CF_enumeration.addEnumeration(unicode_value='airborne', tag='airborne')
flightStatusType.onramp = flightStatusType._CF_enumeration.addEnumeration(unicode_value='onramp', tag='onramp')
flightStatusType.onsurface = flightStatusType._CF_enumeration.addEnumeration(unicode_value='onsurface', tag='onsurface')
flightStatusType._InitializeFacetMap(flightStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'flightStatusType', flightStatusType)
_module_typeBindings.flightStatusType = flightStatusType

# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}positionType with content type ELEMENT_ONLY
class positionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}positionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 38, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'latitude'), 'latitude', '__urnusgovdotfaaatmterminalentitiesv4_0smessmestypes_positionType_latitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 40, 3), )

    
    latitude = property(__latitude.value, __latitude.set, None, None)

    
    # Element longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'longitude'), 'longitude', '__urnusgovdotfaaatmterminalentitiesv4_0smessmestypes_positionType_longitude', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 42, 3), )

    
    longitude = property(__longitude.value, __longitude.set, None, None)

    _ElementMap.update({
        __latitude.name() : __latitude,
        __longitude.name() : __longitude
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.positionType = positionType
Namespace.addCategoryObject('typeBinding', 'positionType', positionType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}surfaceEventRecordType with content type ELEMENT_ONLY
class surfaceEventRecordType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}surfaceEventRecordType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'surfaceEventRecordType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 52, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event'), 'event', '__urnusgovdotfaaatmterminalentitiesv4_0smessmestypes_surfaceEventRecordType_event', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 54, 3), )

    
    event = property(__event.value, __event.set, None, None)

    
    # Element at uses Python identifier at
    __at = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'at'), 'at', '__urnusgovdotfaaatmterminalentitiesv4_0smessmestypes_surfaceEventRecordType_at', False, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 56, 3), )

    
    at = property(__at.value, __at.set, None, None)

    _ElementMap.update({
        __event.name() : __event,
        __at.name() : __at
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.surfaceEventRecordType = surfaceEventRecordType
Namespace.addCategoryObject('typeBinding', 'surfaceEventRecordType', surfaceEventRecordType)


# Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}surfaceEventListType with content type ELEMENT_ONLY
class surfaceEventListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:smestypes}surfaceEventListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'surfaceEventListType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 60, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element eventRecord uses Python identifier eventRecord
    __eventRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'eventRecord'), 'eventRecord', '__urnusgovdotfaaatmterminalentitiesv4_0smessmestypes_surfaceEventListType_eventRecord', True, pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 62, 3), )

    
    eventRecord = property(__eventRecord.value, __eventRecord.set, None, None)

    _ElementMap.update({
        __eventRecord.name() : __eventRecord
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.surfaceEventListType = surfaceEventListType
Namespace.addCategoryObject('typeBinding', 'surfaceEventListType', surfaceEventListType)




positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'latitude'), _ImportedBinding_smes4__common.latitudeType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 40, 3)))

positionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'longitude'), _ImportedBinding_smes4__common.longitudeType, scope=positionType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 42, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(None, 'latitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 40, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(positionType._UseForTag(pyxb.namespace.ExpandedName(None, 'longitude')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
positionType._Automaton = _BuildAutomaton()




surfaceEventRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event'), surfaceEventType, scope=surfaceEventRecordType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 54, 3)))

surfaceEventRecordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'at'), pyxb.binding.datatypes.dateTime, scope=surfaceEventRecordType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 56, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(surfaceEventRecordType._UseForTag(pyxb.namespace.ExpandedName(None, 'event')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 54, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(surfaceEventRecordType._UseForTag(pyxb.namespace.ExpandedName(None, 'at')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
surfaceEventRecordType._Automaton = _BuildAutomaton_()




surfaceEventListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'eventRecord'), surfaceEventRecordType, scope=surfaceEventListType, location=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 62, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=50, metadata=pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 62, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(surfaceEventListType._UseForTag(pyxb.namespace.ExpandedName(None, 'eventRecord')), pyxb.utils.utility.Location('C:\\Users\\awhittington\\Documents\\SWIM\\R4 Schema\\externalInterfaces\\smes\\SMESTypes.xsd', 62, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
surfaceEventListType._Automaton = _BuildAutomaton_2()

