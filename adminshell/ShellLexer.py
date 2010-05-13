# $ANTLR 3.0.1 Shell.antlr3 2010-05-11 21:17:00

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
HEX_8BIT=14
EXPONENT=6
WS=15
ESC_SEQ=8
BYTE_ESC=11
UNICODE_ESC=12
LONG_UNICODE_ESC=13
HEX_DIGIT=10
INT=5
FLOAT=7
ID=4
Tokens=16
EOF=-1
STRING=9

class ShellLexer(Lexer):

    grammarFileName = "Shell.antlr3"

    def __init__(self, input=None):
        Lexer.__init__(self, input)
        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )
        self.dfa21 = self.DFA21(
            self, 21,
            eot = self.DFA21_eot,
            eof = self.DFA21_eof,
            min = self.DFA21_min,
            max = self.DFA21_max,
            accept = self.DFA21_accept,
            special = self.DFA21_special,
            transition = self.DFA21_transition
            )






    # $ANTLR start ID
    def mID(self, ):

        try:
            self.type = ID

            # Shell.antlr3:18:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # Shell.antlr3:18:9: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            if (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # Shell.antlr3:18:33: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((u'0' <= LA1_0 <= u'9') or (u'A' <= LA1_0 <= u'Z') or LA1_0 == u'_' or (u'a' <= LA1_0 <= u'z')) :
                    alt1 = 1


                if alt1 == 1:
                    # Shell.antlr3:
                    if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1






        finally:

            pass

    # $ANTLR end ID



    # $ANTLR start INT
    def mINT(self, ):

        try:
            self.type = INT

            # Shell.antlr3:21:5: ( ( '0' .. '9' )+ )
            # Shell.antlr3:21:9: ( '0' .. '9' )+
            # Shell.antlr3:21:9: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((u'0' <= LA2_0 <= u'9')) :
                    alt2 = 1


                if alt2 == 1:
                    # Shell.antlr3:21:9: '0' .. '9'
                    self.matchRange(u'0', u'9')



                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1






        finally:

            pass

    # $ANTLR end INT



    # $ANTLR start FLOAT
    def mFLOAT(self, ):

        try:
            self.type = FLOAT

            # Shell.antlr3:25:5: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            alt9 = 3
            alt9 = self.dfa9.predict(self.input)
            if alt9 == 1:
                # Shell.antlr3:25:9: ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
                # Shell.antlr3:25:9: ( '0' .. '9' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((u'0' <= LA3_0 <= u'9')) :
                        alt3 = 1


                    if alt3 == 1:
                        # Shell.antlr3:25:10: '0' .. '9'
                        self.matchRange(u'0', u'9')



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(u'.')

                # Shell.antlr3:25:25: ( '0' .. '9' )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((u'0' <= LA4_0 <= u'9')) :
                        alt4 = 1


                    if alt4 == 1:
                        # Shell.antlr3:25:26: '0' .. '9'
                        self.matchRange(u'0', u'9')



                    else:
                        break #loop4


                # Shell.antlr3:25:37: ( EXPONENT )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == u'E' or LA5_0 == u'e') :
                    alt5 = 1
                if alt5 == 1:
                    # Shell.antlr3:25:37: EXPONENT
                    self.mEXPONENT()






            elif alt9 == 2:
                # Shell.antlr3:26:9: '.' ( '0' .. '9' )+ ( EXPONENT )?
                self.match(u'.')

                # Shell.antlr3:26:13: ( '0' .. '9' )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((u'0' <= LA6_0 <= u'9')) :
                        alt6 = 1


                    if alt6 == 1:
                        # Shell.antlr3:26:14: '0' .. '9'
                        self.matchRange(u'0', u'9')



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                # Shell.antlr3:26:25: ( EXPONENT )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == u'E' or LA7_0 == u'e') :
                    alt7 = 1
                if alt7 == 1:
                    # Shell.antlr3:26:25: EXPONENT
                    self.mEXPONENT()






            elif alt9 == 3:
                # Shell.antlr3:27:9: ( '0' .. '9' )+ EXPONENT
                # Shell.antlr3:27:9: ( '0' .. '9' )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((u'0' <= LA8_0 <= u'9')) :
                        alt8 = 1


                    if alt8 == 1:
                        # Shell.antlr3:27:10: '0' .. '9'
                        self.matchRange(u'0', u'9')



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.mEXPONENT()




        finally:

            pass

    # $ANTLR end FLOAT



    # $ANTLR start STRING
    def mSTRING(self, ):

        try:
            self.type = STRING

            # Shell.antlr3:31:5: ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' | '\\'' ( ESC_SEQ | ~ ( '\\\\' | '\\'' ) )* '\\'' )
            alt12 = 2
            LA12_0 = self.input.LA(1)

            if (LA12_0 == u'"') :
                alt12 = 1
            elif (LA12_0 == u'\'') :
                alt12 = 2
            else:
                nvae = NoViableAltException("30:1: STRING : ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' | '\\'' ( ESC_SEQ | ~ ( '\\\\' | '\\'' ) )* '\\'' );", 12, 0, self.input)

                raise nvae

            if alt12 == 1:
                # Shell.antlr3:31:8: '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"'
                self.match(u'"')

                # Shell.antlr3:31:12: ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )*
                while True: #loop10
                    alt10 = 3
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == u'\\') :
                        alt10 = 1
                    elif ((u'\u0000' <= LA10_0 <= u'!') or (u'#' <= LA10_0 <= u'[') or (u']' <= LA10_0 <= u'\uFFFE')) :
                        alt10 = 2


                    if alt10 == 1:
                        # Shell.antlr3:31:14: ESC_SEQ
                        self.mESC_SEQ()



                    elif alt10 == 2:
                        # Shell.antlr3:31:24: ~ ( '\\\\' | '\"' )
                        if (u'\u0000' <= self.input.LA(1) <= u'!') or (u'#' <= self.input.LA(1) <= u'[') or (u']' <= self.input.LA(1) <= u'\uFFFE'):
                            self.input.consume();

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop10


                self.match(u'"')



            elif alt12 == 2:
                # Shell.antlr3:32:8: '\\'' ( ESC_SEQ | ~ ( '\\\\' | '\\'' ) )* '\\''
                self.match(u'\'')

                # Shell.antlr3:32:13: ( ESC_SEQ | ~ ( '\\\\' | '\\'' ) )*
                while True: #loop11
                    alt11 = 3
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == u'\\') :
                        alt11 = 1
                    elif ((u'\u0000' <= LA11_0 <= u'&') or (u'(' <= LA11_0 <= u'[') or (u']' <= LA11_0 <= u'\uFFFE')) :
                        alt11 = 2


                    if alt11 == 1:
                        # Shell.antlr3:32:15: ESC_SEQ
                        self.mESC_SEQ()



                    elif alt11 == 2:
                        # Shell.antlr3:32:25: ~ ( '\\\\' | '\\'' )
                        if (u'\u0000' <= self.input.LA(1) <= u'&') or (u'(' <= self.input.LA(1) <= u'[') or (u']' <= self.input.LA(1) <= u'\uFFFE'):
                            self.input.consume();

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop11


                self.match(u'\'')




        finally:

            pass

    # $ANTLR end STRING



    # $ANTLR start EXPONENT
    def mEXPONENT(self, ):

        try:
            # Shell.antlr3:36:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # Shell.antlr3:36:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            if self.input.LA(1) == u'E' or self.input.LA(1) == u'e':
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # Shell.antlr3:36:22: ( '+' | '-' )?
            alt13 = 2
            LA13_0 = self.input.LA(1)

            if (LA13_0 == u'+' or LA13_0 == u'-') :
                alt13 = 1
            if alt13 == 1:
                # Shell.antlr3:
                if self.input.LA(1) == u'+' or self.input.LA(1) == u'-':
                    self.input.consume();

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





            # Shell.antlr3:36:33: ( '0' .. '9' )+
            cnt14 = 0
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((u'0' <= LA14_0 <= u'9')) :
                    alt14 = 1


                if alt14 == 1:
                    # Shell.antlr3:36:34: '0' .. '9'
                    self.matchRange(u'0', u'9')



                else:
                    if cnt14 >= 1:
                        break #loop14

                    eee = EarlyExitException(14, self.input)
                    raise eee

                cnt14 += 1






        finally:

            pass

    # $ANTLR end EXPONENT



    # $ANTLR start HEX_DIGIT
    def mHEX_DIGIT(self, ):

        try:
            # Shell.antlr3:39:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # Shell.antlr3:39:13: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'F') or (u'a' <= self.input.LA(1) <= u'f'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end HEX_DIGIT



    # $ANTLR start ESC_SEQ
    def mESC_SEQ(self, ):

        try:
            # Shell.antlr3:43:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | BYTE_ESC | UNICODE_ESC | LONG_UNICODE_ESC )
            alt15 = 4
            LA15_0 = self.input.LA(1)

            if (LA15_0 == u'\\') :
                LA15 = self.input.LA(2)
                if LA15 == u'U':
                    alt15 = 4
                elif LA15 == u'"' or LA15 == u'\'' or LA15 == u'\\' or LA15 == u'b' or LA15 == u'f' or LA15 == u'n' or LA15 == u'r' or LA15 == u't':
                    alt15 = 1
                elif LA15 == u'x':
                    alt15 = 2
                elif LA15 == u'u':
                    alt15 = 3
                else:
                    nvae = NoViableAltException("41:1: fragment ESC_SEQ : ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | BYTE_ESC | UNICODE_ESC | LONG_UNICODE_ESC );", 15, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("41:1: fragment ESC_SEQ : ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | BYTE_ESC | UNICODE_ESC | LONG_UNICODE_ESC );", 15, 0, self.input)

                raise nvae

            if alt15 == 1:
                # Shell.antlr3:43:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                self.match(u'\\')

                if self.input.LA(1) == u'"' or self.input.LA(1) == u'\'' or self.input.LA(1) == u'\\' or self.input.LA(1) == u'b' or self.input.LA(1) == u'f' or self.input.LA(1) == u'n' or self.input.LA(1) == u'r' or self.input.LA(1) == u't':
                    self.input.consume();

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt15 == 2:
                # Shell.antlr3:44:9: BYTE_ESC
                self.mBYTE_ESC()



            elif alt15 == 3:
                # Shell.antlr3:45:9: UNICODE_ESC
                self.mUNICODE_ESC()



            elif alt15 == 4:
                # Shell.antlr3:46:9: LONG_UNICODE_ESC
                self.mLONG_UNICODE_ESC()




        finally:

            pass

    # $ANTLR end ESC_SEQ



    # $ANTLR start HEX_8BIT
    def mHEX_8BIT(self, ):

        try:
            # Shell.antlr3:51:5: ( HEX_DIGIT HEX_DIGIT )
            # Shell.antlr3:51:9: HEX_DIGIT HEX_DIGIT
            self.mHEX_DIGIT()

            self.mHEX_DIGIT()





        finally:

            pass

    # $ANTLR end HEX_8BIT



    # $ANTLR start BYTE_ESC
    def mBYTE_ESC(self, ):

        try:
            # Shell.antlr3:56:5: ( '\\\\' 'x' HEX_8BIT )
            # Shell.antlr3:56:9: '\\\\' 'x' HEX_8BIT
            self.match(u'\\')

            self.match(u'x')

            self.mHEX_8BIT()





        finally:

            pass

    # $ANTLR end BYTE_ESC



    # $ANTLR start UNICODE_ESC
    def mUNICODE_ESC(self, ):

        try:
            # Shell.antlr3:61:5: ( '\\\\' 'u' HEX_8BIT HEX_8BIT )
            # Shell.antlr3:61:9: '\\\\' 'u' HEX_8BIT HEX_8BIT
            self.match(u'\\')

            self.match(u'u')

            self.mHEX_8BIT()

            self.mHEX_8BIT()





        finally:

            pass

    # $ANTLR end UNICODE_ESC



    # $ANTLR start LONG_UNICODE_ESC
    def mLONG_UNICODE_ESC(self, ):

        try:
            # Shell.antlr3:66:5: ( '\\\\' 'U' HEX_8BIT HEX_8BIT HEX_8BIT HEX_8BIT )
            # Shell.antlr3:66:9: '\\\\' 'U' HEX_8BIT HEX_8BIT HEX_8BIT HEX_8BIT
            self.match(u'\\')

            self.match(u'U')

            self.mHEX_8BIT()

            self.mHEX_8BIT()

            self.mHEX_8BIT()

            self.mHEX_8BIT()





        finally:

            pass

    # $ANTLR end LONG_UNICODE_ESC



    # $ANTLR start WS
    def mWS(self, ):

        try:
            self.type = WS

            # Shell.antlr3:69:5: ( ( ( ' ' )+ | ( '\\t' )+ | ( '\\r' )+ | ( '\\n' )+ ) )
            # Shell.antlr3:69:9: ( ( ' ' )+ | ( '\\t' )+ | ( '\\r' )+ | ( '\\n' )+ )
            # Shell.antlr3:69:9: ( ( ' ' )+ | ( '\\t' )+ | ( '\\r' )+ | ( '\\n' )+ )
            alt20 = 4
            LA20 = self.input.LA(1)
            if LA20 == u' ':
                alt20 = 1
            elif LA20 == u'\t':
                alt20 = 2
            elif LA20 == u'\r':
                alt20 = 3
            elif LA20 == u'\n':
                alt20 = 4
            else:
                nvae = NoViableAltException("69:9: ( ( ' ' )+ | ( '\\t' )+ | ( '\\r' )+ | ( '\\n' )+ )", 20, 0, self.input)

                raise nvae

            if alt20 == 1:
                # Shell.antlr3:69:11: ( ' ' )+
                # Shell.antlr3:69:11: ( ' ' )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == u' ') :
                        alt16 = 1


                    if alt16 == 1:
                        # Shell.antlr3:69:11: ' '
                        self.match(u' ')



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1




            elif alt20 == 2:
                # Shell.antlr3:70:11: ( '\\t' )+
                # Shell.antlr3:70:11: ( '\\t' )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == u'\t') :
                        alt17 = 1


                    if alt17 == 1:
                        # Shell.antlr3:70:11: '\\t'
                        self.match(u'\t')



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1




            elif alt20 == 3:
                # Shell.antlr3:71:11: ( '\\r' )+
                # Shell.antlr3:71:11: ( '\\r' )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == u'\r') :
                        alt18 = 1


                    if alt18 == 1:
                        # Shell.antlr3:71:11: '\\r'
                        self.match(u'\r')



                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1




            elif alt20 == 4:
                # Shell.antlr3:72:11: ( '\\n' )+
                # Shell.antlr3:72:11: ( '\\n' )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == u'\n') :
                        alt19 = 1


                    if alt19 == 1:
                        # Shell.antlr3:72:11: '\\n'
                        self.match(u'\n')



                    else:
                        if cnt19 >= 1:
                            break #loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1





            #action start
            self.channel=HIDDEN;
            #action end




        finally:

            pass

    # $ANTLR end WS



    def mTokens(self):
        # Shell.antlr3:1:8: ( ID | INT | FLOAT | STRING | WS )
        alt21 = 5
        alt21 = self.dfa21.predict(self.input)
        if alt21 == 1:
            # Shell.antlr3:1:10: ID
            self.mID()



        elif alt21 == 2:
            # Shell.antlr3:1:13: INT
            self.mINT()



        elif alt21 == 3:
            # Shell.antlr3:1:17: FLOAT
            self.mFLOAT()



        elif alt21 == 4:
            # Shell.antlr3:1:23: STRING
            self.mSTRING()



        elif alt21 == 5:
            # Shell.antlr3:1:30: WS
            self.mWS()








    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\3"
        )

    DFA9_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    DFA9 = DFA
    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\2\uffff\1\6\4\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\1\11\1\uffff\1\56\4\uffff"
        )

    DFA21_max = DFA.unpack(
        u"\1\172\1\uffff\1\145\4\uffff"
        )

    DFA21_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\1\4\1\5\1\2"
        )

    DFA21_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA21_transition = [
        DFA.unpack(u"\2\5\2\uffff\1\5\22\uffff\1\5\1\uffff\1\4\4\uffff\1"
        u"\4\6\uffff\1\3\1\uffff\12\2\7\uffff\32\1\4\uffff\1\1\1\uffff\32"
        u"\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\12\2\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #21

    DFA21 = DFA
 

