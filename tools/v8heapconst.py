# Copyright 2013 the V8 project authors. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of Google Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This file is automatically generated from the V8 source and should not
# be modified manually, run 'make grokdump' instead to update this file.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  4: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  6: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  18: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  22: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  26: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  68: "ONE_BYTE_STRING_TYPE",
  69: "CONS_ONE_BYTE_STRING_TYPE",
  70: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  71: "SLICED_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  82: "SHORT_EXTERNAL_STRING_TYPE",
  86: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  90: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "SIMD128_VALUE_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_DOUBLE_ARRAY_TYPE",
  149: "FILLER_TYPE",
  150: "ACCESSOR_INFO_TYPE",
  151: "ACCESSOR_PAIR_TYPE",
  152: "ACCESS_CHECK_INFO_TYPE",
  153: "INTERCEPTOR_INFO_TYPE",
  154: "CALL_HANDLER_INFO_TYPE",
  155: "FUNCTION_TEMPLATE_INFO_TYPE",
  156: "OBJECT_TEMPLATE_INFO_TYPE",
  157: "ALLOCATION_SITE_TYPE",
  158: "ALLOCATION_MEMENTO_TYPE",
  159: "SCRIPT_TYPE",
  160: "TYPE_FEEDBACK_INFO_TYPE",
  161: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  162: "BOX_TYPE",
  163: "PROMISE_RESOLVE_THENABLE_JOB_INFO_TYPE",
  164: "PROMISE_REACTION_JOB_INFO_TYPE",
  165: "DEBUG_INFO_TYPE",
  166: "BREAK_POINT_INFO_TYPE",
  167: "PROTOTYPE_INFO_TYPE",
  168: "TUPLE2_TYPE",
  169: "TUPLE3_TYPE",
  170: "CONTEXT_EXTENSION_TYPE",
  171: "CONSTANT_ELEMENTS_PAIR_TYPE",
  172: "MODULE_TYPE",
  173: "MODULE_INFO_ENTRY_TYPE",
  174: "FIXED_ARRAY_TYPE",
  175: "TRANSITION_ARRAY_TYPE",
  176: "SHARED_FUNCTION_INFO_TYPE",
  177: "CELL_TYPE",
  178: "WEAK_CELL_TYPE",
  179: "PROPERTY_CELL_TYPE",
  180: "JS_PROXY_TYPE",
  181: "JS_GLOBAL_OBJECT_TYPE",
  182: "JS_GLOBAL_PROXY_TYPE",
  183: "JS_SPECIAL_API_OBJECT_TYPE",
  184: "JS_VALUE_TYPE",
  185: "JS_MESSAGE_OBJECT_TYPE",
  186: "JS_DATE_TYPE",
  187: "JS_API_OBJECT_TYPE",
  188: "JS_OBJECT_TYPE",
  189: "JS_ARGUMENTS_TYPE",
  190: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  191: "JS_GENERATOR_OBJECT_TYPE",
  192: "JS_MODULE_NAMESPACE_TYPE",
  193: "JS_ARRAY_TYPE",
  194: "JS_ARRAY_BUFFER_TYPE",
  195: "JS_TYPED_ARRAY_TYPE",
  196: "JS_DATA_VIEW_TYPE",
  197: "JS_SET_TYPE",
  198: "JS_MAP_TYPE",
  199: "JS_SET_ITERATOR_TYPE",
  200: "JS_MAP_ITERATOR_TYPE",
  201: "JS_WEAK_MAP_TYPE",
  202: "JS_WEAK_SET_TYPE",
  203: "JS_PROMISE_TYPE",
  204: "JS_REGEXP_TYPE",
  205: "JS_ERROR_TYPE",
  206: "JS_STRING_ITERATOR_TYPE",
  207: "JS_TYPED_ARRAY_KEY_ITERATOR_TYPE",
  208: "JS_FAST_ARRAY_KEY_ITERATOR_TYPE",
  209: "JS_GENERIC_ARRAY_KEY_ITERATOR_TYPE",
  210: "JS_UINT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  211: "JS_INT8_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  212: "JS_UINT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  213: "JS_INT16_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  214: "JS_UINT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  215: "JS_INT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  216: "JS_FLOAT32_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  217: "JS_FLOAT64_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  218: "JS_UINT8_CLAMPED_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  219: "JS_FAST_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  220: "JS_FAST_HOLEY_SMI_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  221: "JS_FAST_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  222: "JS_FAST_HOLEY_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  223: "JS_FAST_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  224: "JS_FAST_HOLEY_DOUBLE_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  225: "JS_GENERIC_ARRAY_KEY_VALUE_ITERATOR_TYPE",
  226: "JS_UINT8_ARRAY_VALUE_ITERATOR_TYPE",
  227: "JS_INT8_ARRAY_VALUE_ITERATOR_TYPE",
  228: "JS_UINT16_ARRAY_VALUE_ITERATOR_TYPE",
  229: "JS_INT16_ARRAY_VALUE_ITERATOR_TYPE",
  230: "JS_UINT32_ARRAY_VALUE_ITERATOR_TYPE",
  231: "JS_INT32_ARRAY_VALUE_ITERATOR_TYPE",
  232: "JS_FLOAT32_ARRAY_VALUE_ITERATOR_TYPE",
  233: "JS_FLOAT64_ARRAY_VALUE_ITERATOR_TYPE",
  234: "JS_UINT8_CLAMPED_ARRAY_VALUE_ITERATOR_TYPE",
  235: "JS_FAST_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  236: "JS_FAST_HOLEY_SMI_ARRAY_VALUE_ITERATOR_TYPE",
  237: "JS_FAST_ARRAY_VALUE_ITERATOR_TYPE",
  238: "JS_FAST_HOLEY_ARRAY_VALUE_ITERATOR_TYPE",
  239: "JS_FAST_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  240: "JS_FAST_HOLEY_DOUBLE_ARRAY_VALUE_ITERATOR_TYPE",
  241: "JS_GENERIC_ARRAY_VALUE_ITERATOR_TYPE",
  242: "JS_BOUND_FUNCTION_TYPE",
  243: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x84101: (138, "FreeSpaceMap"),
  0x8412d: (132, "MetaMap"),
  0x84159: (131, "NullMap"),
  0x84185: (174, "FixedArrayMap"),
  0x841b1: (4, "OneByteInternalizedStringMap"),
  0x841dd: (149, "OnePointerFillerMap"),
  0x84209: (149, "TwoPointerFillerMap"),
  0x84235: (131, "UninitializedMap"),
  0x84261: (131, "UndefinedMap"),
  0x8428d: (129, "HeapNumberMap"),
  0x842b9: (131, "TheHoleMap"),
  0x842e5: (131, "BooleanMap"),
  0x84311: (136, "ByteArrayMap"),
  0x8433d: (174, "FixedCOWArrayMap"),
  0x84369: (174, "HashTableMap"),
  0x84395: (128, "SymbolMap"),
  0x843c1: (68, "OneByteStringMap"),
  0x843ed: (174, "ScopeInfoMap"),
  0x84419: (176, "SharedFunctionInfoMap"),
  0x84445: (133, "CodeMap"),
  0x84471: (174, "FunctionContextMap"),
  0x8449d: (177, "CellMap"),
  0x844c9: (178, "WeakCellMap"),
  0x844f5: (179, "GlobalPropertyCellMap"),
  0x84521: (135, "ForeignMap"),
  0x8454d: (175, "TransitionArrayMap"),
  0x84579: (131, "NoInterceptorResultSentinelMap"),
  0x845a5: (131, "ArgumentsMarkerMap"),
  0x845d1: (174, "NativeContextMap"),
  0x845fd: (174, "ModuleContextMap"),
  0x84629: (174, "ScriptContextMap"),
  0x84655: (174, "BlockContextMap"),
  0x84681: (174, "CatchContextMap"),
  0x846ad: (174, "WithContextMap"),
  0x846d9: (148, "FixedDoubleArrayMap"),
  0x84705: (134, "MutableHeapNumberMap"),
  0x84731: (174, "OrderedHashTableMap"),
  0x8475d: (174, "SloppyArgumentsElementsMap"),
  0x84789: (185, "JSMessageObjectMap"),
  0x847b5: (137, "BytecodeArrayMap"),
  0x847e1: (174, "ModuleInfoMap"),
  0x8480d: (64, "StringMap"),
  0x84839: (69, "ConsOneByteStringMap"),
  0x84865: (65, "ConsStringMap"),
  0x84891: (67, "SlicedStringMap"),
  0x848bd: (71, "SlicedOneByteStringMap"),
  0x848e9: (66, "ExternalStringMap"),
  0x84915: (74, "ExternalStringWithOneByteDataMap"),
  0x84941: (70, "ExternalOneByteStringMap"),
  0x8496d: (82, "ShortExternalStringMap"),
  0x84999: (90, "ShortExternalStringWithOneByteDataMap"),
  0x849c5: (0, "InternalizedStringMap"),
  0x849f1: (2, "ExternalInternalizedStringMap"),
  0x84a1d: (10, "ExternalInternalizedStringWithOneByteDataMap"),
  0x84a49: (6, "ExternalOneByteInternalizedStringMap"),
  0x84a75: (18, "ShortExternalInternalizedStringMap"),
  0x84aa1: (26, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x84acd: (22, "ShortExternalOneByteInternalizedStringMap"),
  0x84af9: (86, "ShortExternalOneByteStringMap"),
  0x84b25: (130, "Float32x4Map"),
  0x84b51: (130, "Int32x4Map"),
  0x84b7d: (130, "Uint32x4Map"),
  0x84ba9: (130, "Bool32x4Map"),
  0x84bd5: (130, "Int16x8Map"),
  0x84c01: (130, "Uint16x8Map"),
  0x84c2d: (130, "Bool16x8Map"),
  0x84c59: (130, "Int8x16Map"),
  0x84c85: (130, "Uint8x16Map"),
  0x84cb1: (130, "Bool8x16Map"),
  0x84cdd: (131, "ExceptionMap"),
  0x84d09: (131, "TerminationExceptionMap"),
  0x84d35: (131, "OptimizedOutMap"),
  0x84d61: (131, "StaleRegisterMap"),
  0x84d8d: (174, "DebugEvaluateContextMap"),
  0x84db9: (174, "ScriptContextTableMap"),
  0x84de5: (174, "UnseededNumberDictionaryMap"),
  0x84e11: (188, "ExternalMap"),
  0x84e3d: (86, "NativeSourceStringMap"),
  0x84e69: (140, "FixedUint8ArrayMap"),
  0x84e95: (139, "FixedInt8ArrayMap"),
  0x84ec1: (142, "FixedUint16ArrayMap"),
  0x84eed: (141, "FixedInt16ArrayMap"),
  0x84f19: (144, "FixedUint32ArrayMap"),
  0x84f45: (143, "FixedInt32ArrayMap"),
  0x84f71: (145, "FixedFloat32ArrayMap"),
  0x84f9d: (146, "FixedFloat64ArrayMap"),
  0x84fc9: (147, "FixedUint8ClampedArrayMap"),
  0x84ff5: (159, "ScriptMap"),
  0x85021: (157, "AllocationSiteMap"),
  0x8504d: (158, "AllocationMementoMap"),
  0x85079: (150, "AccessorInfoMap"),
  0x850a5: (155, "FunctionTemplateInfoMap"),
  0x850d1: (168, "Tuple2Map"),
  0x850fd: (167, "PrototypeInfoMap"),
  0x85129: (151, "AccessorPairMap"),
  0x85155: (152, "AccessCheckInfoMap"),
  0x85181: (153, "InterceptorInfoMap"),
  0x851ad: (154, "CallHandlerInfoMap"),
  0x851d9: (156, "ObjectTemplateInfoMap"),
  0x85205: (160, "TypeFeedbackInfoMap"),
  0x85231: (161, "AliasedArgumentsEntryMap"),
  0x8525d: (162, "BoxMap"),
  0x85289: (163, "PromiseResolveThenableJobInfoMap"),
  0x852b5: (164, "PromiseReactionJobInfoMap"),
  0x852e1: (165, "DebugInfoMap"),
  0x8530d: (166, "BreakPointInfoMap"),
  0x85339: (169, "Tuple3Map"),
  0x85365: (170, "ContextExtensionMap"),
  0x85391: (171, "ConstantElementsPairMap"),
  0x853bd: (172, "ModuleMap"),
  0x853e9: (173, "ModuleInfoEntryMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_SPACE", 0x84101): "NullValue",
  ("OLD_SPACE", 0x8411d): "EmptyDescriptorArray",
  ("OLD_SPACE", 0x84125): "EmptyFixedArray",
  ("OLD_SPACE", 0x84151): "UninitializedValue",
  ("OLD_SPACE", 0x841a1): "UndefinedValue",
  ("OLD_SPACE", 0x841bd): "NanValue",
  ("OLD_SPACE", 0x841cd): "TheHoleValue",
  ("OLD_SPACE", 0x841fd): "HoleNanValue",
  ("OLD_SPACE", 0x84209): "TrueValue",
  ("OLD_SPACE", 0x84249): "FalseValue",
  ("OLD_SPACE", 0x84279): "empty_string",
  ("OLD_SPACE", 0x84285): "NoInterceptorResultSentinel",
  ("OLD_SPACE", 0x842cd): "ArgumentsMarker",
  ("OLD_SPACE", 0x84305): "EmptyByteArray",
  ("OLD_SPACE", 0x8430d): "EmptyWeakCell",
  ("OLD_SPACE", 0x8431d): "InfinityValue",
  ("OLD_SPACE", 0x8432d): "MinusZeroValue",
  ("OLD_SPACE", 0x8433d): "MinusInfinityValue",
  ("OLD_SPACE", 0x85939): "EmptyLiteralsArray",
  ("OLD_SPACE", 0x85945): "EmptyTypeFeedbackVector",
  ("OLD_SPACE", 0x85955): "EmptyScopeInfo",
  ("OLD_SPACE", 0x8595d): "Exception",
  ("OLD_SPACE", 0x85991): "TerminationException",
  ("OLD_SPACE", 0x859d1): "OptimizedOut",
  ("OLD_SPACE", 0x85a09): "StaleRegister",
  ("OLD_SPACE", 0x85a41): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x85a51): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x85a61): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x85a71): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x85a81): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x85a91): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x85aa1): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x85ab1): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x85ac1): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x85ad1): "EmptyScript",
  ("OLD_SPACE", 0x85b11): "UndefinedCell",
  ("OLD_SPACE", 0x85b19): "EmptySloppyArgumentsElements",
  ("OLD_SPACE", 0x85b29): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x85b75): "DummyVector",
  ("OLD_SPACE", 0x85bb9): "EmptyPropertyCell",
  ("OLD_SPACE", 0x85bc9): "ArrayProtector",
  ("OLD_SPACE", 0x85bd9): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x85be1): "HasInstanceProtector",
  ("OLD_SPACE", 0x85bf1): "SpeciesProtector",
  ("OLD_SPACE", 0x85bf9): "StringLengthProtector",
  ("OLD_SPACE", 0x85c09): "FastArrayIterationProtector",
  ("OLD_SPACE", 0x85c11): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x85c19): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x85c29): "NumberStringCache",
  ("OLD_SPACE", 0x86431): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x86859): "StringSplitCache",
  ("OLD_SPACE", 0x86c61): "RegExpMultipleCache",
  ("OLD_SPACE", 0x87069): "NativesSourceCache",
  ("OLD_SPACE", 0x871d1): "ExperimentalNativesSourceCache",
  ("OLD_SPACE", 0x871ed): "ExtraNativesSourceCache",
  ("OLD_SPACE", 0x87209): "ExperimentalExtraNativesSourceCache",
  ("OLD_SPACE", 0x87215): "EmptyPropertiesDictionary",
  ("OLD_SPACE", 0x87261): "ScriptList",
  ("OLD_SPACE", 0x9ab99): "CodeStubs",
  ("OLD_SPACE", 0xa2bd5): "WeakObjectToCodeTable",
  ("OLD_SPACE", 0xa2ce9): "WeakNewSpaceObjectToCodeList",
  ("OLD_SPACE", 0xa2d31): "NoScriptSharedFunctionInfos",
  ("OLD_SPACE", 0xb26e9): "MessageListeners",
  ("OLD_SPACE", 0xb6d75): "StringTable",
  ("CODE_SPACE", 0x1aa01): "JsConstructEntryCode",
  ("CODE_SPACE", 0x29ba1): "JsEntryCode",
}
