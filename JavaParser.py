# $ANTLR 3.4 Java.g 2012-09-20 01:12:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ABSTRACT=4
AND=5
AND_ASSIGN=6
ANNOTATION_INIT_ARRAY_ELEMENT=7
ANNOTATION_INIT_BLOCK=8
ANNOTATION_INIT_DEFAULT_KEY=9
ANNOTATION_INIT_KEY_LIST=10
ANNOTATION_LIST=11
ANNOTATION_METHOD_DECL=12
ANNOTATION_SCOPE=13
ANNOTATION_TOP_LEVEL_SCOPE=14
ARGUMENT_LIST=15
ARRAY_DECLARATOR=16
ARRAY_DECLARATOR_LIST=17
ARRAY_ELEMENT_ACCESS=18
ARRAY_INITIALIZER=19
ASSERT=20
ASSIGN=21
AT=22
BIT_SHIFT_RIGHT=23
BIT_SHIFT_RIGHT_ASSIGN=24
BLOCK_SCOPE=25
BOOLEAN=26
BREAK=27
BYTE=28
CASE=29
CAST_EXPR=30
CATCH=31
CATCH_CLAUSE_LIST=32
CHAR=33
CHARACTER_LITERAL=34
CLASS=35
CLASS_CONSTRUCTOR_CALL=36
CLASS_INSTANCE_INITIALIZER=37
CLASS_STATIC_INITIALIZER=38
CLASS_TOP_LEVEL_SCOPE=39
COLON=40
COMMA=41
COMMENT=42
CONSTRUCTOR_DECL=43
CONTINUE=44
DEC=45
DECIMAL_LITERAL=46
DEFAULT=47
DIV=48
DIV_ASSIGN=49
DO=50
DOT=51
DOTSTAR=52
DOUBLE=53
ELLIPSIS=54
ELSE=55
ENUM=56
ENUM_TOP_LEVEL_SCOPE=57
EQUAL=58
ESCAPE_SEQUENCE=59
EXPONENT=60
EXPR=61
EXTENDS=62
EXTENDS_BOUND_LIST=63
EXTENDS_CLAUSE=64
FALSE=65
FINAL=66
FINALLY=67
FLOAT=68
FLOATING_POINT_LITERAL=69
FLOAT_TYPE_SUFFIX=70
FOR=71
FORMAL_PARAM_LIST=72
FORMAL_PARAM_STD_DECL=73
FORMAL_PARAM_VARARG_DECL=74
FOR_CONDITION=75
FOR_EACH=76
FOR_INIT=77
FOR_UPDATE=78
FUNCTION_METHOD_DECL=79
GENERIC_TYPE_ARG_LIST=80
GENERIC_TYPE_PARAM_LIST=81
GREATER_OR_EQUAL=82
GREATER_THAN=83
HEX_DIGIT=84
HEX_LITERAL=85
IDENT=86
IF=87
IMPLEMENTS=88
IMPLEMENTS_CLAUSE=89
IMPORT=90
INC=91
INSTANCEOF=92
INT=93
INTEGER_TYPE_SUFFIX=94
INTERFACE=95
INTERFACE_TOP_LEVEL_SCOPE=96
JAVA_ID_PART=97
JAVA_ID_START=98
JAVA_SOURCE=99
LABELED_STATEMENT=100
LBRACK=101
LCURLY=102
LESS_OR_EQUAL=103
LESS_THAN=104
LINE_COMMENT=105
LOCAL_MODIFIER_LIST=106
LOGICAL_AND=107
LOGICAL_NOT=108
LOGICAL_OR=109
LONG=110
LPAREN=111
METHOD_CALL=112
MINUS=113
MINUS_ASSIGN=114
MOD=115
MODIFIER_LIST=116
MOD_ASSIGN=117
NATIVE=118
NEW=119
NOT=120
NOT_EQUAL=121
NULL=122
OCTAL_ESCAPE=123
OCTAL_LITERAL=124
OR=125
OR_ASSIGN=126
PACKAGE=127
PARENTESIZED_EXPR=128
PLUS=129
PLUS_ASSIGN=130
POST_DEC=131
POST_INC=132
PRE_DEC=133
PRE_INC=134
PRIVATE=135
PROTECTED=136
PUBLIC=137
QUALIFIED_TYPE_IDENT=138
QUESTION=139
RBRACK=140
RCURLY=141
RETURN=142
RPAREN=143
SEMI=144
SHIFT_LEFT=145
SHIFT_LEFT_ASSIGN=146
SHIFT_RIGHT=147
SHIFT_RIGHT_ASSIGN=148
SHORT=149
STAR=150
STAR_ASSIGN=151
STATIC=152
STATIC_ARRAY_CREATOR=153
STRICTFP=154
STRING_LITERAL=155
SUPER=156
SUPER_CONSTRUCTOR_CALL=157
SWITCH=158
SWITCH_BLOCK_LABEL_LIST=159
SYNCHRONIZED=160
THIS=161
THIS_CONSTRUCTOR_CALL=162
THROW=163
THROWS=164
THROWS_CLAUSE=165
TRANSIENT=166
TRUE=167
TRY=168
TYPE=169
UNARY_MINUS=170
UNARY_PLUS=171
UNICODE_ESCAPE=172
VAR_DECLARATION=173
VAR_DECLARATOR=174
VAR_DECLARATOR_LIST=175
VOID=176
VOID_METHOD_DECL=177
VOLATILE=178
WHILE=179
WS=180
XOR=181
XOR_ASSIGN=182

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ABSTRACT", "AND", "AND_ASSIGN", "ANNOTATION_INIT_ARRAY_ELEMENT", "ANNOTATION_INIT_BLOCK", 
    "ANNOTATION_INIT_DEFAULT_KEY", "ANNOTATION_INIT_KEY_LIST", "ANNOTATION_LIST", 
    "ANNOTATION_METHOD_DECL", "ANNOTATION_SCOPE", "ANNOTATION_TOP_LEVEL_SCOPE", 
    "ARGUMENT_LIST", "ARRAY_DECLARATOR", "ARRAY_DECLARATOR_LIST", "ARRAY_ELEMENT_ACCESS", 
    "ARRAY_INITIALIZER", "ASSERT", "ASSIGN", "AT", "BIT_SHIFT_RIGHT", "BIT_SHIFT_RIGHT_ASSIGN", 
    "BLOCK_SCOPE", "BOOLEAN", "BREAK", "BYTE", "CASE", "CAST_EXPR", "CATCH", 
    "CATCH_CLAUSE_LIST", "CHAR", "CHARACTER_LITERAL", "CLASS", "CLASS_CONSTRUCTOR_CALL", 
    "CLASS_INSTANCE_INITIALIZER", "CLASS_STATIC_INITIALIZER", "CLASS_TOP_LEVEL_SCOPE", 
    "COLON", "COMMA", "COMMENT", "CONSTRUCTOR_DECL", "CONTINUE", "DEC", 
    "DECIMAL_LITERAL", "DEFAULT", "DIV", "DIV_ASSIGN", "DO", "DOT", "DOTSTAR", 
    "DOUBLE", "ELLIPSIS", "ELSE", "ENUM", "ENUM_TOP_LEVEL_SCOPE", "EQUAL", 
    "ESCAPE_SEQUENCE", "EXPONENT", "EXPR", "EXTENDS", "EXTENDS_BOUND_LIST", 
    "EXTENDS_CLAUSE", "FALSE", "FINAL", "FINALLY", "FLOAT", "FLOATING_POINT_LITERAL", 
    "FLOAT_TYPE_SUFFIX", "FOR", "FORMAL_PARAM_LIST", "FORMAL_PARAM_STD_DECL", 
    "FORMAL_PARAM_VARARG_DECL", "FOR_CONDITION", "FOR_EACH", "FOR_INIT", 
    "FOR_UPDATE", "FUNCTION_METHOD_DECL", "GENERIC_TYPE_ARG_LIST", "GENERIC_TYPE_PARAM_LIST", 
    "GREATER_OR_EQUAL", "GREATER_THAN", "HEX_DIGIT", "HEX_LITERAL", "IDENT", 
    "IF", "IMPLEMENTS", "IMPLEMENTS_CLAUSE", "IMPORT", "INC", "INSTANCEOF", 
    "INT", "INTEGER_TYPE_SUFFIX", "INTERFACE", "INTERFACE_TOP_LEVEL_SCOPE", 
    "JAVA_ID_PART", "JAVA_ID_START", "JAVA_SOURCE", "LABELED_STATEMENT", 
    "LBRACK", "LCURLY", "LESS_OR_EQUAL", "LESS_THAN", "LINE_COMMENT", "LOCAL_MODIFIER_LIST", 
    "LOGICAL_AND", "LOGICAL_NOT", "LOGICAL_OR", "LONG", "LPAREN", "METHOD_CALL", 
    "MINUS", "MINUS_ASSIGN", "MOD", "MODIFIER_LIST", "MOD_ASSIGN", "NATIVE", 
    "NEW", "NOT", "NOT_EQUAL", "NULL", "OCTAL_ESCAPE", "OCTAL_LITERAL", 
    "OR", "OR_ASSIGN", "PACKAGE", "PARENTESIZED_EXPR", "PLUS", "PLUS_ASSIGN", 
    "POST_DEC", "POST_INC", "PRE_DEC", "PRE_INC", "PRIVATE", "PROTECTED", 
    "PUBLIC", "QUALIFIED_TYPE_IDENT", "QUESTION", "RBRACK", "RCURLY", "RETURN", 
    "RPAREN", "SEMI", "SHIFT_LEFT", "SHIFT_LEFT_ASSIGN", "SHIFT_RIGHT", 
    "SHIFT_RIGHT_ASSIGN", "SHORT", "STAR", "STAR_ASSIGN", "STATIC", "STATIC_ARRAY_CREATOR", 
    "STRICTFP", "STRING_LITERAL", "SUPER", "SUPER_CONSTRUCTOR_CALL", "SWITCH", 
    "SWITCH_BLOCK_LABEL_LIST", "SYNCHRONIZED", "THIS", "THIS_CONSTRUCTOR_CALL", 
    "THROW", "THROWS", "THROWS_CLAUSE", "TRANSIENT", "TRUE", "TRY", "TYPE", 
    "UNARY_MINUS", "UNARY_PLUS", "UNICODE_ESCAPE", "VAR_DECLARATION", "VAR_DECLARATOR", 
    "VAR_DECLARATOR_LIST", "VOID", "VOID_METHOD_DECL", "VOLATILE", "WHILE", 
    "WS", "XOR", "XOR_ASSIGN"
]




class JavaParser(Parser):
    grammarFileName = "Java.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(JavaParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class javaSource_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.javaSource_return, self).__init__()

            self.tree = None





    # $ANTLR start "javaSource"
    # Java.g:242:1: javaSource : compilationUnit -> ^( JAVA_SOURCE compilationUnit ) ;
    def javaSource(self, ):
        retval = self.javaSource_return()
        retval.start = self.input.LT(1)

        javaSource_StartIndex = self.input.index()

        root_0 = None

        compilationUnit1 = None


        stream_compilationUnit = RewriteRuleSubtreeStream(self._adaptor, "rule compilationUnit")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:243:5: ( compilationUnit -> ^( JAVA_SOURCE compilationUnit ) )
                # Java.g:243:9: compilationUnit
                pass 
                self._state.following.append(self.FOLLOW_compilationUnit_in_javaSource4489)
                compilationUnit1 = self.compilationUnit()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_compilationUnit.add(compilationUnit1.tree)


                # AST Rewrite
                # elements: compilationUnit
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 244:9: -> ^( JAVA_SOURCE compilationUnit )
                    # Java.g:244:13: ^( JAVA_SOURCE compilationUnit )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(JAVA_SOURCE, "JAVA_SOURCE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_compilationUnit.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, javaSource_StartIndex, success)


            pass
        return retval

    # $ANTLR end "javaSource"


    class compilationUnit_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.compilationUnit_return, self).__init__()

            self.tree = None





    # $ANTLR start "compilationUnit"
    # Java.g:247:1: compilationUnit : annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDecls )* ;
    def compilationUnit(self, ):
        retval = self.compilationUnit_return()
        retval.start = self.input.LT(1)

        compilationUnit_StartIndex = self.input.index()

        root_0 = None

        annotationList2 = None

        packageDeclaration3 = None

        importDeclaration4 = None

        typeDecls5 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:248:5: ( annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDecls )* )
                # Java.g:248:9: annotationList ( packageDeclaration )? ( importDeclaration )* ( typeDecls )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_annotationList_in_compilationUnit4525)
                annotationList2 = self.annotationList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationList2.tree)


                # Java.g:249:9: ( packageDeclaration )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == PACKAGE) :
                    alt1 = 1
                if alt1 == 1:
                    # Java.g:249:9: packageDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_packageDeclaration_in_compilationUnit4536)
                    packageDeclaration3 = self.packageDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, packageDeclaration3.tree)





                # Java.g:250:9: ( importDeclaration )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT) :
                        alt2 = 1


                    if alt2 == 1:
                        # Java.g:250:9: importDeclaration
                        pass 
                        self._state.following.append(self.FOLLOW_importDeclaration_in_compilationUnit4548)
                        importDeclaration4 = self.importDeclaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, importDeclaration4.tree)



                    else:
                        break #loop2


                # Java.g:251:9: ( typeDecls )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ABSTRACT or LA3_0 == AT or LA3_0 == BOOLEAN or LA3_0 == BYTE or LA3_0 == CHAR or LA3_0 == CLASS or LA3_0 == DOUBLE or LA3_0 == ENUM or LA3_0 == FINAL or LA3_0 == FLOAT or LA3_0 == IDENT or LA3_0 == INT or LA3_0 == INTERFACE or LA3_0 == LESS_THAN or LA3_0 == LONG or LA3_0 == NATIVE or (PRIVATE <= LA3_0 <= PUBLIC) or LA3_0 == SEMI or LA3_0 == SHORT or LA3_0 == STATIC or LA3_0 == STRICTFP or LA3_0 == SYNCHRONIZED or LA3_0 == TRANSIENT or LA3_0 == VOID or LA3_0 == VOLATILE) :
                        alt3 = 1


                    if alt3 == 1:
                        # Java.g:251:9: typeDecls
                        pass 
                        self._state.following.append(self.FOLLOW_typeDecls_in_compilationUnit4560)
                        typeDecls5 = self.typeDecls()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, typeDecls5.tree)



                    else:
                        break #loop3




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, compilationUnit_StartIndex, success)


            pass
        return retval

    # $ANTLR end "compilationUnit"


    class typeDecls_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.typeDecls_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeDecls"
    # Java.g:254:1: typeDecls : ( typeDeclaration | SEMI !);
    def typeDecls(self, ):
        retval = self.typeDecls_return()
        retval.start = self.input.LT(1)

        typeDecls_StartIndex = self.input.index()

        root_0 = None

        SEMI7 = None
        typeDeclaration6 = None


        SEMI7_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:255:5: ( typeDeclaration | SEMI !)
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == ABSTRACT or LA4_0 == AT or LA4_0 == BOOLEAN or LA4_0 == BYTE or LA4_0 == CHAR or LA4_0 == CLASS or LA4_0 == DOUBLE or LA4_0 == ENUM or LA4_0 == FINAL or LA4_0 == FLOAT or LA4_0 == IDENT or LA4_0 == INT or LA4_0 == INTERFACE or LA4_0 == LESS_THAN or LA4_0 == LONG or LA4_0 == NATIVE or (PRIVATE <= LA4_0 <= PUBLIC) or LA4_0 == SHORT or LA4_0 == STATIC or LA4_0 == STRICTFP or LA4_0 == SYNCHRONIZED or LA4_0 == TRANSIENT or LA4_0 == VOID or LA4_0 == VOLATILE) :
                    alt4 = 1
                elif (LA4_0 == SEMI) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # Java.g:255:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typeDeclaration_in_typeDecls4580)
                    typeDeclaration6 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration6.tree)



                elif alt4 == 2:
                    # Java.g:256:9: SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    SEMI7 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_typeDecls4590)


                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, typeDecls_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typeDecls"


    class packageDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.packageDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "packageDeclaration"
    # Java.g:259:1: packageDeclaration : PACKAGE ^ qualifiedIdentifier SEMI !;
    def packageDeclaration(self, ):
        retval = self.packageDeclaration_return()
        retval.start = self.input.LT(1)

        packageDeclaration_StartIndex = self.input.index()

        root_0 = None

        PACKAGE8 = None
        SEMI10 = None
        qualifiedIdentifier9 = None


        PACKAGE8_tree = None
        SEMI10_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:260:5: ( PACKAGE ^ qualifiedIdentifier SEMI !)
                # Java.g:260:9: PACKAGE ^ qualifiedIdentifier SEMI !
                pass 
                root_0 = self._adaptor.nil()


                PACKAGE8 = self.match(self.input, PACKAGE, self.FOLLOW_PACKAGE_in_packageDeclaration4610)
                if self._state.backtracking == 0:
                    PACKAGE8_tree = self._adaptor.createWithPayload(PACKAGE8)
                    root_0 = self._adaptor.becomeRoot(PACKAGE8_tree, root_0)



                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_packageDeclaration4613)
                qualifiedIdentifier9 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier9.tree)


                SEMI10 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_packageDeclaration4615)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, packageDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "packageDeclaration"


    class importDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.importDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "importDeclaration"
    # Java.g:263:1: importDeclaration : IMPORT ^ ( STATIC )? qualifiedIdentifier ( DOTSTAR )? SEMI !;
    def importDeclaration(self, ):
        retval = self.importDeclaration_return()
        retval.start = self.input.LT(1)

        importDeclaration_StartIndex = self.input.index()

        root_0 = None

        IMPORT11 = None
        STATIC12 = None
        DOTSTAR14 = None
        SEMI15 = None
        qualifiedIdentifier13 = None


        IMPORT11_tree = None
        STATIC12_tree = None
        DOTSTAR14_tree = None
        SEMI15_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:264:5: ( IMPORT ^ ( STATIC )? qualifiedIdentifier ( DOTSTAR )? SEMI !)
                # Java.g:264:9: IMPORT ^ ( STATIC )? qualifiedIdentifier ( DOTSTAR )? SEMI !
                pass 
                root_0 = self._adaptor.nil()


                IMPORT11 = self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importDeclaration4641)
                if self._state.backtracking == 0:
                    IMPORT11_tree = self._adaptor.createWithPayload(IMPORT11)
                    root_0 = self._adaptor.becomeRoot(IMPORT11_tree, root_0)



                # Java.g:264:17: ( STATIC )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == STATIC) :
                    alt5 = 1
                if alt5 == 1:
                    # Java.g:264:17: STATIC
                    pass 
                    STATIC12 = self.match(self.input, STATIC, self.FOLLOW_STATIC_in_importDeclaration4644)
                    if self._state.backtracking == 0:
                        STATIC12_tree = self._adaptor.createWithPayload(STATIC12)
                        self._adaptor.addChild(root_0, STATIC12_tree)






                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_importDeclaration4647)
                qualifiedIdentifier13 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier13.tree)


                # Java.g:264:45: ( DOTSTAR )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == DOTSTAR) :
                    alt6 = 1
                if alt6 == 1:
                    # Java.g:264:45: DOTSTAR
                    pass 
                    DOTSTAR14 = self.match(self.input, DOTSTAR, self.FOLLOW_DOTSTAR_in_importDeclaration4649)
                    if self._state.backtracking == 0:
                        DOTSTAR14_tree = self._adaptor.createWithPayload(DOTSTAR14)
                        self._adaptor.addChild(root_0, DOTSTAR14_tree)






                SEMI15 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_importDeclaration4652)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, importDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "importDeclaration"


    class typeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.typeDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeDeclaration"
    # Java.g:267:1: typeDeclaration : modifierList ! ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] ) ;
    def typeDeclaration(self, ):
        retval = self.typeDeclaration_return()
        retval.start = self.input.LT(1)

        typeDeclaration_StartIndex = self.input.index()

        root_0 = None

        modifierList16 = None

        classTypeDeclaration17 = None

        interfaceTypeDeclaration18 = None

        enumTypeDeclaration19 = None

        annotationTypeDeclaration20 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:268:5: ( modifierList ! ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] ) )
                # Java.g:268:9: modifierList ! ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] )
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_modifierList_in_typeDeclaration4676)
                modifierList16 = self.modifierList()

                self._state.following.pop()

                # Java.g:269:9: ( classTypeDeclaration[$modifierList.tree] | interfaceTypeDeclaration[$modifierList.tree] | enumTypeDeclaration[$modifierList.tree] | annotationTypeDeclaration[$modifierList.tree] )
                alt7 = 4
                LA7 = self.input.LA(1)
                if LA7 == CLASS:
                    alt7 = 1
                elif LA7 == INTERFACE:
                    alt7 = 2
                elif LA7 == ENUM:
                    alt7 = 3
                elif LA7 == AT:
                    alt7 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # Java.g:269:13: classTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_classTypeDeclaration_in_typeDeclaration4691)
                    classTypeDeclaration17 = self.classTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, classTypeDeclaration17.tree)



                elif alt7 == 2:
                    # Java.g:270:13: interfaceTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_interfaceTypeDeclaration_in_typeDeclaration4706)
                    interfaceTypeDeclaration18 = self.interfaceTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, interfaceTypeDeclaration18.tree)



                elif alt7 == 3:
                    # Java.g:271:13: enumTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_enumTypeDeclaration_in_typeDeclaration4721)
                    enumTypeDeclaration19 = self.enumTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enumTypeDeclaration19.tree)



                elif alt7 == 4:
                    # Java.g:272:13: annotationTypeDeclaration[$modifierList.tree]
                    pass 
                    self._state.following.append(self.FOLLOW_annotationTypeDeclaration_in_typeDeclaration4736)
                    annotationTypeDeclaration20 = self.annotationTypeDeclaration(modifierList16.tree)

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationTypeDeclaration20.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, typeDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typeDeclaration"


    class classTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.classTypeDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "classTypeDeclaration"
    # Java.g:276:1: classTypeDeclaration[CommonTree modifiers] : CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody -> ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody ) ;
    def classTypeDeclaration(self, modifiers): #(self, CommonTree modifiers)
        retval = self.classTypeDeclaration_return()
        retval.start = self.input.LT(1)

        classTypeDeclaration_StartIndex = self.input.index()

        root_0 = None

        CLASS21 = None
        IDENT22 = None
        genericTypeParameterList23 = None

        classExtendsClause24 = None

        implementsClause25 = None

        classBody26 = None


        CLASS21_tree = None
        IDENT22_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_classExtendsClause = RewriteRuleSubtreeStream(self._adaptor, "rule classExtendsClause")
        stream_implementsClause = RewriteRuleSubtreeStream(self._adaptor, "rule implementsClause")
        stream_classBody = RewriteRuleSubtreeStream(self._adaptor, "rule classBody")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:277:5: ( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody -> ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody ) )
                # Java.g:277:9: CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody
                pass 
                CLASS21 = self.match(self.input, CLASS, self.FOLLOW_CLASS_in_classTypeDeclaration4771) 
                if self._state.backtracking == 0:
                    stream_CLASS.add(CLASS21)


                IDENT22 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classTypeDeclaration4773) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT22)


                # Java.g:277:21: ( genericTypeParameterList )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == LESS_THAN) :
                    alt8 = 1
                if alt8 == 1:
                    # Java.g:277:21: genericTypeParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classTypeDeclaration4775)
                    genericTypeParameterList23 = self.genericTypeParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeParameterList.add(genericTypeParameterList23.tree)





                # Java.g:277:47: ( classExtendsClause )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == EXTENDS) :
                    alt9 = 1
                if alt9 == 1:
                    # Java.g:277:47: classExtendsClause
                    pass 
                    self._state.following.append(self.FOLLOW_classExtendsClause_in_classTypeDeclaration4778)
                    classExtendsClause24 = self.classExtendsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_classExtendsClause.add(classExtendsClause24.tree)





                # Java.g:277:67: ( implementsClause )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IMPLEMENTS) :
                    alt10 = 1
                if alt10 == 1:
                    # Java.g:277:67: implementsClause
                    pass 
                    self._state.following.append(self.FOLLOW_implementsClause_in_classTypeDeclaration4781)
                    implementsClause25 = self.implementsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_implementsClause.add(implementsClause25.tree)





                self._state.following.append(self.FOLLOW_classBody_in_classTypeDeclaration4784)
                classBody26 = self.classBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_classBody.add(classBody26.tree)


                # AST Rewrite
                # elements: CLASS, implementsClause, genericTypeParameterList, classBody, IDENT, classExtendsClause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 278:9: -> ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody )
                    # Java.g:278:13: ^( CLASS IDENT ( genericTypeParameterList )? ( classExtendsClause )? ( implementsClause )? classBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_CLASS.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, modifiers)

                    self._adaptor.addChild(root_1, 
                    stream_IDENT.nextNode()
                    )

                    # Java.g:278:40: ( genericTypeParameterList )?
                    if stream_genericTypeParameterList.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                    stream_genericTypeParameterList.reset();

                    # Java.g:278:66: ( classExtendsClause )?
                    if stream_classExtendsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_classExtendsClause.nextTree())


                    stream_classExtendsClause.reset();

                    # Java.g:278:86: ( implementsClause )?
                    if stream_implementsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_implementsClause.nextTree())


                    stream_implementsClause.reset();

                    self._adaptor.addChild(root_1, stream_classBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, classTypeDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "classTypeDeclaration"


    class classExtendsClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.classExtendsClause_return, self).__init__()

            self.tree = None





    # $ANTLR start "classExtendsClause"
    # Java.g:281:1: classExtendsClause : EXTENDS type -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type ) ;
    def classExtendsClause(self, ):
        retval = self.classExtendsClause_return()
        retval.start = self.input.LT(1)

        classExtendsClause_StartIndex = self.input.index()

        root_0 = None

        EXTENDS27 = None
        type28 = None


        EXTENDS27_tree = None
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:282:5: ( EXTENDS type -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type ) )
                # Java.g:282:9: EXTENDS type
                pass 
                EXTENDS27 = self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_classExtendsClause4837) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS27)


                self._state.following.append(self.FOLLOW_type_in_classExtendsClause4839)
                type28 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type28.tree)


                # AST Rewrite
                # elements: type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 283:9: -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type )
                    # Java.g:283:13: ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] type )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(EXTENDS_CLAUSE, EXTENDS27, "EXTENDS_CLAUSE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_type.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, classExtendsClause_StartIndex, success)


            pass
        return retval

    # $ANTLR end "classExtendsClause"


    class interfaceExtendsClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.interfaceExtendsClause_return, self).__init__()

            self.tree = None





    # $ANTLR start "interfaceExtendsClause"
    # Java.g:286:1: interfaceExtendsClause : EXTENDS typeList -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList ) ;
    def interfaceExtendsClause(self, ):
        retval = self.interfaceExtendsClause_return()
        retval.start = self.input.LT(1)

        interfaceExtendsClause_StartIndex = self.input.index()

        root_0 = None

        EXTENDS29 = None
        typeList30 = None


        EXTENDS29_tree = None
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_typeList = RewriteRuleSubtreeStream(self._adaptor, "rule typeList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:287:5: ( EXTENDS typeList -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList ) )
                # Java.g:287:9: EXTENDS typeList
                pass 
                EXTENDS29 = self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_interfaceExtendsClause4883) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS29)


                self._state.following.append(self.FOLLOW_typeList_in_interfaceExtendsClause4885)
                typeList30 = self.typeList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeList.add(typeList30.tree)


                # AST Rewrite
                # elements: typeList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 288:9: -> ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList )
                    # Java.g:288:13: ^( EXTENDS_CLAUSE[$EXTENDS, \"EXTENDS_CLAUSE\"] typeList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(EXTENDS_CLAUSE, EXTENDS29, "EXTENDS_CLAUSE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_typeList.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, interfaceExtendsClause_StartIndex, success)


            pass
        return retval

    # $ANTLR end "interfaceExtendsClause"


    class implementsClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.implementsClause_return, self).__init__()

            self.tree = None





    # $ANTLR start "implementsClause"
    # Java.g:291:1: implementsClause : IMPLEMENTS typeList -> ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList ) ;
    def implementsClause(self, ):
        retval = self.implementsClause_return()
        retval.start = self.input.LT(1)

        implementsClause_StartIndex = self.input.index()

        root_0 = None

        IMPLEMENTS31 = None
        typeList32 = None


        IMPLEMENTS31_tree = None
        stream_IMPLEMENTS = RewriteRuleTokenStream(self._adaptor, "token IMPLEMENTS")
        stream_typeList = RewriteRuleSubtreeStream(self._adaptor, "rule typeList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:292:5: ( IMPLEMENTS typeList -> ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList ) )
                # Java.g:292:9: IMPLEMENTS typeList
                pass 
                IMPLEMENTS31 = self.match(self.input, IMPLEMENTS, self.FOLLOW_IMPLEMENTS_in_implementsClause4929) 
                if self._state.backtracking == 0:
                    stream_IMPLEMENTS.add(IMPLEMENTS31)


                self._state.following.append(self.FOLLOW_typeList_in_implementsClause4931)
                typeList32 = self.typeList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeList.add(typeList32.tree)


                # AST Rewrite
                # elements: typeList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 293:9: -> ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList )
                    # Java.g:293:13: ^( IMPLEMENTS_CLAUSE[$IMPLEMENTS, \"IMPLEMENTS_CLAUSE\"] typeList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(IMPLEMENTS_CLAUSE, IMPLEMENTS31, "IMPLEMENTS_CLAUSE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_typeList.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, implementsClause_StartIndex, success)


            pass
        return retval

    # $ANTLR end "implementsClause"


    class genericTypeParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeParameterList_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeParameterList"
    # Java.g:296:1: genericTypeParameterList : LESS_THAN genericTypeParameter ( COMMA genericTypeParameter )* genericTypeListClosing -> ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ ) ;
    def genericTypeParameterList(self, ):
        retval = self.genericTypeParameterList_return()
        retval.start = self.input.LT(1)

        genericTypeParameterList_StartIndex = self.input.index()

        root_0 = None

        LESS_THAN33 = None
        COMMA35 = None
        genericTypeParameter34 = None

        genericTypeParameter36 = None

        genericTypeListClosing37 = None


        LESS_THAN33_tree = None
        COMMA35_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LESS_THAN = RewriteRuleTokenStream(self._adaptor, "token LESS_THAN")
        stream_genericTypeParameter = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameter")
        stream_genericTypeListClosing = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeListClosing")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:297:5: ( LESS_THAN genericTypeParameter ( COMMA genericTypeParameter )* genericTypeListClosing -> ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ ) )
                # Java.g:297:9: LESS_THAN genericTypeParameter ( COMMA genericTypeParameter )* genericTypeListClosing
                pass 
                LESS_THAN33 = self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_genericTypeParameterList4976) 
                if self._state.backtracking == 0:
                    stream_LESS_THAN.add(LESS_THAN33)


                self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList4978)
                genericTypeParameter34 = self.genericTypeParameter()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeParameter.add(genericTypeParameter34.tree)


                # Java.g:297:40: ( COMMA genericTypeParameter )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == COMMA) :
                        alt11 = 1


                    if alt11 == 1:
                        # Java.g:297:41: COMMA genericTypeParameter
                        pass 
                        COMMA35 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_genericTypeParameterList4981) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA35)


                        self._state.following.append(self.FOLLOW_genericTypeParameter_in_genericTypeParameterList4983)
                        genericTypeParameter36 = self.genericTypeParameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeParameter.add(genericTypeParameter36.tree)



                    else:
                        break #loop11


                self._state.following.append(self.FOLLOW_genericTypeListClosing_in_genericTypeParameterList4987)
                genericTypeListClosing37 = self.genericTypeListClosing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeListClosing.add(genericTypeListClosing37.tree)


                # AST Rewrite
                # elements: genericTypeParameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 298:9: -> ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ )
                    # Java.g:298:13: ^( GENERIC_TYPE_PARAM_LIST[$LESS_THAN, \"GENERIC_TYPE_PARAM_LIST\"] ( genericTypeParameter )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(GENERIC_TYPE_PARAM_LIST, LESS_THAN33, "GENERIC_TYPE_PARAM_LIST")
                    , root_1)

                    # Java.g:298:78: ( genericTypeParameter )+
                    if not (stream_genericTypeParameter.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_genericTypeParameter.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeParameter.nextTree())


                    stream_genericTypeParameter.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, genericTypeParameterList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeParameterList"


    class genericTypeListClosing_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeListClosing_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeListClosing"
    # Java.g:301:1: genericTypeListClosing : ( GREATER_THAN | SHIFT_RIGHT | BIT_SHIFT_RIGHT |);
    def genericTypeListClosing(self, ):
        retval = self.genericTypeListClosing_return()
        retval.start = self.input.LT(1)

        genericTypeListClosing_StartIndex = self.input.index()

        root_0 = None

        GREATER_THAN38 = None
        SHIFT_RIGHT39 = None
        BIT_SHIFT_RIGHT40 = None

        GREATER_THAN38_tree = None
        SHIFT_RIGHT39_tree = None
        BIT_SHIFT_RIGHT40_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:305:5: ( GREATER_THAN | SHIFT_RIGHT | BIT_SHIFT_RIGHT |)
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == GREATER_THAN:
                    LA12_1 = self.input.LA(2)

                    if (self.synpred14_Java()) :
                        alt12 = 1
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 12, 1, self.input)

                        raise nvae


                elif LA12 == SHIFT_RIGHT:
                    LA12_2 = self.input.LA(2)

                    if (self.synpred15_Java()) :
                        alt12 = 2
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 12, 2, self.input)

                        raise nvae


                elif LA12 == BIT_SHIFT_RIGHT:
                    LA12_3 = self.input.LA(2)

                    if (self.synpred16_Java()) :
                        alt12 = 3
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 12, 3, self.input)

                        raise nvae


                elif LA12 == EOF or LA12 == AND or LA12 == AND_ASSIGN or LA12 == ASSIGN or LA12 == BIT_SHIFT_RIGHT_ASSIGN or LA12 == BOOLEAN or LA12 == BYTE or LA12 == CHAR or LA12 == COLON or LA12 == COMMA or LA12 == DIV_ASSIGN or LA12 == DOT or LA12 == DOUBLE or LA12 == ELLIPSIS or LA12 == EQUAL or LA12 == EXTENDS or LA12 == FLOAT or LA12 == IDENT or LA12 == IMPLEMENTS or LA12 == INT or LA12 == LBRACK or LA12 == LCURLY or LA12 == LOGICAL_AND or LA12 == LOGICAL_OR or LA12 == LONG or LA12 == LPAREN or LA12 == MINUS_ASSIGN or LA12 == MOD_ASSIGN or LA12 == NOT_EQUAL or LA12 == OR or LA12 == OR_ASSIGN or LA12 == PLUS_ASSIGN or LA12 == QUESTION or LA12 == RBRACK or LA12 == RCURLY or LA12 == RPAREN or LA12 == SEMI or LA12 == SHIFT_LEFT_ASSIGN or LA12 == SHIFT_RIGHT_ASSIGN or LA12 == SHORT or LA12 == STAR_ASSIGN or LA12 == SUPER or LA12 == THIS or LA12 == VOID or LA12 == XOR or LA12 == XOR_ASSIGN:
                    alt12 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # Java.g:305:9: GREATER_THAN
                    pass 
                    root_0 = self._adaptor.nil()


                    GREATER_THAN38 = self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_genericTypeListClosing5102)
                    if self._state.backtracking == 0:
                        GREATER_THAN38_tree = self._adaptor.createWithPayload(GREATER_THAN38)
                        self._adaptor.addChild(root_0, GREATER_THAN38_tree)




                elif alt12 == 2:
                    # Java.g:306:9: SHIFT_RIGHT
                    pass 
                    root_0 = self._adaptor.nil()


                    SHIFT_RIGHT39 = self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_genericTypeListClosing5112)
                    if self._state.backtracking == 0:
                        SHIFT_RIGHT39_tree = self._adaptor.createWithPayload(SHIFT_RIGHT39)
                        self._adaptor.addChild(root_0, SHIFT_RIGHT39_tree)




                elif alt12 == 3:
                    # Java.g:307:9: BIT_SHIFT_RIGHT
                    pass 
                    root_0 = self._adaptor.nil()


                    BIT_SHIFT_RIGHT40 = self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_genericTypeListClosing5122)
                    if self._state.backtracking == 0:
                        BIT_SHIFT_RIGHT40_tree = self._adaptor.createWithPayload(BIT_SHIFT_RIGHT40)
                        self._adaptor.addChild(root_0, BIT_SHIFT_RIGHT40_tree)




                elif alt12 == 4:
                    # Java.g:309:5: 
                    pass 
                    root_0 = self._adaptor.nil()



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, genericTypeListClosing_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeListClosing"


    class genericTypeParameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeParameter_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeParameter"
    # Java.g:311:1: genericTypeParameter : IDENT ( bound )? -> ^( IDENT ( bound )? ) ;
    def genericTypeParameter(self, ):
        retval = self.genericTypeParameter_return()
        retval.start = self.input.LT(1)

        genericTypeParameter_StartIndex = self.input.index()

        root_0 = None

        IDENT41 = None
        bound42 = None


        IDENT41_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_bound = RewriteRuleSubtreeStream(self._adaptor, "rule bound")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:312:5: ( IDENT ( bound )? -> ^( IDENT ( bound )? ) )
                # Java.g:312:9: IDENT ( bound )?
                pass 
                IDENT41 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_genericTypeParameter5150) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT41)


                # Java.g:312:15: ( bound )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == EXTENDS) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == BOOLEAN or LA13_1 == BYTE or LA13_1 == CHAR or LA13_1 == DOUBLE or LA13_1 == FLOAT or LA13_1 == INT or LA13_1 == LONG or LA13_1 == SHORT) :
                        LA13_3 = self.input.LA(3)

                        if (self.synpred17_Java()) :
                            alt13 = 1
                    elif (LA13_1 == IDENT) :
                        LA13_4 = self.input.LA(3)

                        if (self.synpred17_Java()) :
                            alt13 = 1
                if alt13 == 1:
                    # Java.g:312:15: bound
                    pass 
                    self._state.following.append(self.FOLLOW_bound_in_genericTypeParameter5152)
                    bound42 = self.bound()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_bound.add(bound42.tree)





                # AST Rewrite
                # elements: IDENT, bound
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 313:9: -> ^( IDENT ( bound )? )
                    # Java.g:313:13: ^( IDENT ( bound )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_IDENT.nextNode()
                    , root_1)

                    # Java.g:313:21: ( bound )?
                    if stream_bound.hasNext():
                        self._adaptor.addChild(root_1, stream_bound.nextTree())


                    stream_bound.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 13, genericTypeParameter_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeParameter"


    class bound_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.bound_return, self).__init__()

            self.tree = None





    # $ANTLR start "bound"
    # Java.g:316:1: bound : EXTENDS type ( AND type )* -> ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ ) ;
    def bound(self, ):
        retval = self.bound_return()
        retval.start = self.input.LT(1)

        bound_StartIndex = self.input.index()

        root_0 = None

        EXTENDS43 = None
        AND45 = None
        type44 = None

        type46 = None


        EXTENDS43_tree = None
        AND45_tree = None
        stream_AND = RewriteRuleTokenStream(self._adaptor, "token AND")
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:317:5: ( EXTENDS type ( AND type )* -> ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ ) )
                # Java.g:317:9: EXTENDS type ( AND type )*
                pass 
                EXTENDS43 = self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_bound5198) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS43)


                self._state.following.append(self.FOLLOW_type_in_bound5200)
                type44 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type44.tree)


                # Java.g:317:22: ( AND type )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == AND) :
                        alt14 = 1


                    if alt14 == 1:
                        # Java.g:317:23: AND type
                        pass 
                        AND45 = self.match(self.input, AND, self.FOLLOW_AND_in_bound5203) 
                        if self._state.backtracking == 0:
                            stream_AND.add(AND45)


                        self._state.following.append(self.FOLLOW_type_in_bound5205)
                        type46 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type46.tree)



                    else:
                        break #loop14


                # AST Rewrite
                # elements: type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 318:9: -> ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ )
                    # Java.g:318:13: ^( EXTENDS_BOUND_LIST[$EXTENDS, \"EXTENDS_BOUND_LIST\"] ( type )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(EXTENDS_BOUND_LIST, EXTENDS43, "EXTENDS_BOUND_LIST")
                    , root_1)

                    # Java.g:318:66: ( type )+
                    if not (stream_type.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_type.hasNext():
                        self._adaptor.addChild(root_1, stream_type.nextTree())


                    stream_type.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 14, bound_StartIndex, success)


            pass
        return retval

    # $ANTLR end "bound"


    class enumTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.enumTypeDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "enumTypeDeclaration"
    # Java.g:321:1: enumTypeDeclaration[CommonTree modifiers] : ENUM IDENT ( implementsClause )? enumBody -> ^( ENUM IDENT ( implementsClause )? enumBody ) ;
    def enumTypeDeclaration(self, modifiers): #(self, CommonTree modifiers)
        retval = self.enumTypeDeclaration_return()
        retval.start = self.input.LT(1)

        enumTypeDeclaration_StartIndex = self.input.index()

        root_0 = None

        ENUM47 = None
        IDENT48 = None
        implementsClause49 = None

        enumBody50 = None


        ENUM47_tree = None
        IDENT48_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_ENUM = RewriteRuleTokenStream(self._adaptor, "token ENUM")
        stream_implementsClause = RewriteRuleSubtreeStream(self._adaptor, "rule implementsClause")
        stream_enumBody = RewriteRuleSubtreeStream(self._adaptor, "rule enumBody")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:322:5: ( ENUM IDENT ( implementsClause )? enumBody -> ^( ENUM IDENT ( implementsClause )? enumBody ) )
                # Java.g:322:9: ENUM IDENT ( implementsClause )? enumBody
                pass 
                ENUM47 = self.match(self.input, ENUM, self.FOLLOW_ENUM_in_enumTypeDeclaration5246) 
                if self._state.backtracking == 0:
                    stream_ENUM.add(ENUM47)


                IDENT48 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumTypeDeclaration5248) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT48)


                # Java.g:322:20: ( implementsClause )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IMPLEMENTS) :
                    alt15 = 1
                if alt15 == 1:
                    # Java.g:322:20: implementsClause
                    pass 
                    self._state.following.append(self.FOLLOW_implementsClause_in_enumTypeDeclaration5250)
                    implementsClause49 = self.implementsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_implementsClause.add(implementsClause49.tree)





                self._state.following.append(self.FOLLOW_enumBody_in_enumTypeDeclaration5253)
                enumBody50 = self.enumBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_enumBody.add(enumBody50.tree)


                # AST Rewrite
                # elements: IDENT, enumBody, implementsClause, ENUM
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 323:9: -> ^( ENUM IDENT ( implementsClause )? enumBody )
                    # Java.g:323:13: ^( ENUM IDENT ( implementsClause )? enumBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_ENUM.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, modifiers)

                    self._adaptor.addChild(root_1, 
                    stream_IDENT.nextNode()
                    )

                    # Java.g:323:39: ( implementsClause )?
                    if stream_implementsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_implementsClause.nextTree())


                    stream_implementsClause.reset();

                    self._adaptor.addChild(root_1, stream_enumBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 15, enumTypeDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "enumTypeDeclaration"


    class enumBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.enumBody_return, self).__init__()

            self.tree = None





    # $ANTLR start "enumBody"
    # Java.g:326:1: enumBody : LCURLY enumScopeDeclarations RCURLY -> ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations ) ;
    def enumBody(self, ):
        retval = self.enumBody_return()
        retval.start = self.input.LT(1)

        enumBody_StartIndex = self.input.index()

        root_0 = None

        LCURLY51 = None
        RCURLY53 = None
        enumScopeDeclarations52 = None


        LCURLY51_tree = None
        RCURLY53_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_enumScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule enumScopeDeclarations")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:327:5: ( LCURLY enumScopeDeclarations RCURLY -> ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations ) )
                # Java.g:327:9: LCURLY enumScopeDeclarations RCURLY
                pass 
                LCURLY51 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_enumBody5300) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY51)


                self._state.following.append(self.FOLLOW_enumScopeDeclarations_in_enumBody5302)
                enumScopeDeclarations52 = self.enumScopeDeclarations()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_enumScopeDeclarations.add(enumScopeDeclarations52.tree)


                RCURLY53 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_enumBody5304) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY53)


                # AST Rewrite
                # elements: enumScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 328:9: -> ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations )
                    # Java.g:328:13: ^( ENUM_TOP_LEVEL_SCOPE[$LCURLY, \"ENUM_TOP_LEVEL_SCOPE\"] enumScopeDeclarations )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(ENUM_TOP_LEVEL_SCOPE, LCURLY51, "ENUM_TOP_LEVEL_SCOPE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_enumScopeDeclarations.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 16, enumBody_StartIndex, success)


            pass
        return retval

    # $ANTLR end "enumBody"


    class enumScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.enumScopeDeclarations_return, self).__init__()

            self.tree = None





    # $ANTLR start "enumScopeDeclarations"
    # Java.g:331:1: enumScopeDeclarations : enumConstants ( COMMA !)? ( enumClassScopeDeclarations )? ;
    def enumScopeDeclarations(self, ):
        retval = self.enumScopeDeclarations_return()
        retval.start = self.input.LT(1)

        enumScopeDeclarations_StartIndex = self.input.index()

        root_0 = None

        COMMA55 = None
        enumConstants54 = None

        enumClassScopeDeclarations56 = None


        COMMA55_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:332:5: ( enumConstants ( COMMA !)? ( enumClassScopeDeclarations )? )
                # Java.g:332:9: enumConstants ( COMMA !)? ( enumClassScopeDeclarations )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_enumConstants_in_enumScopeDeclarations5341)
                enumConstants54 = self.enumConstants()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, enumConstants54.tree)


                # Java.g:332:23: ( COMMA !)?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == COMMA) :
                    alt16 = 1
                if alt16 == 1:
                    # Java.g:332:24: COMMA !
                    pass 
                    COMMA55 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_enumScopeDeclarations5344)




                # Java.g:332:33: ( enumClassScopeDeclarations )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == SEMI) :
                    alt17 = 1
                if alt17 == 1:
                    # Java.g:332:33: enumClassScopeDeclarations
                    pass 
                    self._state.following.append(self.FOLLOW_enumClassScopeDeclarations_in_enumScopeDeclarations5349)
                    enumClassScopeDeclarations56 = self.enumClassScopeDeclarations()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enumClassScopeDeclarations56.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 17, enumScopeDeclarations_StartIndex, success)


            pass
        return retval

    # $ANTLR end "enumScopeDeclarations"


    class enumClassScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.enumClassScopeDeclarations_return, self).__init__()

            self.tree = None





    # $ANTLR start "enumClassScopeDeclarations"
    # Java.g:335:1: enumClassScopeDeclarations : SEMI ( classScopeDeclarations )* -> ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) ;
    def enumClassScopeDeclarations(self, ):
        retval = self.enumClassScopeDeclarations_return()
        retval.start = self.input.LT(1)

        enumClassScopeDeclarations_StartIndex = self.input.index()

        root_0 = None

        SEMI57 = None
        classScopeDeclarations58 = None


        SEMI57_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_classScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule classScopeDeclarations")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:336:5: ( SEMI ( classScopeDeclarations )* -> ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) )
                # Java.g:336:9: SEMI ( classScopeDeclarations )*
                pass 
                SEMI57 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_enumClassScopeDeclarations5369) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI57)


                # Java.g:336:14: ( classScopeDeclarations )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == ABSTRACT or LA18_0 == AT or LA18_0 == BOOLEAN or LA18_0 == BYTE or LA18_0 == CHAR or LA18_0 == CLASS or LA18_0 == DOUBLE or LA18_0 == ENUM or LA18_0 == FINAL or LA18_0 == FLOAT or LA18_0 == IDENT or LA18_0 == INT or LA18_0 == INTERFACE or LA18_0 == LCURLY or LA18_0 == LESS_THAN or LA18_0 == LONG or LA18_0 == NATIVE or (PRIVATE <= LA18_0 <= PUBLIC) or LA18_0 == SEMI or LA18_0 == SHORT or LA18_0 == STATIC or LA18_0 == STRICTFP or LA18_0 == SYNCHRONIZED or LA18_0 == TRANSIENT or LA18_0 == VOID or LA18_0 == VOLATILE) :
                        alt18 = 1


                    if alt18 == 1:
                        # Java.g:336:14: classScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_classScopeDeclarations_in_enumClassScopeDeclarations5371)
                        classScopeDeclarations58 = self.classScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classScopeDeclarations.add(classScopeDeclarations58.tree)



                    else:
                        break #loop18


                # AST Rewrite
                # elements: classScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 337:9: -> ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    # Java.g:337:13: ^( CLASS_TOP_LEVEL_SCOPE[$SEMI, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(CLASS_TOP_LEVEL_SCOPE, SEMI57, "CLASS_TOP_LEVEL_SCOPE")
                    , root_1)

                    # Java.g:337:69: ( classScopeDeclarations )*
                    while stream_classScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_classScopeDeclarations.nextTree())


                    stream_classScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 18, enumClassScopeDeclarations_StartIndex, success)


            pass
        return retval

    # $ANTLR end "enumClassScopeDeclarations"


    class enumConstants_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.enumConstants_return, self).__init__()

            self.tree = None





    # $ANTLR start "enumConstants"
    # Java.g:340:1: enumConstants : enumConstant ( COMMA ! enumConstant )* ;
    def enumConstants(self, ):
        retval = self.enumConstants_return()
        retval.start = self.input.LT(1)

        enumConstants_StartIndex = self.input.index()

        root_0 = None

        COMMA60 = None
        enumConstant59 = None

        enumConstant61 = None


        COMMA60_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:341:5: ( enumConstant ( COMMA ! enumConstant )* )
                # Java.g:341:9: enumConstant ( COMMA ! enumConstant )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_enumConstant_in_enumConstants5410)
                enumConstant59 = self.enumConstant()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, enumConstant59.tree)


                # Java.g:341:22: ( COMMA ! enumConstant )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == COMMA) :
                        LA19_1 = self.input.LA(2)

                        if (LA19_1 == AT or LA19_1 == IDENT) :
                            alt19 = 1




                    if alt19 == 1:
                        # Java.g:341:23: COMMA ! enumConstant
                        pass 
                        COMMA60 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_enumConstants5413)

                        self._state.following.append(self.FOLLOW_enumConstant_in_enumConstants5416)
                        enumConstant61 = self.enumConstant()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, enumConstant61.tree)



                    else:
                        break #loop19




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 19, enumConstants_StartIndex, success)


            pass
        return retval

    # $ANTLR end "enumConstants"


    class enumConstant_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.enumConstant_return, self).__init__()

            self.tree = None





    # $ANTLR start "enumConstant"
    # Java.g:344:1: enumConstant : annotationList IDENT ^ ( arguments )? ( classBody )? ;
    def enumConstant(self, ):
        retval = self.enumConstant_return()
        retval.start = self.input.LT(1)

        enumConstant_StartIndex = self.input.index()

        root_0 = None

        IDENT63 = None
        annotationList62 = None

        arguments64 = None

        classBody65 = None


        IDENT63_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:345:5: ( annotationList IDENT ^ ( arguments )? ( classBody )? )
                # Java.g:345:9: annotationList IDENT ^ ( arguments )? ( classBody )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_annotationList_in_enumConstant5441)
                annotationList62 = self.annotationList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationList62.tree)


                IDENT63 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_enumConstant5443)
                if self._state.backtracking == 0:
                    IDENT63_tree = self._adaptor.createWithPayload(IDENT63)
                    root_0 = self._adaptor.becomeRoot(IDENT63_tree, root_0)



                # Java.g:345:31: ( arguments )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == LPAREN) :
                    alt20 = 1
                if alt20 == 1:
                    # Java.g:345:31: arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_enumConstant5446)
                    arguments64 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arguments64.tree)





                # Java.g:345:42: ( classBody )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == LCURLY) :
                    alt21 = 1
                if alt21 == 1:
                    # Java.g:345:42: classBody
                    pass 
                    self._state.following.append(self.FOLLOW_classBody_in_enumConstant5449)
                    classBody65 = self.classBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, classBody65.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 20, enumConstant_StartIndex, success)


            pass
        return retval

    # $ANTLR end "enumConstant"


    class interfaceTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.interfaceTypeDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "interfaceTypeDeclaration"
    # Java.g:348:1: interfaceTypeDeclaration[CommonTree modifiers] : INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody -> ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody ) ;
    def interfaceTypeDeclaration(self, modifiers): #(self, CommonTree modifiers)
        retval = self.interfaceTypeDeclaration_return()
        retval.start = self.input.LT(1)

        interfaceTypeDeclaration_StartIndex = self.input.index()

        root_0 = None

        INTERFACE66 = None
        IDENT67 = None
        genericTypeParameterList68 = None

        interfaceExtendsClause69 = None

        interfaceBody70 = None


        INTERFACE66_tree = None
        IDENT67_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_INTERFACE = RewriteRuleTokenStream(self._adaptor, "token INTERFACE")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_interfaceBody = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceBody")
        stream_interfaceExtendsClause = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceExtendsClause")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:349:5: ( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody -> ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody ) )
                # Java.g:349:9: INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody
                pass 
                INTERFACE66 = self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_interfaceTypeDeclaration5474) 
                if self._state.backtracking == 0:
                    stream_INTERFACE.add(INTERFACE66)


                IDENT67 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceTypeDeclaration5476) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT67)


                # Java.g:349:25: ( genericTypeParameterList )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == LESS_THAN) :
                    alt22 = 1
                if alt22 == 1:
                    # Java.g:349:25: genericTypeParameterList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceTypeDeclaration5478)
                    genericTypeParameterList68 = self.genericTypeParameterList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeParameterList.add(genericTypeParameterList68.tree)





                # Java.g:349:51: ( interfaceExtendsClause )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == EXTENDS) :
                    alt23 = 1
                if alt23 == 1:
                    # Java.g:349:51: interfaceExtendsClause
                    pass 
                    self._state.following.append(self.FOLLOW_interfaceExtendsClause_in_interfaceTypeDeclaration5481)
                    interfaceExtendsClause69 = self.interfaceExtendsClause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_interfaceExtendsClause.add(interfaceExtendsClause69.tree)





                self._state.following.append(self.FOLLOW_interfaceBody_in_interfaceTypeDeclaration5484)
                interfaceBody70 = self.interfaceBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_interfaceBody.add(interfaceBody70.tree)


                # AST Rewrite
                # elements: INTERFACE, interfaceExtendsClause, genericTypeParameterList, IDENT, interfaceBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 350:9: -> ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody )
                    # Java.g:350:13: ^( INTERFACE IDENT ( genericTypeParameterList )? ( interfaceExtendsClause )? interfaceBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_INTERFACE.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, modifiers)

                    self._adaptor.addChild(root_1, 
                    stream_IDENT.nextNode()
                    )

                    # Java.g:350:44: ( genericTypeParameterList )?
                    if stream_genericTypeParameterList.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                    stream_genericTypeParameterList.reset();

                    # Java.g:350:70: ( interfaceExtendsClause )?
                    if stream_interfaceExtendsClause.hasNext():
                        self._adaptor.addChild(root_1, stream_interfaceExtendsClause.nextTree())


                    stream_interfaceExtendsClause.reset();

                    self._adaptor.addChild(root_1, stream_interfaceBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 21, interfaceTypeDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "interfaceTypeDeclaration"


    class typeList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.typeList_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeList"
    # Java.g:353:1: typeList : type ( COMMA ! type )* ;
    def typeList(self, ):
        retval = self.typeList_return()
        retval.start = self.input.LT(1)

        typeList_StartIndex = self.input.index()

        root_0 = None

        COMMA72 = None
        type71 = None

        type73 = None


        COMMA72_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:354:5: ( type ( COMMA ! type )* )
                # Java.g:354:9: type ( COMMA ! type )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_type_in_typeList5534)
                type71 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, type71.tree)


                # Java.g:354:14: ( COMMA ! type )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # Java.g:354:15: COMMA ! type
                        pass 
                        COMMA72 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_typeList5537)

                        self._state.following.append(self.FOLLOW_type_in_typeList5540)
                        type73 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, type73.tree)



                    else:
                        break #loop24




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 22, typeList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typeList"


    class classBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.classBody_return, self).__init__()

            self.tree = None





    # $ANTLR start "classBody"
    # Java.g:357:1: classBody : LCURLY ( classScopeDeclarations )* RCURLY -> ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) ;
    def classBody(self, ):
        retval = self.classBody_return()
        retval.start = self.input.LT(1)

        classBody_StartIndex = self.input.index()

        root_0 = None

        LCURLY74 = None
        RCURLY76 = None
        classScopeDeclarations75 = None


        LCURLY74_tree = None
        RCURLY76_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_classScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule classScopeDeclarations")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:358:5: ( LCURLY ( classScopeDeclarations )* RCURLY -> ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* ) )
                # Java.g:358:9: LCURLY ( classScopeDeclarations )* RCURLY
                pass 
                LCURLY74 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_classBody5565) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY74)


                # Java.g:358:16: ( classScopeDeclarations )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ABSTRACT or LA25_0 == AT or LA25_0 == BOOLEAN or LA25_0 == BYTE or LA25_0 == CHAR or LA25_0 == CLASS or LA25_0 == DOUBLE or LA25_0 == ENUM or LA25_0 == FINAL or LA25_0 == FLOAT or LA25_0 == IDENT or LA25_0 == INT or LA25_0 == INTERFACE or LA25_0 == LCURLY or LA25_0 == LESS_THAN or LA25_0 == LONG or LA25_0 == NATIVE or (PRIVATE <= LA25_0 <= PUBLIC) or LA25_0 == SEMI or LA25_0 == SHORT or LA25_0 == STATIC or LA25_0 == STRICTFP or LA25_0 == SYNCHRONIZED or LA25_0 == TRANSIENT or LA25_0 == VOID or LA25_0 == VOLATILE) :
                        alt25 = 1


                    if alt25 == 1:
                        # Java.g:358:16: classScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_classScopeDeclarations_in_classBody5567)
                        classScopeDeclarations75 = self.classScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classScopeDeclarations.add(classScopeDeclarations75.tree)



                    else:
                        break #loop25


                RCURLY76 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_classBody5570) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY76)


                # AST Rewrite
                # elements: classScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 359:9: -> ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    # Java.g:359:13: ^( CLASS_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( classScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(CLASS_TOP_LEVEL_SCOPE, LCURLY74, "CLASS_TOP_LEVEL_SCOPE")
                    , root_1)

                    # Java.g:359:71: ( classScopeDeclarations )*
                    while stream_classScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_classScopeDeclarations.nextTree())


                    stream_classScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 23, classBody_StartIndex, success)


            pass
        return retval

    # $ANTLR end "classBody"


    class interfaceBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.interfaceBody_return, self).__init__()

            self.tree = None





    # $ANTLR start "interfaceBody"
    # Java.g:362:1: interfaceBody : LCURLY ( interfaceScopeDeclarations )* RCURLY -> ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* ) ;
    def interfaceBody(self, ):
        retval = self.interfaceBody_return()
        retval.start = self.input.LT(1)

        interfaceBody_StartIndex = self.input.index()

        root_0 = None

        LCURLY77 = None
        RCURLY79 = None
        interfaceScopeDeclarations78 = None


        LCURLY77_tree = None
        RCURLY79_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_interfaceScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceScopeDeclarations")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:363:5: ( LCURLY ( interfaceScopeDeclarations )* RCURLY -> ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* ) )
                # Java.g:363:9: LCURLY ( interfaceScopeDeclarations )* RCURLY
                pass 
                LCURLY77 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_interfaceBody5612) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY77)


                # Java.g:363:16: ( interfaceScopeDeclarations )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ABSTRACT or LA26_0 == AT or LA26_0 == BOOLEAN or LA26_0 == BYTE or LA26_0 == CHAR or LA26_0 == CLASS or LA26_0 == DOUBLE or LA26_0 == ENUM or LA26_0 == FINAL or LA26_0 == FLOAT or LA26_0 == IDENT or LA26_0 == INT or LA26_0 == INTERFACE or LA26_0 == LESS_THAN or LA26_0 == LONG or LA26_0 == NATIVE or (PRIVATE <= LA26_0 <= PUBLIC) or LA26_0 == SEMI or LA26_0 == SHORT or LA26_0 == STATIC or LA26_0 == STRICTFP or LA26_0 == SYNCHRONIZED or LA26_0 == TRANSIENT or LA26_0 == VOID or LA26_0 == VOLATILE) :
                        alt26 = 1


                    if alt26 == 1:
                        # Java.g:363:16: interfaceScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_interfaceScopeDeclarations_in_interfaceBody5614)
                        interfaceScopeDeclarations78 = self.interfaceScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_interfaceScopeDeclarations.add(interfaceScopeDeclarations78.tree)



                    else:
                        break #loop26


                RCURLY79 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_interfaceBody5617) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY79)


                # AST Rewrite
                # elements: interfaceScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 364:9: -> ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* )
                    # Java.g:364:13: ^( INTERFACE_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( interfaceScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(INTERFACE_TOP_LEVEL_SCOPE, LCURLY77, "CLASS_TOP_LEVEL_SCOPE")
                    , root_1)

                    # Java.g:364:75: ( interfaceScopeDeclarations )*
                    while stream_interfaceScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_interfaceScopeDeclarations.nextTree())


                    stream_interfaceScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 24, interfaceBody_StartIndex, success)


            pass
        return retval

    # $ANTLR end "interfaceBody"


    class classScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.classScopeDeclarations_return, self).__init__()

            self.tree = None





    # $ANTLR start "classScopeDeclarations"
    # Java.g:367:1: classScopeDeclarations : ( block -> ^( CLASS_INSTANCE_INITIALIZER block ) | STATIC block -> ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block ) | modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) |ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration | SEMI !);
    def classScopeDeclarations(self, ):
        retval = self.classScopeDeclarations_return()
        retval.start = self.input.LT(1)

        classScopeDeclarations_StartIndex = self.input.index()

        root_0 = None

        ident = None
        STATIC81 = None
        IDENT86 = None
        SEMI91 = None
        VOID92 = None
        IDENT93 = None
        SEMI97 = None
        SEMI103 = None
        SEMI105 = None
        block80 = None

        block82 = None

        modifierList83 = None

        genericTypeParameterList84 = None

        type85 = None

        formalParameterList87 = None

        arrayDeclaratorList88 = None

        throwsClause89 = None

        block90 = None

        formalParameterList94 = None

        throwsClause95 = None

        block96 = None

        formalParameterList98 = None

        throwsClause99 = None

        block100 = None

        type101 = None

        classFieldDeclaratorList102 = None

        typeDeclaration104 = None


        ident_tree = None
        STATIC81_tree = None
        IDENT86_tree = None
        SEMI91_tree = None
        VOID92_tree = None
        IDENT93_tree = None
        SEMI97_tree = None
        SEMI103_tree = None
        SEMI105_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_STATIC = RewriteRuleTokenStream(self._adaptor, "token STATIC")
        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_throwsClause = RewriteRuleSubtreeStream(self._adaptor, "rule throwsClause")
        stream_modifierList = RewriteRuleSubtreeStream(self._adaptor, "rule modifierList")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_classFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclaratorList")
        stream_formalParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:368:5: ( block -> ^( CLASS_INSTANCE_INITIALIZER block ) | STATIC block -> ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block ) | modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) |ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration | SEMI !)
                alt36 = 5
                LA36 = self.input.LA(1)
                if LA36 == LCURLY:
                    alt36 = 1
                elif LA36 == STATIC:
                    LA36_2 = self.input.LA(2)

                    if (self.synpred32_Java()) :
                        alt36 = 2
                    elif (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 2, self.input)

                        raise nvae


                elif LA36 == PUBLIC:
                    LA36_3 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 3, self.input)

                        raise nvae


                elif LA36 == PROTECTED:
                    LA36_4 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 4, self.input)

                        raise nvae


                elif LA36 == PRIVATE:
                    LA36_5 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 5, self.input)

                        raise nvae


                elif LA36 == ABSTRACT:
                    LA36_6 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 6, self.input)

                        raise nvae


                elif LA36 == NATIVE:
                    LA36_7 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 7, self.input)

                        raise nvae


                elif LA36 == SYNCHRONIZED:
                    LA36_8 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 8, self.input)

                        raise nvae


                elif LA36 == TRANSIENT:
                    LA36_9 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 9, self.input)

                        raise nvae


                elif LA36 == VOLATILE:
                    LA36_10 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 10, self.input)

                        raise nvae


                elif LA36 == STRICTFP:
                    LA36_11 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 11, self.input)

                        raise nvae


                elif LA36 == FINAL:
                    LA36_12 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 12, self.input)

                        raise nvae


                elif LA36 == AT:
                    LA36_13 = self.input.LA(2)

                    if (self.synpred43_Java()) :
                        alt36 = 3
                    elif (self.synpred44_Java()) :
                        alt36 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 13, self.input)

                        raise nvae


                elif LA36 == BOOLEAN or LA36 == BYTE or LA36 == CHAR or LA36 == DOUBLE or LA36 == FLOAT or LA36 == IDENT or LA36 == INT or LA36 == LESS_THAN or LA36 == LONG or LA36 == SHORT or LA36 == VOID:
                    alt36 = 3
                elif LA36 == CLASS or LA36 == ENUM or LA36 == INTERFACE:
                    alt36 = 4
                elif LA36 == SEMI:
                    alt36 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # Java.g:368:9: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5655)
                    block80 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block80.tree)


                    # AST Rewrite
                    # elements: block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 368:25: -> ^( CLASS_INSTANCE_INITIALIZER block )
                        # Java.g:368:29: ^( CLASS_INSTANCE_INITIALIZER block )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(CLASS_INSTANCE_INITIALIZER, "CLASS_INSTANCE_INITIALIZER")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt36 == 2:
                    # Java.g:369:9: STATIC block
                    pass 
                    STATIC81 = self.match(self.input, STATIC, self.FOLLOW_STATIC_in_classScopeDeclarations5684) 
                    if self._state.backtracking == 0:
                        stream_STATIC.add(STATIC81)


                    self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5686)
                    block82 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block82.tree)


                    # AST Rewrite
                    # elements: block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 369:25: -> ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block )
                        # Java.g:369:29: ^( CLASS_STATIC_INITIALIZER[$STATIC, \"CLASS_STATIC_INITIALIZER\"] block )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(CLASS_STATIC_INITIALIZER, STATIC81, "CLASS_STATIC_INITIALIZER")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt36 == 3:
                    # Java.g:370:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) |ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    pass 
                    self._state.following.append(self.FOLLOW_modifierList_in_classScopeDeclarations5709)
                    modifierList83 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modifierList.add(modifierList83.tree)


                    # Java.g:371:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) |ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) ) | type classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    alt35 = 2
                    LA35 = self.input.LA(1)
                    if LA35 == LESS_THAN or LA35 == VOID:
                        alt35 = 1
                    elif LA35 == BOOLEAN or LA35 == BYTE or LA35 == CHAR or LA35 == DOUBLE or LA35 == FLOAT or LA35 == INT or LA35 == LONG or LA35 == SHORT:
                        LA35_2 = self.input.LA(2)

                        if (self.synpred42_Java()) :
                            alt35 = 1
                        elif (True) :
                            alt35 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 35, 2, self.input)

                            raise nvae


                    elif LA35 == IDENT:
                        LA35_3 = self.input.LA(2)

                        if (self.synpred42_Java()) :
                            alt35 = 1
                        elif (True) :
                            alt35 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 35, 3, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 35, 0, self.input)

                        raise nvae


                    if alt35 == 1:
                        # Java.g:371:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) |ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) )
                        pass 
                        # Java.g:371:13: ( genericTypeParameterList )?
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == LESS_THAN) :
                            alt27 = 1
                        if alt27 == 1:
                            # Java.g:371:13: genericTypeParameterList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_classScopeDeclarations5723)
                            genericTypeParameterList84 = self.genericTypeParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_genericTypeParameterList.add(genericTypeParameterList84.tree)





                        # Java.g:372:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? ) |ident= IDENT formalParameterList ( throwsClause )? block -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block ) )
                        alt34 = 3
                        LA34 = self.input.LA(1)
                        if LA34 == BOOLEAN or LA34 == BYTE or LA34 == CHAR or LA34 == DOUBLE or LA34 == FLOAT or LA34 == INT or LA34 == LONG or LA34 == SHORT:
                            alt34 = 1
                        elif LA34 == IDENT:
                            LA34_2 = self.input.LA(2)

                            if (LA34_2 == DOT or LA34_2 == IDENT or LA34_2 == LBRACK or LA34_2 == LESS_THAN) :
                                alt34 = 1
                            elif (LA34_2 == LPAREN) :
                                alt34 = 3
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 34, 2, self.input)

                                raise nvae


                        elif LA34 == VOID:
                            alt34 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 34, 0, self.input)

                            raise nvae


                        if alt34 == 1:
                            # Java.g:372:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI )
                            pass 
                            self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations5742)
                            type85 = self.type()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_type.add(type85.tree)


                            IDENT86 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations5744) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT86)


                            self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations5746)
                            formalParameterList87 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList87.tree)


                            # Java.g:372:48: ( arrayDeclaratorList )?
                            alt28 = 2
                            LA28_0 = self.input.LA(1)

                            if (LA28_0 == LBRACK) :
                                alt28 = 1
                            if alt28 == 1:
                                # Java.g:372:48: arrayDeclaratorList
                                pass 
                                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_classScopeDeclarations5748)
                                arrayDeclaratorList88 = self.arrayDeclaratorList()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arrayDeclaratorList.add(arrayDeclaratorList88.tree)





                            # Java.g:372:69: ( throwsClause )?
                            alt29 = 2
                            LA29_0 = self.input.LA(1)

                            if (LA29_0 == THROWS) :
                                alt29 = 1
                            if alt29 == 1:
                                # Java.g:372:69: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations5751)
                                throwsClause89 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause89.tree)





                            # Java.g:372:83: ( block | SEMI )
                            alt30 = 2
                            LA30_0 = self.input.LA(1)

                            if (LA30_0 == LCURLY) :
                                alt30 = 1
                            elif (LA30_0 == SEMI) :
                                alt30 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 30, 0, self.input)

                                raise nvae


                            if alt30 == 1:
                                # Java.g:372:84: block
                                pass 
                                self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5755)
                                block90 = self.block()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_block.add(block90.tree)



                            elif alt30 == 2:
                                # Java.g:372:92: SEMI
                                pass 
                                SEMI91 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5759) 
                                if self._state.backtracking == 0:
                                    stream_SEMI.add(SEMI91)





                            # AST Rewrite
                            # elements: formalParameterList, type, IDENT, throwsClause, block, genericTypeParameterList, arrayDeclaratorList, modifierList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 373:17: -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                                # Java.g:373:21: ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(FUNCTION_METHOD_DECL, "FUNCTION_METHOD_DECL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                                # Java.g:373:57: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();

                                self._adaptor.addChild(root_1, stream_type.nextTree())

                                self._adaptor.addChild(root_1, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())

                                # Java.g:373:114: ( arrayDeclaratorList )?
                                if stream_arrayDeclaratorList.hasNext():
                                    self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                                stream_arrayDeclaratorList.reset();

                                # Java.g:373:135: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                # Java.g:373:149: ( block )?
                                if stream_block.hasNext():
                                    self._adaptor.addChild(root_1, stream_block.nextTree())


                                stream_block.reset();

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt34 == 2:
                            # Java.g:374:17: VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI )
                            pass 
                            VOID92 = self.match(self.input, VOID, self.FOLLOW_VOID_in_classScopeDeclarations5821) 
                            if self._state.backtracking == 0:
                                stream_VOID.add(VOID92)


                            IDENT93 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations5823) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT93)


                            self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations5825)
                            formalParameterList94 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList94.tree)


                            # Java.g:374:48: ( throwsClause )?
                            alt31 = 2
                            LA31_0 = self.input.LA(1)

                            if (LA31_0 == THROWS) :
                                alt31 = 1
                            if alt31 == 1:
                                # Java.g:374:48: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations5827)
                                throwsClause95 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause95.tree)





                            # Java.g:374:62: ( block | SEMI )
                            alt32 = 2
                            LA32_0 = self.input.LA(1)

                            if (LA32_0 == LCURLY) :
                                alt32 = 1
                            elif (LA32_0 == SEMI) :
                                alt32 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 32, 0, self.input)

                                raise nvae


                            if alt32 == 1:
                                # Java.g:374:63: block
                                pass 
                                self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5831)
                                block96 = self.block()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_block.add(block96.tree)



                            elif alt32 == 2:
                                # Java.g:374:71: SEMI
                                pass 
                                SEMI97 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5835) 
                                if self._state.backtracking == 0:
                                    stream_SEMI.add(SEMI97)





                            # AST Rewrite
                            # elements: block, genericTypeParameterList, formalParameterList, IDENT, throwsClause, modifierList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 375:17: -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? )
                                # Java.g:375:21: ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ( block )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(VOID_METHOD_DECL, "VOID_METHOD_DECL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                                # Java.g:375:53: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();

                                self._adaptor.addChild(root_1, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())

                                # Java.g:375:105: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                # Java.g:375:119: ( block )?
                                if stream_block.hasNext():
                                    self._adaptor.addChild(root_1, stream_block.nextTree())


                                stream_block.reset();

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt34 == 3:
                            # Java.g:376:17: ident= IDENT formalParameterList ( throwsClause )? block
                            pass 
                            ident = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_classScopeDeclarations5894) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(ident)


                            self._state.following.append(self.FOLLOW_formalParameterList_in_classScopeDeclarations5896)
                            formalParameterList98 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList98.tree)


                            # Java.g:376:49: ( throwsClause )?
                            alt33 = 2
                            LA33_0 = self.input.LA(1)

                            if (LA33_0 == THROWS) :
                                alt33 = 1
                            if alt33 == 1:
                                # Java.g:376:49: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_classScopeDeclarations5898)
                                throwsClause99 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause99.tree)





                            self._state.following.append(self.FOLLOW_block_in_classScopeDeclarations5901)
                            block100 = self.block()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_block.add(block100.tree)


                            # AST Rewrite
                            # elements: formalParameterList, block, genericTypeParameterList, throwsClause, modifierList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 377:17: -> ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block )
                                # Java.g:377:21: ^( CONSTRUCTOR_DECL[$ident, \"CONSTRUCTOR_DECL\"] modifierList ( genericTypeParameterList )? formalParameterList ( throwsClause )? block )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.create(CONSTRUCTOR_DECL, ident, "CONSTRUCTOR_DECL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                                # Java.g:377:81: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();

                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())

                                # Java.g:377:127: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                self._adaptor.addChild(root_1, stream_block.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0







                    elif alt35 == 2:
                        # Java.g:379:13: type classFieldDeclaratorList SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_classScopeDeclarations5965)
                        type101 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type101.tree)


                        self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_classScopeDeclarations5967)
                        classFieldDeclaratorList102 = self.classFieldDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classFieldDeclaratorList.add(classFieldDeclaratorList102.tree)


                        SEMI103 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations5969) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI103)


                        # AST Rewrite
                        # elements: type, classFieldDeclaratorList, modifierList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 380:13: -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            # Java.g:380:17: ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                            self._adaptor.addChild(root_1, stream_type.nextTree())

                            self._adaptor.addChild(root_1, stream_classFieldDeclaratorList.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt36 == 4:
                    # Java.g:382:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typeDeclaration_in_classScopeDeclarations6014)
                    typeDeclaration104 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration104.tree)



                elif alt36 == 5:
                    # Java.g:383:9: SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    SEMI105 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_classScopeDeclarations6024)


                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 25, classScopeDeclarations_StartIndex, success)


            pass
        return retval

    # $ANTLR end "classScopeDeclarations"


    class interfaceScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.interfaceScopeDeclarations_return, self).__init__()

            self.tree = None





    # $ANTLR start "interfaceScopeDeclarations"
    # Java.g:386:1: interfaceScopeDeclarations : ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) ) | typeDeclaration | SEMI !);
    def interfaceScopeDeclarations(self, ):
        retval = self.interfaceScopeDeclarations_return()
        retval.start = self.input.LT(1)

        interfaceScopeDeclarations_StartIndex = self.input.index()

        root_0 = None

        IDENT109 = None
        SEMI113 = None
        VOID114 = None
        IDENT115 = None
        SEMI118 = None
        SEMI121 = None
        SEMI123 = None
        modifierList106 = None

        genericTypeParameterList107 = None

        type108 = None

        formalParameterList110 = None

        arrayDeclaratorList111 = None

        throwsClause112 = None

        formalParameterList116 = None

        throwsClause117 = None

        type119 = None

        interfaceFieldDeclaratorList120 = None

        typeDeclaration122 = None


        IDENT109_tree = None
        SEMI113_tree = None
        VOID114_tree = None
        IDENT115_tree = None
        SEMI118_tree = None
        SEMI121_tree = None
        SEMI123_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_throwsClause = RewriteRuleSubtreeStream(self._adaptor, "rule throwsClause")
        stream_modifierList = RewriteRuleSubtreeStream(self._adaptor, "rule modifierList")
        stream_genericTypeParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeParameterList")
        stream_interfaceFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceFieldDeclaratorList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_formalParameterList = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:387:5: ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) ) | typeDeclaration | SEMI !)
                alt43 = 3
                LA43 = self.input.LA(1)
                if LA43 == PUBLIC:
                    LA43_1 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 1, self.input)

                        raise nvae


                elif LA43 == PROTECTED:
                    LA43_2 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 2, self.input)

                        raise nvae


                elif LA43 == PRIVATE:
                    LA43_3 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 3, self.input)

                        raise nvae


                elif LA43 == STATIC:
                    LA43_4 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 4, self.input)

                        raise nvae


                elif LA43 == ABSTRACT:
                    LA43_5 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 5, self.input)

                        raise nvae


                elif LA43 == NATIVE:
                    LA43_6 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 6, self.input)

                        raise nvae


                elif LA43 == SYNCHRONIZED:
                    LA43_7 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 7, self.input)

                        raise nvae


                elif LA43 == TRANSIENT:
                    LA43_8 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 8, self.input)

                        raise nvae


                elif LA43 == VOLATILE:
                    LA43_9 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 9, self.input)

                        raise nvae


                elif LA43 == STRICTFP:
                    LA43_10 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 10, self.input)

                        raise nvae


                elif LA43 == FINAL:
                    LA43_11 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 11, self.input)

                        raise nvae


                elif LA43 == AT:
                    LA43_12 = self.input.LA(2)

                    if (self.synpred51_Java()) :
                        alt43 = 1
                    elif (self.synpred52_Java()) :
                        alt43 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 43, 12, self.input)

                        raise nvae


                elif LA43 == BOOLEAN or LA43 == BYTE or LA43 == CHAR or LA43 == DOUBLE or LA43 == FLOAT or LA43 == IDENT or LA43 == INT or LA43 == LESS_THAN or LA43 == LONG or LA43 == SHORT or LA43 == VOID:
                    alt43 = 1
                elif LA43 == CLASS or LA43 == ENUM or LA43 == INTERFACE:
                    alt43 = 2
                elif LA43 == SEMI:
                    alt43 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae


                if alt43 == 1:
                    # Java.g:387:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) )
                    pass 
                    self._state.following.append(self.FOLLOW_modifierList_in_interfaceScopeDeclarations6056)
                    modifierList106 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modifierList.add(modifierList106.tree)


                    # Java.g:388:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) ) | type interfaceFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList ) )
                    alt42 = 2
                    LA42 = self.input.LA(1)
                    if LA42 == LESS_THAN or LA42 == VOID:
                        alt42 = 1
                    elif LA42 == BOOLEAN or LA42 == BYTE or LA42 == CHAR or LA42 == DOUBLE or LA42 == FLOAT or LA42 == INT or LA42 == LONG or LA42 == SHORT:
                        LA42_2 = self.input.LA(2)

                        if (self.synpred50_Java()) :
                            alt42 = 1
                        elif (True) :
                            alt42 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 42, 2, self.input)

                            raise nvae


                    elif LA42 == IDENT:
                        LA42_3 = self.input.LA(2)

                        if (self.synpred50_Java()) :
                            alt42 = 1
                        elif (True) :
                            alt42 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 42, 3, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 42, 0, self.input)

                        raise nvae


                    if alt42 == 1:
                        # Java.g:388:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) )
                        pass 
                        # Java.g:388:13: ( genericTypeParameterList )?
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == LESS_THAN) :
                            alt37 = 1
                        if alt37 == 1:
                            # Java.g:388:13: genericTypeParameterList
                            pass 
                            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations6070)
                            genericTypeParameterList107 = self.genericTypeParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_genericTypeParameterList.add(genericTypeParameterList107.tree)





                        # Java.g:389:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ) | VOID IDENT formalParameterList ( throwsClause )? SEMI -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? ) )
                        alt41 = 2
                        LA41_0 = self.input.LA(1)

                        if (LA41_0 == BOOLEAN or LA41_0 == BYTE or LA41_0 == CHAR or LA41_0 == DOUBLE or LA41_0 == FLOAT or LA41_0 == IDENT or LA41_0 == INT or LA41_0 == LONG or LA41_0 == SHORT) :
                            alt41 = 1
                        elif (LA41_0 == VOID) :
                            alt41 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 41, 0, self.input)

                            raise nvae


                        if alt41 == 1:
                            # Java.g:389:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI
                            pass 
                            self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations6089)
                            type108 = self.type()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_type.add(type108.tree)


                            IDENT109 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations6091) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT109)


                            self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations6093)
                            formalParameterList110 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList110.tree)


                            # Java.g:389:48: ( arrayDeclaratorList )?
                            alt38 = 2
                            LA38_0 = self.input.LA(1)

                            if (LA38_0 == LBRACK) :
                                alt38 = 1
                            if alt38 == 1:
                                # Java.g:389:48: arrayDeclaratorList
                                pass 
                                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations6095)
                                arrayDeclaratorList111 = self.arrayDeclaratorList()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arrayDeclaratorList.add(arrayDeclaratorList111.tree)





                            # Java.g:389:69: ( throwsClause )?
                            alt39 = 2
                            LA39_0 = self.input.LA(1)

                            if (LA39_0 == THROWS) :
                                alt39 = 1
                            if alt39 == 1:
                                # Java.g:389:69: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations6098)
                                throwsClause112 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause112.tree)





                            SEMI113 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6101) 
                            if self._state.backtracking == 0:
                                stream_SEMI.add(SEMI113)


                            # AST Rewrite
                            # elements: IDENT, genericTypeParameterList, modifierList, type, formalParameterList, throwsClause, arrayDeclaratorList
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 390:17: -> ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                                # Java.g:390:21: ^( FUNCTION_METHOD_DECL modifierList ( genericTypeParameterList )? type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(FUNCTION_METHOD_DECL, "FUNCTION_METHOD_DECL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                                # Java.g:390:57: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();

                                self._adaptor.addChild(root_1, stream_type.nextTree())

                                self._adaptor.addChild(root_1, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())

                                # Java.g:390:114: ( arrayDeclaratorList )?
                                if stream_arrayDeclaratorList.hasNext():
                                    self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                                stream_arrayDeclaratorList.reset();

                                # Java.g:390:135: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt41 == 2:
                            # Java.g:391:17: VOID IDENT formalParameterList ( throwsClause )? SEMI
                            pass 
                            VOID114 = self.match(self.input, VOID, self.FOLLOW_VOID_in_interfaceScopeDeclarations6159) 
                            if self._state.backtracking == 0:
                                stream_VOID.add(VOID114)


                            IDENT115 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_interfaceScopeDeclarations6161) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT115)


                            self._state.following.append(self.FOLLOW_formalParameterList_in_interfaceScopeDeclarations6163)
                            formalParameterList116 = self.formalParameterList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterList.add(formalParameterList116.tree)


                            # Java.g:391:48: ( throwsClause )?
                            alt40 = 2
                            LA40_0 = self.input.LA(1)

                            if (LA40_0 == THROWS) :
                                alt40 = 1
                            if alt40 == 1:
                                # Java.g:391:48: throwsClause
                                pass 
                                self._state.following.append(self.FOLLOW_throwsClause_in_interfaceScopeDeclarations6165)
                                throwsClause117 = self.throwsClause()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_throwsClause.add(throwsClause117.tree)





                            SEMI118 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6168) 
                            if self._state.backtracking == 0:
                                stream_SEMI.add(SEMI118)


                            # AST Rewrite
                            # elements: IDENT, modifierList, formalParameterList, genericTypeParameterList, throwsClause
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 392:17: -> ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? )
                                # Java.g:392:21: ^( VOID_METHOD_DECL modifierList ( genericTypeParameterList )? IDENT formalParameterList ( throwsClause )? )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(VOID_METHOD_DECL, "VOID_METHOD_DECL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                                # Java.g:392:53: ( genericTypeParameterList )?
                                if stream_genericTypeParameterList.hasNext():
                                    self._adaptor.addChild(root_1, stream_genericTypeParameterList.nextTree())


                                stream_genericTypeParameterList.reset();

                                self._adaptor.addChild(root_1, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, stream_formalParameterList.nextTree())

                                # Java.g:392:105: ( throwsClause )?
                                if stream_throwsClause.hasNext():
                                    self._adaptor.addChild(root_1, stream_throwsClause.nextTree())


                                stream_throwsClause.reset();

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0







                    elif alt42 == 2:
                        # Java.g:394:13: type interfaceFieldDeclaratorList SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_type_in_interfaceScopeDeclarations6231)
                        type119 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type119.tree)


                        self._state.following.append(self.FOLLOW_interfaceFieldDeclaratorList_in_interfaceScopeDeclarations6233)
                        interfaceFieldDeclaratorList120 = self.interfaceFieldDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_interfaceFieldDeclaratorList.add(interfaceFieldDeclaratorList120.tree)


                        SEMI121 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6235) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI121)


                        # AST Rewrite
                        # elements: modifierList, type, interfaceFieldDeclaratorList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 395:13: -> ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList )
                            # Java.g:395:17: ^( VAR_DECLARATION modifierList type interfaceFieldDeclaratorList )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                            self._adaptor.addChild(root_1, stream_type.nextTree())

                            self._adaptor.addChild(root_1, stream_interfaceFieldDeclaratorList.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt43 == 2:
                    # Java.g:397:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typeDeclaration_in_interfaceScopeDeclarations6280)
                    typeDeclaration122 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration122.tree)



                elif alt43 == 3:
                    # Java.g:398:9: SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    SEMI123 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_interfaceScopeDeclarations6290)


                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 26, interfaceScopeDeclarations_StartIndex, success)


            pass
        return retval

    # $ANTLR end "interfaceScopeDeclarations"


    class classFieldDeclaratorList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.classFieldDeclaratorList_return, self).__init__()

            self.tree = None





    # $ANTLR start "classFieldDeclaratorList"
    # Java.g:401:1: classFieldDeclaratorList : classFieldDeclarator ( COMMA classFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ ) ;
    def classFieldDeclaratorList(self, ):
        retval = self.classFieldDeclaratorList_return()
        retval.start = self.input.LT(1)

        classFieldDeclaratorList_StartIndex = self.input.index()

        root_0 = None

        COMMA125 = None
        classFieldDeclarator124 = None

        classFieldDeclarator126 = None


        COMMA125_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_classFieldDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclarator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:402:5: ( classFieldDeclarator ( COMMA classFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ ) )
                # Java.g:402:9: classFieldDeclarator ( COMMA classFieldDeclarator )*
                pass 
                self._state.following.append(self.FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6310)
                classFieldDeclarator124 = self.classFieldDeclarator()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_classFieldDeclarator.add(classFieldDeclarator124.tree)


                # Java.g:402:30: ( COMMA classFieldDeclarator )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == COMMA) :
                        alt44 = 1


                    if alt44 == 1:
                        # Java.g:402:31: COMMA classFieldDeclarator
                        pass 
                        COMMA125 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_classFieldDeclaratorList6313) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA125)


                        self._state.following.append(self.FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6315)
                        classFieldDeclarator126 = self.classFieldDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classFieldDeclarator.add(classFieldDeclarator126.tree)



                    else:
                        break #loop44


                # AST Rewrite
                # elements: classFieldDeclarator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 403:9: -> ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ )
                    # Java.g:403:13: ^( VAR_DECLARATOR_LIST ( classFieldDeclarator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VAR_DECLARATOR_LIST, "VAR_DECLARATOR_LIST")
                    , root_1)

                    # Java.g:403:35: ( classFieldDeclarator )+
                    if not (stream_classFieldDeclarator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_classFieldDeclarator.hasNext():
                        self._adaptor.addChild(root_1, stream_classFieldDeclarator.nextTree())


                    stream_classFieldDeclarator.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 27, classFieldDeclaratorList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "classFieldDeclaratorList"


    class classFieldDeclarator_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.classFieldDeclarator_return, self).__init__()

            self.tree = None





    # $ANTLR start "classFieldDeclarator"
    # Java.g:406:1: classFieldDeclarator : variableDeclaratorId ( ASSIGN variableInitializer )? -> ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? ) ;
    def classFieldDeclarator(self, ):
        retval = self.classFieldDeclarator_return()
        retval.start = self.input.LT(1)

        classFieldDeclarator_StartIndex = self.input.index()

        root_0 = None

        ASSIGN128 = None
        variableDeclaratorId127 = None

        variableInitializer129 = None


        ASSIGN128_tree = None
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_variableInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule variableInitializer")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:407:5: ( variableDeclaratorId ( ASSIGN variableInitializer )? -> ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? ) )
                # Java.g:407:9: variableDeclaratorId ( ASSIGN variableInitializer )?
                pass 
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_classFieldDeclarator6354)
                variableDeclaratorId127 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId127.tree)


                # Java.g:407:30: ( ASSIGN variableInitializer )?
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == ASSIGN) :
                    alt45 = 1
                if alt45 == 1:
                    # Java.g:407:31: ASSIGN variableInitializer
                    pass 
                    ASSIGN128 = self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_classFieldDeclarator6357) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN128)


                    self._state.following.append(self.FOLLOW_variableInitializer_in_classFieldDeclarator6359)
                    variableInitializer129 = self.variableInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_variableInitializer.add(variableInitializer129.tree)





                # AST Rewrite
                # elements: variableInitializer, variableDeclaratorId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 408:9: -> ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? )
                    # Java.g:408:13: ^( VAR_DECLARATOR variableDeclaratorId ( variableInitializer )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VAR_DECLARATOR, "VAR_DECLARATOR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())

                    # Java.g:408:51: ( variableInitializer )?
                    if stream_variableInitializer.hasNext():
                        self._adaptor.addChild(root_1, stream_variableInitializer.nextTree())


                    stream_variableInitializer.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 28, classFieldDeclarator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "classFieldDeclarator"


    class interfaceFieldDeclaratorList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.interfaceFieldDeclaratorList_return, self).__init__()

            self.tree = None





    # $ANTLR start "interfaceFieldDeclaratorList"
    # Java.g:411:1: interfaceFieldDeclaratorList : interfaceFieldDeclarator ( COMMA interfaceFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ ) ;
    def interfaceFieldDeclaratorList(self, ):
        retval = self.interfaceFieldDeclaratorList_return()
        retval.start = self.input.LT(1)

        interfaceFieldDeclaratorList_StartIndex = self.input.index()

        root_0 = None

        COMMA131 = None
        interfaceFieldDeclarator130 = None

        interfaceFieldDeclarator132 = None


        COMMA131_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_interfaceFieldDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule interfaceFieldDeclarator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:412:5: ( interfaceFieldDeclarator ( COMMA interfaceFieldDeclarator )* -> ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ ) )
                # Java.g:412:9: interfaceFieldDeclarator ( COMMA interfaceFieldDeclarator )*
                pass 
                self._state.following.append(self.FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6404)
                interfaceFieldDeclarator130 = self.interfaceFieldDeclarator()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_interfaceFieldDeclarator.add(interfaceFieldDeclarator130.tree)


                # Java.g:412:34: ( COMMA interfaceFieldDeclarator )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == COMMA) :
                        alt46 = 1


                    if alt46 == 1:
                        # Java.g:412:35: COMMA interfaceFieldDeclarator
                        pass 
                        COMMA131 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_interfaceFieldDeclaratorList6407) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA131)


                        self._state.following.append(self.FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6409)
                        interfaceFieldDeclarator132 = self.interfaceFieldDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_interfaceFieldDeclarator.add(interfaceFieldDeclarator132.tree)



                    else:
                        break #loop46


                # AST Rewrite
                # elements: interfaceFieldDeclarator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 413:9: -> ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ )
                    # Java.g:413:13: ^( VAR_DECLARATOR_LIST ( interfaceFieldDeclarator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VAR_DECLARATOR_LIST, "VAR_DECLARATOR_LIST")
                    , root_1)

                    # Java.g:413:35: ( interfaceFieldDeclarator )+
                    if not (stream_interfaceFieldDeclarator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_interfaceFieldDeclarator.hasNext():
                        self._adaptor.addChild(root_1, stream_interfaceFieldDeclarator.nextTree())


                    stream_interfaceFieldDeclarator.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 29, interfaceFieldDeclaratorList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "interfaceFieldDeclaratorList"


    class interfaceFieldDeclarator_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.interfaceFieldDeclarator_return, self).__init__()

            self.tree = None





    # $ANTLR start "interfaceFieldDeclarator"
    # Java.g:416:1: interfaceFieldDeclarator : variableDeclaratorId ASSIGN variableInitializer -> ^( VAR_DECLARATOR variableDeclaratorId variableInitializer ) ;
    def interfaceFieldDeclarator(self, ):
        retval = self.interfaceFieldDeclarator_return()
        retval.start = self.input.LT(1)

        interfaceFieldDeclarator_StartIndex = self.input.index()

        root_0 = None

        ASSIGN134 = None
        variableDeclaratorId133 = None

        variableInitializer135 = None


        ASSIGN134_tree = None
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_variableInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule variableInitializer")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:417:5: ( variableDeclaratorId ASSIGN variableInitializer -> ^( VAR_DECLARATOR variableDeclaratorId variableInitializer ) )
                # Java.g:417:9: variableDeclaratorId ASSIGN variableInitializer
                pass 
                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_interfaceFieldDeclarator6448)
                variableDeclaratorId133 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId133.tree)


                ASSIGN134 = self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_interfaceFieldDeclarator6450) 
                if self._state.backtracking == 0:
                    stream_ASSIGN.add(ASSIGN134)


                self._state.following.append(self.FOLLOW_variableInitializer_in_interfaceFieldDeclarator6452)
                variableInitializer135 = self.variableInitializer()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableInitializer.add(variableInitializer135.tree)


                # AST Rewrite
                # elements: variableInitializer, variableDeclaratorId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 418:9: -> ^( VAR_DECLARATOR variableDeclaratorId variableInitializer )
                    # Java.g:418:13: ^( VAR_DECLARATOR variableDeclaratorId variableInitializer )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VAR_DECLARATOR, "VAR_DECLARATOR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())

                    self._adaptor.addChild(root_1, stream_variableInitializer.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 30, interfaceFieldDeclarator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "interfaceFieldDeclarator"


    class variableDeclaratorId_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.variableDeclaratorId_return, self).__init__()

            self.tree = None





    # $ANTLR start "variableDeclaratorId"
    # Java.g:421:1: variableDeclaratorId : IDENT ^ ( arrayDeclaratorList )? ;
    def variableDeclaratorId(self, ):
        retval = self.variableDeclaratorId_return()
        retval.start = self.input.LT(1)

        variableDeclaratorId_StartIndex = self.input.index()

        root_0 = None

        IDENT136 = None
        arrayDeclaratorList137 = None


        IDENT136_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:422:5: ( IDENT ^ ( arrayDeclaratorList )? )
                # Java.g:422:9: IDENT ^ ( arrayDeclaratorList )?
                pass 
                root_0 = self._adaptor.nil()


                IDENT136 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_variableDeclaratorId6494)
                if self._state.backtracking == 0:
                    IDENT136_tree = self._adaptor.createWithPayload(IDENT136)
                    root_0 = self._adaptor.becomeRoot(IDENT136_tree, root_0)



                # Java.g:422:16: ( arrayDeclaratorList )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == LBRACK) :
                    alt47 = 1
                if alt47 == 1:
                    # Java.g:422:16: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_variableDeclaratorId6497)
                    arrayDeclaratorList137 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayDeclaratorList137.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 31, variableDeclaratorId_StartIndex, success)


            pass
        return retval

    # $ANTLR end "variableDeclaratorId"


    class variableInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.variableInitializer_return, self).__init__()

            self.tree = None





    # $ANTLR start "variableInitializer"
    # Java.g:425:1: variableInitializer : ( arrayInitializer | expression );
    def variableInitializer(self, ):
        retval = self.variableInitializer_return()
        retval.start = self.input.LT(1)

        variableInitializer_StartIndex = self.input.index()

        root_0 = None

        arrayInitializer138 = None

        expression139 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:426:5: ( arrayInitializer | expression )
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == LCURLY) :
                    alt48 = 1
                elif (LA48_0 == BOOLEAN or LA48_0 == BYTE or (CHAR <= LA48_0 <= CHARACTER_LITERAL) or (DEC <= LA48_0 <= DECIMAL_LITERAL) or LA48_0 == DOUBLE or LA48_0 == FALSE or (FLOAT <= LA48_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA48_0 <= IDENT) or LA48_0 == INC or LA48_0 == INT or LA48_0 == LESS_THAN or LA48_0 == LOGICAL_NOT or (LONG <= LA48_0 <= LPAREN) or LA48_0 == MINUS or (NEW <= LA48_0 <= NOT) or LA48_0 == NULL or LA48_0 == OCTAL_LITERAL or LA48_0 == PLUS or LA48_0 == SHORT or (STRING_LITERAL <= LA48_0 <= SUPER) or LA48_0 == THIS or LA48_0 == TRUE or LA48_0 == VOID) :
                    alt48 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae


                if alt48 == 1:
                    # Java.g:426:9: arrayInitializer
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_arrayInitializer_in_variableInitializer6517)
                    arrayInitializer138 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayInitializer138.tree)



                elif alt48 == 2:
                    # Java.g:427:9: expression
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expression_in_variableInitializer6527)
                    expression139 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression139.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 32, variableInitializer_StartIndex, success)


            pass
        return retval

    # $ANTLR end "variableInitializer"


    class arrayDeclarator_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.arrayDeclarator_return, self).__init__()

            self.tree = None





    # $ANTLR start "arrayDeclarator"
    # Java.g:430:1: arrayDeclarator : LBRACK RBRACK -> ^( ARRAY_DECLARATOR ) ;
    def arrayDeclarator(self, ):
        retval = self.arrayDeclarator_return()
        retval.start = self.input.LT(1)

        arrayDeclarator_StartIndex = self.input.index()

        root_0 = None

        LBRACK140 = None
        RBRACK141 = None

        LBRACK140_tree = None
        RBRACK141_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:431:5: ( LBRACK RBRACK -> ^( ARRAY_DECLARATOR ) )
                # Java.g:431:9: LBRACK RBRACK
                pass 
                LBRACK140 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_arrayDeclarator6546) 
                if self._state.backtracking == 0:
                    stream_LBRACK.add(LBRACK140)


                RBRACK141 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_arrayDeclarator6548) 
                if self._state.backtracking == 0:
                    stream_RBRACK.add(RBRACK141)


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 432:9: -> ^( ARRAY_DECLARATOR )
                    # Java.g:432:13: ^( ARRAY_DECLARATOR )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ARRAY_DECLARATOR, "ARRAY_DECLARATOR")
                    , root_1)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 33, arrayDeclarator_StartIndex, success)


            pass
        return retval

    # $ANTLR end "arrayDeclarator"


    class arrayDeclaratorList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.arrayDeclaratorList_return, self).__init__()

            self.tree = None





    # $ANTLR start "arrayDeclaratorList"
    # Java.g:435:1: arrayDeclaratorList : ( arrayDeclarator )+ -> ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ ) ;
    def arrayDeclaratorList(self, ):
        retval = self.arrayDeclaratorList_return()
        retval.start = self.input.LT(1)

        arrayDeclaratorList_StartIndex = self.input.index()

        root_0 = None

        arrayDeclarator142 = None


        stream_arrayDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclarator")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:436:5: ( ( arrayDeclarator )+ -> ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ ) )
                # Java.g:436:9: ( arrayDeclarator )+
                pass 
                # Java.g:436:9: ( arrayDeclarator )+
                cnt49 = 0
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == LBRACK) :
                        LA49_2 = self.input.LA(2)

                        if (self.synpred58_Java()) :
                            alt49 = 1




                    if alt49 == 1:
                        # Java.g:436:9: arrayDeclarator
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclarator_in_arrayDeclaratorList6582)
                        arrayDeclarator142 = self.arrayDeclarator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arrayDeclarator.add(arrayDeclarator142.tree)



                    else:
                        if cnt49 >= 1:
                            break #loop49

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(49, self.input)
                        raise eee

                    cnt49 += 1


                # AST Rewrite
                # elements: arrayDeclarator
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 437:9: -> ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ )
                    # Java.g:437:13: ^( ARRAY_DECLARATOR_LIST ( arrayDeclarator )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ARRAY_DECLARATOR_LIST, "ARRAY_DECLARATOR_LIST")
                    , root_1)

                    # Java.g:437:37: ( arrayDeclarator )+
                    if not (stream_arrayDeclarator.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arrayDeclarator.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclarator.nextTree())


                    stream_arrayDeclarator.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 34, arrayDeclaratorList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "arrayDeclaratorList"


    class arrayInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.arrayInitializer_return, self).__init__()

            self.tree = None





    # $ANTLR start "arrayInitializer"
    # Java.g:440:1: arrayInitializer : LCURLY ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )? RCURLY -> ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* ) ;
    def arrayInitializer(self, ):
        retval = self.arrayInitializer_return()
        retval.start = self.input.LT(1)

        arrayInitializer_StartIndex = self.input.index()

        root_0 = None

        LCURLY143 = None
        COMMA145 = None
        COMMA147 = None
        RCURLY148 = None
        variableInitializer144 = None

        variableInitializer146 = None


        LCURLY143_tree = None
        COMMA145_tree = None
        COMMA147_tree = None
        RCURLY148_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_variableInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule variableInitializer")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:441:5: ( LCURLY ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )? RCURLY -> ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* ) )
                # Java.g:441:9: LCURLY ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )? RCURLY
                pass 
                LCURLY143 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_arrayInitializer6627) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY143)


                # Java.g:441:16: ( variableInitializer ( COMMA variableInitializer )* ( COMMA )? )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == BOOLEAN or LA52_0 == BYTE or (CHAR <= LA52_0 <= CHARACTER_LITERAL) or (DEC <= LA52_0 <= DECIMAL_LITERAL) or LA52_0 == DOUBLE or LA52_0 == FALSE or (FLOAT <= LA52_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA52_0 <= IDENT) or LA52_0 == INC or LA52_0 == INT or LA52_0 == LCURLY or LA52_0 == LESS_THAN or LA52_0 == LOGICAL_NOT or (LONG <= LA52_0 <= LPAREN) or LA52_0 == MINUS or (NEW <= LA52_0 <= NOT) or LA52_0 == NULL or LA52_0 == OCTAL_LITERAL or LA52_0 == PLUS or LA52_0 == SHORT or (STRING_LITERAL <= LA52_0 <= SUPER) or LA52_0 == THIS or LA52_0 == TRUE or LA52_0 == VOID) :
                    alt52 = 1
                if alt52 == 1:
                    # Java.g:441:17: variableInitializer ( COMMA variableInitializer )* ( COMMA )?
                    pass 
                    self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer6630)
                    variableInitializer144 = self.variableInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_variableInitializer.add(variableInitializer144.tree)


                    # Java.g:441:37: ( COMMA variableInitializer )*
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == COMMA) :
                            LA50_1 = self.input.LA(2)

                            if (LA50_1 == BOOLEAN or LA50_1 == BYTE or (CHAR <= LA50_1 <= CHARACTER_LITERAL) or (DEC <= LA50_1 <= DECIMAL_LITERAL) or LA50_1 == DOUBLE or LA50_1 == FALSE or (FLOAT <= LA50_1 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA50_1 <= IDENT) or LA50_1 == INC or LA50_1 == INT or LA50_1 == LCURLY or LA50_1 == LESS_THAN or LA50_1 == LOGICAL_NOT or (LONG <= LA50_1 <= LPAREN) or LA50_1 == MINUS or (NEW <= LA50_1 <= NOT) or LA50_1 == NULL or LA50_1 == OCTAL_LITERAL or LA50_1 == PLUS or LA50_1 == SHORT or (STRING_LITERAL <= LA50_1 <= SUPER) or LA50_1 == THIS or LA50_1 == TRUE or LA50_1 == VOID) :
                                alt50 = 1




                        if alt50 == 1:
                            # Java.g:441:38: COMMA variableInitializer
                            pass 
                            COMMA145 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arrayInitializer6633) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA145)


                            self._state.following.append(self.FOLLOW_variableInitializer_in_arrayInitializer6635)
                            variableInitializer146 = self.variableInitializer()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_variableInitializer.add(variableInitializer146.tree)



                        else:
                            break #loop50


                    # Java.g:441:66: ( COMMA )?
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == COMMA) :
                        alt51 = 1
                    if alt51 == 1:
                        # Java.g:441:66: COMMA
                        pass 
                        COMMA147 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_arrayInitializer6639) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA147)








                RCURLY148 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_arrayInitializer6644) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY148)


                # AST Rewrite
                # elements: variableInitializer
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 442:9: -> ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* )
                    # Java.g:442:13: ^( ARRAY_INITIALIZER[$LCURLY, \"ARRAY_INITIALIZER\"] ( variableInitializer )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(ARRAY_INITIALIZER, LCURLY143, "ARRAY_INITIALIZER")
                    , root_1)

                    # Java.g:442:63: ( variableInitializer )*
                    while stream_variableInitializer.hasNext():
                        self._adaptor.addChild(root_1, stream_variableInitializer.nextTree())


                    stream_variableInitializer.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 35, arrayInitializer_StartIndex, success)


            pass
        return retval

    # $ANTLR end "arrayInitializer"


    class throwsClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.throwsClause_return, self).__init__()

            self.tree = None





    # $ANTLR start "throwsClause"
    # Java.g:445:1: throwsClause : THROWS qualifiedIdentList -> ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList ) ;
    def throwsClause(self, ):
        retval = self.throwsClause_return()
        retval.start = self.input.LT(1)

        throwsClause_StartIndex = self.input.index()

        root_0 = None

        THROWS149 = None
        qualifiedIdentList150 = None


        THROWS149_tree = None
        stream_THROWS = RewriteRuleTokenStream(self._adaptor, "token THROWS")
        stream_qualifiedIdentList = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedIdentList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:446:5: ( THROWS qualifiedIdentList -> ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList ) )
                # Java.g:446:9: THROWS qualifiedIdentList
                pass 
                THROWS149 = self.match(self.input, THROWS, self.FOLLOW_THROWS_in_throwsClause6682) 
                if self._state.backtracking == 0:
                    stream_THROWS.add(THROWS149)


                self._state.following.append(self.FOLLOW_qualifiedIdentList_in_throwsClause6684)
                qualifiedIdentList150 = self.qualifiedIdentList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedIdentList.add(qualifiedIdentList150.tree)


                # AST Rewrite
                # elements: qualifiedIdentList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 447:9: -> ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList )
                    # Java.g:447:13: ^( THROWS_CLAUSE[$THROWS, \"THROWS_CLAUSE\"] qualifiedIdentList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(THROWS_CLAUSE, THROWS149, "THROWS_CLAUSE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_qualifiedIdentList.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 36, throwsClause_StartIndex, success)


            pass
        return retval

    # $ANTLR end "throwsClause"


    class modifierList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.modifierList_return, self).__init__()

            self.tree = None





    # $ANTLR start "modifierList"
    # Java.g:450:1: modifierList : ( modifier )* -> ^( MODIFIER_LIST ( modifier )* ) ;
    def modifierList(self, ):
        retval = self.modifierList_return()
        retval.start = self.input.LT(1)

        modifierList_StartIndex = self.input.index()

        root_0 = None

        modifier151 = None


        stream_modifier = RewriteRuleSubtreeStream(self._adaptor, "rule modifier")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:451:5: ( ( modifier )* -> ^( MODIFIER_LIST ( modifier )* ) )
                # Java.g:451:9: ( modifier )*
                pass 
                # Java.g:451:9: ( modifier )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == AT) :
                        LA53_2 = self.input.LA(2)

                        if (LA53_2 == IDENT) :
                            alt53 = 1


                    elif (LA53_0 == ABSTRACT or LA53_0 == FINAL or LA53_0 == NATIVE or (PRIVATE <= LA53_0 <= PUBLIC) or LA53_0 == STATIC or LA53_0 == STRICTFP or LA53_0 == SYNCHRONIZED or LA53_0 == TRANSIENT or LA53_0 == VOLATILE) :
                        alt53 = 1


                    if alt53 == 1:
                        # Java.g:451:9: modifier
                        pass 
                        self._state.following.append(self.FOLLOW_modifier_in_modifierList6721)
                        modifier151 = self.modifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_modifier.add(modifier151.tree)



                    else:
                        break #loop53


                # AST Rewrite
                # elements: modifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 452:9: -> ^( MODIFIER_LIST ( modifier )* )
                    # Java.g:452:13: ^( MODIFIER_LIST ( modifier )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(MODIFIER_LIST, "MODIFIER_LIST")
                    , root_1)

                    # Java.g:452:29: ( modifier )*
                    while stream_modifier.hasNext():
                        self._adaptor.addChild(root_1, stream_modifier.nextTree())


                    stream_modifier.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 37, modifierList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "modifierList"


    class modifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.modifier_return, self).__init__()

            self.tree = None





    # $ANTLR start "modifier"
    # Java.g:455:1: modifier : ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | localModifier );
    def modifier(self, ):
        retval = self.modifier_return()
        retval.start = self.input.LT(1)

        modifier_StartIndex = self.input.index()

        root_0 = None

        PUBLIC152 = None
        PROTECTED153 = None
        PRIVATE154 = None
        STATIC155 = None
        ABSTRACT156 = None
        NATIVE157 = None
        SYNCHRONIZED158 = None
        TRANSIENT159 = None
        VOLATILE160 = None
        STRICTFP161 = None
        localModifier162 = None


        PUBLIC152_tree = None
        PROTECTED153_tree = None
        PRIVATE154_tree = None
        STATIC155_tree = None
        ABSTRACT156_tree = None
        NATIVE157_tree = None
        SYNCHRONIZED158_tree = None
        TRANSIENT159_tree = None
        VOLATILE160_tree = None
        STRICTFP161_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:456:5: ( PUBLIC | PROTECTED | PRIVATE | STATIC | ABSTRACT | NATIVE | SYNCHRONIZED | TRANSIENT | VOLATILE | STRICTFP | localModifier )
                alt54 = 11
                LA54 = self.input.LA(1)
                if LA54 == PUBLIC:
                    alt54 = 1
                elif LA54 == PROTECTED:
                    alt54 = 2
                elif LA54 == PRIVATE:
                    alt54 = 3
                elif LA54 == STATIC:
                    alt54 = 4
                elif LA54 == ABSTRACT:
                    alt54 = 5
                elif LA54 == NATIVE:
                    alt54 = 6
                elif LA54 == SYNCHRONIZED:
                    alt54 = 7
                elif LA54 == TRANSIENT:
                    alt54 = 8
                elif LA54 == VOLATILE:
                    alt54 = 9
                elif LA54 == STRICTFP:
                    alt54 = 10
                elif LA54 == AT or LA54 == FINAL:
                    alt54 = 11
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae


                if alt54 == 1:
                    # Java.g:456:9: PUBLIC
                    pass 
                    root_0 = self._adaptor.nil()


                    PUBLIC152 = self.match(self.input, PUBLIC, self.FOLLOW_PUBLIC_in_modifier6762)
                    if self._state.backtracking == 0:
                        PUBLIC152_tree = self._adaptor.createWithPayload(PUBLIC152)
                        self._adaptor.addChild(root_0, PUBLIC152_tree)




                elif alt54 == 2:
                    # Java.g:457:9: PROTECTED
                    pass 
                    root_0 = self._adaptor.nil()


                    PROTECTED153 = self.match(self.input, PROTECTED, self.FOLLOW_PROTECTED_in_modifier6772)
                    if self._state.backtracking == 0:
                        PROTECTED153_tree = self._adaptor.createWithPayload(PROTECTED153)
                        self._adaptor.addChild(root_0, PROTECTED153_tree)




                elif alt54 == 3:
                    # Java.g:458:9: PRIVATE
                    pass 
                    root_0 = self._adaptor.nil()


                    PRIVATE154 = self.match(self.input, PRIVATE, self.FOLLOW_PRIVATE_in_modifier6782)
                    if self._state.backtracking == 0:
                        PRIVATE154_tree = self._adaptor.createWithPayload(PRIVATE154)
                        self._adaptor.addChild(root_0, PRIVATE154_tree)




                elif alt54 == 4:
                    # Java.g:459:9: STATIC
                    pass 
                    root_0 = self._adaptor.nil()


                    STATIC155 = self.match(self.input, STATIC, self.FOLLOW_STATIC_in_modifier6792)
                    if self._state.backtracking == 0:
                        STATIC155_tree = self._adaptor.createWithPayload(STATIC155)
                        self._adaptor.addChild(root_0, STATIC155_tree)




                elif alt54 == 5:
                    # Java.g:460:9: ABSTRACT
                    pass 
                    root_0 = self._adaptor.nil()


                    ABSTRACT156 = self.match(self.input, ABSTRACT, self.FOLLOW_ABSTRACT_in_modifier6802)
                    if self._state.backtracking == 0:
                        ABSTRACT156_tree = self._adaptor.createWithPayload(ABSTRACT156)
                        self._adaptor.addChild(root_0, ABSTRACT156_tree)




                elif alt54 == 6:
                    # Java.g:461:9: NATIVE
                    pass 
                    root_0 = self._adaptor.nil()


                    NATIVE157 = self.match(self.input, NATIVE, self.FOLLOW_NATIVE_in_modifier6812)
                    if self._state.backtracking == 0:
                        NATIVE157_tree = self._adaptor.createWithPayload(NATIVE157)
                        self._adaptor.addChild(root_0, NATIVE157_tree)




                elif alt54 == 7:
                    # Java.g:462:9: SYNCHRONIZED
                    pass 
                    root_0 = self._adaptor.nil()


                    SYNCHRONIZED158 = self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_modifier6822)
                    if self._state.backtracking == 0:
                        SYNCHRONIZED158_tree = self._adaptor.createWithPayload(SYNCHRONIZED158)
                        self._adaptor.addChild(root_0, SYNCHRONIZED158_tree)




                elif alt54 == 8:
                    # Java.g:463:9: TRANSIENT
                    pass 
                    root_0 = self._adaptor.nil()


                    TRANSIENT159 = self.match(self.input, TRANSIENT, self.FOLLOW_TRANSIENT_in_modifier6832)
                    if self._state.backtracking == 0:
                        TRANSIENT159_tree = self._adaptor.createWithPayload(TRANSIENT159)
                        self._adaptor.addChild(root_0, TRANSIENT159_tree)




                elif alt54 == 9:
                    # Java.g:464:9: VOLATILE
                    pass 
                    root_0 = self._adaptor.nil()


                    VOLATILE160 = self.match(self.input, VOLATILE, self.FOLLOW_VOLATILE_in_modifier6842)
                    if self._state.backtracking == 0:
                        VOLATILE160_tree = self._adaptor.createWithPayload(VOLATILE160)
                        self._adaptor.addChild(root_0, VOLATILE160_tree)




                elif alt54 == 10:
                    # Java.g:465:9: STRICTFP
                    pass 
                    root_0 = self._adaptor.nil()


                    STRICTFP161 = self.match(self.input, STRICTFP, self.FOLLOW_STRICTFP_in_modifier6852)
                    if self._state.backtracking == 0:
                        STRICTFP161_tree = self._adaptor.createWithPayload(STRICTFP161)
                        self._adaptor.addChild(root_0, STRICTFP161_tree)




                elif alt54 == 11:
                    # Java.g:466:9: localModifier
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localModifier_in_modifier6862)
                    localModifier162 = self.localModifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localModifier162.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 38, modifier_StartIndex, success)


            pass
        return retval

    # $ANTLR end "modifier"


    class localModifierList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.localModifierList_return, self).__init__()

            self.tree = None





    # $ANTLR start "localModifierList"
    # Java.g:469:1: localModifierList : ( localModifier )* -> ^( LOCAL_MODIFIER_LIST ( localModifier )* ) ;
    def localModifierList(self, ):
        retval = self.localModifierList_return()
        retval.start = self.input.LT(1)

        localModifierList_StartIndex = self.input.index()

        root_0 = None

        localModifier163 = None


        stream_localModifier = RewriteRuleSubtreeStream(self._adaptor, "rule localModifier")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:470:5: ( ( localModifier )* -> ^( LOCAL_MODIFIER_LIST ( localModifier )* ) )
                # Java.g:470:9: ( localModifier )*
                pass 
                # Java.g:470:9: ( localModifier )*
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == AT or LA55_0 == FINAL) :
                        alt55 = 1


                    if alt55 == 1:
                        # Java.g:470:9: localModifier
                        pass 
                        self._state.following.append(self.FOLLOW_localModifier_in_localModifierList6881)
                        localModifier163 = self.localModifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localModifier.add(localModifier163.tree)



                    else:
                        break #loop55


                # AST Rewrite
                # elements: localModifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 471:9: -> ^( LOCAL_MODIFIER_LIST ( localModifier )* )
                    # Java.g:471:12: ^( LOCAL_MODIFIER_LIST ( localModifier )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCAL_MODIFIER_LIST, "LOCAL_MODIFIER_LIST")
                    , root_1)

                    # Java.g:471:34: ( localModifier )*
                    while stream_localModifier.hasNext():
                        self._adaptor.addChild(root_1, stream_localModifier.nextTree())


                    stream_localModifier.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 39, localModifierList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "localModifierList"


    class localModifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.localModifier_return, self).__init__()

            self.tree = None





    # $ANTLR start "localModifier"
    # Java.g:474:1: localModifier : ( FINAL | annotation );
    def localModifier(self, ):
        retval = self.localModifier_return()
        retval.start = self.input.LT(1)

        localModifier_StartIndex = self.input.index()

        root_0 = None

        FINAL164 = None
        annotation165 = None


        FINAL164_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:475:5: ( FINAL | annotation )
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == FINAL) :
                    alt56 = 1
                elif (LA56_0 == AT) :
                    alt56 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 56, 0, self.input)

                    raise nvae


                if alt56 == 1:
                    # Java.g:475:9: FINAL
                    pass 
                    root_0 = self._adaptor.nil()


                    FINAL164 = self.match(self.input, FINAL, self.FOLLOW_FINAL_in_localModifier6922)
                    if self._state.backtracking == 0:
                        FINAL164_tree = self._adaptor.createWithPayload(FINAL164)
                        self._adaptor.addChild(root_0, FINAL164_tree)




                elif alt56 == 2:
                    # Java.g:476:9: annotation
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_annotation_in_localModifier6932)
                    annotation165 = self.annotation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotation165.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 40, localModifier_StartIndex, success)


            pass
        return retval

    # $ANTLR end "localModifier"


    class type_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.type_return, self).__init__()

            self.tree = None





    # $ANTLR start "type"
    # Java.g:479:1: type : ( simpleType | objectType );
    def type(self, ):
        retval = self.type_return()
        retval.start = self.input.LT(1)

        type_StartIndex = self.input.index()

        root_0 = None

        simpleType166 = None

        objectType167 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:480:5: ( simpleType | objectType )
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == BOOLEAN or LA57_0 == BYTE or LA57_0 == CHAR or LA57_0 == DOUBLE or LA57_0 == FLOAT or LA57_0 == INT or LA57_0 == LONG or LA57_0 == SHORT) :
                    alt57 = 1
                elif (LA57_0 == IDENT) :
                    alt57 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae


                if alt57 == 1:
                    # Java.g:480:9: simpleType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_simpleType_in_type6951)
                    simpleType166 = self.simpleType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simpleType166.tree)



                elif alt57 == 2:
                    # Java.g:481:9: objectType
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_objectType_in_type6961)
                    objectType167 = self.objectType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, objectType167.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 41, type_StartIndex, success)


            pass
        return retval

    # $ANTLR end "type"


    class simpleType_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.simpleType_return, self).__init__()

            self.tree = None





    # $ANTLR start "simpleType"
    # Java.g:484:1: simpleType : primitiveType ( arrayDeclaratorList )? -> ^( TYPE primitiveType ( arrayDeclaratorList )? ) ;
    def simpleType(self, ):
        retval = self.simpleType_return()
        retval.start = self.input.LT(1)

        simpleType_StartIndex = self.input.index()

        root_0 = None

        primitiveType168 = None

        arrayDeclaratorList169 = None


        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_primitiveType = RewriteRuleSubtreeStream(self._adaptor, "rule primitiveType")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:485:5: ( primitiveType ( arrayDeclaratorList )? -> ^( TYPE primitiveType ( arrayDeclaratorList )? ) )
                # Java.g:485:9: primitiveType ( arrayDeclaratorList )?
                pass 
                self._state.following.append(self.FOLLOW_primitiveType_in_simpleType6981)
                primitiveType168 = self.primitiveType()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_primitiveType.add(primitiveType168.tree)


                # Java.g:485:23: ( arrayDeclaratorList )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == LBRACK) :
                    LA58_1 = self.input.LA(2)

                    if (LA58_1 == RBRACK) :
                        LA58_3 = self.input.LA(3)

                        if (self.synpred76_Java()) :
                            alt58 = 1
                if alt58 == 1:
                    # Java.g:485:23: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_simpleType6983)
                    arrayDeclaratorList169 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arrayDeclaratorList.add(arrayDeclaratorList169.tree)





                # AST Rewrite
                # elements: arrayDeclaratorList, primitiveType
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 486:9: -> ^( TYPE primitiveType ( arrayDeclaratorList )? )
                    # Java.g:486:13: ^( TYPE primitiveType ( arrayDeclaratorList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TYPE, "TYPE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_primitiveType.nextTree())

                    # Java.g:486:34: ( arrayDeclaratorList )?
                    if stream_arrayDeclaratorList.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                    stream_arrayDeclaratorList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 42, simpleType_StartIndex, success)


            pass
        return retval

    # $ANTLR end "simpleType"


    class objectType_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.objectType_return, self).__init__()

            self.tree = None





    # $ANTLR start "objectType"
    # Java.g:489:1: objectType : qualifiedTypeIdent ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? ) ;
    def objectType(self, ):
        retval = self.objectType_return()
        retval.start = self.input.LT(1)

        objectType_StartIndex = self.input.index()

        root_0 = None

        qualifiedTypeIdent170 = None

        arrayDeclaratorList171 = None


        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_qualifiedTypeIdent = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedTypeIdent")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:490:5: ( qualifiedTypeIdent ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? ) )
                # Java.g:490:9: qualifiedTypeIdent ( arrayDeclaratorList )?
                pass 
                self._state.following.append(self.FOLLOW_qualifiedTypeIdent_in_objectType7030)
                qualifiedTypeIdent170 = self.qualifiedTypeIdent()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedTypeIdent.add(qualifiedTypeIdent170.tree)


                # Java.g:490:28: ( arrayDeclaratorList )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == LBRACK) :
                    LA59_1 = self.input.LA(2)

                    if (self.synpred77_Java()) :
                        alt59 = 1
                if alt59 == 1:
                    # Java.g:490:28: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_objectType7032)
                    arrayDeclaratorList171 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arrayDeclaratorList.add(arrayDeclaratorList171.tree)





                # AST Rewrite
                # elements: arrayDeclaratorList, qualifiedTypeIdent
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 491:9: -> ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? )
                    # Java.g:491:13: ^( TYPE qualifiedTypeIdent ( arrayDeclaratorList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TYPE, "TYPE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_qualifiedTypeIdent.nextTree())

                    # Java.g:491:39: ( arrayDeclaratorList )?
                    if stream_arrayDeclaratorList.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                    stream_arrayDeclaratorList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 43, objectType_StartIndex, success)


            pass
        return retval

    # $ANTLR end "objectType"


    class objectTypeSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.objectTypeSimplified_return, self).__init__()

            self.tree = None





    # $ANTLR start "objectTypeSimplified"
    # Java.g:494:1: objectTypeSimplified : qualifiedTypeIdentSimplified ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? ) ;
    def objectTypeSimplified(self, ):
        retval = self.objectTypeSimplified_return()
        retval.start = self.input.LT(1)

        objectTypeSimplified_StartIndex = self.input.index()

        root_0 = None

        qualifiedTypeIdentSimplified172 = None

        arrayDeclaratorList173 = None


        stream_arrayDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclaratorList")
        stream_qualifiedTypeIdentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedTypeIdentSimplified")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:495:5: ( qualifiedTypeIdentSimplified ( arrayDeclaratorList )? -> ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? ) )
                # Java.g:495:9: qualifiedTypeIdentSimplified ( arrayDeclaratorList )?
                pass 
                self._state.following.append(self.FOLLOW_qualifiedTypeIdentSimplified_in_objectTypeSimplified7072)
                qualifiedTypeIdentSimplified172 = self.qualifiedTypeIdentSimplified()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedTypeIdentSimplified.add(qualifiedTypeIdentSimplified172.tree)


                # Java.g:495:38: ( arrayDeclaratorList )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == LBRACK) :
                    alt60 = 1
                if alt60 == 1:
                    # Java.g:495:38: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_objectTypeSimplified7074)
                    arrayDeclaratorList173 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arrayDeclaratorList.add(arrayDeclaratorList173.tree)





                # AST Rewrite
                # elements: arrayDeclaratorList, qualifiedTypeIdentSimplified
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 496:9: -> ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? )
                    # Java.g:496:13: ^( TYPE qualifiedTypeIdentSimplified ( arrayDeclaratorList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TYPE, "TYPE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_qualifiedTypeIdentSimplified.nextTree())

                    # Java.g:496:49: ( arrayDeclaratorList )?
                    if stream_arrayDeclaratorList.hasNext():
                        self._adaptor.addChild(root_1, stream_arrayDeclaratorList.nextTree())


                    stream_arrayDeclaratorList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 44, objectTypeSimplified_StartIndex, success)


            pass
        return retval

    # $ANTLR end "objectTypeSimplified"


    class qualifiedTypeIdent_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.qualifiedTypeIdent_return, self).__init__()

            self.tree = None





    # $ANTLR start "qualifiedTypeIdent"
    # Java.g:499:1: qualifiedTypeIdent : typeIdent ( DOT typeIdent )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ ) ;
    def qualifiedTypeIdent(self, ):
        retval = self.qualifiedTypeIdent_return()
        retval.start = self.input.LT(1)

        qualifiedTypeIdent_StartIndex = self.input.index()

        root_0 = None

        DOT175 = None
        typeIdent174 = None

        typeIdent176 = None


        DOT175_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_typeIdent = RewriteRuleSubtreeStream(self._adaptor, "rule typeIdent")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:500:5: ( typeIdent ( DOT typeIdent )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ ) )
                # Java.g:500:9: typeIdent ( DOT typeIdent )*
                pass 
                self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent7114)
                typeIdent174 = self.typeIdent()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeIdent.add(typeIdent174.tree)


                # Java.g:500:19: ( DOT typeIdent )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == DOT) :
                        LA61_2 = self.input.LA(2)

                        if (self.synpred79_Java()) :
                            alt61 = 1




                    if alt61 == 1:
                        # Java.g:500:20: DOT typeIdent
                        pass 
                        DOT175 = self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedTypeIdent7117) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT175)


                        self._state.following.append(self.FOLLOW_typeIdent_in_qualifiedTypeIdent7119)
                        typeIdent176 = self.typeIdent()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_typeIdent.add(typeIdent176.tree)



                    else:
                        break #loop61


                # AST Rewrite
                # elements: typeIdent
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 501:9: -> ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ )
                    # Java.g:501:13: ^( QUALIFIED_TYPE_IDENT ( typeIdent )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(QUALIFIED_TYPE_IDENT, "QUALIFIED_TYPE_IDENT")
                    , root_1)

                    # Java.g:501:36: ( typeIdent )+
                    if not (stream_typeIdent.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_typeIdent.hasNext():
                        self._adaptor.addChild(root_1, stream_typeIdent.nextTree())


                    stream_typeIdent.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 45, qualifiedTypeIdent_StartIndex, success)


            pass
        return retval

    # $ANTLR end "qualifiedTypeIdent"


    class qualifiedTypeIdentSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.qualifiedTypeIdentSimplified_return, self).__init__()

            self.tree = None





    # $ANTLR start "qualifiedTypeIdentSimplified"
    # Java.g:504:1: qualifiedTypeIdentSimplified : typeIdentSimplified ( DOT typeIdentSimplified )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ ) ;
    def qualifiedTypeIdentSimplified(self, ):
        retval = self.qualifiedTypeIdentSimplified_return()
        retval.start = self.input.LT(1)

        qualifiedTypeIdentSimplified_StartIndex = self.input.index()

        root_0 = None

        DOT178 = None
        typeIdentSimplified177 = None

        typeIdentSimplified179 = None


        DOT178_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_typeIdentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule typeIdentSimplified")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:505:5: ( typeIdentSimplified ( DOT typeIdentSimplified )* -> ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ ) )
                # Java.g:505:9: typeIdentSimplified ( DOT typeIdentSimplified )*
                pass 
                self._state.following.append(self.FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7159)
                typeIdentSimplified177 = self.typeIdentSimplified()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typeIdentSimplified.add(typeIdentSimplified177.tree)


                # Java.g:505:29: ( DOT typeIdentSimplified )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == DOT) :
                        alt62 = 1


                    if alt62 == 1:
                        # Java.g:505:30: DOT typeIdentSimplified
                        pass 
                        DOT178 = self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedTypeIdentSimplified7162) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT178)


                        self._state.following.append(self.FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7164)
                        typeIdentSimplified179 = self.typeIdentSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_typeIdentSimplified.add(typeIdentSimplified179.tree)



                    else:
                        break #loop62


                # AST Rewrite
                # elements: typeIdentSimplified
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 506:9: -> ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ )
                    # Java.g:506:13: ^( QUALIFIED_TYPE_IDENT ( typeIdentSimplified )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(QUALIFIED_TYPE_IDENT, "QUALIFIED_TYPE_IDENT")
                    , root_1)

                    # Java.g:506:36: ( typeIdentSimplified )+
                    if not (stream_typeIdentSimplified.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_typeIdentSimplified.hasNext():
                        self._adaptor.addChild(root_1, stream_typeIdentSimplified.nextTree())


                    stream_typeIdentSimplified.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 46, qualifiedTypeIdentSimplified_StartIndex, success)


            pass
        return retval

    # $ANTLR end "qualifiedTypeIdentSimplified"


    class typeIdent_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.typeIdent_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeIdent"
    # Java.g:509:1: typeIdent : IDENT ^ ( genericTypeArgumentList )? ;
    def typeIdent(self, ):
        retval = self.typeIdent_return()
        retval.start = self.input.LT(1)

        typeIdent_StartIndex = self.input.index()

        root_0 = None

        IDENT180 = None
        genericTypeArgumentList181 = None


        IDENT180_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:510:5: ( IDENT ^ ( genericTypeArgumentList )? )
                # Java.g:510:9: IDENT ^ ( genericTypeArgumentList )?
                pass 
                root_0 = self._adaptor.nil()


                IDENT180 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdent7204)
                if self._state.backtracking == 0:
                    IDENT180_tree = self._adaptor.createWithPayload(IDENT180)
                    root_0 = self._adaptor.becomeRoot(IDENT180_tree, root_0)



                # Java.g:510:16: ( genericTypeArgumentList )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == LESS_THAN) :
                    alt63 = 1
                if alt63 == 1:
                    # Java.g:510:16: genericTypeArgumentList
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentList_in_typeIdent7207)
                    genericTypeArgumentList181 = self.genericTypeArgumentList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, genericTypeArgumentList181.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 47, typeIdent_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typeIdent"


    class typeIdentSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.typeIdentSimplified_return, self).__init__()

            self.tree = None





    # $ANTLR start "typeIdentSimplified"
    # Java.g:513:1: typeIdentSimplified : IDENT ^ ( genericTypeArgumentListSimplified )? ;
    def typeIdentSimplified(self, ):
        retval = self.typeIdentSimplified_return()
        retval.start = self.input.LT(1)

        typeIdentSimplified_StartIndex = self.input.index()

        root_0 = None

        IDENT182 = None
        genericTypeArgumentListSimplified183 = None


        IDENT182_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:514:5: ( IDENT ^ ( genericTypeArgumentListSimplified )? )
                # Java.g:514:9: IDENT ^ ( genericTypeArgumentListSimplified )?
                pass 
                root_0 = self._adaptor.nil()


                IDENT182 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_typeIdentSimplified7227)
                if self._state.backtracking == 0:
                    IDENT182_tree = self._adaptor.createWithPayload(IDENT182)
                    root_0 = self._adaptor.becomeRoot(IDENT182_tree, root_0)



                # Java.g:514:16: ( genericTypeArgumentListSimplified )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == LESS_THAN) :
                    alt64 = 1
                if alt64 == 1:
                    # Java.g:514:16: genericTypeArgumentListSimplified
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_typeIdentSimplified7230)
                    genericTypeArgumentListSimplified183 = self.genericTypeArgumentListSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, genericTypeArgumentListSimplified183.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 48, typeIdentSimplified_StartIndex, success)


            pass
        return retval

    # $ANTLR end "typeIdentSimplified"


    class primitiveType_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.primitiveType_return, self).__init__()

            self.tree = None





    # $ANTLR start "primitiveType"
    # Java.g:517:1: primitiveType : ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE );
    def primitiveType(self, ):
        retval = self.primitiveType_return()
        retval.start = self.input.LT(1)

        primitiveType_StartIndex = self.input.index()

        root_0 = None

        set184 = None

        set184_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:518:5: ( BOOLEAN | CHAR | BYTE | SHORT | INT | LONG | FLOAT | DOUBLE )
                # Java.g:
                pass 
                root_0 = self._adaptor.nil()


                set184 = self.input.LT(1)

                if self.input.LA(1) == BOOLEAN or self.input.LA(1) == BYTE or self.input.LA(1) == CHAR or self.input.LA(1) == DOUBLE or self.input.LA(1) == FLOAT or self.input.LA(1) == INT or self.input.LA(1) == LONG or self.input.LA(1) == SHORT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set184))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 49, primitiveType_StartIndex, success)


            pass
        return retval

    # $ANTLR end "primitiveType"


    class genericTypeArgumentList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeArgumentList_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeArgumentList"
    # Java.g:528:1: genericTypeArgumentList : LESS_THAN genericTypeArgument ( COMMA genericTypeArgument )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ ) ;
    def genericTypeArgumentList(self, ):
        retval = self.genericTypeArgumentList_return()
        retval.start = self.input.LT(1)

        genericTypeArgumentList_StartIndex = self.input.index()

        root_0 = None

        LESS_THAN185 = None
        COMMA187 = None
        genericTypeArgument186 = None

        genericTypeArgument188 = None

        genericTypeListClosing189 = None


        LESS_THAN185_tree = None
        COMMA187_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LESS_THAN = RewriteRuleTokenStream(self._adaptor, "token LESS_THAN")
        stream_genericTypeArgument = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgument")
        stream_genericTypeListClosing = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeListClosing")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:529:5: ( LESS_THAN genericTypeArgument ( COMMA genericTypeArgument )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ ) )
                # Java.g:529:9: LESS_THAN genericTypeArgument ( COMMA genericTypeArgument )* genericTypeListClosing
                pass 
                LESS_THAN185 = self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_genericTypeArgumentList7339) 
                if self._state.backtracking == 0:
                    stream_LESS_THAN.add(LESS_THAN185)


                self._state.following.append(self.FOLLOW_genericTypeArgument_in_genericTypeArgumentList7341)
                genericTypeArgument186 = self.genericTypeArgument()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeArgument.add(genericTypeArgument186.tree)


                # Java.g:529:39: ( COMMA genericTypeArgument )*
                while True: #loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == COMMA) :
                        LA65_2 = self.input.LA(2)

                        if (self.synpred90_Java()) :
                            alt65 = 1




                    if alt65 == 1:
                        # Java.g:529:40: COMMA genericTypeArgument
                        pass 
                        COMMA187 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_genericTypeArgumentList7344) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA187)


                        self._state.following.append(self.FOLLOW_genericTypeArgument_in_genericTypeArgumentList7346)
                        genericTypeArgument188 = self.genericTypeArgument()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgument.add(genericTypeArgument188.tree)



                    else:
                        break #loop65


                self._state.following.append(self.FOLLOW_genericTypeListClosing_in_genericTypeArgumentList7350)
                genericTypeListClosing189 = self.genericTypeListClosing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeListClosing.add(genericTypeListClosing189.tree)


                # AST Rewrite
                # elements: genericTypeArgument
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 530:9: -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ )
                    # Java.g:530:13: ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgument )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(GENERIC_TYPE_ARG_LIST, LESS_THAN185, "GENERIC_TYPE_ARG_LIST")
                    , root_1)

                    # Java.g:530:74: ( genericTypeArgument )+
                    if not (stream_genericTypeArgument.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_genericTypeArgument.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeArgument.nextTree())


                    stream_genericTypeArgument.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 50, genericTypeArgumentList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeArgumentList"


    class genericTypeArgument_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeArgument_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeArgument"
    # Java.g:533:1: genericTypeArgument : ( type | QUESTION ( genericWildcardBoundType )? -> ^( QUESTION ( genericWildcardBoundType )? ) );
    def genericTypeArgument(self, ):
        retval = self.genericTypeArgument_return()
        retval.start = self.input.LT(1)

        genericTypeArgument_StartIndex = self.input.index()

        root_0 = None

        QUESTION191 = None
        type190 = None

        genericWildcardBoundType192 = None


        QUESTION191_tree = None
        stream_QUESTION = RewriteRuleTokenStream(self._adaptor, "token QUESTION")
        stream_genericWildcardBoundType = RewriteRuleSubtreeStream(self._adaptor, "rule genericWildcardBoundType")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:534:5: ( type | QUESTION ( genericWildcardBoundType )? -> ^( QUESTION ( genericWildcardBoundType )? ) )
                alt67 = 2
                LA67_0 = self.input.LA(1)

                if (LA67_0 == BOOLEAN or LA67_0 == BYTE or LA67_0 == CHAR or LA67_0 == DOUBLE or LA67_0 == FLOAT or LA67_0 == IDENT or LA67_0 == INT or LA67_0 == LONG or LA67_0 == SHORT) :
                    alt67 = 1
                elif (LA67_0 == QUESTION) :
                    alt67 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 67, 0, self.input)

                    raise nvae


                if alt67 == 1:
                    # Java.g:534:9: type
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgument7388)
                    type190 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type190.tree)



                elif alt67 == 2:
                    # Java.g:535:9: QUESTION ( genericWildcardBoundType )?
                    pass 
                    QUESTION191 = self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgument7398) 
                    if self._state.backtracking == 0:
                        stream_QUESTION.add(QUESTION191)


                    # Java.g:535:18: ( genericWildcardBoundType )?
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == EXTENDS) :
                        LA66_1 = self.input.LA(2)

                        if (LA66_1 == BOOLEAN or LA66_1 == BYTE or LA66_1 == CHAR or LA66_1 == DOUBLE or LA66_1 == FLOAT or LA66_1 == INT or LA66_1 == LONG or LA66_1 == SHORT) :
                            LA66_4 = self.input.LA(3)

                            if (self.synpred92_Java()) :
                                alt66 = 1
                        elif (LA66_1 == IDENT) :
                            LA66_5 = self.input.LA(3)

                            if (self.synpred92_Java()) :
                                alt66 = 1
                    elif (LA66_0 == SUPER) :
                        LA66_3 = self.input.LA(2)

                        if (LA66_3 == BOOLEAN or LA66_3 == BYTE or LA66_3 == CHAR or LA66_3 == DOUBLE or LA66_3 == FLOAT or LA66_3 == IDENT or LA66_3 == INT or LA66_3 == LONG or LA66_3 == SHORT) :
                            alt66 = 1
                    if alt66 == 1:
                        # Java.g:535:18: genericWildcardBoundType
                        pass 
                        self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_genericTypeArgument7400)
                        genericWildcardBoundType192 = self.genericWildcardBoundType()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericWildcardBoundType.add(genericWildcardBoundType192.tree)





                    # AST Rewrite
                    # elements: QUESTION, genericWildcardBoundType
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 536:9: -> ^( QUESTION ( genericWildcardBoundType )? )
                        # Java.g:536:13: ^( QUESTION ( genericWildcardBoundType )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_QUESTION.nextNode()
                        , root_1)

                        # Java.g:536:24: ( genericWildcardBoundType )?
                        if stream_genericWildcardBoundType.hasNext():
                            self._adaptor.addChild(root_1, stream_genericWildcardBoundType.nextTree())


                        stream_genericWildcardBoundType.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 51, genericTypeArgument_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeArgument"


    class genericWildcardBoundType_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericWildcardBoundType_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericWildcardBoundType"
    # Java.g:539:1: genericWildcardBoundType : ( EXTENDS | SUPER ) ^ type ;
    def genericWildcardBoundType(self, ):
        retval = self.genericWildcardBoundType_return()
        retval.start = self.input.LT(1)

        genericWildcardBoundType_StartIndex = self.input.index()

        root_0 = None

        set193 = None
        type194 = None


        set193_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:540:5: ( ( EXTENDS | SUPER ) ^ type )
                # Java.g:540:9: ( EXTENDS | SUPER ) ^ type
                pass 
                root_0 = self._adaptor.nil()


                set193 = self.input.LT(1)

                set193 = self.input.LT(1)

                if self.input.LA(1) == EXTENDS or self.input.LA(1) == SUPER:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set193), root_0)

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self._state.following.append(self.FOLLOW_type_in_genericWildcardBoundType7451)
                type194 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, type194.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 52, genericWildcardBoundType_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericWildcardBoundType"


    class genericTypeArgumentListSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeArgumentListSimplified_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeArgumentListSimplified"
    # Java.g:543:1: genericTypeArgumentListSimplified : LESS_THAN genericTypeArgumentSimplified ( COMMA genericTypeArgumentSimplified )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ ) ;
    def genericTypeArgumentListSimplified(self, ):
        retval = self.genericTypeArgumentListSimplified_return()
        retval.start = self.input.LT(1)

        genericTypeArgumentListSimplified_StartIndex = self.input.index()

        root_0 = None

        LESS_THAN195 = None
        COMMA197 = None
        genericTypeArgumentSimplified196 = None

        genericTypeArgumentSimplified198 = None

        genericTypeListClosing199 = None


        LESS_THAN195_tree = None
        COMMA197_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LESS_THAN = RewriteRuleTokenStream(self._adaptor, "token LESS_THAN")
        stream_genericTypeArgumentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentSimplified")
        stream_genericTypeListClosing = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeListClosing")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:544:5: ( LESS_THAN genericTypeArgumentSimplified ( COMMA genericTypeArgumentSimplified )* genericTypeListClosing -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ ) )
                # Java.g:544:9: LESS_THAN genericTypeArgumentSimplified ( COMMA genericTypeArgumentSimplified )* genericTypeListClosing
                pass 
                LESS_THAN195 = self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_genericTypeArgumentListSimplified7470) 
                if self._state.backtracking == 0:
                    stream_LESS_THAN.add(LESS_THAN195)


                self._state.following.append(self.FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7472)
                genericTypeArgumentSimplified196 = self.genericTypeArgumentSimplified()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeArgumentSimplified.add(genericTypeArgumentSimplified196.tree)


                # Java.g:544:49: ( COMMA genericTypeArgumentSimplified )*
                while True: #loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if (LA68_0 == COMMA) :
                        alt68 = 1


                    if alt68 == 1:
                        # Java.g:544:50: COMMA genericTypeArgumentSimplified
                        pass 
                        COMMA197 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_genericTypeArgumentListSimplified7475) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA197)


                        self._state.following.append(self.FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7477)
                        genericTypeArgumentSimplified198 = self.genericTypeArgumentSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgumentSimplified.add(genericTypeArgumentSimplified198.tree)



                    else:
                        break #loop68


                self._state.following.append(self.FOLLOW_genericTypeListClosing_in_genericTypeArgumentListSimplified7481)
                genericTypeListClosing199 = self.genericTypeListClosing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_genericTypeListClosing.add(genericTypeListClosing199.tree)


                # AST Rewrite
                # elements: genericTypeArgumentSimplified
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 545:9: -> ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ )
                    # Java.g:545:13: ^( GENERIC_TYPE_ARG_LIST[$LESS_THAN, \"GENERIC_TYPE_ARG_LIST\"] ( genericTypeArgumentSimplified )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(GENERIC_TYPE_ARG_LIST, LESS_THAN195, "GENERIC_TYPE_ARG_LIST")
                    , root_1)

                    # Java.g:545:74: ( genericTypeArgumentSimplified )+
                    if not (stream_genericTypeArgumentSimplified.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_genericTypeArgumentSimplified.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeArgumentSimplified.nextTree())


                    stream_genericTypeArgumentSimplified.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 53, genericTypeArgumentListSimplified_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeArgumentListSimplified"


    class genericTypeArgumentSimplified_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.genericTypeArgumentSimplified_return, self).__init__()

            self.tree = None





    # $ANTLR start "genericTypeArgumentSimplified"
    # Java.g:548:1: genericTypeArgumentSimplified : ( type | QUESTION );
    def genericTypeArgumentSimplified(self, ):
        retval = self.genericTypeArgumentSimplified_return()
        retval.start = self.input.LT(1)

        genericTypeArgumentSimplified_StartIndex = self.input.index()

        root_0 = None

        QUESTION201 = None
        type200 = None


        QUESTION201_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:549:5: ( type | QUESTION )
                alt69 = 2
                LA69_0 = self.input.LA(1)

                if (LA69_0 == BOOLEAN or LA69_0 == BYTE or LA69_0 == CHAR or LA69_0 == DOUBLE or LA69_0 == FLOAT or LA69_0 == IDENT or LA69_0 == INT or LA69_0 == LONG or LA69_0 == SHORT) :
                    alt69 = 1
                elif (LA69_0 == QUESTION) :
                    alt69 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 69, 0, self.input)

                    raise nvae


                if alt69 == 1:
                    # Java.g:549:9: type
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_type_in_genericTypeArgumentSimplified7523)
                    type200 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type200.tree)



                elif alt69 == 2:
                    # Java.g:550:9: QUESTION
                    pass 
                    root_0 = self._adaptor.nil()


                    QUESTION201 = self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_genericTypeArgumentSimplified7533)
                    if self._state.backtracking == 0:
                        QUESTION201_tree = self._adaptor.createWithPayload(QUESTION201)
                        self._adaptor.addChild(root_0, QUESTION201_tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 54, genericTypeArgumentSimplified_StartIndex, success)


            pass
        return retval

    # $ANTLR end "genericTypeArgumentSimplified"


    class qualifiedIdentList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.qualifiedIdentList_return, self).__init__()

            self.tree = None





    # $ANTLR start "qualifiedIdentList"
    # Java.g:553:1: qualifiedIdentList : qualifiedIdentifier ( COMMA ! qualifiedIdentifier )* ;
    def qualifiedIdentList(self, ):
        retval = self.qualifiedIdentList_return()
        retval.start = self.input.LT(1)

        qualifiedIdentList_StartIndex = self.input.index()

        root_0 = None

        COMMA203 = None
        qualifiedIdentifier202 = None

        qualifiedIdentifier204 = None


        COMMA203_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:554:5: ( qualifiedIdentifier ( COMMA ! qualifiedIdentifier )* )
                # Java.g:554:9: qualifiedIdentifier ( COMMA ! qualifiedIdentifier )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7556)
                qualifiedIdentifier202 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier202.tree)


                # Java.g:554:29: ( COMMA ! qualifiedIdentifier )*
                while True: #loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == COMMA) :
                        alt70 = 1


                    if alt70 == 1:
                        # Java.g:554:30: COMMA ! qualifiedIdentifier
                        pass 
                        COMMA203 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_qualifiedIdentList7559)

                        self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7562)
                        qualifiedIdentifier204 = self.qualifiedIdentifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, qualifiedIdentifier204.tree)



                    else:
                        break #loop70




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 55, qualifiedIdentList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "qualifiedIdentList"


    class formalParameterList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.formalParameterList_return, self).__init__()

            self.tree = None





    # $ANTLR start "formalParameterList"
    # Java.g:557:1: formalParameterList : LPAREN ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) ) RPAREN ;
    def formalParameterList(self, ):
        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)

        formalParameterList_StartIndex = self.input.index()

        root_0 = None

        LPAREN205 = None
        COMMA207 = None
        COMMA209 = None
        RPAREN212 = None
        formalParameterStandardDecl206 = None

        formalParameterStandardDecl208 = None

        formalParameterVarArgDecl210 = None

        formalParameterVarArgDecl211 = None


        LPAREN205_tree = None
        COMMA207_tree = None
        COMMA209_tree = None
        RPAREN212_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_formalParameterVarArgDecl = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterVarArgDecl")
        stream_formalParameterStandardDecl = RewriteRuleSubtreeStream(self._adaptor, "rule formalParameterStandardDecl")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:558:5: ( LPAREN ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) ) RPAREN )
                # Java.g:558:9: LPAREN ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) ) RPAREN
                pass 
                LPAREN205 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_formalParameterList7587) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN205)


                # Java.g:559:9: ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? ) | formalParameterVarArgDecl -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl ) | -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ) )
                alt73 = 3
                LA73 = self.input.LA(1)
                if LA73 == FINAL:
                    LA73_1 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 73, 1, self.input)

                        raise nvae


                elif LA73 == AT:
                    LA73_2 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 73, 2, self.input)

                        raise nvae


                elif LA73 == BOOLEAN or LA73 == BYTE or LA73 == CHAR or LA73 == DOUBLE or LA73 == FLOAT or LA73 == INT or LA73 == LONG or LA73 == SHORT:
                    LA73_3 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 73, 3, self.input)

                        raise nvae


                elif LA73 == IDENT:
                    LA73_4 = self.input.LA(2)

                    if (self.synpred99_Java()) :
                        alt73 = 1
                    elif (self.synpred100_Java()) :
                        alt73 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 73, 4, self.input)

                        raise nvae


                elif LA73 == RPAREN:
                    alt73 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 73, 0, self.input)

                    raise nvae


                if alt73 == 1:
                    # Java.g:560:13: formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )?
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList7615)
                    formalParameterStandardDecl206 = self.formalParameterStandardDecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_formalParameterStandardDecl.add(formalParameterStandardDecl206.tree)


                    # Java.g:560:41: ( COMMA formalParameterStandardDecl )*
                    while True: #loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if (LA71_0 == COMMA) :
                            LA71_1 = self.input.LA(2)

                            if (self.synpred97_Java()) :
                                alt71 = 1




                        if alt71 == 1:
                            # Java.g:560:42: COMMA formalParameterStandardDecl
                            pass 
                            COMMA207 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_formalParameterList7618) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA207)


                            self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_formalParameterList7620)
                            formalParameterStandardDecl208 = self.formalParameterStandardDecl()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_formalParameterStandardDecl.add(formalParameterStandardDecl208.tree)



                        else:
                            break #loop71


                    # Java.g:560:78: ( COMMA formalParameterVarArgDecl )?
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == COMMA) :
                        alt72 = 1
                    if alt72 == 1:
                        # Java.g:560:79: COMMA formalParameterVarArgDecl
                        pass 
                        COMMA209 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_formalParameterList7625) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA209)


                        self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_formalParameterList7627)
                        formalParameterVarArgDecl210 = self.formalParameterVarArgDecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_formalParameterVarArgDecl.add(formalParameterVarArgDecl210.tree)





                    # AST Rewrite
                    # elements: formalParameterVarArgDecl, formalParameterStandardDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 561:13: -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? )
                        # Java.g:561:17: ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] ( formalParameterStandardDecl )+ ( formalParameterVarArgDecl )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(FORMAL_PARAM_LIST, LPAREN205, "FORMAL_PARAM_LIST")
                        , root_1)

                        # Java.g:561:67: ( formalParameterStandardDecl )+
                        if not (stream_formalParameterStandardDecl.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_formalParameterStandardDecl.hasNext():
                            self._adaptor.addChild(root_1, stream_formalParameterStandardDecl.nextTree())


                        stream_formalParameterStandardDecl.reset()

                        # Java.g:561:96: ( formalParameterVarArgDecl )?
                        if stream_formalParameterVarArgDecl.hasNext():
                            self._adaptor.addChild(root_1, stream_formalParameterVarArgDecl.nextTree())


                        stream_formalParameterVarArgDecl.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt73 == 2:
                    # Java.g:563:13: formalParameterVarArgDecl
                    pass 
                    self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_formalParameterList7684)
                    formalParameterVarArgDecl211 = self.formalParameterVarArgDecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_formalParameterVarArgDecl.add(formalParameterVarArgDecl211.tree)


                    # AST Rewrite
                    # elements: formalParameterVarArgDecl
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 564:13: -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl )
                        # Java.g:564:17: ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] formalParameterVarArgDecl )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(FORMAL_PARAM_LIST, LPAREN205, "FORMAL_PARAM_LIST")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_formalParameterVarArgDecl.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt73 == 3:
                    # Java.g:566:13: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 566:13: -> ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] )
                        # Java.g:566:17: ^( FORMAL_PARAM_LIST[$LPAREN, \"FORMAL_PARAM_LIST\"] )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(FORMAL_PARAM_LIST, LPAREN205, "FORMAL_PARAM_LIST")
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0






                RPAREN212 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_formalParameterList7761) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN212)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 56, formalParameterList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "formalParameterList"


    class formalParameterStandardDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.formalParameterStandardDecl_return, self).__init__()

            self.tree = None





    # $ANTLR start "formalParameterStandardDecl"
    # Java.g:571:1: formalParameterStandardDecl : localModifierList type variableDeclaratorId -> ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId ) ;
    def formalParameterStandardDecl(self, ):
        retval = self.formalParameterStandardDecl_return()
        retval.start = self.input.LT(1)

        formalParameterStandardDecl_StartIndex = self.input.index()

        root_0 = None

        localModifierList213 = None

        type214 = None

        variableDeclaratorId215 = None


        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:572:5: ( localModifierList type variableDeclaratorId -> ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId ) )
                # Java.g:572:9: localModifierList type variableDeclaratorId
                pass 
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterStandardDecl7784)
                localModifierList213 = self.localModifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localModifierList.add(localModifierList213.tree)


                self._state.following.append(self.FOLLOW_type_in_formalParameterStandardDecl7786)
                type214 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type214.tree)


                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl7788)
                variableDeclaratorId215 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId215.tree)


                # AST Rewrite
                # elements: localModifierList, type, variableDeclaratorId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 573:9: -> ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId )
                    # Java.g:573:13: ^( FORMAL_PARAM_STD_DECL localModifierList type variableDeclaratorId )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(FORMAL_PARAM_STD_DECL, "FORMAL_PARAM_STD_DECL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_localModifierList.nextTree())

                    self._adaptor.addChild(root_1, stream_type.nextTree())

                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 57, formalParameterStandardDecl_StartIndex, success)


            pass
        return retval

    # $ANTLR end "formalParameterStandardDecl"


    class formalParameterVarArgDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.formalParameterVarArgDecl_return, self).__init__()

            self.tree = None





    # $ANTLR start "formalParameterVarArgDecl"
    # Java.g:576:1: formalParameterVarArgDecl : localModifierList type ELLIPSIS variableDeclaratorId -> ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId ) ;
    def formalParameterVarArgDecl(self, ):
        retval = self.formalParameterVarArgDecl_return()
        retval.start = self.input.LT(1)

        formalParameterVarArgDecl_StartIndex = self.input.index()

        root_0 = None

        ELLIPSIS218 = None
        localModifierList216 = None

        type217 = None

        variableDeclaratorId219 = None


        ELLIPSIS218_tree = None
        stream_ELLIPSIS = RewriteRuleTokenStream(self._adaptor, "token ELLIPSIS")
        stream_variableDeclaratorId = RewriteRuleSubtreeStream(self._adaptor, "rule variableDeclaratorId")
        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:577:5: ( localModifierList type ELLIPSIS variableDeclaratorId -> ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId ) )
                # Java.g:577:9: localModifierList type ELLIPSIS variableDeclaratorId
                pass 
                self._state.following.append(self.FOLLOW_localModifierList_in_formalParameterVarArgDecl7832)
                localModifierList216 = self.localModifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localModifierList.add(localModifierList216.tree)


                self._state.following.append(self.FOLLOW_type_in_formalParameterVarArgDecl7834)
                type217 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type217.tree)


                ELLIPSIS218 = self.match(self.input, ELLIPSIS, self.FOLLOW_ELLIPSIS_in_formalParameterVarArgDecl7836) 
                if self._state.backtracking == 0:
                    stream_ELLIPSIS.add(ELLIPSIS218)


                self._state.following.append(self.FOLLOW_variableDeclaratorId_in_formalParameterVarArgDecl7838)
                variableDeclaratorId219 = self.variableDeclaratorId()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variableDeclaratorId.add(variableDeclaratorId219.tree)


                # AST Rewrite
                # elements: localModifierList, variableDeclaratorId, type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 578:9: -> ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId )
                    # Java.g:578:13: ^( FORMAL_PARAM_VARARG_DECL localModifierList type variableDeclaratorId )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(FORMAL_PARAM_VARARG_DECL, "FORMAL_PARAM_VARARG_DECL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_localModifierList.nextTree())

                    self._adaptor.addChild(root_1, stream_type.nextTree())

                    self._adaptor.addChild(root_1, stream_variableDeclaratorId.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 58, formalParameterVarArgDecl_StartIndex, success)


            pass
        return retval

    # $ANTLR end "formalParameterVarArgDecl"


    class qualifiedIdentifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.qualifiedIdentifier_return, self).__init__()

            self.tree = None





    # $ANTLR start "qualifiedIdentifier"
    # Java.g:581:1: qualifiedIdentifier : ( IDENT -> IDENT ) ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )* ;
    def qualifiedIdentifier(self, ):
        retval = self.qualifiedIdentifier_return()
        retval.start = self.input.LT(1)

        qualifiedIdentifier_StartIndex = self.input.index()

        root_0 = None

        ident = None
        IDENT220 = None
        DOT221 = None

        ident_tree = None
        IDENT220_tree = None
        DOT221_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:582:5: ( ( IDENT -> IDENT ) ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )* )
                # Java.g:582:9: ( IDENT -> IDENT ) ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )*
                pass 
                # Java.g:582:9: ( IDENT -> IDENT )
                # Java.g:582:13: IDENT
                pass 
                IDENT220 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier7886) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT220)


                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 582:33: -> IDENT
                    self._adaptor.addChild(root_0, 
                    stream_IDENT.nextNode()
                    )




                    retval.tree = root_0






                # Java.g:584:9: ( DOT ident= IDENT -> ^( DOT $qualifiedIdentifier $ident) )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == DOT) :
                        LA74_2 = self.input.LA(2)

                        if (LA74_2 == IDENT) :
                            LA74_3 = self.input.LA(3)

                            if (self.synpred101_Java()) :
                                alt74 = 1






                    if alt74 == 1:
                        # Java.g:584:13: DOT ident= IDENT
                        pass 
                        DOT221 = self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentifier7929) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT221)


                        ident = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentifier7933) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(ident)


                        # AST Rewrite
                        # elements: DOT, qualifiedIdentifier, ident
                        # token labels: ident
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            stream_ident = RewriteRuleTokenStream(self._adaptor, "token ident", ident)
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 584:33: -> ^( DOT $qualifiedIdentifier $ident)
                            # Java.g:584:37: ^( DOT $qualifiedIdentifier $ident)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_DOT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_retval.nextTree())

                            self._adaptor.addChild(root_1, stream_ident.nextNode())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    else:
                        break #loop74




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 59, qualifiedIdentifier_StartIndex, success)


            pass
        return retval

    # $ANTLR end "qualifiedIdentifier"


    class annotationList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationList_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationList"
    # Java.g:590:1: annotationList : ( annotation )* -> ^( ANNOTATION_LIST ( annotation )* ) ;
    def annotationList(self, ):
        retval = self.annotationList_return()
        retval.start = self.input.LT(1)

        annotationList_StartIndex = self.input.index()

        root_0 = None

        annotation222 = None


        stream_annotation = RewriteRuleSubtreeStream(self._adaptor, "rule annotation")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:591:5: ( ( annotation )* -> ^( ANNOTATION_LIST ( annotation )* ) )
                # Java.g:591:9: ( annotation )*
                pass 
                # Java.g:591:9: ( annotation )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == AT) :
                        LA75_2 = self.input.LA(2)

                        if (LA75_2 == IDENT) :
                            LA75_3 = self.input.LA(3)

                            if (self.synpred102_Java()) :
                                alt75 = 1






                    if alt75 == 1:
                        # Java.g:591:9: annotation
                        pass 
                        self._state.following.append(self.FOLLOW_annotation_in_annotationList7986)
                        annotation222 = self.annotation()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_annotation.add(annotation222.tree)



                    else:
                        break #loop75


                # AST Rewrite
                # elements: annotation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 592:9: -> ^( ANNOTATION_LIST ( annotation )* )
                    # Java.g:592:13: ^( ANNOTATION_LIST ( annotation )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANNOTATION_LIST, "ANNOTATION_LIST")
                    , root_1)

                    # Java.g:592:31: ( annotation )*
                    while stream_annotation.hasNext():
                        self._adaptor.addChild(root_1, stream_annotation.nextTree())


                    stream_annotation.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 60, annotationList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationList"


    class annotation_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotation_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotation"
    # Java.g:595:1: annotation : AT ^ qualifiedIdentifier ( annotationInit )? ;
    def annotation(self, ):
        retval = self.annotation_return()
        retval.start = self.input.LT(1)

        annotation_StartIndex = self.input.index()

        root_0 = None

        AT223 = None
        qualifiedIdentifier224 = None

        annotationInit225 = None


        AT223_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:596:5: ( AT ^ qualifiedIdentifier ( annotationInit )? )
                # Java.g:596:9: AT ^ qualifiedIdentifier ( annotationInit )?
                pass 
                root_0 = self._adaptor.nil()


                AT223 = self.match(self.input, AT, self.FOLLOW_AT_in_annotation8024)
                if self._state.backtracking == 0:
                    AT223_tree = self._adaptor.createWithPayload(AT223)
                    root_0 = self._adaptor.becomeRoot(AT223_tree, root_0)



                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_annotation8027)
                qualifiedIdentifier224 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, qualifiedIdentifier224.tree)


                # Java.g:596:33: ( annotationInit )?
                alt76 = 2
                LA76_0 = self.input.LA(1)

                if (LA76_0 == LPAREN) :
                    alt76 = 1
                if alt76 == 1:
                    # Java.g:596:33: annotationInit
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInit_in_annotation8029)
                    annotationInit225 = self.annotationInit()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationInit225.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 61, annotation_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotation"


    class annotationInit_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationInit_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationInit"
    # Java.g:599:1: annotationInit : LPAREN annotationInitializers RPAREN -> ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers ) ;
    def annotationInit(self, ):
        retval = self.annotationInit_return()
        retval.start = self.input.LT(1)

        annotationInit_StartIndex = self.input.index()

        root_0 = None

        LPAREN226 = None
        RPAREN228 = None
        annotationInitializers227 = None


        LPAREN226_tree = None
        RPAREN228_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_annotationInitializers = RewriteRuleSubtreeStream(self._adaptor, "rule annotationInitializers")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:600:5: ( LPAREN annotationInitializers RPAREN -> ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers ) )
                # Java.g:600:9: LPAREN annotationInitializers RPAREN
                pass 
                LPAREN226 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_annotationInit8053) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN226)


                self._state.following.append(self.FOLLOW_annotationInitializers_in_annotationInit8055)
                annotationInitializers227 = self.annotationInitializers()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_annotationInitializers.add(annotationInitializers227.tree)


                RPAREN228 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_annotationInit8057) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN228)


                # AST Rewrite
                # elements: annotationInitializers
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 601:9: -> ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers )
                    # Java.g:601:13: ^( ANNOTATION_INIT_BLOCK[$LPAREN, \"ANNOTATION_INIT_BLOCK\"] annotationInitializers )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(ANNOTATION_INIT_BLOCK, LPAREN226, "ANNOTATION_INIT_BLOCK")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_annotationInitializers.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 62, annotationInit_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationInit"


    class annotationInitializers_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationInitializers_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationInitializers"
    # Java.g:604:1: annotationInitializers : ( annotationInitializer ( COMMA annotationInitializer )* -> ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ ) | annotationElementValue -> ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) );
    def annotationInitializers(self, ):
        retval = self.annotationInitializers_return()
        retval.start = self.input.LT(1)

        annotationInitializers_StartIndex = self.input.index()

        root_0 = None

        COMMA230 = None
        annotationInitializer229 = None

        annotationInitializer231 = None

        annotationElementValue232 = None


        COMMA230_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_annotationElementValue = RewriteRuleSubtreeStream(self._adaptor, "rule annotationElementValue")
        stream_annotationInitializer = RewriteRuleSubtreeStream(self._adaptor, "rule annotationInitializer")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:605:5: ( annotationInitializer ( COMMA annotationInitializer )* -> ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ ) | annotationElementValue -> ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue ) )
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if (LA78_0 == IDENT) :
                    LA78_1 = self.input.LA(2)

                    if (LA78_1 == ASSIGN) :
                        alt78 = 1
                    elif (LA78_1 == AND or LA78_1 == BIT_SHIFT_RIGHT or LA78_1 == DEC or LA78_1 == DIV or LA78_1 == DOT or LA78_1 == EQUAL or (GREATER_OR_EQUAL <= LA78_1 <= GREATER_THAN) or (INC <= LA78_1 <= INSTANCEOF) or LA78_1 == LBRACK or (LESS_OR_EQUAL <= LA78_1 <= LESS_THAN) or LA78_1 == LOGICAL_AND or LA78_1 == LOGICAL_OR or LA78_1 == LPAREN or LA78_1 == MINUS or LA78_1 == MOD or LA78_1 == NOT_EQUAL or LA78_1 == OR or LA78_1 == PLUS or LA78_1 == QUESTION or LA78_1 == RPAREN or LA78_1 == SHIFT_LEFT or LA78_1 == SHIFT_RIGHT or LA78_1 == STAR or LA78_1 == XOR) :
                        alt78 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 78, 1, self.input)

                        raise nvae


                elif (LA78_0 == AT or LA78_0 == BOOLEAN or LA78_0 == BYTE or (CHAR <= LA78_0 <= CHARACTER_LITERAL) or (DEC <= LA78_0 <= DECIMAL_LITERAL) or LA78_0 == DOUBLE or LA78_0 == FALSE or (FLOAT <= LA78_0 <= FLOATING_POINT_LITERAL) or LA78_0 == HEX_LITERAL or LA78_0 == INC or LA78_0 == INT or LA78_0 == LCURLY or LA78_0 == LESS_THAN or LA78_0 == LOGICAL_NOT or (LONG <= LA78_0 <= LPAREN) or LA78_0 == MINUS or (NEW <= LA78_0 <= NOT) or LA78_0 == NULL or LA78_0 == OCTAL_LITERAL or LA78_0 == PLUS or LA78_0 == SHORT or (STRING_LITERAL <= LA78_0 <= SUPER) or LA78_0 == THIS or LA78_0 == TRUE or LA78_0 == VOID) :
                    alt78 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 78, 0, self.input)

                    raise nvae


                if alt78 == 1:
                    # Java.g:605:9: annotationInitializer ( COMMA annotationInitializer )*
                    pass 
                    self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers8094)
                    annotationInitializer229 = self.annotationInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationInitializer.add(annotationInitializer229.tree)


                    # Java.g:605:31: ( COMMA annotationInitializer )*
                    while True: #loop77
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == COMMA) :
                            alt77 = 1


                        if alt77 == 1:
                            # Java.g:605:32: COMMA annotationInitializer
                            pass 
                            COMMA230 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_annotationInitializers8097) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA230)


                            self._state.following.append(self.FOLLOW_annotationInitializer_in_annotationInitializers8099)
                            annotationInitializer231 = self.annotationInitializer()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_annotationInitializer.add(annotationInitializer231.tree)



                        else:
                            break #loop77


                    # AST Rewrite
                    # elements: annotationInitializer
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 606:9: -> ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ )
                        # Java.g:606:13: ^( ANNOTATION_INIT_KEY_LIST ( annotationInitializer )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ANNOTATION_INIT_KEY_LIST, "ANNOTATION_INIT_KEY_LIST")
                        , root_1)

                        # Java.g:606:40: ( annotationInitializer )+
                        if not (stream_annotationInitializer.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_annotationInitializer.hasNext():
                            self._adaptor.addChild(root_1, stream_annotationInitializer.nextTree())


                        stream_annotationInitializer.reset()

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt78 == 2:
                    # Java.g:607:9: annotationElementValue
                    pass 
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializers8129)
                    annotationElementValue232 = self.annotationElementValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationElementValue.add(annotationElementValue232.tree)


                    # AST Rewrite
                    # elements: annotationElementValue
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 608:9: -> ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                        # Java.g:608:13: ^( ANNOTATION_INIT_DEFAULT_KEY annotationElementValue )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ANNOTATION_INIT_DEFAULT_KEY, "ANNOTATION_INIT_DEFAULT_KEY")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_annotationElementValue.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 63, annotationInitializers_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationInitializers"


    class annotationInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationInitializer_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationInitializer"
    # Java.g:611:1: annotationInitializer : IDENT ^ ASSIGN ! annotationElementValue ;
    def annotationInitializer(self, ):
        retval = self.annotationInitializer_return()
        retval.start = self.input.LT(1)

        annotationInitializer_StartIndex = self.input.index()

        root_0 = None

        IDENT233 = None
        ASSIGN234 = None
        annotationElementValue235 = None


        IDENT233_tree = None
        ASSIGN234_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:612:5: ( IDENT ^ ASSIGN ! annotationElementValue )
                # Java.g:612:9: IDENT ^ ASSIGN ! annotationElementValue
                pass 
                root_0 = self._adaptor.nil()


                IDENT233 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationInitializer8170)
                if self._state.backtracking == 0:
                    IDENT233_tree = self._adaptor.createWithPayload(IDENT233)
                    root_0 = self._adaptor.becomeRoot(IDENT233_tree, root_0)



                ASSIGN234 = self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_annotationInitializer8173)

                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationInitializer8176)
                annotationElementValue235 = self.annotationElementValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationElementValue235.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 64, annotationInitializer_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationInitializer"


    class annotationElementValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationElementValue_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationElementValue"
    # Java.g:615:1: annotationElementValue : ( annotationElementValueExpression | annotation | annotationElementValueArrayInitializer );
    def annotationElementValue(self, ):
        retval = self.annotationElementValue_return()
        retval.start = self.input.LT(1)

        annotationElementValue_StartIndex = self.input.index()

        root_0 = None

        annotationElementValueExpression236 = None

        annotation237 = None

        annotationElementValueArrayInitializer238 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:616:5: ( annotationElementValueExpression | annotation | annotationElementValueArrayInitializer )
                alt79 = 3
                LA79 = self.input.LA(1)
                if LA79 == BOOLEAN or LA79 == BYTE or LA79 == CHAR or LA79 == CHARACTER_LITERAL or LA79 == DEC or LA79 == DECIMAL_LITERAL or LA79 == DOUBLE or LA79 == FALSE or LA79 == FLOAT or LA79 == FLOATING_POINT_LITERAL or LA79 == HEX_LITERAL or LA79 == IDENT or LA79 == INC or LA79 == INT or LA79 == LESS_THAN or LA79 == LOGICAL_NOT or LA79 == LONG or LA79 == LPAREN or LA79 == MINUS or LA79 == NEW or LA79 == NOT or LA79 == NULL or LA79 == OCTAL_LITERAL or LA79 == PLUS or LA79 == SHORT or LA79 == STRING_LITERAL or LA79 == SUPER or LA79 == THIS or LA79 == TRUE or LA79 == VOID:
                    alt79 = 1
                elif LA79 == AT:
                    alt79 = 2
                elif LA79 == LCURLY:
                    alt79 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 79, 0, self.input)

                    raise nvae


                if alt79 == 1:
                    # Java.g:616:9: annotationElementValueExpression
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_annotationElementValueExpression_in_annotationElementValue8199)
                    annotationElementValueExpression236 = self.annotationElementValueExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationElementValueExpression236.tree)



                elif alt79 == 2:
                    # Java.g:617:9: annotation
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_annotation_in_annotationElementValue8209)
                    annotation237 = self.annotation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotation237.tree)



                elif alt79 == 3:
                    # Java.g:618:9: annotationElementValueArrayInitializer
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_annotationElementValueArrayInitializer_in_annotationElementValue8219)
                    annotationElementValueArrayInitializer238 = self.annotationElementValueArrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotationElementValueArrayInitializer238.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 65, annotationElementValue_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationElementValue"


    class annotationElementValueExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationElementValueExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationElementValueExpression"
    # Java.g:621:1: annotationElementValueExpression : conditionalExpression -> ^( EXPR conditionalExpression ) ;
    def annotationElementValueExpression(self, ):
        retval = self.annotationElementValueExpression_return()
        retval.start = self.input.LT(1)

        annotationElementValueExpression_StartIndex = self.input.index()

        root_0 = None

        conditionalExpression239 = None


        stream_conditionalExpression = RewriteRuleSubtreeStream(self._adaptor, "rule conditionalExpression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:622:5: ( conditionalExpression -> ^( EXPR conditionalExpression ) )
                # Java.g:622:9: conditionalExpression
                pass 
                self._state.following.append(self.FOLLOW_conditionalExpression_in_annotationElementValueExpression8242)
                conditionalExpression239 = self.conditionalExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_conditionalExpression.add(conditionalExpression239.tree)


                # AST Rewrite
                # elements: conditionalExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 623:9: -> ^( EXPR conditionalExpression )
                    # Java.g:623:13: ^( EXPR conditionalExpression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_conditionalExpression.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 66, annotationElementValueExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationElementValueExpression"


    class annotationElementValueArrayInitializer_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationElementValueArrayInitializer_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationElementValueArrayInitializer"
    # Java.g:626:1: annotationElementValueArrayInitializer : LCURLY ( annotationElementValue ( COMMA annotationElementValue )* )? ( COMMA )? RCURLY -> ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* ) ;
    def annotationElementValueArrayInitializer(self, ):
        retval = self.annotationElementValueArrayInitializer_return()
        retval.start = self.input.LT(1)

        annotationElementValueArrayInitializer_StartIndex = self.input.index()

        root_0 = None

        LCURLY240 = None
        COMMA242 = None
        COMMA244 = None
        RCURLY245 = None
        annotationElementValue241 = None

        annotationElementValue243 = None


        LCURLY240_tree = None
        COMMA242_tree = None
        COMMA244_tree = None
        RCURLY245_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_annotationElementValue = RewriteRuleSubtreeStream(self._adaptor, "rule annotationElementValue")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:627:5: ( LCURLY ( annotationElementValue ( COMMA annotationElementValue )* )? ( COMMA )? RCURLY -> ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* ) )
                # Java.g:627:9: LCURLY ( annotationElementValue ( COMMA annotationElementValue )* )? ( COMMA )? RCURLY
                pass 
                LCURLY240 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_annotationElementValueArrayInitializer8282) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY240)


                # Java.g:627:16: ( annotationElementValue ( COMMA annotationElementValue )* )?
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if (LA81_0 == AT or LA81_0 == BOOLEAN or LA81_0 == BYTE or (CHAR <= LA81_0 <= CHARACTER_LITERAL) or (DEC <= LA81_0 <= DECIMAL_LITERAL) or LA81_0 == DOUBLE or LA81_0 == FALSE or (FLOAT <= LA81_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA81_0 <= IDENT) or LA81_0 == INC or LA81_0 == INT or LA81_0 == LCURLY or LA81_0 == LESS_THAN or LA81_0 == LOGICAL_NOT or (LONG <= LA81_0 <= LPAREN) or LA81_0 == MINUS or (NEW <= LA81_0 <= NOT) or LA81_0 == NULL or LA81_0 == OCTAL_LITERAL or LA81_0 == PLUS or LA81_0 == SHORT or (STRING_LITERAL <= LA81_0 <= SUPER) or LA81_0 == THIS or LA81_0 == TRUE or LA81_0 == VOID) :
                    alt81 = 1
                if alt81 == 1:
                    # Java.g:627:17: annotationElementValue ( COMMA annotationElementValue )*
                    pass 
                    self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8285)
                    annotationElementValue241 = self.annotationElementValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationElementValue.add(annotationElementValue241.tree)


                    # Java.g:627:40: ( COMMA annotationElementValue )*
                    while True: #loop80
                        alt80 = 2
                        LA80_0 = self.input.LA(1)

                        if (LA80_0 == COMMA) :
                            LA80_1 = self.input.LA(2)

                            if (LA80_1 == AT or LA80_1 == BOOLEAN or LA80_1 == BYTE or (CHAR <= LA80_1 <= CHARACTER_LITERAL) or (DEC <= LA80_1 <= DECIMAL_LITERAL) or LA80_1 == DOUBLE or LA80_1 == FALSE or (FLOAT <= LA80_1 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA80_1 <= IDENT) or LA80_1 == INC or LA80_1 == INT or LA80_1 == LCURLY or LA80_1 == LESS_THAN or LA80_1 == LOGICAL_NOT or (LONG <= LA80_1 <= LPAREN) or LA80_1 == MINUS or (NEW <= LA80_1 <= NOT) or LA80_1 == NULL or LA80_1 == OCTAL_LITERAL or LA80_1 == PLUS or LA80_1 == SHORT or (STRING_LITERAL <= LA80_1 <= SUPER) or LA80_1 == THIS or LA80_1 == TRUE or LA80_1 == VOID) :
                                alt80 = 1




                        if alt80 == 1:
                            # Java.g:627:41: COMMA annotationElementValue
                            pass 
                            COMMA242 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_annotationElementValueArrayInitializer8288) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA242)


                            self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8290)
                            annotationElementValue243 = self.annotationElementValue()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_annotationElementValue.add(annotationElementValue243.tree)



                        else:
                            break #loop80





                # Java.g:627:74: ( COMMA )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if (LA82_0 == COMMA) :
                    alt82 = 1
                if alt82 == 1:
                    # Java.g:627:75: COMMA
                    pass 
                    COMMA244 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_annotationElementValueArrayInitializer8297) 
                    if self._state.backtracking == 0:
                        stream_COMMA.add(COMMA244)





                RCURLY245 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_annotationElementValueArrayInitializer8301) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY245)


                # AST Rewrite
                # elements: annotationElementValue
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 628:9: -> ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* )
                    # Java.g:628:13: ^( ANNOTATION_INIT_ARRAY_ELEMENT[$LCURLY, \"ANNOTATION_ELEM_VALUE_ARRAY_INIT\"] ( annotationElementValue )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(ANNOTATION_INIT_ARRAY_ELEMENT, LCURLY240, "ANNOTATION_ELEM_VALUE_ARRAY_INIT")
                    , root_1)

                    # Java.g:628:90: ( annotationElementValue )*
                    while stream_annotationElementValue.hasNext():
                        self._adaptor.addChild(root_1, stream_annotationElementValue.nextTree())


                    stream_annotationElementValue.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 67, annotationElementValueArrayInitializer_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationElementValueArrayInitializer"


    class annotationTypeDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationTypeDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationTypeDeclaration"
    # Java.g:631:1: annotationTypeDeclaration[CommonTree modifiers] : AT INTERFACE IDENT annotationBody -> ^( AT IDENT annotationBody ) ;
    def annotationTypeDeclaration(self, modifiers): #(self, CommonTree modifiers)
        retval = self.annotationTypeDeclaration_return()
        retval.start = self.input.LT(1)

        annotationTypeDeclaration_StartIndex = self.input.index()

        root_0 = None

        AT246 = None
        INTERFACE247 = None
        IDENT248 = None
        annotationBody249 = None


        AT246_tree = None
        INTERFACE247_tree = None
        IDENT248_tree = None
        stream_AT = RewriteRuleTokenStream(self._adaptor, "token AT")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_INTERFACE = RewriteRuleTokenStream(self._adaptor, "token INTERFACE")
        stream_annotationBody = RewriteRuleSubtreeStream(self._adaptor, "rule annotationBody")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:632:5: ( AT INTERFACE IDENT annotationBody -> ^( AT IDENT annotationBody ) )
                # Java.g:632:9: AT INTERFACE IDENT annotationBody
                pass 
                AT246 = self.match(self.input, AT, self.FOLLOW_AT_in_annotationTypeDeclaration8344) 
                if self._state.backtracking == 0:
                    stream_AT.add(AT246)


                INTERFACE247 = self.match(self.input, INTERFACE, self.FOLLOW_INTERFACE_in_annotationTypeDeclaration8346) 
                if self._state.backtracking == 0:
                    stream_INTERFACE.add(INTERFACE247)


                IDENT248 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationTypeDeclaration8348) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT248)


                self._state.following.append(self.FOLLOW_annotationBody_in_annotationTypeDeclaration8350)
                annotationBody249 = self.annotationBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_annotationBody.add(annotationBody249.tree)


                # AST Rewrite
                # elements: IDENT, annotationBody, AT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 633:9: -> ^( AT IDENT annotationBody )
                    # Java.g:633:12: ^( AT IDENT annotationBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_AT.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, modifiers)

                    self._adaptor.addChild(root_1, 
                    stream_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_annotationBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 68, annotationTypeDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationTypeDeclaration"


    class annotationBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationBody_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationBody"
    # Java.g:636:1: annotationBody : LCURLY ( annotationScopeDeclarations )* RCURLY -> ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* ) ;
    def annotationBody(self, ):
        retval = self.annotationBody_return()
        retval.start = self.input.LT(1)

        annotationBody_StartIndex = self.input.index()

        root_0 = None

        LCURLY250 = None
        RCURLY252 = None
        annotationScopeDeclarations251 = None


        LCURLY250_tree = None
        RCURLY252_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_annotationScopeDeclarations = RewriteRuleSubtreeStream(self._adaptor, "rule annotationScopeDeclarations")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:637:5: ( LCURLY ( annotationScopeDeclarations )* RCURLY -> ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* ) )
                # Java.g:637:9: LCURLY ( annotationScopeDeclarations )* RCURLY
                pass 
                LCURLY250 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_annotationBody8393) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY250)


                # Java.g:637:16: ( annotationScopeDeclarations )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == ABSTRACT or LA83_0 == AT or LA83_0 == BOOLEAN or LA83_0 == BYTE or LA83_0 == CHAR or LA83_0 == CLASS or LA83_0 == DOUBLE or LA83_0 == ENUM or LA83_0 == FINAL or LA83_0 == FLOAT or LA83_0 == IDENT or LA83_0 == INT or LA83_0 == INTERFACE or LA83_0 == LESS_THAN or LA83_0 == LONG or LA83_0 == NATIVE or (PRIVATE <= LA83_0 <= PUBLIC) or LA83_0 == SHORT or LA83_0 == STATIC or LA83_0 == STRICTFP or LA83_0 == SYNCHRONIZED or LA83_0 == TRANSIENT or LA83_0 == VOID or LA83_0 == VOLATILE) :
                        alt83 = 1


                    if alt83 == 1:
                        # Java.g:637:16: annotationScopeDeclarations
                        pass 
                        self._state.following.append(self.FOLLOW_annotationScopeDeclarations_in_annotationBody8395)
                        annotationScopeDeclarations251 = self.annotationScopeDeclarations()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_annotationScopeDeclarations.add(annotationScopeDeclarations251.tree)



                    else:
                        break #loop83


                RCURLY252 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_annotationBody8398) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY252)


                # AST Rewrite
                # elements: annotationScopeDeclarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 638:9: -> ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* )
                    # Java.g:638:13: ^( ANNOTATION_TOP_LEVEL_SCOPE[$LCURLY, \"CLASS_TOP_LEVEL_SCOPE\"] ( annotationScopeDeclarations )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(ANNOTATION_TOP_LEVEL_SCOPE, LCURLY250, "CLASS_TOP_LEVEL_SCOPE")
                    , root_1)

                    # Java.g:638:76: ( annotationScopeDeclarations )*
                    while stream_annotationScopeDeclarations.hasNext():
                        self._adaptor.addChild(root_1, stream_annotationScopeDeclarations.nextTree())


                    stream_annotationScopeDeclarations.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 69, annotationBody_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationBody"


    class annotationScopeDeclarations_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationScopeDeclarations_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationScopeDeclarations"
    # Java.g:641:1: annotationScopeDeclarations : ( modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration );
    def annotationScopeDeclarations(self, ):
        retval = self.annotationScopeDeclarations_return()
        retval.start = self.input.LT(1)

        annotationScopeDeclarations_StartIndex = self.input.index()

        root_0 = None

        IDENT255 = None
        LPAREN256 = None
        RPAREN257 = None
        SEMI259 = None
        SEMI261 = None
        modifierList253 = None

        type254 = None

        annotationDefaultValue258 = None

        classFieldDeclaratorList260 = None

        typeDeclaration262 = None


        IDENT255_tree = None
        LPAREN256_tree = None
        RPAREN257_tree = None
        SEMI259_tree = None
        SEMI261_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_modifierList = RewriteRuleSubtreeStream(self._adaptor, "rule modifierList")
        stream_annotationDefaultValue = RewriteRuleSubtreeStream(self._adaptor, "rule annotationDefaultValue")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_classFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclaratorList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:642:5: ( modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) ) | typeDeclaration )
                alt86 = 2
                LA86 = self.input.LA(1)
                if LA86 == PUBLIC:
                    LA86_1 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 1, self.input)

                        raise nvae


                elif LA86 == PROTECTED:
                    LA86_2 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 2, self.input)

                        raise nvae


                elif LA86 == PRIVATE:
                    LA86_3 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 3, self.input)

                        raise nvae


                elif LA86 == STATIC:
                    LA86_4 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 4, self.input)

                        raise nvae


                elif LA86 == ABSTRACT:
                    LA86_5 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 5, self.input)

                        raise nvae


                elif LA86 == NATIVE:
                    LA86_6 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 6, self.input)

                        raise nvae


                elif LA86 == SYNCHRONIZED:
                    LA86_7 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 7, self.input)

                        raise nvae


                elif LA86 == TRANSIENT:
                    LA86_8 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 8, self.input)

                        raise nvae


                elif LA86 == VOLATILE:
                    LA86_9 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 9, self.input)

                        raise nvae


                elif LA86 == STRICTFP:
                    LA86_10 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 10, self.input)

                        raise nvae


                elif LA86 == FINAL:
                    LA86_11 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 11, self.input)

                        raise nvae


                elif LA86 == AT:
                    LA86_12 = self.input.LA(2)

                    if (self.synpred114_Java()) :
                        alt86 = 1
                    elif (True) :
                        alt86 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 86, 12, self.input)

                        raise nvae


                elif LA86 == BOOLEAN or LA86 == BYTE or LA86 == CHAR or LA86 == DOUBLE or LA86 == FLOAT or LA86 == IDENT or LA86 == INT or LA86 == LONG or LA86 == SHORT:
                    alt86 = 1
                elif LA86 == CLASS or LA86 == ENUM or LA86 == INTERFACE:
                    alt86 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 86, 0, self.input)

                    raise nvae


                if alt86 == 1:
                    # Java.g:642:9: modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    pass 
                    self._state.following.append(self.FOLLOW_modifierList_in_annotationScopeDeclarations8440)
                    modifierList253 = self.modifierList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modifierList.add(modifierList253.tree)


                    self._state.following.append(self.FOLLOW_type_in_annotationScopeDeclarations8442)
                    type254 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type254.tree)


                    # Java.g:643:9: ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? ) | classFieldDeclaratorList SEMI -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList ) )
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == IDENT) :
                        LA85_1 = self.input.LA(2)

                        if (LA85_1 == LPAREN) :
                            alt85 = 1
                        elif (LA85_1 == ASSIGN or LA85_1 == COMMA or LA85_1 == LBRACK or LA85_1 == SEMI) :
                            alt85 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 85, 1, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 85, 0, self.input)

                        raise nvae


                    if alt85 == 1:
                        # Java.g:643:13: IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI
                        pass 
                        IDENT255 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_annotationScopeDeclarations8456) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT255)


                        LPAREN256 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_annotationScopeDeclarations8458) 
                        if self._state.backtracking == 0:
                            stream_LPAREN.add(LPAREN256)


                        RPAREN257 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_annotationScopeDeclarations8460) 
                        if self._state.backtracking == 0:
                            stream_RPAREN.add(RPAREN257)


                        # Java.g:643:33: ( annotationDefaultValue )?
                        alt84 = 2
                        LA84_0 = self.input.LA(1)

                        if (LA84_0 == DEFAULT) :
                            alt84 = 1
                        if alt84 == 1:
                            # Java.g:643:33: annotationDefaultValue
                            pass 
                            self._state.following.append(self.FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations8462)
                            annotationDefaultValue258 = self.annotationDefaultValue()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_annotationDefaultValue.add(annotationDefaultValue258.tree)





                        SEMI259 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_annotationScopeDeclarations8465) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI259)


                        # AST Rewrite
                        # elements: IDENT, annotationDefaultValue, type, modifierList
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 644:13: -> ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? )
                            # Java.g:644:17: ^( ANNOTATION_METHOD_DECL modifierList type IDENT ( annotationDefaultValue )? )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(ANNOTATION_METHOD_DECL, "ANNOTATION_METHOD_DECL")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                            self._adaptor.addChild(root_1, stream_type.nextTree())

                            self._adaptor.addChild(root_1, 
                            stream_IDENT.nextNode()
                            )

                            # Java.g:644:66: ( annotationDefaultValue )?
                            if stream_annotationDefaultValue.hasNext():
                                self._adaptor.addChild(root_1, stream_annotationDefaultValue.nextTree())


                            stream_annotationDefaultValue.reset();

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt85 == 2:
                        # Java.g:645:13: classFieldDeclaratorList SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_annotationScopeDeclarations8507)
                        classFieldDeclaratorList260 = self.classFieldDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classFieldDeclaratorList.add(classFieldDeclaratorList260.tree)


                        SEMI261 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_annotationScopeDeclarations8509) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI261)


                        # AST Rewrite
                        # elements: classFieldDeclaratorList, modifierList, type
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 646:13: -> ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            # Java.g:646:17: ^( VAR_DECLARATION modifierList type classFieldDeclaratorList )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_modifierList.nextTree())

                            self._adaptor.addChild(root_1, stream_type.nextTree())

                            self._adaptor.addChild(root_1, stream_classFieldDeclaratorList.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt86 == 2:
                    # Java.g:648:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typeDeclaration_in_annotationScopeDeclarations8554)
                    typeDeclaration262 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration262.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 70, annotationScopeDeclarations_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationScopeDeclarations"


    class annotationDefaultValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.annotationDefaultValue_return, self).__init__()

            self.tree = None





    # $ANTLR start "annotationDefaultValue"
    # Java.g:651:1: annotationDefaultValue : DEFAULT ^ annotationElementValue ;
    def annotationDefaultValue(self, ):
        retval = self.annotationDefaultValue_return()
        retval.start = self.input.LT(1)

        annotationDefaultValue_StartIndex = self.input.index()

        root_0 = None

        DEFAULT263 = None
        annotationElementValue264 = None


        DEFAULT263_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:652:5: ( DEFAULT ^ annotationElementValue )
                # Java.g:652:9: DEFAULT ^ annotationElementValue
                pass 
                root_0 = self._adaptor.nil()


                DEFAULT263 = self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_annotationDefaultValue8577)
                if self._state.backtracking == 0:
                    DEFAULT263_tree = self._adaptor.createWithPayload(DEFAULT263)
                    root_0 = self._adaptor.becomeRoot(DEFAULT263_tree, root_0)



                self._state.following.append(self.FOLLOW_annotationElementValue_in_annotationDefaultValue8580)
                annotationElementValue264 = self.annotationElementValue()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, annotationElementValue264.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 71, annotationDefaultValue_StartIndex, success)


            pass
        return retval

    # $ANTLR end "annotationDefaultValue"


    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.block_return, self).__init__()

            self.tree = None





    # $ANTLR start "block"
    # Java.g:657:1: block : LCURLY ( blockStatement )* RCURLY -> ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* ) ;
    def block(self, ):
        retval = self.block_return()
        retval.start = self.input.LT(1)

        block_StartIndex = self.input.index()

        root_0 = None

        LCURLY265 = None
        RCURLY267 = None
        blockStatement266 = None


        LCURLY265_tree = None
        RCURLY267_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_blockStatement = RewriteRuleSubtreeStream(self._adaptor, "rule blockStatement")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:658:5: ( LCURLY ( blockStatement )* RCURLY -> ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* ) )
                # Java.g:658:9: LCURLY ( blockStatement )* RCURLY
                pass 
                LCURLY265 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_block8601) 
                if self._state.backtracking == 0:
                    stream_LCURLY.add(LCURLY265)


                # Java.g:658:16: ( blockStatement )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == ABSTRACT or LA87_0 == ASSERT or LA87_0 == AT or (BOOLEAN <= LA87_0 <= BYTE) or (CHAR <= LA87_0 <= CLASS) or (CONTINUE <= LA87_0 <= DECIMAL_LITERAL) or LA87_0 == DO or LA87_0 == DOUBLE or LA87_0 == ENUM or (FALSE <= LA87_0 <= FINAL) or (FLOAT <= LA87_0 <= FLOATING_POINT_LITERAL) or LA87_0 == FOR or (HEX_LITERAL <= LA87_0 <= IF) or LA87_0 == INC or LA87_0 == INT or LA87_0 == INTERFACE or LA87_0 == LCURLY or LA87_0 == LESS_THAN or LA87_0 == LOGICAL_NOT or (LONG <= LA87_0 <= LPAREN) or LA87_0 == MINUS or (NATIVE <= LA87_0 <= NOT) or LA87_0 == NULL or LA87_0 == OCTAL_LITERAL or LA87_0 == PLUS or (PRIVATE <= LA87_0 <= PUBLIC) or LA87_0 == RETURN or LA87_0 == SEMI or LA87_0 == SHORT or LA87_0 == STATIC or (STRICTFP <= LA87_0 <= SUPER) or LA87_0 == SWITCH or (SYNCHRONIZED <= LA87_0 <= THIS) or LA87_0 == THROW or (TRANSIENT <= LA87_0 <= TRY) or LA87_0 == VOID or (VOLATILE <= LA87_0 <= WHILE)) :
                        alt87 = 1


                    if alt87 == 1:
                        # Java.g:658:16: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_block8603)
                        blockStatement266 = self.blockStatement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_blockStatement.add(blockStatement266.tree)



                    else:
                        break #loop87


                RCURLY267 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_block8606) 
                if self._state.backtracking == 0:
                    stream_RCURLY.add(RCURLY267)


                # AST Rewrite
                # elements: blockStatement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 659:9: -> ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* )
                    # Java.g:659:13: ^( BLOCK_SCOPE[$LCURLY, \"BLOCK_SCOPE\"] ( blockStatement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(BLOCK_SCOPE, LCURLY265, "BLOCK_SCOPE")
                    , root_1)

                    # Java.g:659:51: ( blockStatement )*
                    while stream_blockStatement.hasNext():
                        self._adaptor.addChild(root_1, stream_blockStatement.nextTree())


                    stream_blockStatement.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 72, block_StartIndex, success)


            pass
        return retval

    # $ANTLR end "block"


    class blockStatement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.blockStatement_return, self).__init__()

            self.tree = None





    # $ANTLR start "blockStatement"
    # Java.g:662:1: blockStatement : ( localVariableDeclaration SEMI !| typeDeclaration | statement );
    def blockStatement(self, ):
        retval = self.blockStatement_return()
        retval.start = self.input.LT(1)

        blockStatement_StartIndex = self.input.index()

        root_0 = None

        SEMI269 = None
        localVariableDeclaration268 = None

        typeDeclaration270 = None

        statement271 = None


        SEMI269_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:663:5: ( localVariableDeclaration SEMI !| typeDeclaration | statement )
                alt88 = 3
                LA88 = self.input.LA(1)
                if LA88 == FINAL:
                    LA88_1 = self.input.LA(2)

                    if (self.synpred116_Java()) :
                        alt88 = 1
                    elif (self.synpred117_Java()) :
                        alt88 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 88, 1, self.input)

                        raise nvae


                elif LA88 == AT:
                    LA88_2 = self.input.LA(2)

                    if (self.synpred116_Java()) :
                        alt88 = 1
                    elif (self.synpred117_Java()) :
                        alt88 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 88, 2, self.input)

                        raise nvae


                elif LA88 == BOOLEAN or LA88 == BYTE or LA88 == CHAR or LA88 == DOUBLE or LA88 == FLOAT or LA88 == INT or LA88 == LONG or LA88 == SHORT:
                    LA88_3 = self.input.LA(2)

                    if (self.synpred116_Java()) :
                        alt88 = 1
                    elif (True) :
                        alt88 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 88, 3, self.input)

                        raise nvae


                elif LA88 == IDENT:
                    LA88_4 = self.input.LA(2)

                    if (self.synpred116_Java()) :
                        alt88 = 1
                    elif (True) :
                        alt88 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 88, 4, self.input)

                        raise nvae


                elif LA88 == ABSTRACT or LA88 == CLASS or LA88 == ENUM or LA88 == INTERFACE or LA88 == NATIVE or LA88 == PRIVATE or LA88 == PROTECTED or LA88 == PUBLIC or LA88 == STATIC or LA88 == STRICTFP or LA88 == TRANSIENT or LA88 == VOLATILE:
                    alt88 = 2
                elif LA88 == SYNCHRONIZED:
                    LA88_11 = self.input.LA(2)

                    if (self.synpred117_Java()) :
                        alt88 = 2
                    elif (True) :
                        alt88 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 88, 11, self.input)

                        raise nvae


                elif LA88 == ASSERT or LA88 == BREAK or LA88 == CHARACTER_LITERAL or LA88 == CONTINUE or LA88 == DEC or LA88 == DECIMAL_LITERAL or LA88 == DO or LA88 == FALSE or LA88 == FLOATING_POINT_LITERAL or LA88 == FOR or LA88 == HEX_LITERAL or LA88 == IF or LA88 == INC or LA88 == LCURLY or LA88 == LESS_THAN or LA88 == LOGICAL_NOT or LA88 == LPAREN or LA88 == MINUS or LA88 == NEW or LA88 == NOT or LA88 == NULL or LA88 == OCTAL_LITERAL or LA88 == PLUS or LA88 == RETURN or LA88 == SEMI or LA88 == STRING_LITERAL or LA88 == SUPER or LA88 == SWITCH or LA88 == THIS or LA88 == THROW or LA88 == TRUE or LA88 == TRY or LA88 == VOID or LA88 == WHILE:
                    alt88 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 88, 0, self.input)

                    raise nvae


                if alt88 == 1:
                    # Java.g:663:9: localVariableDeclaration SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_blockStatement8644)
                    localVariableDeclaration268 = self.localVariableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localVariableDeclaration268.tree)


                    SEMI269 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_blockStatement8646)


                elif alt88 == 2:
                    # Java.g:664:9: typeDeclaration
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typeDeclaration_in_blockStatement8657)
                    typeDeclaration270 = self.typeDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typeDeclaration270.tree)



                elif alt88 == 3:
                    # Java.g:665:9: statement
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_in_blockStatement8667)
                    statement271 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, statement271.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 73, blockStatement_StartIndex, success)


            pass
        return retval

    # $ANTLR end "blockStatement"


    class localVariableDeclaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.localVariableDeclaration_return, self).__init__()

            self.tree = None





    # $ANTLR start "localVariableDeclaration"
    # Java.g:668:1: localVariableDeclaration : localModifierList type classFieldDeclaratorList -> ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList ) ;
    def localVariableDeclaration(self, ):
        retval = self.localVariableDeclaration_return()
        retval.start = self.input.LT(1)

        localVariableDeclaration_StartIndex = self.input.index()

        root_0 = None

        localModifierList272 = None

        type273 = None

        classFieldDeclaratorList274 = None


        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_classFieldDeclaratorList = RewriteRuleSubtreeStream(self._adaptor, "rule classFieldDeclaratorList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:669:5: ( localModifierList type classFieldDeclaratorList -> ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList ) )
                # Java.g:669:9: localModifierList type classFieldDeclaratorList
                pass 
                self._state.following.append(self.FOLLOW_localModifierList_in_localVariableDeclaration8690)
                localModifierList272 = self.localModifierList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localModifierList.add(localModifierList272.tree)


                self._state.following.append(self.FOLLOW_type_in_localVariableDeclaration8692)
                type273 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type273.tree)


                self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_localVariableDeclaration8694)
                classFieldDeclaratorList274 = self.classFieldDeclaratorList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_classFieldDeclaratorList.add(classFieldDeclaratorList274.tree)


                # AST Rewrite
                # elements: classFieldDeclaratorList, type, localModifierList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 670:9: -> ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList )
                    # Java.g:670:13: ^( VAR_DECLARATION localModifierList type classFieldDeclaratorList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VAR_DECLARATION, "VAR_DECLARATION")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_localModifierList.nextTree())

                    self._adaptor.addChild(root_1, stream_type.nextTree())

                    self._adaptor.addChild(root_1, stream_classFieldDeclaratorList.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 74, localVariableDeclaration_StartIndex, success)


            pass
        return retval

    # $ANTLR end "localVariableDeclaration"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.statement_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement"
    # Java.g:674:1: statement : ( block | ASSERT expr1= expression ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) ) | IF parenthesizedExpression ifStat= statement ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) ) | FOR LPAREN ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) ) | WHILE parenthesizedExpression statement -> ^( WHILE parenthesizedExpression statement ) | DO statement WHILE parenthesizedExpression SEMI -> ^( DO statement parenthesizedExpression ) | TRY block ( catches ( finallyClause )? | finallyClause ) -> ^( TRY block ( catches )? ( finallyClause )? ) | SWITCH parenthesizedExpression LCURLY switchBlockLabels RCURLY -> ^( SWITCH parenthesizedExpression switchBlockLabels ) | SYNCHRONIZED parenthesizedExpression block -> ^( SYNCHRONIZED parenthesizedExpression block ) | RETURN ( expression )? SEMI -> ^( RETURN ( expression )? ) | THROW expression SEMI -> ^( THROW expression ) | BREAK ( IDENT )? SEMI -> ^( BREAK ( IDENT )? ) | CONTINUE ( IDENT )? SEMI -> ^( CONTINUE ( IDENT )? ) | IDENT COLON statement -> ^( LABELED_STATEMENT IDENT statement ) | expression SEMI !| SEMI );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)

        statement_StartIndex = self.input.index()

        root_0 = None

        ASSERT276 = None
        COLON277 = None
        SEMI278 = None
        SEMI279 = None
        IF280 = None
        ELSE282 = None
        FOR283 = None
        LPAREN284 = None
        SEMI286 = None
        SEMI288 = None
        RPAREN290 = None
        IDENT294 = None
        COLON295 = None
        RPAREN297 = None
        WHILE299 = None
        DO302 = None
        WHILE304 = None
        SEMI306 = None
        TRY307 = None
        SWITCH312 = None
        LCURLY314 = None
        RCURLY316 = None
        SYNCHRONIZED317 = None
        RETURN320 = None
        SEMI322 = None
        THROW323 = None
        SEMI325 = None
        BREAK326 = None
        IDENT327 = None
        SEMI328 = None
        CONTINUE329 = None
        IDENT330 = None
        SEMI331 = None
        IDENT332 = None
        COLON333 = None
        SEMI336 = None
        SEMI337 = None
        expr1 = None

        expr2 = None

        ifStat = None

        elseStat = None

        block275 = None

        parenthesizedExpression281 = None

        forInit285 = None

        forCondition287 = None

        forUpdater289 = None

        statement291 = None

        localModifierList292 = None

        type293 = None

        expression296 = None

        statement298 = None

        parenthesizedExpression300 = None

        statement301 = None

        statement303 = None

        parenthesizedExpression305 = None

        block308 = None

        catches309 = None

        finallyClause310 = None

        finallyClause311 = None

        parenthesizedExpression313 = None

        switchBlockLabels315 = None

        parenthesizedExpression318 = None

        block319 = None

        expression321 = None

        expression324 = None

        statement334 = None

        expression335 = None


        ASSERT276_tree = None
        COLON277_tree = None
        SEMI278_tree = None
        SEMI279_tree = None
        IF280_tree = None
        ELSE282_tree = None
        FOR283_tree = None
        LPAREN284_tree = None
        SEMI286_tree = None
        SEMI288_tree = None
        RPAREN290_tree = None
        IDENT294_tree = None
        COLON295_tree = None
        RPAREN297_tree = None
        WHILE299_tree = None
        DO302_tree = None
        WHILE304_tree = None
        SEMI306_tree = None
        TRY307_tree = None
        SWITCH312_tree = None
        LCURLY314_tree = None
        RCURLY316_tree = None
        SYNCHRONIZED317_tree = None
        RETURN320_tree = None
        SEMI322_tree = None
        THROW323_tree = None
        SEMI325_tree = None
        BREAK326_tree = None
        IDENT327_tree = None
        SEMI328_tree = None
        CONTINUE329_tree = None
        IDENT330_tree = None
        SEMI331_tree = None
        IDENT332_tree = None
        COLON333_tree = None
        SEMI336_tree = None
        SEMI337_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_SYNCHRONIZED = RewriteRuleTokenStream(self._adaptor, "token SYNCHRONIZED")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_CONTINUE = RewriteRuleTokenStream(self._adaptor, "token CONTINUE")
        stream_SWITCH = RewriteRuleTokenStream(self._adaptor, "token SWITCH")
        stream_RCURLY = RewriteRuleTokenStream(self._adaptor, "token RCURLY")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_RETURN = RewriteRuleTokenStream(self._adaptor, "token RETURN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_FOR = RewriteRuleTokenStream(self._adaptor, "token FOR")
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_LCURLY = RewriteRuleTokenStream(self._adaptor, "token LCURLY")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_ASSERT = RewriteRuleTokenStream(self._adaptor, "token ASSERT")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")
        stream_THROW = RewriteRuleTokenStream(self._adaptor, "token THROW")
        stream_TRY = RewriteRuleTokenStream(self._adaptor, "token TRY")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_finallyClause = RewriteRuleSubtreeStream(self._adaptor, "rule finallyClause")
        stream_catches = RewriteRuleSubtreeStream(self._adaptor, "rule catches")
        stream_forUpdater = RewriteRuleSubtreeStream(self._adaptor, "rule forUpdater")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_forCondition = RewriteRuleSubtreeStream(self._adaptor, "rule forCondition")
        stream_localModifierList = RewriteRuleSubtreeStream(self._adaptor, "rule localModifierList")
        stream_forInit = RewriteRuleSubtreeStream(self._adaptor, "rule forInit")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_switchBlockLabels = RewriteRuleSubtreeStream(self._adaptor, "rule switchBlockLabels")
        stream_parenthesizedExpression = RewriteRuleSubtreeStream(self._adaptor, "rule parenthesizedExpression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:675:5: ( block | ASSERT expr1= expression ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) ) | IF parenthesizedExpression ifStat= statement ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) ) | FOR LPAREN ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) ) | WHILE parenthesizedExpression statement -> ^( WHILE parenthesizedExpression statement ) | DO statement WHILE parenthesizedExpression SEMI -> ^( DO statement parenthesizedExpression ) | TRY block ( catches ( finallyClause )? | finallyClause ) -> ^( TRY block ( catches )? ( finallyClause )? ) | SWITCH parenthesizedExpression LCURLY switchBlockLabels RCURLY -> ^( SWITCH parenthesizedExpression switchBlockLabels ) | SYNCHRONIZED parenthesizedExpression block -> ^( SYNCHRONIZED parenthesizedExpression block ) | RETURN ( expression )? SEMI -> ^( RETURN ( expression )? ) | THROW expression SEMI -> ^( THROW expression ) | BREAK ( IDENT )? SEMI -> ^( BREAK ( IDENT )? ) | CONTINUE ( IDENT )? SEMI -> ^( CONTINUE ( IDENT )? ) | IDENT COLON statement -> ^( LABELED_STATEMENT IDENT statement ) | expression SEMI !| SEMI )
                alt97 = 16
                LA97 = self.input.LA(1)
                if LA97 == LCURLY:
                    alt97 = 1
                elif LA97 == ASSERT:
                    alt97 = 2
                elif LA97 == IF:
                    alt97 = 3
                elif LA97 == FOR:
                    alt97 = 4
                elif LA97 == WHILE:
                    alt97 = 5
                elif LA97 == DO:
                    alt97 = 6
                elif LA97 == TRY:
                    alt97 = 7
                elif LA97 == SWITCH:
                    alt97 = 8
                elif LA97 == SYNCHRONIZED:
                    alt97 = 9
                elif LA97 == RETURN:
                    alt97 = 10
                elif LA97 == THROW:
                    alt97 = 11
                elif LA97 == BREAK:
                    alt97 = 12
                elif LA97 == CONTINUE:
                    alt97 = 13
                elif LA97 == IDENT:
                    LA97_14 = self.input.LA(2)

                    if (LA97_14 == COLON) :
                        alt97 = 14
                    elif ((AND <= LA97_14 <= AND_ASSIGN) or LA97_14 == ASSIGN or (BIT_SHIFT_RIGHT <= LA97_14 <= BIT_SHIFT_RIGHT_ASSIGN) or LA97_14 == DEC or (DIV <= LA97_14 <= DIV_ASSIGN) or LA97_14 == DOT or LA97_14 == EQUAL or (GREATER_OR_EQUAL <= LA97_14 <= GREATER_THAN) or (INC <= LA97_14 <= INSTANCEOF) or LA97_14 == LBRACK or (LESS_OR_EQUAL <= LA97_14 <= LESS_THAN) or LA97_14 == LOGICAL_AND or LA97_14 == LOGICAL_OR or LA97_14 == LPAREN or (MINUS <= LA97_14 <= MOD) or LA97_14 == MOD_ASSIGN or LA97_14 == NOT_EQUAL or (OR <= LA97_14 <= OR_ASSIGN) or (PLUS <= LA97_14 <= PLUS_ASSIGN) or LA97_14 == QUESTION or (SEMI <= LA97_14 <= SHIFT_RIGHT_ASSIGN) or (STAR <= LA97_14 <= STAR_ASSIGN) or (XOR <= LA97_14 <= XOR_ASSIGN)) :
                        alt97 = 15
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 97, 14, self.input)

                        raise nvae


                elif LA97 == BOOLEAN or LA97 == BYTE or LA97 == CHAR or LA97 == CHARACTER_LITERAL or LA97 == DEC or LA97 == DECIMAL_LITERAL or LA97 == DOUBLE or LA97 == FALSE or LA97 == FLOAT or LA97 == FLOATING_POINT_LITERAL or LA97 == HEX_LITERAL or LA97 == INC or LA97 == INT or LA97 == LESS_THAN or LA97 == LOGICAL_NOT or LA97 == LONG or LA97 == LPAREN or LA97 == MINUS or LA97 == NEW or LA97 == NOT or LA97 == NULL or LA97 == OCTAL_LITERAL or LA97 == PLUS or LA97 == SHORT or LA97 == STRING_LITERAL or LA97 == SUPER or LA97 == THIS or LA97 == TRUE or LA97 == VOID:
                    alt97 = 15
                elif LA97 == SEMI:
                    alt97 = 16
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 97, 0, self.input)

                    raise nvae


                if alt97 == 1:
                    # Java.g:675:9: block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_block_in_statement8747)
                    block275 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block275.tree)



                elif alt97 == 2:
                    # Java.g:676:9: ASSERT expr1= expression ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) )
                    pass 
                    ASSERT276 = self.match(self.input, ASSERT, self.FOLLOW_ASSERT_in_statement8757) 
                    if self._state.backtracking == 0:
                        stream_ASSERT.add(ASSERT276)


                    self._state.following.append(self.FOLLOW_expression_in_statement8761)
                    expr1 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expr1.tree)


                    # Java.g:677:9: ( COLON expr2= expression SEMI -> ^( ASSERT $expr1 $expr2) | SEMI -> ^( ASSERT $expr1) )
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == COLON) :
                        alt89 = 1
                    elif (LA89_0 == SEMI) :
                        alt89 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 89, 0, self.input)

                        raise nvae


                    if alt89 == 1:
                        # Java.g:677:13: COLON expr2= expression SEMI
                        pass 
                        COLON277 = self.match(self.input, COLON, self.FOLLOW_COLON_in_statement8776) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON277)


                        self._state.following.append(self.FOLLOW_expression_in_statement8780)
                        expr2 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expr2.tree)


                        SEMI278 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement8782) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI278)


                        # AST Rewrite
                        # elements: ASSERT, expr2, expr1
                        # token labels: 
                        # rule labels: retval, expr1, expr2
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                            if expr1 is not None:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "rule expr1", expr1.tree)
                            else:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "token expr1", None)

                            if expr2 is not None:
                                stream_expr2 = RewriteRuleSubtreeStream(self._adaptor, "rule expr2", expr2.tree)
                            else:
                                stream_expr2 = RewriteRuleSubtreeStream(self._adaptor, "token expr2", None)


                            root_0 = self._adaptor.nil()
                            # 677:77: -> ^( ASSERT $expr1 $expr2)
                            # Java.g:677:81: ^( ASSERT $expr1 $expr2)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_ASSERT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_expr1.nextTree())

                            self._adaptor.addChild(root_1, stream_expr2.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt89 == 2:
                        # Java.g:678:13: SEMI
                        pass 
                        SEMI279 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement8845) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI279)


                        # AST Rewrite
                        # elements: expr1, ASSERT
                        # token labels: 
                        # rule labels: retval, expr1
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                            if expr1 is not None:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "rule expr1", expr1.tree)
                            else:
                                stream_expr1 = RewriteRuleSubtreeStream(self._adaptor, "token expr1", None)


                            root_0 = self._adaptor.nil()
                            # 678:77: -> ^( ASSERT $expr1)
                            # Java.g:678:81: ^( ASSERT $expr1)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_ASSERT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_expr1.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt97 == 3:
                    # Java.g:680:9: IF parenthesizedExpression ifStat= statement ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) )
                    pass 
                    IF280 = self.match(self.input, IF, self.FOLLOW_IF_in_statement8934) 
                    if self._state.backtracking == 0:
                        stream_IF.add(IF280)


                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement8936)
                    parenthesizedExpression281 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression281.tree)


                    self._state.following.append(self.FOLLOW_statement_in_statement8940)
                    ifStat = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(ifStat.tree)


                    # Java.g:681:9: ( ELSE elseStat= statement -> ^( IF parenthesizedExpression $ifStat $elseStat) | -> ^( IF parenthesizedExpression $ifStat) )
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == ELSE) :
                        LA90_1 = self.input.LA(2)

                        if (self.synpred121_Java()) :
                            alt90 = 1
                        elif (True) :
                            alt90 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 90, 1, self.input)

                            raise nvae


                    elif (LA90_0 == EOF or LA90_0 == ABSTRACT or LA90_0 == ASSERT or LA90_0 == AT or (BOOLEAN <= LA90_0 <= CASE) or (CHAR <= LA90_0 <= CLASS) or (CONTINUE <= LA90_0 <= DEFAULT) or LA90_0 == DO or LA90_0 == DOUBLE or LA90_0 == ENUM or (FALSE <= LA90_0 <= FINAL) or (FLOAT <= LA90_0 <= FLOATING_POINT_LITERAL) or LA90_0 == FOR or (HEX_LITERAL <= LA90_0 <= IF) or LA90_0 == INC or LA90_0 == INT or LA90_0 == INTERFACE or LA90_0 == LCURLY or LA90_0 == LESS_THAN or LA90_0 == LOGICAL_NOT or (LONG <= LA90_0 <= LPAREN) or LA90_0 == MINUS or (NATIVE <= LA90_0 <= NOT) or LA90_0 == NULL or LA90_0 == OCTAL_LITERAL or LA90_0 == PLUS or (PRIVATE <= LA90_0 <= PUBLIC) or (RCURLY <= LA90_0 <= RETURN) or LA90_0 == SEMI or LA90_0 == SHORT or LA90_0 == STATIC or (STRICTFP <= LA90_0 <= SUPER) or LA90_0 == SWITCH or (SYNCHRONIZED <= LA90_0 <= THIS) or LA90_0 == THROW or (TRANSIENT <= LA90_0 <= TRY) or LA90_0 == VOID or (VOLATILE <= LA90_0 <= WHILE)) :
                        alt90 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 90, 0, self.input)

                        raise nvae


                    if alt90 == 1:
                        # Java.g:681:13: ELSE elseStat= statement
                        pass 
                        ELSE282 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement8955) 
                        if self._state.backtracking == 0:
                            stream_ELSE.add(ELSE282)


                        self._state.following.append(self.FOLLOW_statement_in_statement8959)
                        elseStat = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(elseStat.tree)


                        # AST Rewrite
                        # elements: IF, elseStat, parenthesizedExpression, ifStat
                        # token labels: 
                        # rule labels: retval, ifStat, elseStat
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                            if ifStat is not None:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "rule ifStat", ifStat.tree)
                            else:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "token ifStat", None)

                            if elseStat is not None:
                                stream_elseStat = RewriteRuleSubtreeStream(self._adaptor, "rule elseStat", elseStat.tree)
                            else:
                                stream_elseStat = RewriteRuleSubtreeStream(self._adaptor, "token elseStat", None)


                            root_0 = self._adaptor.nil()
                            # 681:77: -> ^( IF parenthesizedExpression $ifStat $elseStat)
                            # Java.g:681:81: ^( IF parenthesizedExpression $ifStat $elseStat)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_IF.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                            self._adaptor.addChild(root_1, stream_ifStat.nextTree())

                            self._adaptor.addChild(root_1, stream_elseStat.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt90 == 2:
                        # Java.g:682:77: 
                        pass 
                        # AST Rewrite
                        # elements: parenthesizedExpression, ifStat, IF
                        # token labels: 
                        # rule labels: retval, ifStat
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                            if ifStat is not None:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "rule ifStat", ifStat.tree)
                            else:
                                stream_ifStat = RewriteRuleSubtreeStream(self._adaptor, "token ifStat", None)


                            root_0 = self._adaptor.nil()
                            # 682:77: -> ^( IF parenthesizedExpression $ifStat)
                            # Java.g:682:81: ^( IF parenthesizedExpression $ifStat)
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_IF.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                            self._adaptor.addChild(root_1, stream_ifStat.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt97 == 4:
                    # Java.g:684:9: FOR LPAREN ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) )
                    pass 
                    FOR283 = self.match(self.input, FOR, self.FOLLOW_FOR_in_statement9125) 
                    if self._state.backtracking == 0:
                        stream_FOR.add(FOR283)


                    LPAREN284 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_statement9127) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN284)


                    # Java.g:685:9: ( forInit SEMI forCondition SEMI forUpdater RPAREN statement -> ^( FOR forInit forCondition forUpdater statement ) | localModifierList type IDENT COLON expression RPAREN statement -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement ) )
                    alt91 = 2
                    LA91 = self.input.LA(1)
                    if LA91 == FINAL:
                        LA91_1 = self.input.LA(2)

                        if (self.synpred123_Java()) :
                            alt91 = 1
                        elif (True) :
                            alt91 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 91, 1, self.input)

                            raise nvae


                    elif LA91 == AT:
                        LA91_2 = self.input.LA(2)

                        if (self.synpred123_Java()) :
                            alt91 = 1
                        elif (True) :
                            alt91 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 91, 2, self.input)

                            raise nvae


                    elif LA91 == BOOLEAN or LA91 == BYTE or LA91 == CHAR or LA91 == DOUBLE or LA91 == FLOAT or LA91 == INT or LA91 == LONG or LA91 == SHORT:
                        LA91_3 = self.input.LA(2)

                        if (self.synpred123_Java()) :
                            alt91 = 1
                        elif (True) :
                            alt91 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 91, 3, self.input)

                            raise nvae


                    elif LA91 == IDENT:
                        LA91_4 = self.input.LA(2)

                        if (self.synpred123_Java()) :
                            alt91 = 1
                        elif (True) :
                            alt91 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 91, 4, self.input)

                            raise nvae


                    elif LA91 == CHARACTER_LITERAL or LA91 == DEC or LA91 == DECIMAL_LITERAL or LA91 == FALSE or LA91 == FLOATING_POINT_LITERAL or LA91 == HEX_LITERAL or LA91 == INC or LA91 == LESS_THAN or LA91 == LOGICAL_NOT or LA91 == LPAREN or LA91 == MINUS or LA91 == NEW or LA91 == NOT or LA91 == NULL or LA91 == OCTAL_LITERAL or LA91 == PLUS or LA91 == SEMI or LA91 == STRING_LITERAL or LA91 == SUPER or LA91 == THIS or LA91 == TRUE or LA91 == VOID:
                        alt91 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 91, 0, self.input)

                        raise nvae


                    if alt91 == 1:
                        # Java.g:685:13: forInit SEMI forCondition SEMI forUpdater RPAREN statement
                        pass 
                        self._state.following.append(self.FOLLOW_forInit_in_statement9142)
                        forInit285 = self.forInit()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_forInit.add(forInit285.tree)


                        SEMI286 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9144) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI286)


                        self._state.following.append(self.FOLLOW_forCondition_in_statement9146)
                        forCondition287 = self.forCondition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_forCondition.add(forCondition287.tree)


                        SEMI288 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9148) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI288)


                        self._state.following.append(self.FOLLOW_forUpdater_in_statement9150)
                        forUpdater289 = self.forUpdater()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_forUpdater.add(forUpdater289.tree)


                        RPAREN290 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_statement9152) 
                        if self._state.backtracking == 0:
                            stream_RPAREN.add(RPAREN290)


                        self._state.following.append(self.FOLLOW_statement_in_statement9154)
                        statement291 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement291.tree)


                        # AST Rewrite
                        # elements: forInit, FOR, statement, forUpdater, forCondition
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 685:77: -> ^( FOR forInit forCondition forUpdater statement )
                            # Java.g:685:81: ^( FOR forInit forCondition forUpdater statement )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_FOR.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_forInit.nextTree())

                            self._adaptor.addChild(root_1, stream_forCondition.nextTree())

                            self._adaptor.addChild(root_1, stream_forUpdater.nextTree())

                            self._adaptor.addChild(root_1, stream_statement.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt91 == 2:
                        # Java.g:686:13: localModifierList type IDENT COLON expression RPAREN statement
                        pass 
                        self._state.following.append(self.FOLLOW_localModifierList_in_statement9189)
                        localModifierList292 = self.localModifierList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localModifierList.add(localModifierList292.tree)


                        self._state.following.append(self.FOLLOW_type_in_statement9191)
                        type293 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type293.tree)


                        IDENT294 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9193) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT294)


                        COLON295 = self.match(self.input, COLON, self.FOLLOW_COLON_in_statement9195) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON295)


                        self._state.following.append(self.FOLLOW_expression_in_statement9197)
                        expression296 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression296.tree)


                        RPAREN297 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_statement9199) 
                        if self._state.backtracking == 0:
                            stream_RPAREN.add(RPAREN297)


                        self._state.following.append(self.FOLLOW_statement_in_statement9201)
                        statement298 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement298.tree)


                        # AST Rewrite
                        # elements: localModifierList, expression, IDENT, type, statement
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 687:77: -> ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement )
                            # Java.g:687:81: ^( FOR_EACH[$FOR, \"FOR_EACH\"] localModifierList type IDENT expression statement )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.create(FOR_EACH, FOR283, "FOR_EACH")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_localModifierList.nextTree())

                            self._adaptor.addChild(root_1, stream_type.nextTree())

                            self._adaptor.addChild(root_1, 
                            stream_IDENT.nextNode()
                            )

                            self._adaptor.addChild(root_1, stream_expression.nextTree())

                            self._adaptor.addChild(root_1, stream_statement.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt97 == 5:
                    # Java.g:689:9: WHILE parenthesizedExpression statement
                    pass 
                    WHILE299 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement9316) 
                    if self._state.backtracking == 0:
                        stream_WHILE.add(WHILE299)


                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9318)
                    parenthesizedExpression300 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression300.tree)


                    self._state.following.append(self.FOLLOW_statement_in_statement9320)
                    statement301 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement301.tree)


                    # AST Rewrite
                    # elements: parenthesizedExpression, WHILE, statement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 689:77: -> ^( WHILE parenthesizedExpression statement )
                        # Java.g:689:81: ^( WHILE parenthesizedExpression statement )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_WHILE.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 6:
                    # Java.g:690:9: DO statement WHILE parenthesizedExpression SEMI
                    pass 
                    DO302 = self.match(self.input, DO, self.FOLLOW_DO_in_statement9369) 
                    if self._state.backtracking == 0:
                        stream_DO.add(DO302)


                    self._state.following.append(self.FOLLOW_statement_in_statement9371)
                    statement303 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement303.tree)


                    WHILE304 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement9373) 
                    if self._state.backtracking == 0:
                        stream_WHILE.add(WHILE304)


                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9375)
                    parenthesizedExpression305 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression305.tree)


                    SEMI306 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9377) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI306)


                    # AST Rewrite
                    # elements: parenthesizedExpression, statement, DO
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 690:77: -> ^( DO statement parenthesizedExpression )
                        # Java.g:690:81: ^( DO statement parenthesizedExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_DO.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 7:
                    # Java.g:691:9: TRY block ( catches ( finallyClause )? | finallyClause )
                    pass 
                    TRY307 = self.match(self.input, TRY, self.FOLLOW_TRY_in_statement9418) 
                    if self._state.backtracking == 0:
                        stream_TRY.add(TRY307)


                    self._state.following.append(self.FOLLOW_block_in_statement9420)
                    block308 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block308.tree)


                    # Java.g:691:19: ( catches ( finallyClause )? | finallyClause )
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == CATCH) :
                        alt93 = 1
                    elif (LA93_0 == FINALLY) :
                        alt93 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 93, 0, self.input)

                        raise nvae


                    if alt93 == 1:
                        # Java.g:691:20: catches ( finallyClause )?
                        pass 
                        self._state.following.append(self.FOLLOW_catches_in_statement9423)
                        catches309 = self.catches()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_catches.add(catches309.tree)


                        # Java.g:691:28: ( finallyClause )?
                        alt92 = 2
                        LA92_0 = self.input.LA(1)

                        if (LA92_0 == FINALLY) :
                            alt92 = 1
                        if alt92 == 1:
                            # Java.g:691:28: finallyClause
                            pass 
                            self._state.following.append(self.FOLLOW_finallyClause_in_statement9425)
                            finallyClause310 = self.finallyClause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_finallyClause.add(finallyClause310.tree)






                    elif alt93 == 2:
                        # Java.g:691:45: finallyClause
                        pass 
                        self._state.following.append(self.FOLLOW_finallyClause_in_statement9430)
                        finallyClause311 = self.finallyClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_finallyClause.add(finallyClause311.tree)





                    # AST Rewrite
                    # elements: TRY, catches, block, finallyClause
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 691:77: -> ^( TRY block ( catches )? ( finallyClause )? )
                        # Java.g:691:81: ^( TRY block ( catches )? ( finallyClause )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_TRY.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        # Java.g:691:93: ( catches )?
                        if stream_catches.hasNext():
                            self._adaptor.addChild(root_1, stream_catches.nextTree())


                        stream_catches.reset();

                        # Java.g:691:102: ( finallyClause )?
                        if stream_finallyClause.hasNext():
                            self._adaptor.addChild(root_1, stream_finallyClause.nextTree())


                        stream_finallyClause.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 8:
                    # Java.g:692:9: SWITCH parenthesizedExpression LCURLY switchBlockLabels RCURLY
                    pass 
                    SWITCH312 = self.match(self.input, SWITCH, self.FOLLOW_SWITCH_in_statement9473) 
                    if self._state.backtracking == 0:
                        stream_SWITCH.add(SWITCH312)


                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9475)
                    parenthesizedExpression313 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression313.tree)


                    LCURLY314 = self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_statement9477) 
                    if self._state.backtracking == 0:
                        stream_LCURLY.add(LCURLY314)


                    self._state.following.append(self.FOLLOW_switchBlockLabels_in_statement9479)
                    switchBlockLabels315 = self.switchBlockLabels()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_switchBlockLabels.add(switchBlockLabels315.tree)


                    RCURLY316 = self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_statement9481) 
                    if self._state.backtracking == 0:
                        stream_RCURLY.add(RCURLY316)


                    # AST Rewrite
                    # elements: SWITCH, switchBlockLabels, parenthesizedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 692:77: -> ^( SWITCH parenthesizedExpression switchBlockLabels )
                        # Java.g:692:81: ^( SWITCH parenthesizedExpression switchBlockLabels )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_SWITCH.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                        self._adaptor.addChild(root_1, stream_switchBlockLabels.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 9:
                    # Java.g:693:9: SYNCHRONIZED parenthesizedExpression block
                    pass 
                    SYNCHRONIZED317 = self.match(self.input, SYNCHRONIZED, self.FOLLOW_SYNCHRONIZED_in_statement9507) 
                    if self._state.backtracking == 0:
                        stream_SYNCHRONIZED.add(SYNCHRONIZED317)


                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_statement9509)
                    parenthesizedExpression318 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parenthesizedExpression.add(parenthesizedExpression318.tree)


                    self._state.following.append(self.FOLLOW_block_in_statement9511)
                    block319 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block319.tree)


                    # AST Rewrite
                    # elements: parenthesizedExpression, SYNCHRONIZED, block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 693:77: -> ^( SYNCHRONIZED parenthesizedExpression block )
                        # Java.g:693:81: ^( SYNCHRONIZED parenthesizedExpression block )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_SYNCHRONIZED.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_parenthesizedExpression.nextTree())

                        self._adaptor.addChild(root_1, stream_block.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 10:
                    # Java.g:694:9: RETURN ( expression )? SEMI
                    pass 
                    RETURN320 = self.match(self.input, RETURN, self.FOLLOW_RETURN_in_statement9557) 
                    if self._state.backtracking == 0:
                        stream_RETURN.add(RETURN320)


                    # Java.g:694:16: ( expression )?
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == BOOLEAN or LA94_0 == BYTE or (CHAR <= LA94_0 <= CHARACTER_LITERAL) or (DEC <= LA94_0 <= DECIMAL_LITERAL) or LA94_0 == DOUBLE or LA94_0 == FALSE or (FLOAT <= LA94_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA94_0 <= IDENT) or LA94_0 == INC or LA94_0 == INT or LA94_0 == LESS_THAN or LA94_0 == LOGICAL_NOT or (LONG <= LA94_0 <= LPAREN) or LA94_0 == MINUS or (NEW <= LA94_0 <= NOT) or LA94_0 == NULL or LA94_0 == OCTAL_LITERAL or LA94_0 == PLUS or LA94_0 == SHORT or (STRING_LITERAL <= LA94_0 <= SUPER) or LA94_0 == THIS or LA94_0 == TRUE or LA94_0 == VOID) :
                        alt94 = 1
                    if alt94 == 1:
                        # Java.g:694:16: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_statement9559)
                        expression321 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression321.tree)





                    SEMI322 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9562) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI322)


                    # AST Rewrite
                    # elements: RETURN, expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 694:77: -> ^( RETURN ( expression )? )
                        # Java.g:694:81: ^( RETURN ( expression )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_RETURN.nextNode()
                        , root_1)

                        # Java.g:694:90: ( expression )?
                        if stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 11:
                    # Java.g:695:9: THROW expression SEMI
                    pass 
                    THROW323 = self.match(self.input, THROW, self.FOLLOW_THROW_in_statement9626) 
                    if self._state.backtracking == 0:
                        stream_THROW.add(THROW323)


                    self._state.following.append(self.FOLLOW_expression_in_statement9628)
                    expression324 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression324.tree)


                    SEMI325 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9630) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI325)


                    # AST Rewrite
                    # elements: THROW, expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 695:77: -> ^( THROW expression )
                        # Java.g:695:81: ^( THROW expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_THROW.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 12:
                    # Java.g:696:9: BREAK ( IDENT )? SEMI
                    pass 
                    BREAK326 = self.match(self.input, BREAK, self.FOLLOW_BREAK_in_statement9695) 
                    if self._state.backtracking == 0:
                        stream_BREAK.add(BREAK326)


                    # Java.g:696:15: ( IDENT )?
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == IDENT) :
                        alt95 = 1
                    if alt95 == 1:
                        # Java.g:696:15: IDENT
                        pass 
                        IDENT327 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9697) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT327)





                    SEMI328 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9700) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI328)


                    # AST Rewrite
                    # elements: IDENT, BREAK
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 696:77: -> ^( BREAK ( IDENT )? )
                        # Java.g:696:81: ^( BREAK ( IDENT )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_BREAK.nextNode()
                        , root_1)

                        # Java.g:696:89: ( IDENT )?
                        if stream_IDENT.hasNext():
                            self._adaptor.addChild(root_1, 
                            stream_IDENT.nextNode()
                            )


                        stream_IDENT.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 13:
                    # Java.g:697:9: CONTINUE ( IDENT )? SEMI
                    pass 
                    CONTINUE329 = self.match(self.input, CONTINUE, self.FOLLOW_CONTINUE_in_statement9770) 
                    if self._state.backtracking == 0:
                        stream_CONTINUE.add(CONTINUE329)


                    # Java.g:697:18: ( IDENT )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == IDENT) :
                        alt96 = 1
                    if alt96 == 1:
                        # Java.g:697:18: IDENT
                        pass 
                        IDENT330 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9772) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT330)





                    SEMI331 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9775) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI331)


                    # AST Rewrite
                    # elements: CONTINUE, IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 697:77: -> ^( CONTINUE ( IDENT )? )
                        # Java.g:697:81: ^( CONTINUE ( IDENT )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_CONTINUE.nextNode()
                        , root_1)

                        # Java.g:697:92: ( IDENT )?
                        if stream_IDENT.hasNext():
                            self._adaptor.addChild(root_1, 
                            stream_IDENT.nextNode()
                            )


                        stream_IDENT.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 14:
                    # Java.g:698:9: IDENT COLON statement
                    pass 
                    IDENT332 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement9842) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT332)


                    COLON333 = self.match(self.input, COLON, self.FOLLOW_COLON_in_statement9844) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON333)


                    self._state.following.append(self.FOLLOW_statement_in_statement9846)
                    statement334 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement334.tree)


                    # AST Rewrite
                    # elements: IDENT, statement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 698:77: -> ^( LABELED_STATEMENT IDENT statement )
                        # Java.g:698:81: ^( LABELED_STATEMENT IDENT statement )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LABELED_STATEMENT, "LABELED_STATEMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_IDENT.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt97 == 15:
                    # Java.g:699:9: expression SEMI !
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expression_in_statement9913)
                    expression335 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression335.tree)


                    SEMI336 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9915)


                elif alt97 == 16:
                    # Java.g:700:9: SEMI
                    pass 
                    root_0 = self._adaptor.nil()


                    SEMI337 = self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement9926)
                    if self._state.backtracking == 0:
                        SEMI337_tree = self._adaptor.createWithPayload(SEMI337)
                        self._adaptor.addChild(root_0, SEMI337_tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 75, statement_StartIndex, success)


            pass
        return retval

    # $ANTLR end "statement"


    class catches_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.catches_return, self).__init__()

            self.tree = None





    # $ANTLR start "catches"
    # Java.g:703:1: catches : ( catchClause )+ -> ^( CATCH_CLAUSE_LIST ( catchClause )+ ) ;
    def catches(self, ):
        retval = self.catches_return()
        retval.start = self.input.LT(1)

        catches_StartIndex = self.input.index()

        root_0 = None

        catchClause338 = None


        stream_catchClause = RewriteRuleSubtreeStream(self._adaptor, "rule catchClause")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:704:5: ( ( catchClause )+ -> ^( CATCH_CLAUSE_LIST ( catchClause )+ ) )
                # Java.g:704:9: ( catchClause )+
                pass 
                # Java.g:704:9: ( catchClause )+
                cnt98 = 0
                while True: #loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if (LA98_0 == CATCH) :
                        alt98 = 1


                    if alt98 == 1:
                        # Java.g:704:9: catchClause
                        pass 
                        self._state.following.append(self.FOLLOW_catchClause_in_catches9965)
                        catchClause338 = self.catchClause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_catchClause.add(catchClause338.tree)



                    else:
                        if cnt98 >= 1:
                            break #loop98

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(98, self.input)
                        raise eee

                    cnt98 += 1


                # AST Rewrite
                # elements: catchClause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 705:9: -> ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                    # Java.g:705:13: ^( CATCH_CLAUSE_LIST ( catchClause )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(CATCH_CLAUSE_LIST, "CATCH_CLAUSE_LIST")
                    , root_1)

                    # Java.g:705:33: ( catchClause )+
                    if not (stream_catchClause.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_catchClause.hasNext():
                        self._adaptor.addChild(root_1, stream_catchClause.nextTree())


                    stream_catchClause.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 76, catches_StartIndex, success)


            pass
        return retval

    # $ANTLR end "catches"


    class catchClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.catchClause_return, self).__init__()

            self.tree = None





    # $ANTLR start "catchClause"
    # Java.g:708:1: catchClause : CATCH ^ LPAREN ! formalParameterStandardDecl RPAREN ! block ;
    def catchClause(self, ):
        retval = self.catchClause_return()
        retval.start = self.input.LT(1)

        catchClause_StartIndex = self.input.index()

        root_0 = None

        CATCH339 = None
        LPAREN340 = None
        RPAREN342 = None
        formalParameterStandardDecl341 = None

        block343 = None


        CATCH339_tree = None
        LPAREN340_tree = None
        RPAREN342_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:709:5: ( CATCH ^ LPAREN ! formalParameterStandardDecl RPAREN ! block )
                # Java.g:709:9: CATCH ^ LPAREN ! formalParameterStandardDecl RPAREN ! block
                pass 
                root_0 = self._adaptor.nil()


                CATCH339 = self.match(self.input, CATCH, self.FOLLOW_CATCH_in_catchClause10007)
                if self._state.backtracking == 0:
                    CATCH339_tree = self._adaptor.createWithPayload(CATCH339)
                    root_0 = self._adaptor.becomeRoot(CATCH339_tree, root_0)



                LPAREN340 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_catchClause10010)

                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_catchClause10013)
                formalParameterStandardDecl341 = self.formalParameterStandardDecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, formalParameterStandardDecl341.tree)


                RPAREN342 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_catchClause10015)

                self._state.following.append(self.FOLLOW_block_in_catchClause10018)
                block343 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block343.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 77, catchClause_StartIndex, success)


            pass
        return retval

    # $ANTLR end "catchClause"


    class finallyClause_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.finallyClause_return, self).__init__()

            self.tree = None





    # $ANTLR start "finallyClause"
    # Java.g:712:1: finallyClause : FINALLY block -> block ;
    def finallyClause(self, ):
        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)

        finallyClause_StartIndex = self.input.index()

        root_0 = None

        FINALLY344 = None
        block345 = None


        FINALLY344_tree = None
        stream_FINALLY = RewriteRuleTokenStream(self._adaptor, "token FINALLY")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:713:5: ( FINALLY block -> block )
                # Java.g:713:9: FINALLY block
                pass 
                FINALLY344 = self.match(self.input, FINALLY, self.FOLLOW_FINALLY_in_finallyClause10037) 
                if self._state.backtracking == 0:
                    stream_FINALLY.add(FINALLY344)


                self._state.following.append(self.FOLLOW_block_in_finallyClause10039)
                block345 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block.add(block345.tree)


                # AST Rewrite
                # elements: block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 714:9: -> block
                    self._adaptor.addChild(root_0, stream_block.nextTree())




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 78, finallyClause_StartIndex, success)


            pass
        return retval

    # $ANTLR end "finallyClause"


    class switchBlockLabels_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.switchBlockLabels_return, self).__init__()

            self.tree = None





    # $ANTLR start "switchBlockLabels"
    # Java.g:717:1: switchBlockLabels : switchCaseLabels ( switchDefaultLabel )? switchCaseLabels -> ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? switchCaseLabels ) ;
    def switchBlockLabels(self, ):
        retval = self.switchBlockLabels_return()
        retval.start = self.input.LT(1)

        switchBlockLabels_StartIndex = self.input.index()

        root_0 = None

        switchCaseLabels346 = None

        switchDefaultLabel347 = None

        switchCaseLabels348 = None


        stream_switchDefaultLabel = RewriteRuleSubtreeStream(self._adaptor, "rule switchDefaultLabel")
        stream_switchCaseLabels = RewriteRuleSubtreeStream(self._adaptor, "rule switchCaseLabels")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:718:5: ( switchCaseLabels ( switchDefaultLabel )? switchCaseLabels -> ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? switchCaseLabels ) )
                # Java.g:718:9: switchCaseLabels ( switchDefaultLabel )? switchCaseLabels
                pass 
                self._state.following.append(self.FOLLOW_switchCaseLabels_in_switchBlockLabels10071)
                switchCaseLabels346 = self.switchCaseLabels()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_switchCaseLabels.add(switchCaseLabels346.tree)


                # Java.g:718:26: ( switchDefaultLabel )?
                alt99 = 2
                LA99_0 = self.input.LA(1)

                if (LA99_0 == DEFAULT) :
                    alt99 = 1
                if alt99 == 1:
                    # Java.g:718:26: switchDefaultLabel
                    pass 
                    self._state.following.append(self.FOLLOW_switchDefaultLabel_in_switchBlockLabels10073)
                    switchDefaultLabel347 = self.switchDefaultLabel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_switchDefaultLabel.add(switchDefaultLabel347.tree)





                self._state.following.append(self.FOLLOW_switchCaseLabels_in_switchBlockLabels10076)
                switchCaseLabels348 = self.switchCaseLabels()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_switchCaseLabels.add(switchCaseLabels348.tree)


                # AST Rewrite
                # elements: switchDefaultLabel, switchCaseLabels, switchCaseLabels
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 719:9: -> ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? switchCaseLabels )
                    # Java.g:719:13: ^( SWITCH_BLOCK_LABEL_LIST switchCaseLabels ( switchDefaultLabel )? switchCaseLabels )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(SWITCH_BLOCK_LABEL_LIST, "SWITCH_BLOCK_LABEL_LIST")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_switchCaseLabels.nextTree())

                    # Java.g:719:56: ( switchDefaultLabel )?
                    if stream_switchDefaultLabel.hasNext():
                        self._adaptor.addChild(root_1, stream_switchDefaultLabel.nextTree())


                    stream_switchDefaultLabel.reset();

                    self._adaptor.addChild(root_1, stream_switchCaseLabels.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 79, switchBlockLabels_StartIndex, success)


            pass
        return retval

    # $ANTLR end "switchBlockLabels"


    class switchCaseLabels_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.switchCaseLabels_return, self).__init__()

            self.tree = None





    # $ANTLR start "switchCaseLabels"
    # Java.g:722:1: switchCaseLabels : ( switchCaseLabel )* ;
    def switchCaseLabels(self, ):
        retval = self.switchCaseLabels_return()
        retval.start = self.input.LT(1)

        switchCaseLabels_StartIndex = self.input.index()

        root_0 = None

        switchCaseLabel349 = None



        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:723:5: ( ( switchCaseLabel )* )
                # Java.g:723:9: ( switchCaseLabel )*
                pass 
                root_0 = self._adaptor.nil()


                # Java.g:723:9: ( switchCaseLabel )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == CASE) :
                        LA100_2 = self.input.LA(2)

                        if (self.synpred143_Java()) :
                            alt100 = 1




                    if alt100 == 1:
                        # Java.g:723:9: switchCaseLabel
                        pass 
                        self._state.following.append(self.FOLLOW_switchCaseLabel_in_switchCaseLabels10121)
                        switchCaseLabel349 = self.switchCaseLabel()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, switchCaseLabel349.tree)



                    else:
                        break #loop100




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 80, switchCaseLabels_StartIndex, success)


            pass
        return retval

    # $ANTLR end "switchCaseLabels"


    class switchCaseLabel_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.switchCaseLabel_return, self).__init__()

            self.tree = None





    # $ANTLR start "switchCaseLabel"
    # Java.g:726:1: switchCaseLabel : CASE ^ expression COLON ! ( blockStatement )* ;
    def switchCaseLabel(self, ):
        retval = self.switchCaseLabel_return()
        retval.start = self.input.LT(1)

        switchCaseLabel_StartIndex = self.input.index()

        root_0 = None

        CASE350 = None
        COLON352 = None
        expression351 = None

        blockStatement353 = None


        CASE350_tree = None
        COLON352_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:727:5: ( CASE ^ expression COLON ! ( blockStatement )* )
                # Java.g:727:9: CASE ^ expression COLON ! ( blockStatement )*
                pass 
                root_0 = self._adaptor.nil()


                CASE350 = self.match(self.input, CASE, self.FOLLOW_CASE_in_switchCaseLabel10149)
                if self._state.backtracking == 0:
                    CASE350_tree = self._adaptor.createWithPayload(CASE350)
                    root_0 = self._adaptor.becomeRoot(CASE350_tree, root_0)



                self._state.following.append(self.FOLLOW_expression_in_switchCaseLabel10152)
                expression351 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression351.tree)


                COLON352 = self.match(self.input, COLON, self.FOLLOW_COLON_in_switchCaseLabel10154)

                # Java.g:727:33: ( blockStatement )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == ABSTRACT or LA101_0 == ASSERT or LA101_0 == AT or (BOOLEAN <= LA101_0 <= BYTE) or (CHAR <= LA101_0 <= CLASS) or (CONTINUE <= LA101_0 <= DECIMAL_LITERAL) or LA101_0 == DO or LA101_0 == DOUBLE or LA101_0 == ENUM or (FALSE <= LA101_0 <= FINAL) or (FLOAT <= LA101_0 <= FLOATING_POINT_LITERAL) or LA101_0 == FOR or (HEX_LITERAL <= LA101_0 <= IF) or LA101_0 == INC or LA101_0 == INT or LA101_0 == INTERFACE or LA101_0 == LCURLY or LA101_0 == LESS_THAN or LA101_0 == LOGICAL_NOT or (LONG <= LA101_0 <= LPAREN) or LA101_0 == MINUS or (NATIVE <= LA101_0 <= NOT) or LA101_0 == NULL or LA101_0 == OCTAL_LITERAL or LA101_0 == PLUS or (PRIVATE <= LA101_0 <= PUBLIC) or LA101_0 == RETURN or LA101_0 == SEMI or LA101_0 == SHORT or LA101_0 == STATIC or (STRICTFP <= LA101_0 <= SUPER) or LA101_0 == SWITCH or (SYNCHRONIZED <= LA101_0 <= THIS) or LA101_0 == THROW or (TRANSIENT <= LA101_0 <= TRY) or LA101_0 == VOID or (VOLATILE <= LA101_0 <= WHILE)) :
                        alt101 = 1


                    if alt101 == 1:
                        # Java.g:727:33: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchCaseLabel10157)
                        blockStatement353 = self.blockStatement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blockStatement353.tree)



                    else:
                        break #loop101




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 81, switchCaseLabel_StartIndex, success)


            pass
        return retval

    # $ANTLR end "switchCaseLabel"


    class switchDefaultLabel_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.switchDefaultLabel_return, self).__init__()

            self.tree = None





    # $ANTLR start "switchDefaultLabel"
    # Java.g:730:1: switchDefaultLabel : DEFAULT ^ COLON ! ( blockStatement )* ;
    def switchDefaultLabel(self, ):
        retval = self.switchDefaultLabel_return()
        retval.start = self.input.LT(1)

        switchDefaultLabel_StartIndex = self.input.index()

        root_0 = None

        DEFAULT354 = None
        COLON355 = None
        blockStatement356 = None


        DEFAULT354_tree = None
        COLON355_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:731:5: ( DEFAULT ^ COLON ! ( blockStatement )* )
                # Java.g:731:9: DEFAULT ^ COLON ! ( blockStatement )*
                pass 
                root_0 = self._adaptor.nil()


                DEFAULT354 = self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_switchDefaultLabel10181)
                if self._state.backtracking == 0:
                    DEFAULT354_tree = self._adaptor.createWithPayload(DEFAULT354)
                    root_0 = self._adaptor.becomeRoot(DEFAULT354_tree, root_0)



                COLON355 = self.match(self.input, COLON, self.FOLLOW_COLON_in_switchDefaultLabel10184)

                # Java.g:731:25: ( blockStatement )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == ABSTRACT or LA102_0 == ASSERT or LA102_0 == AT or (BOOLEAN <= LA102_0 <= BYTE) or (CHAR <= LA102_0 <= CLASS) or (CONTINUE <= LA102_0 <= DECIMAL_LITERAL) or LA102_0 == DO or LA102_0 == DOUBLE or LA102_0 == ENUM or (FALSE <= LA102_0 <= FINAL) or (FLOAT <= LA102_0 <= FLOATING_POINT_LITERAL) or LA102_0 == FOR or (HEX_LITERAL <= LA102_0 <= IF) or LA102_0 == INC or LA102_0 == INT or LA102_0 == INTERFACE or LA102_0 == LCURLY or LA102_0 == LESS_THAN or LA102_0 == LOGICAL_NOT or (LONG <= LA102_0 <= LPAREN) or LA102_0 == MINUS or (NATIVE <= LA102_0 <= NOT) or LA102_0 == NULL or LA102_0 == OCTAL_LITERAL or LA102_0 == PLUS or (PRIVATE <= LA102_0 <= PUBLIC) or LA102_0 == RETURN or LA102_0 == SEMI or LA102_0 == SHORT or LA102_0 == STATIC or (STRICTFP <= LA102_0 <= SUPER) or LA102_0 == SWITCH or (SYNCHRONIZED <= LA102_0 <= THIS) or LA102_0 == THROW or (TRANSIENT <= LA102_0 <= TRY) or LA102_0 == VOID or (VOLATILE <= LA102_0 <= WHILE)) :
                        alt102 = 1


                    if alt102 == 1:
                        # Java.g:731:25: blockStatement
                        pass 
                        self._state.following.append(self.FOLLOW_blockStatement_in_switchDefaultLabel10187)
                        blockStatement356 = self.blockStatement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, blockStatement356.tree)



                    else:
                        break #loop102




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 82, switchDefaultLabel_StartIndex, success)


            pass
        return retval

    # $ANTLR end "switchDefaultLabel"


    class forInit_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.forInit_return, self).__init__()

            self.tree = None





    # $ANTLR start "forInit"
    # Java.g:734:1: forInit : ( localVariableDeclaration -> ^( FOR_INIT localVariableDeclaration ) | expressionList -> ^( FOR_INIT expressionList ) | -> ^( FOR_INIT ) );
    def forInit(self, ):
        retval = self.forInit_return()
        retval.start = self.input.LT(1)

        forInit_StartIndex = self.input.index()

        root_0 = None

        localVariableDeclaration357 = None

        expressionList358 = None


        stream_expressionList = RewriteRuleSubtreeStream(self._adaptor, "rule expressionList")
        stream_localVariableDeclaration = RewriteRuleSubtreeStream(self._adaptor, "rule localVariableDeclaration")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:735:5: ( localVariableDeclaration -> ^( FOR_INIT localVariableDeclaration ) | expressionList -> ^( FOR_INIT expressionList ) | -> ^( FOR_INIT ) )
                alt103 = 3
                LA103 = self.input.LA(1)
                if LA103 == AT or LA103 == FINAL:
                    alt103 = 1
                elif LA103 == BOOLEAN or LA103 == BYTE or LA103 == CHAR or LA103 == DOUBLE or LA103 == FLOAT or LA103 == INT or LA103 == LONG or LA103 == SHORT:
                    LA103_3 = self.input.LA(2)

                    if (self.synpred146_Java()) :
                        alt103 = 1
                    elif (self.synpred147_Java()) :
                        alt103 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 103, 3, self.input)

                        raise nvae


                elif LA103 == IDENT:
                    LA103_4 = self.input.LA(2)

                    if (self.synpred146_Java()) :
                        alt103 = 1
                    elif (self.synpred147_Java()) :
                        alt103 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 103, 4, self.input)

                        raise nvae


                elif LA103 == CHARACTER_LITERAL or LA103 == DEC or LA103 == DECIMAL_LITERAL or LA103 == FALSE or LA103 == FLOATING_POINT_LITERAL or LA103 == HEX_LITERAL or LA103 == INC or LA103 == LESS_THAN or LA103 == LOGICAL_NOT or LA103 == LPAREN or LA103 == MINUS or LA103 == NEW or LA103 == NOT or LA103 == NULL or LA103 == OCTAL_LITERAL or LA103 == PLUS or LA103 == STRING_LITERAL or LA103 == SUPER or LA103 == THIS or LA103 == TRUE or LA103 == VOID:
                    alt103 = 2
                elif LA103 == SEMI:
                    alt103 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 103, 0, self.input)

                    raise nvae


                if alt103 == 1:
                    # Java.g:735:9: localVariableDeclaration
                    pass 
                    self._state.following.append(self.FOLLOW_localVariableDeclaration_in_forInit10211)
                    localVariableDeclaration357 = self.localVariableDeclaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localVariableDeclaration.add(localVariableDeclaration357.tree)


                    # AST Rewrite
                    # elements: localVariableDeclaration
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 735:37: -> ^( FOR_INIT localVariableDeclaration )
                        # Java.g:735:41: ^( FOR_INIT localVariableDeclaration )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(FOR_INIT, "FOR_INIT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_localVariableDeclaration.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt103 == 2:
                    # Java.g:736:9: expressionList
                    pass 
                    self._state.following.append(self.FOLLOW_expressionList_in_forInit10233)
                    expressionList358 = self.expressionList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressionList.add(expressionList358.tree)


                    # AST Rewrite
                    # elements: expressionList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 736:37: -> ^( FOR_INIT expressionList )
                        # Java.g:736:41: ^( FOR_INIT expressionList )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(FOR_INIT, "FOR_INIT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_expressionList.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt103 == 3:
                    # Java.g:737:37: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 737:37: -> ^( FOR_INIT )
                        # Java.g:737:41: ^( FOR_INIT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(FOR_INIT, "FOR_INIT")
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 83, forInit_StartIndex, success)


            pass
        return retval

    # $ANTLR end "forInit"


    class forCondition_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.forCondition_return, self).__init__()

            self.tree = None





    # $ANTLR start "forCondition"
    # Java.g:740:1: forCondition : ( expression )? -> ^( FOR_CONDITION ( expression )? ) ;
    def forCondition(self, ):
        retval = self.forCondition_return()
        retval.start = self.input.LT(1)

        forCondition_StartIndex = self.input.index()

        root_0 = None

        expression359 = None


        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:741:5: ( ( expression )? -> ^( FOR_CONDITION ( expression )? ) )
                # Java.g:741:9: ( expression )?
                pass 
                # Java.g:741:9: ( expression )?
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if (LA104_0 == BOOLEAN or LA104_0 == BYTE or (CHAR <= LA104_0 <= CHARACTER_LITERAL) or (DEC <= LA104_0 <= DECIMAL_LITERAL) or LA104_0 == DOUBLE or LA104_0 == FALSE or (FLOAT <= LA104_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA104_0 <= IDENT) or LA104_0 == INC or LA104_0 == INT or LA104_0 == LESS_THAN or LA104_0 == LOGICAL_NOT or (LONG <= LA104_0 <= LPAREN) or LA104_0 == MINUS or (NEW <= LA104_0 <= NOT) or LA104_0 == NULL or LA104_0 == OCTAL_LITERAL or LA104_0 == PLUS or LA104_0 == SHORT or (STRING_LITERAL <= LA104_0 <= SUPER) or LA104_0 == THIS or LA104_0 == TRUE or LA104_0 == VOID) :
                    alt104 = 1
                if alt104 == 1:
                    # Java.g:741:9: expression
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_forCondition10321)
                    expression359 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression359.tree)





                # AST Rewrite
                # elements: expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 742:9: -> ^( FOR_CONDITION ( expression )? )
                    # Java.g:742:13: ^( FOR_CONDITION ( expression )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(FOR_CONDITION, "FOR_CONDITION")
                    , root_1)

                    # Java.g:742:29: ( expression )?
                    if stream_expression.hasNext():
                        self._adaptor.addChild(root_1, stream_expression.nextTree())


                    stream_expression.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 84, forCondition_StartIndex, success)


            pass
        return retval

    # $ANTLR end "forCondition"


    class forUpdater_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.forUpdater_return, self).__init__()

            self.tree = None





    # $ANTLR start "forUpdater"
    # Java.g:745:1: forUpdater : ( expressionList )? -> ^( FOR_UPDATE ( expressionList )? ) ;
    def forUpdater(self, ):
        retval = self.forUpdater_return()
        retval.start = self.input.LT(1)

        forUpdater_StartIndex = self.input.index()

        root_0 = None

        expressionList360 = None


        stream_expressionList = RewriteRuleSubtreeStream(self._adaptor, "rule expressionList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 85):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:746:5: ( ( expressionList )? -> ^( FOR_UPDATE ( expressionList )? ) )
                # Java.g:746:9: ( expressionList )?
                pass 
                # Java.g:746:9: ( expressionList )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if (LA105_0 == BOOLEAN or LA105_0 == BYTE or (CHAR <= LA105_0 <= CHARACTER_LITERAL) or (DEC <= LA105_0 <= DECIMAL_LITERAL) or LA105_0 == DOUBLE or LA105_0 == FALSE or (FLOAT <= LA105_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA105_0 <= IDENT) or LA105_0 == INC or LA105_0 == INT or LA105_0 == LESS_THAN or LA105_0 == LOGICAL_NOT or (LONG <= LA105_0 <= LPAREN) or LA105_0 == MINUS or (NEW <= LA105_0 <= NOT) or LA105_0 == NULL or LA105_0 == OCTAL_LITERAL or LA105_0 == PLUS or LA105_0 == SHORT or (STRING_LITERAL <= LA105_0 <= SUPER) or LA105_0 == THIS or LA105_0 == TRUE or LA105_0 == VOID) :
                    alt105 = 1
                if alt105 == 1:
                    # Java.g:746:9: expressionList
                    pass 
                    self._state.following.append(self.FOLLOW_expressionList_in_forUpdater10363)
                    expressionList360 = self.expressionList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressionList.add(expressionList360.tree)





                # AST Rewrite
                # elements: expressionList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 747:9: -> ^( FOR_UPDATE ( expressionList )? )
                    # Java.g:747:13: ^( FOR_UPDATE ( expressionList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(FOR_UPDATE, "FOR_UPDATE")
                    , root_1)

                    # Java.g:747:26: ( expressionList )?
                    if stream_expressionList.hasNext():
                        self._adaptor.addChild(root_1, stream_expressionList.nextTree())


                    stream_expressionList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 85, forUpdater_StartIndex, success)


            pass
        return retval

    # $ANTLR end "forUpdater"


    class parenthesizedExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.parenthesizedExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "parenthesizedExpression"
    # Java.g:752:1: parenthesizedExpression : LPAREN expression RPAREN -> ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression ) ;
    def parenthesizedExpression(self, ):
        retval = self.parenthesizedExpression_return()
        retval.start = self.input.LT(1)

        parenthesizedExpression_StartIndex = self.input.index()

        root_0 = None

        LPAREN361 = None
        RPAREN363 = None
        expression362 = None


        LPAREN361_tree = None
        RPAREN363_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 86):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:753:5: ( LPAREN expression RPAREN -> ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression ) )
                # Java.g:753:9: LPAREN expression RPAREN
                pass 
                LPAREN361 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parenthesizedExpression10403) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN361)


                self._state.following.append(self.FOLLOW_expression_in_parenthesizedExpression10405)
                expression362 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression362.tree)


                RPAREN363 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parenthesizedExpression10407) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN363)


                # AST Rewrite
                # elements: expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 754:9: -> ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression )
                    # Java.g:754:13: ^( PARENTESIZED_EXPR[$LPAREN, \"PARENTESIZED_EXPR\"] expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(PARENTESIZED_EXPR, LPAREN361, "PARENTESIZED_EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 86, parenthesizedExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "parenthesizedExpression"


    class expressionList_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.expressionList_return, self).__init__()

            self.tree = None





    # $ANTLR start "expressionList"
    # Java.g:757:1: expressionList : expression ( COMMA ! expression )* ;
    def expressionList(self, ):
        retval = self.expressionList_return()
        retval.start = self.input.LT(1)

        expressionList_StartIndex = self.input.index()

        root_0 = None

        COMMA365 = None
        expression364 = None

        expression366 = None


        COMMA365_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 87):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:758:5: ( expression ( COMMA ! expression )* )
                # Java.g:758:9: expression ( COMMA ! expression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expression_in_expressionList10448)
                expression364 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression364.tree)


                # Java.g:758:20: ( COMMA ! expression )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == COMMA) :
                        alt106 = 1


                    if alt106 == 1:
                        # Java.g:758:21: COMMA ! expression
                        pass 
                        COMMA365 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList10451)

                        self._state.following.append(self.FOLLOW_expression_in_expressionList10454)
                        expression366 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, expression366.tree)



                    else:
                        break #loop106




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 87, expressionList_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expressionList"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.expression_return, self).__init__()

            self.tree = None





    # $ANTLR start "expression"
    # Java.g:761:1: expression : assignmentExpression -> ^( EXPR assignmentExpression ) ;
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)

        expression_StartIndex = self.input.index()

        root_0 = None

        assignmentExpression367 = None


        stream_assignmentExpression = RewriteRuleSubtreeStream(self._adaptor, "rule assignmentExpression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 88):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:762:5: ( assignmentExpression -> ^( EXPR assignmentExpression ) )
                # Java.g:762:9: assignmentExpression
                pass 
                self._state.following.append(self.FOLLOW_assignmentExpression_in_expression10475)
                assignmentExpression367 = self.assignmentExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression367.tree)


                # AST Rewrite
                # elements: assignmentExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 763:9: -> ^( EXPR assignmentExpression )
                    # Java.g:763:13: ^( EXPR assignmentExpression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_assignmentExpression.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 88, expression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "expression"


    class assignmentExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.assignmentExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "assignmentExpression"
    # Java.g:766:1: assignmentExpression : conditionalExpression ( ( ASSIGN ^| PLUS_ASSIGN ^| MINUS_ASSIGN ^| STAR_ASSIGN ^| DIV_ASSIGN ^| AND_ASSIGN ^| OR_ASSIGN ^| XOR_ASSIGN ^| MOD_ASSIGN ^| SHIFT_LEFT_ASSIGN ^| SHIFT_RIGHT_ASSIGN ^| BIT_SHIFT_RIGHT_ASSIGN ^) assignmentExpression )? ;
    def assignmentExpression(self, ):
        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)

        assignmentExpression_StartIndex = self.input.index()

        root_0 = None

        ASSIGN369 = None
        PLUS_ASSIGN370 = None
        MINUS_ASSIGN371 = None
        STAR_ASSIGN372 = None
        DIV_ASSIGN373 = None
        AND_ASSIGN374 = None
        OR_ASSIGN375 = None
        XOR_ASSIGN376 = None
        MOD_ASSIGN377 = None
        SHIFT_LEFT_ASSIGN378 = None
        SHIFT_RIGHT_ASSIGN379 = None
        BIT_SHIFT_RIGHT_ASSIGN380 = None
        conditionalExpression368 = None

        assignmentExpression381 = None


        ASSIGN369_tree = None
        PLUS_ASSIGN370_tree = None
        MINUS_ASSIGN371_tree = None
        STAR_ASSIGN372_tree = None
        DIV_ASSIGN373_tree = None
        AND_ASSIGN374_tree = None
        OR_ASSIGN375_tree = None
        XOR_ASSIGN376_tree = None
        MOD_ASSIGN377_tree = None
        SHIFT_LEFT_ASSIGN378_tree = None
        SHIFT_RIGHT_ASSIGN379_tree = None
        BIT_SHIFT_RIGHT_ASSIGN380_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 89):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:767:5: ( conditionalExpression ( ( ASSIGN ^| PLUS_ASSIGN ^| MINUS_ASSIGN ^| STAR_ASSIGN ^| DIV_ASSIGN ^| AND_ASSIGN ^| OR_ASSIGN ^| XOR_ASSIGN ^| MOD_ASSIGN ^| SHIFT_LEFT_ASSIGN ^| SHIFT_RIGHT_ASSIGN ^| BIT_SHIFT_RIGHT_ASSIGN ^) assignmentExpression )? )
                # Java.g:767:9: conditionalExpression ( ( ASSIGN ^| PLUS_ASSIGN ^| MINUS_ASSIGN ^| STAR_ASSIGN ^| DIV_ASSIGN ^| AND_ASSIGN ^| OR_ASSIGN ^| XOR_ASSIGN ^| MOD_ASSIGN ^| SHIFT_LEFT_ASSIGN ^| SHIFT_RIGHT_ASSIGN ^| BIT_SHIFT_RIGHT_ASSIGN ^) assignmentExpression )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression10511)
                conditionalExpression368 = self.conditionalExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, conditionalExpression368.tree)


                # Java.g:768:9: ( ( ASSIGN ^| PLUS_ASSIGN ^| MINUS_ASSIGN ^| STAR_ASSIGN ^| DIV_ASSIGN ^| AND_ASSIGN ^| OR_ASSIGN ^| XOR_ASSIGN ^| MOD_ASSIGN ^| SHIFT_LEFT_ASSIGN ^| SHIFT_RIGHT_ASSIGN ^| BIT_SHIFT_RIGHT_ASSIGN ^) assignmentExpression )?
                alt108 = 2
                LA108_0 = self.input.LA(1)

                if (LA108_0 == AND_ASSIGN or LA108_0 == ASSIGN or LA108_0 == BIT_SHIFT_RIGHT_ASSIGN or LA108_0 == DIV_ASSIGN or LA108_0 == MINUS_ASSIGN or LA108_0 == MOD_ASSIGN or LA108_0 == OR_ASSIGN or LA108_0 == PLUS_ASSIGN or LA108_0 == SHIFT_LEFT_ASSIGN or LA108_0 == SHIFT_RIGHT_ASSIGN or LA108_0 == STAR_ASSIGN or LA108_0 == XOR_ASSIGN) :
                    alt108 = 1
                if alt108 == 1:
                    # Java.g:768:13: ( ASSIGN ^| PLUS_ASSIGN ^| MINUS_ASSIGN ^| STAR_ASSIGN ^| DIV_ASSIGN ^| AND_ASSIGN ^| OR_ASSIGN ^| XOR_ASSIGN ^| MOD_ASSIGN ^| SHIFT_LEFT_ASSIGN ^| SHIFT_RIGHT_ASSIGN ^| BIT_SHIFT_RIGHT_ASSIGN ^) assignmentExpression
                    pass 
                    # Java.g:768:13: ( ASSIGN ^| PLUS_ASSIGN ^| MINUS_ASSIGN ^| STAR_ASSIGN ^| DIV_ASSIGN ^| AND_ASSIGN ^| OR_ASSIGN ^| XOR_ASSIGN ^| MOD_ASSIGN ^| SHIFT_LEFT_ASSIGN ^| SHIFT_RIGHT_ASSIGN ^| BIT_SHIFT_RIGHT_ASSIGN ^)
                    alt107 = 12
                    LA107 = self.input.LA(1)
                    if LA107 == ASSIGN:
                        alt107 = 1
                    elif LA107 == PLUS_ASSIGN:
                        alt107 = 2
                    elif LA107 == MINUS_ASSIGN:
                        alt107 = 3
                    elif LA107 == STAR_ASSIGN:
                        alt107 = 4
                    elif LA107 == DIV_ASSIGN:
                        alt107 = 5
                    elif LA107 == AND_ASSIGN:
                        alt107 = 6
                    elif LA107 == OR_ASSIGN:
                        alt107 = 7
                    elif LA107 == XOR_ASSIGN:
                        alt107 = 8
                    elif LA107 == MOD_ASSIGN:
                        alt107 = 9
                    elif LA107 == SHIFT_LEFT_ASSIGN:
                        alt107 = 10
                    elif LA107 == SHIFT_RIGHT_ASSIGN:
                        alt107 = 11
                    elif LA107 == BIT_SHIFT_RIGHT_ASSIGN:
                        alt107 = 12
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 107, 0, self.input)

                        raise nvae


                    if alt107 == 1:
                        # Java.g:768:17: ASSIGN ^
                        pass 
                        ASSIGN369 = self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignmentExpression10530)
                        if self._state.backtracking == 0:
                            ASSIGN369_tree = self._adaptor.createWithPayload(ASSIGN369)
                            root_0 = self._adaptor.becomeRoot(ASSIGN369_tree, root_0)




                    elif alt107 == 2:
                        # Java.g:769:17: PLUS_ASSIGN ^
                        pass 
                        PLUS_ASSIGN370 = self.match(self.input, PLUS_ASSIGN, self.FOLLOW_PLUS_ASSIGN_in_assignmentExpression10549)
                        if self._state.backtracking == 0:
                            PLUS_ASSIGN370_tree = self._adaptor.createWithPayload(PLUS_ASSIGN370)
                            root_0 = self._adaptor.becomeRoot(PLUS_ASSIGN370_tree, root_0)




                    elif alt107 == 3:
                        # Java.g:770:17: MINUS_ASSIGN ^
                        pass 
                        MINUS_ASSIGN371 = self.match(self.input, MINUS_ASSIGN, self.FOLLOW_MINUS_ASSIGN_in_assignmentExpression10568)
                        if self._state.backtracking == 0:
                            MINUS_ASSIGN371_tree = self._adaptor.createWithPayload(MINUS_ASSIGN371)
                            root_0 = self._adaptor.becomeRoot(MINUS_ASSIGN371_tree, root_0)




                    elif alt107 == 4:
                        # Java.g:771:17: STAR_ASSIGN ^
                        pass 
                        STAR_ASSIGN372 = self.match(self.input, STAR_ASSIGN, self.FOLLOW_STAR_ASSIGN_in_assignmentExpression10587)
                        if self._state.backtracking == 0:
                            STAR_ASSIGN372_tree = self._adaptor.createWithPayload(STAR_ASSIGN372)
                            root_0 = self._adaptor.becomeRoot(STAR_ASSIGN372_tree, root_0)




                    elif alt107 == 5:
                        # Java.g:772:17: DIV_ASSIGN ^
                        pass 
                        DIV_ASSIGN373 = self.match(self.input, DIV_ASSIGN, self.FOLLOW_DIV_ASSIGN_in_assignmentExpression10606)
                        if self._state.backtracking == 0:
                            DIV_ASSIGN373_tree = self._adaptor.createWithPayload(DIV_ASSIGN373)
                            root_0 = self._adaptor.becomeRoot(DIV_ASSIGN373_tree, root_0)




                    elif alt107 == 6:
                        # Java.g:773:17: AND_ASSIGN ^
                        pass 
                        AND_ASSIGN374 = self.match(self.input, AND_ASSIGN, self.FOLLOW_AND_ASSIGN_in_assignmentExpression10625)
                        if self._state.backtracking == 0:
                            AND_ASSIGN374_tree = self._adaptor.createWithPayload(AND_ASSIGN374)
                            root_0 = self._adaptor.becomeRoot(AND_ASSIGN374_tree, root_0)




                    elif alt107 == 7:
                        # Java.g:774:17: OR_ASSIGN ^
                        pass 
                        OR_ASSIGN375 = self.match(self.input, OR_ASSIGN, self.FOLLOW_OR_ASSIGN_in_assignmentExpression10644)
                        if self._state.backtracking == 0:
                            OR_ASSIGN375_tree = self._adaptor.createWithPayload(OR_ASSIGN375)
                            root_0 = self._adaptor.becomeRoot(OR_ASSIGN375_tree, root_0)




                    elif alt107 == 8:
                        # Java.g:775:17: XOR_ASSIGN ^
                        pass 
                        XOR_ASSIGN376 = self.match(self.input, XOR_ASSIGN, self.FOLLOW_XOR_ASSIGN_in_assignmentExpression10663)
                        if self._state.backtracking == 0:
                            XOR_ASSIGN376_tree = self._adaptor.createWithPayload(XOR_ASSIGN376)
                            root_0 = self._adaptor.becomeRoot(XOR_ASSIGN376_tree, root_0)




                    elif alt107 == 9:
                        # Java.g:776:17: MOD_ASSIGN ^
                        pass 
                        MOD_ASSIGN377 = self.match(self.input, MOD_ASSIGN, self.FOLLOW_MOD_ASSIGN_in_assignmentExpression10682)
                        if self._state.backtracking == 0:
                            MOD_ASSIGN377_tree = self._adaptor.createWithPayload(MOD_ASSIGN377)
                            root_0 = self._adaptor.becomeRoot(MOD_ASSIGN377_tree, root_0)




                    elif alt107 == 10:
                        # Java.g:777:17: SHIFT_LEFT_ASSIGN ^
                        pass 
                        SHIFT_LEFT_ASSIGN378 = self.match(self.input, SHIFT_LEFT_ASSIGN, self.FOLLOW_SHIFT_LEFT_ASSIGN_in_assignmentExpression10701)
                        if self._state.backtracking == 0:
                            SHIFT_LEFT_ASSIGN378_tree = self._adaptor.createWithPayload(SHIFT_LEFT_ASSIGN378)
                            root_0 = self._adaptor.becomeRoot(SHIFT_LEFT_ASSIGN378_tree, root_0)




                    elif alt107 == 11:
                        # Java.g:778:17: SHIFT_RIGHT_ASSIGN ^
                        pass 
                        SHIFT_RIGHT_ASSIGN379 = self.match(self.input, SHIFT_RIGHT_ASSIGN, self.FOLLOW_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10720)
                        if self._state.backtracking == 0:
                            SHIFT_RIGHT_ASSIGN379_tree = self._adaptor.createWithPayload(SHIFT_RIGHT_ASSIGN379)
                            root_0 = self._adaptor.becomeRoot(SHIFT_RIGHT_ASSIGN379_tree, root_0)




                    elif alt107 == 12:
                        # Java.g:779:17: BIT_SHIFT_RIGHT_ASSIGN ^
                        pass 
                        BIT_SHIFT_RIGHT_ASSIGN380 = self.match(self.input, BIT_SHIFT_RIGHT_ASSIGN, self.FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10739)
                        if self._state.backtracking == 0:
                            BIT_SHIFT_RIGHT_ASSIGN380_tree = self._adaptor.createWithPayload(BIT_SHIFT_RIGHT_ASSIGN380)
                            root_0 = self._adaptor.becomeRoot(BIT_SHIFT_RIGHT_ASSIGN380_tree, root_0)






                    self._state.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression10761)
                    assignmentExpression381 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignmentExpression381.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 89, assignmentExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "assignmentExpression"


    class conditionalExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.conditionalExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "conditionalExpression"
    # Java.g:784:1: conditionalExpression : logicalOrExpression ( QUESTION ^ assignmentExpression COLON ! conditionalExpression )? ;
    def conditionalExpression(self, ):
        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)

        conditionalExpression_StartIndex = self.input.index()

        root_0 = None

        QUESTION383 = None
        COLON385 = None
        logicalOrExpression382 = None

        assignmentExpression384 = None

        conditionalExpression386 = None


        QUESTION383_tree = None
        COLON385_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 90):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:785:5: ( logicalOrExpression ( QUESTION ^ assignmentExpression COLON ! conditionalExpression )? )
                # Java.g:785:9: logicalOrExpression ( QUESTION ^ assignmentExpression COLON ! conditionalExpression )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_logicalOrExpression_in_conditionalExpression10786)
                logicalOrExpression382 = self.logicalOrExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logicalOrExpression382.tree)


                # Java.g:785:29: ( QUESTION ^ assignmentExpression COLON ! conditionalExpression )?
                alt109 = 2
                LA109_0 = self.input.LA(1)

                if (LA109_0 == QUESTION) :
                    alt109 = 1
                if alt109 == 1:
                    # Java.g:785:30: QUESTION ^ assignmentExpression COLON ! conditionalExpression
                    pass 
                    QUESTION383 = self.match(self.input, QUESTION, self.FOLLOW_QUESTION_in_conditionalExpression10789)
                    if self._state.backtracking == 0:
                        QUESTION383_tree = self._adaptor.createWithPayload(QUESTION383)
                        root_0 = self._adaptor.becomeRoot(QUESTION383_tree, root_0)



                    self._state.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression10792)
                    assignmentExpression384 = self.assignmentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignmentExpression384.tree)


                    COLON385 = self.match(self.input, COLON, self.FOLLOW_COLON_in_conditionalExpression10794)

                    self._state.following.append(self.FOLLOW_conditionalExpression_in_conditionalExpression10797)
                    conditionalExpression386 = self.conditionalExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, conditionalExpression386.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 90, conditionalExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "conditionalExpression"


    class logicalOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.logicalOrExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "logicalOrExpression"
    # Java.g:788:1: logicalOrExpression : logicalAndExpression ( LOGICAL_OR ^ logicalAndExpression )* ;
    def logicalOrExpression(self, ):
        retval = self.logicalOrExpression_return()
        retval.start = self.input.LT(1)

        logicalOrExpression_StartIndex = self.input.index()

        root_0 = None

        LOGICAL_OR388 = None
        logicalAndExpression387 = None

        logicalAndExpression389 = None


        LOGICAL_OR388_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 91):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:789:5: ( logicalAndExpression ( LOGICAL_OR ^ logicalAndExpression )* )
                # Java.g:789:9: logicalAndExpression ( LOGICAL_OR ^ logicalAndExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_logicalAndExpression_in_logicalOrExpression10818)
                logicalAndExpression387 = self.logicalAndExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logicalAndExpression387.tree)


                # Java.g:789:30: ( LOGICAL_OR ^ logicalAndExpression )*
                while True: #loop110
                    alt110 = 2
                    LA110_0 = self.input.LA(1)

                    if (LA110_0 == LOGICAL_OR) :
                        alt110 = 1


                    if alt110 == 1:
                        # Java.g:789:31: LOGICAL_OR ^ logicalAndExpression
                        pass 
                        LOGICAL_OR388 = self.match(self.input, LOGICAL_OR, self.FOLLOW_LOGICAL_OR_in_logicalOrExpression10821)
                        if self._state.backtracking == 0:
                            LOGICAL_OR388_tree = self._adaptor.createWithPayload(LOGICAL_OR388)
                            root_0 = self._adaptor.becomeRoot(LOGICAL_OR388_tree, root_0)



                        self._state.following.append(self.FOLLOW_logicalAndExpression_in_logicalOrExpression10824)
                        logicalAndExpression389 = self.logicalAndExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, logicalAndExpression389.tree)



                    else:
                        break #loop110




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 91, logicalOrExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "logicalOrExpression"


    class logicalAndExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.logicalAndExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "logicalAndExpression"
    # Java.g:792:1: logicalAndExpression : inclusiveOrExpression ( LOGICAL_AND ^ inclusiveOrExpression )* ;
    def logicalAndExpression(self, ):
        retval = self.logicalAndExpression_return()
        retval.start = self.input.LT(1)

        logicalAndExpression_StartIndex = self.input.index()

        root_0 = None

        LOGICAL_AND391 = None
        inclusiveOrExpression390 = None

        inclusiveOrExpression392 = None


        LOGICAL_AND391_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 92):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:793:5: ( inclusiveOrExpression ( LOGICAL_AND ^ inclusiveOrExpression )* )
                # Java.g:793:9: inclusiveOrExpression ( LOGICAL_AND ^ inclusiveOrExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_inclusiveOrExpression_in_logicalAndExpression10845)
                inclusiveOrExpression390 = self.inclusiveOrExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, inclusiveOrExpression390.tree)


                # Java.g:793:31: ( LOGICAL_AND ^ inclusiveOrExpression )*
                while True: #loop111
                    alt111 = 2
                    LA111_0 = self.input.LA(1)

                    if (LA111_0 == LOGICAL_AND) :
                        alt111 = 1


                    if alt111 == 1:
                        # Java.g:793:32: LOGICAL_AND ^ inclusiveOrExpression
                        pass 
                        LOGICAL_AND391 = self.match(self.input, LOGICAL_AND, self.FOLLOW_LOGICAL_AND_in_logicalAndExpression10848)
                        if self._state.backtracking == 0:
                            LOGICAL_AND391_tree = self._adaptor.createWithPayload(LOGICAL_AND391)
                            root_0 = self._adaptor.becomeRoot(LOGICAL_AND391_tree, root_0)



                        self._state.following.append(self.FOLLOW_inclusiveOrExpression_in_logicalAndExpression10851)
                        inclusiveOrExpression392 = self.inclusiveOrExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, inclusiveOrExpression392.tree)



                    else:
                        break #loop111




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 92, logicalAndExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "logicalAndExpression"


    class inclusiveOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.inclusiveOrExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "inclusiveOrExpression"
    # Java.g:796:1: inclusiveOrExpression : exclusiveOrExpression ( OR ^ exclusiveOrExpression )* ;
    def inclusiveOrExpression(self, ):
        retval = self.inclusiveOrExpression_return()
        retval.start = self.input.LT(1)

        inclusiveOrExpression_StartIndex = self.input.index()

        root_0 = None

        OR394 = None
        exclusiveOrExpression393 = None

        exclusiveOrExpression395 = None


        OR394_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 93):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:797:5: ( exclusiveOrExpression ( OR ^ exclusiveOrExpression )* )
                # Java.g:797:9: exclusiveOrExpression ( OR ^ exclusiveOrExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10872)
                exclusiveOrExpression393 = self.exclusiveOrExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, exclusiveOrExpression393.tree)


                # Java.g:797:31: ( OR ^ exclusiveOrExpression )*
                while True: #loop112
                    alt112 = 2
                    LA112_0 = self.input.LA(1)

                    if (LA112_0 == OR) :
                        alt112 = 1


                    if alt112 == 1:
                        # Java.g:797:32: OR ^ exclusiveOrExpression
                        pass 
                        OR394 = self.match(self.input, OR, self.FOLLOW_OR_in_inclusiveOrExpression10875)
                        if self._state.backtracking == 0:
                            OR394_tree = self._adaptor.createWithPayload(OR394)
                            root_0 = self._adaptor.becomeRoot(OR394_tree, root_0)



                        self._state.following.append(self.FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10878)
                        exclusiveOrExpression395 = self.exclusiveOrExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, exclusiveOrExpression395.tree)



                    else:
                        break #loop112




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 93, inclusiveOrExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "inclusiveOrExpression"


    class exclusiveOrExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.exclusiveOrExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "exclusiveOrExpression"
    # Java.g:800:1: exclusiveOrExpression : andExpression ( XOR ^ andExpression )* ;
    def exclusiveOrExpression(self, ):
        retval = self.exclusiveOrExpression_return()
        retval.start = self.input.LT(1)

        exclusiveOrExpression_StartIndex = self.input.index()

        root_0 = None

        XOR397 = None
        andExpression396 = None

        andExpression398 = None


        XOR397_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 94):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:801:5: ( andExpression ( XOR ^ andExpression )* )
                # Java.g:801:9: andExpression ( XOR ^ andExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_andExpression_in_exclusiveOrExpression10899)
                andExpression396 = self.andExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, andExpression396.tree)


                # Java.g:801:23: ( XOR ^ andExpression )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == XOR) :
                        alt113 = 1


                    if alt113 == 1:
                        # Java.g:801:24: XOR ^ andExpression
                        pass 
                        XOR397 = self.match(self.input, XOR, self.FOLLOW_XOR_in_exclusiveOrExpression10902)
                        if self._state.backtracking == 0:
                            XOR397_tree = self._adaptor.createWithPayload(XOR397)
                            root_0 = self._adaptor.becomeRoot(XOR397_tree, root_0)



                        self._state.following.append(self.FOLLOW_andExpression_in_exclusiveOrExpression10905)
                        andExpression398 = self.andExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, andExpression398.tree)



                    else:
                        break #loop113




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 94, exclusiveOrExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "exclusiveOrExpression"


    class andExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.andExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "andExpression"
    # Java.g:804:1: andExpression : equalityExpression ( AND ^ equalityExpression )* ;
    def andExpression(self, ):
        retval = self.andExpression_return()
        retval.start = self.input.LT(1)

        andExpression_StartIndex = self.input.index()

        root_0 = None

        AND400 = None
        equalityExpression399 = None

        equalityExpression401 = None


        AND400_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 95):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:805:5: ( equalityExpression ( AND ^ equalityExpression )* )
                # Java.g:805:9: equalityExpression ( AND ^ equalityExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_equalityExpression_in_andExpression10926)
                equalityExpression399 = self.equalityExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, equalityExpression399.tree)


                # Java.g:805:28: ( AND ^ equalityExpression )*
                while True: #loop114
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == AND) :
                        alt114 = 1


                    if alt114 == 1:
                        # Java.g:805:29: AND ^ equalityExpression
                        pass 
                        AND400 = self.match(self.input, AND, self.FOLLOW_AND_in_andExpression10929)
                        if self._state.backtracking == 0:
                            AND400_tree = self._adaptor.createWithPayload(AND400)
                            root_0 = self._adaptor.becomeRoot(AND400_tree, root_0)



                        self._state.following.append(self.FOLLOW_equalityExpression_in_andExpression10932)
                        equalityExpression401 = self.equalityExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, equalityExpression401.tree)



                    else:
                        break #loop114




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 95, andExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "andExpression"


    class equalityExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.equalityExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "equalityExpression"
    # Java.g:808:1: equalityExpression : instanceOfExpression ( ( EQUAL ^| NOT_EQUAL ^) instanceOfExpression )* ;
    def equalityExpression(self, ):
        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)

        equalityExpression_StartIndex = self.input.index()

        root_0 = None

        EQUAL403 = None
        NOT_EQUAL404 = None
        instanceOfExpression402 = None

        instanceOfExpression405 = None


        EQUAL403_tree = None
        NOT_EQUAL404_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 96):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:809:5: ( instanceOfExpression ( ( EQUAL ^| NOT_EQUAL ^) instanceOfExpression )* )
                # Java.g:809:9: instanceOfExpression ( ( EQUAL ^| NOT_EQUAL ^) instanceOfExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_instanceOfExpression_in_equalityExpression10953)
                instanceOfExpression402 = self.instanceOfExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, instanceOfExpression402.tree)


                # Java.g:810:9: ( ( EQUAL ^| NOT_EQUAL ^) instanceOfExpression )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == EQUAL or LA116_0 == NOT_EQUAL) :
                        alt116 = 1


                    if alt116 == 1:
                        # Java.g:810:13: ( EQUAL ^| NOT_EQUAL ^) instanceOfExpression
                        pass 
                        # Java.g:810:13: ( EQUAL ^| NOT_EQUAL ^)
                        alt115 = 2
                        LA115_0 = self.input.LA(1)

                        if (LA115_0 == EQUAL) :
                            alt115 = 1
                        elif (LA115_0 == NOT_EQUAL) :
                            alt115 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 115, 0, self.input)

                            raise nvae


                        if alt115 == 1:
                            # Java.g:810:17: EQUAL ^
                            pass 
                            EQUAL403 = self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_equalityExpression10972)
                            if self._state.backtracking == 0:
                                EQUAL403_tree = self._adaptor.createWithPayload(EQUAL403)
                                root_0 = self._adaptor.becomeRoot(EQUAL403_tree, root_0)




                        elif alt115 == 2:
                            # Java.g:811:17: NOT_EQUAL ^
                            pass 
                            NOT_EQUAL404 = self.match(self.input, NOT_EQUAL, self.FOLLOW_NOT_EQUAL_in_equalityExpression10991)
                            if self._state.backtracking == 0:
                                NOT_EQUAL404_tree = self._adaptor.createWithPayload(NOT_EQUAL404)
                                root_0 = self._adaptor.becomeRoot(NOT_EQUAL404_tree, root_0)






                        self._state.following.append(self.FOLLOW_instanceOfExpression_in_equalityExpression11021)
                        instanceOfExpression405 = self.instanceOfExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, instanceOfExpression405.tree)



                    else:
                        break #loop116




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 96, equalityExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "equalityExpression"


    class instanceOfExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.instanceOfExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "instanceOfExpression"
    # Java.g:817:1: instanceOfExpression : relationalExpression ( INSTANCEOF ^ type )? ;
    def instanceOfExpression(self, ):
        retval = self.instanceOfExpression_return()
        retval.start = self.input.LT(1)

        instanceOfExpression_StartIndex = self.input.index()

        root_0 = None

        INSTANCEOF407 = None
        relationalExpression406 = None

        type408 = None


        INSTANCEOF407_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 97):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:818:5: ( relationalExpression ( INSTANCEOF ^ type )? )
                # Java.g:818:9: relationalExpression ( INSTANCEOF ^ type )?
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_relationalExpression_in_instanceOfExpression11051)
                relationalExpression406 = self.relationalExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, relationalExpression406.tree)


                # Java.g:818:30: ( INSTANCEOF ^ type )?
                alt117 = 2
                LA117_0 = self.input.LA(1)

                if (LA117_0 == INSTANCEOF) :
                    alt117 = 1
                if alt117 == 1:
                    # Java.g:818:31: INSTANCEOF ^ type
                    pass 
                    INSTANCEOF407 = self.match(self.input, INSTANCEOF, self.FOLLOW_INSTANCEOF_in_instanceOfExpression11054)
                    if self._state.backtracking == 0:
                        INSTANCEOF407_tree = self._adaptor.createWithPayload(INSTANCEOF407)
                        root_0 = self._adaptor.becomeRoot(INSTANCEOF407_tree, root_0)



                    self._state.following.append(self.FOLLOW_type_in_instanceOfExpression11057)
                    type408 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type408.tree)







                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 97, instanceOfExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "instanceOfExpression"


    class relationalExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.relationalExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "relationalExpression"
    # Java.g:821:1: relationalExpression : shiftExpression ( ( LESS_OR_EQUAL ^| GREATER_OR_EQUAL ^| LESS_THAN ^| GREATER_THAN ^) shiftExpression )* ;
    def relationalExpression(self, ):
        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)

        relationalExpression_StartIndex = self.input.index()

        root_0 = None

        LESS_OR_EQUAL410 = None
        GREATER_OR_EQUAL411 = None
        LESS_THAN412 = None
        GREATER_THAN413 = None
        shiftExpression409 = None

        shiftExpression414 = None


        LESS_OR_EQUAL410_tree = None
        GREATER_OR_EQUAL411_tree = None
        LESS_THAN412_tree = None
        GREATER_THAN413_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 98):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:822:5: ( shiftExpression ( ( LESS_OR_EQUAL ^| GREATER_OR_EQUAL ^| LESS_THAN ^| GREATER_THAN ^) shiftExpression )* )
                # Java.g:822:9: shiftExpression ( ( LESS_OR_EQUAL ^| GREATER_OR_EQUAL ^| LESS_THAN ^| GREATER_THAN ^) shiftExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_shiftExpression_in_relationalExpression11078)
                shiftExpression409 = self.shiftExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, shiftExpression409.tree)


                # Java.g:823:9: ( ( LESS_OR_EQUAL ^| GREATER_OR_EQUAL ^| LESS_THAN ^| GREATER_THAN ^) shiftExpression )*
                while True: #loop119
                    alt119 = 2
                    LA119_0 = self.input.LA(1)

                    if ((GREATER_OR_EQUAL <= LA119_0 <= GREATER_THAN) or (LESS_OR_EQUAL <= LA119_0 <= LESS_THAN)) :
                        alt119 = 1


                    if alt119 == 1:
                        # Java.g:823:13: ( LESS_OR_EQUAL ^| GREATER_OR_EQUAL ^| LESS_THAN ^| GREATER_THAN ^) shiftExpression
                        pass 
                        # Java.g:823:13: ( LESS_OR_EQUAL ^| GREATER_OR_EQUAL ^| LESS_THAN ^| GREATER_THAN ^)
                        alt118 = 4
                        LA118 = self.input.LA(1)
                        if LA118 == LESS_OR_EQUAL:
                            alt118 = 1
                        elif LA118 == GREATER_OR_EQUAL:
                            alt118 = 2
                        elif LA118 == LESS_THAN:
                            alt118 = 3
                        elif LA118 == GREATER_THAN:
                            alt118 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 118, 0, self.input)

                            raise nvae


                        if alt118 == 1:
                            # Java.g:823:17: LESS_OR_EQUAL ^
                            pass 
                            LESS_OR_EQUAL410 = self.match(self.input, LESS_OR_EQUAL, self.FOLLOW_LESS_OR_EQUAL_in_relationalExpression11097)
                            if self._state.backtracking == 0:
                                LESS_OR_EQUAL410_tree = self._adaptor.createWithPayload(LESS_OR_EQUAL410)
                                root_0 = self._adaptor.becomeRoot(LESS_OR_EQUAL410_tree, root_0)




                        elif alt118 == 2:
                            # Java.g:824:17: GREATER_OR_EQUAL ^
                            pass 
                            GREATER_OR_EQUAL411 = self.match(self.input, GREATER_OR_EQUAL, self.FOLLOW_GREATER_OR_EQUAL_in_relationalExpression11116)
                            if self._state.backtracking == 0:
                                GREATER_OR_EQUAL411_tree = self._adaptor.createWithPayload(GREATER_OR_EQUAL411)
                                root_0 = self._adaptor.becomeRoot(GREATER_OR_EQUAL411_tree, root_0)




                        elif alt118 == 3:
                            # Java.g:825:17: LESS_THAN ^
                            pass 
                            LESS_THAN412 = self.match(self.input, LESS_THAN, self.FOLLOW_LESS_THAN_in_relationalExpression11135)
                            if self._state.backtracking == 0:
                                LESS_THAN412_tree = self._adaptor.createWithPayload(LESS_THAN412)
                                root_0 = self._adaptor.becomeRoot(LESS_THAN412_tree, root_0)




                        elif alt118 == 4:
                            # Java.g:826:17: GREATER_THAN ^
                            pass 
                            GREATER_THAN413 = self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_relationalExpression11154)
                            if self._state.backtracking == 0:
                                GREATER_THAN413_tree = self._adaptor.createWithPayload(GREATER_THAN413)
                                root_0 = self._adaptor.becomeRoot(GREATER_THAN413_tree, root_0)






                        self._state.following.append(self.FOLLOW_shiftExpression_in_relationalExpression11183)
                        shiftExpression414 = self.shiftExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, shiftExpression414.tree)



                    else:
                        break #loop119




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 98, relationalExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "relationalExpression"


    class shiftExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.shiftExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "shiftExpression"
    # Java.g:832:1: shiftExpression : additiveExpression ( ( BIT_SHIFT_RIGHT ^| SHIFT_RIGHT ^| SHIFT_LEFT ^) additiveExpression )* ;
    def shiftExpression(self, ):
        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)

        shiftExpression_StartIndex = self.input.index()

        root_0 = None

        BIT_SHIFT_RIGHT416 = None
        SHIFT_RIGHT417 = None
        SHIFT_LEFT418 = None
        additiveExpression415 = None

        additiveExpression419 = None


        BIT_SHIFT_RIGHT416_tree = None
        SHIFT_RIGHT417_tree = None
        SHIFT_LEFT418_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 99):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:833:5: ( additiveExpression ( ( BIT_SHIFT_RIGHT ^| SHIFT_RIGHT ^| SHIFT_LEFT ^) additiveExpression )* )
                # Java.g:833:9: additiveExpression ( ( BIT_SHIFT_RIGHT ^| SHIFT_RIGHT ^| SHIFT_LEFT ^) additiveExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_additiveExpression_in_shiftExpression11217)
                additiveExpression415 = self.additiveExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, additiveExpression415.tree)


                # Java.g:834:9: ( ( BIT_SHIFT_RIGHT ^| SHIFT_RIGHT ^| SHIFT_LEFT ^) additiveExpression )*
                while True: #loop121
                    alt121 = 2
                    LA121_0 = self.input.LA(1)

                    if (LA121_0 == BIT_SHIFT_RIGHT or LA121_0 == SHIFT_LEFT or LA121_0 == SHIFT_RIGHT) :
                        alt121 = 1


                    if alt121 == 1:
                        # Java.g:834:13: ( BIT_SHIFT_RIGHT ^| SHIFT_RIGHT ^| SHIFT_LEFT ^) additiveExpression
                        pass 
                        # Java.g:834:13: ( BIT_SHIFT_RIGHT ^| SHIFT_RIGHT ^| SHIFT_LEFT ^)
                        alt120 = 3
                        LA120 = self.input.LA(1)
                        if LA120 == BIT_SHIFT_RIGHT:
                            alt120 = 1
                        elif LA120 == SHIFT_RIGHT:
                            alt120 = 2
                        elif LA120 == SHIFT_LEFT:
                            alt120 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 120, 0, self.input)

                            raise nvae


                        if alt120 == 1:
                            # Java.g:834:17: BIT_SHIFT_RIGHT ^
                            pass 
                            BIT_SHIFT_RIGHT416 = self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_shiftExpression11235)
                            if self._state.backtracking == 0:
                                BIT_SHIFT_RIGHT416_tree = self._adaptor.createWithPayload(BIT_SHIFT_RIGHT416)
                                root_0 = self._adaptor.becomeRoot(BIT_SHIFT_RIGHT416_tree, root_0)




                        elif alt120 == 2:
                            # Java.g:835:17: SHIFT_RIGHT ^
                            pass 
                            SHIFT_RIGHT417 = self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_shiftExpression11254)
                            if self._state.backtracking == 0:
                                SHIFT_RIGHT417_tree = self._adaptor.createWithPayload(SHIFT_RIGHT417)
                                root_0 = self._adaptor.becomeRoot(SHIFT_RIGHT417_tree, root_0)




                        elif alt120 == 3:
                            # Java.g:836:17: SHIFT_LEFT ^
                            pass 
                            SHIFT_LEFT418 = self.match(self.input, SHIFT_LEFT, self.FOLLOW_SHIFT_LEFT_in_shiftExpression11273)
                            if self._state.backtracking == 0:
                                SHIFT_LEFT418_tree = self._adaptor.createWithPayload(SHIFT_LEFT418)
                                root_0 = self._adaptor.becomeRoot(SHIFT_LEFT418_tree, root_0)






                        self._state.following.append(self.FOLLOW_additiveExpression_in_shiftExpression11302)
                        additiveExpression419 = self.additiveExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, additiveExpression419.tree)



                    else:
                        break #loop121




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 99, shiftExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "shiftExpression"


    class additiveExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.additiveExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "additiveExpression"
    # Java.g:842:1: additiveExpression : multiplicativeExpression ( ( PLUS ^| MINUS ^) multiplicativeExpression )* ;
    def additiveExpression(self, ):
        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)

        additiveExpression_StartIndex = self.input.index()

        root_0 = None

        PLUS421 = None
        MINUS422 = None
        multiplicativeExpression420 = None

        multiplicativeExpression423 = None


        PLUS421_tree = None
        MINUS422_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 100):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:843:5: ( multiplicativeExpression ( ( PLUS ^| MINUS ^) multiplicativeExpression )* )
                # Java.g:843:9: multiplicativeExpression ( ( PLUS ^| MINUS ^) multiplicativeExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression11332)
                multiplicativeExpression420 = self.multiplicativeExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, multiplicativeExpression420.tree)


                # Java.g:844:9: ( ( PLUS ^| MINUS ^) multiplicativeExpression )*
                while True: #loop123
                    alt123 = 2
                    LA123_0 = self.input.LA(1)

                    if (LA123_0 == MINUS or LA123_0 == PLUS) :
                        alt123 = 1


                    if alt123 == 1:
                        # Java.g:844:13: ( PLUS ^| MINUS ^) multiplicativeExpression
                        pass 
                        # Java.g:844:13: ( PLUS ^| MINUS ^)
                        alt122 = 2
                        LA122_0 = self.input.LA(1)

                        if (LA122_0 == PLUS) :
                            alt122 = 1
                        elif (LA122_0 == MINUS) :
                            alt122 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 122, 0, self.input)

                            raise nvae


                        if alt122 == 1:
                            # Java.g:844:17: PLUS ^
                            pass 
                            PLUS421 = self.match(self.input, PLUS, self.FOLLOW_PLUS_in_additiveExpression11350)
                            if self._state.backtracking == 0:
                                PLUS421_tree = self._adaptor.createWithPayload(PLUS421)
                                root_0 = self._adaptor.becomeRoot(PLUS421_tree, root_0)




                        elif alt122 == 2:
                            # Java.g:845:17: MINUS ^
                            pass 
                            MINUS422 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_additiveExpression11369)
                            if self._state.backtracking == 0:
                                MINUS422_tree = self._adaptor.createWithPayload(MINUS422)
                                root_0 = self._adaptor.becomeRoot(MINUS422_tree, root_0)






                        self._state.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression11398)
                        multiplicativeExpression423 = self.multiplicativeExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, multiplicativeExpression423.tree)



                    else:
                        break #loop123




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 100, additiveExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "additiveExpression"


    class multiplicativeExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.multiplicativeExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "multiplicativeExpression"
    # Java.g:851:1: multiplicativeExpression : unaryExpression ( ( STAR ^| DIV ^| MOD ^) unaryExpression )* ;
    def multiplicativeExpression(self, ):
        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)

        multiplicativeExpression_StartIndex = self.input.index()

        root_0 = None

        STAR425 = None
        DIV426 = None
        MOD427 = None
        unaryExpression424 = None

        unaryExpression428 = None


        STAR425_tree = None
        DIV426_tree = None
        MOD427_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 101):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:852:5: ( unaryExpression ( ( STAR ^| DIV ^| MOD ^) unaryExpression )* )
                # Java.g:852:9: unaryExpression ( ( STAR ^| DIV ^| MOD ^) unaryExpression )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression11428)
                unaryExpression424 = self.unaryExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, unaryExpression424.tree)


                # Java.g:853:9: ( ( STAR ^| DIV ^| MOD ^) unaryExpression )*
                while True: #loop125
                    alt125 = 2
                    LA125_0 = self.input.LA(1)

                    if (LA125_0 == DIV or LA125_0 == MOD or LA125_0 == STAR) :
                        alt125 = 1


                    if alt125 == 1:
                        # Java.g:853:13: ( STAR ^| DIV ^| MOD ^) unaryExpression
                        pass 
                        # Java.g:853:13: ( STAR ^| DIV ^| MOD ^)
                        alt124 = 3
                        LA124 = self.input.LA(1)
                        if LA124 == STAR:
                            alt124 = 1
                        elif LA124 == DIV:
                            alt124 = 2
                        elif LA124 == MOD:
                            alt124 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 124, 0, self.input)

                            raise nvae


                        if alt124 == 1:
                            # Java.g:853:17: STAR ^
                            pass 
                            STAR425 = self.match(self.input, STAR, self.FOLLOW_STAR_in_multiplicativeExpression11447)
                            if self._state.backtracking == 0:
                                STAR425_tree = self._adaptor.createWithPayload(STAR425)
                                root_0 = self._adaptor.becomeRoot(STAR425_tree, root_0)




                        elif alt124 == 2:
                            # Java.g:854:17: DIV ^
                            pass 
                            DIV426 = self.match(self.input, DIV, self.FOLLOW_DIV_in_multiplicativeExpression11466)
                            if self._state.backtracking == 0:
                                DIV426_tree = self._adaptor.createWithPayload(DIV426)
                                root_0 = self._adaptor.becomeRoot(DIV426_tree, root_0)




                        elif alt124 == 3:
                            # Java.g:855:17: MOD ^
                            pass 
                            MOD427 = self.match(self.input, MOD, self.FOLLOW_MOD_in_multiplicativeExpression11485)
                            if self._state.backtracking == 0:
                                MOD427_tree = self._adaptor.createWithPayload(MOD427)
                                root_0 = self._adaptor.becomeRoot(MOD427_tree, root_0)






                        self._state.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression11514)
                        unaryExpression428 = self.unaryExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unaryExpression428.tree)



                    else:
                        break #loop125




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 101, multiplicativeExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "multiplicativeExpression"


    class unaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.unaryExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "unaryExpression"
    # Java.g:861:1: unaryExpression : ( PLUS unaryExpression -> ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression ) | MINUS unaryExpression -> ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression ) | INC postfixedExpression -> ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression ) | DEC postfixedExpression -> ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression ) | unaryExpressionNotPlusMinus );
    def unaryExpression(self, ):
        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)

        unaryExpression_StartIndex = self.input.index()

        root_0 = None

        PLUS429 = None
        MINUS431 = None
        INC433 = None
        DEC435 = None
        unaryExpression430 = None

        unaryExpression432 = None

        postfixedExpression434 = None

        postfixedExpression436 = None

        unaryExpressionNotPlusMinus437 = None


        PLUS429_tree = None
        MINUS431_tree = None
        INC433_tree = None
        DEC435_tree = None
        stream_DEC = RewriteRuleTokenStream(self._adaptor, "token DEC")
        stream_INC = RewriteRuleTokenStream(self._adaptor, "token INC")
        stream_PLUS = RewriteRuleTokenStream(self._adaptor, "token PLUS")
        stream_MINUS = RewriteRuleTokenStream(self._adaptor, "token MINUS")
        stream_postfixedExpression = RewriteRuleSubtreeStream(self._adaptor, "rule postfixedExpression")
        stream_unaryExpression = RewriteRuleSubtreeStream(self._adaptor, "rule unaryExpression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 102):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:862:5: ( PLUS unaryExpression -> ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression ) | MINUS unaryExpression -> ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression ) | INC postfixedExpression -> ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression ) | DEC postfixedExpression -> ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression ) | unaryExpressionNotPlusMinus )
                alt126 = 5
                LA126 = self.input.LA(1)
                if LA126 == PLUS:
                    alt126 = 1
                elif LA126 == MINUS:
                    alt126 = 2
                elif LA126 == INC:
                    alt126 = 3
                elif LA126 == DEC:
                    alt126 = 4
                elif LA126 == BOOLEAN or LA126 == BYTE or LA126 == CHAR or LA126 == CHARACTER_LITERAL or LA126 == DECIMAL_LITERAL or LA126 == DOUBLE or LA126 == FALSE or LA126 == FLOAT or LA126 == FLOATING_POINT_LITERAL or LA126 == HEX_LITERAL or LA126 == IDENT or LA126 == INT or LA126 == LESS_THAN or LA126 == LOGICAL_NOT or LA126 == LONG or LA126 == LPAREN or LA126 == NEW or LA126 == NOT or LA126 == NULL or LA126 == OCTAL_LITERAL or LA126 == SHORT or LA126 == STRING_LITERAL or LA126 == SUPER or LA126 == THIS or LA126 == TRUE or LA126 == VOID:
                    alt126 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 126, 0, self.input)

                    raise nvae


                if alt126 == 1:
                    # Java.g:862:9: PLUS unaryExpression
                    pass 
                    PLUS429 = self.match(self.input, PLUS, self.FOLLOW_PLUS_in_unaryExpression11548) 
                    if self._state.backtracking == 0:
                        stream_PLUS.add(PLUS429)


                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpression11550)
                    unaryExpression430 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression430.tree)


                    # AST Rewrite
                    # elements: unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 862:37: -> ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression )
                        # Java.g:862:41: ^( UNARY_PLUS[$PLUS, \"UNARY_PLUS\"] unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(UNARY_PLUS, PLUS429, "UNARY_PLUS")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt126 == 2:
                    # Java.g:863:9: MINUS unaryExpression
                    pass 
                    MINUS431 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_unaryExpression11577) 
                    if self._state.backtracking == 0:
                        stream_MINUS.add(MINUS431)


                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpression11579)
                    unaryExpression432 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression432.tree)


                    # AST Rewrite
                    # elements: unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 863:37: -> ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression )
                        # Java.g:863:41: ^( UNARY_MINUS[$MINUS, \"UNARY_MINUS\"] unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(UNARY_MINUS, MINUS431, "UNARY_MINUS")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt126 == 3:
                    # Java.g:864:9: INC postfixedExpression
                    pass 
                    INC433 = self.match(self.input, INC, self.FOLLOW_INC_in_unaryExpression11605) 
                    if self._state.backtracking == 0:
                        stream_INC.add(INC433)


                    self._state.following.append(self.FOLLOW_postfixedExpression_in_unaryExpression11607)
                    postfixedExpression434 = self.postfixedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_postfixedExpression.add(postfixedExpression434.tree)


                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 864:37: -> ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression )
                        # Java.g:864:41: ^( PRE_INC[$INC, \"PRE_INC\"] postfixedExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(PRE_INC, INC433, "PRE_INC")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_postfixedExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt126 == 4:
                    # Java.g:865:9: DEC postfixedExpression
                    pass 
                    DEC435 = self.match(self.input, DEC, self.FOLLOW_DEC_in_unaryExpression11631) 
                    if self._state.backtracking == 0:
                        stream_DEC.add(DEC435)


                    self._state.following.append(self.FOLLOW_postfixedExpression_in_unaryExpression11633)
                    postfixedExpression436 = self.postfixedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_postfixedExpression.add(postfixedExpression436.tree)


                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 865:37: -> ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression )
                        # Java.g:865:41: ^( PRE_DEC[$DEC, \"PRE_DEC\"] postfixedExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(PRE_DEC, DEC435, "PRE_DEC")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_postfixedExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt126 == 5:
                    # Java.g:866:9: unaryExpressionNotPlusMinus
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_unaryExpressionNotPlusMinus_in_unaryExpression11657)
                    unaryExpressionNotPlusMinus437 = self.unaryExpressionNotPlusMinus()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unaryExpressionNotPlusMinus437.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 102, unaryExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "unaryExpression"


    class unaryExpressionNotPlusMinus_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.unaryExpressionNotPlusMinus_return, self).__init__()

            self.tree = None





    # $ANTLR start "unaryExpressionNotPlusMinus"
    # Java.g:869:1: unaryExpressionNotPlusMinus : ( NOT unaryExpression -> ^( NOT unaryExpression ) | LOGICAL_NOT unaryExpression -> ^( LOGICAL_NOT unaryExpression ) | LPAREN type RPAREN unaryExpression -> ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression ) | postfixedExpression );
    def unaryExpressionNotPlusMinus(self, ):
        retval = self.unaryExpressionNotPlusMinus_return()
        retval.start = self.input.LT(1)

        unaryExpressionNotPlusMinus_StartIndex = self.input.index()

        root_0 = None

        NOT438 = None
        LOGICAL_NOT440 = None
        LPAREN442 = None
        RPAREN444 = None
        unaryExpression439 = None

        unaryExpression441 = None

        type443 = None

        unaryExpression445 = None

        postfixedExpression446 = None


        NOT438_tree = None
        LOGICAL_NOT440_tree = None
        LPAREN442_tree = None
        RPAREN444_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LOGICAL_NOT = RewriteRuleTokenStream(self._adaptor, "token LOGICAL_NOT")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_unaryExpression = RewriteRuleSubtreeStream(self._adaptor, "rule unaryExpression")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 103):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:870:5: ( NOT unaryExpression -> ^( NOT unaryExpression ) | LOGICAL_NOT unaryExpression -> ^( LOGICAL_NOT unaryExpression ) | LPAREN type RPAREN unaryExpression -> ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression ) | postfixedExpression )
                alt127 = 4
                LA127 = self.input.LA(1)
                if LA127 == NOT:
                    alt127 = 1
                elif LA127 == LOGICAL_NOT:
                    alt127 = 2
                elif LA127 == LPAREN:
                    LA127_3 = self.input.LA(2)

                    if (self.synpred190_Java()) :
                        alt127 = 3
                    elif (True) :
                        alt127 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 127, 3, self.input)

                        raise nvae


                elif LA127 == BOOLEAN or LA127 == BYTE or LA127 == CHAR or LA127 == CHARACTER_LITERAL or LA127 == DECIMAL_LITERAL or LA127 == DOUBLE or LA127 == FALSE or LA127 == FLOAT or LA127 == FLOATING_POINT_LITERAL or LA127 == HEX_LITERAL or LA127 == IDENT or LA127 == INT or LA127 == LESS_THAN or LA127 == LONG or LA127 == NEW or LA127 == NULL or LA127 == OCTAL_LITERAL or LA127 == SHORT or LA127 == STRING_LITERAL or LA127 == SUPER or LA127 == THIS or LA127 == TRUE or LA127 == VOID:
                    alt127 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 127, 0, self.input)

                    raise nvae


                if alt127 == 1:
                    # Java.g:870:9: NOT unaryExpression
                    pass 
                    NOT438 = self.match(self.input, NOT, self.FOLLOW_NOT_in_unaryExpressionNotPlusMinus11676) 
                    if self._state.backtracking == 0:
                        stream_NOT.add(NOT438)


                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11678)
                    unaryExpression439 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression439.tree)


                    # AST Rewrite
                    # elements: NOT, unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 870:57: -> ^( NOT unaryExpression )
                        # Java.g:870:61: ^( NOT unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_NOT.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt127 == 2:
                    # Java.g:871:9: LOGICAL_NOT unaryExpression
                    pass 
                    LOGICAL_NOT440 = self.match(self.input, LOGICAL_NOT, self.FOLLOW_LOGICAL_NOT_in_unaryExpressionNotPlusMinus11725) 
                    if self._state.backtracking == 0:
                        stream_LOGICAL_NOT.add(LOGICAL_NOT440)


                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11727)
                    unaryExpression441 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression441.tree)


                    # AST Rewrite
                    # elements: unaryExpression, LOGICAL_NOT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 871:57: -> ^( LOGICAL_NOT unaryExpression )
                        # Java.g:871:61: ^( LOGICAL_NOT unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_LOGICAL_NOT.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt127 == 3:
                    # Java.g:872:9: LPAREN type RPAREN unaryExpression
                    pass 
                    LPAREN442 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_unaryExpressionNotPlusMinus11766) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN442)


                    self._state.following.append(self.FOLLOW_type_in_unaryExpressionNotPlusMinus11768)
                    type443 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type443.tree)


                    RPAREN444 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_unaryExpressionNotPlusMinus11770) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN444)


                    self._state.following.append(self.FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11772)
                    unaryExpression445 = self.unaryExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unaryExpression.add(unaryExpression445.tree)


                    # AST Rewrite
                    # elements: type, unaryExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 872:57: -> ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression )
                        # Java.g:872:61: ^( CAST_EXPR[$LPAREN, \"CAST_EXPR\"] type unaryExpression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(CAST_EXPR, LPAREN442, "CAST_EXPR")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_type.nextTree())

                        self._adaptor.addChild(root_1, stream_unaryExpression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt127 == 4:
                    # Java.g:873:9: postfixedExpression
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_postfixedExpression_in_unaryExpressionNotPlusMinus11807)
                    postfixedExpression446 = self.postfixedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, postfixedExpression446.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 103, unaryExpressionNotPlusMinus_StartIndex, success)


            pass
        return retval

    # $ANTLR end "unaryExpressionNotPlusMinus"


    class postfixedExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.postfixedExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "postfixedExpression"
    # Java.g:876:1: postfixedExpression : ( primaryExpression -> primaryExpression ) (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )* ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )? ;
    def postfixedExpression(self, ):
        retval = self.postfixedExpression_return()
        retval.start = self.input.LT(1)

        postfixedExpression_StartIndex = self.input.index()

        root_0 = None

        outerDot = None
        Super = None
        innerDot = None
        IDENT449 = None
        THIS451 = None
        SUPER453 = None
        IDENT454 = None
        LBRACK457 = None
        RBRACK459 = None
        INC460 = None
        DEC461 = None
        primaryExpression447 = None

        genericTypeArgumentListSimplified448 = None

        arguments450 = None

        arguments452 = None

        arguments455 = None

        innerNewExpression456 = None

        expression458 = None


        outerDot_tree = None
        Super_tree = None
        innerDot_tree = None
        IDENT449_tree = None
        THIS451_tree = None
        SUPER453_tree = None
        IDENT454_tree = None
        LBRACK457_tree = None
        RBRACK459_tree = None
        INC460_tree = None
        DEC461_tree = None
        stream_RBRACK = RewriteRuleTokenStream(self._adaptor, "token RBRACK")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_INC = RewriteRuleTokenStream(self._adaptor, "token INC")
        stream_DEC = RewriteRuleTokenStream(self._adaptor, "token DEC")
        stream_LBRACK = RewriteRuleTokenStream(self._adaptor, "token LBRACK")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_primaryExpression = RewriteRuleSubtreeStream(self._adaptor, "rule primaryExpression")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        stream_innerNewExpression = RewriteRuleSubtreeStream(self._adaptor, "rule innerNewExpression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 104):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:878:5: ( ( primaryExpression -> primaryExpression ) (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )* ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )? )
                # Java.g:878:9: ( primaryExpression -> primaryExpression ) (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )* ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )?
                pass 
                # Java.g:878:9: ( primaryExpression -> primaryExpression )
                # Java.g:878:13: primaryExpression
                pass 
                self._state.following.append(self.FOLLOW_primaryExpression_in_postfixedExpression11843)
                primaryExpression447 = self.primaryExpression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_primaryExpression.add(primaryExpression447.tree)


                # AST Rewrite
                # elements: primaryExpression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 878:53: -> primaryExpression
                    self._adaptor.addChild(root_0, stream_primaryExpression.nextTree())




                    retval.tree = root_0






                # Java.g:881:9: (outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) ) | LBRACK expression RBRACK -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression ) )*
                while True: #loop132
                    alt132 = 3
                    LA132_0 = self.input.LA(1)

                    if (LA132_0 == DOT) :
                        alt132 = 1
                    elif (LA132_0 == LBRACK) :
                        alt132 = 2


                    if alt132 == 1:
                        # Java.g:881:13: outerDot= DOT ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) )
                        pass 
                        outerDot = self.match(self.input, DOT, self.FOLLOW_DOT_in_postfixedExpression11905) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(outerDot)


                        # Java.g:882:13: ( ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )? | THIS -> ^( DOT $postfixedExpression THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments ) | ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )? | innerNewExpression -> ^( DOT $postfixedExpression innerNewExpression ) )
                        alt131 = 5
                        LA131 = self.input.LA(1)
                        if LA131 == IDENT or LA131 == LESS_THAN:
                            alt131 = 1
                        elif LA131 == THIS:
                            alt131 = 2
                        elif LA131 == SUPER:
                            LA131_3 = self.input.LA(2)

                            if (LA131_3 == DOT) :
                                alt131 = 4
                            elif (LA131_3 == LPAREN) :
                                alt131 = 3
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 131, 3, self.input)

                                raise nvae


                        elif LA131 == NEW:
                            alt131 = 5
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 131, 0, self.input)

                            raise nvae


                        if alt131 == 1:
                            # Java.g:882:17: ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )?
                            pass 
                            # Java.g:882:17: ( ( genericTypeArgumentListSimplified )? IDENT -> ^( DOT $postfixedExpression IDENT ) )
                            # Java.g:882:21: ( genericTypeArgumentListSimplified )? IDENT
                            pass 
                            # Java.g:882:21: ( genericTypeArgumentListSimplified )?
                            alt128 = 2
                            LA128_0 = self.input.LA(1)

                            if (LA128_0 == LESS_THAN) :
                                alt128 = 1
                            if alt128 == 1:
                                # Java.g:882:21: genericTypeArgumentListSimplified
                                pass 
                                self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_postfixedExpression11955)
                                genericTypeArgumentListSimplified448 = self.genericTypeArgumentListSimplified()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified448.tree)





                            IDENT449 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_postfixedExpression12037) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT449)


                            # AST Rewrite
                            # elements: postfixedExpression, IDENT, DOT
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 884:53: -> ^( DOT $postfixedExpression IDENT )
                                # Java.g:884:57: ^( DOT $postfixedExpression IDENT )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                stream_DOT.nextNode()
                                , root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_1, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0






                            # Java.g:886:17: ( arguments -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments ) )?
                            alt129 = 2
                            LA129_0 = self.input.LA(1)

                            if (LA129_0 == LPAREN) :
                                alt129 = 1
                            if alt129 == 1:
                                # Java.g:886:21: arguments
                                pass 
                                self._state.following.append(self.FOLLOW_arguments_in_postfixedExpression12116)
                                arguments450 = self.arguments()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arguments.add(arguments450.tree)


                                # AST Rewrite
                                # elements: genericTypeArgumentListSimplified, postfixedExpression, arguments
                                # token labels: 
                                # rule labels: retval
                                # token list labels: 
                                # rule list labels: 
                                # wildcard labels: 
                                if self._state.backtracking == 0:
                                    retval.tree = root_0
                                    if retval is not None:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                    else:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                    root_0 = self._adaptor.nil()
                                    # 886:53: -> ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments )
                                    # Java.g:886:57: ^( METHOD_CALL $postfixedExpression ( genericTypeArgumentListSimplified )? arguments )
                                    root_1 = self._adaptor.nil()
                                    root_1 = self._adaptor.becomeRoot(
                                    self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                                    , root_1)

                                    self._adaptor.addChild(root_1, stream_retval.nextTree())

                                    # Java.g:886:92: ( genericTypeArgumentListSimplified )?
                                    if stream_genericTypeArgumentListSimplified.hasNext():
                                        self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                                    stream_genericTypeArgumentListSimplified.reset();

                                    self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                    self._adaptor.addChild(root_0, root_1)




                                    retval.tree = root_0







                        elif alt131 == 2:
                            # Java.g:888:17: THIS
                            pass 
                            THIS451 = self.match(self.input, THIS, self.FOLLOW_THIS_in_postfixedExpression12190) 
                            if self._state.backtracking == 0:
                                stream_THIS.add(THIS451)


                            # AST Rewrite
                            # elements: DOT, THIS, postfixedExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 888:53: -> ^( DOT $postfixedExpression THIS )
                                # Java.g:888:57: ^( DOT $postfixedExpression THIS )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                stream_DOT.nextNode()
                                , root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_1, 
                                stream_THIS.nextNode()
                                )

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt131 == 3:
                            # Java.g:889:17: Super= SUPER arguments
                            pass 
                            Super = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_postfixedExpression12253) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(Super)


                            self._state.following.append(self.FOLLOW_arguments_in_postfixedExpression12255)
                            arguments452 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments452.tree)


                            # AST Rewrite
                            # elements: arguments, postfixedExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 889:57: -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments )
                                # Java.g:889:61: ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] $postfixedExpression arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.create(SUPER_CONSTRUCTOR_CALL, Super, "SUPER_CONSTRUCTOR_CALL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt131 == 4:
                            # Java.g:890:17: ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) ) ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )?
                            pass 
                            # Java.g:890:17: ( SUPER innerDot= DOT IDENT -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT ) )
                            # Java.g:890:21: SUPER innerDot= DOT IDENT
                            pass 
                            SUPER453 = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_postfixedExpression12308) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(SUPER453)


                            innerDot = self.match(self.input, DOT, self.FOLLOW_DOT_in_postfixedExpression12312) 
                            if self._state.backtracking == 0:
                                stream_DOT.add(innerDot)


                            IDENT454 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_postfixedExpression12314) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT454)


                            # AST Rewrite
                            # elements: outerDot, innerDot, IDENT, SUPER, postfixedExpression
                            # token labels: outerDot, innerDot
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                stream_outerDot = RewriteRuleTokenStream(self._adaptor, "token outerDot", outerDot)
                                stream_innerDot = RewriteRuleTokenStream(self._adaptor, "token innerDot", innerDot)
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 890:53: -> ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT )
                                # Java.g:890:57: ^( $innerDot ^( $outerDot $postfixedExpression SUPER ) IDENT )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_innerDot.nextNode(), root_1)

                                # Java.g:890:69: ^( $outerDot $postfixedExpression SUPER )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(stream_outerDot.nextNode(), root_2)

                                self._adaptor.addChild(root_2, stream_retval.nextTree())

                                self._adaptor.addChild(root_2, 
                                stream_SUPER.nextNode()
                                )

                                self._adaptor.addChild(root_1, root_2)

                                self._adaptor.addChild(root_1, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0






                            # Java.g:892:17: ( arguments -> ^( METHOD_CALL $postfixedExpression arguments ) )?
                            alt130 = 2
                            LA130_0 = self.input.LA(1)

                            if (LA130_0 == LPAREN) :
                                alt130 = 1
                            if alt130 == 1:
                                # Java.g:892:21: arguments
                                pass 
                                self._state.following.append(self.FOLLOW_arguments_in_postfixedExpression12381)
                                arguments455 = self.arguments()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    stream_arguments.add(arguments455.tree)


                                # AST Rewrite
                                # elements: arguments, postfixedExpression
                                # token labels: 
                                # rule labels: retval
                                # token list labels: 
                                # rule list labels: 
                                # wildcard labels: 
                                if self._state.backtracking == 0:
                                    retval.tree = root_0
                                    if retval is not None:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                    else:
                                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                    root_0 = self._adaptor.nil()
                                    # 892:53: -> ^( METHOD_CALL $postfixedExpression arguments )
                                    # Java.g:892:57: ^( METHOD_CALL $postfixedExpression arguments )
                                    root_1 = self._adaptor.nil()
                                    root_1 = self._adaptor.becomeRoot(
                                    self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                                    , root_1)

                                    self._adaptor.addChild(root_1, stream_retval.nextTree())

                                    self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                    self._adaptor.addChild(root_0, root_1)




                                    retval.tree = root_0







                        elif alt131 == 5:
                            # Java.g:894:17: innerNewExpression
                            pass 
                            self._state.following.append(self.FOLLOW_innerNewExpression_in_postfixedExpression12452)
                            innerNewExpression456 = self.innerNewExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_innerNewExpression.add(innerNewExpression456.tree)


                            # AST Rewrite
                            # elements: postfixedExpression, DOT, innerNewExpression
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 894:53: -> ^( DOT $postfixedExpression innerNewExpression )
                                # Java.g:894:57: ^( DOT $postfixedExpression innerNewExpression )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                stream_DOT.nextNode()
                                , root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_1, stream_innerNewExpression.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0







                    elif alt132 == 2:
                        # Java.g:896:13: LBRACK expression RBRACK
                        pass 
                        LBRACK457 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_postfixedExpression12509) 
                        if self._state.backtracking == 0:
                            stream_LBRACK.add(LBRACK457)


                        self._state.following.append(self.FOLLOW_expression_in_postfixedExpression12511)
                        expression458 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression458.tree)


                        RBRACK459 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_postfixedExpression12513) 
                        if self._state.backtracking == 0:
                            stream_RBRACK.add(RBRACK459)


                        # AST Rewrite
                        # elements: postfixedExpression, expression
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 896:53: -> ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression )
                            # Java.g:896:57: ^( ARRAY_ELEMENT_ACCESS $postfixedExpression expression )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(ARRAY_ELEMENT_ACCESS, "ARRAY_ELEMENT_ACCESS")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_retval.nextTree())

                            self._adaptor.addChild(root_1, stream_expression.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    else:
                        break #loop132


                # Java.g:899:9: ( INC -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression) | DEC -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression) )?
                alt133 = 3
                LA133_0 = self.input.LA(1)

                if (LA133_0 == INC) :
                    alt133 = 1
                elif (LA133_0 == DEC) :
                    alt133 = 2
                if alt133 == 1:
                    # Java.g:899:13: INC
                    pass 
                    INC460 = self.match(self.input, INC, self.FOLLOW_INC_in_postfixedExpression12574) 
                    if self._state.backtracking == 0:
                        stream_INC.add(INC460)


                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 899:17: -> ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression)
                        # Java.g:899:20: ^( POST_INC[$INC, \"POST_INC\"] $postfixedExpression)
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(POST_INC, INC460, "POST_INC")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt133 == 2:
                    # Java.g:900:13: DEC
                    pass 
                    DEC461 = self.match(self.input, DEC, self.FOLLOW_DEC_in_postfixedExpression12598) 
                    if self._state.backtracking == 0:
                        stream_DEC.add(DEC461)


                    # AST Rewrite
                    # elements: postfixedExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 900:17: -> ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression)
                        # Java.g:900:20: ^( POST_DEC[$DEC, \"POST_DEC\"] $postfixedExpression)
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(POST_DEC, DEC461, "POST_DEC")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0








                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 104, postfixedExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "postfixedExpression"


    class primaryExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.primaryExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "primaryExpression"
    # Java.g:904:1: primaryExpression : ( parenthesizedExpression | literal | newExpression | qualifiedIdentExpression | genericTypeArgumentListSimplified ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) ) | ( THIS -> THIS ) ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )? | SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments ) | ( SUPER DOT IDENT ) ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) ) | ( primitiveType -> primitiveType ) ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )* DOT CLASS -> ^( DOT $primaryExpression CLASS ) | VOID DOT CLASS -> ^( DOT VOID CLASS ) );
    def primaryExpression(self, ):
        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)

        primaryExpression_StartIndex = self.input.index()

        root_0 = None

        SUPER467 = None
        DOT469 = None
        IDENT470 = None
        IDENT472 = None
        THIS474 = None
        THIS476 = None
        SUPER478 = None
        SUPER480 = None
        DOT481 = None
        IDENT482 = None
        DOT486 = None
        CLASS487 = None
        VOID488 = None
        DOT489 = None
        CLASS490 = None
        parenthesizedExpression462 = None

        literal463 = None

        newExpression464 = None

        qualifiedIdentExpression465 = None

        genericTypeArgumentListSimplified466 = None

        arguments468 = None

        arguments471 = None

        arguments473 = None

        arguments475 = None

        arguments477 = None

        arguments479 = None

        arguments483 = None

        primitiveType484 = None

        arrayDeclarator485 = None


        SUPER467_tree = None
        DOT469_tree = None
        IDENT470_tree = None
        IDENT472_tree = None
        THIS474_tree = None
        THIS476_tree = None
        SUPER478_tree = None
        SUPER480_tree = None
        DOT481_tree = None
        IDENT482_tree = None
        DOT486_tree = None
        CLASS487_tree = None
        VOID488_tree = None
        DOT489_tree = None
        CLASS490_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_arrayDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclarator")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_primitiveType = RewriteRuleSubtreeStream(self._adaptor, "rule primitiveType")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 105):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:905:5: ( parenthesizedExpression | literal | newExpression | qualifiedIdentExpression | genericTypeArgumentListSimplified ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) ) | ( THIS -> THIS ) ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )? | SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments ) | ( SUPER DOT IDENT ) ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) ) | ( primitiveType -> primitiveType ) ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )* DOT CLASS -> ^( DOT $primaryExpression CLASS ) | VOID DOT CLASS -> ^( DOT VOID CLASS ) )
                alt139 = 10
                LA139 = self.input.LA(1)
                if LA139 == LPAREN:
                    alt139 = 1
                elif LA139 == CHARACTER_LITERAL or LA139 == DECIMAL_LITERAL or LA139 == FALSE or LA139 == FLOATING_POINT_LITERAL or LA139 == HEX_LITERAL or LA139 == NULL or LA139 == OCTAL_LITERAL or LA139 == STRING_LITERAL or LA139 == TRUE:
                    alt139 = 2
                elif LA139 == NEW:
                    alt139 = 3
                elif LA139 == IDENT:
                    alt139 = 4
                elif LA139 == LESS_THAN:
                    alt139 = 5
                elif LA139 == THIS:
                    alt139 = 6
                elif LA139 == SUPER:
                    LA139_7 = self.input.LA(2)

                    if (LA139_7 == DOT) :
                        alt139 = 8
                    elif (LA139_7 == LPAREN) :
                        alt139 = 7
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 139, 7, self.input)

                        raise nvae


                elif LA139 == BOOLEAN or LA139 == BYTE or LA139 == CHAR or LA139 == DOUBLE or LA139 == FLOAT or LA139 == INT or LA139 == LONG or LA139 == SHORT:
                    alt139 = 9
                elif LA139 == VOID:
                    alt139 = 10
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 139, 0, self.input)

                    raise nvae


                if alt139 == 1:
                    # Java.g:905:9: parenthesizedExpression
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_parenthesizedExpression_in_primaryExpression12646)
                    parenthesizedExpression462 = self.parenthesizedExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parenthesizedExpression462.tree)



                elif alt139 == 2:
                    # Java.g:906:9: literal
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_literal_in_primaryExpression12656)
                    literal463 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, literal463.tree)



                elif alt139 == 3:
                    # Java.g:907:9: newExpression
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_newExpression_in_primaryExpression12666)
                    newExpression464 = self.newExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, newExpression464.tree)



                elif alt139 == 4:
                    # Java.g:908:9: qualifiedIdentExpression
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_qualifiedIdentExpression_in_primaryExpression12676)
                    qualifiedIdentExpression465 = self.qualifiedIdentExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, qualifiedIdentExpression465.tree)



                elif alt139 == 5:
                    # Java.g:909:9: genericTypeArgumentListSimplified ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) )
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_primaryExpression12686)
                    genericTypeArgumentListSimplified466 = self.genericTypeArgumentListSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified466.tree)


                    # Java.g:910:9: ( SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) ) | IDENT arguments -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments ) | THIS arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) )
                    alt135 = 3
                    LA135 = self.input.LA(1)
                    if LA135 == SUPER:
                        alt135 = 1
                    elif LA135 == IDENT:
                        alt135 = 2
                    elif LA135 == THIS:
                        alt135 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 135, 0, self.input)

                        raise nvae


                    if alt135 == 1:
                        # Java.g:910:13: SUPER ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) )
                        pass 
                        SUPER467 = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression12701) 
                        if self._state.backtracking == 0:
                            stream_SUPER.add(SUPER467)


                        # Java.g:911:13: ( arguments -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments ) | DOT IDENT arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments ) )
                        alt134 = 2
                        LA134_0 = self.input.LA(1)

                        if (LA134_0 == LPAREN) :
                            alt134 = 1
                        elif (LA134_0 == DOT) :
                            alt134 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 134, 0, self.input)

                            raise nvae


                        if alt134 == 1:
                            # Java.g:911:17: arguments
                            pass 
                            self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12719)
                            arguments468 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments468.tree)


                            # AST Rewrite
                            # elements: genericTypeArgumentListSimplified, arguments
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 911:57: -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                                # Java.g:911:61: ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.create(SUPER_CONSTRUCTOR_CALL, SUPER467, "SUPER_CONSTRUCTOR_CALL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt134 == 2:
                            # Java.g:912:17: DOT IDENT arguments
                            pass 
                            DOT469 = self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression12779) 
                            if self._state.backtracking == 0:
                                stream_DOT.add(DOT469)


                            IDENT470 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression12781) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT470)


                            self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12783)
                            arguments471 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments471.tree)


                            # AST Rewrite
                            # elements: SUPER, genericTypeArgumentListSimplified, DOT, arguments, IDENT
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 912:57: -> ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments )
                                # Java.g:912:61: ^( METHOD_CALL ^( DOT SUPER IDENT ) genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                                , root_1)

                                # Java.g:912:75: ^( DOT SUPER IDENT )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(
                                stream_DOT.nextNode()
                                , root_2)

                                self._adaptor.addChild(root_2, 
                                stream_SUPER.nextNode()
                                )

                                self._adaptor.addChild(root_2, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, root_2)

                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0







                    elif alt135 == 2:
                        # Java.g:914:13: IDENT arguments
                        pass 
                        IDENT472 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression12850) 
                        if self._state.backtracking == 0:
                            stream_IDENT.add(IDENT472)


                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12852)
                        arguments473 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments473.tree)


                        # AST Rewrite
                        # elements: arguments, IDENT, genericTypeArgumentListSimplified
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 914:57: -> ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments )
                            # Java.g:914:61: ^( METHOD_CALL IDENT genericTypeArgumentListSimplified arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                            , root_1)

                            self._adaptor.addChild(root_1, 
                            stream_IDENT.nextNode()
                            )

                            self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt135 == 3:
                        # Java.g:915:13: THIS arguments
                        pass 
                        THIS474 = self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression12907) 
                        if self._state.backtracking == 0:
                            stream_THIS.add(THIS474)


                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression12909)
                        arguments475 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments475.tree)


                        # AST Rewrite
                        # elements: arguments, genericTypeArgumentListSimplified
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 915:57: -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                            # Java.g:915:61: ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] genericTypeArgumentListSimplified arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.create(THIS_CONSTRUCTOR_CALL, THIS474, "THIS_CONSTRUCTOR_CALL")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt139 == 6:
                    # Java.g:917:9: ( THIS -> THIS ) ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )?
                    pass 
                    # Java.g:917:9: ( THIS -> THIS )
                    # Java.g:917:13: THIS
                    pass 
                    THIS476 = self.match(self.input, THIS, self.FOLLOW_THIS_in_primaryExpression12974) 
                    if self._state.backtracking == 0:
                        stream_THIS.add(THIS476)


                    # AST Rewrite
                    # elements: THIS
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 917:57: -> THIS
                        self._adaptor.addChild(root_0, 
                        stream_THIS.nextNode()
                        )




                        retval.tree = root_0






                    # Java.g:919:9: ( arguments -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments ) )?
                    alt136 = 2
                    LA136_0 = self.input.LA(1)

                    if (LA136_0 == LPAREN) :
                        alt136 = 1
                    if alt136 == 1:
                        # Java.g:919:13: arguments
                        pass 
                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression13042)
                        arguments477 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments477.tree)


                        # AST Rewrite
                        # elements: arguments
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 919:57: -> ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments )
                            # Java.g:919:61: ^( THIS_CONSTRUCTOR_CALL[$THIS, \"THIS_CONSTRUCTOR_CALL\"] arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.create(THIS_CONSTRUCTOR_CALL, THIS476, "THIS_CONSTRUCTOR_CALL")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt139 == 7:
                    # Java.g:921:9: SUPER arguments
                    pass 
                    SUPER478 = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression13107) 
                    if self._state.backtracking == 0:
                        stream_SUPER.add(SUPER478)


                    self._state.following.append(self.FOLLOW_arguments_in_primaryExpression13109)
                    arguments479 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arguments.add(arguments479.tree)


                    # AST Rewrite
                    # elements: arguments
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 921:57: -> ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments )
                        # Java.g:921:61: ^( SUPER_CONSTRUCTOR_CALL[$SUPER, \"SUPER_CONSTRUCTOR_CALL\"] arguments )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(SUPER_CONSTRUCTOR_CALL, SUPER478, "SUPER_CONSTRUCTOR_CALL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_arguments.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt139 == 8:
                    # Java.g:922:9: ( SUPER DOT IDENT ) ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) )
                    pass 
                    # Java.g:922:9: ( SUPER DOT IDENT )
                    # Java.g:922:13: SUPER DOT IDENT
                    pass 
                    SUPER480 = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_primaryExpression13165) 
                    if self._state.backtracking == 0:
                        stream_SUPER.add(SUPER480)


                    DOT481 = self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression13167) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT481)


                    IDENT482 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_primaryExpression13169) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(IDENT482)





                    # Java.g:924:9: ( arguments -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments ) | -> ^( DOT SUPER IDENT ) )
                    alt137 = 2
                    LA137_0 = self.input.LA(1)

                    if (LA137_0 == LPAREN) :
                        alt137 = 1
                    elif (LA137_0 == EOF or (AND <= LA137_0 <= AND_ASSIGN) or LA137_0 == ASSIGN or (BIT_SHIFT_RIGHT <= LA137_0 <= BIT_SHIFT_RIGHT_ASSIGN) or (COLON <= LA137_0 <= COMMA) or LA137_0 == DEC or (DIV <= LA137_0 <= DIV_ASSIGN) or LA137_0 == DOT or LA137_0 == EQUAL or (GREATER_OR_EQUAL <= LA137_0 <= GREATER_THAN) or (INC <= LA137_0 <= INSTANCEOF) or LA137_0 == LBRACK or (LESS_OR_EQUAL <= LA137_0 <= LESS_THAN) or LA137_0 == LOGICAL_AND or LA137_0 == LOGICAL_OR or (MINUS <= LA137_0 <= MOD) or LA137_0 == MOD_ASSIGN or LA137_0 == NOT_EQUAL or (OR <= LA137_0 <= OR_ASSIGN) or (PLUS <= LA137_0 <= PLUS_ASSIGN) or (QUESTION <= LA137_0 <= RCURLY) or (RPAREN <= LA137_0 <= SHIFT_RIGHT_ASSIGN) or (STAR <= LA137_0 <= STAR_ASSIGN) or (XOR <= LA137_0 <= XOR_ASSIGN)) :
                        alt137 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 137, 0, self.input)

                        raise nvae


                    if alt137 == 1:
                        # Java.g:924:13: arguments
                        pass 
                        self._state.following.append(self.FOLLOW_arguments_in_primaryExpression13193)
                        arguments483 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments483.tree)


                        # AST Rewrite
                        # elements: arguments, SUPER, IDENT, DOT
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 924:57: -> ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments )
                            # Java.g:924:61: ^( METHOD_CALL ^( DOT SUPER IDENT ) arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                            , root_1)

                            # Java.g:924:75: ^( DOT SUPER IDENT )
                            root_2 = self._adaptor.nil()
                            root_2 = self._adaptor.becomeRoot(
                            stream_DOT.nextNode()
                            , root_2)

                            self._adaptor.addChild(root_2, 
                            stream_SUPER.nextNode()
                            )

                            self._adaptor.addChild(root_2, 
                            stream_IDENT.nextNode()
                            )

                            self._adaptor.addChild(root_1, root_2)

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt137 == 2:
                        # Java.g:925:57: 
                        pass 
                        # AST Rewrite
                        # elements: SUPER, IDENT, DOT
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 925:57: -> ^( DOT SUPER IDENT )
                            # Java.g:925:61: ^( DOT SUPER IDENT )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_DOT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, 
                            stream_SUPER.nextNode()
                            )

                            self._adaptor.addChild(root_1, 
                            stream_IDENT.nextNode()
                            )

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0







                elif alt139 == 9:
                    # Java.g:927:9: ( primitiveType -> primitiveType ) ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )* DOT CLASS
                    pass 
                    # Java.g:927:9: ( primitiveType -> primitiveType )
                    # Java.g:927:13: primitiveType
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_primaryExpression13335)
                    primitiveType484 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_primitiveType.add(primitiveType484.tree)


                    # AST Rewrite
                    # elements: primitiveType
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 927:57: -> primitiveType
                        self._adaptor.addChild(root_0, stream_primitiveType.nextTree())




                        retval.tree = root_0






                    # Java.g:929:9: ( arrayDeclarator -> ^( arrayDeclarator $primaryExpression) )*
                    while True: #loop138
                        alt138 = 2
                        LA138_0 = self.input.LA(1)

                        if (LA138_0 == LBRACK) :
                            alt138 = 1


                        if alt138 == 1:
                            # Java.g:929:13: arrayDeclarator
                            pass 
                            self._state.following.append(self.FOLLOW_arrayDeclarator_in_primaryExpression13394)
                            arrayDeclarator485 = self.arrayDeclarator()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arrayDeclarator.add(arrayDeclarator485.tree)


                            # AST Rewrite
                            # elements: primaryExpression, arrayDeclarator
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 929:57: -> ^( arrayDeclarator $primaryExpression)
                                # Java.g:929:61: ^( arrayDeclarator $primaryExpression)
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_arrayDeclarator.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        else:
                            break #loop138


                    DOT486 = self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression13457) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT486)


                    CLASS487 = self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression13459) 
                    if self._state.backtracking == 0:
                        stream_CLASS.add(CLASS487)


                    # AST Rewrite
                    # elements: CLASS, primaryExpression, DOT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 931:57: -> ^( DOT $primaryExpression CLASS )
                        # Java.g:931:61: ^( DOT $primaryExpression CLASS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_DOT.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())

                        self._adaptor.addChild(root_1, 
                        stream_CLASS.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt139 == 10:
                    # Java.g:932:9: VOID DOT CLASS
                    pass 
                    VOID488 = self.match(self.input, VOID, self.FOLLOW_VOID_in_primaryExpression13519) 
                    if self._state.backtracking == 0:
                        stream_VOID.add(VOID488)


                    DOT489 = self.match(self.input, DOT, self.FOLLOW_DOT_in_primaryExpression13521) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT489)


                    CLASS490 = self.match(self.input, CLASS, self.FOLLOW_CLASS_in_primaryExpression13523) 
                    if self._state.backtracking == 0:
                        stream_CLASS.add(CLASS490)


                    # AST Rewrite
                    # elements: VOID, CLASS, DOT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 932:57: -> ^( DOT VOID CLASS )
                        # Java.g:932:61: ^( DOT VOID CLASS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_DOT.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_VOID.nextNode()
                        )

                        self._adaptor.addChild(root_1, 
                        stream_CLASS.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 105, primaryExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "primaryExpression"


    class qualifiedIdentExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.qualifiedIdentExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "qualifiedIdentExpression"
    # Java.g:935:1: qualifiedIdentExpression : ( qualifiedIdentifier -> qualifiedIdentifier ) ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) |outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )? ;
    def qualifiedIdentExpression(self, ):
        retval = self.qualifiedIdentExpression_return()
        retval.start = self.input.LT(1)

        qualifiedIdentExpression_StartIndex = self.input.index()

        root_0 = None

        outerDot = None
        Super = None
        innerDot = None
        DOT493 = None
        CLASS494 = None
        CLASS496 = None
        SUPER499 = None
        IDENT500 = None
        IDENT502 = None
        THIS504 = None
        qualifiedIdentifier491 = None

        arrayDeclarator492 = None

        arguments495 = None

        genericTypeArgumentListSimplified497 = None

        arguments498 = None

        arguments501 = None

        arguments503 = None

        arguments505 = None

        innerNewExpression506 = None


        outerDot_tree = None
        Super_tree = None
        innerDot_tree = None
        DOT493_tree = None
        CLASS494_tree = None
        CLASS496_tree = None
        SUPER499_tree = None
        IDENT500_tree = None
        IDENT502_tree = None
        THIS504_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_arrayDeclarator = RewriteRuleSubtreeStream(self._adaptor, "rule arrayDeclarator")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_qualifiedIdentifier = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedIdentifier")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        stream_innerNewExpression = RewriteRuleSubtreeStream(self._adaptor, "rule innerNewExpression")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 106):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:937:5: ( ( qualifiedIdentifier -> qualifiedIdentifier ) ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) |outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )? )
                # Java.g:937:9: ( qualifiedIdentifier -> qualifiedIdentifier ) ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) |outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )?
                pass 
                # Java.g:937:9: ( qualifiedIdentifier -> qualifiedIdentifier )
                # Java.g:937:13: qualifiedIdentifier
                pass 
                self._state.following.append(self.FOLLOW_qualifiedIdentifier_in_qualifiedIdentExpression13603)
                qualifiedIdentifier491 = self.qualifiedIdentifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_qualifiedIdentifier.add(qualifiedIdentifier491.tree)


                # AST Rewrite
                # elements: qualifiedIdentifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 937:61: -> qualifiedIdentifier
                    self._adaptor.addChild(root_0, stream_qualifiedIdentifier.nextTree())




                    retval.tree = root_0






                # Java.g:940:9: ( ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) ) | arguments -> ^( METHOD_CALL qualifiedIdentifier arguments ) |outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) ) )?
                alt143 = 4
                LA143 = self.input.LA(1)
                if LA143 == LBRACK:
                    LA143_1 = self.input.LA(2)

                    if (self.synpred218_Java()) :
                        alt143 = 1
                elif LA143 == LPAREN:
                    alt143 = 2
                elif LA143 == DOT:
                    LA143_3 = self.input.LA(2)

                    if (self.synpred226_Java()) :
                        alt143 = 3
                if alt143 == 1:
                    # Java.g:940:13: ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+ ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) )
                    pass 
                    # Java.g:940:13: ( arrayDeclarator -> ^( arrayDeclarator $qualifiedIdentExpression) )+
                    cnt140 = 0
                    while True: #loop140
                        alt140 = 2
                        LA140_0 = self.input.LA(1)

                        if (LA140_0 == LBRACK) :
                            alt140 = 1


                        if alt140 == 1:
                            # Java.g:940:17: arrayDeclarator
                            pass 
                            self._state.following.append(self.FOLLOW_arrayDeclarator_in_qualifiedIdentExpression13673)
                            arrayDeclarator492 = self.arrayDeclarator()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arrayDeclarator.add(arrayDeclarator492.tree)


                            # AST Rewrite
                            # elements: qualifiedIdentExpression, arrayDeclarator
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 940:57: -> ^( arrayDeclarator $qualifiedIdentExpression)
                                # Java.g:940:61: ^( arrayDeclarator $qualifiedIdentExpression)
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(stream_arrayDeclarator.nextNode(), root_1)

                                self._adaptor.addChild(root_1, stream_retval.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        else:
                            if cnt140 >= 1:
                                break #loop140

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            eee = EarlyExitException(140, self.input)
                            raise eee

                        cnt140 += 1


                    # Java.g:942:13: ( DOT CLASS -> ^( DOT $qualifiedIdentExpression CLASS ) )
                    # Java.g:942:17: DOT CLASS
                    pass 
                    DOT493 = self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentExpression13741) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT493)


                    CLASS494 = self.match(self.input, CLASS, self.FOLLOW_CLASS_in_qualifiedIdentExpression13743) 
                    if self._state.backtracking == 0:
                        stream_CLASS.add(CLASS494)


                    # AST Rewrite
                    # elements: DOT, CLASS, qualifiedIdentExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 942:57: -> ^( DOT $qualifiedIdentExpression CLASS )
                        # Java.g:942:61: ^( DOT $qualifiedIdentExpression CLASS )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        stream_DOT.nextNode()
                        , root_1)

                        self._adaptor.addChild(root_1, stream_retval.nextTree())

                        self._adaptor.addChild(root_1, 
                        stream_CLASS.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0







                elif alt143 == 2:
                    # Java.g:944:13: arguments
                    pass 
                    self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13813)
                    arguments495 = self.arguments()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_arguments.add(arguments495.tree)


                    # AST Rewrite
                    # elements: qualifiedIdentifier, arguments
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 944:57: -> ^( METHOD_CALL qualifiedIdentifier arguments )
                        # Java.g:944:61: ^( METHOD_CALL qualifiedIdentifier arguments )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())

                        self._adaptor.addChild(root_1, stream_arguments.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt143 == 3:
                    # Java.g:945:13: outerDot= DOT ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) )
                    pass 
                    outerDot = self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentExpression13874) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(outerDot)


                    # Java.g:946:13: ( CLASS -> ^( DOT qualifiedIdentifier CLASS ) | genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) ) | THIS -> ^( DOT qualifiedIdentifier THIS ) |Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments ) | innerNewExpression -> ^( DOT qualifiedIdentifier innerNewExpression ) )
                    alt142 = 5
                    LA142 = self.input.LA(1)
                    if LA142 == CLASS:
                        alt142 = 1
                    elif LA142 == LESS_THAN:
                        alt142 = 2
                    elif LA142 == THIS:
                        alt142 = 3
                    elif LA142 == SUPER:
                        alt142 = 4
                    elif LA142 == NEW:
                        alt142 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 142, 0, self.input)

                        raise nvae


                    if alt142 == 1:
                        # Java.g:946:17: CLASS
                        pass 
                        CLASS496 = self.match(self.input, CLASS, self.FOLLOW_CLASS_in_qualifiedIdentExpression13892) 
                        if self._state.backtracking == 0:
                            stream_CLASS.add(CLASS496)


                        # AST Rewrite
                        # elements: qualifiedIdentifier, DOT, CLASS
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 946:57: -> ^( DOT qualifiedIdentifier CLASS )
                            # Java.g:946:61: ^( DOT qualifiedIdentifier CLASS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_DOT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())

                            self._adaptor.addChild(root_1, 
                            stream_CLASS.nextNode()
                            )

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt142 == 2:
                        # Java.g:947:17: genericTypeArgumentListSimplified (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) )
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_qualifiedIdentExpression13955)
                        genericTypeArgumentListSimplified497 = self.genericTypeArgumentListSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified497.tree)


                        # Java.g:948:17: (Super= SUPER arguments -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments ) | SUPER innerDot= DOT IDENT arguments -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments ) | IDENT arguments -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments ) )
                        alt141 = 3
                        LA141_0 = self.input.LA(1)

                        if (LA141_0 == SUPER) :
                            LA141_1 = self.input.LA(2)

                            if (LA141_1 == DOT) :
                                alt141 = 2
                            elif (LA141_1 == LPAREN) :
                                alt141 = 1
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 141, 1, self.input)

                                raise nvae


                        elif (LA141_0 == IDENT) :
                            alt141 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 141, 0, self.input)

                            raise nvae


                        if alt141 == 1:
                            # Java.g:948:21: Super= SUPER arguments
                            pass 
                            Super = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_qualifiedIdentExpression13980) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(Super)


                            self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression13982)
                            arguments498 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments498.tree)


                            # AST Rewrite
                            # elements: arguments, qualifiedIdentifier, genericTypeArgumentListSimplified
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 948:57: -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments )
                                # Java.g:948:61: ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.create(SUPER_CONSTRUCTOR_CALL, Super, "SUPER_CONSTRUCTOR_CALL")
                                , root_1)

                                self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())

                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt141 == 2:
                            # Java.g:949:21: SUPER innerDot= DOT IDENT arguments
                            pass 
                            SUPER499 = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_qualifiedIdentExpression14032) 
                            if self._state.backtracking == 0:
                                stream_SUPER.add(SUPER499)


                            innerDot = self.match(self.input, DOT, self.FOLLOW_DOT_in_qualifiedIdentExpression14036) 
                            if self._state.backtracking == 0:
                                stream_DOT.add(innerDot)


                            IDENT500 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentExpression14038) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT500)


                            self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression14040)
                            arguments501 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments501.tree)


                            # AST Rewrite
                            # elements: outerDot, arguments, qualifiedIdentifier, SUPER, innerDot, IDENT, genericTypeArgumentListSimplified
                            # token labels: outerDot, innerDot
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                stream_outerDot = RewriteRuleTokenStream(self._adaptor, "token outerDot", outerDot)
                                stream_innerDot = RewriteRuleTokenStream(self._adaptor, "token innerDot", innerDot)
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 949:57: -> ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments )
                                # Java.g:949:61: ^( METHOD_CALL ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT ) genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                                , root_1)

                                # Java.g:949:75: ^( $innerDot ^( $outerDot qualifiedIdentifier SUPER ) IDENT )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(stream_innerDot.nextNode(), root_2)

                                # Java.g:949:87: ^( $outerDot qualifiedIdentifier SUPER )
                                root_3 = self._adaptor.nil()
                                root_3 = self._adaptor.becomeRoot(stream_outerDot.nextNode(), root_3)

                                self._adaptor.addChild(root_3, stream_qualifiedIdentifier.nextTree())

                                self._adaptor.addChild(root_3, 
                                stream_SUPER.nextNode()
                                )

                                self._adaptor.addChild(root_2, root_3)

                                self._adaptor.addChild(root_2, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, root_2)

                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0




                        elif alt141 == 3:
                            # Java.g:950:21: IDENT arguments
                            pass 
                            IDENT502 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_qualifiedIdentExpression14090) 
                            if self._state.backtracking == 0:
                                stream_IDENT.add(IDENT502)


                            self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression14092)
                            arguments503 = self.arguments()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_arguments.add(arguments503.tree)


                            # AST Rewrite
                            # elements: qualifiedIdentifier, DOT, genericTypeArgumentListSimplified, IDENT, arguments
                            # token labels: 
                            # rule labels: retval
                            # token list labels: 
                            # rule list labels: 
                            # wildcard labels: 
                            if self._state.backtracking == 0:
                                retval.tree = root_0
                                if retval is not None:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                                else:
                                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                                root_0 = self._adaptor.nil()
                                # 950:57: -> ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments )
                                # Java.g:950:61: ^( METHOD_CALL ^( DOT qualifiedIdentifier IDENT ) genericTypeArgumentListSimplified arguments )
                                root_1 = self._adaptor.nil()
                                root_1 = self._adaptor.becomeRoot(
                                self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL")
                                , root_1)

                                # Java.g:950:75: ^( DOT qualifiedIdentifier IDENT )
                                root_2 = self._adaptor.nil()
                                root_2 = self._adaptor.becomeRoot(
                                stream_DOT.nextNode()
                                , root_2)

                                self._adaptor.addChild(root_2, stream_qualifiedIdentifier.nextTree())

                                self._adaptor.addChild(root_2, 
                                stream_IDENT.nextNode()
                                )

                                self._adaptor.addChild(root_1, root_2)

                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())

                                self._adaptor.addChild(root_1, stream_arguments.nextTree())

                                self._adaptor.addChild(root_0, root_1)




                                retval.tree = root_0







                    elif alt142 == 3:
                        # Java.g:952:17: THIS
                        pass 
                        THIS504 = self.match(self.input, THIS, self.FOLLOW_THIS_in_qualifiedIdentExpression14167) 
                        if self._state.backtracking == 0:
                            stream_THIS.add(THIS504)


                        # AST Rewrite
                        # elements: DOT, THIS, qualifiedIdentifier
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 952:57: -> ^( DOT qualifiedIdentifier THIS )
                            # Java.g:952:61: ^( DOT qualifiedIdentifier THIS )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_DOT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())

                            self._adaptor.addChild(root_1, 
                            stream_THIS.nextNode()
                            )

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt142 == 4:
                        # Java.g:953:17: Super= SUPER arguments
                        pass 
                        Super = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_qualifiedIdentExpression14233) 
                        if self._state.backtracking == 0:
                            stream_SUPER.add(Super)


                        self._state.following.append(self.FOLLOW_arguments_in_qualifiedIdentExpression14235)
                        arguments505 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments505.tree)


                        # AST Rewrite
                        # elements: qualifiedIdentifier, arguments
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 953:57: -> ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments )
                            # Java.g:953:61: ^( SUPER_CONSTRUCTOR_CALL[$Super, \"SUPER_CONSTRUCTOR_CALL\"] qualifiedIdentifier arguments )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.create(SUPER_CONSTRUCTOR_CALL, Super, "SUPER_CONSTRUCTOR_CALL")
                            , root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt142 == 5:
                        # Java.g:954:17: innerNewExpression
                        pass 
                        self._state.following.append(self.FOLLOW_innerNewExpression_in_qualifiedIdentExpression14283)
                        innerNewExpression506 = self.innerNewExpression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_innerNewExpression.add(innerNewExpression506.tree)


                        # AST Rewrite
                        # elements: DOT, qualifiedIdentifier, innerNewExpression
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 954:57: -> ^( DOT qualifiedIdentifier innerNewExpression )
                            # Java.g:954:61: ^( DOT qualifiedIdentifier innerNewExpression )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            stream_DOT.nextNode()
                            , root_1)

                            self._adaptor.addChild(root_1, stream_qualifiedIdentifier.nextTree())

                            self._adaptor.addChild(root_1, stream_innerNewExpression.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0











                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 106, qualifiedIdentExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "qualifiedIdentExpression"


    class newExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.newExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "newExpression"
    # Java.g:959:1: newExpression : NEW ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) ) ;
    def newExpression(self, ):
        retval = self.newExpression_return()
        retval.start = self.input.LT(1)

        newExpression_StartIndex = self.input.index()

        root_0 = None

        NEW507 = None
        primitiveType508 = None

        newArrayConstruction509 = None

        genericTypeArgumentListSimplified510 = None

        qualifiedTypeIdentSimplified511 = None

        newArrayConstruction512 = None

        arguments513 = None

        classBody514 = None


        NEW507_tree = None
        stream_NEW = RewriteRuleTokenStream(self._adaptor, "token NEW")
        stream_newArrayConstruction = RewriteRuleSubtreeStream(self._adaptor, "rule newArrayConstruction")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_qualifiedTypeIdentSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule qualifiedTypeIdentSimplified")
        stream_primitiveType = RewriteRuleSubtreeStream(self._adaptor, "rule primitiveType")
        stream_classBody = RewriteRuleSubtreeStream(self._adaptor, "rule classBody")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 107):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:960:5: ( NEW ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) ) )
                # Java.g:960:9: NEW ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) )
                pass 
                NEW507 = self.match(self.input, NEW, self.FOLLOW_NEW_in_newExpression14359) 
                if self._state.backtracking == 0:
                    stream_NEW.add(NEW507)


                # Java.g:961:9: ( primitiveType newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction ) | ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) ) )
                alt147 = 2
                LA147_0 = self.input.LA(1)

                if (LA147_0 == BOOLEAN or LA147_0 == BYTE or LA147_0 == CHAR or LA147_0 == DOUBLE or LA147_0 == FLOAT or LA147_0 == INT or LA147_0 == LONG or LA147_0 == SHORT) :
                    alt147 = 1
                elif (LA147_0 == IDENT or LA147_0 == LESS_THAN) :
                    alt147 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 147, 0, self.input)

                    raise nvae


                if alt147 == 1:
                    # Java.g:961:13: primitiveType newArrayConstruction
                    pass 
                    self._state.following.append(self.FOLLOW_primitiveType_in_newExpression14375)
                    primitiveType508 = self.primitiveType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_primitiveType.add(primitiveType508.tree)


                    self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression14377)
                    newArrayConstruction509 = self.newArrayConstruction()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_newArrayConstruction.add(newArrayConstruction509.tree)


                    # AST Rewrite
                    # elements: newArrayConstruction, primitiveType
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 962:13: -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction )
                        # Java.g:962:17: ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] primitiveType newArrayConstruction )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.create(STATIC_ARRAY_CREATOR, NEW507, "STATIC_ARRAY_CREATOR")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_primitiveType.nextTree())

                        self._adaptor.addChild(root_1, stream_newArrayConstruction.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt147 == 2:
                    # Java.g:963:13: ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) )
                    pass 
                    # Java.g:963:13: ( genericTypeArgumentListSimplified )?
                    alt144 = 2
                    LA144_0 = self.input.LA(1)

                    if (LA144_0 == LESS_THAN) :
                        alt144 = 1
                    if alt144 == 1:
                        # Java.g:963:13: genericTypeArgumentListSimplified
                        pass 
                        self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_newExpression14421)
                        genericTypeArgumentListSimplified510 = self.genericTypeArgumentListSimplified()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified510.tree)





                    self._state.following.append(self.FOLLOW_qualifiedTypeIdentSimplified_in_newExpression14424)
                    qualifiedTypeIdentSimplified511 = self.qualifiedTypeIdentSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_qualifiedTypeIdentSimplified.add(qualifiedTypeIdentSimplified511.tree)


                    # Java.g:964:13: ( newArrayConstruction -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction ) | arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? ) )
                    alt146 = 2
                    LA146_0 = self.input.LA(1)

                    if (LA146_0 == LBRACK) :
                        alt146 = 1
                    elif (LA146_0 == LPAREN) :
                        alt146 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 146, 0, self.input)

                        raise nvae


                    if alt146 == 1:
                        # Java.g:964:17: newArrayConstruction
                        pass 
                        self._state.following.append(self.FOLLOW_newArrayConstruction_in_newExpression14442)
                        newArrayConstruction512 = self.newArrayConstruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_newArrayConstruction.add(newArrayConstruction512.tree)


                        # AST Rewrite
                        # elements: newArrayConstruction, genericTypeArgumentListSimplified, qualifiedTypeIdentSimplified
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 965:17: -> ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction )
                            # Java.g:965:21: ^( STATIC_ARRAY_CREATOR[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified newArrayConstruction )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.create(STATIC_ARRAY_CREATOR, NEW507, "STATIC_ARRAY_CREATOR")
                            , root_1)

                            # Java.g:965:74: ( genericTypeArgumentListSimplified )?
                            if stream_genericTypeArgumentListSimplified.hasNext():
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                            stream_genericTypeArgumentListSimplified.reset();

                            self._adaptor.addChild(root_1, stream_qualifiedTypeIdentSimplified.nextTree())

                            self._adaptor.addChild(root_1, stream_newArrayConstruction.nextTree())

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0




                    elif alt146 == 2:
                        # Java.g:966:17: arguments ( classBody )?
                        pass 
                        self._state.following.append(self.FOLLOW_arguments_in_newExpression14507)
                        arguments513 = self.arguments()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_arguments.add(arguments513.tree)


                        # Java.g:966:27: ( classBody )?
                        alt145 = 2
                        LA145_0 = self.input.LA(1)

                        if (LA145_0 == LCURLY) :
                            alt145 = 1
                        if alt145 == 1:
                            # Java.g:966:27: classBody
                            pass 
                            self._state.following.append(self.FOLLOW_classBody_in_newExpression14509)
                            classBody514 = self.classBody()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_classBody.add(classBody514.tree)





                        # AST Rewrite
                        # elements: classBody, qualifiedTypeIdentSimplified, genericTypeArgumentListSimplified, arguments
                        # token labels: 
                        # rule labels: retval
                        # token list labels: 
                        # rule list labels: 
                        # wildcard labels: 
                        if self._state.backtracking == 0:
                            retval.tree = root_0
                            if retval is not None:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                            else:
                                stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                            root_0 = self._adaptor.nil()
                            # 967:17: -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? )
                            # Java.g:967:21: ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? qualifiedTypeIdentSimplified arguments ( classBody )? )
                            root_1 = self._adaptor.nil()
                            root_1 = self._adaptor.becomeRoot(
                            self._adaptor.create(CLASS_CONSTRUCTOR_CALL, NEW507, "STATIC_ARRAY_CREATOR")
                            , root_1)

                            # Java.g:967:76: ( genericTypeArgumentListSimplified )?
                            if stream_genericTypeArgumentListSimplified.hasNext():
                                self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                            stream_genericTypeArgumentListSimplified.reset();

                            self._adaptor.addChild(root_1, stream_qualifiedTypeIdentSimplified.nextTree())

                            self._adaptor.addChild(root_1, stream_arguments.nextTree())

                            # Java.g:967:150: ( classBody )?
                            if stream_classBody.hasNext():
                                self._adaptor.addChild(root_1, stream_classBody.nextTree())


                            stream_classBody.reset();

                            self._adaptor.addChild(root_0, root_1)




                            retval.tree = root_0











                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 107, newExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "newExpression"


    class innerNewExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.innerNewExpression_return, self).__init__()

            self.tree = None





    # $ANTLR start "innerNewExpression"
    # Java.g:972:1: innerNewExpression : NEW ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? ) ;
    def innerNewExpression(self, ):
        retval = self.innerNewExpression_return()
        retval.start = self.input.LT(1)

        innerNewExpression_StartIndex = self.input.index()

        root_0 = None

        NEW515 = None
        IDENT517 = None
        genericTypeArgumentListSimplified516 = None

        arguments518 = None

        classBody519 = None


        NEW515_tree = None
        IDENT517_tree = None
        stream_NEW = RewriteRuleTokenStream(self._adaptor, "token NEW")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_arguments = RewriteRuleSubtreeStream(self._adaptor, "rule arguments")
        stream_classBody = RewriteRuleSubtreeStream(self._adaptor, "rule classBody")
        stream_genericTypeArgumentListSimplified = RewriteRuleSubtreeStream(self._adaptor, "rule genericTypeArgumentListSimplified")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 108):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:973:5: ( NEW ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? ) )
                # Java.g:973:9: NEW ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )?
                pass 
                NEW515 = self.match(self.input, NEW, self.FOLLOW_NEW_in_innerNewExpression14608) 
                if self._state.backtracking == 0:
                    stream_NEW.add(NEW515)


                # Java.g:973:13: ( genericTypeArgumentListSimplified )?
                alt148 = 2
                LA148_0 = self.input.LA(1)

                if (LA148_0 == LESS_THAN) :
                    alt148 = 1
                if alt148 == 1:
                    # Java.g:973:13: genericTypeArgumentListSimplified
                    pass 
                    self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_innerNewExpression14610)
                    genericTypeArgumentListSimplified516 = self.genericTypeArgumentListSimplified()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_genericTypeArgumentListSimplified.add(genericTypeArgumentListSimplified516.tree)





                IDENT517 = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_innerNewExpression14613) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT517)


                self._state.following.append(self.FOLLOW_arguments_in_innerNewExpression14615)
                arguments518 = self.arguments()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_arguments.add(arguments518.tree)


                # Java.g:973:64: ( classBody )?
                alt149 = 2
                LA149_0 = self.input.LA(1)

                if (LA149_0 == LCURLY) :
                    alt149 = 1
                if alt149 == 1:
                    # Java.g:973:64: classBody
                    pass 
                    self._state.following.append(self.FOLLOW_classBody_in_innerNewExpression14617)
                    classBody519 = self.classBody()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_classBody.add(classBody519.tree)





                # AST Rewrite
                # elements: arguments, IDENT, classBody, genericTypeArgumentListSimplified
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 974:9: -> ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? )
                    # Java.g:974:13: ^( CLASS_CONSTRUCTOR_CALL[$NEW, \"STATIC_ARRAY_CREATOR\"] ( genericTypeArgumentListSimplified )? IDENT arguments ( classBody )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(CLASS_CONSTRUCTOR_CALL, NEW515, "STATIC_ARRAY_CREATOR")
                    , root_1)

                    # Java.g:974:68: ( genericTypeArgumentListSimplified )?
                    if stream_genericTypeArgumentListSimplified.hasNext():
                        self._adaptor.addChild(root_1, stream_genericTypeArgumentListSimplified.nextTree())


                    stream_genericTypeArgumentListSimplified.reset();

                    self._adaptor.addChild(root_1, 
                    stream_IDENT.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_arguments.nextTree())

                    # Java.g:974:119: ( classBody )?
                    if stream_classBody.hasNext():
                        self._adaptor.addChild(root_1, stream_classBody.nextTree())


                    stream_classBody.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 108, innerNewExpression_StartIndex, success)


            pass
        return retval

    # $ANTLR end "innerNewExpression"


    class newArrayConstruction_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.newArrayConstruction_return, self).__init__()

            self.tree = None





    # $ANTLR start "newArrayConstruction"
    # Java.g:977:1: newArrayConstruction : ( arrayDeclaratorList arrayInitializer | LBRACK ! expression RBRACK ! ( LBRACK ! expression RBRACK !)* ( arrayDeclaratorList )? );
    def newArrayConstruction(self, ):
        retval = self.newArrayConstruction_return()
        retval.start = self.input.LT(1)

        newArrayConstruction_StartIndex = self.input.index()

        root_0 = None

        LBRACK522 = None
        RBRACK524 = None
        LBRACK525 = None
        RBRACK527 = None
        arrayDeclaratorList520 = None

        arrayInitializer521 = None

        expression523 = None

        expression526 = None

        arrayDeclaratorList528 = None


        LBRACK522_tree = None
        RBRACK524_tree = None
        LBRACK525_tree = None
        RBRACK527_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 109):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:978:5: ( arrayDeclaratorList arrayInitializer | LBRACK ! expression RBRACK ! ( LBRACK ! expression RBRACK !)* ( arrayDeclaratorList )? )
                alt152 = 2
                LA152_0 = self.input.LA(1)

                if (LA152_0 == LBRACK) :
                    LA152_1 = self.input.LA(2)

                    if (LA152_1 == RBRACK) :
                        alt152 = 1
                    elif (LA152_1 == BOOLEAN or LA152_1 == BYTE or (CHAR <= LA152_1 <= CHARACTER_LITERAL) or (DEC <= LA152_1 <= DECIMAL_LITERAL) or LA152_1 == DOUBLE or LA152_1 == FALSE or (FLOAT <= LA152_1 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA152_1 <= IDENT) or LA152_1 == INC or LA152_1 == INT or LA152_1 == LESS_THAN or LA152_1 == LOGICAL_NOT or (LONG <= LA152_1 <= LPAREN) or LA152_1 == MINUS or (NEW <= LA152_1 <= NOT) or LA152_1 == NULL or LA152_1 == OCTAL_LITERAL or LA152_1 == PLUS or LA152_1 == SHORT or (STRING_LITERAL <= LA152_1 <= SUPER) or LA152_1 == THIS or LA152_1 == TRUE or LA152_1 == VOID) :
                        alt152 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 152, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 152, 0, self.input)

                    raise nvae


                if alt152 == 1:
                    # Java.g:978:9: arrayDeclaratorList arrayInitializer
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction14663)
                    arrayDeclaratorList520 = self.arrayDeclaratorList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayDeclaratorList520.tree)


                    self._state.following.append(self.FOLLOW_arrayInitializer_in_newArrayConstruction14665)
                    arrayInitializer521 = self.arrayInitializer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arrayInitializer521.tree)



                elif alt152 == 2:
                    # Java.g:979:9: LBRACK ! expression RBRACK ! ( LBRACK ! expression RBRACK !)* ( arrayDeclaratorList )?
                    pass 
                    root_0 = self._adaptor.nil()


                    LBRACK522 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_newArrayConstruction14675)

                    self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction14678)
                    expression523 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression523.tree)


                    RBRACK524 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_newArrayConstruction14680)

                    # Java.g:979:36: ( LBRACK ! expression RBRACK !)*
                    while True: #loop150
                        alt150 = 2
                        LA150_0 = self.input.LA(1)

                        if (LA150_0 == LBRACK) :
                            LA150_1 = self.input.LA(2)

                            if (self.synpred234_Java()) :
                                alt150 = 1




                        if alt150 == 1:
                            # Java.g:979:37: LBRACK ! expression RBRACK !
                            pass 
                            LBRACK525 = self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_newArrayConstruction14684)

                            self._state.following.append(self.FOLLOW_expression_in_newArrayConstruction14687)
                            expression526 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, expression526.tree)


                            RBRACK527 = self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_newArrayConstruction14689)


                        else:
                            break #loop150


                    # Java.g:979:66: ( arrayDeclaratorList )?
                    alt151 = 2
                    LA151_0 = self.input.LA(1)

                    if (LA151_0 == LBRACK) :
                        LA151_1 = self.input.LA(2)

                        if (LA151_1 == RBRACK) :
                            alt151 = 1
                    if alt151 == 1:
                        # Java.g:979:66: arrayDeclaratorList
                        pass 
                        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_newArrayConstruction14694)
                        arrayDeclaratorList528 = self.arrayDeclaratorList()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arrayDeclaratorList528.tree)






                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 109, newArrayConstruction_StartIndex, success)


            pass
        return retval

    # $ANTLR end "newArrayConstruction"


    class arguments_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.arguments_return, self).__init__()

            self.tree = None





    # $ANTLR start "arguments"
    # Java.g:982:1: arguments : LPAREN ( expressionList )? RPAREN -> ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? ) ;
    def arguments(self, ):
        retval = self.arguments_return()
        retval.start = self.input.LT(1)

        arguments_StartIndex = self.input.index()

        root_0 = None

        LPAREN529 = None
        RPAREN531 = None
        expressionList530 = None


        LPAREN529_tree = None
        RPAREN531_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expressionList = RewriteRuleSubtreeStream(self._adaptor, "rule expressionList")
        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 110):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:983:5: ( LPAREN ( expressionList )? RPAREN -> ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? ) )
                # Java.g:983:9: LPAREN ( expressionList )? RPAREN
                pass 
                LPAREN529 = self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_arguments14714) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN529)


                # Java.g:983:16: ( expressionList )?
                alt153 = 2
                LA153_0 = self.input.LA(1)

                if (LA153_0 == BOOLEAN or LA153_0 == BYTE or (CHAR <= LA153_0 <= CHARACTER_LITERAL) or (DEC <= LA153_0 <= DECIMAL_LITERAL) or LA153_0 == DOUBLE or LA153_0 == FALSE or (FLOAT <= LA153_0 <= FLOATING_POINT_LITERAL) or (HEX_LITERAL <= LA153_0 <= IDENT) or LA153_0 == INC or LA153_0 == INT or LA153_0 == LESS_THAN or LA153_0 == LOGICAL_NOT or (LONG <= LA153_0 <= LPAREN) or LA153_0 == MINUS or (NEW <= LA153_0 <= NOT) or LA153_0 == NULL or LA153_0 == OCTAL_LITERAL or LA153_0 == PLUS or LA153_0 == SHORT or (STRING_LITERAL <= LA153_0 <= SUPER) or LA153_0 == THIS or LA153_0 == TRUE or LA153_0 == VOID) :
                    alt153 = 1
                if alt153 == 1:
                    # Java.g:983:16: expressionList
                    pass 
                    self._state.following.append(self.FOLLOW_expressionList_in_arguments14716)
                    expressionList530 = self.expressionList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressionList.add(expressionList530.tree)





                RPAREN531 = self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_arguments14719) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN531)


                # AST Rewrite
                # elements: expressionList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 984:9: -> ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? )
                    # Java.g:984:13: ^( ARGUMENT_LIST[$LPAREN, \"ARGUMENT_LIST\"] ( expressionList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.create(ARGUMENT_LIST, LPAREN529, "ARGUMENT_LIST")
                    , root_1)

                    # Java.g:984:55: ( expressionList )?
                    if stream_expressionList.hasNext():
                        self._adaptor.addChild(root_1, stream_expressionList.nextTree())


                    stream_expressionList.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 110, arguments_StartIndex, success)


            pass
        return retval

    # $ANTLR end "arguments"


    class literal_return(ParserRuleReturnScope):
        def __init__(self):
            super(JavaParser.literal_return, self).__init__()

            self.tree = None





    # $ANTLR start "literal"
    # Java.g:987:1: literal : ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL );
    def literal(self, ):
        retval = self.literal_return()
        retval.start = self.input.LT(1)

        literal_StartIndex = self.input.index()

        root_0 = None

        set532 = None

        set532_tree = None

        success = False

        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 111):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval


                # Java.g:988:5: ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL | FLOATING_POINT_LITERAL | CHARACTER_LITERAL | STRING_LITERAL | TRUE | FALSE | NULL )
                # Java.g:
                pass 
                root_0 = self._adaptor.nil()


                set532 = self.input.LT(1)

                if self.input.LA(1) == CHARACTER_LITERAL or self.input.LA(1) == DECIMAL_LITERAL or self.input.LA(1) == FALSE or self.input.LA(1) == FLOATING_POINT_LITERAL or self.input.LA(1) == HEX_LITERAL or self.input.LA(1) == NULL or self.input.LA(1) == OCTAL_LITERAL or self.input.LA(1) == STRING_LITERAL or self.input.LA(1) == TRUE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set532))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                success = True

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 111, literal_StartIndex, success)


            pass
        return retval

    # $ANTLR end "literal"

    # $ANTLR start "synpred14_Java"
    def synpred14_Java_fragment(self, ):
        # Java.g:305:9: ( GREATER_THAN )
        # Java.g:305:9: GREATER_THAN
        pass 
        self.match(self.input, GREATER_THAN, self.FOLLOW_GREATER_THAN_in_synpred14_Java5102)



    # $ANTLR end "synpred14_Java"



    # $ANTLR start "synpred15_Java"
    def synpred15_Java_fragment(self, ):
        # Java.g:306:9: ( SHIFT_RIGHT )
        # Java.g:306:9: SHIFT_RIGHT
        pass 
        self.match(self.input, SHIFT_RIGHT, self.FOLLOW_SHIFT_RIGHT_in_synpred15_Java5112)



    # $ANTLR end "synpred15_Java"



    # $ANTLR start "synpred16_Java"
    def synpred16_Java_fragment(self, ):
        # Java.g:307:9: ( BIT_SHIFT_RIGHT )
        # Java.g:307:9: BIT_SHIFT_RIGHT
        pass 
        self.match(self.input, BIT_SHIFT_RIGHT, self.FOLLOW_BIT_SHIFT_RIGHT_in_synpred16_Java5122)



    # $ANTLR end "synpred16_Java"



    # $ANTLR start "synpred17_Java"
    def synpred17_Java_fragment(self, ):
        # Java.g:312:15: ( bound )
        # Java.g:312:15: bound
        pass 
        self._state.following.append(self.FOLLOW_bound_in_synpred17_Java5152)
        self.bound()

        self._state.following.pop()



    # $ANTLR end "synpred17_Java"



    # $ANTLR start "synpred32_Java"
    def synpred32_Java_fragment(self, ):
        # Java.g:369:9: ( STATIC block )
        # Java.g:369:9: STATIC block
        pass 
        self.match(self.input, STATIC, self.FOLLOW_STATIC_in_synpred32_Java5684)

        self._state.following.append(self.FOLLOW_block_in_synpred32_Java5686)
        self.block()

        self._state.following.pop()



    # $ANTLR end "synpred32_Java"



    # $ANTLR start "synpred42_Java"
    def synpred42_Java_fragment(self, ):
        # Java.g:371:13: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block ) )
        # Java.g:371:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block )
        pass 
        # Java.g:371:13: ( genericTypeParameterList )?
        alt159 = 2
        LA159_0 = self.input.LA(1)

        if (LA159_0 == LESS_THAN) :
            alt159 = 1
        if alt159 == 1:
            # Java.g:371:13: genericTypeParameterList
            pass 
            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred42_Java5723)
            self.genericTypeParameterList()

            self._state.following.pop()




        # Java.g:372:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block )
        alt166 = 3
        LA166 = self.input.LA(1)
        if LA166 == BOOLEAN or LA166 == BYTE or LA166 == CHAR or LA166 == DOUBLE or LA166 == FLOAT or LA166 == INT or LA166 == LONG or LA166 == SHORT:
            alt166 = 1
        elif LA166 == IDENT:
            LA166_2 = self.input.LA(2)

            if (LA166_2 == DOT or LA166_2 == IDENT or LA166_2 == LBRACK or LA166_2 == LESS_THAN) :
                alt166 = 1
            elif (LA166_2 == LPAREN) :
                alt166 = 3
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 166, 2, self.input)

                raise nvae


        elif LA166 == VOID:
            alt166 = 2
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 166, 0, self.input)

            raise nvae


        if alt166 == 1:
            # Java.g:372:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI )
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred42_Java5742)
            self.type()

            self._state.following.pop()

            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred42_Java5744)

            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred42_Java5746)
            self.formalParameterList()

            self._state.following.pop()

            # Java.g:372:48: ( arrayDeclaratorList )?
            alt160 = 2
            LA160_0 = self.input.LA(1)

            if (LA160_0 == LBRACK) :
                alt160 = 1
            if alt160 == 1:
                # Java.g:372:48: arrayDeclaratorList
                pass 
                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred42_Java5748)
                self.arrayDeclaratorList()

                self._state.following.pop()




            # Java.g:372:69: ( throwsClause )?
            alt161 = 2
            LA161_0 = self.input.LA(1)

            if (LA161_0 == THROWS) :
                alt161 = 1
            if alt161 == 1:
                # Java.g:372:69: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred42_Java5751)
                self.throwsClause()

                self._state.following.pop()




            # Java.g:372:83: ( block | SEMI )
            alt162 = 2
            LA162_0 = self.input.LA(1)

            if (LA162_0 == LCURLY) :
                alt162 = 1
            elif (LA162_0 == SEMI) :
                alt162 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 162, 0, self.input)

                raise nvae


            if alt162 == 1:
                # Java.g:372:84: block
                pass 
                self._state.following.append(self.FOLLOW_block_in_synpred42_Java5755)
                self.block()

                self._state.following.pop()


            elif alt162 == 2:
                # Java.g:372:92: SEMI
                pass 
                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred42_Java5759)





        elif alt166 == 2:
            # Java.g:374:17: VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI )
            pass 
            self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred42_Java5821)

            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred42_Java5823)

            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred42_Java5825)
            self.formalParameterList()

            self._state.following.pop()

            # Java.g:374:48: ( throwsClause )?
            alt163 = 2
            LA163_0 = self.input.LA(1)

            if (LA163_0 == THROWS) :
                alt163 = 1
            if alt163 == 1:
                # Java.g:374:48: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred42_Java5827)
                self.throwsClause()

                self._state.following.pop()




            # Java.g:374:62: ( block | SEMI )
            alt164 = 2
            LA164_0 = self.input.LA(1)

            if (LA164_0 == LCURLY) :
                alt164 = 1
            elif (LA164_0 == SEMI) :
                alt164 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 164, 0, self.input)

                raise nvae


            if alt164 == 1:
                # Java.g:374:63: block
                pass 
                self._state.following.append(self.FOLLOW_block_in_synpred42_Java5831)
                self.block()

                self._state.following.pop()


            elif alt164 == 2:
                # Java.g:374:71: SEMI
                pass 
                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred42_Java5835)





        elif alt166 == 3:
            # Java.g:376:17: ident= IDENT formalParameterList ( throwsClause )? block
            pass 
            ident = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred42_Java5894)

            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred42_Java5896)
            self.formalParameterList()

            self._state.following.pop()

            # Java.g:376:49: ( throwsClause )?
            alt165 = 2
            LA165_0 = self.input.LA(1)

            if (LA165_0 == THROWS) :
                alt165 = 1
            if alt165 == 1:
                # Java.g:376:49: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred42_Java5898)
                self.throwsClause()

                self._state.following.pop()




            self._state.following.append(self.FOLLOW_block_in_synpred42_Java5901)
            self.block()

            self._state.following.pop()






    # $ANTLR end "synpred42_Java"



    # $ANTLR start "synpred43_Java"
    def synpred43_Java_fragment(self, ):
        # Java.g:370:9: ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block ) | type classFieldDeclaratorList SEMI ) )
        # Java.g:370:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block ) | type classFieldDeclaratorList SEMI )
        pass 
        self._state.following.append(self.FOLLOW_modifierList_in_synpred43_Java5709)
        self.modifierList()

        self._state.following.pop()

        # Java.g:371:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block ) | type classFieldDeclaratorList SEMI )
        alt175 = 2
        LA175 = self.input.LA(1)
        if LA175 == LESS_THAN or LA175 == VOID:
            alt175 = 1
        elif LA175 == BOOLEAN or LA175 == BYTE or LA175 == CHAR or LA175 == DOUBLE or LA175 == FLOAT or LA175 == INT or LA175 == LONG or LA175 == SHORT:
            LA175_2 = self.input.LA(2)

            if (self.synpred42_Java()) :
                alt175 = 1
            elif (True) :
                alt175 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 175, 2, self.input)

                raise nvae


        elif LA175 == IDENT:
            LA175_3 = self.input.LA(2)

            if (self.synpred42_Java()) :
                alt175 = 1
            elif (True) :
                alt175 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 175, 3, self.input)

                raise nvae


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 175, 0, self.input)

            raise nvae


        if alt175 == 1:
            # Java.g:371:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block )
            pass 
            # Java.g:371:13: ( genericTypeParameterList )?
            alt167 = 2
            LA167_0 = self.input.LA(1)

            if (LA167_0 == LESS_THAN) :
                alt167 = 1
            if alt167 == 1:
                # Java.g:371:13: genericTypeParameterList
                pass 
                self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred43_Java5723)
                self.genericTypeParameterList()

                self._state.following.pop()




            # Java.g:372:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI ) | VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI ) |ident= IDENT formalParameterList ( throwsClause )? block )
            alt174 = 3
            LA174 = self.input.LA(1)
            if LA174 == BOOLEAN or LA174 == BYTE or LA174 == CHAR or LA174 == DOUBLE or LA174 == FLOAT or LA174 == INT or LA174 == LONG or LA174 == SHORT:
                alt174 = 1
            elif LA174 == IDENT:
                LA174_2 = self.input.LA(2)

                if (LA174_2 == DOT or LA174_2 == IDENT or LA174_2 == LBRACK or LA174_2 == LESS_THAN) :
                    alt174 = 1
                elif (LA174_2 == LPAREN) :
                    alt174 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 174, 2, self.input)

                    raise nvae


            elif LA174 == VOID:
                alt174 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 174, 0, self.input)

                raise nvae


            if alt174 == 1:
                # Java.g:372:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? ( block | SEMI )
                pass 
                self._state.following.append(self.FOLLOW_type_in_synpred43_Java5742)
                self.type()

                self._state.following.pop()

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred43_Java5744)

                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred43_Java5746)
                self.formalParameterList()

                self._state.following.pop()

                # Java.g:372:48: ( arrayDeclaratorList )?
                alt168 = 2
                LA168_0 = self.input.LA(1)

                if (LA168_0 == LBRACK) :
                    alt168 = 1
                if alt168 == 1:
                    # Java.g:372:48: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred43_Java5748)
                    self.arrayDeclaratorList()

                    self._state.following.pop()




                # Java.g:372:69: ( throwsClause )?
                alt169 = 2
                LA169_0 = self.input.LA(1)

                if (LA169_0 == THROWS) :
                    alt169 = 1
                if alt169 == 1:
                    # Java.g:372:69: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred43_Java5751)
                    self.throwsClause()

                    self._state.following.pop()




                # Java.g:372:83: ( block | SEMI )
                alt170 = 2
                LA170_0 = self.input.LA(1)

                if (LA170_0 == LCURLY) :
                    alt170 = 1
                elif (LA170_0 == SEMI) :
                    alt170 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 170, 0, self.input)

                    raise nvae


                if alt170 == 1:
                    # Java.g:372:84: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_synpred43_Java5755)
                    self.block()

                    self._state.following.pop()


                elif alt170 == 2:
                    # Java.g:372:92: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred43_Java5759)





            elif alt174 == 2:
                # Java.g:374:17: VOID IDENT formalParameterList ( throwsClause )? ( block | SEMI )
                pass 
                self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred43_Java5821)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred43_Java5823)

                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred43_Java5825)
                self.formalParameterList()

                self._state.following.pop()

                # Java.g:374:48: ( throwsClause )?
                alt171 = 2
                LA171_0 = self.input.LA(1)

                if (LA171_0 == THROWS) :
                    alt171 = 1
                if alt171 == 1:
                    # Java.g:374:48: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred43_Java5827)
                    self.throwsClause()

                    self._state.following.pop()




                # Java.g:374:62: ( block | SEMI )
                alt172 = 2
                LA172_0 = self.input.LA(1)

                if (LA172_0 == LCURLY) :
                    alt172 = 1
                elif (LA172_0 == SEMI) :
                    alt172 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 172, 0, self.input)

                    raise nvae


                if alt172 == 1:
                    # Java.g:374:63: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_synpred43_Java5831)
                    self.block()

                    self._state.following.pop()


                elif alt172 == 2:
                    # Java.g:374:71: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred43_Java5835)





            elif alt174 == 3:
                # Java.g:376:17: ident= IDENT formalParameterList ( throwsClause )? block
                pass 
                ident = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred43_Java5894)

                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred43_Java5896)
                self.formalParameterList()

                self._state.following.pop()

                # Java.g:376:49: ( throwsClause )?
                alt173 = 2
                LA173_0 = self.input.LA(1)

                if (LA173_0 == THROWS) :
                    alt173 = 1
                if alt173 == 1:
                    # Java.g:376:49: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred43_Java5898)
                    self.throwsClause()

                    self._state.following.pop()




                self._state.following.append(self.FOLLOW_block_in_synpred43_Java5901)
                self.block()

                self._state.following.pop()





        elif alt175 == 2:
            # Java.g:379:13: type classFieldDeclaratorList SEMI
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred43_Java5965)
            self.type()

            self._state.following.pop()

            self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_synpred43_Java5967)
            self.classFieldDeclaratorList()

            self._state.following.pop()

            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred43_Java5969)






    # $ANTLR end "synpred43_Java"



    # $ANTLR start "synpred44_Java"
    def synpred44_Java_fragment(self, ):
        # Java.g:382:9: ( typeDeclaration )
        # Java.g:382:9: typeDeclaration
        pass 
        self._state.following.append(self.FOLLOW_typeDeclaration_in_synpred44_Java6014)
        self.typeDeclaration()

        self._state.following.pop()



    # $ANTLR end "synpred44_Java"



    # $ANTLR start "synpred50_Java"
    def synpred50_Java_fragment(self, ):
        # Java.g:388:13: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) )
        # Java.g:388:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
        pass 
        # Java.g:388:13: ( genericTypeParameterList )?
        alt178 = 2
        LA178_0 = self.input.LA(1)

        if (LA178_0 == LESS_THAN) :
            alt178 = 1
        if alt178 == 1:
            # Java.g:388:13: genericTypeParameterList
            pass 
            self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred50_Java6070)
            self.genericTypeParameterList()

            self._state.following.pop()




        # Java.g:389:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
        alt182 = 2
        LA182_0 = self.input.LA(1)

        if (LA182_0 == BOOLEAN or LA182_0 == BYTE or LA182_0 == CHAR or LA182_0 == DOUBLE or LA182_0 == FLOAT or LA182_0 == IDENT or LA182_0 == INT or LA182_0 == LONG or LA182_0 == SHORT) :
            alt182 = 1
        elif (LA182_0 == VOID) :
            alt182 = 2
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 182, 0, self.input)

            raise nvae


        if alt182 == 1:
            # Java.g:389:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred50_Java6089)
            self.type()

            self._state.following.pop()

            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred50_Java6091)

            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred50_Java6093)
            self.formalParameterList()

            self._state.following.pop()

            # Java.g:389:48: ( arrayDeclaratorList )?
            alt179 = 2
            LA179_0 = self.input.LA(1)

            if (LA179_0 == LBRACK) :
                alt179 = 1
            if alt179 == 1:
                # Java.g:389:48: arrayDeclaratorList
                pass 
                self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred50_Java6095)
                self.arrayDeclaratorList()

                self._state.following.pop()




            # Java.g:389:69: ( throwsClause )?
            alt180 = 2
            LA180_0 = self.input.LA(1)

            if (LA180_0 == THROWS) :
                alt180 = 1
            if alt180 == 1:
                # Java.g:389:69: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred50_Java6098)
                self.throwsClause()

                self._state.following.pop()




            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred50_Java6101)


        elif alt182 == 2:
            # Java.g:391:17: VOID IDENT formalParameterList ( throwsClause )? SEMI
            pass 
            self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred50_Java6159)

            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred50_Java6161)

            self._state.following.append(self.FOLLOW_formalParameterList_in_synpred50_Java6163)
            self.formalParameterList()

            self._state.following.pop()

            # Java.g:391:48: ( throwsClause )?
            alt181 = 2
            LA181_0 = self.input.LA(1)

            if (LA181_0 == THROWS) :
                alt181 = 1
            if alt181 == 1:
                # Java.g:391:48: throwsClause
                pass 
                self._state.following.append(self.FOLLOW_throwsClause_in_synpred50_Java6165)
                self.throwsClause()

                self._state.following.pop()




            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred50_Java6168)






    # $ANTLR end "synpred50_Java"



    # $ANTLR start "synpred51_Java"
    def synpred51_Java_fragment(self, ):
        # Java.g:387:9: ( modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) | type interfaceFieldDeclaratorList SEMI ) )
        # Java.g:387:9: modifierList ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) | type interfaceFieldDeclaratorList SEMI )
        pass 
        self._state.following.append(self.FOLLOW_modifierList_in_synpred51_Java6056)
        self.modifierList()

        self._state.following.pop()

        # Java.g:388:9: ( ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI ) | type interfaceFieldDeclaratorList SEMI )
        alt188 = 2
        LA188 = self.input.LA(1)
        if LA188 == LESS_THAN or LA188 == VOID:
            alt188 = 1
        elif LA188 == BOOLEAN or LA188 == BYTE or LA188 == CHAR or LA188 == DOUBLE or LA188 == FLOAT or LA188 == INT or LA188 == LONG or LA188 == SHORT:
            LA188_2 = self.input.LA(2)

            if (self.synpred50_Java()) :
                alt188 = 1
            elif (True) :
                alt188 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 188, 2, self.input)

                raise nvae


        elif LA188 == IDENT:
            LA188_3 = self.input.LA(2)

            if (self.synpred50_Java()) :
                alt188 = 1
            elif (True) :
                alt188 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 188, 3, self.input)

                raise nvae


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 188, 0, self.input)

            raise nvae


        if alt188 == 1:
            # Java.g:388:13: ( genericTypeParameterList )? ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
            pass 
            # Java.g:388:13: ( genericTypeParameterList )?
            alt183 = 2
            LA183_0 = self.input.LA(1)

            if (LA183_0 == LESS_THAN) :
                alt183 = 1
            if alt183 == 1:
                # Java.g:388:13: genericTypeParameterList
                pass 
                self._state.following.append(self.FOLLOW_genericTypeParameterList_in_synpred51_Java6070)
                self.genericTypeParameterList()

                self._state.following.pop()




            # Java.g:389:13: ( type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI | VOID IDENT formalParameterList ( throwsClause )? SEMI )
            alt187 = 2
            LA187_0 = self.input.LA(1)

            if (LA187_0 == BOOLEAN or LA187_0 == BYTE or LA187_0 == CHAR or LA187_0 == DOUBLE or LA187_0 == FLOAT or LA187_0 == IDENT or LA187_0 == INT or LA187_0 == LONG or LA187_0 == SHORT) :
                alt187 = 1
            elif (LA187_0 == VOID) :
                alt187 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 187, 0, self.input)

                raise nvae


            if alt187 == 1:
                # Java.g:389:17: type IDENT formalParameterList ( arrayDeclaratorList )? ( throwsClause )? SEMI
                pass 
                self._state.following.append(self.FOLLOW_type_in_synpred51_Java6089)
                self.type()

                self._state.following.pop()

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred51_Java6091)

                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred51_Java6093)
                self.formalParameterList()

                self._state.following.pop()

                # Java.g:389:48: ( arrayDeclaratorList )?
                alt184 = 2
                LA184_0 = self.input.LA(1)

                if (LA184_0 == LBRACK) :
                    alt184 = 1
                if alt184 == 1:
                    # Java.g:389:48: arrayDeclaratorList
                    pass 
                    self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred51_Java6095)
                    self.arrayDeclaratorList()

                    self._state.following.pop()




                # Java.g:389:69: ( throwsClause )?
                alt185 = 2
                LA185_0 = self.input.LA(1)

                if (LA185_0 == THROWS) :
                    alt185 = 1
                if alt185 == 1:
                    # Java.g:389:69: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred51_Java6098)
                    self.throwsClause()

                    self._state.following.pop()




                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred51_Java6101)


            elif alt187 == 2:
                # Java.g:391:17: VOID IDENT formalParameterList ( throwsClause )? SEMI
                pass 
                self.match(self.input, VOID, self.FOLLOW_VOID_in_synpred51_Java6159)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred51_Java6161)

                self._state.following.append(self.FOLLOW_formalParameterList_in_synpred51_Java6163)
                self.formalParameterList()

                self._state.following.pop()

                # Java.g:391:48: ( throwsClause )?
                alt186 = 2
                LA186_0 = self.input.LA(1)

                if (LA186_0 == THROWS) :
                    alt186 = 1
                if alt186 == 1:
                    # Java.g:391:48: throwsClause
                    pass 
                    self._state.following.append(self.FOLLOW_throwsClause_in_synpred51_Java6165)
                    self.throwsClause()

                    self._state.following.pop()




                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred51_Java6168)





        elif alt188 == 2:
            # Java.g:394:13: type interfaceFieldDeclaratorList SEMI
            pass 
            self._state.following.append(self.FOLLOW_type_in_synpred51_Java6231)
            self.type()

            self._state.following.pop()

            self._state.following.append(self.FOLLOW_interfaceFieldDeclaratorList_in_synpred51_Java6233)
            self.interfaceFieldDeclaratorList()

            self._state.following.pop()

            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred51_Java6235)






    # $ANTLR end "synpred51_Java"



    # $ANTLR start "synpred52_Java"
    def synpred52_Java_fragment(self, ):
        # Java.g:397:9: ( typeDeclaration )
        # Java.g:397:9: typeDeclaration
        pass 
        self._state.following.append(self.FOLLOW_typeDeclaration_in_synpred52_Java6280)
        self.typeDeclaration()

        self._state.following.pop()



    # $ANTLR end "synpred52_Java"



    # $ANTLR start "synpred58_Java"
    def synpred58_Java_fragment(self, ):
        # Java.g:436:9: ( arrayDeclarator )
        # Java.g:436:9: arrayDeclarator
        pass 
        self._state.following.append(self.FOLLOW_arrayDeclarator_in_synpred58_Java6582)
        self.arrayDeclarator()

        self._state.following.pop()



    # $ANTLR end "synpred58_Java"



    # $ANTLR start "synpred76_Java"
    def synpred76_Java_fragment(self, ):
        # Java.g:485:23: ( arrayDeclaratorList )
        # Java.g:485:23: arrayDeclaratorList
        pass 
        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred76_Java6983)
        self.arrayDeclaratorList()

        self._state.following.pop()



    # $ANTLR end "synpred76_Java"



    # $ANTLR start "synpred77_Java"
    def synpred77_Java_fragment(self, ):
        # Java.g:490:28: ( arrayDeclaratorList )
        # Java.g:490:28: arrayDeclaratorList
        pass 
        self._state.following.append(self.FOLLOW_arrayDeclaratorList_in_synpred77_Java7032)
        self.arrayDeclaratorList()

        self._state.following.pop()



    # $ANTLR end "synpred77_Java"



    # $ANTLR start "synpred79_Java"
    def synpred79_Java_fragment(self, ):
        # Java.g:500:20: ( DOT typeIdent )
        # Java.g:500:20: DOT typeIdent
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred79_Java7117)

        self._state.following.append(self.FOLLOW_typeIdent_in_synpred79_Java7119)
        self.typeIdent()

        self._state.following.pop()



    # $ANTLR end "synpred79_Java"



    # $ANTLR start "synpred90_Java"
    def synpred90_Java_fragment(self, ):
        # Java.g:529:40: ( COMMA genericTypeArgument )
        # Java.g:529:40: COMMA genericTypeArgument
        pass 
        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred90_Java7344)

        self._state.following.append(self.FOLLOW_genericTypeArgument_in_synpred90_Java7346)
        self.genericTypeArgument()

        self._state.following.pop()



    # $ANTLR end "synpred90_Java"



    # $ANTLR start "synpred92_Java"
    def synpred92_Java_fragment(self, ):
        # Java.g:535:18: ( genericWildcardBoundType )
        # Java.g:535:18: genericWildcardBoundType
        pass 
        self._state.following.append(self.FOLLOW_genericWildcardBoundType_in_synpred92_Java7400)
        self.genericWildcardBoundType()

        self._state.following.pop()



    # $ANTLR end "synpred92_Java"



    # $ANTLR start "synpred97_Java"
    def synpred97_Java_fragment(self, ):
        # Java.g:560:42: ( COMMA formalParameterStandardDecl )
        # Java.g:560:42: COMMA formalParameterStandardDecl
        pass 
        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred97_Java7618)

        self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_synpred97_Java7620)
        self.formalParameterStandardDecl()

        self._state.following.pop()



    # $ANTLR end "synpred97_Java"



    # $ANTLR start "synpred99_Java"
    def synpred99_Java_fragment(self, ):
        # Java.g:560:13: ( formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )? )
        # Java.g:560:13: formalParameterStandardDecl ( COMMA formalParameterStandardDecl )* ( COMMA formalParameterVarArgDecl )?
        pass 
        self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_synpred99_Java7615)
        self.formalParameterStandardDecl()

        self._state.following.pop()

        # Java.g:560:41: ( COMMA formalParameterStandardDecl )*
        while True: #loop191
            alt191 = 2
            LA191_0 = self.input.LA(1)

            if (LA191_0 == COMMA) :
                LA191_1 = self.input.LA(2)

                if (self.synpred97_Java()) :
                    alt191 = 1




            if alt191 == 1:
                # Java.g:560:42: COMMA formalParameterStandardDecl
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred99_Java7618)

                self._state.following.append(self.FOLLOW_formalParameterStandardDecl_in_synpred99_Java7620)
                self.formalParameterStandardDecl()

                self._state.following.pop()


            else:
                break #loop191


        # Java.g:560:78: ( COMMA formalParameterVarArgDecl )?
        alt192 = 2
        LA192_0 = self.input.LA(1)

        if (LA192_0 == COMMA) :
            alt192 = 1
        if alt192 == 1:
            # Java.g:560:79: COMMA formalParameterVarArgDecl
            pass 
            self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred99_Java7625)

            self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_synpred99_Java7627)
            self.formalParameterVarArgDecl()

            self._state.following.pop()






    # $ANTLR end "synpred99_Java"



    # $ANTLR start "synpred100_Java"
    def synpred100_Java_fragment(self, ):
        # Java.g:563:13: ( formalParameterVarArgDecl )
        # Java.g:563:13: formalParameterVarArgDecl
        pass 
        self._state.following.append(self.FOLLOW_formalParameterVarArgDecl_in_synpred100_Java7684)
        self.formalParameterVarArgDecl()

        self._state.following.pop()



    # $ANTLR end "synpred100_Java"



    # $ANTLR start "synpred101_Java"
    def synpred101_Java_fragment(self, ):
        # Java.g:584:13: ( DOT ident= IDENT )
        # Java.g:584:13: DOT ident= IDENT
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred101_Java7929)

        ident = self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred101_Java7933)



    # $ANTLR end "synpred101_Java"



    # $ANTLR start "synpred102_Java"
    def synpred102_Java_fragment(self, ):
        # Java.g:591:9: ( annotation )
        # Java.g:591:9: annotation
        pass 
        self._state.following.append(self.FOLLOW_annotation_in_synpred102_Java7986)
        self.annotation()

        self._state.following.pop()



    # $ANTLR end "synpred102_Java"



    # $ANTLR start "synpred114_Java"
    def synpred114_Java_fragment(self, ):
        # Java.g:642:9: ( modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI | classFieldDeclaratorList SEMI ) )
        # Java.g:642:9: modifierList type ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI | classFieldDeclaratorList SEMI )
        pass 
        self._state.following.append(self.FOLLOW_modifierList_in_synpred114_Java8440)
        self.modifierList()

        self._state.following.pop()

        self._state.following.append(self.FOLLOW_type_in_synpred114_Java8442)
        self.type()

        self._state.following.pop()

        # Java.g:643:9: ( IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI | classFieldDeclaratorList SEMI )
        alt197 = 2
        LA197_0 = self.input.LA(1)

        if (LA197_0 == IDENT) :
            LA197_1 = self.input.LA(2)

            if (LA197_1 == LPAREN) :
                alt197 = 1
            elif (LA197_1 == ASSIGN or LA197_1 == COMMA or LA197_1 == LBRACK or LA197_1 == SEMI) :
                alt197 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 197, 1, self.input)

                raise nvae


        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 197, 0, self.input)

            raise nvae


        if alt197 == 1:
            # Java.g:643:13: IDENT LPAREN RPAREN ( annotationDefaultValue )? SEMI
            pass 
            self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred114_Java8456)

            self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred114_Java8458)

            self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred114_Java8460)

            # Java.g:643:33: ( annotationDefaultValue )?
            alt196 = 2
            LA196_0 = self.input.LA(1)

            if (LA196_0 == DEFAULT) :
                alt196 = 1
            if alt196 == 1:
                # Java.g:643:33: annotationDefaultValue
                pass 
                self._state.following.append(self.FOLLOW_annotationDefaultValue_in_synpred114_Java8462)
                self.annotationDefaultValue()

                self._state.following.pop()




            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred114_Java8465)


        elif alt197 == 2:
            # Java.g:645:13: classFieldDeclaratorList SEMI
            pass 
            self._state.following.append(self.FOLLOW_classFieldDeclaratorList_in_synpred114_Java8507)
            self.classFieldDeclaratorList()

            self._state.following.pop()

            self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred114_Java8509)






    # $ANTLR end "synpred114_Java"



    # $ANTLR start "synpred116_Java"
    def synpred116_Java_fragment(self, ):
        # Java.g:663:9: ( localVariableDeclaration SEMI )
        # Java.g:663:9: localVariableDeclaration SEMI
        pass 
        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_synpred116_Java8644)
        self.localVariableDeclaration()

        self._state.following.pop()

        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred116_Java8646)



    # $ANTLR end "synpred116_Java"



    # $ANTLR start "synpred117_Java"
    def synpred117_Java_fragment(self, ):
        # Java.g:664:9: ( typeDeclaration )
        # Java.g:664:9: typeDeclaration
        pass 
        self._state.following.append(self.FOLLOW_typeDeclaration_in_synpred117_Java8657)
        self.typeDeclaration()

        self._state.following.pop()



    # $ANTLR end "synpred117_Java"



    # $ANTLR start "synpred121_Java"
    def synpred121_Java_fragment(self, ):
        # Java.g:681:13: ( ELSE elseStat= statement )
        # Java.g:681:13: ELSE elseStat= statement
        pass 
        self.match(self.input, ELSE, self.FOLLOW_ELSE_in_synpred121_Java8955)

        self._state.following.append(self.FOLLOW_statement_in_synpred121_Java8959)
        elseStat = self.statement()

        self._state.following.pop()



    # $ANTLR end "synpred121_Java"



    # $ANTLR start "synpred123_Java"
    def synpred123_Java_fragment(self, ):
        # Java.g:685:13: ( forInit SEMI forCondition SEMI forUpdater RPAREN statement )
        # Java.g:685:13: forInit SEMI forCondition SEMI forUpdater RPAREN statement
        pass 
        self._state.following.append(self.FOLLOW_forInit_in_synpred123_Java9142)
        self.forInit()

        self._state.following.pop()

        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred123_Java9144)

        self._state.following.append(self.FOLLOW_forCondition_in_synpred123_Java9146)
        self.forCondition()

        self._state.following.pop()

        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_synpred123_Java9148)

        self._state.following.append(self.FOLLOW_forUpdater_in_synpred123_Java9150)
        self.forUpdater()

        self._state.following.pop()

        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred123_Java9152)

        self._state.following.append(self.FOLLOW_statement_in_synpred123_Java9154)
        self.statement()

        self._state.following.pop()



    # $ANTLR end "synpred123_Java"



    # $ANTLR start "synpred143_Java"
    def synpred143_Java_fragment(self, ):
        # Java.g:723:9: ( switchCaseLabel )
        # Java.g:723:9: switchCaseLabel
        pass 
        self._state.following.append(self.FOLLOW_switchCaseLabel_in_synpred143_Java10121)
        self.switchCaseLabel()

        self._state.following.pop()



    # $ANTLR end "synpred143_Java"



    # $ANTLR start "synpred146_Java"
    def synpred146_Java_fragment(self, ):
        # Java.g:735:9: ( localVariableDeclaration )
        # Java.g:735:9: localVariableDeclaration
        pass 
        self._state.following.append(self.FOLLOW_localVariableDeclaration_in_synpred146_Java10211)
        self.localVariableDeclaration()

        self._state.following.pop()



    # $ANTLR end "synpred146_Java"



    # $ANTLR start "synpred147_Java"
    def synpred147_Java_fragment(self, ):
        # Java.g:736:9: ( expressionList )
        # Java.g:736:9: expressionList
        pass 
        self._state.following.append(self.FOLLOW_expressionList_in_synpred147_Java10233)
        self.expressionList()

        self._state.following.pop()



    # $ANTLR end "synpred147_Java"



    # $ANTLR start "synpred190_Java"
    def synpred190_Java_fragment(self, ):
        # Java.g:872:9: ( LPAREN type RPAREN unaryExpression )
        # Java.g:872:9: LPAREN type RPAREN unaryExpression
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred190_Java11766)

        self._state.following.append(self.FOLLOW_type_in_synpred190_Java11768)
        self.type()

        self._state.following.pop()

        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred190_Java11770)

        self._state.following.append(self.FOLLOW_unaryExpression_in_synpred190_Java11772)
        self.unaryExpression()

        self._state.following.pop()



    # $ANTLR end "synpred190_Java"



    # $ANTLR start "synpred218_Java"
    def synpred218_Java_fragment(self, ):
        # Java.g:940:13: ( ( arrayDeclarator )+ ( DOT CLASS ) )
        # Java.g:940:13: ( arrayDeclarator )+ ( DOT CLASS )
        pass 
        # Java.g:940:13: ( arrayDeclarator )+
        cnt220 = 0
        while True: #loop220
            alt220 = 2
            LA220_0 = self.input.LA(1)

            if (LA220_0 == LBRACK) :
                alt220 = 1


            if alt220 == 1:
                # Java.g:940:17: arrayDeclarator
                pass 
                self._state.following.append(self.FOLLOW_arrayDeclarator_in_synpred218_Java13673)
                self.arrayDeclarator()

                self._state.following.pop()


            else:
                if cnt220 >= 1:
                    break #loop220

                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                eee = EarlyExitException(220, self.input)
                raise eee

            cnt220 += 1


        # Java.g:942:13: ( DOT CLASS )
        # Java.g:942:17: DOT CLASS
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred218_Java13741)

        self.match(self.input, CLASS, self.FOLLOW_CLASS_in_synpred218_Java13743)






    # $ANTLR end "synpred218_Java"



    # $ANTLR start "synpred226_Java"
    def synpred226_Java_fragment(self, ):
        # Java.g:945:13: (outerDot= DOT ( CLASS | genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments ) | THIS |Super= SUPER arguments | innerNewExpression ) )
        # Java.g:945:13: outerDot= DOT ( CLASS | genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments ) | THIS |Super= SUPER arguments | innerNewExpression )
        pass 
        outerDot = self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred226_Java13874)

        # Java.g:946:13: ( CLASS | genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments ) | THIS |Super= SUPER arguments | innerNewExpression )
        alt223 = 5
        LA223 = self.input.LA(1)
        if LA223 == CLASS:
            alt223 = 1
        elif LA223 == LESS_THAN:
            alt223 = 2
        elif LA223 == THIS:
            alt223 = 3
        elif LA223 == SUPER:
            alt223 = 4
        elif LA223 == NEW:
            alt223 = 5
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed


            nvae = NoViableAltException("", 223, 0, self.input)

            raise nvae


        if alt223 == 1:
            # Java.g:946:17: CLASS
            pass 
            self.match(self.input, CLASS, self.FOLLOW_CLASS_in_synpred226_Java13892)


        elif alt223 == 2:
            # Java.g:947:17: genericTypeArgumentListSimplified (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments )
            pass 
            self._state.following.append(self.FOLLOW_genericTypeArgumentListSimplified_in_synpred226_Java13955)
            self.genericTypeArgumentListSimplified()

            self._state.following.pop()

            # Java.g:948:17: (Super= SUPER arguments | SUPER innerDot= DOT IDENT arguments | IDENT arguments )
            alt222 = 3
            LA222_0 = self.input.LA(1)

            if (LA222_0 == SUPER) :
                LA222_1 = self.input.LA(2)

                if (LA222_1 == DOT) :
                    alt222 = 2
                elif (LA222_1 == LPAREN) :
                    alt222 = 1
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 222, 1, self.input)

                    raise nvae


            elif (LA222_0 == IDENT) :
                alt222 = 3
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 222, 0, self.input)

                raise nvae


            if alt222 == 1:
                # Java.g:948:21: Super= SUPER arguments
                pass 
                Super = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_synpred226_Java13980)

                self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java13982)
                self.arguments()

                self._state.following.pop()


            elif alt222 == 2:
                # Java.g:949:21: SUPER innerDot= DOT IDENT arguments
                pass 
                self.match(self.input, SUPER, self.FOLLOW_SUPER_in_synpred226_Java14032)

                innerDot = self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred226_Java14036)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred226_Java14038)

                self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java14040)
                self.arguments()

                self._state.following.pop()


            elif alt222 == 3:
                # Java.g:950:21: IDENT arguments
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_synpred226_Java14090)

                self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java14092)
                self.arguments()

                self._state.following.pop()





        elif alt223 == 3:
            # Java.g:952:17: THIS
            pass 
            self.match(self.input, THIS, self.FOLLOW_THIS_in_synpred226_Java14167)


        elif alt223 == 4:
            # Java.g:953:17: Super= SUPER arguments
            pass 
            Super = self.match(self.input, SUPER, self.FOLLOW_SUPER_in_synpred226_Java14233)

            self._state.following.append(self.FOLLOW_arguments_in_synpred226_Java14235)
            self.arguments()

            self._state.following.pop()


        elif alt223 == 5:
            # Java.g:954:17: innerNewExpression
            pass 
            self._state.following.append(self.FOLLOW_innerNewExpression_in_synpred226_Java14283)
            self.innerNewExpression()

            self._state.following.pop()






    # $ANTLR end "synpred226_Java"



    # $ANTLR start "synpred234_Java"
    def synpred234_Java_fragment(self, ):
        # Java.g:979:37: ( LBRACK expression RBRACK )
        # Java.g:979:37: LBRACK expression RBRACK
        pass 
        self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_synpred234_Java14684)

        self._state.following.append(self.FOLLOW_expression_in_synpred234_Java14687)
        self.expression()

        self._state.following.pop()

        self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_synpred234_Java14689)



    # $ANTLR end "synpred234_Java"




    def synpred226_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred226_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred43_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred43_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred121_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred121_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred76_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred76_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred114_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred114_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred116_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred116_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred97_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred97_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred102_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred102_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred218_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred218_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred117_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred117_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred79_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred79_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred101_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred101_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred16_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred16_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred147_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred147_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred42_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred42_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred143_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred143_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred190_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred190_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred77_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred77_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred51_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred51_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred100_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred100_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred52_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred52_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred123_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred123_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred32_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred32_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred92_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred92_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred90_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred90_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred58_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred58_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred50_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred50_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred14_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred14_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred99_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred99_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred234_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred234_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred146_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred146_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred44_Java(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred44_Java_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_compilationUnit_in_javaSource4489 = frozenset([1])
    FOLLOW_annotationList_in_compilationUnit4525 = frozenset([1, 4, 22, 35, 56, 66, 90, 95, 118, 127, 135, 136, 137, 144, 152, 154, 160, 166, 178])
    FOLLOW_packageDeclaration_in_compilationUnit4536 = frozenset([1, 4, 22, 35, 56, 66, 90, 95, 118, 135, 136, 137, 144, 152, 154, 160, 166, 178])
    FOLLOW_importDeclaration_in_compilationUnit4548 = frozenset([1, 4, 22, 35, 56, 66, 90, 95, 118, 135, 136, 137, 144, 152, 154, 160, 166, 178])
    FOLLOW_typeDecls_in_compilationUnit4560 = frozenset([1, 4, 22, 35, 56, 66, 95, 118, 135, 136, 137, 144, 152, 154, 160, 166, 178])
    FOLLOW_typeDeclaration_in_typeDecls4580 = frozenset([1])
    FOLLOW_SEMI_in_typeDecls4590 = frozenset([1])
    FOLLOW_PACKAGE_in_packageDeclaration4610 = frozenset([86])
    FOLLOW_qualifiedIdentifier_in_packageDeclaration4613 = frozenset([144])
    FOLLOW_SEMI_in_packageDeclaration4615 = frozenset([1])
    FOLLOW_IMPORT_in_importDeclaration4641 = frozenset([86, 152])
    FOLLOW_STATIC_in_importDeclaration4644 = frozenset([86])
    FOLLOW_qualifiedIdentifier_in_importDeclaration4647 = frozenset([52, 144])
    FOLLOW_DOTSTAR_in_importDeclaration4649 = frozenset([144])
    FOLLOW_SEMI_in_importDeclaration4652 = frozenset([1])
    FOLLOW_modifierList_in_typeDeclaration4676 = frozenset([22, 35, 56, 95])
    FOLLOW_classTypeDeclaration_in_typeDeclaration4691 = frozenset([1])
    FOLLOW_interfaceTypeDeclaration_in_typeDeclaration4706 = frozenset([1])
    FOLLOW_enumTypeDeclaration_in_typeDeclaration4721 = frozenset([1])
    FOLLOW_annotationTypeDeclaration_in_typeDeclaration4736 = frozenset([1])
    FOLLOW_CLASS_in_classTypeDeclaration4771 = frozenset([86])
    FOLLOW_IDENT_in_classTypeDeclaration4773 = frozenset([62, 88, 102, 104])
    FOLLOW_genericTypeParameterList_in_classTypeDeclaration4775 = frozenset([62, 88, 102])
    FOLLOW_classExtendsClause_in_classTypeDeclaration4778 = frozenset([88, 102])
    FOLLOW_implementsClause_in_classTypeDeclaration4781 = frozenset([102])
    FOLLOW_classBody_in_classTypeDeclaration4784 = frozenset([1])
    FOLLOW_EXTENDS_in_classExtendsClause4837 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_classExtendsClause4839 = frozenset([1])
    FOLLOW_EXTENDS_in_interfaceExtendsClause4883 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_typeList_in_interfaceExtendsClause4885 = frozenset([1])
    FOLLOW_IMPLEMENTS_in_implementsClause4929 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_typeList_in_implementsClause4931 = frozenset([1])
    FOLLOW_LESS_THAN_in_genericTypeParameterList4976 = frozenset([86])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList4978 = frozenset([23, 41, 83, 147])
    FOLLOW_COMMA_in_genericTypeParameterList4981 = frozenset([86])
    FOLLOW_genericTypeParameter_in_genericTypeParameterList4983 = frozenset([23, 41, 83, 147])
    FOLLOW_genericTypeListClosing_in_genericTypeParameterList4987 = frozenset([1])
    FOLLOW_GREATER_THAN_in_genericTypeListClosing5102 = frozenset([1])
    FOLLOW_SHIFT_RIGHT_in_genericTypeListClosing5112 = frozenset([1])
    FOLLOW_BIT_SHIFT_RIGHT_in_genericTypeListClosing5122 = frozenset([1])
    FOLLOW_IDENT_in_genericTypeParameter5150 = frozenset([1, 62])
    FOLLOW_bound_in_genericTypeParameter5152 = frozenset([1])
    FOLLOW_EXTENDS_in_bound5198 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_bound5200 = frozenset([1, 5])
    FOLLOW_AND_in_bound5203 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_bound5205 = frozenset([1, 5])
    FOLLOW_ENUM_in_enumTypeDeclaration5246 = frozenset([86])
    FOLLOW_IDENT_in_enumTypeDeclaration5248 = frozenset([88, 102])
    FOLLOW_implementsClause_in_enumTypeDeclaration5250 = frozenset([102])
    FOLLOW_enumBody_in_enumTypeDeclaration5253 = frozenset([1])
    FOLLOW_LCURLY_in_enumBody5300 = frozenset([22, 86])
    FOLLOW_enumScopeDeclarations_in_enumBody5302 = frozenset([141])
    FOLLOW_RCURLY_in_enumBody5304 = frozenset([1])
    FOLLOW_enumConstants_in_enumScopeDeclarations5341 = frozenset([1, 41, 144])
    FOLLOW_COMMA_in_enumScopeDeclarations5344 = frozenset([1, 144])
    FOLLOW_enumClassScopeDeclarations_in_enumScopeDeclarations5349 = frozenset([1])
    FOLLOW_SEMI_in_enumClassScopeDeclarations5369 = frozenset([1, 4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 102, 104, 110, 118, 135, 136, 137, 144, 149, 152, 154, 160, 166, 176, 178])
    FOLLOW_classScopeDeclarations_in_enumClassScopeDeclarations5371 = frozenset([1, 4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 102, 104, 110, 118, 135, 136, 137, 144, 149, 152, 154, 160, 166, 176, 178])
    FOLLOW_enumConstant_in_enumConstants5410 = frozenset([1, 41])
    FOLLOW_COMMA_in_enumConstants5413 = frozenset([22, 86])
    FOLLOW_enumConstant_in_enumConstants5416 = frozenset([1, 41])
    FOLLOW_annotationList_in_enumConstant5441 = frozenset([86])
    FOLLOW_IDENT_in_enumConstant5443 = frozenset([1, 102, 111])
    FOLLOW_arguments_in_enumConstant5446 = frozenset([1, 102])
    FOLLOW_classBody_in_enumConstant5449 = frozenset([1])
    FOLLOW_INTERFACE_in_interfaceTypeDeclaration5474 = frozenset([86])
    FOLLOW_IDENT_in_interfaceTypeDeclaration5476 = frozenset([62, 102, 104])
    FOLLOW_genericTypeParameterList_in_interfaceTypeDeclaration5478 = frozenset([62, 102])
    FOLLOW_interfaceExtendsClause_in_interfaceTypeDeclaration5481 = frozenset([102])
    FOLLOW_interfaceBody_in_interfaceTypeDeclaration5484 = frozenset([1])
    FOLLOW_type_in_typeList5534 = frozenset([1, 41])
    FOLLOW_COMMA_in_typeList5537 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_typeList5540 = frozenset([1, 41])
    FOLLOW_LCURLY_in_classBody5565 = frozenset([4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 102, 104, 110, 118, 135, 136, 137, 141, 144, 149, 152, 154, 160, 166, 176, 178])
    FOLLOW_classScopeDeclarations_in_classBody5567 = frozenset([4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 102, 104, 110, 118, 135, 136, 137, 141, 144, 149, 152, 154, 160, 166, 176, 178])
    FOLLOW_RCURLY_in_classBody5570 = frozenset([1])
    FOLLOW_LCURLY_in_interfaceBody5612 = frozenset([4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 104, 110, 118, 135, 136, 137, 141, 144, 149, 152, 154, 160, 166, 176, 178])
    FOLLOW_interfaceScopeDeclarations_in_interfaceBody5614 = frozenset([4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 104, 110, 118, 135, 136, 137, 141, 144, 149, 152, 154, 160, 166, 176, 178])
    FOLLOW_RCURLY_in_interfaceBody5617 = frozenset([1])
    FOLLOW_block_in_classScopeDeclarations5655 = frozenset([1])
    FOLLOW_STATIC_in_classScopeDeclarations5684 = frozenset([102])
    FOLLOW_block_in_classScopeDeclarations5686 = frozenset([1])
    FOLLOW_modifierList_in_classScopeDeclarations5709 = frozenset([26, 28, 33, 53, 68, 86, 93, 104, 110, 149, 176])
    FOLLOW_genericTypeParameterList_in_classScopeDeclarations5723 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149, 176])
    FOLLOW_type_in_classScopeDeclarations5742 = frozenset([86])
    FOLLOW_IDENT_in_classScopeDeclarations5744 = frozenset([111])
    FOLLOW_formalParameterList_in_classScopeDeclarations5746 = frozenset([101, 102, 144, 164])
    FOLLOW_arrayDeclaratorList_in_classScopeDeclarations5748 = frozenset([102, 144, 164])
    FOLLOW_throwsClause_in_classScopeDeclarations5751 = frozenset([102, 144])
    FOLLOW_block_in_classScopeDeclarations5755 = frozenset([1])
    FOLLOW_SEMI_in_classScopeDeclarations5759 = frozenset([1])
    FOLLOW_VOID_in_classScopeDeclarations5821 = frozenset([86])
    FOLLOW_IDENT_in_classScopeDeclarations5823 = frozenset([111])
    FOLLOW_formalParameterList_in_classScopeDeclarations5825 = frozenset([102, 144, 164])
    FOLLOW_throwsClause_in_classScopeDeclarations5827 = frozenset([102, 144])
    FOLLOW_block_in_classScopeDeclarations5831 = frozenset([1])
    FOLLOW_SEMI_in_classScopeDeclarations5835 = frozenset([1])
    FOLLOW_IDENT_in_classScopeDeclarations5894 = frozenset([111])
    FOLLOW_formalParameterList_in_classScopeDeclarations5896 = frozenset([102, 164])
    FOLLOW_throwsClause_in_classScopeDeclarations5898 = frozenset([102])
    FOLLOW_block_in_classScopeDeclarations5901 = frozenset([1])
    FOLLOW_type_in_classScopeDeclarations5965 = frozenset([86])
    FOLLOW_classFieldDeclaratorList_in_classScopeDeclarations5967 = frozenset([144])
    FOLLOW_SEMI_in_classScopeDeclarations5969 = frozenset([1])
    FOLLOW_typeDeclaration_in_classScopeDeclarations6014 = frozenset([1])
    FOLLOW_SEMI_in_classScopeDeclarations6024 = frozenset([1])
    FOLLOW_modifierList_in_interfaceScopeDeclarations6056 = frozenset([26, 28, 33, 53, 68, 86, 93, 104, 110, 149, 176])
    FOLLOW_genericTypeParameterList_in_interfaceScopeDeclarations6070 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149, 176])
    FOLLOW_type_in_interfaceScopeDeclarations6089 = frozenset([86])
    FOLLOW_IDENT_in_interfaceScopeDeclarations6091 = frozenset([111])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations6093 = frozenset([101, 144, 164])
    FOLLOW_arrayDeclaratorList_in_interfaceScopeDeclarations6095 = frozenset([144, 164])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations6098 = frozenset([144])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6101 = frozenset([1])
    FOLLOW_VOID_in_interfaceScopeDeclarations6159 = frozenset([86])
    FOLLOW_IDENT_in_interfaceScopeDeclarations6161 = frozenset([111])
    FOLLOW_formalParameterList_in_interfaceScopeDeclarations6163 = frozenset([144, 164])
    FOLLOW_throwsClause_in_interfaceScopeDeclarations6165 = frozenset([144])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6168 = frozenset([1])
    FOLLOW_type_in_interfaceScopeDeclarations6231 = frozenset([86])
    FOLLOW_interfaceFieldDeclaratorList_in_interfaceScopeDeclarations6233 = frozenset([144])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6235 = frozenset([1])
    FOLLOW_typeDeclaration_in_interfaceScopeDeclarations6280 = frozenset([1])
    FOLLOW_SEMI_in_interfaceScopeDeclarations6290 = frozenset([1])
    FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6310 = frozenset([1, 41])
    FOLLOW_COMMA_in_classFieldDeclaratorList6313 = frozenset([86])
    FOLLOW_classFieldDeclarator_in_classFieldDeclaratorList6315 = frozenset([1, 41])
    FOLLOW_variableDeclaratorId_in_classFieldDeclarator6354 = frozenset([1, 21])
    FOLLOW_ASSIGN_in_classFieldDeclarator6357 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_variableInitializer_in_classFieldDeclarator6359 = frozenset([1])
    FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6404 = frozenset([1, 41])
    FOLLOW_COMMA_in_interfaceFieldDeclaratorList6407 = frozenset([86])
    FOLLOW_interfaceFieldDeclarator_in_interfaceFieldDeclaratorList6409 = frozenset([1, 41])
    FOLLOW_variableDeclaratorId_in_interfaceFieldDeclarator6448 = frozenset([21])
    FOLLOW_ASSIGN_in_interfaceFieldDeclarator6450 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_variableInitializer_in_interfaceFieldDeclarator6452 = frozenset([1])
    FOLLOW_IDENT_in_variableDeclaratorId6494 = frozenset([1, 101])
    FOLLOW_arrayDeclaratorList_in_variableDeclaratorId6497 = frozenset([1])
    FOLLOW_arrayInitializer_in_variableInitializer6517 = frozenset([1])
    FOLLOW_expression_in_variableInitializer6527 = frozenset([1])
    FOLLOW_LBRACK_in_arrayDeclarator6546 = frozenset([140])
    FOLLOW_RBRACK_in_arrayDeclarator6548 = frozenset([1])
    FOLLOW_arrayDeclarator_in_arrayDeclaratorList6582 = frozenset([1, 101])
    FOLLOW_LCURLY_in_arrayInitializer6627 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 141, 149, 155, 156, 161, 167, 176])
    FOLLOW_variableInitializer_in_arrayInitializer6630 = frozenset([41, 141])
    FOLLOW_COMMA_in_arrayInitializer6633 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_variableInitializer_in_arrayInitializer6635 = frozenset([41, 141])
    FOLLOW_COMMA_in_arrayInitializer6639 = frozenset([141])
    FOLLOW_RCURLY_in_arrayInitializer6644 = frozenset([1])
    FOLLOW_THROWS_in_throwsClause6682 = frozenset([86])
    FOLLOW_qualifiedIdentList_in_throwsClause6684 = frozenset([1])
    FOLLOW_modifier_in_modifierList6721 = frozenset([1, 4, 22, 66, 118, 135, 136, 137, 152, 154, 160, 166, 178])
    FOLLOW_PUBLIC_in_modifier6762 = frozenset([1])
    FOLLOW_PROTECTED_in_modifier6772 = frozenset([1])
    FOLLOW_PRIVATE_in_modifier6782 = frozenset([1])
    FOLLOW_STATIC_in_modifier6792 = frozenset([1])
    FOLLOW_ABSTRACT_in_modifier6802 = frozenset([1])
    FOLLOW_NATIVE_in_modifier6812 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_modifier6822 = frozenset([1])
    FOLLOW_TRANSIENT_in_modifier6832 = frozenset([1])
    FOLLOW_VOLATILE_in_modifier6842 = frozenset([1])
    FOLLOW_STRICTFP_in_modifier6852 = frozenset([1])
    FOLLOW_localModifier_in_modifier6862 = frozenset([1])
    FOLLOW_localModifier_in_localModifierList6881 = frozenset([1, 22, 66])
    FOLLOW_FINAL_in_localModifier6922 = frozenset([1])
    FOLLOW_annotation_in_localModifier6932 = frozenset([1])
    FOLLOW_simpleType_in_type6951 = frozenset([1])
    FOLLOW_objectType_in_type6961 = frozenset([1])
    FOLLOW_primitiveType_in_simpleType6981 = frozenset([1, 101])
    FOLLOW_arrayDeclaratorList_in_simpleType6983 = frozenset([1])
    FOLLOW_qualifiedTypeIdent_in_objectType7030 = frozenset([1, 101])
    FOLLOW_arrayDeclaratorList_in_objectType7032 = frozenset([1])
    FOLLOW_qualifiedTypeIdentSimplified_in_objectTypeSimplified7072 = frozenset([1, 101])
    FOLLOW_arrayDeclaratorList_in_objectTypeSimplified7074 = frozenset([1])
    FOLLOW_typeIdent_in_qualifiedTypeIdent7114 = frozenset([1, 51])
    FOLLOW_DOT_in_qualifiedTypeIdent7117 = frozenset([86])
    FOLLOW_typeIdent_in_qualifiedTypeIdent7119 = frozenset([1, 51])
    FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7159 = frozenset([1, 51])
    FOLLOW_DOT_in_qualifiedTypeIdentSimplified7162 = frozenset([86])
    FOLLOW_typeIdentSimplified_in_qualifiedTypeIdentSimplified7164 = frozenset([1, 51])
    FOLLOW_IDENT_in_typeIdent7204 = frozenset([1, 104])
    FOLLOW_genericTypeArgumentList_in_typeIdent7207 = frozenset([1])
    FOLLOW_IDENT_in_typeIdentSimplified7227 = frozenset([1, 104])
    FOLLOW_genericTypeArgumentListSimplified_in_typeIdentSimplified7230 = frozenset([1])
    FOLLOW_LESS_THAN_in_genericTypeArgumentList7339 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 139, 149])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList7341 = frozenset([23, 41, 83, 147])
    FOLLOW_COMMA_in_genericTypeArgumentList7344 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 139, 149])
    FOLLOW_genericTypeArgument_in_genericTypeArgumentList7346 = frozenset([23, 41, 83, 147])
    FOLLOW_genericTypeListClosing_in_genericTypeArgumentList7350 = frozenset([1])
    FOLLOW_type_in_genericTypeArgument7388 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgument7398 = frozenset([1, 62, 156])
    FOLLOW_genericWildcardBoundType_in_genericTypeArgument7400 = frozenset([1])
    FOLLOW_set_in_genericWildcardBoundType7442 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_genericWildcardBoundType7451 = frozenset([1])
    FOLLOW_LESS_THAN_in_genericTypeArgumentListSimplified7470 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 139, 149])
    FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7472 = frozenset([23, 41, 83, 147])
    FOLLOW_COMMA_in_genericTypeArgumentListSimplified7475 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 139, 149])
    FOLLOW_genericTypeArgumentSimplified_in_genericTypeArgumentListSimplified7477 = frozenset([23, 41, 83, 147])
    FOLLOW_genericTypeListClosing_in_genericTypeArgumentListSimplified7481 = frozenset([1])
    FOLLOW_type_in_genericTypeArgumentSimplified7523 = frozenset([1])
    FOLLOW_QUESTION_in_genericTypeArgumentSimplified7533 = frozenset([1])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7556 = frozenset([1, 41])
    FOLLOW_COMMA_in_qualifiedIdentList7559 = frozenset([86])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentList7562 = frozenset([1, 41])
    FOLLOW_LPAREN_in_formalParameterList7587 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 143, 149])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList7615 = frozenset([41, 143])
    FOLLOW_COMMA_in_formalParameterList7618 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 149])
    FOLLOW_formalParameterStandardDecl_in_formalParameterList7620 = frozenset([41, 143])
    FOLLOW_COMMA_in_formalParameterList7625 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 149])
    FOLLOW_formalParameterVarArgDecl_in_formalParameterList7627 = frozenset([143])
    FOLLOW_formalParameterVarArgDecl_in_formalParameterList7684 = frozenset([143])
    FOLLOW_RPAREN_in_formalParameterList7761 = frozenset([1])
    FOLLOW_localModifierList_in_formalParameterStandardDecl7784 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_formalParameterStandardDecl7786 = frozenset([86])
    FOLLOW_variableDeclaratorId_in_formalParameterStandardDecl7788 = frozenset([1])
    FOLLOW_localModifierList_in_formalParameterVarArgDecl7832 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_formalParameterVarArgDecl7834 = frozenset([54])
    FOLLOW_ELLIPSIS_in_formalParameterVarArgDecl7836 = frozenset([86])
    FOLLOW_variableDeclaratorId_in_formalParameterVarArgDecl7838 = frozenset([1])
    FOLLOW_IDENT_in_qualifiedIdentifier7886 = frozenset([1, 51])
    FOLLOW_DOT_in_qualifiedIdentifier7929 = frozenset([86])
    FOLLOW_IDENT_in_qualifiedIdentifier7933 = frozenset([1, 51])
    FOLLOW_annotation_in_annotationList7986 = frozenset([1, 22])
    FOLLOW_AT_in_annotation8024 = frozenset([86])
    FOLLOW_qualifiedIdentifier_in_annotation8027 = frozenset([1, 111])
    FOLLOW_annotationInit_in_annotation8029 = frozenset([1])
    FOLLOW_LPAREN_in_annotationInit8053 = frozenset([22, 26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_annotationInitializers_in_annotationInit8055 = frozenset([143])
    FOLLOW_RPAREN_in_annotationInit8057 = frozenset([1])
    FOLLOW_annotationInitializer_in_annotationInitializers8094 = frozenset([1, 41])
    FOLLOW_COMMA_in_annotationInitializers8097 = frozenset([86])
    FOLLOW_annotationInitializer_in_annotationInitializers8099 = frozenset([1, 41])
    FOLLOW_annotationElementValue_in_annotationInitializers8129 = frozenset([1])
    FOLLOW_IDENT_in_annotationInitializer8170 = frozenset([21])
    FOLLOW_ASSIGN_in_annotationInitializer8173 = frozenset([22, 26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_annotationElementValue_in_annotationInitializer8176 = frozenset([1])
    FOLLOW_annotationElementValueExpression_in_annotationElementValue8199 = frozenset([1])
    FOLLOW_annotation_in_annotationElementValue8209 = frozenset([1])
    FOLLOW_annotationElementValueArrayInitializer_in_annotationElementValue8219 = frozenset([1])
    FOLLOW_conditionalExpression_in_annotationElementValueExpression8242 = frozenset([1])
    FOLLOW_LCURLY_in_annotationElementValueArrayInitializer8282 = frozenset([22, 26, 28, 33, 34, 41, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 141, 149, 155, 156, 161, 167, 176])
    FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8285 = frozenset([41, 141])
    FOLLOW_COMMA_in_annotationElementValueArrayInitializer8288 = frozenset([22, 26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_annotationElementValue_in_annotationElementValueArrayInitializer8290 = frozenset([41, 141])
    FOLLOW_COMMA_in_annotationElementValueArrayInitializer8297 = frozenset([141])
    FOLLOW_RCURLY_in_annotationElementValueArrayInitializer8301 = frozenset([1])
    FOLLOW_AT_in_annotationTypeDeclaration8344 = frozenset([95])
    FOLLOW_INTERFACE_in_annotationTypeDeclaration8346 = frozenset([86])
    FOLLOW_IDENT_in_annotationTypeDeclaration8348 = frozenset([102])
    FOLLOW_annotationBody_in_annotationTypeDeclaration8350 = frozenset([1])
    FOLLOW_LCURLY_in_annotationBody8393 = frozenset([4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 110, 118, 135, 136, 137, 141, 149, 152, 154, 160, 166, 178])
    FOLLOW_annotationScopeDeclarations_in_annotationBody8395 = frozenset([4, 22, 26, 28, 33, 35, 53, 56, 66, 68, 86, 93, 95, 110, 118, 135, 136, 137, 141, 149, 152, 154, 160, 166, 178])
    FOLLOW_RCURLY_in_annotationBody8398 = frozenset([1])
    FOLLOW_modifierList_in_annotationScopeDeclarations8440 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_annotationScopeDeclarations8442 = frozenset([86])
    FOLLOW_IDENT_in_annotationScopeDeclarations8456 = frozenset([111])
    FOLLOW_LPAREN_in_annotationScopeDeclarations8458 = frozenset([143])
    FOLLOW_RPAREN_in_annotationScopeDeclarations8460 = frozenset([47, 144])
    FOLLOW_annotationDefaultValue_in_annotationScopeDeclarations8462 = frozenset([144])
    FOLLOW_SEMI_in_annotationScopeDeclarations8465 = frozenset([1])
    FOLLOW_classFieldDeclaratorList_in_annotationScopeDeclarations8507 = frozenset([144])
    FOLLOW_SEMI_in_annotationScopeDeclarations8509 = frozenset([1])
    FOLLOW_typeDeclaration_in_annotationScopeDeclarations8554 = frozenset([1])
    FOLLOW_DEFAULT_in_annotationDefaultValue8577 = frozenset([22, 26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_annotationElementValue_in_annotationDefaultValue8580 = frozenset([1])
    FOLLOW_LCURLY_in_block8601 = frozenset([4, 20, 22, 26, 27, 28, 33, 34, 35, 44, 45, 46, 50, 53, 56, 65, 66, 68, 69, 71, 85, 86, 87, 91, 93, 95, 102, 104, 108, 110, 111, 113, 118, 119, 120, 122, 124, 129, 135, 136, 137, 141, 142, 144, 149, 152, 154, 155, 156, 158, 160, 161, 163, 166, 167, 168, 176, 178, 179])
    FOLLOW_blockStatement_in_block8603 = frozenset([4, 20, 22, 26, 27, 28, 33, 34, 35, 44, 45, 46, 50, 53, 56, 65, 66, 68, 69, 71, 85, 86, 87, 91, 93, 95, 102, 104, 108, 110, 111, 113, 118, 119, 120, 122, 124, 129, 135, 136, 137, 141, 142, 144, 149, 152, 154, 155, 156, 158, 160, 161, 163, 166, 167, 168, 176, 178, 179])
    FOLLOW_RCURLY_in_block8606 = frozenset([1])
    FOLLOW_localVariableDeclaration_in_blockStatement8644 = frozenset([144])
    FOLLOW_SEMI_in_blockStatement8646 = frozenset([1])
    FOLLOW_typeDeclaration_in_blockStatement8657 = frozenset([1])
    FOLLOW_statement_in_blockStatement8667 = frozenset([1])
    FOLLOW_localModifierList_in_localVariableDeclaration8690 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_localVariableDeclaration8692 = frozenset([86])
    FOLLOW_classFieldDeclaratorList_in_localVariableDeclaration8694 = frozenset([1])
    FOLLOW_block_in_statement8747 = frozenset([1])
    FOLLOW_ASSERT_in_statement8757 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_statement8761 = frozenset([40, 144])
    FOLLOW_COLON_in_statement8776 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_statement8780 = frozenset([144])
    FOLLOW_SEMI_in_statement8782 = frozenset([1])
    FOLLOW_SEMI_in_statement8845 = frozenset([1])
    FOLLOW_IF_in_statement8934 = frozenset([111])
    FOLLOW_parenthesizedExpression_in_statement8936 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement8940 = frozenset([1, 55])
    FOLLOW_ELSE_in_statement8955 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement8959 = frozenset([1])
    FOLLOW_FOR_in_statement9125 = frozenset([111])
    FOLLOW_LPAREN_in_statement9127 = frozenset([22, 26, 28, 33, 34, 45, 46, 53, 65, 66, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 144, 149, 155, 156, 161, 167, 176])
    FOLLOW_forInit_in_statement9142 = frozenset([144])
    FOLLOW_SEMI_in_statement9144 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 144, 149, 155, 156, 161, 167, 176])
    FOLLOW_forCondition_in_statement9146 = frozenset([144])
    FOLLOW_SEMI_in_statement9148 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 143, 149, 155, 156, 161, 167, 176])
    FOLLOW_forUpdater_in_statement9150 = frozenset([143])
    FOLLOW_RPAREN_in_statement9152 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement9154 = frozenset([1])
    FOLLOW_localModifierList_in_statement9189 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_statement9191 = frozenset([86])
    FOLLOW_IDENT_in_statement9193 = frozenset([40])
    FOLLOW_COLON_in_statement9195 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_statement9197 = frozenset([143])
    FOLLOW_RPAREN_in_statement9199 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement9201 = frozenset([1])
    FOLLOW_WHILE_in_statement9316 = frozenset([111])
    FOLLOW_parenthesizedExpression_in_statement9318 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement9320 = frozenset([1])
    FOLLOW_DO_in_statement9369 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement9371 = frozenset([179])
    FOLLOW_WHILE_in_statement9373 = frozenset([111])
    FOLLOW_parenthesizedExpression_in_statement9375 = frozenset([144])
    FOLLOW_SEMI_in_statement9377 = frozenset([1])
    FOLLOW_TRY_in_statement9418 = frozenset([102])
    FOLLOW_block_in_statement9420 = frozenset([31, 67])
    FOLLOW_catches_in_statement9423 = frozenset([1, 67])
    FOLLOW_finallyClause_in_statement9425 = frozenset([1])
    FOLLOW_finallyClause_in_statement9430 = frozenset([1])
    FOLLOW_SWITCH_in_statement9473 = frozenset([111])
    FOLLOW_parenthesizedExpression_in_statement9475 = frozenset([102])
    FOLLOW_LCURLY_in_statement9477 = frozenset([29, 47])
    FOLLOW_switchBlockLabels_in_statement9479 = frozenset([141])
    FOLLOW_RCURLY_in_statement9481 = frozenset([1])
    FOLLOW_SYNCHRONIZED_in_statement9507 = frozenset([111])
    FOLLOW_parenthesizedExpression_in_statement9509 = frozenset([102])
    FOLLOW_block_in_statement9511 = frozenset([1])
    FOLLOW_RETURN_in_statement9557 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 144, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_statement9559 = frozenset([144])
    FOLLOW_SEMI_in_statement9562 = frozenset([1])
    FOLLOW_THROW_in_statement9626 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_statement9628 = frozenset([144])
    FOLLOW_SEMI_in_statement9630 = frozenset([1])
    FOLLOW_BREAK_in_statement9695 = frozenset([86, 144])
    FOLLOW_IDENT_in_statement9697 = frozenset([144])
    FOLLOW_SEMI_in_statement9700 = frozenset([1])
    FOLLOW_CONTINUE_in_statement9770 = frozenset([86, 144])
    FOLLOW_IDENT_in_statement9772 = frozenset([144])
    FOLLOW_SEMI_in_statement9775 = frozenset([1])
    FOLLOW_IDENT_in_statement9842 = frozenset([40])
    FOLLOW_COLON_in_statement9844 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_statement9846 = frozenset([1])
    FOLLOW_expression_in_statement9913 = frozenset([144])
    FOLLOW_SEMI_in_statement9915 = frozenset([1])
    FOLLOW_SEMI_in_statement9926 = frozenset([1])
    FOLLOW_catchClause_in_catches9965 = frozenset([1, 31])
    FOLLOW_CATCH_in_catchClause10007 = frozenset([111])
    FOLLOW_LPAREN_in_catchClause10010 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 149])
    FOLLOW_formalParameterStandardDecl_in_catchClause10013 = frozenset([143])
    FOLLOW_RPAREN_in_catchClause10015 = frozenset([102])
    FOLLOW_block_in_catchClause10018 = frozenset([1])
    FOLLOW_FINALLY_in_finallyClause10037 = frozenset([102])
    FOLLOW_block_in_finallyClause10039 = frozenset([1])
    FOLLOW_switchCaseLabels_in_switchBlockLabels10071 = frozenset([29, 47])
    FOLLOW_switchDefaultLabel_in_switchBlockLabels10073 = frozenset([29])
    FOLLOW_switchCaseLabels_in_switchBlockLabels10076 = frozenset([1])
    FOLLOW_switchCaseLabel_in_switchCaseLabels10121 = frozenset([1, 29])
    FOLLOW_CASE_in_switchCaseLabel10149 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_switchCaseLabel10152 = frozenset([40])
    FOLLOW_COLON_in_switchCaseLabel10154 = frozenset([1, 4, 20, 22, 26, 27, 28, 33, 34, 35, 44, 45, 46, 50, 53, 56, 65, 66, 68, 69, 71, 85, 86, 87, 91, 93, 95, 102, 104, 108, 110, 111, 113, 118, 119, 120, 122, 124, 129, 135, 136, 137, 142, 144, 149, 152, 154, 155, 156, 158, 160, 161, 163, 166, 167, 168, 176, 178, 179])
    FOLLOW_blockStatement_in_switchCaseLabel10157 = frozenset([1, 4, 20, 22, 26, 27, 28, 33, 34, 35, 44, 45, 46, 50, 53, 56, 65, 66, 68, 69, 71, 85, 86, 87, 91, 93, 95, 102, 104, 108, 110, 111, 113, 118, 119, 120, 122, 124, 129, 135, 136, 137, 142, 144, 149, 152, 154, 155, 156, 158, 160, 161, 163, 166, 167, 168, 176, 178, 179])
    FOLLOW_DEFAULT_in_switchDefaultLabel10181 = frozenset([40])
    FOLLOW_COLON_in_switchDefaultLabel10184 = frozenset([1, 4, 20, 22, 26, 27, 28, 33, 34, 35, 44, 45, 46, 50, 53, 56, 65, 66, 68, 69, 71, 85, 86, 87, 91, 93, 95, 102, 104, 108, 110, 111, 113, 118, 119, 120, 122, 124, 129, 135, 136, 137, 142, 144, 149, 152, 154, 155, 156, 158, 160, 161, 163, 166, 167, 168, 176, 178, 179])
    FOLLOW_blockStatement_in_switchDefaultLabel10187 = frozenset([1, 4, 20, 22, 26, 27, 28, 33, 34, 35, 44, 45, 46, 50, 53, 56, 65, 66, 68, 69, 71, 85, 86, 87, 91, 93, 95, 102, 104, 108, 110, 111, 113, 118, 119, 120, 122, 124, 129, 135, 136, 137, 142, 144, 149, 152, 154, 155, 156, 158, 160, 161, 163, 166, 167, 168, 176, 178, 179])
    FOLLOW_localVariableDeclaration_in_forInit10211 = frozenset([1])
    FOLLOW_expressionList_in_forInit10233 = frozenset([1])
    FOLLOW_expression_in_forCondition10321 = frozenset([1])
    FOLLOW_expressionList_in_forUpdater10363 = frozenset([1])
    FOLLOW_LPAREN_in_parenthesizedExpression10403 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_parenthesizedExpression10405 = frozenset([143])
    FOLLOW_RPAREN_in_parenthesizedExpression10407 = frozenset([1])
    FOLLOW_expression_in_expressionList10448 = frozenset([1, 41])
    FOLLOW_COMMA_in_expressionList10451 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_expressionList10454 = frozenset([1, 41])
    FOLLOW_assignmentExpression_in_expression10475 = frozenset([1])
    FOLLOW_conditionalExpression_in_assignmentExpression10511 = frozenset([1, 6, 21, 24, 49, 114, 117, 126, 130, 146, 148, 151, 182])
    FOLLOW_ASSIGN_in_assignmentExpression10530 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_PLUS_ASSIGN_in_assignmentExpression10549 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_MINUS_ASSIGN_in_assignmentExpression10568 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_STAR_ASSIGN_in_assignmentExpression10587 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_DIV_ASSIGN_in_assignmentExpression10606 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_AND_ASSIGN_in_assignmentExpression10625 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_OR_ASSIGN_in_assignmentExpression10644 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_XOR_ASSIGN_in_assignmentExpression10663 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_MOD_ASSIGN_in_assignmentExpression10682 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_SHIFT_LEFT_ASSIGN_in_assignmentExpression10701 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10720 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_BIT_SHIFT_RIGHT_ASSIGN_in_assignmentExpression10739 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_assignmentExpression_in_assignmentExpression10761 = frozenset([1])
    FOLLOW_logicalOrExpression_in_conditionalExpression10786 = frozenset([1, 139])
    FOLLOW_QUESTION_in_conditionalExpression10789 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_assignmentExpression_in_conditionalExpression10792 = frozenset([40])
    FOLLOW_COLON_in_conditionalExpression10794 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_conditionalExpression_in_conditionalExpression10797 = frozenset([1])
    FOLLOW_logicalAndExpression_in_logicalOrExpression10818 = frozenset([1, 109])
    FOLLOW_LOGICAL_OR_in_logicalOrExpression10821 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_logicalAndExpression_in_logicalOrExpression10824 = frozenset([1, 109])
    FOLLOW_inclusiveOrExpression_in_logicalAndExpression10845 = frozenset([1, 107])
    FOLLOW_LOGICAL_AND_in_logicalAndExpression10848 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_inclusiveOrExpression_in_logicalAndExpression10851 = frozenset([1, 107])
    FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10872 = frozenset([1, 125])
    FOLLOW_OR_in_inclusiveOrExpression10875 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_exclusiveOrExpression_in_inclusiveOrExpression10878 = frozenset([1, 125])
    FOLLOW_andExpression_in_exclusiveOrExpression10899 = frozenset([1, 181])
    FOLLOW_XOR_in_exclusiveOrExpression10902 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_andExpression_in_exclusiveOrExpression10905 = frozenset([1, 181])
    FOLLOW_equalityExpression_in_andExpression10926 = frozenset([1, 5])
    FOLLOW_AND_in_andExpression10929 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_equalityExpression_in_andExpression10932 = frozenset([1, 5])
    FOLLOW_instanceOfExpression_in_equalityExpression10953 = frozenset([1, 58, 121])
    FOLLOW_EQUAL_in_equalityExpression10972 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_NOT_EQUAL_in_equalityExpression10991 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_instanceOfExpression_in_equalityExpression11021 = frozenset([1, 58, 121])
    FOLLOW_relationalExpression_in_instanceOfExpression11051 = frozenset([1, 92])
    FOLLOW_INSTANCEOF_in_instanceOfExpression11054 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_instanceOfExpression11057 = frozenset([1])
    FOLLOW_shiftExpression_in_relationalExpression11078 = frozenset([1, 82, 83, 103, 104])
    FOLLOW_LESS_OR_EQUAL_in_relationalExpression11097 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_GREATER_OR_EQUAL_in_relationalExpression11116 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_LESS_THAN_in_relationalExpression11135 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_GREATER_THAN_in_relationalExpression11154 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_shiftExpression_in_relationalExpression11183 = frozenset([1, 82, 83, 103, 104])
    FOLLOW_additiveExpression_in_shiftExpression11217 = frozenset([1, 23, 145, 147])
    FOLLOW_BIT_SHIFT_RIGHT_in_shiftExpression11235 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_SHIFT_RIGHT_in_shiftExpression11254 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_SHIFT_LEFT_in_shiftExpression11273 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_additiveExpression_in_shiftExpression11302 = frozenset([1, 23, 145, 147])
    FOLLOW_multiplicativeExpression_in_additiveExpression11332 = frozenset([1, 113, 129])
    FOLLOW_PLUS_in_additiveExpression11350 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_MINUS_in_additiveExpression11369 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_multiplicativeExpression_in_additiveExpression11398 = frozenset([1, 113, 129])
    FOLLOW_unaryExpression_in_multiplicativeExpression11428 = frozenset([1, 48, 115, 150])
    FOLLOW_STAR_in_multiplicativeExpression11447 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_DIV_in_multiplicativeExpression11466 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_MOD_in_multiplicativeExpression11485 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_multiplicativeExpression11514 = frozenset([1, 48, 115, 150])
    FOLLOW_PLUS_in_unaryExpression11548 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_unaryExpression11550 = frozenset([1])
    FOLLOW_MINUS_in_unaryExpression11577 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_unaryExpression11579 = frozenset([1])
    FOLLOW_INC_in_unaryExpression11605 = frozenset([26, 28, 33, 34, 46, 53, 65, 68, 69, 85, 86, 93, 104, 110, 111, 119, 122, 124, 149, 155, 156, 161, 167, 176])
    FOLLOW_postfixedExpression_in_unaryExpression11607 = frozenset([1])
    FOLLOW_DEC_in_unaryExpression11631 = frozenset([26, 28, 33, 34, 46, 53, 65, 68, 69, 85, 86, 93, 104, 110, 111, 119, 122, 124, 149, 155, 156, 161, 167, 176])
    FOLLOW_postfixedExpression_in_unaryExpression11633 = frozenset([1])
    FOLLOW_unaryExpressionNotPlusMinus_in_unaryExpression11657 = frozenset([1])
    FOLLOW_NOT_in_unaryExpressionNotPlusMinus11676 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11678 = frozenset([1])
    FOLLOW_LOGICAL_NOT_in_unaryExpressionNotPlusMinus11725 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11727 = frozenset([1])
    FOLLOW_LPAREN_in_unaryExpressionNotPlusMinus11766 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_unaryExpressionNotPlusMinus11768 = frozenset([143])
    FOLLOW_RPAREN_in_unaryExpressionNotPlusMinus11770 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_unaryExpressionNotPlusMinus11772 = frozenset([1])
    FOLLOW_postfixedExpression_in_unaryExpressionNotPlusMinus11807 = frozenset([1])
    FOLLOW_primaryExpression_in_postfixedExpression11843 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_DOT_in_postfixedExpression11905 = frozenset([86, 104, 119, 156, 161])
    FOLLOW_genericTypeArgumentListSimplified_in_postfixedExpression11955 = frozenset([86])
    FOLLOW_IDENT_in_postfixedExpression12037 = frozenset([1, 45, 51, 91, 101, 111])
    FOLLOW_arguments_in_postfixedExpression12116 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_THIS_in_postfixedExpression12190 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_SUPER_in_postfixedExpression12253 = frozenset([111])
    FOLLOW_arguments_in_postfixedExpression12255 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_SUPER_in_postfixedExpression12308 = frozenset([51])
    FOLLOW_DOT_in_postfixedExpression12312 = frozenset([86])
    FOLLOW_IDENT_in_postfixedExpression12314 = frozenset([1, 45, 51, 91, 101, 111])
    FOLLOW_arguments_in_postfixedExpression12381 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_innerNewExpression_in_postfixedExpression12452 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_LBRACK_in_postfixedExpression12509 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_postfixedExpression12511 = frozenset([140])
    FOLLOW_RBRACK_in_postfixedExpression12513 = frozenset([1, 45, 51, 91, 101])
    FOLLOW_INC_in_postfixedExpression12574 = frozenset([1])
    FOLLOW_DEC_in_postfixedExpression12598 = frozenset([1])
    FOLLOW_parenthesizedExpression_in_primaryExpression12646 = frozenset([1])
    FOLLOW_literal_in_primaryExpression12656 = frozenset([1])
    FOLLOW_newExpression_in_primaryExpression12666 = frozenset([1])
    FOLLOW_qualifiedIdentExpression_in_primaryExpression12676 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_primaryExpression12686 = frozenset([86, 156, 161])
    FOLLOW_SUPER_in_primaryExpression12701 = frozenset([51, 111])
    FOLLOW_arguments_in_primaryExpression12719 = frozenset([1])
    FOLLOW_DOT_in_primaryExpression12779 = frozenset([86])
    FOLLOW_IDENT_in_primaryExpression12781 = frozenset([111])
    FOLLOW_arguments_in_primaryExpression12783 = frozenset([1])
    FOLLOW_IDENT_in_primaryExpression12850 = frozenset([111])
    FOLLOW_arguments_in_primaryExpression12852 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression12907 = frozenset([111])
    FOLLOW_arguments_in_primaryExpression12909 = frozenset([1])
    FOLLOW_THIS_in_primaryExpression12974 = frozenset([1, 111])
    FOLLOW_arguments_in_primaryExpression13042 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression13107 = frozenset([111])
    FOLLOW_arguments_in_primaryExpression13109 = frozenset([1])
    FOLLOW_SUPER_in_primaryExpression13165 = frozenset([51])
    FOLLOW_DOT_in_primaryExpression13167 = frozenset([86])
    FOLLOW_IDENT_in_primaryExpression13169 = frozenset([1, 111])
    FOLLOW_arguments_in_primaryExpression13193 = frozenset([1])
    FOLLOW_primitiveType_in_primaryExpression13335 = frozenset([51, 101])
    FOLLOW_arrayDeclarator_in_primaryExpression13394 = frozenset([51, 101])
    FOLLOW_DOT_in_primaryExpression13457 = frozenset([35])
    FOLLOW_CLASS_in_primaryExpression13459 = frozenset([1])
    FOLLOW_VOID_in_primaryExpression13519 = frozenset([51])
    FOLLOW_DOT_in_primaryExpression13521 = frozenset([35])
    FOLLOW_CLASS_in_primaryExpression13523 = frozenset([1])
    FOLLOW_qualifiedIdentifier_in_qualifiedIdentExpression13603 = frozenset([1, 51, 101, 111])
    FOLLOW_arrayDeclarator_in_qualifiedIdentExpression13673 = frozenset([51, 101])
    FOLLOW_DOT_in_qualifiedIdentExpression13741 = frozenset([35])
    FOLLOW_CLASS_in_qualifiedIdentExpression13743 = frozenset([1])
    FOLLOW_arguments_in_qualifiedIdentExpression13813 = frozenset([1])
    FOLLOW_DOT_in_qualifiedIdentExpression13874 = frozenset([35, 104, 119, 156, 161])
    FOLLOW_CLASS_in_qualifiedIdentExpression13892 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_qualifiedIdentExpression13955 = frozenset([86, 156])
    FOLLOW_SUPER_in_qualifiedIdentExpression13980 = frozenset([111])
    FOLLOW_arguments_in_qualifiedIdentExpression13982 = frozenset([1])
    FOLLOW_SUPER_in_qualifiedIdentExpression14032 = frozenset([51])
    FOLLOW_DOT_in_qualifiedIdentExpression14036 = frozenset([86])
    FOLLOW_IDENT_in_qualifiedIdentExpression14038 = frozenset([111])
    FOLLOW_arguments_in_qualifiedIdentExpression14040 = frozenset([1])
    FOLLOW_IDENT_in_qualifiedIdentExpression14090 = frozenset([111])
    FOLLOW_arguments_in_qualifiedIdentExpression14092 = frozenset([1])
    FOLLOW_THIS_in_qualifiedIdentExpression14167 = frozenset([1])
    FOLLOW_SUPER_in_qualifiedIdentExpression14233 = frozenset([111])
    FOLLOW_arguments_in_qualifiedIdentExpression14235 = frozenset([1])
    FOLLOW_innerNewExpression_in_qualifiedIdentExpression14283 = frozenset([1])
    FOLLOW_NEW_in_newExpression14359 = frozenset([26, 28, 33, 53, 68, 86, 93, 104, 110, 149])
    FOLLOW_primitiveType_in_newExpression14375 = frozenset([101])
    FOLLOW_newArrayConstruction_in_newExpression14377 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_newExpression14421 = frozenset([86])
    FOLLOW_qualifiedTypeIdentSimplified_in_newExpression14424 = frozenset([101, 111])
    FOLLOW_newArrayConstruction_in_newExpression14442 = frozenset([1])
    FOLLOW_arguments_in_newExpression14507 = frozenset([1, 102])
    FOLLOW_classBody_in_newExpression14509 = frozenset([1])
    FOLLOW_NEW_in_innerNewExpression14608 = frozenset([86, 104])
    FOLLOW_genericTypeArgumentListSimplified_in_innerNewExpression14610 = frozenset([86])
    FOLLOW_IDENT_in_innerNewExpression14613 = frozenset([111])
    FOLLOW_arguments_in_innerNewExpression14615 = frozenset([1, 102])
    FOLLOW_classBody_in_innerNewExpression14617 = frozenset([1])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction14663 = frozenset([102])
    FOLLOW_arrayInitializer_in_newArrayConstruction14665 = frozenset([1])
    FOLLOW_LBRACK_in_newArrayConstruction14675 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_newArrayConstruction14678 = frozenset([140])
    FOLLOW_RBRACK_in_newArrayConstruction14680 = frozenset([1, 101])
    FOLLOW_LBRACK_in_newArrayConstruction14684 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_newArrayConstruction14687 = frozenset([140])
    FOLLOW_RBRACK_in_newArrayConstruction14689 = frozenset([1, 101])
    FOLLOW_arrayDeclaratorList_in_newArrayConstruction14694 = frozenset([1])
    FOLLOW_LPAREN_in_arguments14714 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 143, 149, 155, 156, 161, 167, 176])
    FOLLOW_expressionList_in_arguments14716 = frozenset([143])
    FOLLOW_RPAREN_in_arguments14719 = frozenset([1])
    FOLLOW_GREATER_THAN_in_synpred14_Java5102 = frozenset([1])
    FOLLOW_SHIFT_RIGHT_in_synpred15_Java5112 = frozenset([1])
    FOLLOW_BIT_SHIFT_RIGHT_in_synpred16_Java5122 = frozenset([1])
    FOLLOW_bound_in_synpred17_Java5152 = frozenset([1])
    FOLLOW_STATIC_in_synpred32_Java5684 = frozenset([102])
    FOLLOW_block_in_synpred32_Java5686 = frozenset([1])
    FOLLOW_genericTypeParameterList_in_synpred42_Java5723 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149, 176])
    FOLLOW_type_in_synpred42_Java5742 = frozenset([86])
    FOLLOW_IDENT_in_synpred42_Java5744 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred42_Java5746 = frozenset([101, 102, 144, 164])
    FOLLOW_arrayDeclaratorList_in_synpred42_Java5748 = frozenset([102, 144, 164])
    FOLLOW_throwsClause_in_synpred42_Java5751 = frozenset([102, 144])
    FOLLOW_block_in_synpred42_Java5755 = frozenset([1])
    FOLLOW_SEMI_in_synpred42_Java5759 = frozenset([1])
    FOLLOW_VOID_in_synpred42_Java5821 = frozenset([86])
    FOLLOW_IDENT_in_synpred42_Java5823 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred42_Java5825 = frozenset([102, 144, 164])
    FOLLOW_throwsClause_in_synpred42_Java5827 = frozenset([102, 144])
    FOLLOW_block_in_synpred42_Java5831 = frozenset([1])
    FOLLOW_SEMI_in_synpred42_Java5835 = frozenset([1])
    FOLLOW_IDENT_in_synpred42_Java5894 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred42_Java5896 = frozenset([102, 164])
    FOLLOW_throwsClause_in_synpred42_Java5898 = frozenset([102])
    FOLLOW_block_in_synpred42_Java5901 = frozenset([1])
    FOLLOW_modifierList_in_synpred43_Java5709 = frozenset([26, 28, 33, 53, 68, 86, 93, 104, 110, 149, 176])
    FOLLOW_genericTypeParameterList_in_synpred43_Java5723 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149, 176])
    FOLLOW_type_in_synpred43_Java5742 = frozenset([86])
    FOLLOW_IDENT_in_synpred43_Java5744 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred43_Java5746 = frozenset([101, 102, 144, 164])
    FOLLOW_arrayDeclaratorList_in_synpred43_Java5748 = frozenset([102, 144, 164])
    FOLLOW_throwsClause_in_synpred43_Java5751 = frozenset([102, 144])
    FOLLOW_block_in_synpred43_Java5755 = frozenset([1])
    FOLLOW_SEMI_in_synpred43_Java5759 = frozenset([1])
    FOLLOW_VOID_in_synpred43_Java5821 = frozenset([86])
    FOLLOW_IDENT_in_synpred43_Java5823 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred43_Java5825 = frozenset([102, 144, 164])
    FOLLOW_throwsClause_in_synpred43_Java5827 = frozenset([102, 144])
    FOLLOW_block_in_synpred43_Java5831 = frozenset([1])
    FOLLOW_SEMI_in_synpred43_Java5835 = frozenset([1])
    FOLLOW_IDENT_in_synpred43_Java5894 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred43_Java5896 = frozenset([102, 164])
    FOLLOW_throwsClause_in_synpred43_Java5898 = frozenset([102])
    FOLLOW_block_in_synpred43_Java5901 = frozenset([1])
    FOLLOW_type_in_synpred43_Java5965 = frozenset([86])
    FOLLOW_classFieldDeclaratorList_in_synpred43_Java5967 = frozenset([144])
    FOLLOW_SEMI_in_synpred43_Java5969 = frozenset([1])
    FOLLOW_typeDeclaration_in_synpred44_Java6014 = frozenset([1])
    FOLLOW_genericTypeParameterList_in_synpred50_Java6070 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149, 176])
    FOLLOW_type_in_synpred50_Java6089 = frozenset([86])
    FOLLOW_IDENT_in_synpred50_Java6091 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred50_Java6093 = frozenset([101, 144, 164])
    FOLLOW_arrayDeclaratorList_in_synpred50_Java6095 = frozenset([144, 164])
    FOLLOW_throwsClause_in_synpred50_Java6098 = frozenset([144])
    FOLLOW_SEMI_in_synpred50_Java6101 = frozenset([1])
    FOLLOW_VOID_in_synpred50_Java6159 = frozenset([86])
    FOLLOW_IDENT_in_synpred50_Java6161 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred50_Java6163 = frozenset([144, 164])
    FOLLOW_throwsClause_in_synpred50_Java6165 = frozenset([144])
    FOLLOW_SEMI_in_synpred50_Java6168 = frozenset([1])
    FOLLOW_modifierList_in_synpred51_Java6056 = frozenset([26, 28, 33, 53, 68, 86, 93, 104, 110, 149, 176])
    FOLLOW_genericTypeParameterList_in_synpred51_Java6070 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149, 176])
    FOLLOW_type_in_synpred51_Java6089 = frozenset([86])
    FOLLOW_IDENT_in_synpred51_Java6091 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred51_Java6093 = frozenset([101, 144, 164])
    FOLLOW_arrayDeclaratorList_in_synpred51_Java6095 = frozenset([144, 164])
    FOLLOW_throwsClause_in_synpred51_Java6098 = frozenset([144])
    FOLLOW_SEMI_in_synpred51_Java6101 = frozenset([1])
    FOLLOW_VOID_in_synpred51_Java6159 = frozenset([86])
    FOLLOW_IDENT_in_synpred51_Java6161 = frozenset([111])
    FOLLOW_formalParameterList_in_synpred51_Java6163 = frozenset([144, 164])
    FOLLOW_throwsClause_in_synpred51_Java6165 = frozenset([144])
    FOLLOW_SEMI_in_synpred51_Java6168 = frozenset([1])
    FOLLOW_type_in_synpred51_Java6231 = frozenset([86])
    FOLLOW_interfaceFieldDeclaratorList_in_synpred51_Java6233 = frozenset([144])
    FOLLOW_SEMI_in_synpred51_Java6235 = frozenset([1])
    FOLLOW_typeDeclaration_in_synpred52_Java6280 = frozenset([1])
    FOLLOW_arrayDeclarator_in_synpred58_Java6582 = frozenset([1])
    FOLLOW_arrayDeclaratorList_in_synpred76_Java6983 = frozenset([1])
    FOLLOW_arrayDeclaratorList_in_synpred77_Java7032 = frozenset([1])
    FOLLOW_DOT_in_synpred79_Java7117 = frozenset([86])
    FOLLOW_typeIdent_in_synpred79_Java7119 = frozenset([1])
    FOLLOW_COMMA_in_synpred90_Java7344 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 139, 149])
    FOLLOW_genericTypeArgument_in_synpred90_Java7346 = frozenset([1])
    FOLLOW_genericWildcardBoundType_in_synpred92_Java7400 = frozenset([1])
    FOLLOW_COMMA_in_synpred97_Java7618 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 149])
    FOLLOW_formalParameterStandardDecl_in_synpred97_Java7620 = frozenset([1])
    FOLLOW_formalParameterStandardDecl_in_synpred99_Java7615 = frozenset([1, 41])
    FOLLOW_COMMA_in_synpred99_Java7618 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 149])
    FOLLOW_formalParameterStandardDecl_in_synpred99_Java7620 = frozenset([1, 41])
    FOLLOW_COMMA_in_synpred99_Java7625 = frozenset([22, 26, 28, 33, 53, 66, 68, 86, 93, 110, 149])
    FOLLOW_formalParameterVarArgDecl_in_synpred99_Java7627 = frozenset([1])
    FOLLOW_formalParameterVarArgDecl_in_synpred100_Java7684 = frozenset([1])
    FOLLOW_DOT_in_synpred101_Java7929 = frozenset([86])
    FOLLOW_IDENT_in_synpred101_Java7933 = frozenset([1])
    FOLLOW_annotation_in_synpred102_Java7986 = frozenset([1])
    FOLLOW_modifierList_in_synpred114_Java8440 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_synpred114_Java8442 = frozenset([86])
    FOLLOW_IDENT_in_synpred114_Java8456 = frozenset([111])
    FOLLOW_LPAREN_in_synpred114_Java8458 = frozenset([143])
    FOLLOW_RPAREN_in_synpred114_Java8460 = frozenset([47, 144])
    FOLLOW_annotationDefaultValue_in_synpred114_Java8462 = frozenset([144])
    FOLLOW_SEMI_in_synpred114_Java8465 = frozenset([1])
    FOLLOW_classFieldDeclaratorList_in_synpred114_Java8507 = frozenset([144])
    FOLLOW_SEMI_in_synpred114_Java8509 = frozenset([1])
    FOLLOW_localVariableDeclaration_in_synpred116_Java8644 = frozenset([144])
    FOLLOW_SEMI_in_synpred116_Java8646 = frozenset([1])
    FOLLOW_typeDeclaration_in_synpred117_Java8657 = frozenset([1])
    FOLLOW_ELSE_in_synpred121_Java8955 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_synpred121_Java8959 = frozenset([1])
    FOLLOW_forInit_in_synpred123_Java9142 = frozenset([144])
    FOLLOW_SEMI_in_synpred123_Java9144 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 144, 149, 155, 156, 161, 167, 176])
    FOLLOW_forCondition_in_synpred123_Java9146 = frozenset([144])
    FOLLOW_SEMI_in_synpred123_Java9148 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 143, 149, 155, 156, 161, 167, 176])
    FOLLOW_forUpdater_in_synpred123_Java9150 = frozenset([143])
    FOLLOW_RPAREN_in_synpred123_Java9152 = frozenset([20, 26, 27, 28, 33, 34, 44, 45, 46, 50, 53, 65, 68, 69, 71, 85, 86, 87, 91, 93, 102, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 142, 144, 149, 155, 156, 158, 160, 161, 163, 167, 168, 176, 179])
    FOLLOW_statement_in_synpred123_Java9154 = frozenset([1])
    FOLLOW_switchCaseLabel_in_synpred143_Java10121 = frozenset([1])
    FOLLOW_localVariableDeclaration_in_synpred146_Java10211 = frozenset([1])
    FOLLOW_expressionList_in_synpred147_Java10233 = frozenset([1])
    FOLLOW_LPAREN_in_synpred190_Java11766 = frozenset([26, 28, 33, 53, 68, 86, 93, 110, 149])
    FOLLOW_type_in_synpred190_Java11768 = frozenset([143])
    FOLLOW_RPAREN_in_synpred190_Java11770 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_unaryExpression_in_synpred190_Java11772 = frozenset([1])
    FOLLOW_arrayDeclarator_in_synpred218_Java13673 = frozenset([51, 101])
    FOLLOW_DOT_in_synpred218_Java13741 = frozenset([35])
    FOLLOW_CLASS_in_synpred218_Java13743 = frozenset([1])
    FOLLOW_DOT_in_synpred226_Java13874 = frozenset([35, 104, 119, 156, 161])
    FOLLOW_CLASS_in_synpred226_Java13892 = frozenset([1])
    FOLLOW_genericTypeArgumentListSimplified_in_synpred226_Java13955 = frozenset([86, 156])
    FOLLOW_SUPER_in_synpred226_Java13980 = frozenset([111])
    FOLLOW_arguments_in_synpred226_Java13982 = frozenset([1])
    FOLLOW_SUPER_in_synpred226_Java14032 = frozenset([51])
    FOLLOW_DOT_in_synpred226_Java14036 = frozenset([86])
    FOLLOW_IDENT_in_synpred226_Java14038 = frozenset([111])
    FOLLOW_arguments_in_synpred226_Java14040 = frozenset([1])
    FOLLOW_IDENT_in_synpred226_Java14090 = frozenset([111])
    FOLLOW_arguments_in_synpred226_Java14092 = frozenset([1])
    FOLLOW_THIS_in_synpred226_Java14167 = frozenset([1])
    FOLLOW_SUPER_in_synpred226_Java14233 = frozenset([111])
    FOLLOW_arguments_in_synpred226_Java14235 = frozenset([1])
    FOLLOW_innerNewExpression_in_synpred226_Java14283 = frozenset([1])
    FOLLOW_LBRACK_in_synpred234_Java14684 = frozenset([26, 28, 33, 34, 45, 46, 53, 65, 68, 69, 85, 86, 91, 93, 104, 108, 110, 111, 113, 119, 120, 122, 124, 129, 149, 155, 156, 161, 167, 176])
    FOLLOW_expression_in_synpred234_Java14687 = frozenset([140])
    FOLLOW_RBRACK_in_synpred234_Java14689 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("JavaLexer", JavaParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
